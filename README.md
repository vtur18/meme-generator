Meme-generator Project

Overview of the project:

The goal of this project is to build a "meme generator" to dynamically generate memes on an image 
with an overlaid quote. This application interacts with a variety of filetypes (PDF, Word Documents, 
CSVs, Text files). It will accept user input through a command-line tool and a web service. 

Instructions for setting up and running the program:

All folders and files uploaded are needed for the program to run. The programs and modules utilize 
public libraries which may need to be installed. The arial.tff font in base folder will need to be 
added.

The meme.py can be executed by running python3 meme.py. This will randomly generate memes which are 
stored in the ‘tmp’ folder.  To run with user specific criteria: python3 meme.py –path (location of 
your image) –body (your quote) –author (who wrote the quote) 

The app.py file can be excuted by running python3 app.py.  This will open up a webpage which you 
can copy the url to your web browser.  You can generate random memes by clicking on the Random button 
or Creator button to specify an image, quote, and author. In Creator, if a bad url is entered it will
return meme_bad_url.html page. The generated memes will be stored in the ‘static’ folder.

The following sample .jpg or .png url link can be used for example:

https://images.ctfassets.net/2y9b3o528xhq/5p7HANmA1jsw8P9EVOeVso/cbfa17357399d99a76d641c777e81a81/self-paced.png
https://images.ctfassets.net/2y9b3o528xhq/5sXS0Rr3MEr66P5elfYX7P/3728cc2d85c0979cb29d5cb291369038/mentor.jpg
https://www.spockthedog.com/wp-content/uploads/2017/01/its-harder-to-run-then-to-stay-still.jpg    
https://www.spockthedog.com/wp-content/uploads/2014/08/My-Firest-Day-At-The-Job.jpg        
https://www.spockthedog.com/wp-content/uploads/2014/08/Ready-For-A-Walk-Master.jpg       

Sub-modules:

The QuoteEngine module consists 
of different ingestors to pull quotes from CSV, Docx, PDF, Txt files into a [quotes, author] list.  
Random Images are scanned in meme.py and app.py and feed to MemeEngine module to add the quotes to the images.

Sources for this project:
Udacity class, knowledge base questions and answers and google searches.
