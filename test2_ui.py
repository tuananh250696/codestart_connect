from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class Ui_Form(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1024, 600)
        self.TEXT = QtWidgets.QTextBrowser(Dialog)
        self.TEXT.setGeometry(QtCore.QRect(890, 30, 131, 81))
        self.TEXT.setObjectName("TEXT")
        self.imgLabel = QtWidgets.QLabel(Dialog)
        self.imgLabel.setGeometry(QtCore.QRect(275, 115, 743, 483))
        self.imgLabel.setAutoFillBackground(False)
        self.imgLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.imgLabel.setText("")
        self.imgLabel.setObjectName("imgLabel")

        self.CAPTURE = QtWidgets.QPushButton(Dialog)
        self.CAPTURE.setGeometry(QtCore.QRect(200, 30, 181, 81))
        self.CAPTURE.setObjectName("CAPTURE")

        self.imgLabel_2 = QtWidgets.QLabel(Dialog)
        self.imgLabel_2.setGeometry(QtCore.QRect(0, 0, 1922, 30))
        self.imgLabel_2.setAutoFillBackground(False)
        self.imgLabel_2.setFrameShape(QtWidgets.QFrame.Box)
        self.imgLabel_2.setText("")
        self.imgLabel_2.setPixmap(QtGui.QPixmap("ngang1.png"))
        self.imgLabel_2.setObjectName("imgLabel_2")
        # creating a combo box for selecting camera
        self.camera_selector1 = QtWidgets.QComboBox(Dialog)
        self.camera_selector1.setGeometry(QtCore.QRect(550, 30, 171, 81))
        # adding status tip to it
        # self.camera_selector1.addItems("TỰ động chụp")
        # self.camera_selector1.setToolTip("TỰ động chụp")

        # creating a combo box for selecting camera
        self.camera_selector = QtWidgets.QComboBox(Dialog)
        self.camera_selector.setGeometry(QtCore.QRect(0, 30, 201, 81))
        # adding status tip to it
        self.camera_selector.setStatusTip("Choose camera to take pictures")

        # adding tool tip to it
        self.camera_selector.setToolTip("Select Camera")
        self.camera_selector.setToolTipDuration(2500)

        self.NEXT_3 = QtWidgets.QPushButton(Dialog)
        self.NEXT_3.setGeometry(QtCore.QRect(380, 30, 171, 81))
        self.NEXT_3.setObjectName("NEXT_3")
        self.NEXT_7 = QtWidgets.QPushButton(Dialog)
        self.NEXT_7.setGeometry(QtCore.QRect(720, 30, 171, 81))
        self.NEXT_7.setObjectName("NEXT_7")

        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(2, 115, 270, 475))#(2, 115, 213, 475))
        self.listWidget.setObjectName("ListWidgetItem")
        self.listWidget.setIconSize(QtCore.QSize(188, 190))
        self.listWidget.setResizeMode(QtWidgets.QListView.Adjust)
        self.listWidget.setFlow(QtWidgets.QListView.TopToBottom)

        #         self.camera_selector3 = QtWidgets.QComboBox(self.listWidget)
        #         self.camera_selector3.setGeometry(QtCore.QRect(2, 2, 220, 60))

       #  self.check1 = QtWidgets.QCheckBox("Football")
       #  self.check1.setIcon(QtGui.QIcon('demo.png'))
       #  self.check1.setIconSize(QtGui.QSize(40, 40))
       #  self.check1.setFont(QtGui.QFont("Sanserif", 13))
       #  self.listWidget.addWidget(self.check1)
       #  #self.check1.setFont(QtGui.QFont("Sanserif", 13))
       # # hbox.addWidget(self.check1)
       #  self.listWidget.itemEntered.connect(
       #      lambda item: item.setCheckState(Qt.Checked if item.checkState() == Qt.Unchecked else  Qt.Unchecked))
        self.item = QListWidgetItem("Item ")
        font = QFont('Times', 14)
        self.item.setFont(font)
        self.item.setCheckState(QtCore.Qt.Unchecked)
        # self.item.setCheckable(True)
        #self.item.setChetateckS(False)
        self.listWidget.addItem(self.item)
        self.it  = QtWidgets.QListWidgetItem(self.listWidget)
