Download the Folder(`Flask_Assessment`) <br>
Create a virtual environment using the following process:
1. pip install virtualenv
2. virtualenv my_name(flask_scrapping)

Activate the virtual env using the following:
1. On Windows using the Powershell: flask_scrapping\Scripts\activate.ps1
2. On Windows using the Command Promp: flask_scrapping\Scripts\activate.bat
3. On Unix or MacOS, using the bash shell: source flask_scrapping/bin/activate

After activating the environment `pip install Flask` to the virtual environment. <br>
create a `.env` file in the `Flask_Assessment` folder, not the `Youtube folder` and pass in your `Google Youtube Api`. <br>
You can get the API Key from `Google Cloud Platform` using https://cloud.google.com/ <br>
Once you generate the API Key, open the `.env file` and pass it as `YOUTUBE_API_KEY=` in the `Flask_Assessment folder` and not the `Youtube folder`. <br>

In the powershell, run the following process:
1. set FLASK_ENV=development
2. set FLASK_APP=__init__.py
3. Flask run

Once you are successful, click on the link: http://localhost:5000/ . Input the channel you trying to find at the end of the link e.g http://localhost:5000/JieJenn








