# dashboard/settings_panel.py
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class SettingsPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout()
        
        # Threshold settings
        group = QGroupBox("Threshold Settings")
        form_layout = QFormLayout()
        
        self.wifi_in = QDoubleSpinBox()
        self.wifi_in.setRange(0, 100)
        self.wifi_in.setValue(1.0)
        
        self.wifi_out = QDoubleSpinBox()
        self.wifi_out.setRange(0, 100)
        self.wifi_out.setValue(0.5)
        
        form_layout.addRow("WiFi Inbound (Mbps):", self.wifi_in)
        form_layout.addRow("WiFi Outbound (Mbps):", self.wifi_out)
        
        group.setLayout(form_layout)
        layout.addWidget(group)
        
        # Save button
        save_btn = QPushButton("Save Settings")
        layout.addWidget(save_btn)
        
        layout.addStretch()
        self.setLayout(layout)