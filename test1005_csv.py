from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import csv
from play1005 import Ui_Dialog

# 初始化應用程式
app = QApplication(sys.argv)
widget = QWidget()
ui = Ui_Dialog()
ui.setupUi(widget)

# 讀取語言設定檔 language.txt
with open("language.txt", mode="r") as file:
    txt = file.readline().strip().lower()  # 去除換行符號並轉為小寫
    
# 根據語言設定選擇對應的 CSV 文件
if txt == "chinese":
    readfile = "chi.csv"
elif txt == "english":
    readfile = "eng.csv"
elif txt == "japanese":
    readfile = "jap.csv"
else:
    readfile = "chi.csv"  # 預設為中文

# 初始化翻譯字典
translate = {}

# 從對應的 CSV 文件中讀取翻譯對應資料
try:
    with open(readfile, mode="r", encoding="utf-8") as f:
        csv_reader = csv.reader(f)
        # 讀取第一行標題作為 key，例如：["button", "hello", "morning"]
        keys = next(csv_reader)
        
        # 讀取第二行內容作為對應的翻譯值
        values = next(csv_reader)
        
        # 將 keys 和 values 結合為字典，例如：{"button": "ボタン", "hello": "んにちは", "morning": "おはよう"}
        translate = dict(zip(keys, values))
except FileNotFoundError:
    print(f"無法找到指定的翻譯檔案：{readfile}")
    translate = {"button": "Button", "hello": "Hello", "morning": "Good Morning"}  # 預設英文字典

# 設定按鈕和標籤的文字
ui.pushButton.setText(translate.get("button", "Button"))  # 如果沒有找到對應的 key，使用 "Button" 作為預設

# 定義按鈕點擊事件
def buttonClick():
    ui.label.setText(translate.get("hello", "Hello"))  # 如果沒有找到對應的 key，使用 "Hello" 作為預設

# 連接按鈕點擊事件
ui.pushButton.clicked.connect(buttonClick)

# 顯示視窗
widget.show()
app.exec_()
