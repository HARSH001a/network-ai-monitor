# dashboard/widgets.py
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import pyqtgraph as pg
import numpy as np

class GaugeWidget(QWidget):
    def __init__(self, title, value, max_value=10, unit="Mbps"):
        super().__init__()
        self.title = title
        self.value = value
        self.max_value = max_value
        self.unit = unit
        self.setMinimumSize(150, 150)
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Calculate percentage
        percent = min(self.value / self.max_value, 1.0)
        
        # Draw gauge background
        rect = QRect(10, 10, self.width() - 20, self.height() - 50)
        painter.setPen(QPen(QColor(100, 100, 100), 2))
        painter.setBrush(QColor(50, 50, 50))
        painter.drawEllipse(rect)
        
        # Draw gauge value
        color = self.get_color(percent)
        painter.setPen(QPen(color, 8))
        start_angle = 90 * 16
        span_angle = -percent * 360 * 16
        painter.drawArc(rect, start_angle, span_angle)
        
        # Draw text
        painter.setPen(QColor(255, 255, 255))
        painter.setFont(QFont("Arial", 10))
        
        # Title
        painter.drawText(0, self.height() - 30, self.width(), 20,
                         Qt.AlignCenter, self.title)
        
        # Value
        value_text = f"{self.value:.2f} {self.unit}"
        painter.setFont(QFont("Arial", 14, QFont.Bold))
        painter.drawText(rect, Qt.AlignCenter, value_text)
    
    def get_color(self, percent):
        if percent < 0.5:
            return QColor(40, 167, 69)  # Green
        elif percent < 0.8:
            return QColor(255, 193, 7)   # Yellow
        else:
            return QColor(220, 53, 69)   # Red

class TrafficGraph(QWidget):
    def __init__(self, history_size=20):
        super().__init__()
        self.history_size = history_size
        self.inbound_data = []
        self.outbound_data = []
        self.setMinimumHeight(80)
        self.setMaximumHeight(120)
    
    def add_data(self, inbound, outbound):
        self.inbound_data.append(inbound)
        self.outbound_data.append(outbound)
        
        # Keep only last N values
        if len(self.inbound_data) > self.history_size:
            self.inbound_data = self.inbound_data[-self.history_size:]
            self.outbound_data = self.outbound_data[-self.history_size:]
        
        self.update()
    
    def paintEvent(self, event):
        if len(self.inbound_data) < 2:
            return
        
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        width = self.width()
        height = self.height()
        margin = 10
        
        # Draw background
        painter.fillRect(0, 0, width, height, QColor(40, 40, 40))
        
        # Calculate scaling
        max_value = max(max(self.inbound_data or [0]), max(self.outbound_data or [0]), 0.1)
        
        # Draw grid
        painter.setPen(QPen(QColor(80, 80, 80), 1))
        for i in range(0, 6):
            y = margin + (height - 2 * margin) * i / 5
            painter.drawLine(margin, y, width - margin, y)
        
        # Draw inbound line
        if len(self.inbound_data) > 1:
            self.draw_line(painter, self.inbound_data, max_value, 
                          QColor(0, 200, 255), "Inbound", width, height, margin)
        
        # Draw outbound line
        if len(self.outbound_data) > 1:
            self.draw_line(painter, self.outbound_data, max_value,
                          QColor(255, 100, 100), "Outbound", width, height, margin)
    
    def draw_line(self, painter, data, max_value, color, label, width, height, margin):
        painter.setPen(QPen(color, 2))
        
        points = []
        for i, value in enumerate(data):
            x = margin + (width - 2 * margin) * i / (len(data) - 1) if len(data) > 1 else width // 2
            y = height - margin - (height - 2 * margin) * (value / max_value)
            points.append(QPointF(x, y))
        
        for i in range(len(points) - 1):
            painter.drawLine(points[i], points[i + 1])
        
        # Draw label
        painter.setPen(color)
        painter.setFont(QFont("Arial", 8))
        painter.drawText(5, 15, label)

class PyQtGraphWidget(pg.PlotWidget):
    """Alternative using pyqtgraph for better performance"""
    def __init__(self):
        super().__init__()
        self.setBackground('k')
        self.showGrid(x=True, y=True, alpha=0.3)
        self.setLabel('left', 'Mbps')
        self.setLabel('bottom', 'Time')
        
        self.inbound_curve = self.plot(pen='c', name='Inbound')
        self.outbound_curve = self.plot(pen='r', name='Outbound')
        
        self.inbound_data = []
        self.outbound_data = []
        self.timestamps = []
    
    def add_data(self, inbound, outbound):
        from datetime import datetime
        self.timestamps.append(datetime.now())
        self.inbound_data.append(inbound)
        self.outbound_data.append(outbound)
        
        # Keep last 50 points
        keep = 50
        if len(self.timestamps) > keep:
            self.timestamps = self.timestamps[-keep:]
            self.inbound_data = self.inbound_data[-keep:]
            self.outbound_data = self.outbound_data[-keep:]
        
        # Update plot
        x = list(range(len(self.timestamps)))
        self.inbound_curve.setData(x, self.inbound_data)
        self.outbound_curve.setData(x, self.outbound_data)