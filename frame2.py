from PyQt5.QtWidgets import QApplication, QWidget,QFileDialog
import sys


def call():
	fname = QFileDialog.getSaveFileName("SaveFile","","Text files(*.txt);;CSV files(*.csv)")
	