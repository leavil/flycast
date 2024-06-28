# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon 



class View(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(QtCore.QSize(600,110))
        MainWindow.setMaximumSize(QtCore.QSize(600, 200))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background:rgb(91,90,90);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_top = QtWidgets.QFrame(self.centralwidget)
        self.frame_top.setMaximumSize(QtCore.QSize(16777215, 55))
        self.frame_top.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_top.setObjectName("frame_top")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_top)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_toodle = QtWidgets.QFrame(self.frame_top)
        self.frame_toodle.setMinimumSize(QtCore.QSize(80, 55))
        self.frame_toodle.setMaximumSize(QtCore.QSize(80, 55))
        self.frame_toodle.setStyleSheet("background:rgb(0,143,150);")
        self.frame_toodle.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_toodle.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_toodle.setObjectName("frame_toodle")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_toodle)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.toodle = QtWidgets.QPushButton(self.frame_toodle)
        self.toodle.setMinimumSize(QtCore.QSize(80, 55))
        self.toodle.setMaximumSize(QtCore.QSize(80, 55))
        self.toodle.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(0,178,178);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(0,0,0,0);\n"
"}")
        self.toodle.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("src/icons/1x/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toodle.setIcon(icon)
        self.toodle.setIconSize(QtCore.QSize(22, 12))
        self.toodle.setFlat(True)
        self.toodle.setObjectName("toodle")
        self.horizontalLayout_3.addWidget(self.toodle)
        self.horizontalLayout.addWidget(self.frame_toodle)
        self.frame_top_east = QtWidgets.QFrame(self.frame_top)
        self.frame_top_east.setMaximumSize(QtCore.QSize(16777215, 55))
        self.frame_top_east.setStyleSheet("background:rgb(51,51,51);")
        self.frame_top_east.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_east.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_top_east.setObjectName("frame_top_east")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_top_east)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_appname = QtWidgets.QFrame(self.frame_top_east)
        self.frame_appname.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_appname.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_appname.setObjectName("frame_appname")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_appname)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(7)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_4.addWidget(self.frame_appname)
        self.frame_user = QtWidgets.QFrame(self.frame_top_east)
        self.frame_user.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_user.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_user.setObjectName("frame_user")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_user)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem)
        self.lab_appname = QtWidgets.QLabel(self.frame_user)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(24)
        self.lab_appname.setFont(font)
        self.lab_appname.setStyleSheet("color:rgb(255,255,255);")
        self.lab_appname.setObjectName("lab_appname")
        self.horizontalLayout_9.addWidget(self.lab_appname)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem1)
        self.lab_user = QtWidgets.QLabel(self.frame_user)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(24)
        self.lab_user.setFont(font)
        self.lab_user.setStyleSheet("color:rgb(255,255,255);")
        self.lab_user.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lab_user.setObjectName("lab_user")
        self.horizontalLayout_9.addWidget(self.lab_user)
        self.horizontalLayout_4.addWidget(self.frame_user)
        self.frame_person = QtWidgets.QFrame(self.frame_top_east)
        self.frame_person.setMinimumSize(QtCore.QSize(55, 55))
        self.frame_person.setMaximumSize(QtCore.QSize(55, 55))
        self.frame_person.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_person.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_person.setObjectName("frame_person")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_person)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lab_person = QtWidgets.QLabel(self.frame_person)
        self.lab_person.setMaximumSize(QtCore.QSize(55, 55))
        self.lab_person.setText("")
        self.lab_person.setPixmap(QtGui.QPixmap("src/icons/1x/user.png"))
        self.lab_person.setScaledContents(False)
        self.lab_person.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_person.setObjectName("lab_person")
        self.horizontalLayout_8.addWidget(self.lab_person)
        self.horizontalLayout_4.addWidget(self.frame_person)
        self.frame_max = QtWidgets.QFrame(self.frame_top_east)
        self.frame_max.setMinimumSize(QtCore.QSize(55, 55))
        self.frame_max.setMaximumSize(QtCore.QSize(55, 55))
        self.frame_max.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_max.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_max.setObjectName("frame_max")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_max)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.bn_min = QtWidgets.QPushButton(self.frame_max)
        self.bn_min.setMaximumSize(QtCore.QSize(55, 55))
        self.bn_min.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(0,0,0,0);\n"
