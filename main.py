import sys
import argparse
import serial


def main():
    parser = argparse.ArgumentParser(description='COM3ポートでArduinoとシリアル通信をします')
    args = parser.parse_args()
    run()


def run():
    port = 'COM3'  # OS依存, serial.tools.list_ports.comports() で調べられる
    try:
        ser = serial.Serial(port, 9600)
    except:
        sys.exit(sys.exc_info()[1])

    while True:
        print(ser.read(1).decode('utf-8'))  # 1バイト読んで文字列に変換


if __name__ == '__main__':
    main()
