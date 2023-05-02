import sys
from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QWidget,
    QLabel, QCheckBox, QComboBox, QListWidget, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton,
    QLineEdit, QSpinBox, QDoubleSpinBox, QSlider
)
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.setWindowTitle("Reading Time App")

        # Create layout
        main_layout = QHBoxLayout()


        # Create two columbs
        left_pane = QVBoxLayout()
        right_pane = QVBoxLayout()


        # Title Label
        title_label = QLabel("Reading Time Calculator")


        # Set the font
        h1_font = title_label.font()
        h1_font.setPointSize(30)
        title_label.setFont(h1_font)
        
        
        # Reading speed input
        readingspeed_label = QLabel("Reading Speed")
        readingspeed_spinbox = QDoubleSpinBox()


        # Total pages input
        totalpages_label = QLabel("Total Pages")
        totalpages_spinbox = QSpinBox()


        # Current page input
        currentpage_label = QLabel("Current Page")
        currentpage_spinbox = QSpinBox()


        # Calculate button
        calculate_label = QLabel("Calculate")
        calculate_button = QPushButton()


        # Results Pane Widgets
        results_title = QLabel("Results")
        results_title.setAlignment (Qt.AlignmentFlag.AlignHCenter | 
                                 Qt.AlignmentFlag.AlignTop)
        h2_font = results_title.font()
        h2_font.setPointSize(26)
        results_title.setFont(h2_font)
        results_window = QLineEdit("Enter the page number you want to read to in the 'total pages' box. Then, input your current page number in the 'current page' box.")
        results_window.setMinimumHeight(100)
        

        # Align the label
        title_label.setAlignment(Qt.AlignmentFlag.AlignHCenter | 
                                 Qt.AlignmentFlag.AlignTop)


        # Add our left pane widgets
        left_pane.addWidget(title_label)
        left_pane.addWidget(totalpages_label)
        left_pane.addWidget(totalpages_spinbox)
        left_pane.addWidget(currentpage_label)
        left_pane.addWidget(currentpage_spinbox)
        left_pane.addWidget(readingspeed_label)
        left_pane.addWidget(readingspeed_spinbox)


        #Add our right pane widets
        right_pane.addWidget(results_title)
        right_pane.addWidget(results_window)
        right_pane.addWidget(calculate_label)
        right_pane.addWidget(calculate_button)


        # Add the two panes to the layout
        main_layout.addLayout(left_pane)
        main_layout.addLayout(right_pane)


        # Set the main layout
        gui = QWidget()
        gui.setLayout(main_layout)
        self.setCentralWidget(gui)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()