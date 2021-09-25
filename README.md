# NATURETRUST

[View live project here](https://naturetrust.herokuapp.com/)

![Mockup](documentation/media/mockup.jpg)

[NATURETRUST](https://naturetrust.herokuapp.com/) is an aspiring e-commerice site which aims to create a collaborative relationship between gaming companies and charitable organisations to help contribute towards the planet's sustainabilty. Users can buy games or adoptions pack on the site, and by purchasing with NatureTrust they can contribute towards an environmental charity. The bussiness schema behind Naturetrust is: for each game purchased with, Naturetrust will contribute 12% of its total price to one of the partnered charities. Adoption packs would count towards a 70% donation to the associated charity.

Naturetrust aims to bring awareness to vital role many wildlife plays in the ecosystem. These are often not the animals you would typically see in adoption packs for many renowned charities, but that is what makes Naturetrust unique. Currently, NatureTrust offers adoption packs for bees, sharks, and even plankton,
because we recognise that losing them could be detrimental for everyone living on Earth. 

PLEASE NOTE: This website is a business concept created as a milestone project to be assessed. I do not own any rights to the game content used in this site, and do not affiliate with these companies, nor do I accept real payments or sell real keys and/or adoption packs.


## Contents 

- [UX](#ux)

    - [Strategy Plane](#strategy-plane)

    - [User Stories](#user-stories)

    - [Scope Plane](#scope-plane)
    
    - [Skeleton Plane](#skeleton-plane)

    - [Surface Plane](##surface-plane)

- [Database Schema](#database-schema)

- [Accessibility](#accessibility)

- [Technologies Used](#technologies-used)

- [Testing](#testing)

- [Deployment](#deployment)

    - [Heroku](#heroku)

    - [AWS](#aws)

- [Credits](#credits)


-----

## UX


### Strategy Plane

#### Project Goals 

The primary aim of this website is to sell games and adoption packs, and contribute a percentage of those profits to charities that help protect the ecosystem. I also wish to spread awareness about some of these animals in order to encourage people to take better care of the earth.


#### Site Owner Goals

The primary goal is to establish a community platform that would have the potential to grow and thrive as a real-world application. It is imperative that the application has a high-quality layout and UX design, meets acccessibility guidelines, prioritizes its information appropriately and handles the back-end intuitively. 

#### Target Audience 

The primary target audience is gamers as the main product that is sold will be games. However the site is suitable for any target audience who wish to purchase a a game and/or adoption pack.


-----


### User Stories


#### Viewing and Navigation

![User stories](documentation/media/user-stories-1.png)


#### Registration and User Accounts

![User stories](documentation/media/user-stories-2.png)


#### Making a Purchase at Checkout

![User stories](documentation/media/user-stories-3.png)


-----


### Scope Plane


#### Functional Specifications and Requirements

- Good UX design that is repsonsive, user friendly and easy to navigate.

- Clear and accessible navigation options for the site. This can be in the form of a fixed navbar at the top of the page, which will allow users to navigate to any part of the site easily and efficiently.

- Data must be dynamic, and must be organised in a way that is intuitive and clear.

- The site should not restrict users who are not logged in. Users should be able to purchase items without the need to create an account.

- The site should be intuitive and enjoyable for the user.




-----


### Skeleton Plane

#### Wireframes

I used [Figma](https://www.figma.com/) to construct the surface plane. After delving into writing the code for the application, some design alterations were made. This included using a separate page for the Log In and Register process rather than using a modal, which may have been obstructive on smaller and/or touchscreen devices.

Each page has a wireframe for both desktop and mobile devices. I did not include a tablet wireframe in the design phase because I wanted the site to look nearly identical on larger tablet and desktop devices. Particularly as many laptops now can also function as a touchscreen tablet, I thought it was important that there were no stark differences between the two as this may have compromised good UX design. Nevertheless, the mobile wireframe can represent tablet devices with smaller screens.

Each wireframe can be viewed via the links below.


##### Basic Wireframes


##### Home page

![Basic wireframe](documentation/media/wireframe-basic-home.png)


##### Games page

![Basic wireframe](documentation/media/wireframe-basic-games.png)


##### Product details page

![Basic wireframe](documentation/media/wireframe-basic-details.png)


##### Shopping cart

![Basic wireframe](documentation/media/wireframe-basic-checkout.png)


##### Checkout page

![Basic wireframe](documentation/media/wireframe-basic-cart.png)



##### Detailed Wireframes


##### Home page

![Detailed wireframe](documentation/media/wireframe-detailed-home.png)


##### Log in and Sign Up page

![Detailed wireframe](documentation/media/wireframe-detailed-account.png)


##### Games page

![Detailed wireframe](documentation/media/wireframe-detailed-games.png)


##### Buy game page

![Detailed wireframe](documentation/media/wireframe-detailed-buygame.png)


##### Adoptions page

![Detailed wireframe](documentation/media/wireframe-detailed-adoptions.png)


##### Product details page

![Detailed wireframe](documentation/media/wireframe-detailed-details.png)


##### Shopping cart

![Detailed wireframe](documentation/media/wireframe-detailed-checkout.png)



##### Checkout page

![Detailed wireframe](documentation/media/wireframe-detailed-cart.png)



-----

### Surface Plane


#### Typography

The two main fonts that were used were **AgencyFB** and **Chinese Rocks**. CHinese rocks is an icon font within [Rockstar Red Dead Redemption Official Site](https://www.rockstargames.com/reddeadredemption2/), and I felt that the Agency had a strong sci-fi aesthetic. This helped incorporate a modern, fresh and clean look to the website's design, while the bold contrast of Chinese Rocks was perfect to make certain text stand out. 

I chose to use Chinese Rocks as the font would be recognisable to many of the target audience, helps the overall theme which resolves a lot around selling games.


#### Colour

The site's colour scheme consisted of red and blues. The blue is reminiscent of the ocean, and provided a soft foreground to alot of the text and images. The red was used to make buttons stand out and provide good colour contrast which improves accessibility. Cyan blues and linear gradient where implemented to help create a glow effect which adde visual variety and improved the overall UI and theme.



-----


## Database Schema


![Database model](documentation/media/data-model.png)


To handle fixtures, dynamic data in the backend, NOSQL and PostGres was used. NOSQl was used in the development and PostGres is used in the deployed version. 

The database model is centered around the `product` class. The product class acts as link between the `order` class and `edition` and `package` class, which is the product that is used for users to make purchases with.

#### Games

Although the `game` class holds key information, it is not what connects the game to the `order`, for that the `edition` class is used. There may be many editions for one game, and each edition may have a different price, which is why the `product` class calls to `edition` to construct the order. The ForeignKey is named `game` to cleary identify what app model it is associated with.


#### Adoptions

Like the edition class, the `adoption` class is **not** used to connect an adoption pack to an order, for that purpose the `package` class is used. This works in a very similar way to the edition class, as each adoption can have many packages, with each one potentially having a different price. This is why the `product` class calls to `package` to construct the order. The ForeignKey is named `adoption` to cleary identify what app model it is associated with.#


#### Order

The order model uses `user_profile` to retrieve contact and shipping/billing information and inject that data into the order object. The order model is linked to an inline `orderlineitem` class which is used to store product information including, the `product` ForeignKey, the quantity, product price and total. 

The `product` class is there to act as a link between the `edition` and `package` class. A user may not purchase from both categories at a time, so a class needed to be constructed to retrieve data from the correct class.


-----


----

## Accessibility 

- All images imported via img tags in the HTML files have been given meaningful, clear and descriptive alt attributes to conform to accessibility guidelines.

- Most of the font size is relatively large in order to cater for audiences who have difficulties with their vision.

- Good colour contrast has been used throughout the project to ensure that all the content is readable.


-----


## Technologies Used

### Languages 

- HTML (5)
- CSS (3)
- Javascript
- Python 3

### Frameworks, Libraries and Programs 

- [Django](https://www.djangoproject.com/)
    - Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It was the used to build the project, implement security features and more.

- [Heroku](https://www.heroku.com/)
    - Heroku is a platform service that enables developers to build, ruin and operate applications within its cloud server. It was used to deploy my web-application.

- [Materialize 1.0.0](https://getbootstrap.com/)
    - Materialize 1.0.0 is a modern responsive CSS framework based on Material Design by Google. It was used to help with the site's responsiveness, implement useful and intuitive features and provide a clean foundation for the website's design.

- [JQuery 3.5.1](https://jquery.com/)
    - JQuery 3.5.1 was used to initialize certian features within the [Materialize 1.0.0](https://getbootstrap.com/) framework. It was also used to write custom JS code.

- [Figma](https://www.figma.com/)
  - Figma is a powerful website design system that can be used to construct prototypes. I used Figma to create my wireframes for this project.

- [Visual Studio Code](https://code.visualstudio.com/)
  - Visual Studio Code was the software used to write the code. 
  
- [Git](https://git-scm.com/)
  - Git was used for version control by utilising the GitBash terminal in Visual Studio Code to commit to Git and push to [GitHub](https://github.com/).
  
- [GitHub](https://github.com/)
  - GitHub is used to store the project's code after being pushed to Git. It acts as a cloud-based service to store the project’s assets and code. My GitHub account was linked to [Heroku](https://www.heroku.com/) to trigger automatic deployment of my web-application.

- [Smartmockups - Free Product Mockup Generator](https://smartmockups.com/)
  - Smartmockups is a web-application that allows you to create free mockup images. I used it in this readme file to present a mockup image of the project.

- [Responsively App](https://responsively.app/)
  - Responsively App is DevTool software that allows you to see an instant preview of all target screens for your website in a single window, side-by-side. It was used to check the responsiveness of my site.

- [Asana](https://app.asana.com/0/home/1192103038725952)
  - Asana is a web and mobile application designed to help you organise, track and manage your projects. It was used to organise my project and schedule each task efficiently.

- [Creatrly](https://creately.com/)
    - Creatrly is an online sketching/whiteboard tool. I used it to visually demonstrate the relationships between each collection in the database.

- [Coolors](https://coolors.co/)
    - Coolors is a visual workspace where you can create diagrams, flowcharts and more. It was used to demonstrate the colours used in on the website.

-----

## Testing

Testing documentation can be found in a separate [TESTING.md](TESTING.md) file


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


-----

## Credits


### Content

- All content was written by the developer.

- Game details were taken from [Rockstar Games](https://www.rockstargames.com/) and [Frontier Games](https://www.frontier.co.uk/our-games/planet-zoo)



### Inspiration

- [Rockstar Red Dead Redemption Official Site](https://www.rockstargames.com/reddeadredemption2/)

- [CD Keys](https://www.cdkeys.com/)


### Acknowledgements


- [CodeInstitute](https://codeinstitute.net/) for the course material, knowledge and inspiration.

- [StackOverflow](https://stackoverflow.com/) for the perpetual source of help and inspiration.

- [Slack Community](https://slack.com/intl/en-gb/) for all the help, advice and inspiration.

- [Rockstar Games](https://www.rockstargames.com/) for the game content and UI inspiration

- [Frontier Games](https://www.frontier.co.uk/our-games/planet-zoo) for the game content

- I also want to thank my mentor, Can Sucullu, for his help and valuable suggestions throughout this project.

- Finally, I want to thank friends and family members for their continual support and feedback. 
