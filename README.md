This is an application that uses the Twilio API for WhatsApp, Beautiful Soup, and Python 3 to parse the Goodreads quotes webpage.

## To Run the Application
You will need a few things to run this application.

* [Python 3](https://www.python.org/downloads/) installed
* [Ngrok](https://ngrok.com/) to make your Flask app visible from the internet so Twilio can send requests to it 
* A Twilio account ([sign up for a free Twilio account here](http://twilio.com/try-twilio))
* Your [WhatsApp sandbox](https://www.twilio.com/console/sms/whatsapp/sandbox) set up in your Twilio account

### Prepare this Application

Clone the application, `cd` into the directory and install the necessary libraries and modules with *pip3*.

```bash
git clone https://github.com/elizabethsiegle/parse-html-for-top-goodreads-quotes-with-sms 
cd parse-html-for-top-goodreads-quotes-with-sms
pip3 install requests twilio flask string bs4 random 
```
If this throws permission errors run `pip3 install --user [package]`. 

On the command line in that directory run 
```bash
python goodreads.py
``` 
and then open up a new terminal tab, get to the directory with your code, and run
```bash
ngrok http 5000
```
Make sure you configure your Twilio phone number configured with that public-facing URL as shown in this handy [tutorial](https://www.twilio.com/docs/guides/how-to-set-up-your-python-and-flask-development-environment#create-a-simple-flask-application).

You're now all set to build the rest of the app!