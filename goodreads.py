
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request 
import requests
import string
from bs4 import BeautifulSoup
import random, requests, bs4

def scrape_and_clean(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    
    #get quotes from page
    div_quotes = soup.find_all("div", attrs={"class":"quoteText"})
    corp = ''
    for q in div_quotes:
        author = ""
        # If no author, then skip
        try:
            author = q.find("a").get_text() + "\n"
        except:
            continue
        quote = ""
        # turn multiline quotes/poems into a single string
        for i in range(len(q.contents)):
            line = q.contents[i].encode("ascii", errors="ignore").decode("utf-8")
            if (line[0] == "<"): # is tag
                break
            else:
                quote += line
        q.contents[0] = quote

        quote = q.contents[0].encode("ascii", errors="ignore").decode("utf-8")
        quote = "\"" + quote.strip() + "\" "
        corp += quote + '-' + author + "#"
    quotes = filter(lambda x: x in string.printable, corp) #clean
    return quotes

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def send_sms():
    #incoming message
    msg = request.values.get("Body").lower()
    if msg == "popular": #main quotes page on Goodreads
        url = "https://goodreads.com/quotes"
    else:
        url = "http://www.goodreads.com/quotes/search?utf8=%E2%9C%93&q=" + msg
    quotes = scrape_and_clean(url).split("#")
    print("quotes ", quotes)
    quote = random.choice(quotes) + '\n\n' 
    print("quote ", quote)
    res = MessagingResponse()
    res.message(quote)
    return str(res)

if __name__ == '__main__':
    app.run(debug=True)