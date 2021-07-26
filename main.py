import glob
import hashlib
import re

ENABLE_DEBUG = False


def gen_hash(in_txt: str, salt: str) -> bytes:
    b_txt = bytes(salt + in_txt, "utf-8")
    m = hashlib.sha256(b_txt)
    return m.digest()[0]


def gen_hash_wrapper(k: int, in_txt: str):
    for i in range(k):
        yield gen_hash(in_txt, str(i))


def calc_bfindex(word: str) -> int:
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
    if ENABLE_DEBUG:
        print("Bfindex::bits =", bin(bfindex)[2:].zfill(64))
    return bfindex


def get_words(filename: str) -> list:
    with open(filename) as f:
        # 空白/改行で分割
        _words = re.split(r"[\n ]", f.read())
        # 空要素の削除
        words = list(filter(None, _words))
    return words


def search_bfindex(bfindex_table: list, target_bfindex: int) -> int:
    for i, _bf in enumerate(bfindex_table):
        if _bf == target_bfindex:
            return i
    return -1


def main():
    print("# step.1 - ファイルからキーワードの登録")
    input_files = glob.glob("input_files/*")
    file_table = {}

    for in_file in input_files:
        print(f"File = {in_file}")
        bfindex_table = []
        word_table = []

        for word in get_words(in_file):
            bf = calc_bfindex(word)
            if ENABLE_DEBUG:
                print(f"Word = {word}")
                print(f"Bfindex = {bf}")
            bfindex_table.append(bf)
            word_table.append(word)

        file_table[in_file] = {
            "bfindex": bfindex_table,
            "word": word_table,
        }

    """
    # 重複の数え上げ
    for i,i_bft in enumerate(bfindex_table):
        for j,j_bft in enumerate(bfindex_table):
            if i >= j:
                continue
            elif i_bft == j_bft:
                print(word_table[i], "==", word_table[j])
    """

    print()
    print("# step.2 - キーワード入力による検索")
    search_word = input("[Search Keyword | END]> ")
    if search_word == "END":
        return

    target_bfindex = calc_bfindex(search_word)
    for fname, body in file_table.items():
        res = search_bfindex(body["bfindex"], target_bfindex)
        # print(target_bfindex in body["bfindex"])
        if res >= 0:  # match
            print("Positive in", fname)
            print("\t", body["word"][res], "==", search_word)
            """
            if body["word"][res] == search_word:  # true-positive
                print("TP Found::", search_word)
            else:  # false-positive
                print("FP Found::", search_word)
            """
        else:  # unmatch
            print("Negative in", fname)


if __name__ == "__main__":
    main()
