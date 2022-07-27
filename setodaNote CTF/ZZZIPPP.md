# ZZZIPPP

あなたはあるファイルの解析作業を依頼されました。何重にも入れ子になった箱のようなファイルのようで、その中に組織にとって重要な機密情報が入っているようです。

添付されたファイルを解析してフラグを入手してください。

## Solution

初めに解いたときは

```txt
unzip flag1000.zip
unzip flag999.zip
unzip flag998.zip
(以下略)
unzip flag1.zip
```

みたいな文字列を用意してシェルに投げた．

さすがに雑すぎたので調べた．pythonは便利だねぇ．

```python
import os
import zipfile

for i in range (1000, 0, -1):
    filename = "flag" + str(i) + ".zip"
    with zipfile.ZipFile(filename, "r") as zp:
        zp.extractall()
    os.remove(filename)
```

``flag{loop-zip-1989-zip-loop}``
