# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QComboBox, QTextEdit
# import openai
#
# # Set your OpenAI API key
# openai.api_key = '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'
# class MyApp(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         main_vbox = QVBoxLayout(self)
#
#         # Select Horizontal Box
#         select_hbox = QHBoxLayout()
#         form_vbox = QVBoxLayout()
#         to_vbox = QVBoxLayout()
#
#         # Hello Label and ComboBox
#         hello_label = QLabel("From:")
#         self.form_combobox = QComboBox()
#         self.form_combobox.addItems(["JAVA", "PYTHON", "C", "C++", "RUBY", "RUST", "JAVASCRIPT", "C#"])
#         form_vbox.addWidget(hello_label)
#         form_vbox.addWidget(self.form_combobox)
#
#         # World Label and ComboBox
#         world_label = QLabel("To:")
#         self.to_combobox = QComboBox()
#         self.to_combobox.addItems(["JAVA", "PYTHON", "C", "C++", "RUBY", "RUST", "JAVASCRIPT", "C#"])
#         to_vbox.addWidget(world_label)
#         to_vbox.addWidget(self.to_combobox)
#
#         select_hbox.addLayout(form_vbox)
#         select_hbox.addLayout(to_vbox)
#
#         main_vbox.addLayout(select_hbox)
#
#         button = QPushButton("Convert", self)
#         button.clicked.connect(self.convert_text)  # Connect the button click to the convert_text function
#         main_vbox.addWidget(button)
#
#         text_hbox = QHBoxLayout()
#
#         source_code_text_area = QTextEdit(self)
#         self.source_code_text_area = source_code_text_area  # Store a reference to the first text area
#         self.converted_code_text_area = QTextEdit(self)
#         self.converted_code_text_area.setReadOnly(True)
#
#         text_hbox.addWidget(source_code_text_area)
#         text_hbox.addWidget(self.converted_code_text_area)
#
#         main_vbox.addLayout(text_hbox)
#
#         self.setLayout(main_vbox)
#         self.setGeometry(100, 100, 400, 300)
#         self.setWindowTitle('PyQt5 Application')
#         self.show()
#
#     def convert_text(self):
#
#         # Get the selected options from the combo boxes
#         from_language = self.form_combobox.currentText()
#         to_language = self.to_combobox.currentText()
#
#         # Get the text from the first text area
#         source_code = self.source_code_text_area.toPlainText()
#
#         prompt = f"convert the following {from_language} code into {to_language} code:\n\n {source_code}"
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": "system", "content": "You are a Python code."},
#                 {"role": "user", "content": prompt}
#             ],
#             temperature=0.7,
#             max_tokens=150,
#             stop=["\n```"]
#         )
#         converted_code = response.choices[0].message['content']
#
#         # Set the processed text to the second text area
#         self.converted_code_text_area.setText(converted_code)
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = MyApp()
#     sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QComboBox, QTextEdit, \
    QMessageBox
from PyQt5.QtGui import QClipboard, QFont
import openai

