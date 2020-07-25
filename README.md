# ZChatterbot
This is a simple chatbot using the Chatterbot library that can connect to Whatsapp using Twilio.

Note:
1.You will need to sign up for your own Twilio account (They've got free trials)
2.I intentionally left out the training data I used , given that it's a bunch of my whatsapp chat logs , so the github only has a dummy file called "data.txt" that you have to fill up yourself.
3.This approach is fine for a 'for fun' demo as I used Flask's inbuilt development server which according to the docs themselves are " not designed to be particularly efficient, stable, or secure" . However if you are serious about building a bot for production, you'd probably need to explore a "proper" Python  HTTP Server like Gnuicorn