"}")
        self.bn_min.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("src/icons/1x/hideAsset 53.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bn_min.setIcon(icon1)
        self.bn_min.setIconSize(QtCore.QSize(22, 22))
        self.bn_min.setFlat(True)
        self.bn_min.setObjectName("bn_min")
        self.horizontalLayout_6.addWidget(self.bn_min)
        self.horizontalLayout_4.addWidget(self.frame_max)
        self.frame_close = QtWidgets.QFrame(self.frame_top_east)
        self.frame_close.setMinimumSize(QtCore.QSize(55, 55))
        self.frame_close.setMaximumSize(QtCore.QSize(55, 55))
        self.frame_close.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_close.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_close.setObjectName("frame_close")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_close)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.bn_close = QtWidgets.QPushButton(self.frame_close)
        self.bn_close.setMaximumSize(QtCore.QSize(55, 55))
        self.bn_close.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(0,0,0,0);\n"
"}")
        self.bn_close.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("src/icons/1x/closeAsset 43.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bn_close.setIcon(icon2)
        self.bn_close.setIconSize(QtCore.QSize(22, 22))
        self.bn_close.setFlat(True)
        self.bn_close.setObjectName("bn_close")
        self.horizontalLayout_5.addWidget(self.bn_close)
        self.horizontalLayout_4.addWidget(self.frame_close)
        self.horizontalLayout.addWidget(self.frame_top_east)
        self.verticalLayout.addWidget(self.frame_top)
        self.frame_bottom = QtWidgets.QFrame(self.centralwidget)
        self.frame_bottom.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_bottom.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_bottom.setObjectName("frame_bottom")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_bottom)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_bottom_east = QtWidgets.QFrame(self.frame_bottom)
        self.frame_bottom_east.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_bottom_east.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_bottom_east.setObjectName("frame_bottom_east")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_bottom_east)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_top_2 = QtWidgets.QFrame(self.frame_bottom_east)
        self.frame_top_2.setEnabled(True)
        self.frame_top_2.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_top_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_top_2.setStyleSheet("background:rgb(51,51,51);")
        self.frame_top_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_top_2.setObjectName("frame_top_2")
        self.verticalLayout_2.addWidget(self.frame_top_2)
        self.panelfront = QtWidgets.QFrame(self.frame_bottom_east)
        self.panelfront.setObjectName("panelfront")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.panelfront)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.home = QtWidgets.QFrame(self.panelfront)
        self.home.setStyleSheet("background:rgb(51,51,51);")
        self.home.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.home.setFrameShadow(QtWidgets.QFrame.Raised)
        self.home.setObjectName("home")
        self.bn_home = QtWidgets.QPushButton(self.home)
        self.bn_home.setEnabled(True)
        self.bn_home.setGeometry(QtCore.QRect(0, 0, 141, 80))
        self.bn_home.setMinimumSize(QtCore.QSize(80, 80))
        self.bn_home.setMaximumSize(QtCore.QSize(160, 55))
        self.bn_home.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(0,0,0,0);\n"
