from pathlib import Path
import hashlib

dir = Path("input")
hashes = []

for f in dir.iterdir():
    h = hashlib.sha3_256(f.read_bytes()).hexdigest()
    k = 1
    for i in h:
        k *= (int(i, 16) + 1)
    hashes.append((k,h))
    

for i in hashes:
    print(i)
    

# h = dir / "file_00.data"
# h = hashlib.sha3_256(h.read_bytes()).hexdigest()
# print(f'hash = {h}')
# k = 1
# for i in h:
#     k *= (int(i, 16) + 1)
    
# print(f'sorting key = {k}')
# for h in dir.iterdir():
#     h = hashlib.sha3_256(h.read_bytes()).hexdigest()
#     print(h)
# print(f'hash = {h}')
    # print(f'sorting key = {k}')