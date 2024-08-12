import sys
from PyQt5.QtWidgets import QApplication
from olympic_database import OlympicDatabase
from olympic_gui import OlympicResultsGUI
from olympic_scraper import scrape_olympic_results

class OlympicResultsApp:
    def __init__(self):
        self.db = OlympicDatabase("olympic_results.db")
        self.gui = OlympicResultsGUI(self.db)

    def run(self):
        self.gui.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    olympic_app = OlympicResultsApp()
    olympic_app.run()
    sys.exit(app.exec_())