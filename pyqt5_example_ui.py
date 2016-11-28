import sys
import requests
from PyQt5.QtWidgets import QApplication ,QWidget,QHBoxButton, QPushButton,QTextEdit , QVBoxLayout
from PyQt5.QtGui import QFont
from bs4 import BeautifulSoup
#123123
class init_ui(QWidget):	# ui interface to create
	global array,namelist
	global num,y
	num = 0
	array = ["","headline","entertainment","international","sports","finance"]
	namelist = ["今日熱門","頭條","娛樂","國際","運動","金融"]
	def __init__(self):
		super().__init__()
		self.ui()
	def ui(self):
		self.resize(1200,800)

		self.setWindowTitle("Welcome to my house")
		btn = QPushButton("爬蟲",self)	# apple news search
		btn.clicked.connect(self.search)
		btn2 = QPushButton("關於",self)	# author introduce 
		btn2.clicked.connect(self.author)
		# text to show main screen
		self.text = QTextEdit("",self)
		self.text.resize(400,800)
		self.text.setReadOnly(True)

		bottomlayout = QVBoxLayout()
		bottomlayout.addWidget(btn)
		bottomlayout.addWidget(btn2)

		centerlayout = QVBoxLayout()
		centerlayout.addWidget(self.text)

		mainlayout = QVBoxLayout()
		mainlayout.addLayout(centerlayout,5)
		mainlayout.addLayout(bottomlayout)
		self.setLayout(mainlayout)
		self.show()
	# push btn to search url
	def search(self):
		global num
		global y
		# print(num)
		self.text.setFont(QFont("標楷體",15,30,False))
		if num == 0:
			y = "" # save the url get details
			for j in range(0,len(array)):
			# 例外處理 try for solution
				try:
					res = requests.get('http://www.appledaily.com.tw/appledaily/hotdaily/'+array[j])
					res.encoding = 'utf=8'
					soup = BeautifulSoup(res.text,"html.parser")
			# x+=soup.select('time')[0].text+"\n"
				except:
					self.text.setText("發生錯誤! 請檢察網路連線------")
					break
				y += namelist[j] + ":\n"
				try:
					for i in range(0,31):
						y +="%2d." % int(i+1)+soup.select('.aht_title')[i].text+" *"+soup.select('.aht_pv_num')[i].text+"\n"
				except:
					y += "\n"
			self.text.setText(y)
			num = 1
		else:
			self.text.setText(y)
	# push btn2 to know author things
	def author(self):
		x = ""
		self.text.setFont(QFont("標楷體",40,60,False))
		x += "作者: Wayne\n開發時間: 2016/11/25 "
		self.text.setText(x)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ui_run = init_ui()
	sys.exit(app.exec_())