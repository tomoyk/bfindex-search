import hashlib

def gen_hash(in_txt: str, salt: str):
    b_txt = bytes(salt + in_txt, 'utf-8')
    m = hashlib.sha256(b_txt)
    return m.digest()[0]

def calc(k, in_txt):
    for i in range(k):
        yield gen_hash(in_txt, str(i))

def bfindex():
    _bfindex = 0
    m = 64
    k = 3
    for p in calc(k, "hello"):
        print(p % m)

def main():
    bfindex()

if __name__ == "__main__":
    main()
