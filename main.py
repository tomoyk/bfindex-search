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


def calc_bfindex(word) -> int:
    m = 64  # N[bit]
    bfindex = 0  # long
    k = 3
    for c in gen_hash_wrapper(k, word):
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
    bfindex_table = {}
    for in_file in input_files:
        print(f"File = {in_file}")
        for word in get_words(in_file):
            print(f"Word = {word}")
            bf = calc_bfindex(word)
            print(f"Bfindex = {bf}")
            bfindex_table[bf] = in_file
    
    print("# step.2 - キーワード入力による検索")
    search_word = input("Word >")
    search_bindex = calc_bfindex(search_word)
    print(bfindex_table.get(search_bindex, "Not Found"))
    

if __name__ == "__main__":
    main()
