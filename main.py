import sys, os
from PyQt4 import QtGui
from welcomeview import *
from directoryview import *
from sportsview import *
from newsview import *
from emailview import *
from mapview import *
from labview import *

app = QtGui.QApplication(sys.argv)
window = QtGui.QMainWindow()
dialog = QtGui.QDialog()
ui = WelcomeView()
ui.setupUi(window)
directoryView = DirectoryView()
directoryView.setupUi(QtGui.QDialog())
sportsView = SportsView()
sportsView.setupUi(QtGui.QDialog())
newsView = NewsView()
newsView.setupUi(QtGui.QDialog())
emailView = EmailView()
emailView.setupUi(QtGui.QDialog())
mapView = MapView()
mapView.setupUi(QtGui.QDialog())
labView = LabView()
labView.setupUi(QtGui.QDialog())

ui.directoryButton.connect(ui.directoryButton, QtCore.SIGNAL("clicked()"), directoryView.helper.showPage)
ui.sportsButton.connect(ui.sportsButton, QtCore.SIGNAL("clicked()"), sportsView.helper.showPage)
ui.newsButton.connect(ui.newsButton, QtCore.SIGNAL("clicked()"), newsView.helper.showPage)
ui.mailButton.connect(ui.mailButton, QtCore.SIGNAL("clicked()"), emailView.helper.showPage)
ui.mapButton.connect(ui.mapButton, QtCore.SIGNAL("clicked()"), mapView.helper.showPage)
ui.labButton.connect(ui.labButton, QtCore.SIGNAL("clicked()"), labView.helper.showPage)
#temp button to close program
ui.exit.connect(ui.exit, QtCore.SIGNAL("clicked()"), window.close)
#test = QtGui.QCursor(QtGui.QPixmap(os.getcwd()+"/images/finger.png"), 126, 31)
#app.setOverrideCursor(test)

window.show()
sys.exit(app.exec_())
