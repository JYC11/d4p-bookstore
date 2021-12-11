# Django For Professionals: Big Project(Ch3 onwards)

The book now goes into the main meatiest project: A bookstore website.

We set up django and docker and postgres as we covered in chapter 1 and 2.

## Chapter 3

Instead of using the default user model, we are going to use a custom user model.

How to add a custom user model:
1. Create a CustomUser model
2. Update settings.py
3. Customize UserCreationForm and UserChangeForm
4. Add the custom user model to admin.py

As usual, we wrote tests by creating a normal user and superuser.

## Chapter 4 & 5 - HTML stuff and built in auth
Html stuff

As usual we add the html stuff and then we add tests to check if the html used is what we expect.

Chapter 5 we dived a bit more deep into the built in auth package and added more html/tests.

The built in auth package is loaded in when we first create the project and is added to the settings.py file.

It provides login, logout, password change, password reset, password reset confirm routes out of the box for when we do SSR. It is basically an app that we can create using django except that it's already there when we make a django project.

To make the auth app function properly we do need to add some templates that the the auth app expects there to be like registration/signup.html.

## Chapter 6 - Crispy forms and static files
Added crispy forms and even more static files. Not much to say. Bootstrap, forms, html and css.
As usual added more tests.

A note about static files:
set where the static files are located in and where there will be the static root files properly so you don't mess up when you deploy the django project.

## Chapter 7 - Using django allauth
This chapter I learned how to use the django allauth package instead of the built in django auth app.

It is mostly more already-there django magic that involves installing a package and setting variation configurations in the settings.py file(+ changing around a few html files).

## Chapter 8 - Environment variables
Environment variables are a handy way to use secrets keys and other sensitive information without directly hardcoding them into the project.

It is as simple as adding the variables to the docker compose file then calling them with the os package where it is needed.

## Chapter 9 - Sending emails
Setting up email sending with mailgun. Making sure to put secret keys in the docker file so that it is not exposed in the code directly.

## Chapter 10 - Books app
Pretty standard app creation with corresponding view,templates and templates.

Some nuance:
* id vs pk
id is a number that is auto-incremented and auto set for a model. The id is treated as the pk for the model but the pk CAN be changed. When in doubt it is usually safer to use the pk.

A uuid may be safer to use than an auto incrementing pk because it could be really easy to access pages to scrape by just auto incrementing the pk in the url(Also easier to figure out how many records there may be).

A uuid is a universally unique identifier which is (what I understand) is a completely randomly generated string of letters and numbers. Because it is generated randomly, it would prevent the downsides of above.

## Chapter 11 - Adding reviews to books
In this chapter I added reviews to books. It was pretty simple because I just needed to add a model to the books app and establish a many-to-many relationship with django's built in models by inserting foreign keys in the Review model.

## Chapter 12 - Adding media uploads
Media(uploaded by users) cannot be trusted. So they must be dealt with differently and is kinda out of scope at the moment. I could add more by creating a proper CRUD to this bookstore thing but I want to learn how django works with docker and postgres + couple of other things like security in this book so I'll touch upon a more polished project later. Besides, most people create web apps with APIs so will need to focus on that.

## Chapter 13 - Permissions
Like restricting what users can see by gating them with login, permissions can be used to further restrict what things user can see things. 

Like how authorization was implemented with logins mixins, permissions can also be implemented with permission mixins.

Mixins are a way to allow multiple inheritance when making classes. It is used when you want to provde multiple features to a class or use one feature in a lot of classes.

It sorta seems like interfaces in Java because you can inherit multiple interfaces in Java to enforce a certain design of a class.

## Chapter 14 - Payment
In this chapter we deal with payments with Stripe. Unfortunately, Stripe isn't available in S.Korea so I had to pick Japan as the country. That means I can't actually implement Stripe properly because I can't register S.Korean addresses to a Japanese business. I could fake the address but it seems like too much of a hassle. So I may need to look for S.Korean alternatives.

I learned about get_context_data() in this chapter as a way to access the stripe publishable key from the html template. So what is a context? A context is a dictionary(key value) that a template uses to access well um data? is how I understand. By default it seems to have what is in the corresponding view (which is based on the model) but it can be overridden to include other key-value pairs. So we overrode this method to have it include the stripe publishable key so that the template can acccess this key in order to allow payments.

