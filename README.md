[![install](https://github.com/nogibjj/Final_LG_JL_KM/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/Final_LG_JL_KM/actions/workflows/install.yml) 

[![format](https://github.com/nogibjj/Final_LG_JL_KM/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/Final_LG_JL_KM/actions/workflows/format.yml)

[![lint](https://github.com/nogibjj/Final_LG_JL_KM/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/Final_LG_JL_KM/actions/workflows/lint.yml) 

[![test](https://github.com/nogibjj/Final_LG_JL_KM/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/Final_LG_JL_KM/actions/workflows/test.yml)

# Book Buddy: 
Data Engineering Systems Final Project by Jiechen Li, Haliunaa Munkhuu, and Lilly Grella

## Project Goals:

This application intends to recommend a book based on a user-selected genre. 
The app has two pages: one focused on the selection of the genre and one focused on the resulting recommended book.
recommendation.py performs the recommendation process for the app.

## Using Book Buddy:

* Go to the following URL: `URL`
* Select Genre
* Click `Recommend Me!` and you will be redirected to a page with a recommend.
* At this point, you can click on the picture of the book that is recommended and you will be rerouted to the amazon page to purchase the book.
* Alternatively, if you want to be recommended a new book, click `Try Again!`

## Areas for Improvement:
* Improving the recommendation algorithm using machine learning techniques such as clustering

## Using AI Programming: 
* We used github CoPilot to aid in flask development
* We used codewhisperer and ChatGPT to help develop our front end code and the python recommendation code

## Building the App:
* Step 1: Write recommendation python code
* Step 2: Develop Flask code, developing URLs for different pages for our client, 
* Step 3: Develop HTML files/CSS code
* Step 4: Create Docker image for Azure to run the app
* Step 5: Deploy to Azure

## Dependencies:
* Recommendation Python Code: Pandas
* App Creation: Flask,HTML, CSS
* Build Tools: 
  * Linting: pylint
  * Testing: Pytest
  * Formatting: black
  * Deployment: Azure