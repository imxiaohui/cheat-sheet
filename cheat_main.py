#!/usr/bin/env python
''' PyQt program to display cheat sheet info for python'''

import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QTextDocument, QTextCursor
from python_cheat_sheet_gui import Ui_PythonCheatSheet

class PythonCheatSheet(QtGui.QDialog, Ui_PythonCheatSheet):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_PythonCheatSheet()
        self.ui.setupUi(self)
        self.browser = self.ui.results_browser
        self.browser.acceptRichText
        self.ui.lists_button.clicked.connect(self.list_info)
        self.ui.strings_button.clicked.connect(self.string_info)
        self.ui.keywords_button.clicked.connect(self.keywords_info)
        self.ui.expressions_button.clicked.connect(self.expressions_info)
        self.ui.conditionals_button.clicked.connect(self.conditionals_info)
        self.ui.decorators_button.clicked.connect(self.decorators_info)
        self.ui.exceptions_button.clicked.connect(self.exceptions_info)
        self.ui.yield_button.clicked.connect(self.yield_info)
        self.ui.twisted_button.clicked.connect(self.twisted_info)
        self.ui.examples_button.clicked.connect(self.examples_info)
        self.ui.clear_button.clicked.connect(self.clear)
        self.ui.quit_button.clicked.connect(self.reject)
        self.ui.search_text.returnPressed.connect(self.do_search)
        self.first_search = True

    def do_search(self):
        search_for = self.ui.search_text.text()
        if self.first_search:
            self.first_search = False
            self.browser.moveCursor(QTextCursor.Start)
        if self.browser.find(search_for) == False:
            self.first_search = True # Wrap searching

    def add_data(self, name, data_fd):
        self.browser.append('\n{0}:'.format(name))
        lines = data_fd.readlines()
        for line in lines:
            self.browser.append(line.rstrip())

    def list_info(self):
        with open('./list_info') as fd:
            self.add_data('Lists', fd)

    def string_info(self):
        with open('./string_info') as fd:
            self.add_data('Strings', fd)

    def keywords_info(self):
        with open('./keywords_info') as fd:
            self.add_data('Keywords', fd)

    def expressions_info(self):
        with open('./expressions_info') as fd:
            self.add_data('Expressions', fd)

    def conditionals_info(self):
        with open('./conditionals_info') as fd:
            self.add_data('Conditionals', fd)

    def decorators_info(self):
        with open('./decorators_info') as fd:
            self.add_data('Decorator', fd)

    def exceptions_info(self):
        with open('./exceptions_info') as fd:
            self.add_data('Exceptions', fd)

    def yield_info(self):
        with open('./yield_info') as fd:
            self.add_data('Yield', fd)

    def twisted_info(self):
        with open('./twisted_info') as fd:
            self.add_data('Twisted', fd)

    def examples_info(self):
        with open('./examples_info') as fd:
            self.add_data('Examples', fd)

    def clear(self):
        self.browser.clear()

    def reject(self):
        QtCore.QCoreApplication.instance().quit()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    myapp = PythonCheatSheet()
    myapp.show()
    sys.exit(app.exec_())
