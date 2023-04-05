import sys
from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QWidget,
    QLabel, QCheckBox, QComboBox, QListWidget, QLineEdit, QVBoxLayout,
    QLineEdit, QSpinBox, QDoubleSpinBox, QSlider
)
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.setWindowTitle("My App")

        # Create our layouts
        vertical_layout = QVBoxLayout()

        # QLabels
        title_label = QLabel("Reading Time Calculator")
        title_font = title_label.font()
        title_font.setPointSize(30)
        title_label.setFont(title_font)\
        

        # Align the label
        title_label.setAlignment(Qt.AlignmentFlag.AlignHCenter | 
                                 Qt.AlignmentFlag.AlignTop)

        
        # Add label to vertical_layout
        vertical_layout.addWidget(title_label)


        # Set the main layout
        gui = QWidget()
        gui.setLayout(vertical_layout)
        self.setCentralWidget(gui)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()