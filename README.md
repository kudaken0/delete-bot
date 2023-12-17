# delete-bot(メッセージ削除bot)

# 仕様
![sample](https://github.com/kudaken0/delete-bot/blob/main/images/demo.gif)  
当リポジトリで公開しているコードは最初のメッセージを無視してそれ以降のメッセージを削除するようにしています。
なぜそうしているかと言うと、最初のメッセージを無視しないと、bot自身(メッセージを削除中..)のメッセージも削除してしまうからです。
そして、まだ開発段階のため不備が少しあります。
不備がございましたらメール(contact@kudaken.com)かdiscord(kudaken)のDMに送ってください。
# 初期設定
※Pythonをインストールしている前提で説明します。
## discord.pyをインストール
まず以下のコマンドを実行してdiscord.pyをインストールしてください。
```pip install discord.py```
これでdiscord.pyのインストールが完了しました。
## botアカウント作成
[こちら](https://discordpy.readthedocs.io/ja/latest/discord.html)の記事をご参照ください。
