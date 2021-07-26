import glob
import hashlib


def gen_hash(in_txt: str, salt: str) -> bytes:
    b_txt = bytes(salt + in_txt, 'utf-8')
    m = hashlib.sha256(b_txt)
    return m.digest()[0]


def calc(k: int, in_txt: str):
    for i in range(k):
        yield gen_hash(in_txt, str(i))


def calc_wrap(filename: str):
    m = 64  # N[bit]
    bfindex = 0  # long
    k = 3

    with open(filename) as f:
        file_content = f.read()

    for c in calc(k, file_content):
        fit_hash = c % m
        invol = 2 ** fit_hash
        print(invol)
        bfindex = bfindex | invol
        # print("p =", p, "fit_hash =", fit_hash)
        # print("invol =", invol, "bfindex =", bfindex)
        print(bin(bfindex)[2:].zfill(64))


def main():
    input_files = glob.glob("input_files/*")
    for in_file in input_files:
        calc_wrap(in_file)


if __name__ == "__main__":
    main()
