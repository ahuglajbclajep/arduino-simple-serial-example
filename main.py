import sys
import argparse
import serial
import serial.tools.list_ports


def main():
    parser = argparse.ArgumentParser(description="Arduinoとシリアル通信をします")
    parser.add_argument("-p", "--port", help="ポートの指定")
    parser.add_argument("-r", "--rate", type=int, default=9600, help="レートの指定")
    parser.add_argument("-s", "--show", action="store_true", help="使用するポートを表示")
    args = parser.parse_args()

    run(args.port, args.rate, args.show)


def run(port, rate, show):
    try:
        if port is None:
            port = serial.tools.list_ports.comports()[0][0]  # 最初のポートのdeviceを取得

        if show:
            print("device:" + port)

        ser = serial.Serial(port, rate)
    except IndexError:  # ポートの自動取得に失敗したとき
        sys.stderr.write("ポートが検出できませんでした。")
        sys.exit(1)
    except:
        sys.exit(sys.exc_info()[1])

    while True:
        if ser.read():  # 1バイト読む, ボタンを押すとArduinoから1が送られる
            print("serial catched")


if __name__ == '__main__':
    main()
