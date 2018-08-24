This is an application that uses the Twilio API for WhatsApp, Beautiful Soup, and Python 3 to parse the Goodreads quotes webpage.

## To Run the Application
You will need a few things to run this application.

* [Python 3](https://www.python.org/downloads/) installed
* [Ngrok](https://ngrok.com/) to make your Flask app visible from the internet so Twilio can send requests to it 
* A Twilio account ([sign up for a free Twilio account here](http://twilio.com/try-twilio))
* Your [WhatsApp sandbox](https://www.twilio.com/console/sms/whatsapp/sandbox) set up in your Twilio account

### Prepare this Application
At the moment, only approved business accounts can use Twilio's WhatsApp API so we need to go on over to the [Twilio WhatsApp Sandbox](https://www.twilio.com/console/sms/whatsapp/sandbox) in our Twilio console. To activate it we must choose a Sandbox number, agree to the terms of WhatsApp, and select *Activate Sandbox*. 
![Twilio WhatsApp Sandbox](https://user-images.githubusercontent.com/8932430/44609408-5eb60200-a7ac-11e8-8c20-488463b86890.png)

To join a Sandbox, send “join <your sandbox keyword found in your console>” to your Sandbox number in WhatsApp and you should get a response confirming you’ve joined. You can follow these [instructions](https://www.twilio.com/docs/sms/whatsapp/api#twilio-sandbox-for-whatsapp) to install the [WhatsApp Sandbox](https://www.twilio.com/console/sms/whatsapp/sandbox) Channel in your account and [connect your WhatsApp account with the Sandbox](https://www.twilio.com/docs/sms/whatsapp/api#joining-a-sandbox).

Next, clone this application, `cd` into the directory and install the necessary libraries and modules with *pip3*.

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
Make sure you configure your Twilio phone number configured with that public-facing URL as shown in this handy [tutorial](https://www.twilio.com/docs/guides/how-to-set-up-your-python-and-flask-development-environment#create-a-simple-flask-application) and pass it to your WhatsApp number as shown below.
![](https://user-images.githubusercontent.com/8932430/44609419-64134c80-a7ac-11e8-8a1e-035868f63230.png)

Tada! You're now all set to build the rest of the app and should be able to send messages that look like this.
![Example WhatsApp message](https://user-images.githubusercontent.com/8932430/44609404-59f14e00-a7ac-11e8-8fde-821904f6e5a3.png)

