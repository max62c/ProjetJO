import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QLineEdit, QLabel, QHBoxLayout
from PyQt5.QtCore import Qt

class OlympicResultsGUI(QMainWindow):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Olympic Games Results')
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Search bar
        search_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Enter year to search...")
        search_button = QPushButton("Search")
        search_button.clicked.connect(self.search_results)
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(search_button)
        layout.addLayout(search_layout)

        # Results table
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(['Event', 'Gold', 'Silver', 'Bronze', 'Year'])
        layout.addWidget(self.table)

        # Scrape button
        scrape_button = QPushButton("Scrape New Data")
        scrape_button.clicked.connect(self.scrape_new_data)
        layout.addWidget(scrape_button)

    def search_results(self):
        year = self.search_input.text()
        if year.isdigit():
            results = self.db.fetch_results(int(year))
        else:
            results = self.db.fetch_results()

        self.populate_table(results)

    def populate_table(self, results):
        self.table.setRowCount(0)
        for row_num, row_data in enumerate(results):
            self.table.insertRow(row_num)
            for col_num, col_data in enumerate(row_data[1:]):  # Skip the ID column
                self.table.setItem(row_num, col_num, QTableWidgetItem(str(col_data)))

    def scrape_new_data(self):
        # This is where you would call your web scraping function
        # For now, we'll just print a message
        print("Scraping new data... (Not implemented)")

# Example usage:
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     db = OlympicDatabase("olympic_results.db")
#     gui = OlympicResultsGUI(db)
#     gui.show()
#     sys.exit(app.exec_())