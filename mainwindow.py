# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(585, 610)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setEnabled(True)
        self.page.setObjectName("page")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fileNameLabel = QtWidgets.QLabel(self.page)
        self.fileNameLabel.setEnabled(True)
        self.fileNameLabel.setObjectName("fileNameLabel")
        self.verticalLayout.addWidget(self.fileNameLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_9 = QtWidgets.QLabel(self.page)
        self.label_9.setEnabled(True)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.originalList = QtWidgets.QListWidget(self.page)
        self.originalList.setEnabled(True)
        self.originalList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.originalList.setObjectName("originalList")
        self.verticalLayout_3.addWidget(self.originalList)
        self.label_10 = QtWidgets.QLabel(self.page)
        self.label_10.setEnabled(True)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        self.originalRowCount = QtWidgets.QSpinBox(self.page)
        self.originalRowCount.setEnabled(True)
        self.originalRowCount.setReadOnly(True)
        self.originalRowCount.setMaximum(999999999)
        self.originalRowCount.setObjectName("originalRowCount")
        self.verticalLayout_3.addWidget(self.originalRowCount)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.addButton = QtWidgets.QPushButton(self.page)
        self.addButton.setEnabled(True)
        self.addButton.setObjectName("addButton")
        self.verticalLayout_4.addWidget(self.addButton)
        self.removeButton = QtWidgets.QPushButton(self.page)
        self.removeButton.setEnabled(True)
        self.removeButton.setObjectName("removeButton")
        self.verticalLayout_4.addWidget(self.removeButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_13 = QtWidgets.QLabel(self.page)
        self.label_13.setEnabled(True)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_5.addWidget(self.label_13)
        self.newList = QtWidgets.QListWidget(self.page)
        self.newList.setEnabled(True)
        self.newList.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.newList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.newList.setObjectName("newList")
        self.verticalLayout_5.addWidget(self.newList)
        self.label_14 = QtWidgets.QLabel(self.page)
        self.label_14.setEnabled(True)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_5.addWidget(self.label_14)
        self.newRowCount = QtWidgets.QSpinBox(self.page)
        self.newRowCount.setEnabled(True)
        self.newRowCount.setMaximum(999999999)
        self.newRowCount.setObjectName("newRowCount")
        self.verticalLayout_5.addWidget(self.newRowCount)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.page_2)
        self.label_6.setEnabled(True)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.page_2)
        self.label_7.setEnabled(True)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_6.addWidget(self.label_7)
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setEnabled(True)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.page_2)
        self.label_5.setEnabled(True)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setOpenExternalLinks(True)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.label = QtWidgets.QLabel(self.page_2)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.label_11 = QtWidgets.QLabel(self.page_2)
        self.label_11.setEnabled(True)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_6.addWidget(self.label_11)
        self.textBrowser = QtWidgets.QTextBrowser(self.page_2)
        self.textBrowser.setEnabled(True)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_6.addWidget(self.textBrowser)
        self.doneButton = QtWidgets.QPushButton(self.page_2)
        self.doneButton.setEnabled(True)
        self.doneButton.setObjectName("doneButton")
        self.verticalLayout_6.addWidget(self.doneButton)
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 585, 33))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_csv = QtWidgets.QAction(MainWindow)
        self.actionOpen_csv.setObjectName("actionOpen_csv")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSave_csv = QtWidgets.QAction(MainWindow)
        self.actionSave_csv.setObjectName("actionSave_csv")
        self.menuFile.addAction(self.actionOpen_csv)
        self.menuFile.addAction(self.actionSave_csv)
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CSV Editor"))
        self.page.setToolTip(_translate("MainWindow", "Open a file to begin"))
        self.fileNameLabel.setText(_translate("MainWindow", "File name"))
        self.label_9.setText(_translate("MainWindow", "Original Columns"))
        self.label_10.setText(_translate("MainWindow", "Original row count"))
        self.addButton.setText(_translate("MainWindow", ">>"))
        self.removeButton.setText(_translate("MainWindow", "<<"))
        self.label_13.setText(_translate("MainWindow", "New Columns"))
        self.label_14.setText(_translate("MainWindow", "New row count"))
        self.label_6.setText(_translate("MainWindow", "Version"))
        self.label_7.setText(_translate("MainWindow", "CSV Editor v0.1"))
        self.label_4.setText(_translate("MainWindow", "Homepage"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><a href=\"https://github.com/ScriptSmith/csveditor\"><span style=\" text-decoration: underline; color:#0000ff;\">https://github.com/ScriptSmith/csveditor</span></a></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Icon Source"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><a href=\"https://icons8.com\"><span style=\" text-decoration: underline; color:#0000ff;\">https://icons8.com</span></a></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "License"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">You should have received a copy of the GNU General Public License along with this program.  If not, see <a href=\"http://www.gnu.org/licenses\"><span style=\" text-decoration: underline; color:#0000ff;\">http://www.gnu.org/licenses</span></a>.</p></body></html>"))
        self.doneButton.setText(_translate("MainWindow", "Done"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen_csv.setText(_translate("MainWindow", "Open"))
        self.actionOpen_csv.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionSave_csv.setText(_translate("MainWindow", "Save As"))
        self.actionSave_csv.setShortcut(_translate("MainWindow", "Ctrl+S"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

