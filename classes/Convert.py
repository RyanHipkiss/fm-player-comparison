from bs4 import BeautifulSoup
import csv

class Convert:
    def __init__(self, html_file, csv_file):
        self.html_file = html_file
        self.csv_file = csv_file
        
    def read_html(self):
        with open(self.html_file, 'r', encoding='utf-8') as f:
            self.contents = f.read()
        self.soup = BeautifulSoup(self.contents, 'html.parser')
        self.table = self.soup.find('table')
        
    def get_headers(self):
        return self.table.find_all('th')
        
    def get_rows(self):
        return self.table.find_all('tr')
        
    def convert(self):
        self.read_html()
        headers = self.get_headers()
        
        with open(self.csv_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([header.text for header in headers])
            
            rows = self.get_rows()
            for row in rows:
                cells = row.find_all('td')
                writer.writerow([cell.text for cell in cells])

    def getCsvContent(self):
        content = []
        with open(self.csv_file, 'r', encoding='utf-8') as f:
            # Skip the first row (headers)
            next(f)
            reader = csv.reader(f)
            for row in reader:
                if any(cell.strip() for cell in row):  # Check if row has non-empty values
                    content.append(row)
        return content