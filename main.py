import sys
import PySide6.QtWidgets as Qw
import PySide6.QtCore as Qc
import calc as c

class MainWindow(Qw.QMainWindow):
    
    
    #Window関連
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('YourCalculation')
        self.setGeometry(100, 50, 400, 300) 

    #Question関連
        label = Qw.QLabel(self)
        label.setGeometry(0, 0, 400, 200)
        labelStyle = """QLabel{
            color: #FFFFFF;
            font-size: 72px;
            background-color: #000000;
        }"""
        label.setMargin(70)
        label.setStyleSheet(labelStyle)
        label.setText(f"{str(c.fs)}+{str(c.ss)}=")

    #Answer関連
        self.ans = Qw.QLineEdit(self)
        self.ans.setGeometry(150,250,120,30)
        self.ans.returnPressed.connect(self.tof)
        
    def tof(self):
        if self.ans.text() == str(c.ans):
            print('正解！')
            
        else:
            print('不正解')


if __name__ == '__main__':
    app = Qw.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())