from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import time
import algorithms, tools

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(1202, 680)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
		MainWindow.setSizePolicy(sizePolicy)
		MainWindow.setMinimumSize(QtCore.QSize(1202, 680))
		MainWindow.setMaximumSize(QtCore.QSize(1202, 680))
		icon = QtGui.QIcon("icon.ico")
		MainWindow.setWindowIcon(icon)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.buttonGenRan = QtWidgets.QPushButton(self.centralwidget)
		self.buttonGenRan.setGeometry(QtCore.QRect(390, 80, 121, 30))
		self.buttonGenRan.setObjectName("buttonGenRan")
		self.labelStatus = QtWidgets.QLabel(self.centralwidget)
		self.labelStatus.setGeometry(QtCore.QRect(20, 142, 47, 13))
		self.labelStatus.setAlignment(QtCore.Qt.AlignCenter)
		self.labelStatus.setObjectName("labelStatus")
		self.labelStatusVal = QtWidgets.QLabel(self.centralwidget)
		self.labelStatusVal.setGeometry(QtCore.QRect(70, 140, 150, 16))
		self.labelStatusVal.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
		self.labelStatusVal.setObjectName("labelStatusVal")
		self.sliderDelay = QtWidgets.QSlider(self.centralwidget)
		self.sliderDelay.setGeometry(QtCore.QRect(650, 40, 121, 30))
		self.sliderDelay.setMinimum(100)
		self.sliderDelay.setMaximum(1000)
		self.sliderDelay.setSingleStep(100)
		self.sliderDelay.setTracking(False)
		self.sliderDelay.setOrientation(QtCore.Qt.Horizontal)
		self.sliderDelay.setInvertedAppearance(False)
		self.sliderDelay.setInvertedControls(False)
		self.sliderDelay.setTickPosition(QtWidgets.QSlider.NoTicks)
		self.sliderDelay.setObjectName("sliderDelay")
		__class__.bar48 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar48.setGeometry(QtCore.QRect(569, 170, 12, 500))
		__class__.bar48.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar48.setProperty("value", 50)
		__class__.bar48.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar48.setTextVisible(False)
		__class__.bar48.setOrientation(QtCore.Qt.Vertical)
		__class__.bar48.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar48.setObjectName("bar48")
		__class__.bar45 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar45.setGeometry(QtCore.QRect(533, 170, 12, 500))
		__class__.bar45.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar45.setProperty("value", 50)
		__class__.bar45.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar45.setTextVisible(False)
		__class__.bar45.setOrientation(QtCore.Qt.Vertical)
		__class__.bar45.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar45.setObjectName("bar45")
		__class__.bar1 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar1.setGeometry(QtCore.QRect(14, 170, 12, 500))
		__class__.bar1.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar1.setProperty("value", 50)
		__class__.bar1.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar1.setTextVisible(False)
		__class__.bar1.setOrientation(QtCore.Qt.Vertical)
		__class__.bar1.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar1.setObjectName("bar1")
		__class__.bar38 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar38.setGeometry(QtCore.QRect(451, 170, 12, 500))
		__class__.bar38.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar38.setProperty("value", 50)
		__class__.bar38.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar38.setTextVisible(False)
		__class__.bar38.setOrientation(QtCore.Qt.Vertical)
		__class__.bar38.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar38.setObjectName("bar38")
		__class__.bar64 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar64.setGeometry(QtCore.QRect(757, 170, 12, 500))
		__class__.bar64.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar64.setProperty("value", 50)
		__class__.bar64.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar64.setTextVisible(False)
		__class__.bar64.setOrientation(QtCore.Qt.Vertical)
		__class__.bar64.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar64.setObjectName("bar64")
		__class__.bar34 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar34.setGeometry(QtCore.QRect(404, 170, 12, 500))
		__class__.bar34.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar34.setProperty("value", 50)
		__class__.bar34.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar34.setTextVisible(False)
		__class__.bar34.setOrientation(QtCore.Qt.Vertical)
		__class__.bar34.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar34.setObjectName("bar34")
		__class__.bar32 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar32.setGeometry(QtCore.QRect(380, 170, 12, 500))
		__class__.bar32.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar32.setProperty("value", 50)
		__class__.bar32.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar32.setTextVisible(False)
		__class__.bar32.setOrientation(QtCore.Qt.Vertical)
		__class__.bar32.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar32.setObjectName("bar32")
		__class__.bar28 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar28.setGeometry(QtCore.QRect(333, 170, 12, 500))
		__class__.bar28.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar28.setProperty("value", 50)
		__class__.bar28.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar28.setTextVisible(False)
		__class__.bar28.setOrientation(QtCore.Qt.Vertical)
		__class__.bar28.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar28.setObjectName("bar28")
		__class__.bar44 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar44.setGeometry(QtCore.QRect(521, 170, 12, 500))
		__class__.bar44.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar44.setProperty("value", 50)
		__class__.bar44.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar44.setTextVisible(False)
		__class__.bar44.setOrientation(QtCore.Qt.Vertical)
		__class__.bar44.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar44.setObjectName("bar44")
		__class__.bar98 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar98.setEnabled(True)
		__class__.bar98.setGeometry(QtCore.QRect(1158, 170, 12, 500))
		__class__.bar98.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar98.setProperty("value", 50)
		__class__.bar98.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar98.setTextVisible(False)
		__class__.bar98.setOrientation(QtCore.Qt.Vertical)
		__class__.bar98.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar98.setObjectName("bar98")
		__class__.bar2 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar2.setGeometry(QtCore.QRect(26, 170, 12, 500))
		__class__.bar2.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar2.setProperty("value", 50)
		__class__.bar2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar2.setTextVisible(False)
		__class__.bar2.setOrientation(QtCore.Qt.Vertical)
		__class__.bar2.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar2.setObjectName("bar2")
		__class__.bar56 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar56.setGeometry(QtCore.QRect(663, 170, 12, 500))
		__class__.bar56.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar56.setProperty("value", 50)
		__class__.bar56.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar56.setTextVisible(False)
		__class__.bar56.setOrientation(QtCore.Qt.Vertical)
		__class__.bar56.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar56.setObjectName("bar56")
		__class__.bar49 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar49.setGeometry(QtCore.QRect(580, 170, 12, 500))
		__class__.bar49.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar49.setProperty("value", 50)
		__class__.bar49.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar49.setTextVisible(False)
		__class__.bar49.setOrientation(QtCore.Qt.Vertical)
		__class__.bar49.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar49.setObjectName("bar49")
		__class__.bar99 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar99.setGeometry(QtCore.QRect(1170, 170, 12, 500))
		__class__.bar99.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar99.setProperty("value", 50)
		__class__.bar99.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar99.setTextVisible(False)
		__class__.bar99.setOrientation(QtCore.Qt.Vertical)
		__class__.bar99.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar99.setObjectName("bar99")
		__class__.bar26 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar26.setGeometry(QtCore.QRect(309, 170, 12, 500))
		__class__.bar26.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar26.setProperty("value", 50)
		__class__.bar26.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar26.setTextVisible(False)
		__class__.bar26.setOrientation(QtCore.Qt.Vertical)
		__class__.bar26.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar26.setObjectName("bar26")
		__class__.bar12 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar12.setGeometry(QtCore.QRect(144, 170, 12, 500))
		__class__.bar12.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar12.setProperty("value", 50)
		__class__.bar12.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar12.setTextVisible(False)
		__class__.bar12.setOrientation(QtCore.Qt.Vertical)
		__class__.bar12.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar12.setObjectName("bar12")
		__class__.bar17 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar17.setGeometry(QtCore.QRect(203, 170, 12, 500))
		__class__.bar17.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar17.setProperty("value", 50)
		__class__.bar17.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar17.setTextVisible(False)
		__class__.bar17.setOrientation(QtCore.Qt.Vertical)
		__class__.bar17.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar17.setObjectName("bar17")
		__class__.bar16 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar16.setGeometry(QtCore.QRect(191, 170, 12, 500))
		__class__.bar16.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar16.setProperty("value", 50)
		__class__.bar16.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar16.setTextVisible(False)
		__class__.bar16.setOrientation(QtCore.Qt.Vertical)
		__class__.bar16.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar16.setObjectName("bar16")
		__class__.bar23 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar23.setGeometry(QtCore.QRect(274, 170, 12, 500))
		__class__.bar23.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar23.setProperty("value", 50)
		__class__.bar23.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar23.setTextVisible(False)
		__class__.bar23.setOrientation(QtCore.Qt.Vertical)
		__class__.bar23.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar23.setObjectName("bar23")
		__class__.bar69 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar69.setGeometry(QtCore.QRect(816, 170, 12, 500))
		__class__.bar69.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar69.setProperty("value", 50)
		__class__.bar69.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar69.setTextVisible(False)
		__class__.bar69.setOrientation(QtCore.Qt.Vertical)
		__class__.bar69.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar69.setObjectName("bar69")
		__class__.bar81 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar81.setGeometry(QtCore.QRect(958, 170, 12, 500))
		__class__.bar81.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar81.setProperty("value", 50)
		__class__.bar81.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar81.setTextVisible(False)
		__class__.bar81.setOrientation(QtCore.Qt.Vertical)
		__class__.bar81.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar81.setObjectName("bar81")
		__class__.bar59 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar59.setGeometry(QtCore.QRect(698, 170, 12, 500))
		__class__.bar59.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar59.setProperty("value", 50)
		__class__.bar59.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar59.setTextVisible(False)
		__class__.bar59.setOrientation(QtCore.Qt.Vertical)
		__class__.bar59.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar59.setObjectName("bar59")
		__class__.bar43 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar43.setGeometry(QtCore.QRect(510, 170, 12, 500))
		__class__.bar43.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar43.setProperty("value", 50)
		__class__.bar43.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar43.setTextVisible(False)
		__class__.bar43.setOrientation(QtCore.Qt.Vertical)
		__class__.bar43.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar43.setObjectName("bar43")
		__class__.bar95 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar95.setEnabled(True)
		__class__.bar95.setGeometry(QtCore.QRect(1123, 170, 12, 500))
		__class__.bar95.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar95.setProperty("value", 50)
		__class__.bar95.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar95.setTextVisible(False)
		__class__.bar95.setOrientation(QtCore.Qt.Vertical)
		__class__.bar95.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar95.setObjectName("bar95")
		__class__.bar89 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar89.setGeometry(QtCore.QRect(1052, 170, 12, 500))
		__class__.bar89.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar89.setProperty("value", 50)
		__class__.bar89.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar89.setTextVisible(False)
		__class__.bar89.setOrientation(QtCore.Qt.Vertical)
		__class__.bar89.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar89.setObjectName("bar89")
		__class__.bar75 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar75.setGeometry(QtCore.QRect(887, 170, 12, 500))
		__class__.bar75.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar75.setProperty("value", 50)
		__class__.bar75.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar75.setTextVisible(False)
		__class__.bar75.setOrientation(QtCore.Qt.Vertical)
		__class__.bar75.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar75.setObjectName("bar75")
		__class__.bar70 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar70.setGeometry(QtCore.QRect(828, 170, 12, 500))
		__class__.bar70.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar70.setProperty("value", 50)
		__class__.bar70.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar70.setTextVisible(False)
		__class__.bar70.setOrientation(QtCore.Qt.Vertical)
		__class__.bar70.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar70.setObjectName("bar70")
		__class__.bar42 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar42.setGeometry(QtCore.QRect(498, 170, 12, 500))
		__class__.bar42.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar42.setProperty("value", 50)
		__class__.bar42.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar42.setTextVisible(False)
		__class__.bar42.setOrientation(QtCore.Qt.Vertical)
		__class__.bar42.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar42.setObjectName("bar42")
		__class__.bar41 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar41.setGeometry(QtCore.QRect(486, 170, 12, 500))
		__class__.bar41.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar41.setProperty("value", 50)
		__class__.bar41.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar41.setTextVisible(False)
		__class__.bar41.setOrientation(QtCore.Qt.Vertical)
		__class__.bar41.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar41.setObjectName("bar41")
		__class__.bar22 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar22.setGeometry(QtCore.QRect(262, 170, 12, 500))
		__class__.bar22.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar22.setProperty("value", 50)
		__class__.bar22.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar22.setTextVisible(False)
		__class__.bar22.setOrientation(QtCore.Qt.Vertical)
		__class__.bar22.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar22.setObjectName("bar22")
		__class__.bar31 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar31.setGeometry(QtCore.QRect(368, 170, 12, 500))
		__class__.bar31.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar31.setProperty("value", 50)
		__class__.bar31.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar31.setTextVisible(False)
		__class__.bar31.setOrientation(QtCore.Qt.Vertical)
		__class__.bar31.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar31.setObjectName("bar31")
		__class__.bar39 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar39.setGeometry(QtCore.QRect(463, 170, 12, 500))
		__class__.bar39.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar39.setProperty("value", 50)
		__class__.bar39.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar39.setTextVisible(False)
		__class__.bar39.setOrientation(QtCore.Qt.Vertical)
		__class__.bar39.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar39.setObjectName("bar39")
		__class__.bar63 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar63.setGeometry(QtCore.QRect(745, 170, 12, 500))
		__class__.bar63.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar63.setProperty("value", 50)
		__class__.bar63.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar63.setTextVisible(False)
		__class__.bar63.setOrientation(QtCore.Qt.Vertical)
		__class__.bar63.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar63.setObjectName("bar63")
		__class__.bar88 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar88.setGeometry(QtCore.QRect(1040, 170, 12, 500))
		__class__.bar88.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar88.setProperty("value", 50)
		__class__.bar88.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar88.setTextVisible(False)
		__class__.bar88.setOrientation(QtCore.Qt.Vertical)
		__class__.bar88.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar88.setObjectName("bar88")
		__class__.bar7 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar7.setGeometry(QtCore.QRect(85, 170, 12, 500))
		__class__.bar7.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar7.setProperty("value", 50)
		__class__.bar7.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar7.setTextVisible(False)
		__class__.bar7.setOrientation(QtCore.Qt.Vertical)
		__class__.bar7.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar7.setObjectName("bar7")
		__class__.bar35 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar35.setGeometry(QtCore.QRect(415, 170, 12, 500))
		__class__.bar35.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar35.setProperty("value", 50)
		__class__.bar35.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar35.setTextVisible(False)
		__class__.bar35.setOrientation(QtCore.Qt.Vertical)
		__class__.bar35.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar35.setObjectName("bar35")
		__class__.bar54 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar54.setGeometry(QtCore.QRect(639, 170, 12, 500))
		__class__.bar54.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar54.setProperty("value", 50)
		__class__.bar54.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar54.setTextVisible(False)
		__class__.bar54.setOrientation(QtCore.Qt.Vertical)
		__class__.bar54.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar54.setObjectName("bar54")
		__class__.bar65 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar65.setGeometry(QtCore.QRect(769, 170, 12, 500))
		__class__.bar65.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar65.setProperty("value", 50)
		__class__.bar65.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar65.setTextVisible(False)
		__class__.bar65.setOrientation(QtCore.Qt.Vertical)
		__class__.bar65.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar65.setObjectName("bar65")
		__class__.bar55 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar55.setGeometry(QtCore.QRect(651, 170, 12, 500))
		__class__.bar55.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar55.setProperty("value", 50)
		__class__.bar55.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar55.setTextVisible(False)
		__class__.bar55.setOrientation(QtCore.Qt.Vertical)
		__class__.bar55.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar55.setObjectName("bar55")
		__class__.bar47 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar47.setGeometry(QtCore.QRect(557, 170, 12, 500))
		__class__.bar47.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar47.setProperty("value", 50)
		__class__.bar47.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar47.setTextVisible(False)
		__class__.bar47.setOrientation(QtCore.Qt.Vertical)
		__class__.bar47.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar47.setObjectName("bar47")
		__class__.bar40 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar40.setGeometry(QtCore.QRect(474, 170, 12, 500))
		__class__.bar40.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar40.setProperty("value", 50)
		__class__.bar40.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar40.setTextVisible(False)
		__class__.bar40.setOrientation(QtCore.Qt.Vertical)
		__class__.bar40.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar40.setObjectName("bar40")
		__class__.bar74 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar74.setGeometry(QtCore.QRect(875, 170, 12, 500))
		__class__.bar74.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar74.setProperty("value", 50)
		__class__.bar74.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar74.setTextVisible(False)
		__class__.bar74.setOrientation(QtCore.Qt.Vertical)
		__class__.bar74.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar74.setObjectName("bar74")
		__class__.bar4 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar4.setGeometry(QtCore.QRect(50, 170, 12, 500))
		__class__.bar4.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar4.setProperty("value", 50)
		__class__.bar4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar4.setTextVisible(False)
		__class__.bar4.setOrientation(QtCore.Qt.Vertical)
		__class__.bar4.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar4.setObjectName("bar4")
		__class__.bar36 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar36.setGeometry(QtCore.QRect(427, 170, 12, 500))
		__class__.bar36.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar36.setProperty("value", 50)
		__class__.bar36.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar36.setTextVisible(False)
		__class__.bar36.setOrientation(QtCore.Qt.Vertical)
		__class__.bar36.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar36.setObjectName("bar36")
		__class__.bar58 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar58.setGeometry(QtCore.QRect(687, 170, 12, 500))
		__class__.bar58.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar58.setProperty("value", 50)
		__class__.bar58.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar58.setTextVisible(False)
		__class__.bar58.setOrientation(QtCore.Qt.Vertical)
		__class__.bar58.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar58.setObjectName("bar58")
		__class__.bar72 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar72.setGeometry(QtCore.QRect(852, 170, 12, 500))
		__class__.bar72.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar72.setProperty("value", 50)
		__class__.bar72.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar72.setTextVisible(False)
		__class__.bar72.setOrientation(QtCore.Qt.Vertical)
		__class__.bar72.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar72.setObjectName("bar72")
		__class__.bar51 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar51.setGeometry(QtCore.QRect(604, 170, 12, 500))
		__class__.bar51.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar51.setProperty("value", 50)
		__class__.bar51.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar51.setTextVisible(False)
		__class__.bar51.setOrientation(QtCore.Qt.Vertical)
		__class__.bar51.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar51.setObjectName("bar51")
		__class__.bar87 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar87.setGeometry(QtCore.QRect(1028, 170, 12, 500))
		__class__.bar87.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar87.setProperty("value", 50)
		__class__.bar87.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar87.setTextVisible(False)
		__class__.bar87.setOrientation(QtCore.Qt.Vertical)
		__class__.bar87.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar87.setObjectName("bar87")
		__class__.bar79 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar79.setGeometry(QtCore.QRect(934, 170, 12, 500))
		__class__.bar79.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar79.setProperty("value", 50)
		__class__.bar79.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar79.setTextVisible(False)
		__class__.bar79.setOrientation(QtCore.Qt.Vertical)
		__class__.bar79.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar79.setObjectName("bar79")
		__class__.bar94 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar94.setGeometry(QtCore.QRect(1111, 170, 12, 500))
		__class__.bar94.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar94.setProperty("value", 50)
		__class__.bar94.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar94.setTextVisible(False)
		__class__.bar94.setOrientation(QtCore.Qt.Vertical)
		__class__.bar94.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar94.setObjectName("bar94")
		__class__.bar71 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar71.setGeometry(QtCore.QRect(840, 170, 12, 500))
		__class__.bar71.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar71.setProperty("value", 50)
		__class__.bar71.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar71.setTextVisible(False)
		__class__.bar71.setOrientation(QtCore.Qt.Vertical)
		__class__.bar71.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar71.setObjectName("bar71")
		__class__.bar50 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar50.setGeometry(QtCore.QRect(592, 170, 12, 500))
		__class__.bar50.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar50.setProperty("value", 50)
		__class__.bar50.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar50.setTextVisible(False)
		__class__.bar50.setOrientation(QtCore.Qt.Vertical)
		__class__.bar50.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar50.setObjectName("bar50")
		__class__.bar10 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar10.setGeometry(QtCore.QRect(121, 170, 12, 500))
		__class__.bar10.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar10.setProperty("value", 50)
		__class__.bar10.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar10.setTextVisible(False)
		__class__.bar10.setOrientation(QtCore.Qt.Vertical)
		__class__.bar10.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar10.setObjectName("bar10")
		__class__.bar96 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar96.setGeometry(QtCore.QRect(1135, 170, 12, 500))
		__class__.bar96.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar96.setProperty("value", 50)
		__class__.bar96.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar96.setTextVisible(False)
		__class__.bar96.setOrientation(QtCore.Qt.Vertical)
		__class__.bar96.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar96.setObjectName("bar96")
		__class__.bar8 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar8.setGeometry(QtCore.QRect(97, 170, 12, 500))
		__class__.bar8.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar8.setProperty("value", 50)
		__class__.bar8.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar8.setTextVisible(False)
		__class__.bar8.setOrientation(QtCore.Qt.Vertical)
		__class__.bar8.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar8.setObjectName("bar8")
		__class__.bar21 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar21.setGeometry(QtCore.QRect(250, 170, 12, 500))
		__class__.bar21.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar21.setProperty("value", 50)
		__class__.bar21.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar21.setTextVisible(False)
		__class__.bar21.setOrientation(QtCore.Qt.Vertical)
		__class__.bar21.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar21.setObjectName("bar21")
		__class__.bar25 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar25.setGeometry(QtCore.QRect(297, 170, 12, 500))
		__class__.bar25.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar25.setProperty("value", 50)
		__class__.bar25.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar25.setTextVisible(False)
		__class__.bar25.setOrientation(QtCore.Qt.Vertical)
		__class__.bar25.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar25.setObjectName("bar25")
		__class__.bar100 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar100.setGeometry(QtCore.QRect(1182, 170, 12, 500))
		__class__.bar100.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar100.setProperty("value", 50)
		__class__.bar100.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar100.setTextVisible(False)
		__class__.bar100.setOrientation(QtCore.Qt.Vertical)
		__class__.bar100.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar100.setObjectName("bar100")
		__class__.bar80 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar80.setGeometry(QtCore.QRect(946, 170, 12, 500))
		__class__.bar80.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar80.setProperty("value", 50)
		__class__.bar80.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar80.setTextVisible(False)
		__class__.bar80.setOrientation(QtCore.Qt.Vertical)
		__class__.bar80.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar80.setObjectName("bar80")
		__class__.bar29 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar29.setGeometry(QtCore.QRect(345, 170, 12, 500))
		__class__.bar29.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar29.setProperty("value", 50)
		__class__.bar29.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar29.setTextVisible(False)
		__class__.bar29.setOrientation(QtCore.Qt.Vertical)
		__class__.bar29.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar29.setObjectName("bar29")
		__class__.bar78 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar78.setGeometry(QtCore.QRect(922, 170, 12, 500))
		__class__.bar78.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar78.setProperty("value", 50)
		__class__.bar78.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar78.setTextVisible(False)
		__class__.bar78.setOrientation(QtCore.Qt.Vertical)
		__class__.bar78.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar78.setObjectName("bar78")
		__class__.bar86 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar86.setGeometry(QtCore.QRect(1017, 170, 12, 500))
		__class__.bar86.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar86.setProperty("value", 50)
		__class__.bar86.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar86.setTextVisible(False)
		__class__.bar86.setOrientation(QtCore.Qt.Vertical)
		__class__.bar86.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar86.setObjectName("bar86")
		__class__.bar67 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar67.setGeometry(QtCore.QRect(793, 170, 12, 500))
		__class__.bar67.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar67.setProperty("value", 50)
		__class__.bar67.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar67.setTextVisible(False)
		__class__.bar67.setOrientation(QtCore.Qt.Vertical)
		__class__.bar67.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar67.setObjectName("bar67")
		__class__.bar52 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar52.setGeometry(QtCore.QRect(616, 170, 12, 500))
		__class__.bar52.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar52.setProperty("value", 50)
		__class__.bar52.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar52.setTextVisible(False)
		__class__.bar52.setOrientation(QtCore.Qt.Vertical)
		__class__.bar52.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar52.setObjectName("bar52")
		__class__.bar82 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar82.setGeometry(QtCore.QRect(969, 170, 12, 500))
		__class__.bar82.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar82.setProperty("value", 50)
		__class__.bar82.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar82.setTextVisible(False)
		__class__.bar82.setOrientation(QtCore.Qt.Vertical)
		__class__.bar82.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar82.setObjectName("bar82")
		__class__.bar24 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar24.setGeometry(QtCore.QRect(286, 170, 12, 500))
		__class__.bar24.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar24.setProperty("value", 50)
		__class__.bar24.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar24.setTextVisible(False)
		__class__.bar24.setOrientation(QtCore.Qt.Vertical)
		__class__.bar24.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar24.setObjectName("bar24")
		__class__.bar20 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar20.setGeometry(QtCore.QRect(239, 170, 12, 500))
		__class__.bar20.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar20.setProperty("value", 50)
		__class__.bar20.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar20.setTextVisible(False)
		__class__.bar20.setOrientation(QtCore.Qt.Vertical)
		__class__.bar20.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar20.setObjectName("bar20")
		__class__.bar76 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar76.setGeometry(QtCore.QRect(899, 170, 12, 500))
		__class__.bar76.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar76.setProperty("value", 50)
		__class__.bar76.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar76.setTextVisible(False)
		__class__.bar76.setOrientation(QtCore.Qt.Vertical)
		__class__.bar76.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar76.setObjectName("bar76")
		__class__.bar27 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar27.setGeometry(QtCore.QRect(321, 170, 12, 500))
		__class__.bar27.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar27.setProperty("value", 50)
		__class__.bar27.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar27.setTextVisible(False)
		__class__.bar27.setOrientation(QtCore.Qt.Vertical)
		__class__.bar27.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar27.setObjectName("bar27")
		__class__.bar83 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar83.setGeometry(QtCore.QRect(981, 170, 12, 500))
		__class__.bar83.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar83.setProperty("value", 50)
		__class__.bar83.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar83.setTextVisible(False)
		__class__.bar83.setOrientation(QtCore.Qt.Vertical)
		__class__.bar83.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar83.setObjectName("bar83")
		__class__.bar57 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar57.setGeometry(QtCore.QRect(675, 170, 12, 500))
		__class__.bar57.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar57.setProperty("value", 50)
		__class__.bar57.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar57.setTextVisible(False)
		__class__.bar57.setOrientation(QtCore.Qt.Vertical)
		__class__.bar57.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar57.setObjectName("bar57")
		__class__.bar6 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar6.setGeometry(QtCore.QRect(73, 170, 12, 500))
		__class__.bar6.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar6.setProperty("value", 50)
		__class__.bar6.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar6.setTextVisible(False)
		__class__.bar6.setOrientation(QtCore.Qt.Vertical)
		__class__.bar6.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar6.setObjectName("bar6")
		__class__.bar53 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar53.setGeometry(QtCore.QRect(628, 170, 12, 500))
		__class__.bar53.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar53.setProperty("value", 50)
		__class__.bar53.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar53.setTextVisible(False)
		__class__.bar53.setOrientation(QtCore.Qt.Vertical)
		__class__.bar53.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar53.setObjectName("bar53")
		__class__.bar33 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar33.setGeometry(QtCore.QRect(392, 170, 12, 500))
		__class__.bar33.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar33.setProperty("value", 50)
		__class__.bar33.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar33.setTextVisible(False)
		__class__.bar33.setOrientation(QtCore.Qt.Vertical)
		__class__.bar33.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar33.setObjectName("bar33")
		__class__.bar77 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar77.setGeometry(QtCore.QRect(911, 170, 12, 500))
		__class__.bar77.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar77.setProperty("value", 50)
		__class__.bar77.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar77.setTextVisible(False)
		__class__.bar77.setOrientation(QtCore.Qt.Vertical)
		__class__.bar77.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar77.setObjectName("bar77")
		__class__.bar66 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar66.setGeometry(QtCore.QRect(781, 170, 12, 500))
		__class__.bar66.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar66.setProperty("value", 50)
		__class__.bar66.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar66.setTextVisible(False)
		__class__.bar66.setOrientation(QtCore.Qt.Vertical)
		__class__.bar66.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar66.setObjectName("bar66")
		__class__.bar13 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar13.setGeometry(QtCore.QRect(156, 170, 12, 500))
		__class__.bar13.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar13.setProperty("value", 50)
		__class__.bar13.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar13.setTextVisible(False)
		__class__.bar13.setOrientation(QtCore.Qt.Vertical)
		__class__.bar13.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar13.setObjectName("bar13")
		__class__.bar9 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar9.setGeometry(QtCore.QRect(109, 170, 12, 500))
		__class__.bar9.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar9.setProperty("value", 50)
		__class__.bar9.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar9.setTextVisible(False)
		__class__.bar9.setOrientation(QtCore.Qt.Vertical)
		__class__.bar9.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar9.setObjectName("bar9")
		__class__.bar90 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar90.setGeometry(QtCore.QRect(1064, 170, 12, 500))
		__class__.bar90.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar90.setProperty("value", 50)
		__class__.bar90.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar90.setTextVisible(False)
		__class__.bar90.setOrientation(QtCore.Qt.Vertical)
		__class__.bar90.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar90.setObjectName("bar90")
		__class__.bar37 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar37.setGeometry(QtCore.QRect(439, 170, 12, 500))
		__class__.bar37.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar37.setProperty("value", 50)
		__class__.bar37.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar37.setTextVisible(False)
		__class__.bar37.setOrientation(QtCore.Qt.Vertical)
		__class__.bar37.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar37.setObjectName("bar37")
		__class__.bar84 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar84.setGeometry(QtCore.QRect(993, 170, 12, 500))
		__class__.bar84.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar84.setProperty("value", 50)
		__class__.bar84.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar84.setTextVisible(False)
		__class__.bar84.setOrientation(QtCore.Qt.Vertical)
		__class__.bar84.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar84.setObjectName("bar84")
		__class__.bar93 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar93.setGeometry(QtCore.QRect(1099, 170, 12, 500))
		__class__.bar93.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar93.setProperty("value", 50)
		__class__.bar93.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar93.setTextVisible(False)
		__class__.bar93.setOrientation(QtCore.Qt.Vertical)
		__class__.bar93.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar93.setObjectName("bar93")
		__class__.bar18 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar18.setGeometry(QtCore.QRect(215, 170, 12, 500))
		__class__.bar18.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar18.setProperty("value", 50)
		__class__.bar18.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar18.setTextVisible(False)
		__class__.bar18.setOrientation(QtCore.Qt.Vertical)
		__class__.bar18.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar18.setObjectName("bar18")
		__class__.bar97 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar97.setGeometry(QtCore.QRect(1146, 170, 12, 500))
		__class__.bar97.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar97.setProperty("value", 50)
		__class__.bar97.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar97.setTextVisible(False)
		__class__.bar97.setOrientation(QtCore.Qt.Vertical)
		__class__.bar97.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar97.setObjectName("bar97")
		__class__.bar14 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar14.setGeometry(QtCore.QRect(168, 170, 12, 500))
		__class__.bar14.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar14.setProperty("value", 50)
		__class__.bar14.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar14.setTextVisible(False)
		__class__.bar14.setOrientation(QtCore.Qt.Vertical)
		__class__.bar14.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar14.setObjectName("bar14")
		__class__.bar62 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar62.setGeometry(QtCore.QRect(734, 170, 12, 500))
		__class__.bar62.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar62.setProperty("value", 50)
		__class__.bar62.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar62.setTextVisible(False)
		__class__.bar62.setOrientation(QtCore.Qt.Vertical)
		__class__.bar62.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar62.setObjectName("bar62")
		__class__.bar91 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar91.setGeometry(QtCore.QRect(1076, 170, 12, 500))
		__class__.bar91.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar91.setProperty("value", 50)
		__class__.bar91.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar91.setTextVisible(False)
		__class__.bar91.setOrientation(QtCore.Qt.Vertical)
		__class__.bar91.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar91.setObjectName("bar91")
		__class__.bar73 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar73.setGeometry(QtCore.QRect(863, 170, 12, 500))
		__class__.bar73.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar73.setProperty("value", 50)
		__class__.bar73.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar73.setTextVisible(False)
		__class__.bar73.setOrientation(QtCore.Qt.Vertical)
		__class__.bar73.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar73.setObjectName("bar73")
		__class__.bar11 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar11.setGeometry(QtCore.QRect(132, 170, 12, 500))
		__class__.bar11.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar11.setProperty("value", 50)
		__class__.bar11.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar11.setTextVisible(False)
		__class__.bar11.setOrientation(QtCore.Qt.Vertical)
		__class__.bar11.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar11.setObjectName("bar11")
		__class__.bar5 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar5.setGeometry(QtCore.QRect(62, 170, 12, 500))
		__class__.bar5.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar5.setProperty("value", 50)
		__class__.bar5.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar5.setTextVisible(False)
		__class__.bar5.setOrientation(QtCore.Qt.Vertical)
		__class__.bar5.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar5.setObjectName("bar5")
		__class__.bar61 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar61.setGeometry(QtCore.QRect(722, 170, 12, 500))
		__class__.bar61.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar61.setProperty("value", 50)
		__class__.bar61.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar61.setTextVisible(False)
		__class__.bar61.setOrientation(QtCore.Qt.Vertical)
		__class__.bar61.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar61.setObjectName("bar61")
		__class__.bar30 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar30.setGeometry(QtCore.QRect(356, 170, 12, 500))
		__class__.bar30.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar30.setProperty("value", 50)
		__class__.bar30.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar30.setTextVisible(False)
		__class__.bar30.setOrientation(QtCore.Qt.Vertical)
		__class__.bar30.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar30.setObjectName("bar30")
		__class__.bar85 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar85.setGeometry(QtCore.QRect(1005, 170, 12, 500))
		__class__.bar85.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar85.setProperty("value", 50)
		__class__.bar85.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar85.setTextVisible(False)
		__class__.bar85.setOrientation(QtCore.Qt.Vertical)
		__class__.bar85.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar85.setObjectName("bar85")
		__class__.bar46 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar46.setGeometry(QtCore.QRect(545, 170, 12, 500))
		__class__.bar46.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar46.setProperty("value", 50)
		__class__.bar46.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar46.setTextVisible(False)
		__class__.bar46.setOrientation(QtCore.Qt.Vertical)
		__class__.bar46.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar46.setObjectName("bar46")
		__class__.bar19 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar19.setGeometry(QtCore.QRect(227, 170, 12, 500))
		__class__.bar19.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar19.setProperty("value", 50)
		__class__.bar19.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar19.setTextVisible(False)
		__class__.bar19.setOrientation(QtCore.Qt.Vertical)
		__class__.bar19.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar19.setObjectName("bar19")
		__class__.bar60 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar60.setGeometry(QtCore.QRect(710, 170, 12, 500))
		__class__.bar60.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar60.setProperty("value", 50)
		__class__.bar60.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar60.setTextVisible(False)
		__class__.bar60.setOrientation(QtCore.Qt.Vertical)
		__class__.bar60.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar60.setObjectName("bar60")
		__class__.bar68 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar68.setGeometry(QtCore.QRect(804, 170, 12, 500))
		__class__.bar68.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar68.setProperty("value", 50)
		__class__.bar68.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar68.setTextVisible(False)
		__class__.bar68.setOrientation(QtCore.Qt.Vertical)
		__class__.bar68.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar68.setObjectName("bar68")
		__class__.bar3 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar3.setGeometry(QtCore.QRect(38, 170, 12, 500))
		__class__.bar3.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar3.setProperty("value", 50)
		__class__.bar3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar3.setTextVisible(False)
		__class__.bar3.setOrientation(QtCore.Qt.Vertical)
		__class__.bar3.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar3.setObjectName("bar3")
		__class__.bar15 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar15.setGeometry(QtCore.QRect(180, 170, 12, 500))
		__class__.bar15.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar15.setProperty("value", 50)
		__class__.bar15.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar15.setTextVisible(False)
		__class__.bar15.setOrientation(QtCore.Qt.Vertical)
		__class__.bar15.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar15.setObjectName("bar15")
		__class__.bar92 = QtWidgets.QProgressBar(self.centralwidget)
		__class__.bar92.setGeometry(QtCore.QRect(1087, 170, 12, 500))
		__class__.bar92.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid black;\n"
