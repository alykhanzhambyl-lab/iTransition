import hashlib
# sh = hashlib.new('sha3_256')
# sh.update(b'Something that supposed to be hashed')
# print(sh.hexdigest())

def debug_print(**kwargs):
    for name, value in kwargs.items():
        print(f"{name}: {value}")

sh = hashlib.sha3_256(b"Something that supposed to be hashed", usedforsecurity= False)
dgst = sh.hexdigest()
bt_digest = sh.digest()
size = sh.digest_size
nm = sh.name

debug_print(
    dgst=dgst,
    bt_digest=bt_digest,
    size=size,
    nm = nm
)
