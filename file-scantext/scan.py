import sys
from pathlib import Path
from datetime import datetime as DateTime

fname = sys.argv[1]
ftype = sys.argv[2]


path = Path(fname)


pattern = '*' + ftype

list_file = list(path.glob(pattern))

for p in list_file :
    dt = DateTime.fromtimestamp(p.stat().st_mtime)
    full_name = p.resolve()
    
    taille = p.stat().st_size
    print(taille, str(full_name), f'date = {dt}')
    with open(p.name) as f:
        print(f.readline())