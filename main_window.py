from PySide6 import QtWidgets, QtGui
from PySide6.QtWidgets import QMessageBox
from draw import Pend
from style import STYLE

class MainWindow:
    def __init__(self) -> None:
        self.app = QtWidgets.QApplication()
        
        self.window = QtWidgets.QWidget()
        self.window.setWindowTitle("Моделирование маятника")
        self.window.setStyleSheet(STYLE)
        icon = QtGui.QIcon(r"photo\1437104.ico")
        self.window.setWindowIcon(icon)
        
        box = QtWidgets.QVBoxLayout()
        
        thread_length_label = QtWidgets.QLabel("Введите длину нити")
        deflection_angle_label = QtWidgets.QLabel("Введите угол отклонения")
        pendulum_mass_label = QtWidgets.QLabel("Введите массу маятника")
        
        self.entry_thread_length = QtWidgets.QLineEdit()
        self.entry_deflection_angle = QtWidgets.QLineEdit()
        self.entry_pendulum_mass = QtWidgets.QLineEdit()
        
        start = QtWidgets.QPushButton("Начать моделирование")
        
        start.clicked.connect(self.running_the_simulation)
        
        box.addWidget(thread_length_label)
        box.addWidget(self.entry_thread_length)
        
        box.addWidget(deflection_angle_label)
        box.addWidget(self.entry_deflection_angle)
        
        box.addWidget(pendulum_mass_label)
        box.addWidget(self.entry_pendulum_mass)
        
        box.addWidget(start)
        
        self.window.setLayout(box)
        
    def run(self):
        self.window.show()
        self.app.exec()
        
    def running_the_simulation(self):
        
        try:
            length = int(self.entry_thread_length.text())
            angle = int(self.entry_deflection_angle.text())
            mass = int(self.entry_pendulum_mass.text())
        except:
            msg_error = QMessageBox()
            msg_error.setText("Вы ввели неверные значения для модуляции")
            msg_error.setStandardButtons(QMessageBox.Discard)
            ret = msg_error.exec() 
            
            if ret == QMessageBox.Discard:
                msg_error.destroy()
            
        run = Pend(length, angle, mass)
        run.run_sim()