To test third party services, we can use a service like Cypress. Currently out of scope of the book but can be looked into later.

## Chapter 15 - Searching for books
Searching is a key part of any web application and I learn how to implement it in this chapter. 

For the MTV (model template view) project like this, I implement a search function in the View section of the MTV. We use the query method provided by django models and access the search parameter by accessing the query param that is sent by the search bar. Surprisingly simple to implement but can be probably more advanced based on more complicated search and filtering conditions.

## Chapter 16 - Tracking app performance
You can write a web app but it is no guarantee that it will be efficient. Efficient meaning that the web app does just the right number/amount of things to get the web app running(vague I know but I wanted to put it in simpler terms). 

So for example these things can mess with efficiency: way too many SQL queries, way too many calculations, no indexing in databases, too large static assets.

To find out how well the app is performing, we can use the django debug toolbar. Django really does seem to have everything.
### SQL
Making queries more efficient can be done in two possible ways:
* select_related -> Using a join to select one-to-many or one-to-one relationship data. Get a large amount of data then do the stuff instead of multiple queries.
* prefetch_related -> Used for many-to-many or many-to-one relationship. A look up is done for each relationship and the "join" occurs in Python instead of SQL. May need to look further into how this is done since I don't really get why it's done in Python not SQL.
### Caching
Storing expensive calculations in memory for quick retrieval is a way to make the web app run faster. Once the calculation is done, it doesn't need to be run again and can be just read from the in-memory db.

Django has it's own cache framework but there are other options like Memchached, Redis, etc. The developer should think about what things to cache and for how long to cache them for as the RAM isn't very large compared to the hard disk. They should also consider if caching is necessary(tbh they should consider it for all optimizations) because it may be overkill.
### Indexing
Indexing is a way to speed up database performance. From what I know, data is stored in a list/array? like data structure in a database and when a SELECT is performed, the data is searched one by one until the relevant data is found. But when the data is indexed, the database searches through the indexes only and finds the relevant data more quickly.

It may be tempting to add indexes to all database tables but indexes also take up extra disk space so it should be added when it is really necessary. The book says the general rule of thumb is that if a given field is being used frequently(such as 10~25% of all queries), it should be considered strongly to be indexed.

### Compressing static assets
Large static assets can make site loading slow so compressing them can be a way to make the site load faster.

Sometimes it may be appropriate to use a Content Delivery Network to store media when sites get extremely large.

## Chapter 17 - Security
Keep your web app safe.
* Don't give everyone full access to everything
* Keep Django updated and maintain things when features get deprecated
* Have a deployment checklist ('python manage.py check --deploy'=>use this to check)
* Make a separate docker file for deployment with different settings(Set debug to true, set allowed hosts before deployment, etc)

Common security problems:
* SQL injection -> injecting small pieces of SQL to be run on the database(like dropping an entire table)
* Cross Site Scripting(XSS) -> injecting small pieces of code into webpages(usually javascript)
* Cross Site Request Forgery(CSRF) -> a malicious actor intercepts a user's session/cookie to make your web app think that the user is sending a legitimate request
* Clickjacking -> tricking a user to click a hidden iframe(a way to embed one website into another) to get them to do things they didn't mean to do
* Insecure HTTP -> HTTP by default is not secure so malicious actors can intercept the transfer protocols.
* Admin -> accessing admin through website.com/admin

How Django deals with them:
* SQL injection -> django by default sanitizes user input
* XSS -> SECURE_BROWSER_XSS_FILTER = True setting
* CSRF -> csrf token in templates
* Clickjacking -> X_FRAME_OPTIONS = 'DENY'
* Insecure HTTP -> SECURE_SSL_REDIRECT = True(How is HTTP made secure though? Should google some more), enforcing HTTPS by adding a Strict Transport Security Header, enforcing secure Cookies
* Admin -> change the /admin to something else, enforce 2fa for admin, use django-admin-honeypot

## Chapter 18 - Deployment
Like the previous books, we deploy the web app with heroku.
These are the steps I followed:
1. Install WhiteNoise > a library used to serve static files, supposedly it is much better to use than the default one provided by django
2. Install Gunicorn > apparently better than the default Web Server Gateway Interface(WSGI)
3. Install dj-database-url > a way to parse database url env variables and automatically convert to proper configuration format
4. Install heroku CLI and sign up to heroku

