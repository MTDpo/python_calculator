# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
                               QMainWindow, QPushButton, QSizePolicy, QWidget)
import files_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(361, 569)
        MainWindow.setStyleSheet(u"QWidget {\n"
                                 "	color: white;\n"
                                 "	background-color: #121212;\n"
                                 "	font-family: Rubik;\n"
                                 "	font-size: 16pt;\n"
                                 "	font-weight: 600;\n"
                                 "}\n"
                                 "QPushButton {\n"
                                 "	background-color: transparent;\n"
                                 "	border: none;\n"
                                 "}\n"
                                 "QPushButton:hover {\n"
                                 "	background-color: #666;\n"
                                 "}\n"
                                 "QPushButton:pressed {\n"
                                 "	background-color: #888;\n"
                                 "}\n"
                                 "")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 361, 41))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet(u"color: #888;")
        self.label.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(0, 50, 361, 61))
        self.lineEdit.setStyleSheet(u"font-size: 40pt;\n"
                                    "border: none;")
        self.lineEdit.setMaxLength(16)
        self.lineEdit.setCursorPosition(3)
        self.lineEdit.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.lineEdit.setReadOnly(True)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 120, 361, 451))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.layoutWidget.sizePolicy().hasHeightForWidth())
        self.layoutWidget.setSizePolicy(sizePolicy1)
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_delimetr = QPushButton(self.layoutWidget)
        self.pushButton_delimetr.setObjectName(u"pushButton_delimetr")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_delimetr.sizePolicy().hasHeightForWidth())
        self.pushButton_delimetr.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pushButton_delimetr, 5, 2, 1, 1)

        self.pushButton_equal = QPushButton(self.layoutWidget)
        self.pushButton_equal.setObjectName(u"pushButton_equal")
        sizePolicy2.setHeightForWidth(self.pushButton_equal.sizePolicy().hasHeightForWidth())
        self.pushButton_equal.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pushButton_equal, 5, 3, 1, 1)

        self.pushButton_2 = QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy2.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pushButton_2, 4, 1, 1, 1)

        self.pushButton_C = QPushButton(self.layoutWidget)
        self.pushButton_C.setObjectName(u"pushButton_C")
        sizePolicy2.setHeightForWidth(self.pushButton_C.sizePolicy().hasHeightForWidth())
        self.pushButton_C.setSizePolicy(sizePolicy2)
        self.pushButton_C.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_C, 0, 2, 1, 1)

        self.pushButton_sqrt = QPushButton(self.layoutWidget)
        self.pushButton_sqrt.setObjectName(u"pushButton_sqrt")
        sizePolicy2.setHeightForWidth(self.pushButton_sqrt.sizePolicy().hasHeightForWidth())
        self.pushButton_sqrt.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pushButton_sqrt, 1, 2, 1, 1)

        self.pushButton_7 = QPushButton(self.layoutWidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy2.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pushButton_7, 2, 0, 1, 1)

        self.pushButton_9 = QPushButton(self.layoutWidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy2.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pushButton_9, 2, 2, 1, 1)

        self.pushButton_division = QPushButton(self.layoutWidget)
        self.pushButton_division.setObjectName(u"pushButton_division")
        sizePolicy2.setHeightForWidth(self.pushButton_division.sizePolicy().hasHeightForWidth())
        self.pushButton_division.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pushButton_division, 1, 3, 1, 1)

        self.pushButton_clear = QPushButton(self.layoutWidget)
        self.pushButton_clear.setObjectName(u"pushButton_clear")
        sizePolicy2.setHeightForWidth(self.pushButton_clear.sizePolicy().hasHeightForWidth())
        self.pushButton_clear.setSizePolicy(sizePolicy2)
        icon = QIcon()
        icon.addFile(u":/icons/icons8-clear-symbol-60.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_clear.setIcon(icon)
        self.pushButton_clear.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.pushButton_clear, 0, 3, 1, 1)

        self.pushButton_degree = QPushButton(self.layoutWidget)
        self.pushButton_degree.setObjectName(u"pushButton_degree")
        sizePolicy2.setHeightForWidth(self.pushButton_degree.sizePolicy().hasHeightForWidth())
        self.pushButton_degree.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pushButton_degree, 1, 1, 1, 1)

        self.pushButton_divisionx = QPushButton(self.layoutWidget)
        self.pushButton_divisionx.setObjectName(u"pushButton_divisionx")
        sizePolicy2.setHeightForWidth(self.pushButton_divisionx.sizePolicy().hasHeightForWidth())
        self.pushButton_divisionx.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pushButton_divisionx, 1, 0, 1, 1)

        self.pushButton_8 = QPushButton(self.layoutWidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy2.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pushButton_8, 2, 1, 1, 1)

        self.pushButton_5 = QPushButton(self.layoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy2.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pushButton_5, 3, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy2.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pushButton_3, 4, 2, 1, 1)

        self.pushButton_1 = QPushButton(self.layoutWidget)
        self.pushButton_1.setObjectName(u"pushButton_1")
        sizePolicy2.setHeightForWidth(self.pushButton_1.sizePolicy().hasHeightForWidth())
        self.pushButton_1.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pushButton_1, 4, 0, 1, 1)

        self.pushButton_plus = QPushButton(self.layoutWidget)
        self.pushButton_plus.setObjectName(u"pushButton_plus")
        sizePolicy2.setHeightForWidth(self.pushButton_plus.sizePolicy().hasHeightForWidth())
        self.pushButton_plus.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pushButton_plus, 4, 3, 1, 1)

        self.pushButton_minus = QPushButton(self.layoutWidget)
        self.pushButton_minus.setObjectName(u"pushButton_minus")
        sizePolicy2.setHeightForWidth(self.pushButton_minus.sizePolicy().hasHeightForWidth())
        self.pushButton_minus.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pushButton_minus, 3, 3, 1, 1)

        self.pushButton_4 = QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy2.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pushButton_4, 3, 0, 1, 1)

        self.pushButton_CE = QPushButton(self.layoutWidget)
        self.pushButton_CE.setObjectName(u"pushButton_CE")
        sizePolicy2.setHeightForWidth(self.pushButton_CE.sizePolicy().hasHeightForWidth())
        self.pushButton_CE.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pushButton_CE, 0, 1, 1, 1)

        self.pushButton_multiply = QPushButton(self.layoutWidget)
        self.pushButton_multiply.setObjectName(u"pushButton_multiply")
        sizePolicy2.setHeightForWidth(self.pushButton_multiply.sizePolicy().hasHeightForWidth())
        self.pushButton_multiply.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pushButton_multiply, 2, 3, 1, 1)

        self.pushButton_6 = QPushButton(self.layoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy2.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pushButton_6, 3, 2, 1, 1)

        self.pushButton_minus_plus = QPushButton(self.layoutWidget)
        self.pushButton_minus_plus.setObjectName(u"pushButton_minus_plus")
        sizePolicy2.setHeightForWidth(self.pushButton_minus_plus.sizePolicy().hasHeightForWidth())
        self.pushButton_minus_plus.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pushButton_minus_plus, 5, 0, 1, 1)

        self.pushButton_0 = QPushButton(self.layoutWidget)
        self.pushButton_0.setObjectName(u"pushButton_0")
        sizePolicy2.setHeightForWidth(self.pushButton_0.sizePolicy().hasHeightForWidth())
        self.pushButton_0.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pushButton_0, 5, 1, 1, 1)

        self.pushButton_percent = QPushButton(self.layoutWidget)
        self.pushButton_percent.setObjectName(u"pushButton_percent")
        sizePolicy2.setHeightForWidth(self.pushButton_percent.sizePolicy().hasHeightForWidth())
        self.pushButton_percent.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pushButton_percent, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculator", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"228 + 221 * 14 = 1041040", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"122", None))
        self.pushButton_delimetr.setText(QCoreApplication.translate("MainWindow", u".", None))
        # if QT_CONFIG(shortcut)
        self.pushButton_delimetr.setShortcut(QCoreApplication.translate("MainWindow", u".", None))
        # endif // QT_CONFIG(shortcut)
        self.pushButton_equal.setText(QCoreApplication.translate("MainWindow", u"=", None))
        # if QT_CONFIG(shortcut)
        self.pushButton_equal.setShortcut(QCoreApplication.translate("MainWindow", u"=, Return", None))
        # endif // QT_CONFIG(shortcut)
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        # if QT_CONFIG(shortcut)
        self.pushButton_2.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
        # endif // QT_CONFIG(shortcut)
        self.pushButton_C.setText(QCoreApplication.translate("MainWindow", u"C", None))
        # if QT_CONFIG(shortcut)
        self.pushButton_C.setShortcut(QCoreApplication.translate("MainWindow", u"C", None))
        # endif // QT_CONFIG(shortcut)
        self.pushButton_sqrt.setText(QCoreApplication.translate("MainWindow", u"sqrt(x)", None))
        # if QT_CONFIG(shortcut)
        self.pushButton_sqrt.setShortcut("")
        # endif // QT_CONFIG(shortcut)
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        # if QT_CONFIG(shortcut)
        self.pushButton_7.setShortcut(QCoreApplication.translate("MainWindow", u"7", None))
        # endif // QT_CONFIG(shortcut)
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        # if QT_CONFIG(shortcut)
        self.pushButton_9.setShortcut(QCoreApplication.translate("MainWindow", u"9", None))
        # endif // QT_CONFIG(shortcut)
        self.pushButton_division.setText(QCoreApplication.translate("MainWindow", u"/", None))
        # if QT_CONFIG(shortcut)
        self.pushButton_division.setShortcut(QCoreApplication.translate("MainWindow", u"/", None))
        # endif // QT_CONFIG(shortcut)
        self.pushButton_clear.setText("")
        self.pushButton_degree.setText(QCoreApplication.translate("MainWindow", u"x^2", None))
        self.pushButton_divisionx.setText(QCoreApplication.translate("MainWindow", u"1/x", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        # if QT_CONFIG(shortcut)
        self.pushButton_8.setShortcut(QCoreApplication.translate("MainWindow", u"8", None))
        # endif // QT_CONFIG(shortcut)
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        # if QT_CONFIG(shortcut)
        self.pushButton_5.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
        # endif // QT_CONFIG(shortcut)
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        # if QT_CONFIG(shortcut)
        self.pushButton_3.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
        # endif // QT_CONFIG(shortcut)
        self.pushButton_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        # if QT_CONFIG(shortcut)
        self.pushButton_1.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
        # endif // QT_CONFIG(shortcut)
        self.pushButton_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        # if QT_CONFIG(shortcut)
        self.pushButton_plus.setShortcut(QCoreApplication.translate("MainWindow", u"+", None))
        # endif // QT_CONFIG(shortcut)
        self.pushButton_minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        # if QT_CONFIG(shortcut)
        self.pushButton_minus.setShortcut(QCoreApplication.translate("MainWindow", u"-", None))
        # endif // QT_CONFIG(shortcut)
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        # if QT_CONFIG(shortcut)
        self.pushButton_4.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
        # endif // QT_CONFIG(shortcut)
        self.pushButton_CE.setText(QCoreApplication.translate("MainWindow", u"CE", None))
        # if QT_CONFIG(shortcut)
        self.pushButton_CE.setShortcut("")
        # endif // QT_CONFIG(shortcut)
        self.pushButton_multiply.setText(QCoreApplication.translate("MainWindow", u"*", None))
        # if QT_CONFIG(shortcut)
        self.pushButton_multiply.setShortcut(QCoreApplication.translate("MainWindow", u"*", None))
        # endif // QT_CONFIG(shortcut)
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        # if QT_CONFIG(shortcut)
        self.pushButton_6.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
        # endif // QT_CONFIG(shortcut)
        self.pushButton_minus_plus.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
        self.pushButton_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        # if QT_CONFIG(shortcut)
        self.pushButton_0.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
        # endif // QT_CONFIG(shortcut)
        self.pushButton_percent.setText(QCoreApplication.translate("MainWindow", u"%", None))
        # if QT_CONFIG(shortcut)
        self.pushButton_percent.setShortcut("")
# endif // QT_CONFIG(shortcut)
# retranslateUi
