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

You'll also need to provide Django with a secret key, which it uses for cryptographic signing.
If you're just developing locally, you can make this anything you want.
Assign its value in a new file called the `secrets.py`, which should be in the same directory as `settings.py`.
```
echo "secretkey = (your_generated_string)" > (top_level_directory)/spgbackend/secretkey.py
```
You will also need to assign the following variables some value in the `secrets.py` file:
    db_host, db_name, db_password, db_user,
    mailchimp_api_key, mailchimp_audience_id, mailchimp_data_center,
    email_host, email_password, email_user
The value can be the empty string if you are not testing email/subscriptions

#### Running the web server
This command will start a local webserver.
```
python manage.py runserver
```
You should see the website by navigating to localhost:8000.
