## Inspiration
My first week of college involved meeting lots and lots of new people. Exchanging contact information with everyone was a pain. The only quick way to exchange a means of communication was Snapchat; Snapchat has a QR code that can be scanned to quickly send a friend request to another person. That got me thinking "if only there were something this simple for exchanging phone numbers."
## What it does
QR Connect is a quick way of exchanging contact information with others. Simply select what information you want to share and then generate a QR code with the push of a button. Another person can scan the QR code in the app, and it will create a new contact with the person's shared information
## How I built it
The Kivy package in Python streamlined the entire GUI. As for handling the QR codes, the qrcode Python package was used.
## Challenges I ran into
The Kivy package for GUIs almost has its own language built-in, so there was a learning curve with it. Also, the API for integrating the app directly with an API for Android devices was written in Java, so had I done more research into packages I could use for the project before beginning the code, I would have written it entirely in Java instead of Python. Using the camera to scan a QR code and show it on the screen is difficult; Kivy seems to be somewhat ill-equipt to work with live camera footage, and it also doesn't help that I can't get live camera footage in the first place without connecting it to the Android API
## Accomplishments that I'm proud of
The GUI was surprisingly fun to create and figure out from scratch. I would love to make it look a bit nicer, but for something developed in less than 24 hours, I think it looks pretty nice.
## What I learned
GUIs can be a bit harder to develop than I expected; I think I completely lucked out that Kivy exists and I found it. It simplified tons of the code for me, which gave me lots of extra time to figure out how to use and integrate the QR codes
## What's next for QR Connect
I have two main things on my mind for continuing this project:
1. Investigating the QR code generation. Currently, it seems that the QR code is always the same when the generate button is pressed. I want to be sure if this is a bug or not, and if it is, then I need to fix it
2. Properly implementing QR code scanning
3. Connecting the app to the Android API to actually make the app capable of what I set out to have it do. 
As it stands, this is more of a proof of concept than a finished app, as a few main features are either missing or potentially bugged.