"}")
        self.bn_home.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("src/icons/1x/homeAsset 46.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bn_home.setIcon(icon3)
        self.bn_home.setIconSize(QtCore.QSize(22, 22))
        self.bn_home.setFlat(True)
        self.bn_home.setObjectName("bn_home")
        self.horizontalLayout_14.addWidget(self.home)
        self.plane = QtWidgets.QFrame(self.panelfront)
        self.plane.setStyleSheet("background:rgb(51,51,51);")
        self.plane.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.plane.setFrameShadow(QtWidgets.QFrame.Raised)
        self.plane.setObjectName("plane")
        self.bn_plane = QtWidgets.QPushButton(self.plane)
        self.bn_plane.setGeometry(QtCore.QRect(0, 0, 141, 80))
        self.bn_plane.setMinimumSize(QtCore.QSize(80, 80))
        self.bn_plane.setMaximumSize(QtCore.QSize(160, 55))
        self.bn_plane.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(0,0,0,0);\n"
"}")
        self.bn_plane.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("src/icons/1x/planewhitebig.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bn_plane.setIcon(icon4)
        self.bn_plane.setIconSize(QtCore.QSize(22, 22))
        self.bn_plane.setFlat(True)
        self.bn_plane.setObjectName("bn_plane")
        self.horizontalLayout_14.addWidget(self.plane)
        self.weather = QtWidgets.QFrame(self.panelfront)
        self.weather.setStyleSheet("background:rgb(51,51,51);")
        self.weather.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.weather.setFrameShadow(QtWidgets.QFrame.Raised)
        self.weather.setObjectName("weather")
        self.bn_weather = QtWidgets.QPushButton(self.weather)
        self.bn_weather.setGeometry(QtCore.QRect(0, 0, 141, 80))
        self.bn_weather.setMinimumSize(QtCore.QSize(80, 80))
        self.bn_weather.setMaximumSize(QtCore.QSize(160, 80))
        self.bn_weather.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(0,0,0,0);\n"
"}")
        self.bn_weather.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("src/icons/1x/worldAsset 60.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bn_weather.setIcon(icon5)
        self.bn_weather.setIconSize(QtCore.QSize(20, 22))
        self.bn_weather.setFlat(True)
        self.bn_weather.setObjectName("bn_weather")
        self.horizontalLayout_14.addWidget(self.weather)
        self.settings = QtWidgets.QFrame(self.panelfront)
        self.settings.setStyleSheet("background:rgb(51,51,51);")
        self.settings.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.settings.setFrameShadow(QtWidgets.QFrame.Raised)
        self.settings.setObjectName("settings")
        self.bn_settings = QtWidgets.QPushButton(self.settings)
        self.bn_settings.setGeometry(QtCore.QRect(0, 0, 141, 80))
        self.bn_settings.setMinimumSize(QtCore.QSize(80, 80))
        self.bn_settings.setMaximumSize(QtCore.QSize(160, 55))
        self.bn_settings.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(0,0,0,0);\n"
"}")
        self.bn_settings.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("src/icons/1x/settAsset 50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bn_settings.setIcon(icon6)
        self.bn_settings.setObjectName("bn_settings")
        self.horizontalLayout_14.addWidget(self.settings)
        self.verticalLayout_2.addWidget(self.panelfront)
        self.frame_low = QtWidgets.QFrame(self.frame_bottom_east)
        self.frame_low.setMinimumSize(QtCore.QSize(0, 20))
        self.frame_low.setMaximumSize(QtCore.QSize(16777215, 20))
        self.frame_low.setStyleSheet("")
        self.frame_low.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_low.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_low.setObjectName("frame_low")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_low)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.frame_tab = QtWidgets.QFrame(self.frame_low)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.frame_tab.setFont(font)
        self.frame_tab.setStyleSheet("background:rgb(51,51,51);")
        self.frame_tab.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_tab.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_tab.setObjectName("frame_tab")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_tab)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.horizontalLayout_11.addWidget(self.frame_tab)
        self.frame_drag = QtWidgets.QFrame(self.frame_low)
        self.frame_drag.setMinimumSize(QtCore.QSize(20, 20))
        self.frame_drag.setMaximumSize(QtCore.QSize(20, 20))
        self.frame_drag.setStyleSheet("background:rgb(51,51,51);")
        self.frame_drag.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_drag.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_drag.setObjectName("frame_drag")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_drag)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.horizontalLayout_11.addWidget(self.frame_drag)
        self.verticalLayout_2.addWidget(self.frame_low)
        self.horizontalLayout_2.addWidget(self.frame_bottom_east)
        self.verticalLayout.addWidget(self.frame_bottom)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.bn_min.clicked.connect(MainWindow.hide) # type: ignore
        self.bn_close.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lab_appname.setText(_translate("MainWindow", "<html><head/><body><p>Fly Cast</p></body></html>"))
        self.lab_user.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">User Name</span></p></body></html>"))
        self.bn_min.setToolTip(_translate("MainWindow", "Minimize"))
        self.bn_close.setToolTip(_translate("MainWindow", "Close"))
        self.bn_home.setToolTip(_translate("MainWindow", "Home"))
        self.bn_plane.setToolTip(_translate("MainWindow", "Plane"))
        self.bn_weather.setToolTip(_translate("MainWindow", "Weather"))
        self.bn_settings.setToolTip(_translate("MainWindow", "settings"))
        self.frame_drag.setToolTip(_translate("MainWindow", "Drag"))