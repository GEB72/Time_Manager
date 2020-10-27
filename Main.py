from DataHandler import update_dict, get_from_pickler, sort_data, send_to_pickler
from UI import *
from datetime import datetime, timedelta
import multiprocessing
import sys


def timer_loop():
    get_from_pickler()

    while True:
        # checks if a minute has passed using computer time
        try:
            if datetime.now() - time_comparison > timedelta(minutes=1):
                send_to_pickler()
                del time_comparison
        except NameError:
            time_comparison = datetime.now()
        update_dict()


def terminate_program(QMainWindow):
    QMainWindow.close()

    # terminate ui_loop
    p1.terminate()


# initialise variable to track recent date_range button event
global current_state
current_state = 0


class MainWindow(QMainWindow):
    def __init__(self):
        # first ensure initial data is present
        get_from_pickler()

        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # allow window movement
        def window_move(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()
        self.ui.TitleFrame.mouseMoveEvent = window_move

        # remove title bar/ background
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # minimize event
        self.ui.btnMinimize.clicked.connect(lambda: self.showMinimized())

        # close event
        self.ui.buttonMinimize.clicked.connect(lambda: terminate_program(self))

        # set dateEdit initial values
        self.ui.dateEdit_3.setDate(QDate.currentDate())
        self.ui.dateEdit_4.setDate(QDate.currentDate())

        # hide events
        self.hide1 = False
        self.hide2 = False
        self.hide3 = False
        self.ui.pushButton_14.clicked.connect(lambda: self.hide_event(self.ui.textBrowser_4, self.hide1))
        self.ui.pushButton_15.clicked.connect(lambda: self.hide_event(self.ui.graphicsView, self.hide2))
        self.ui.pushButton_16.clicked.connect(lambda: self.hide_event(self.ui.graphicsView_2, self.hide3))

        self.ui.textBrowser_4.append("Application".ljust(25) + "\th:m")
        self.ui.textBrowser_4.append("")

        # add initial data
        for x in sort_data(0, 0):
            x[0] = x[0].ljust(25)
            text = "\t".join(x)
            self.ui.textBrowser_4.append(text)

        # sorting events
        self.ui.pushButton_7.clicked.connect(lambda: self.update_sort_data(self.ui.pushButton_7.text()))
        self.ui.pushButton_10.clicked.connect(lambda: self.update_sort_data(self.ui.pushButton_10.text()))
        self.ui.pushButton_11.clicked.connect(lambda: self.update_sort_data(self.ui.pushButton_11.text()))
        self.ui.pushButton_9.clicked.connect(lambda: self.update_sort_data(self.ui.pushButton_9.text()))
        self.ui.pushButton_8.clicked.connect(lambda: self.update_sort_data(self.ui.pushButton_8.text()))

        # custom date range event
        self.ui.btnMinimize_2.clicked.connect(self.custom_date_range)

        # use QTimer for update
        global current_state
        self.timer = QTimer()
        self.timer.timeout.connect(lambda: self.update_sort_data(current_state))
        self.timer.setInterval(1000)
        self.timer.start()

        # instantiate pie chart
        self.chart = QtCharts.QChart()
        self.chart.legend().setVisible(1)
        self.chart.legend().setAlignment(Qt.AlignRight)
        self.series = QtCharts.QPieSeries()
        self.chart.addSeries(self.series)
        self.ui.graphicsView.setChart(self.chart)
        self.ui.graphicsView.setRenderHint(QPainter.Antialiasing)
        self.chart.setBackgroundVisible(0)
        self.chart1 = QtCharts.QChart()
        self.ui.graphicsView_2.setChart(self.chart1)
        self.chart1.setBackgroundVisible(0)


        self.show()

    def hide_event(self, thing, boolean):
        if not boolean:
            thing.hide()
        else:
            thing.show()

        if thing.objectName() == "textBrowser_4":
            self.hide1 = not self.hide1
        elif thing.objectName() == "graphicsView":
            self.hide2 = not self.hide2
        elif thing.objectName() == "graphicsView_2":
            self.hide3 = not self.hide3

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def custom_date_range(self):
        global current_state
        current_state = "Custom"

    def update_sort_data(self, date_range):
        # adjust state, clear and populate browser
        global current_state

        # clear series and browser
        self.ui.textBrowser_4.clear()
        self.series.clear()
        self.ui.textBrowser_4.append("Application".ljust(25) + "\th:m")
        self.ui.textBrowser_4.append("")

        if current_state == "Custom":
            start_date = self.ui.dateEdit_3.text().replace("/","-")
            end_date = self.ui.dateEdit_4.text().replace("/","-")

            for z in sort_data(start_date, end_date):
                z[0] = z[0].ljust(25)
                self.series.append(z[0], self.get_seconds_val(z[1]))
                text2 = "\t".join(z)
                self.ui.textBrowser_4.append(text2)
            current_state = date_range
            return

        for y in sort_data(0, date_range):
            y[0] = y[0].ljust(25)
            self.series.append(y[0], self.get_seconds_val(y[1]))
            text2 = "\t".join(y)
            self.ui.textBrowser_4.append(text2)
        current_state = date_range

    def get_seconds_val(self, formatted_time):
        h, m = formatted_time.split(":")
        return int(h)*3600 + int(m)*60

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=timer_loop)
    p1.start()

    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
