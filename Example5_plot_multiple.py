import sys
from PySide6.QtWidgets import QApplication, QMainWindow
# Alternatively use 'PyQt6'/'PyQt5' or 'PySide2' imports
import pyqtgraph as pg

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        plot = pg.PlotWidget()
        plot.setBackground('w')

        # data obtained from: https://rsf.org/en/index
        year = [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
        freedom_of_press_austria_ranking = [16, 16, 16, 14, 13, 7, 5, 5, 12, 12, 7, 11, 11, 11, 16, 18, 17, 31]
        freedom_of_press_swiss_ranking = [1, 9, 11, 7, 7, 6, 8, 8, 14, 15, 20, 7, 7, 5, 6, 8, 10, 14]
        
        pen_red = pg.mkPen(color=(255, 0, 0), width=5)              # create a pen to 'draw' the plot (red)
        pen_blue = pg.mkPen(color=(0, 0, 255), width=5)             # create a pen to 'draw' the plot (blue)
        plot.setTitle("Freedom of press index")
        styles = {'font-size':'20px'}
        plot.setLabel('left', 'Freedom of press ranking', **styles)
        plot.setLabel('bottom', 'Year', **styles)
        plot.showGrid(x=True, y=True)
        plot.addLegend()
        plot.plot(year, freedom_of_press_austria_ranking, pen=pen_red, name="Austria")      #plot the data with the specific pen
        plot.plot(year, freedom_of_press_swiss_ranking, pen=pen_blue, name="Switzerland")   #plot the data with the specific pen
        self.setCentralWidget(plot)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()