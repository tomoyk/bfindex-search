# bfindex-search

bfindexを用いた検索システム

[レポートの概要](report.md)

## 環境

- Python 3.9.5
- macOS Big Sur 11.2.3

## 使い方

事前に `input_files/` にテキストファイルを格納する．

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