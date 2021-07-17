import hashlib

def gen_hash(in_txt: str, salt: str) -> bytes:
    b_txt = bytes(salt + in_txt, 'utf-8')
    m = hashlib.sha256(b_txt)
    return m.digest()[0]

def calc(k: int, in_txt: str):
    for i in range(k):
        yield gen_hash(in_txt, str(i))

def main():
    bfindex = 0  # long
    m = 64
    k = 3
    for c in calc(k, "hello"):
        fit_hash = c % m
        invol = 2 ** fit_hash
        print(invol)
        bfindex = bfindex | invol
        # print("p =", p, "fit_hash =", fit_hash)
        # print("invol =", invol, "bfindex =", bfindex)
        print(bin(bfindex)[2:].zfill(64))


if __name__ == "__main__":
    main()
