# dashboard/alert_panel.py
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class AlertPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout()
        
        # Toolbar
        toolbar = QHBoxLayout()
        clear_btn = QPushButton("Clear All")
        export_btn = QPushButton("Export Alerts")
        toolbar.addWidget(clear_btn)
        toolbar.addWidget(export_btn)
        toolbar.addStretch()
        layout.addLayout(toolbar)
        
        # Alert list
        self.alert_list = QListWidget()
        layout.addWidget(self.alert_list)
        
        self.setLayout(layout)