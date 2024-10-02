from PySide6 import QtWidgets, QtGui
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
        observation_time_label = QtWidgets.QLabel("Введите время наблюдения")
        
        entry_thread_length = QtWidgets.QLineEdit()
        entry_deflection_angle = QtWidgets.QLineEdit()
        entry_pendulum_mass = QtWidgets.QLineEdit()
        entry_observation_time = QtWidgets.QLineEdit()
        
        start = QtWidgets.QPushButton("Начать моделирование")
        
        box.addWidget(thread_length_label)
        box.addWidget(entry_thread_length)
        
        box.addWidget(deflection_angle_label)
        box.addWidget(entry_deflection_angle)
        
        box.addWidget(pendulum_mass_label)
        box.addWidget(entry_pendulum_mass)
        
        box.addWidget(observation_time_label)
        box.addWidget(entry_observation_time)
        
        box.addWidget(start)
        
        self.window.setLayout(box)
        
    def run(self):
        self.window.show()
        self.app.exec()