# naturetrust


## Contents 


- [Deployment](#deployment)

    - [Heroku](#heroku)

    - [AWS](#aws)


-----

## Deployment


### Heroku

1. First you will need Heroku's `PostGres` add on to ensure that the sqlite file-based database can work once deployed. Search for PostGres in  the **Resources** tab in Heroku. 

2. Add the add on. You will now see a `DATABASE_URL` within the config vars.

3. Install the following packages to your app: `pip3 install dj-database-url`, `pip3 install psycopg2-binary`

4. Import dj-database-url in your settings.py file: `import dj_database_url`

5. To get database to work on the deployed version, we need to tell the app to use the PostGres `DATABASE_URL` from Heroku. To test that first locally, comment out the default configuration for the database settings and replace the default database with a call to `dj_database_url.parse(<URL_from_heroku_config_vars>)`.

6. Remember, because you are now connected to Postgres, you need to run migrations again with `python3 manage.py migrate`.

7. Since we’re now using a different database, it won’t have any of our models or user information in it. To fix that, we need it to match the sqlite3 database by importing all of your data by using your fixtures, using the following command syntax: `python3 manage.py loaddata <object>`. Ensure that any tables with dependencies are loaded first to avoid any issues. For this project, I made the loadata commands in the following order:
```
python manage.py loaddata games
python manage.py loaddata editions
python manage.py loaddata sections
python manage.py loaddata content

python3 manage.py loaddata adoptions
python3 manage.py loaddata packages
```

8. Finally, set your superuser again so that it can work in the deployed site, using `python3 manage.py createsuperuser`.

9. The database will now work on the deployed version with Heroku, however, we still want to use the default database setting when running the project locally. To fix this issue you need to connect to sqlite when using the local version, and postgres for the deployed version. Do so by replacing your database settings to the following:
```
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
```

10. To ensure that the databases work correctly, we need a few things. First install **unicorn** using `pip3 install gunicorn`. Don't forget to update your requirements.txt by using `pip3 freeze > requirements.txt`.

11. Now you can create your Procfile to tell Heroku to create a web dyno which will run unicorn and serve our django app, using the following syntax: `web: gunicorn <app_name>.wsgi:application`. In my case, this is: `web: gunicorn legion.wsgi:application`

12. If you aren't logged in to Heroku already, log in via the CL using `heroku login -i`. You also may need to initialize your heroku git remote, using: `heroku git:remote -a <appname>`

13. Temporarily disable `collectstatic` so that Heroku won't collect static files when deploying the app, using `heroku config:set DISABLE_COLLECTSTATIC=1 --app <appname>`. This will be added to your config vars in Heroku.

14. Add the hostname of your Heroku app to `allowed_hosts` in `settings.py`. Add localhost also so that your local version will still work. **Note** if you are using Visual Studio code, then you may need to add or change `localhost` to '127.0.0.1' to ensure that the application can still run locally. Below is what it may look like in your settings:
```
ALLOWED_HOSTS = ['naturetrust.herokuapp.com', 'localhost', '127.0.0.1']
```

15. Commit changes and push to GitHub. Then push to heroku by using `git push heroku master`.

16. Within Heroku, navigate to the **Deploy** tab and **Enable Automatic Deploys** to sync Heroku to your GitHub repository.

17. Generate a secret Django key using a generator, and add it to your config variables in Heroku. Then in your` setting.py` file, update your `SECRET_KEY` settings and your `Debug` settings to the following:
```
SECRET_KEY = os.environ.get('SECRET_KEY', '')

DEBUG = 'DEVELOPMENT' in os.environ
```


### AWS

Amazon AWS was used to store the application's static and media files. Listed below are the required steps to get AWS running correctly.

Create an AWS account and work your way through the registration process. 

#### Create Bucket

1. Once your account is created, navigate to the services tab and searh for **S3**, click on it to get started.

2. Create a new bucket via the AWS S3 service by clicking the `create bucket` button. 

3. Enter your bucket name. It's good practice to name the bucket to match the Heroku app name. In my case, my bucket name was `naturetrust`, which matches the name on Heroku.

4. Select the region that is closest to you and uncheck `block all public access` and acknowledge that the bucket will be public.

5. Click `create bucket` to create your bucket.


#### Bucket Settings

1. Click on your new bucket to navigate to its settings.

2. Once there, first click the **properties** tab to turn on static website hosting.

3. Scroll down to **Static website hosting** and click edit. Ensure that `static website hosting` is enabled, and add the default values to index document and error document, which would be 'index.html' and 'error.html'. Once done, click **save changes**.

4. Next, navigate to the **permissions** tab, and scroll down to the **Cross-origin resource sharing (CORS)** section. Click the edit button and paste in the following code:
```
[
    {
        "AllowedHeaders": [
            "Authorization"
        ],
        "AllowedMethods": [
            "GET"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": []
    }
]
```

5. Then navigate to **Bucket policy** and click the edit button. Click **Policy generator** to generate a security policy for your bucket. 

6. Choose `S3 Bucket Policy` for your **policy type**.

7. Allow **all** principles by adding a `*` to the **Principal** field.

8. Select `Get Object` in the **Actions** select field.

9. Copy the **Amazon ARN** from the previous tab (your bucket policy tab) and copy your `Bucket ARN` and paste it into the **Amazon Resource Name ARN** field.

10. Click **Add statement** and then **Generate policy**, and then copy the generated policy into the bucket policy editor. Before you click save, add `/*` to the end of your Resource url to allow full access to all resources in the bucket. It may look something like this:
```
"Resource": "arn:aws:s3:::naturetrust/*"
```

11. Finally, navigate to the **Access Control List** section, still within the Permissions tab, to set the **List Objects** permission to **Everyone** under the **Public Access** section.


#### Create a User Access

1. Navigate to the AWS Services menu and search for **IAM**. IAM stands for Identity and Access Management and will allow a user to access the S3 bucket we have created.

2. First we want to create a group for our user to live in. To do that, click on the **User Groups** tab in the sidenav, and create a new group by clicking the **Create group** button to your right. Give the group a name that is relevant to your application and purpose. In my case, I named the group `manage-legion-app`. Click **Create group** to create your new group.

3. Next, navigate to the **Policies** tab in the sidenav and click **Create Policy**.

4. Navigate to the JSON tab and click **Import managed policy** to import a AWS pre-built policy for full access to S3.

5. Search for **S3** and then import the **AmazonS3FullAccess** policy.

6. However we only want full access to *our* bucket and everything within it, to do that we are going to create a group access policy to give group access to the S3 bucket we have created.

7. Using a new tab so you don't loose the one you are currently on, navigate to the **bucket policy page** in S3 to get the bucket ARN. Paste that into **Resources** inside the JSON tab inside **IAM**. You'll also want to add another rule for all files and folders in the bucket. Look below for an example:
```
"Statement": [
    {
        "Effect": "Allow",
        "Action": "s3:*",
        "Resource": [
            "arn:aws:s3:::naturetrust",
            "arn:aws:s3:::naturetrust/*"
        ]
    }
]
```

8. Click Next, and next again to navigate to **Review Policy**. Give your policy a name and description then click **Create Policy**.

9. Now navigate back to the **User Groups** tab in the sidenav and click on the group you create before. In the **Permissions** tab, click **Add Permissions** and then **Attach Policies**. Search for the policy you just created, check it and click **Add Permissions**. 

10. Finally, we want to assign the user to the group, so that it can use the policy to access the files within the application.

11. Navigate to the **Users** tab in the sidenav and click **Add User**. Create a user using the following syntax `<appname>-staticfiles-user`, which in my case is, `naturetrust-staticfiles-user`, give them **programmatic access** and select **Next**.

12. Now you and add the user to your group with the policy attached by clicking on the group name you just created.

13. Click through until the end and click **Create user**.

14. Finally click **Download .csv** - a CSV file containing the user access key and secret access key - which you will use in the Django app. Note that you cannot go through this process again so ensure that you keep this file safe.


#### Connect to Django and Add Static Files

1. Add the AWS **Access Key ID** and **Secret Access Key** that you just downloaded in the previous step to your config vars in Heroku. Also add the variable `USE_AWS: True`.

2. In your project, install the boto3 and django-storages using the following commands: `pip3 install boto3`, `pip3 install django-storages`. Remember to freeze your requirements.txt file by using the command: `pip freeze > requirements.txt`.

3. Add storages to your installed apps.

4. Next we need to tell Django which bucket it should be communicating with. We’ll only want to do this on Heroku so use an if statement to check if there’s an environment variable called `USE_AWS` in the environment, and if so define the `AWS_STORAGE_BUCKET_NAME` and `AWS_S3_REGION_NAME` and also the access key and secret access key which we’ll get from the environment. Additionally, you need to tell Django where the static files will be coming from in production, which is going to be the bucket name from AWS, stored inside the `AWS_S3_CUSTOM_DOMAIN`. It’s very important to keep these keys secret, because if they end up in version control, someone could use them to store or move data through your S3 bucket and Amazon would charge your card.

5. Your settings file may now look something like this:
```
if 'USE_AWS' in os.environ:
    AWS_STORAGE_BUCKET_NAME = 'naturetrust'
    AWS_S3_REGION_NAME = 'eu-west-2'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
```

6. If it exists, remove the `DISABLE_COLLECTSTATIC` from your Heroku config vars as this time django will collect static files automatically and upload them to S3.

7. The next step is to tell Django that in production, we want to use S3 to store static files whenever someone runs `collectstatic`, and that any uploaded product images should go there also. To do that create a new py file called `custom_storages.py` and import your settings and s3boto3 storage class. Paste the following code inside:
```
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```

8. The last step is to go to `settings.py` and tell it that we want to use our storage class for static file storage, and that the location it should save static files to is a folder called **static**, and then do the same thing for media files. We also need to override and explicitly set URLS for static and media files using our custom domain and the new locations. Add the following code below the code you added in **step 5**:
```
# Static and media files
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATICFILES_LOCATION = 'static'
DEFAULT_FILE_LOCATION = 'custom_storages.MediaStorage'
MEDIAFILES_LOCATION = 'media'

# Override static and media URLS in production
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```

9. Add `AWS_S3_OBJECT_PARAMETERS` to tell the browser it’s okay to cache static files for a long time to improve performance:
```
AWS_S3_OBJECT_PARAMATERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000',
}
```

#### Add Media Files to S3

1. Navigate to your bucket in S3 and create a **new folder** called **media**.

2. Inside click **upload** and select all images from your project directory.

3. Under the **Permissions** tab, check **Grant public read-access** to these objects.

4. Click Upload to upload your media files.



### Stripe and Heroku

1. Create a Stripe account if you haven't done so already and navigate to **API Keys** under the **Developers** tab.

2. From there, find and copy `STRIPE_PUBLIC_KEY` and `STRIPE_SECRET_KEY` and paste them into the Heroku config vars. Give them the same name so that they can be accessed by your application.

3. To setup a webhook, navigate to to the **Webhooks** tab on Stripe, and click **Add Endpoint**. In there paste in the appropriate url for your application. For me this was `
https://naturetrust.herokuapp.com/checkout/wh/` and check *recieve all events**. Add the endpoint.

4. You can now reveal your webhook signing secret, which you can add to Heroku config variables as done before. 

5. Ensure all your variable names match the names defined in `settings.py`.

6. Send a test webhook from Stripe to ensure that the listener is working by clicking **send test webhook**.
