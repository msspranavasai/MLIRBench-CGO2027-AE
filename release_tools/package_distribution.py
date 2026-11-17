#!/usr/bin/env python3
"""Deterministic outer archive; scientific implementation is not changed."""
import argparse
import gzip
import hashlib
import tarfile
from pathlib import Path

def sha(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''): h.update(b)
    return h.hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--root',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--timestamp',type=int,required=True)
    a=ap.parse_args(); root=a.root.resolve(); output=a.output.resolve()
    if output.is_relative_to(root): ap.error('Outer archive must be outside distribution root')
    if output.exists(): ap.error('Refusing to overwrite an existing archive')
    if not (root/'docker/mlirbench-ae-v0.3.0rc5-image.tar').is_file(): ap.error('Required Docker export missing')
    files=sorted(p for p in root.rglob('*') if p.is_file())
    if any(p.is_symlink() for p in root.rglob('*')): ap.error('Symlinks must be reviewed before packaging')
    forbidden={'.git','__pycache__','.venv','.pytest_cache','.DS_Store'}
    if any(any(part in forbidden for part in p.relative_to(root).parts) for p in files): ap.error('Development files found')
    manifest=root/'MANIFEST.sha256'
    manifest.write_text(''.join(sha(p)+'  '+p.relative_to(root).as_posix()+'\n' for p in files if p!=manifest))
    files=sorted(p for p in root.rglob('*') if p.is_file())
    output.parent.mkdir(parents=True,exist_ok=True)
    with output.open('xb') as f, gzip.GzipFile(filename='',mode='wb',fileobj=f,mtime=0,compresslevel=6) as gz:
        with tarfile.open(fileobj=gz,mode='w|',format=tarfile.PAX_FORMAT) as tf:
            for p in files:
                info=tf.gettarinfo(str(p),arcname=root.name+'/'+p.relative_to(root).as_posix())
                info.uid=info.gid=0; info.uname=info.gname='';info.mtime=a.timestamp
                info.mode=0o755 if p.stat().st_mode & 0o111 else 0o644
                info.pax_headers={}
                with p.open('rb') as stream: tf.addfile(info,stream)
    checksum=sha(output)
    output.with_name(output.name+'.sha256').write_text(checksum+'  '+output.name+'\n')
    print(str(output)+' '+str(output.stat().st_size)+' bytes SHA256 '+checksum)

if __name__=='__main__':main()
