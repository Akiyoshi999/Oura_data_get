# Oura_data_get
##  プログラムの概要
Oura ringの本日のデータ、1週間分のデータの平均値を取得し、取得したスコアをLINEで通知する。
## 作成の動機
Oura ringは自分の睡眠状態や健康状態を数値化してくれる便利なものだが、各日付毎のスコアしか分からない上にアプリを開かないとスコアが確認できないのが面倒。。
そこでスコアをLINEに送信することによって、LINEで本日のスコアや1週間分の平均スコアを確認したいと思い作成しました。

##  事前準備
- OuraのPersonal Access Token を作成すること
https://cloud.ouraring.com/personal-access-tokens

- LINE notify を登録しToken  を作成すること
https://notify-bot.line.me/ja/

## 使い方
1. 事前準備で使用したtokenの値を[code/config.ini]ファイルの各項目に記載する。また1週間のデータをまとめて取得したい曜日を設定する。
1. python LineMain.pyを実行、Windowsなら[Oura_get.bat]を実行することによってLINEに本日のスコアが送信される。
1. タスクスケジューラに起動することによって毎日決まった時刻にLINEを送信する事ができる。 

## 使用画面
![](https://raw.githubusercontent.com/wiki/Akiyoshi999/Oura_data_get/images/oura_get_photo.PNG)
