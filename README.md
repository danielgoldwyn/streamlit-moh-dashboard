# Streamlit Malaysia COVID ICU Quick Stats page

This project was created as proof of concept of using data provided by the Malaysian Ministry of Health on Covid-19 case numbers

You can find the live version of this app [here](https://moh-covid.herokuapp.com/)!
_due to this being a free Heroku account allow for upto 30 seconds for dyno to startup_

## Using this code in your local maching

1. Ensure computer has python 3 installed
2. Clone this repo to your computer.
3. Navigate to root of cloned files
4. Create a virtual environment

```shell
python3 -m venv venv
```

5. Activate virtual environment

   1. For linux/mac

   ```bash
   source venv/bin/activate
   ```

   2. For Windows (cmd.exe)

   ```bash
   venv/Scripts/activate.bat
   ```

   3. For Windows (powershell)

   ```bash
   venv/Scripts/Activate.ps1
   ```

6. To install dependancies in virtual environment, first activate virtual environment and then key in

```shell
 pip install -r requirements.txt
```

7. Once all dependancies have been installed you can start the project on a localhost by typing

```shell
 streamlit run main.py
```

## Additional notes

1. Procfile, setup.sh, runtime.txt are only needed due to hosting a live version of this app on Heroku. It is not needed if you are running this on localhost.
2. runtime.txt sets the python version as 3.8.10 due to some conflict when uploading to Heroku which by default uses a more current version. Once the bug has been cleared on Heroku's side this file may not be needed to deploy this app onto Heroku
