# kuso-arduino-button
PythonとかPyCharmとかArduinoとかの練習

## Description
pyserialを使ってArduinoとシリアル通信ができます  
まだそれだけ

## Usage
### Install
```
git clone git@github.com:ahuglajbclajep/kuso-arduino-button.git
cd kuso-arduino-button
pip install -r requirements.txt
python3 main.py
```  
and Arduino setup.

### Run
```
python3 main.py -p COM3 # ポートの指定
python3 main.py -r 9600 # 転送レートの指定
python3 main.py -s # 使用するポートを表示
```

## Future Releases
* オプションで指定したものを起動するとか？
* なにか案があれば[issues](https://github.com/ahuglajbclajep/kuso-arduino-button/issues)にどうぞ

## Contribution
1. Fork it  
2. Create your feature branch  
3. Commit your changes  
4. Push to the branch  
5. Create new Pull Request

## License
[MIT](LICENSE)
