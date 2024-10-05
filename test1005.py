from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from play1005 import Ui_Dialog

app = QApplication(sys.argv)
widget = QWidget()
ui = Ui_Dialog()
ui.setupUi(widget)

# 先定義字典
# 初始化變數
ui.label.setText("")

translate_to_chinese = {"button" : "按鈕",
                        "hello" : "你好"}

translate_to_english = {"button" : "buttom",
                        "hello" : "hello"}

translate_to_japanese = {"button" : "ボタン",
                        "hello" : "こんにちは"}

# 開啟語言指定檔
# 進行轉譯 
with open ("language.txt", mode = "r") as file:
    txt = file.readline()
    # print(txt)根據讀取到的語言設定選擇對應的字典
    if txt == "chinese":
        translate = translate_to_chinese
    elif txt == "english":
        translate = translate_to_english
    elif txt == "japanese":
        translate = translate_to_japanese
    else:
        translate = translate_to_chinese # 預設中文
        # translate = {"button": "無法辨識", "hello": "無法辨識"}  # 預設錯誤訊息

ui.pushButton.setText(translate["button"])
    
def buttonClick():
    ui.label.setText(translate["hello"])
    # msg = QMessageBox()
    # msg.setInformativeText(translate["hello"])
    # msg.exec_()

ui.pushButton.clicked.connect(buttonClick)
widget.show()
app.exec_()

