# dashboard/main_window.py (simplified version)
import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import darkdetect

# Import our panels
from dashboard.interface_panel import InterfacePanel
from dashboard.alert_panel import AlertPanel
from dashboard.log_viewer import LogViewer
from dashboard.settings_panel import SettingsPanel

# Create placeholder classes for missing imports
if 'LogViewer' not in globals():
    class LogViewer(QWidget):
        def __init__(self):
            super().__init__()
            layout = QVBoxLayout()
            layout.addWidget(QLabel("Log Viewer - Placeholder"))
            self.setLayout(layout)

if 'SettingsPanel' not in globals():
    class SettingsPanel(QWidget):
        def __init__(self):
            super().__init__()
            layout = QVBoxLayout()
            layout.addWidget(QLabel("Settings Panel - Placeholder"))
            self.setLayout(layout)

if 'AlertPanel' not in globals():
    class AlertPanel(QWidget):
        def __init__(self):
            super().__init__()
            layout = QVBoxLayout()
            layout.addWidget(QLabel("Alert Panel - Placeholder"))
            self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI Network Monitor - Dashboard")
        self.setGeometry(100, 100, 1400, 900)
        
        # Create a timer to simulate data updates
        self.timer = QTimer()
        self.timer.timeout.connect(self.simulate_data)
        
        # Setup UI
        self.setup_menu()
        self.setup_toolbar()
        self.setup_statusbar()
        self.setup_central_widget()
        
        # Apply theme
        self.apply_theme()
        
        # Start simulation timer
        self.timer.start(1000)  # Update every second
    
    def setup_menu(self):
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu("File")
        file_menu.addAction("Export Logs...")
        file_menu.addSeparator()
        file_menu.addAction("Exit", self.close)
        
        # View menu
        view_menu = menubar.addMenu("View")
        view_menu.addAction("Dark Theme", lambda: self.apply_theme('dark'))
        view_menu.addAction("Light Theme", lambda: self.apply_theme('light'))
    
    def setup_toolbar(self):
        toolbar = self.addToolBar("Main Toolbar")
        toolbar.setMovable(False)
        
        # Start/Stop buttons
        self.start_btn = QAction("▶ Start Monitoring", self)
        self.start_btn.triggered.connect(self.start_monitoring)
        toolbar.addAction(self.start_btn)
        
        self.stop_btn = QAction("⏹ Stop Monitoring", self)
        self.stop_btn.triggered.connect(self.stop_monitoring)
        self.stop_btn.setEnabled(False)
        toolbar.addAction(self.stop_btn)
        
        toolbar.addSeparator()
        toolbar.addAction("Refresh", self.refresh_data)
    
    def setup_statusbar(self):
        self.status_bar = self.statusBar()
        
        # Status indicators
        self.status_label = QLabel("Stopped")
        self.status_label.setStyleSheet("padding: 5px; background-color: #dc3545; color: white; border-radius: 3px;")
        self.status_bar.addWidget(self.status_label)
        
        # Interface count
        self.interface_label = QLabel("Interfaces: 0")
        self.status_bar.addPermanentWidget(self.interface_label)
        
        # Alert count
        self.alert_label = QLabel("Alerts: 0")
        self.status_bar.addPermanentWidget(self.alert_label)
    
    def setup_central_widget(self):
        # Create main splitter
        main_splitter = QSplitter(Qt.Horizontal)
        
        # Left panel: Interface monitoring
        self.interface_panel = InterfacePanel()
        main_splitter.addWidget(self.interface_panel)
        
        # Right panel: Tab widget
        right_tabs = QTabWidget()
        
        # Alert panel
        self.alert_panel = AlertPanel()
        right_tabs.addTab(self.alert_panel, "Alerts")
        
        # Log viewer
        self.log_viewer = LogViewer()
        right_tabs.addTab(self.log_viewer, "Logs")
        
        # Settings panel
        self.settings_panel = SettingsPanel()
        right_tabs.addTab(self.settings_panel, "Settings")
        
        main_splitter.addWidget(right_tabs)
        
        # Set initial sizes
        main_splitter.setSizes([700, 700])
        
        self.setCentralWidget(main_splitter)
    
    def apply_theme(self, theme=None):
        if theme is None:
            theme = 'dark' if darkdetect.isDark() else 'light'
        
        if theme == 'dark':
            self.setStyleSheet("""
                QMainWindow { background-color: #2b2b2b; }
                QLabel { color: #ffffff; }
                QPushButton { 
                    background-color: #3c3c3c; 
                    color: white; 
                    border: 1px solid #555; 
                    padding: 5px; 
                    border-radius: 3px;
                }
                QPushButton:hover { background-color: #4a4a4a; }
                QTabWidget::pane { border: 1px solid #555; }
                QTabBar::tab { 
                    background-color: #3c3c3c; 
                    color: white; 
                    padding: 8px; 
                    margin-right: 2px;
                }
                QTabBar::tab:selected { background-color: #505050; }
            """)
        else:
            self.setStyleSheet("""
                QMainWindow { background-color: #f0f0f0; }
                QLabel { color: #000000; }
                QPushButton { 
                    background-color: #e0e0e0; 
                    color: black; 
                    border: 1px solid #aaa; 
                    padding: 5px; 
                    border-radius: 3px;
                }
                QPushButton:hover { background-color: #d0d0d0; }
            """)
    
    def start_monitoring(self):
        self.start_btn.setEnabled(False)
        self.stop_btn.setEnabled(True)
        self.status_label.setText("Monitoring")
        self.status_label.setStyleSheet("padding: 5px; background-color: #28a745; color: white; border-radius: 3px;")
        print("Monitoring started")
    
    def stop_monitoring(self):
        self.start_btn.setEnabled(True)
        self.stop_btn.setEnabled(False)
        self.status_label.setText("Stopped")
        self.status_label.setStyleSheet("padding: 5px; background-color: #dc3545; color: white; border-radius: 3px;")
        print("Monitoring stopped")
    
    def refresh_data(self):
        print("Refreshing data...")
    
    def simulate_data(self):
        """Simulate network data for testing"""
        import random
        
        simulated_data = {
            "eth0": {
                "in": random.uniform(0, 8.0),
                "out": random.uniform(0, 3.0)
            },
            "wlan0": {
                "in": random.uniform(0, 2.0),
                "out": random.uniform(0, 1.0)
            },
            "lo": {
                "in": random.uniform(0, 0.1),
                "out": random.uniform(0, 0.1)
            }
        }
        
        self.interface_panel.update_data(simulated_data)
        self.interface_label.setText(f"Interfaces: {len(simulated_data)}")