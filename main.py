import glob
import hashlib
import re


def gen_hash(in_txt: str, salt: str) -> bytes:
    b_txt = bytes(salt + in_txt, 'utf-8')
    m = hashlib.sha256(b_txt)
    return m.digest()[0]


def gen_hash_wrapper(k: int, in_txt: str):
    for i in range(k):
        yield gen_hash(in_txt, str(i))


def calc_bfindex(words: list) -> int:
    m = 64  # N[bit]
    bfindex = 0  # long
    k = 3
    for c in gen_hash_wrapper(k, words):
        fit_hash = c % m
        invol = 2 ** fit_hash
        # print(invol)
        bfindex = bfindex | invol
        # print("p =", p, "fit_hash =", fit_hash)
        # print("invol =", invol, "bfindex =", bfindex)
    print("Bfindex::bits =", bin(bfindex)[2:].zfill(64))
    return bfindex


def get_words(filename: str) -> list:
    with open(filename) as f:
        # 空白/改行で分割
        _words = re.split(r"[\n ]", f.read())
        # 空要素の削除
        words = list(filter(None, _words))
    return words

def main():
    print("# step.1 - ファイルからキーワードの登録")
    input_files = glob.glob("input_files/*")
    for in_file in input_files:
        print(f"File = {in_file}")
        for word in get_words(in_file):
            print(f"Word = {word}")
            bf = calc_bfindex(word)
            print(f"Bfindex = {bf}")

if __name__ == "__main__":
    main()
