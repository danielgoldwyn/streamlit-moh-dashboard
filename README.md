# Streamlit Malaysia COVID ICU Quick Stats page

This project was created as proof of concept of using data provided by the Malaysian Ministry of Health on Covid-19 case numbers

## Using this code in your local maching

1. Clone this repo to your computer.
2. Create a virtual environment and install the dependancies from requirements.txt
3. To install dependancies in virtual environment, first activate virtual environment and then key in
   '''shell
   pip install -r requirements.txt
   '''
4. Once all dependancies have been installed you can start the project on a localhost by typing
   '''shell
   streamlit run main.py
   '''

## Additional notes

1. Procfile, setup.sh, runtime.txt are only needed due to hosting a live verion of this app on Heroku. It is not needed if you are running this on localhost.
2. runtime.txt sets the python version as 3.8.10 due to some conflict when uploading to Heroku which by default uses a more current version. Once the bug has been cleared on Heroku's side this file may not be needed to deploy this app onto Heroku

You can find the live version of this app [here](https://moh-covid.herokuapp.com/)!