"}")
		__class__.bar92.setProperty("value", 50)
		__class__.bar92.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
		__class__.bar92.setTextVisible(False)
		__class__.bar92.setOrientation(QtCore.Qt.Vertical)
		__class__.bar92.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
		__class__.bar92.setObjectName("bar92")
		self.comboSelect = QtWidgets.QComboBox(self.centralwidget)
		self.comboSelect.setGeometry(QtCore.QRect(520, 40, 121, 30))
		self.comboSelect.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
		self.comboSelect.setObjectName("comboSelect")
		self.comboSelect.addItem("")
		self.comboSelect.addItem("")
		self.comboSelect.addItem("")
		self.comboSelect.addItem("")
		self.comboSelect.addItem("")
		self.comboSelect.addItem("")
		self.buttonLoadFile = QtWidgets.QPushButton(self.centralwidget)
		self.buttonLoadFile.setGeometry(QtCore.QRect(390, 40, 121, 30))
		self.buttonLoadFile.setObjectName("buttonLoadFile")
		self.labelData = QtWidgets.QLabel(self.centralwidget)
		self.labelData.setGeometry(QtCore.QRect(390, 10, 121, 30))
		self.labelData.setAlignment(QtCore.Qt.AlignCenter)
		self.labelData.setObjectName("labelData")
		self.labelAlgorithm = QtWidgets.QLabel(self.centralwidget)
		self.labelAlgorithm.setGeometry(QtCore.QRect(520, 10, 121, 30))
		self.labelAlgorithm.setAlignment(QtCore.Qt.AlignCenter)
		self.labelAlgorithm.setObjectName("labelAlgorithm")
		self.buttonStart = QtWidgets.QPushButton(self.centralwidget)
		self.buttonStart.setGeometry(QtCore.QRect(520, 130, 121, 30))
		self.buttonStart.setObjectName("buttonStart")
		self.labelTime = QtWidgets.QLabel(self.centralwidget)
		self.labelTime.setGeometry(QtCore.QRect(1050, 140, 47, 16))
		self.labelTime.setAlignment(QtCore.Qt.AlignCenter)
		self.labelTime.setObjectName("labelTime")
		self.labelTimeVal = QtWidgets.QLabel(self.centralwidget)
		self.labelTimeVal.setGeometry(QtCore.QRect(1100, 140, 61, 16))
		self.labelTimeVal.setText("")
		self.labelTimeVal.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
		self.labelTimeVal.setObjectName("labelTimeVal")
		self.labelDelay = QtWidgets.QLabel(self.centralwidget)
		self.labelDelay.setGeometry(QtCore.QRect(650, 10, 121, 30))
		self.labelDelay.setAlignment(QtCore.Qt.AlignCenter)
		self.labelDelay.setObjectName("labelDelay")
		self.lebelDelayVal = QtWidgets.QLabel(self.centralwidget)
		self.lebelDelayVal.setGeometry(QtCore.QRect(650, 80, 121, 30))
		self.lebelDelayVal.setAlignment(QtCore.Qt.AlignCenter)
		self.lebelDelayVal.setObjectName("lebelDelayVal")
		MainWindow.setCentralWidget(self.centralwidget)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "Algotihim Visualizer"))
		self.buttonGenRan.setText(_translate("MainWindow", "Generate Random"))
		self.labelStatus.setText(_translate("MainWindow", "Status:"))
		self.bar48.setFormat(_translate("MainWindow", "%p"))
		self.bar45.setFormat(_translate("MainWindow", "%p"))
		self.bar1.setFormat(_translate("MainWindow", "%p"))
		self.bar38.setFormat(_translate("MainWindow", "%p"))
		self.bar64.setFormat(_translate("MainWindow", "%p"))
		self.bar34.setFormat(_translate("MainWindow", "%p"))
		self.bar32.setFormat(_translate("MainWindow", "%p"))
		self.bar28.setFormat(_translate("MainWindow", "%p"))
		self.bar44.setFormat(_translate("MainWindow", "%p"))
		self.bar98.setFormat(_translate("MainWindow", "%p"))
		self.bar2.setFormat(_translate("MainWindow", "%p"))
		self.bar56.setFormat(_translate("MainWindow", "%p"))
		self.bar49.setFormat(_translate("MainWindow", "%p"))
		self.bar99.setFormat(_translate("MainWindow", "%p"))
		self.bar26.setFormat(_translate("MainWindow", "%p"))
		self.bar12.setFormat(_translate("MainWindow", "%p"))
		self.bar17.setFormat(_translate("MainWindow", "%p"))
		self.bar16.setFormat(_translate("MainWindow", "%p"))
		self.bar23.setFormat(_translate("MainWindow", "%p"))
		self.bar69.setFormat(_translate("MainWindow", "%p"))
		self.bar81.setFormat(_translate("MainWindow", "%p"))
		self.bar59.setFormat(_translate("MainWindow", "%p"))
		self.bar43.setFormat(_translate("MainWindow", "%p"))
		self.bar95.setFormat(_translate("MainWindow", "%p"))
		self.bar89.setFormat(_translate("MainWindow", "%p"))
		self.bar75.setFormat(_translate("MainWindow", "%p"))
		self.bar70.setFormat(_translate("MainWindow", "%p"))
		self.bar42.setFormat(_translate("MainWindow", "%p"))
		self.bar41.setFormat(_translate("MainWindow", "%p"))
		self.bar22.setFormat(_translate("MainWindow", "%p"))
		self.bar31.setFormat(_translate("MainWindow", "%p"))
		self.bar39.setFormat(_translate("MainWindow", "%p"))
		self.bar63.setFormat(_translate("MainWindow", "%p"))
		self.bar88.setFormat(_translate("MainWindow", "%p"))
		self.bar7.setFormat(_translate("MainWindow", "%p"))
		self.bar35.setFormat(_translate("MainWindow", "%p"))
		self.bar54.setFormat(_translate("MainWindow", "%p"))
		self.bar65.setFormat(_translate("MainWindow", "%p"))
		self.bar55.setFormat(_translate("MainWindow", "%p"))
		self.bar47.setFormat(_translate("MainWindow", "%p"))
		self.bar40.setFormat(_translate("MainWindow", "%p"))
		self.bar74.setFormat(_translate("MainWindow", "%p"))
		self.bar4.setFormat(_translate("MainWindow", "%p"))
		self.bar36.setFormat(_translate("MainWindow", "%p"))
		self.bar58.setFormat(_translate("MainWindow", "%p"))
		self.bar72.setFormat(_translate("MainWindow", "%p"))
		self.bar51.setFormat(_translate("MainWindow", "%p"))
		self.bar87.setFormat(_translate("MainWindow", "%p"))
		self.bar79.setFormat(_translate("MainWindow", "%p"))
		self.bar94.setFormat(_translate("MainWindow", "%p"))
		self.bar71.setFormat(_translate("MainWindow", "%p"))
		self.bar50.setFormat(_translate("MainWindow", "%p"))
		self.bar10.setFormat(_translate("MainWindow", "%p"))
		self.bar96.setFormat(_translate("MainWindow", "%p"))
		self.bar8.setFormat(_translate("MainWindow", "%p"))
		self.bar21.setFormat(_translate("MainWindow", "%p"))
		self.bar25.setFormat(_translate("MainWindow", "%p"))
		self.bar100.setFormat(_translate("MainWindow", "%p"))
		self.bar80.setFormat(_translate("MainWindow", "%p"))
		self.bar29.setFormat(_translate("MainWindow", "%p"))
		self.bar78.setFormat(_translate("MainWindow", "%p"))
		self.bar86.setFormat(_translate("MainWindow", "%p"))
		self.bar67.setFormat(_translate("MainWindow", "%p"))
		self.bar52.setFormat(_translate("MainWindow", "%p"))
		self.bar82.setFormat(_translate("MainWindow", "%p"))
		self.bar24.setFormat(_translate("MainWindow", "%p"))
		self.bar20.setFormat(_translate("MainWindow", "%p"))
		self.bar76.setFormat(_translate("MainWindow", "%p"))
		self.bar27.setFormat(_translate("MainWindow", "%p"))
		self.bar83.setFormat(_translate("MainWindow", "%p"))
		self.bar57.setFormat(_translate("MainWindow", "%p"))
		self.bar6.setFormat(_translate("MainWindow", "%p"))
		self.bar53.setFormat(_translate("MainWindow", "%p"))
		self.bar33.setFormat(_translate("MainWindow", "%p"))
		self.bar77.setFormat(_translate("MainWindow", "%p"))
		self.bar66.setFormat(_translate("MainWindow", "%p"))
		self.bar13.setFormat(_translate("MainWindow", "%p"))
		self.bar9.setFormat(_translate("MainWindow", "%p"))
		self.bar90.setFormat(_translate("MainWindow", "%p"))
		self.bar37.setFormat(_translate("MainWindow", "%p"))
		self.bar84.setFormat(_translate("MainWindow", "%p"))
		self.bar93.setFormat(_translate("MainWindow", "%p"))
		self.bar18.setFormat(_translate("MainWindow", "%p"))
		self.bar97.setFormat(_translate("MainWindow", "%p"))
		self.bar14.setFormat(_translate("MainWindow", "%p"))
		self.bar62.setFormat(_translate("MainWindow", "%p"))
		self.bar91.setFormat(_translate("MainWindow", "%p"))
		self.bar73.setFormat(_translate("MainWindow", "%p"))
		self.bar11.setFormat(_translate("MainWindow", "%p"))
		self.bar5.setFormat(_translate("MainWindow", "%p"))
		self.bar61.setFormat(_translate("MainWindow", "%p"))
		self.bar30.setFormat(_translate("MainWindow", "%p"))
		self.bar85.setFormat(_translate("MainWindow", "%p"))
		self.bar46.setFormat(_translate("MainWindow", "%p"))
		self.bar19.setFormat(_translate("MainWindow", "%p"))
		self.bar60.setFormat(_translate("MainWindow", "%p"))
		self.bar68.setFormat(_translate("MainWindow", "%p"))
		self.bar3.setFormat(_translate("MainWindow", "%p"))
		self.bar15.setFormat(_translate("MainWindow", "%p"))
		self.bar92.setFormat(_translate("MainWindow", "%p"))
		self.comboSelect.setItemText(0, _translate("MainWindow", "Shell Sort"))
		self.comboSelect.setItemText(1, _translate("MainWindow", "Insertion Sort"))
		self.comboSelect.setItemText(2, _translate("MainWindow", "Radix Sort"))
		self.comboSelect.setItemText(3, _translate("MainWindow", "Selection Sort"))
		self.comboSelect.setItemText(4, _translate("MainWindow", "Bubble Sort"))
		self.comboSelect.setItemText(5, _translate("MainWindow", "Comb Sort"))
		self.labelDelay.setText(_translate("MainWindow", "Delay (ms)"))
		self.lebelDelayVal.setText(_translate("MainWindow", "0.1"))
		self.buttonLoadFile.setText(_translate("MainWindow", "Load From File"))
		self.labelData.setText(_translate("MainWindow", "Data to sort"))
		self.labelAlgorithm.setText(_translate("MainWindow", "Sorting algorithm"))
		self.buttonStart.setText(_translate("MainWindow", "START"))
		self.labelTime.setText(_translate("MainWindow", "Time:"))
		self.labelTimeVal.setText(_translate("MainWindow", "0s"))

		self.buttonLoadFile.clicked.connect(self.loadFile)
		self.buttonGenRan.clicked.connect(self.generateRandom)
		self.buttonStart.clicked.connect(self.startSort)
		self.sliderDelay.valueChanged.connect(self.updateDelay)

	data = []
	delay = 0.001

	# updates delay
	def updateDelay(self):
		self.delay = self.sliderDelay.value() / 1000
		self.lebelDelayVal.setText(str(self.sliderDelay.value()))

	# opens file explorer and passes file name for loading
	def loadFile(self):
		fileFilter = "Text Files (*.txt);;All Files (*.*)"
		fileName = QFileDialog.getOpenFileName(caption="Select file with data", directory=".", filter=fileFilter)

		if fileName[0] == "":
			pass
		else:
			self.data = tools.readData(fileName[0])
		self.setupBars()

	# calling function to generate random data
	def generateRandom(self):
		self.data = tools.generateRandomArray()
		self.setupBars()

	# runs sorting and saves sorted data
	def startSort(self):
		barArr = [self.bar1, self.bar2, self.bar3, self.bar4, self.bar5, self.bar6, self.bar7, self.bar8, self.bar9, self.bar10, self.bar11, self.bar12, self.bar13, self.bar14, self.bar15, self.bar16, self.bar17, self.bar18, self.bar19, self.bar20, self.bar21, self.bar22, self.bar23, self.bar24, self.bar25, self.bar26, self.bar27, self.bar28, self.bar29, self.bar30, self.bar31, self.bar32, self.bar33, self.bar34, self.bar35, self.bar36, self.bar37, self.bar38, self.bar39, self.bar40, self.bar41, self.bar42, self.bar43, self.bar44, self.bar45, self.bar46, self.bar47, self.bar48, self.bar49, self.bar50, self.bar51, self.bar52, self.bar53, self.bar54, self.bar55, self.bar56, self.bar57, self.bar58, self.bar59, self.bar60, self.bar61, self.bar62, self.bar63, self.bar64, self.bar65, self.bar66, self.bar67, self.bar68, self.bar69, self.bar70, self.bar71, self.bar72, self.bar73, self.bar74, self.bar75, self.bar76, self.bar77, self.bar78, self.bar79, self.bar80, self.bar81, self.bar82, self.bar83, self.bar84, self.bar85, self.bar86, self.bar87, self.bar88, self.bar89, self.bar90, self.bar91, self.bar92, self.bar93, self.bar94, self.bar95, self.bar96, self.bar97, self.bar98, self.bar99, self.bar100]

		algo = str(self.comboSelect.currentText())

		if algo == "Shell Sort":
			self.labelStatusVal.setText("Sorting with Shell Sort...")
			startTime = time.time()
			self.data = algorithms.Algorithms.ShellSort(self.delay)
			self.labelTimeVal.setText(str(round(time.time() - startTime, 2)) + "s")
			self.labelStatusVal.setText("Idle")
		elif algo == "Insertion Sort":
			self.labelStatusVal.setText("Sorting with Insertion Sort...")
			startTime = time.time()
			self.data = algorithms.Algorithms.InsertionSort(self.delay)
			self.labelTimeVal.setText(str(round(time.time() - startTime, 2)) + "s")
			self.labelStatusVal.setText("Idle")
		elif algo == "Radix Sort":
			self.labelStatusVal.setText("Sorting with Radix Sort...")
			startTime = time.time()
			self.data = algorithms.Algorithms.radixSortHelper(self.delay)
			self.labelTimeVal.setText(str(round(time.time() - startTime, 2)) + "s")
			self.labelStatusVal.setText("Idle")
		elif algo == "Selection Sort":
			self.labelStatusVal.setText("Sorting with Selection Sort....")
			startTime = time.time()
			self.data = algorithms.Algorithms.SelectionSort(self.delay)
			self.labelTimeVal.setText(str(round(time.time() - startTime, 2)) + "s")
			self.labelStatusVal.setText("Idle")
		elif algo == "Bubble Sort":
			self.labelStatusVal.setText("Sorting with Bubble Sort...")
			startTime = time.time()
			self.data = algorithms.Algorithms.BubbleSort(self.delay)
			self.labelTimeVal.setText(str(round(time.time() - startTime, 2)) + "s")
			self.labelStatusVal.setText("Idle")
		elif algo == "Comb Sort":
			self.labelStatusVal.setText("Sorting with Comb Sort...")
			startTime = time.time()
			self.data = algorithms.Algorithms.CombSort(self.delay)
			self.labelTimeVal.setText(str(round(time.time() - startTime, 2)) + "s")
			self.labelStatusVal.setText("Idle")

		tools.saveSorted(self.data)

	# sets up the bars with loaded data
	def setupBars(self):
		self.labelStatusVal.setText("Setting up bars...")

		bars = [self.bar1, self.bar2, self.bar3, self.bar4, self.bar5, self.bar6, self.bar7, self.bar8, self.bar9, self.bar10, self.bar11, self.bar12, self.bar13, self.bar14, self.bar15, self.bar16, self.bar17, self.bar18, self.bar19, self.bar20, self.bar21, self.bar22, self.bar23, self.bar24, self.bar25, self.bar26, self.bar27, self.bar28, self.bar29, self.bar30, self.bar31, self.bar32, self.bar33, self.bar34, self.bar35, self.bar36, self.bar37, self.bar38, self.bar39, self.bar40, self.bar41, self.bar42, self.bar43, self.bar44, self.bar45, self.bar46, self.bar47, self.bar48, self.bar49, self.bar50, self.bar51, self.bar52, self.bar53, self.bar54, self.bar55, self.bar56, self.bar57, self.bar58, self.bar59, self.bar60, self.bar61, self.bar62, self.bar63, self.bar64, self.bar65, self.bar66, self.bar67, self.bar68, self.bar69, self.bar70, self.bar71, self.bar72, self.bar73, self.bar74, self.bar75, self.bar76, self.bar77, self.bar78, self.bar79, self.bar80, self.bar81, self.bar82, self.bar83, self.bar84, self.bar85, self.bar86, self.bar87, self.bar88, self.bar89, self.bar90, self.bar91, self.bar92, self.bar93, self.bar94, self.bar95, self.bar96, self.bar97, self.bar98, self.bar99, self.bar100]

		for i in range(len(bars)):
			bars[i].setValue(self.data[i])
			time.sleep(self.delay)

		self.labelStatusVal.setText("Idle")