import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_olympic_results(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # This is a placeholder for the actual scraping logic
    # You'll need to inspect the website's structure and adjust accordingly
    results = []
    tables = soup.find_all('table', class_='results-table')
    for table in tables:
        rows = table.find_all('tr')
        for row in rows[1:]:  # Skip header row
            columns = row.find_all('td')
            if len(columns) > 0:
                result = {
                    'event': columns[0].text.strip(),
                    'gold': columns[1].text.strip(),
                    'silver': columns[2].text.strip(),
                    'bronze': columns[3].text.strip()
                }
                results.append(result)
    
    return pd.DataFrame(results)

# Example usage
# df = scrape_olympic_results('https://olympics.com/fr/paris-2024')