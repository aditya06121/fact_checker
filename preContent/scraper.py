#TODO: implement fall back later...

from newspaper import Article
import re
import unicodedata

def normalize_text(text):
    """
    Normalize text: lowercasing, Unicode cleanup, remove URLs, special chars, and whitespace.
    """
    # Unicode normalization
    text = unicodedata.normalize("NFKC", text)

    # Lowercase (only if using an uncased BERT model)
    text = text.lower()

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)

    # Remove HTML-like tags
    text = re.sub(r"<.*?>", "", text)

    # Remove special characters (preserve basic punctuation)
    text = re.sub(r"[^a-zA-Z0-9\s.,!?'-]", "", text)

    # Normalize whitespace
    text = re.sub(r"\s+", " ", text).strip()

    return text

def scraper(url):
    article = Article(url)
    article.download()
    article.parse()
    
    # Raw cleaning
    clean_text = article.text.replace('\t', '').replace('\n', '').replace('\r', '').replace('\\','')
    
    # Normalize the cleaned text
    normalized_text = normalize_text(clean_text)
    return f"{article.title} </s> {normalized_text}"

if __name__=="__main__":
    print(scraper("https://www.thehindu.com/news/international/elon-musk-slams-ingratitude-after-trumps-very-disappointed-remark/article69662452.ece"))