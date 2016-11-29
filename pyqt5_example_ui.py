import time
import sys
import requests
import frame2 
from PyQt5.QtWidgets import QRadioButton,QLabel,QApplication ,QWidget,QHBoxLayout,QPushButton,QTextEdit , QVBoxLayout , QFileDialog
from PyQt5.QtGui import QFont,QColor
from bs4 import BeautifulSoup

# Color [0] 黃色 [1] 橘色 [2]
global Colordatabase,Fontdatabase
Colordatabase = ["background-color: #ffff00","background-color: #fc5219","background-color: #ab2888","background-color: #8755fc"]
# Font 
Fontdatabase = [QFont('normal',15,30,False),QFont('normal',40,60,False),QFont('標楷體',10,10,False)]

class init_ui(QWidget):	# ui interface to create
	
	# array url 網址
	# namelist gui look title name
	# radiolist radiobutton name use
	# radioname to loop use 

	global array,namelist,radiolist,radioname
	global num,y
	num = 0
	array = ["","headline","entertainment","international","sports","finance"]
	namelist = ["今日熱門","頭條","娛樂","國際","運動","金融"]
	radiolist = ["1","2","3"]
	radioname = ["rb1","rb2","rb3"]
	def __init__(self):
		super().__init__()
		self.ui()
	def ui(self):
		# know radiobutton was pushed
		radiobtncontrol = 0
		
		self.resize(1200,800)
		self.setWindowTitle("apples爬蟲")
		# Button

		btn = QPushButton("爬蟲",self)	# apple news search
		btn.clicked.connect(self.search)
		btn.setStyleSheet(Colordatabase[0])
		btn2 = QPushButton("關於",self)	# author introduce 
		btn2.clicked.connect(self.author)
		btn3 = QPushButton("Intent",self)
		btn3.clicked.connect(self.newFrame)
		# text to show main screen
		self.text = QTextEdit("",self)
		self.text.setReadOnly(True)
		self.timelook = QLabel("",self)

		#Layout
		
		rightlayout = QVBoxLayout()

		for radioi in range(0,3):
			radioname[radioi] = QRadioButton(radiolist[radioi],self)
			rightlayout.addWidget(radioname[radioi])
		radioname[0].clicked.connect(self.radiofunction1)
		radioname[1].clicked.connect(self.radiofunction2)
		radioname[2].clicked.connect(self.radiofunction3)
		rightlayout.addWidget(btn3)
		bottomlayout = QVBoxLayout()
		bottomlayout.addWidget(btn)
		bottomlayout.addWidget(btn2)
		toplayout = QVBoxLayout()
		toplayout.addWidget(self.timelook)
		centerlayout = QHBoxLayout()
		centerlayout.addWidget(self.text)
		centerlayout.addLayout(rightlayout)
		mainlayout = QVBoxLayout()
		mainlayout.addLayout(toplayout)
		mainlayout.addLayout(centerlayout,5)
		mainlayout.addLayout(bottomlayout)
		self.setLayout(mainlayout)
		
		# show
		self.Timeget()
		self.show()
	# push btn to search url
	def search(self):
		global num
		global y
		global Maxtitle

		self.text.setFont(Fontdatabase[0]) 
		if num == 0:
			Maxtitle=""
			y = "" # save the url get details
			y += "----蘋果新聞----\n搜尋時間: "+time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())+"\n\n"
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
						if Maxtitle < soup.select('.aht_pv_num')[i].text:
							Maxtitle = soup.select('.aht_title')[i].text+" *"+soup.select('.aht_pv_num')[i].text
				except:
					y += "\n"
			y += "本日人氣=> "+Maxtitle
			self.text.setText(y)
			num = 1
		else:
			self.text.setText(y)
		self.Timeget()	# time change
	# to save the search details
	# to make designer for save & see
	def newFrame(self):
		fopen = QFileDialog.getSaveFileName(self,"Open file","爬蟲detail.txt","(*.txt);;(*.py)")
		
		if fopen[0]:
			ff = open(fopen[0],"w")
			ff.write(self.text.toPlainText())
			ff.close()
		# self.text.setText()

		
	# push btn2 to know author things
	def author(self):
		x = ""
		self.text.setFont(Fontdatabase[1])
		x += "作者: Wayne\n開發時間: 2016/11/25 "
		self.text.setText(x)
		self.Timeget()
	# radio function def
	def radiofunction1(self):
		self.text.setFont(Fontdatabase[2])
		self.text.setText("1")
		self.Timeget()
	def radiofunction2(self):
		self.text.setFont(Fontdatabase[2])
		self.text.setText("2")
		self.Timeget()
	def radiofunction3(self):
		self.text.setFont(Fontdatabase[2])
		self.text.setText("3")
		self.Timeget()
	# make user know the time now
	def Timeget(self):
		global stime
		stime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
		self.timelook.setText(str(stime))

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ui_run = init_ui()
	sys.exit(app.exec_())