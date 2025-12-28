from PyQt6.QtWidgets import QWidget, QRubberBand
from PyQt6.QtCore import QPoint, QRect, QSize, Qt

class AreaSelector(QWidget):
    def __init__(self):
        super().__init__()
        # Macht das Fenster rahmenlos und immer im Vordergrund
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.Tool)
        self.setWindowOpacity(0.3) # Halbtransparent
        self.setCursor(Qt.CursorShape.CrossCursor)
        
        # Den gesamten Bildschirm abdecken
        self.setGeometry(0, 0, 10000, 10000) # Grob über alle Monitore (vereinfacht)
        
        self.origin = QPoint()
        self.rubber_band = QRubberBand(QRubberBand.Shape.Rectangle, self)
        self.selected_region = None

    def mousePressEvent(self, event):
        self.origin = event.pos()
        self.rubber_band.setGeometry(QRect(self.origin, QSize()))
        self.rubber_band.show()

    def mouseMoveEvent(self, event):
        self.rubber_band.setGeometry(QRect(self.origin, event.pos()).normalized())

    def mouseReleaseEvent(self, event):
        self.rubber_band.hide()
        rect = self.rubber_band.geometry()
 
        # Der entscheidende Part: Abfrage des Skalierungsfaktors
        # Wir nehmen das aktuelle Fenster als Referenz für den Screen
        screen = self.screen()
        dpr = screen.devicePixelRatio() 
        
        # Skalierung der logischen GUI-Koordinaten in physische Pixel & Koordinaten speichern
        self.selected_region = {
            "top": int(rect.y() * dpr),
            "left": int(rect.x() * dpr),
            "width": int(rect.width() * dpr),
            "height": int(rect.height() * dpr)
        }
        self.close()