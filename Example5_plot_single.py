import sys
from PySide6.QtWidgets import QApplication, QMainWindow
# Alternatively use 'PyQt6'/'PyQt5' or 'PySide2' imports
import pyqtgraph as pg

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        plot = pg.PlotWidget()                                                  # create a plot widget
        plot.setBackground('w')                                                 # set the background color to white

        # data obtained from: https://rsf.org/en/index
        year = [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
        freedom_of_press_austria_ranking = [16, 16, 16, 14, 13, 7, 5, 5, 12, 12, 7, 11, 11, 11, 16, 18, 17, 31]

        pen = pg.mkPen(color=(255, 0, 0), width=5)                              # create a pen to 'draw' the plot
        plot.setTitle("Freedom of press index - Austria")                       # set the title of the plot
        styles = {'font-size':'20px'}                                           # prepare a style
        plot.setLabel('left', 'Freedom of press ranking', **styles)             # label the y axis
        plot.setLabel('bottom', 'Year', **styles)                               # label the x axis
        plot.showGrid(x=True, y=True)                                           # display the grid of the plot
        plot.plot(year, freedom_of_press_austria_ranking, pen=pen)              # plot the provided data
        self.setCentralWidget(plot)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()