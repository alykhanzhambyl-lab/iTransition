from pathlib import Path
import hashlib

dir = Path("input")
h = dir / "file_00.data"
h = hashlib.sha3_256(h.read_bytes()).hexdigest()
print(f'hash = {h}')
d: int = 0
# for i in h:
#     i = int(i, base=16)
#     d += i
d = 0

print(f'number version = {d}')

# for f in dir.iterdir():
#     h = hashlib.sha3_256(f.read_bytes()).hexdigest()
#     key = []
#     for i in h:
#         i = int(i, base=16)
#         i += 1
    
# for h in dir.iterdir():
#     h = hashlib.sha3_256(h.read_bytes()).hexdigest()
#     print(h)
