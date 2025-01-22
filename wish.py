from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt

def set_label():
    label.setText("Шалость удалась!")
    button.setText("Использовано")

app = QApplication([])
window = QWidget()
window.resize(400,200)
window.setWindowTitle("Приложение с секретом")

label = QLabel("Торжественно клянусь, что замышляю только шалость")
button = QPushButton("Шалость")
line = QVBoxLayout()

line.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)
line.addWidget(button)
window.setLayout(line)

button.clicked.connect(set_label)

window.show()
app.exec()













