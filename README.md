## Snow Pier Games Website

#### Requirements
* [Python 3](https://www.python.org/downloads/)

#### Getting started
First you'll need to install the required python packages, most notably [Django](https://www.djangoproject.com/), a high-level Python web framework.
Do this by running the following command from the top-level directory of this repo.
```
cd (top_level_directory)
pip install -r requirements.txt
```

You'll also need to create a `(top_level_directory)/spgbackend/secrets.py` file, in which you'll need to define these
values:
```
secretkey = "secretkey"
db_host = ""
db_name = ""
db_password = ""
db_user = ""
mailchimp_api_key = ""
mailchimp_audience_id = ""
mailchimp_data_center = ""
email_host = ""
email_password = ""
email_user = ""
sendgrid_api_key = ""
```
If you are developing locally, they can all be assigned to an empty string (except for the secretkey, which Django
complains about being empty). If you need any of the actual values for testing purposes, contact one of the contributors
to this repository.

#### Running the web server
This command will start a local webserver.
```
python manage.py runserver
```
You should see the website by navigating to localhost:8000.
