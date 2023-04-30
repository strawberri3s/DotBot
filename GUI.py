from PyQt5.QtWidgets import QApplication, QTextEdit, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton,QStackedLayout,QLabel,QFileDialog,QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from NeV1 import MultiThreadScan
import sys
import threading
import  resources_rc
import datetime





class PrintOutput(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.output = QTextEdit()
        self.output.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.output.setStyleSheet("background:#bcbcbc; border:0px;border-radius: 4px;")
        self.output.setReadOnly(True) # Set read-only property
        layout.addWidget(self.output)


        # Add line text box and button
        self.input = QLineEdit()
        self.input.setMinimumSize(200,40)
        self.input.setStyleSheet("background:#bcbcbc; border-radius: 4px;")
        self.button = QPushButton('Submit')
        self.button.setMinimumSize(100,40)
        self.button.setStyleSheet("""background-color: #294B93;
    color: #FFFFFF;
    
    border: none;
    border-radius: 4px;
    font-weight: bold;
    text-transform: uppercase;""")
        self.button.clicked.connect(self.submit)
        self.button1 = QPushButton('')
        icon = QIcon(':/fold.png')
        self.button1.setIcon(icon)
        self.button1.setMinimumSize(40,40)
        self.button1.setStyleSheet("""background-color: #294B93;
    color: #FFFFFF;
    
    border: none;
    border-radius: 4px;
    font-weight: bold;
    text-transform: uppercase;""")
        self.button1.clicked.connect(self.choose)
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.input)
        button_layout.addWidget(self.button1)
        button_layout.addWidget(self.button)
        layout.addLayout(button_layout)
        self.setMinimumSize(800,600)
        self.setStyleSheet("background:#eeeeee; ")
        self.setLayout(layout)
        self.file_path = None

    def choose(self):
        self.file_path, _ = QFileDialog.getOpenFileName(None, "Select file", "", "Text File (*.txt)")


    def addTxt(self,input_text):
        text = MultiThreadScan(input_text)
        with open(self.file_path, 'w') as file:
            current_time = str(datetime.datetime.now())
            file.write(current_time)
            for item in text:
                file.write(str(item) + '\n')    
        for row in range(len(text)):
            temp = text[row]
            str1 = str(temp[0])
            str2 = str(temp[1])
            str3 = str(temp[2])
            str4 = str(temp[3])
            str5 = str(temp[4])
            str6 = str(temp[5])
            rich_text = f'<span style="font-size: 10pt;"><font color="blue">{str1}</font><font color="black">{str2}</font><font color="red">{str3}</font><font color="black">{str4}</font><font color="red">{str5}</font><font color="blue">{str6}</font>'
            self.output.insertHtml(rich_text)
            self.output.append("\n")

    def msg(self):
        msgBox = QMessageBox()
        msgBox.setStyleSheet("""QPushButton{background-color: #294B93;
    color: #FFFFFF;
    width:80px;
    height:40px;
    border: none;
    border-radius: 4px;
    font-weight: bold;
    text-transform: uppercase;}

    QMessageBox{background:#eeeeee;}
        """)
        msgBox.setText("You need to enter an URL, it must be in the form: https://example.com/")
        msgBox.exec_()


    def submit(self):
        if self.file_path != None:
            input_text = self.input.text()
            if input_text[0:8] != "https://":
                self.msg()

            else:
                msgBox = QMessageBox()
                msgBox.setStyleSheet("""QPushButton{background-color: #294B93;
    color: #FFFFFF;
    width:80px;
    height:40px;
    border: none;
    border-radius: 4px;
    font-weight: bold;
    text-transform: uppercase;}

    QMessageBox{background:#eeeeee;}
        """)
                msgBox.setText("Please Wait   ")
                msgBox.exec_()
                msgBox.setDisabled(True)
                self.setDisabled(True)

                thread = threading.Thread(target=self.addTxt, args=(input_text,))
                thread.start()
                thread.join()
                msgBox.setDisabled(False)
                self.setDisabled(False)
            
            

        else:
            self.msg()
        

        
        
        

    def write(self, message):
        self.output.insertPlainText(message)

class MyApp(QApplication):
    def __init__(self, args):
        super().__init__(args)
        self.print_output = PrintOutput()

if __name__ == '__main__':
    app = MyApp(sys.argv)
    app.print_output.show()
    sys.exit(app.exec_())
