from PyQt4.QtCore import *
from PyQt4.QtGui import *
from random import randint

class CustomListBox(QListView):
    def __init__(self, parent=None):
        QListView.__init__(self, parent)
        self.buildModel()
        self.setModel(self.model)
        #bind event for clicking a row (FML)
        self.connect(self, SIGNAL("clicked(QModelIndex)"), \
            self.clickHandler)

    def buildModel(self):
        self.model = QStandardItemModel()
        
        #generate background gradient
        grad = QLinearGradient(0,0,0,75)
        grad.setColorAt(0, QColor('gray'))
        grad.setColorAt(1, QColor('black'))

        for n in range(25):                   
            item = QStandardItem('Item %s' % randint(1, 100))
            item.setForeground(QColor('gold'))
            item.setBackground(grad)
            item.setSizeHint(QSize(200,50))
            item.setTextAlignment(Qt.AlignCenter)
            item.setFont(QFont(QString('helvetica'), 20, 75, False))
            item.setEditable(False)
            self.model.appendRow(item)

    def clickHandler(self, event):
        print "You clicked item %i" % event.row()

if __name__ == "__main__":
    import sys
    from PyQt4.QtGui import QApplication
    app = QApplication(sys.argv)
    widget = CustomListBox()
    widget.show()
    sys.exit(app.exec_())
