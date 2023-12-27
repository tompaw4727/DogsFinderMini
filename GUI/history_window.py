from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)

from PySide6.QtGui import QFont
from PySide6.QtWidgets import QTextBrowser

class Ui_history_widget(object):
    def setupUi(self, history_widget):
        if not history_widget.objectName():
            history_widget.setObjectName(u"history_widget")
        history_widget.resize(499, 369)
        history_widget.setFixedSize(499, 369)
        history_widget.setStyleSheet(u"QWidget {\n"
                                     "background: #E1ECC8\n"
                                     "}")
        self.textBrowser = QTextBrowser(history_widget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(30, 60, 441, 291))
        font = QFont()
        font.setFamilies([u"Garamond"])
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet(u"QTextBrowser {\n"
                                       "background: #F7FFE5;\n"
                                       "border: 1px solid #000000;\n"
                                       "}")
        self.textBrowser_2 = QTextBrowser(history_widget)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(50, 10, 401, 41))
        font1 = QFont()
        font1.setFamilies([u"Garamond"])
        font1.setPointSize(12)
        font1.setBold(False)
        self.textBrowser_2.setFont(font1)
        self.textBrowser_2.setStyleSheet(u"QTextBrowser {\n"
                                         "color: #000000;\n"
                                         "background: #A0C49D;\n"
                                         "border: 1px solid #000000;\n"
                                         "border-radius: 20px;\n"
                                         "border-style: outset;\n"
                                         "}")
        self.textBrowser_2.setLineWidth(4)

        self.retranslateUi(history_widget)

        QMetaObject.connectSlotsByName(history_widget)
    # setupUi

    def retranslateUi(self, history_widget):
        history_widget.setWindowTitle(QCoreApplication.translate("history_widget", u"Form", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("history_widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Garamond'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">A little history of this breed:</span></p></body></html>", None))


