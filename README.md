# メッセージ削除bot
# 目次
- [delete-bot(メッセージ削除bot)](#delete-bot%E3%83%A1%E3%83%83%E3%82%BB%E3%83%BC%E3%82%B8%E5%89%8A%E9%99%A4bot)
- [仕様](#%E4%BB%95%E6%A7%98)
- [初期設定](#%E5%88%9D%E6%9C%9F%E8%A8%AD%E5%AE%9A)
  - [discord.pyをインストール](#discordpy%E3%82%92%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB)
  - [botアカウント作成](#bot%E3%82%A2%E3%82%AB%E3%82%A6%E3%83%B3%E3%83%88%E4%BD%9C%E6%88%90)
  - [botに必要な権限](#bot%E3%81%AB%E5%BF%85%E8%A6%81%E3%81%AA%E6%A8%A9%E9%99%90)
- [アップデート履歴](#%E3%82%A2%E3%83%83%E3%83%97%E3%83%87%E3%83%BC%E3%83%88%E5%B1%A5%E6%AD%B4)
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
これでdiscord.pyのインストール完了です。
## botアカウント作成
[こちら](https://discordpy.readthedocs.io/ja/latest/discord.html)の記事をご参照ください。
## botに必要な権限
- メッセージを送信(Send Message)
- メッセージの管理(Manage Message)
- アプリコマンドを使う(Use Slash Command)
# アップデート履歴
- 2023/12/18 レート制限に引っかからないように一度に消せるメッセージ数を15に制限しました。