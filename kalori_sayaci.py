import PySide6 
import sys
import numpy as np
import pandas as pd
from PySide6 import *
from kalori import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        
        #minimum pencere boyutu
        self.setMinimumSize(850,600)
        
        # Kaydırma çubuğunu gizleyelim
        self.ui.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        
        
        #menu butonları ayarlama
        self.ui.pushButton.clicked.connect(lambda: self.page_1())
        self.ui.pushButton_2.clicked.connect(lambda: self.page_2())
        self.ui.pushButton_3.clicked.connect(lambda: self.slideLeftMenu())
        
        #Filtreleme fonksiyonları
        self.ui.lineEdit.textEdited.connect(lambda: self.filter())
        
        self.food_list()
        
        
        
        self.show()
    
    
    
    def filter(self):
        typed=self.ui.lineEdit.text()
        
        data=np.array([])
        
        for item in self.yemek_isimleri:
            if typed.lower() in item.lower():
                data=np.append(data,item)
                
        self.ui.listWidget.clear()
        
        for filtrelenmiş_yemek_isimleri in data:
            self.ui.listWidget.addItem(filtrelenmiş_yemek_isimleri)
                
        
    
    
    
    def slideLeftMenu(self):
        width= self.ui.menu.width()
        
        if width ==0:
            newWidth=200
        else:
            newWidth=0
            
        self.animation=QPropertyAnimation(self.ui.menu,b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()
        
    
    def food_list(self):
            self.yemekler=pd.read_json("yemekler.json")
            self.yemek_isimleri=self.yemekler["Yemek"].values
            
            for yemek_ismi in self.yemek_isimleri:
                self.ui.listWidget.addItem(yemek_ismi)
                
            
    
    
    def page_1(self):
        self.ui.label_3.setText("Yemek Listesi")
        self.ui.stackedWidget.setCurrentWidget(self.ui.yemekler)
    
    def page_2(self):
        self.ui.label_3.setText("Kalori Takibim")
        self.ui.stackedWidget.setCurrentWidget(self.ui.kalori)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Uygulamamızın arkaplanda çalışmasını sağlayalım.
    app.setQuitOnLastWindowClosed(False)
    window = MainWindow() 
    window.show()
    sys.exit(app.exec_())