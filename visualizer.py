import sys
import ui

if __name__ == "__main__":
	app = ui.QtWidgets.QApplication(sys.argv)
	MainWindow = ui.QtWidgets.QMainWindow()
	ui = ui.Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())