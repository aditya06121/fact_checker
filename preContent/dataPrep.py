# TODO: implement fallback and proper error handling.

from preContent.scraper import scraper

def dataPrep(text):
    scraped_data = scraper(text)
    return scraped_data

if __name__=="__main__":
    print(dataPrep("https://www.bloomberg.com/news/articles/2025-06-06/apple-wwdc-2025-preview-ios-26-macos-26-new-ai-features-ipados-26-redesigns"))