import requests
from bs4 import BeautifulSoup
import pdfkit


def scrape_website(url):
    try:
        # Fetch HTML content from the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        html_content = response.text

        # Parse HTML using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract text content from the website
        website_text = soup.get_text(separator='\n')

        return website_text

    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


def save_as_pdf(text, filename):
    if not text:
        print("Error: Empty text content")
        return

    # Save text content to a PDF file
    options = {'no-images': None, 'disable-smart-shrinking': None, 'print-media-type': None, 'use-xserver': None}
    pdfkit.from_string(text, filename, options=options)

# Example usage:
# url = 'https://example.com'
# text = scrape_website(url)
# save_as_pdf(text, 'example.pdf')
