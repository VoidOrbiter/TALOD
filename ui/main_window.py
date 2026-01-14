from PyQt5.QtWidgets import (
    QApplication, QWidget, QGridLayout,
    QTextEdit, QLabel, QPushButton
)
import sys

class GameWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TALOD - Tales And Legends of Draemort")
        layout = QGridLayout()
        self.setLayout(layout)

        # --- Left Column ---
        layout.addWidget(QTextEdit("Grid Map"), 0, 0)
        layout.addWidget(QTextEdit("Party List"), 1, 0, 3, 1)

        # --- Center ---
        layout.addWidget(QTextEdit("Title / Location Name"), 0, 1, 1, 2)
        layout.addWidget(QTextEdit("Character Sheet / Equipment"), 0, 3, 2, 1)

        # --- Main Narrative Block ---
        layout.addWidget(QTextEdit("Main Text Log"), 1, 1, 1, 2)

        # --- Dashboard ---
        layout.addWidget(QTextEdit("Subconcious"), 2, 1)
        layout.addWidget(QTextEdit("Side Text"), 2, 2)
        layout.addWidget(QTextEdit("Items / Inventory"), 2, 3, 2, 1)

        # --- Actions ---
        layout.addWidget(QTextEdit("Actions maybe commands"), 3, 1, 1, 2)

        # --- Stretching ---
        layout.setColumnStretch(1, 2)
        layout.setColumnStretch(2, 2)
        layout.setRowStretch(1, 4)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GameWindow()
    window.show()

    sys.exit(app.exec_())