#        self.item.clicked.connect(self.w1)

        item1 = QListWidgetItem("Item ")
        item1.setCheckState(QtCore.Qt.Unchecked)
        #item1.setCheckState(False)
        self.listWidget.addItem(item1)
        self.it1 = QtWidgets.QListWidgetItem(self.listWidget)

        item2 = QListWidgetItem("Item ")
        item2.setCheckState(Qt.Checked)
        item2.setCheckState(False)
        self.listWidget.addItem(item2)
        self.it2 = QtWidgets.QListWidgetItem(self.listWidget)

        item3 = QListWidgetItem("Item ")
        item3.setCheckState(Qt.Checked)
        item3.setCheckState(False)
        self.listWidget.addItem(item3)
        self.it3 = QtWidgets.QListWidgetItem(self.listWidget)

        item4 = QListWidgetItem("Item ")
        item4.setCheckState(Qt.Checked)
        item4.setCheckState(False)
        self.listWidget.addItem(item4)
        self.it4 = QtWidgets.QListWidgetItem(self.listWidget)

        item5 = QListWidgetItem("Item ")
        item5.setCheckState(Qt.Checked)
        item5.setCheckState(False)
        self.listWidget.addItem(item5)
        self.it5 = QtWidgets.QListWidgetItem(self.listWidget)

        item6 = QListWidgetItem("Item ")
        item6.setCheckState(Qt.Checked)
        item6.setCheckState(False)
        self.listWidget.addItem(item6)
        self.it6 = QtWidgets.QListWidgetItem(self.listWidget)

        item7 = QListWidgetItem("Item ")
        item7.setCheckState(Qt.Checked)
        item7.setCheckState(False)
        self.listWidget.addItem(item7)
        self.it7 = QtWidgets.QListWidgetItem(self.listWidget)

        item8 = QListWidgetItem("Item ")
        item8.setCheckState(Qt.Checked)
        item8.setCheckState(False)
        self.listWidget.addItem(item8)
        self.it8 = QtWidgets.QListWidgetItem(self.listWidget)

        item9 = QListWidgetItem("Item ")
        item9.setCheckState(Qt.Checked)
        item9.setCheckState(False)
        self.listWidget.addItem(item9)
        self.it9 = QtWidgets.QListWidgetItem(self.listWidget)

        item10 = QListWidgetItem("Item ")
        item10.setCheckState(Qt.Checked)
        item10.setCheckState(False)
        self.listWidget.addItem(item10)
        self.it10 = QtWidgets.QListWidgetItem(self.listWidget)

        item11 = QListWidgetItem("Item ")
        item11.setCheckState(Qt.Checked)
        item11.setCheckState(False)
        self.listWidget.addItem(item11)
        self.it11 = QtWidgets.QListWidgetItem(self.listWidget)

        item12 = QListWidgetItem("Item ")
        item12.setCheckState(Qt.Checked)
        item12.setCheckState(False)
        self.listWidget.addItem(item12)
        self.it12 = QtWidgets.QListWidgetItem(self.listWidget)

        item13 = QListWidgetItem("Item ")
        item13.setCheckState(Qt.Checked)
        item13.setCheckState(False)
        self.listWidget.addItem(item13)
        self.it13 = QtWidgets.QListWidgetItem(self.listWidget)

        item14 = QListWidgetItem("Item ")
        item14.setCheckState(Qt.Checked)
        item14.setCheckState(False)
        self.listWidget.addItem(item14)
        self.it14 = QtWidgets.QListWidgetItem(self.listWidget)

        item15 = QListWidgetItem("Item ")
        item15.setCheckState(Qt.Checked)
        item15.setCheckState(False)
        self.listWidget.addItem(item15)
        self.it15 = QtWidgets.QListWidgetItem(self.listWidget)

        item16 = QListWidgetItem("Item ")
        item16.setCheckState(Qt.Checked)
        item16.setCheckState(False)
        self.listWidget.addItem(item16)
        self.it16 = QtWidgets.QListWidgetItem(self.listWidget)

        item17 = QListWidgetItem("Item ")
        item17.setCheckState(Qt.Checked)
        item17.setCheckState(False)
        self.listWidget.addItem(item17)
        self.it17 = QtWidgets.QListWidgetItem(self.listWidget)

        self.TEXT.raise_()
        self.imgLabel.raise_()
        #         self.checkBox_4.raise_()

        self.imgLabel_2.raise_()
        self.CAPTURE.raise_()
        self.NEXT_3.raise_()
        self.NEXT_7.raise_()

        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.CAPTURE.setText(_translate("Dialog", "Chụp Ảnh"))
        self.NEXT_3.setText(_translate("Dialog", "Chẩn Đoán"))
        self.NEXT_7.setText(_translate("Dialog", "Đóng"))

