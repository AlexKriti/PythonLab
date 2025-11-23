import requests
from bs4 import BeautifulSoup
import csv
import time
import os
import sys
import re

class CountryDataScraper:
    def __init__(self, input_file="countries.txt", output_file="countries_data.csv", cache_dir="cache"):
        self.input_file = input_file
        self.output_file = output_file
        self.cache_dir = cache_dir
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        
        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)
    
    def get_cached_page(self, country):
        cache_file = os.path.join(self.cache_dir, f"{country.replace(' ', '_')}.html")
        if os.path.exists(cache_file):
            with open(cache_file, 'r', encoding='utf-8') as f:
                return f.read()
        return None
    
    def save_to_cache(self, country, content):
        cache_file = os.path.join(self.cache_dir, f"{country.replace(' ', '_')}.html")
        with open(cache_file, 'w', encoding='utf-8') as f:
            f.write(content)
    
    def fetch_country_page(self, country):
        cached_content = self.get_cached_page(country)
        if cached_content:
            return cached_content
        
        url = f"https://en.wikipedia.org/wiki/{country.replace(' ', '_')}"
        try:
            response = self.session.get(url)
            response.raise_for_status()
            self.save_to_cache(country, response.text)
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching {country}: {e}")
            return None
    
    def parse_number(self, text):
        if not text:
            return None
        text = re.sub(r'[^\d.]', '', text.split('[')[0])
        try:
            return float(text) if '.' in text else int(text)
        except ValueError:
            return None
    
    def extract_country_data(self, html, country):
        if not html:
            return None, None, None
        
        soup = BeautifulSoup(html, 'html.parser')
        
        capital = None
        area = None
        population = None
        
        try:
            infobox = soup.find('table', {'class': 'infobox'})
            if not infobox:
                return None, None, None
            
            rows = infobox.find_all('tr')
            
            for row in rows:
                headers = row.find_all('th')
                cells = row.find_all('td')
                
                if len(headers) > 0 and len(cells) > 0:
                    header_text = headers[0].get_text().strip().lower()
                    
                    if 'capital' in header_text and not capital:
                        capital_links = cells[0].find_all('a')
                        if capital_links:
                            capital = capital_links[0].get_text().strip()
                    
                    elif 'area' in header_text and not area:
                        area_text = cells[0].get_text().split('km')[0].strip()
                        area = self.parse_number(area_text)
                    
                    elif 'population' in header_text and not population:
                        population_text = cells[0].get_text().split('[')[0].strip()
                        population = self.parse_number(population_text)
            
            if not population:
                population_row = infobox.find('tr', string=re.compile('Population'))
                if population_row and population_row.find_next_sibling('tr'):
                    population_cell = population_row.find_next_sibling('tr').find('td')
                    if population_cell:
                        population_text = population_cell.get_text().split('[')[0].strip()
                        population = self.parse_number(population_text)
                        
        except Exception as e:
            print(f"Error parsing {country}: {e}")
        
        return capital, area, population
    
    def read_countries(self):
        try:
            with open(self.input_file, 'r', encoding='utf-8') as f:
                return [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print(f"Input file {self.input_file} not found")
            return []
    
    def write_csv(self, data):
        try:
            with open(self.output_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['country', 'city', 'area', 'population'])
                writer.writerows(data)
            print(f"Data saved to {self.output_file}")
        except Exception as e:
            print(f"Error writing CSV: {e}")
    
    def run(self):
        countries = self.read_countries()
        if not countries:
            return
        
        results = []
        
        for i, country in enumerate(countries):
            print(f"Processing {country} ({i+1}/{len(countries)})")
            
            html = self.fetch_country_page(country)
            capital, area, population = self.extract_country_data(html, country)
            
            results.append([country, capital or 'N/A', area or 'N/A', population or 'N/A'])
            
            if i < len(countries) - 1:
                time.sleep(1)
        
        self.write_csv(results)
        print(f"Completed! Processed {len(results)} countries")

def main():
    input_file = "countries.txt"
    output_file = "countries_data.csv"
    
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    if len(sys.argv) > 2:
        output_file = sys.argv[2]
    
    scraper = CountryDataScraper(input_file, output_file)
    scraper.run()

if __name__ == "__main__":
    main()