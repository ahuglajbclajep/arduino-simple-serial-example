# arduino-simple-serial-example

[pyserial](https://pypi.org/project/pyserial/) を使って Arduino とシリアル通信をする例。

## 使い方

1. `pip install -r requirements.txt`
2. [画像](arduino/wiring.jpg) を参考に配線
3. USB ケーブルで Arduino と PC をつなぐ
4. `python3 main.py -p COM3`
5. ボタンを押す

```sh
$ python3 main.py -h
usage: main.py [-h] [-p PORT] [-r RATE] [-s]

Arduinoとシリアル通信をします

optional arguments:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  ポートの指定
  -r RATE, --rate RATE  レートの指定
  -s, --show            使用するポートを表示
```
