---
url: https://docs.cloud.google.com/appengine/docs/standard/nodejs/building-app/updating-web-service/
title: Update your web service \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:19.964043+00:00
---

# Update your web service  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/nodejs/building-app/updating-web-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Update your web service Stay organized with collections  Save and categorize content based on your preferences. 

### Region ID

The `REGION_ID` is an abbreviated code that Google assigns based on the region you select when you create your app. The code does not correspond to a country or province, even though some region IDs may appear similar to commonly used country and province codes. For apps created after February 2020, `REGION_ID.r` is included in App Engine URLs. For existing apps created before this date, the region ID is optional in the URL.

Learn more [about region IDs](https://docs.cloud.google.com/appengine/docs/standard/nodejs/how-requests-are-routed#region-id). 

OK

**Note:** If you are deploying a new Node.js web service to Google Cloud, we recommend getting started with [Cloud Run](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-nodejs-service).

This section of the guide shows how to write, test, and deploy updates to the example web service you deployed in the previous section, [Deploying Your Web Service](https://docs.cloud.google.com/appengine/docs/standard/nodejs/building-app/deploying-web-service).

## Before you begin

If you haven't already completed the previous sections in this "Building an App" guide, do the following:

  1. [Create a Google Cloud project with an App Engine app](https://docs.cloud.google.com/appengine/docs/standard/nodejs/building-app/creating-project).
  2. [Write a simple Node.js web service](https://docs.cloud.google.com/appengine/docs/standard/nodejs/building-app/writing-web-service).
  3. [Deploy the web service on App Engine](https://docs.cloud.google.com/appengine/docs/standard/nodejs/building-app/deploying-web-service).



## Update the example web service

The following sections update the example web service with a form and a handler that responds when a user submits the form.

### Create a form for user input

To let a user submit data to your server, use an HTML form.

  1. In your `my-nodejs-service` folder, create a folder named `views` to store your HTML files.

  2. In the `views` folder, create a file named `form.html` and add the following code:
         
         <!DOCTYPE html>
         <html>
           <head>
             <title>My App Engine App</title>
           </head>
           <body>
             <h2>Create a new post</h2>
             <form method="POST" action="/submit">
               <div>
                 <input type="text" name="name" placeholder="Name">
               </div>
               <div>
                 <textarea name="message" placeholder="Message"></textarea>
               </div>
               <div>
                 <button type="submit">Submit</button>
               </div>
             </form>
           </body>
         </html>




This simple form allows a user to enter a name and message to send to the server. It sends the data via an HTTP `POST` request to `/submit`, as specified by the `method` and `action` attributes on the `<form>` element.

At this point, you should have a file structure like the following:
    
    
    my-nodejs-service/
      views/
        form.html
      app.yaml
      package.json
      server.js
    

### Display the form

  1. Add the following line to the top of your `server.js` file to import the `path` module:
         
         const path = require(`path`);
         

  2. Add the following Express handler to show the form when a user browses to `/submit`:
         
         app.get('/submit', (req, res) => {
           res.sendFile(path.join(__dirname, '/views/form.html'));
         });




### Create a handler for submitted data

When a user submits a message to the server, a `POST` request with the data is sent to `/submit`. To read the data from the body of the request, use Express `urlencoded` middleware and create a new request handler.

  1. Set your app to use Express `urlencoded` middleware:
         
         // This middleware is available in Express v4.16.0 onwards
         app.use(express.urlencoded({extended: true}));

  2. Add a `POST` handler to your `server.js` file to read the data:
         
         app.post('/submit', (req, res) => {
           console.log({
             name: req.body.name,
             message: req.body.message,
           });
           res.send('Thanks for your message!');
         });




This sample handler logs the user's name and message to the console, but you could also perform operations on the data or store it in a database.

## Test the form locally

Test your new form locally before deploying your changes.

  1. Start your Node.js server:
         
         npm start
         

  2. View your form at `<http://localhost:8080/submit>`.

Submit a message with the form. You should see your name and message appear in your terminal.




## Deploy your changes

When you deploy an update, a new version of your default service is created and traffic is automatically routed to the latest version. To deploy:

  1. From your `my-nodejs-service` folder, run the following command:
         
         gcloud app deploy
         

This is the same command you learned in [Deploy Your Web Service](https://docs.cloud.google.com/appengine/docs/standard/nodejs/building-app/deploying-web-service).

  2. Confirm that a new version is listed in the Google Cloud console:

[View versions](https://console.cloud.google.com/appengine/versions)

You should see two versions corresponding to the previous and current deployment.




After deploying, your new form is accessible at `https://PROJECT_ID.REGION_ID.r.appspot.com``/submit`. Use it to submit a message or two!

If you do not need the previous version anymore, you can delete it from the versions page in the Google Cloud console.

## Next steps

Now that your app has a form for users to submit data, learn how to [view your application’s logs in the Google Cloud console](https://docs.cloud.google.com/appengine/docs/standard/nodejs/building-app/viewing-service-logs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
