
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request 
from bs4 import BeautifulSoup
import requests, string, random

def scrape_and_clean(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content)
    
    #get quotes from page
    #div_quotes = soup("div", attrs={"class":"quoteText"}) #soup("div") == soup.find_all("div")
    quotes = ''
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
            #find returns
            line = q.contents[i].encode("ascii", errors="ignore").decode("utf-8")
            print("line ", line)
            if (line[0] == "<"): # is tag, ignore characters that aren't part of quote 
                break
            else:
                quote += line

        quote = q.contents[0].encode("ascii", errors="ignore").decode("utf-8")
        quote = "\"" + quote.strip() + "\""
        quotes += quote + '\n\n' + '-' + author + "#"
    quotes_to_return = filter(lambda x: x in string.printable, quotes) #clean
    return quotes_to_return

app = Flask(__name__)
@app.route('/whatsapp', methods=['POST'])
def send_sms():
    #incoming message
    msg = request.values.get("Body").lower()
    if msg == "popular": #main quotes page on Goodreads
        url = "https://goodreads.com/quotes"
    else:
        url = "http://www.goodreads.com/quotes/search?utf8=%E2%9C%93&q=" + msg # + "%32" + "commit=Search" utf8=✓&q=
    quotes = "".join(scrape_and_clean(url)).split("#")
    print("all quotes ", quotes)
    #quotes.split("#")
   
    if len(quotes) == 1:
        quote = quotes.pop()
    elif len(quotes) == 0:
        quote = "no tags, try another one like \'jane austen\', \'harry potter\', or \'lord of the rings\'."
    else:
        quote = random.choice(quotes) + '\n\n' 
    print("random quote ", quote)
    res = MessagingResponse()
    res.message(quote)
    return str(res)

if __name__ == '__main__':
    app.run(debug=True)