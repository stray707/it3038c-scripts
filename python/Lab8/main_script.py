import quotescraper
import urlscraper
import htmlprettify

def main():
    print("Select an option:")
    print("1. Quote Scraper")
    print("2. URL Scraper")
    print("3. HTML Prettify")

    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        run_quote_scraper()
    elif choice == "2":
        run_url_scraper()
    elif choice == "3":
        run_html_prettify()
    else:
        print("Invalid choice!")

def run_quote_scraper():
    print("Running Quote Scraper...\n")
    # You can call any function or directly execute the script content here.
    # As of your provided content, the quotescraper script runs code directly. 
    # For simplicity, I'm treating the scripts as runnable code directly.
    quotescraper


def run_url_scraper():
    print("Running URL Scraper...\n")
    urlscraper

def run_html_prettify():
    print("Running HTML Prettify...\n")
    htmlprettify



if __name__ == "__main__":
    main()