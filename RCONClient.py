from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets

from helpers import *


# noinspection PyUnresolvedReferences
class Ui_MainWindow(object):
    # This function is auto-generated by pyuic, do not change as it may be overridden.
    # noinspection PyAttributeOutsideInit
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(783, 683)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(6, 5, 6, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.master_layout = QtWidgets.QGridLayout()
        self.master_layout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.master_layout.setObjectName("master_layout")
        self.config_dropdown = QtWidgets.QComboBox(self.centralwidget)
        self.config_dropdown.setObjectName("config_dropdown")
        self.master_layout.addWidget(self.config_dropdown, 0, 0, 1, 1)
        self.scroll_area = QtWidgets.QScrollArea(self.centralwidget)
        self.scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scroll_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setObjectName("scroll_area")
        self.scroll_area_contents = QtWidgets.QWidget()
        self.scroll_area_contents.setGeometry(QtCore.QRect(0, 0, 769, 578))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scroll_area_contents.sizePolicy().hasHeightForWidth())
        self.scroll_area_contents.setSizePolicy(sizePolicy)
        self.scroll_area_contents.setObjectName("scroll_area_contents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scroll_area_contents)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.console = QtWidgets.QTextBrowser(self.scroll_area_contents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.console.sizePolicy().hasHeightForWidth())
        self.console.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.console.setFont(font)
        self.console.setObjectName("console")
        self.gridLayout_2.addWidget(self.console, 0, 0, 1, 1)
        self.scroll_area.setWidget(self.scroll_area_contents)
        self.master_layout.addWidget(self.scroll_area, 1, 0, 1, 1)
        self.input_layout = QtWidgets.QHBoxLayout()
        self.input_layout.setObjectName("input_layout")
        self.command_input = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.command_input.sizePolicy().hasHeightForWidth())
        self.command_input.setSizePolicy(sizePolicy)
        self.command_input.setMinimumSize(QtCore.QSize(680, 0))
        self.command_input.setInputMask("")
        self.command_input.setObjectName("command_input")
        self.input_layout.addWidget(self.command_input)
        self.submit_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submit_button.sizePolicy().hasHeightForWidth())
        self.submit_button.setSizePolicy(sizePolicy)
        self.submit_button.setObjectName("submit_button")
        self.input_layout.addWidget(self.submit_button)
        self.master_layout.addLayout(self.input_layout, 2, 0, 1, 1)
        self.gridLayout.addLayout(self.master_layout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 783, 21))
        self.menubar.setObjectName("menubar")
        self.menu_configs = QtWidgets.QMenu(self.menubar)
        self.menu_configs.setObjectName("menu_configs")
        self.menu_preferences = QtWidgets.QMenu(self.menubar)
        self.menu_preferences.setObjectName("menu_preferences")
        self.menu_instance = QtWidgets.QMenu(self.menubar)
        self.menu_instance.setObjectName("menu_instance")
        self.menu_tools = QtWidgets.QMenu(self.menubar)
        self.menu_tools.setObjectName("menu_tools")
        MainWindow.setMenuBar(self.menubar)
        self.action_config_new = QtWidgets.QAction(MainWindow)
        self.action_config_new.setObjectName("action_config_new")
        self.action_config_edit = QtWidgets.QAction(MainWindow)
        self.action_config_edit.setObjectName("action_config_edit")
        self.action_config_delete = QtWidgets.QAction(MainWindow)
        self.action_config_delete.setObjectName("action_config_delete")
        self.action_instance_clear = QtWidgets.QAction(MainWindow)
        self.action_instance_clear.setObjectName("action_instance_clear")
        self.action_config_reorder = QtWidgets.QAction(MainWindow)
        self.action_config_reorder.setObjectName("action_config_reorder")
        self.action_instance_save = QtWidgets.QAction(MainWindow)
        self.action_instance_save.setObjectName("action_instance_save")
        self.menu_configs.addAction(self.action_config_new)
        self.menu_configs.addAction(self.action_config_edit)
        self.menu_configs.addAction(self.action_config_delete)
        self.menu_configs.addAction(self.action_config_reorder)
        self.menu_instance.addAction(self.action_instance_clear)
        self.menu_instance.addAction(self.action_instance_save)
        self.menubar.addAction(self.menu_instance.menuAction())
        self.menubar.addAction(self.menu_configs.menuAction())
        self.menubar.addAction(self.menu_tools.menuAction())
        self.menubar.addAction(self.menu_preferences.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.config_dropdown, self.command_input)
        MainWindow.setTabOrder(self.command_input, self.console)
        MainWindow.setTabOrder(self.console, self.scroll_area)
        MainWindow.setTabOrder(self.scroll_area, self.submit_button)

        # Start custom code, do not override anything under this line.
        # Custom variables
        self.consoles = {}

        # Setup dropdown
        self.set_dropdown()

        # Bind callbacks
        self.submit_button.clicked.connect(self.submit_command)  # Bind submit button to submit_command function
        self.action_config_new.triggered.connect(self.new_config)  # Bind new config button to new_config function
        self.action_config_edit.triggered.connect(self.edit_config)  # Bind edit config button to edit_config function
        self.action_config_delete.triggered.connect(self.delete_config)  # Bind delete config button to delete_config function
        self.action_config_reorder.triggered.connect(self.reorder_configs)  # Bind reorder config button to reorder_configs function
        self.action_instance_clear.triggered.connect(self.clear_console)  # Bind clear instance button to clear_console function
        self.action_instance_save.triggered.connect(self.save_console)  # Bind save instance button to save_console function
        self.config_dropdown.currentIndexChanged.connect(self.change_console_config)  # Bind dropdown to change_console_config function

    # This function is auto-generated by pyuic, do not change as it may be overridden.
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RCON Client v{}".format(VERSION)))
        self.command_input.setPlaceholderText(_translate("MainWindow", "Enter your command here"))
        self.submit_button.setText(_translate("MainWindow", "Submit"))
        self.submit_button.setShortcut(_translate("MainWindow", "Return"))
        self.menu_configs.setTitle(_translate("MainWindow", "Configurations"))
        self.menu_preferences.setTitle(_translate("MainWindow", "Preferences"))
        self.menu_instance.setTitle(_translate("MainWindow", "Instance"))
        self.menu_tools.setTitle(_translate("MainWindow", "Tools"))
        self.action_config_new.setText(_translate("MainWindow", "New"))
        self.action_config_edit.setText(_translate("MainWindow", "Edit Current"))
        self.action_config_delete.setText(_translate("MainWindow", "Delete Current"))
        self.action_instance_clear.setText(_translate("MainWindow", "Clear Console"))
        self.action_instance_save.setText(_translate("MainWindow", "Save Console"))
        self.action_instance_save.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.action_config_reorder.setText(_translate("MainWindow", "Reorder"))

    # CUSTOM METHODS
    def set_dropdown(self):
        self.config_dropdown.clear()
        self.config_dropdown.addItems(CONFIG.keys())

    def get_active_config(self) -> str:
        return self.config_dropdown.currentText()

    # CALLBACKS
    def submit_command(self):
        """This is a callback function that is called when the submit button is clicked."""
        # Only submit command if command_input or the button has focus. This is to avoid accidental submits w/ keybinds.
        if self.command_input.hasFocus() or self.submit_button.hasFocus():
            # Do not allow the submission of an empty command
            if self.command_input.text().strip() == "":
                return
            # Do not continue if there is no active config
            if self.get_active_config() == "":
                return QtWidgets.QMessageBox.critical(None, "Error", "No active configuration selected.")
            command = self.command_input.text()
            self.console.append("] {}".format(command))
            self.command_input.clear()
            try:
                self.console.append(send_rcon_command(command, *CONFIG[self.get_active_config()].values()))
            except Exception as e:
                self.console.append("Error: {}".format(e))
            self.console.verticalScrollBar().setValue(self.console.verticalScrollBar().maximum())
            # Update consoles output cache
            self.consoles[self.get_active_config()] = self.console.toPlainText()

    def new_config(self):
        dialog = ConfigEditor(self.new_config_dialog_callback)
        dialog.exec()

    def edit_config(self):
        dialog = ConfigEditor(self.edit_config_dialog_callback, CONFIG[self.get_active_config()], self.get_active_config())
        dialog.exec()

    def delete_config(self):
        reply = QtWidgets.QMessageBox.question(None, "Confirm", "Are you sure you want to delete \"{}\"?".format(
            self.get_active_config()), QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            del CONFIG[self.get_active_config()]
            save_config(CONFIG)
            self.set_dropdown()

    def reorder_configs(self):
        dialog = ConfigReorderDialog(self.reorder_configs_dialog_callback, CONFIG)
        dialog.exec()

    def new_config_dialog_callback(self, config_name, ip, port, password, _):
        if config_name in CONFIG:
            return QtWidgets.QMessageBox.critical(None, "Error", "A configuration with that name already exists.")
        CONFIG[config_name] = {"ip": ip, "port": port, "password": password}
        save_config(CONFIG)
        self.set_dropdown()

    def edit_config_dialog_callback(self, config_name, ip, port, password, old_config_name):
        if old_config_name is not None and config_name in CONFIG:
            return QtWidgets.QMessageBox.critical(None, "Error", "A configuration with that name already exists.")
        CONFIG[config_name] = {"ip": ip, "port": port, "password": password}
        if old_config_name is not None:
            del CONFIG[old_config_name]
        save_config(CONFIG)
        self.set_dropdown()

    def reorder_configs_dialog_callback(self, config_order):
        # noinspection PyGlobalUndefined
        global CONFIG
        CONFIG = {i: CONFIG[i] for i in config_order}
        save_config(CONFIG)
        self.set_dropdown()

    def clear_console(self):
        self.console.clear()

    def save_console(self):
        filename = QtWidgets.QFileDialog.getSaveFileName(None, "Save Console", clean_filename(
            "rcon_output_{}_{}".format(self.get_active_config().lower().strip(),
                                       datetime.now().strftime("%Y-%H-%M-%S_%f"))), "Text Files (*.txt)")[0]
        if filename == "":
            return
        with open(filename, "w") as f:
            f.write(self.console.toPlainText())

    def change_console_config(self):
        self.clear_console()
        if self.get_active_config() in self.consoles:
            self.console.append(self.consoles[self.get_active_config()])
            self.console.verticalScrollBar().setValue(self.console.verticalScrollBar().maximum())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