# Set your OpenAI API key
openai.api_key = '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'


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        main_vbox = QVBoxLayout(self)

        # Set background color
        self.setStyleSheet("background-color: #f0f0f0;")

        # Select Horizontal Box
        select_hbox = QHBoxLayout()
        form_vbox = QVBoxLayout()
        to_vbox = QVBoxLayout()

        # Hello Label and ComboBox
        hello_label = QLabel("From:")
        self.form_combobox = QComboBox()
        self.form_combobox.addItems(["JAVA", "PYTHON", "C", "C++", "RUBY", "RUST", "JAVASCRIPT", "C#"])
        self.form_combobox.setStyleSheet(
            "QComboBox { background-color: white; color: black; border: 1px solid #ccc; border-radius: 5px; padding: 5px; }"
            "QComboBox::drop-down { subcontrol-origin: padding; subcontrol-position: top right; width: 0px; border-left-width: 1px; border-left-color: #ccc; border-left-style: solid; }")
        form_vbox.addWidget(hello_label)
        form_vbox.addWidget(self.form_combobox)

        # World Label and ComboBox
        world_label = QLabel("To:")
        self.to_combobox = QComboBox()
        self.to_combobox.addItems(["JAVA", "PYTHON", "C", "C++", "RUBY", "RUST", "JAVASCRIPT", "C#"])
        self.to_combobox.setStyleSheet(
            "QComboBox { background-color: white; color: black; border: 1px solid #ccc; border-radius: 5px; padding: 5px; }"
            "QComboBox::drop-down { subcontrol-origin: padding; subcontrol-position: top right; width: 0px; border-left-width: 1px; border-left-color: #ccc; border-left-style: solid; }")
        to_vbox.addWidget(world_label)
        to_vbox.addWidget(self.to_combobox)

        select_hbox.addLayout(form_vbox)
        select_hbox.addLayout(to_vbox)

        main_vbox.addLayout(select_hbox)

        button = QPushButton("Convert", self)
        button.clicked.connect(self.convert_text)  # Connect the button click to the convert_text function
        button.setStyleSheet(
            "QPushButton { background-color: #4CAF50; color: white; border: none; padding: 10px 20px; font-size: 16px; border-radius: 5px; }"
            "QPushButton:hover { background-color: #45a049; }")
        main_vbox.addWidget(button)

        text_hbox = QHBoxLayout()

        source_code_text_area = QTextEdit(self)
        self.source_code_text_area = source_code_text_area  # Store a reference to the first text area
        self.source_code_text_area.setPlaceholderText("Write your source code here....")
        self.source_code_text_area.setStyleSheet(
            "background-color: white; color: black; border: 1px solid #ccc; border-radius: 5px; padding: 10px;")
        self.converted_code_text_area = QTextEdit(self)
        self.converted_code_text_area.setReadOnly(True)
        self.converted_code_text_area.setPlaceholderText("Converted code....")
        self.converted_code_text_area.setStyleSheet(
            "background-color: white; color: black; border: 1px solid #ccc; border-radius: 5px; padding: 10px;")

        text_hbox.addWidget(source_code_text_area)
        text_hbox.addWidget(self.converted_code_text_area)

        main_vbox.addLayout(text_hbox)

        # Add horizontal box for buttons
        buttons_hbox = QHBoxLayout()

        # Clear button
        clear_button = QPushButton("Clear All")
        clear_button.clicked.connect(self.clear_all)
        clear_button.setStyleSheet(
            "QPushButton { background-color: #f44336; color: white; border: none; padding: 10px 20px; font-size: 16px; border-radius: 5px; }"
            "QPushButton:hover { background-color: #d32f2f; }")
        buttons_hbox.addWidget(clear_button)

        # Copy button
        copy_button = QPushButton("Copy to Clipboard")
        copy_button.clicked.connect(self.copy_to_clipboard)
        copy_button.setStyleSheet(
            "QPushButton { background-color: #008CBA; color: white; border: none; padding: 10px 20px; font-size: 16px; border-radius: 5px; }"
            "QPushButton:hover { background-color: #006f8a; }")
        buttons_hbox.addWidget(copy_button)

        main_vbox.addLayout(buttons_hbox)

        self.setLayout(main_vbox)
        self.setGeometry(100, 100, 600, 400)  # Increased size for better visibility
        self.setWindowTitle('Code Converter')
        self.show()

    def convert_text(self):
        # Get the selected options from the combo boxes
        from_language = self.form_combobox.currentText()
        to_language = self.to_combobox.currentText()

        # Get the text from the first text area
        source_code = self.source_code_text_area.toPlainText()

        prompt = f"convert the following {from_language} code into {to_language} code:\n\n {source_code}"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a Python code."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=150,
            stop=["\n```"]
        )
        converted_code = response.choices[0].message['content']

        # Set the processed text to the second text area
        self.converted_code_text_area.setText(converted_code)

    def clear_all(self):
        self.source_code_text_area.clear()
        self.converted_code_text_area.clear()

    def copy_to_clipboard(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.converted_code_text_area.toPlainText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
