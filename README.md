# bfindex-search

bfindexを用いた検索システム

[レポートの概要](report.md)

## 環境

- Python 3.9.5
- macOS Big Sur 11.2.3

## 使い方

事前に `input_files/` にテキストファイルを格納する．

サンプルデータセットは以下で作った．

```
seq 1 100 | sed "s/^/katakura/g" > katakura
```

`main.py`を実行する．

```
python main.py
```

検索したいキーワードを入力する．

```
# step.2 -キーワード入力による検索
[Search Keyword | END]> security
```

## false positiveの例

```
> python main.py
# step.1 -ファイルからキーワードの登録
File = input_files/hello1000
File = input_files/world
File = input_files/hello

# step.2 -キーワード入力による検索
[Search Keyword | END]> hello620
Positive in input_files/hello1000
	 hello165 == hello620
Negative in input_files/world
Negative in input_files/hello

> python main.py
# step.1 -ファイルからキーワードの登録
File = input_files/hello1000
File = input_files/world
File = input_files/hello

# step.2 -キーワード入力による検索
[Search Keyword | END]> hello165
Positive in input_files/hello1000
	 hello165 == hello165
Negative in input_files/world
Negative in input_files/hello
```

動作例2

```
$ python main.py
# step.1 -ファイルからキーワードの登録
File = input_files/minamino
File = input_files/koukadai
File = input_files/hachioji
File = input_files/security
File = input_files/hello1000
File = input_files/world
File = input_files/cloud
File = input_files/katakura
File = input_files/report
File = input_files/hello

# step.2 -キーワード入力による検索
[Search Keyword | END]> hello620
Negative in input_files/minamino
Negative in input_files/koukadai
Negative in input_files/hachioji
Negative in input_files/security
Positive in input_files/hello1000
	 hello165 == hello620
Negative in input_files/world
Negative in input_files/cloud
Negative in input_files/katakura
Negative in input_files/report
Negative in input_files/hello
```
