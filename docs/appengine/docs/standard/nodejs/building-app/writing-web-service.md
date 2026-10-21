---
url: https://docs.cloud.google.com/appengine/docs/standard/nodejs/building-app/writing-web-service/
title: Write your web service with Node.js \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:47:33.370465+00:00
---

# Write your web service with Node.js  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/nodejs/building-app/writing-web-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Write your web service with Node.js Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** If you are deploying a new Node.js web service to Google Cloud, we recommend getting started with [Cloud Run](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-nodejs-service).

This guide shows how to write a Node.js web service to run in the App Engine standard environment. To learn more about the Node.js runtime and how it works, see [Node.js Runtime Environment](https://docs.cloud.google.com/appengine/docs/standard/nodejs/runtime).

## Before you begin

  * [Install Node.js LTS](https://nodejs.org/en/download/).



## Key points

  * You can use dependencies by listing them in your [`package.json`](https://docs.npmjs.com/files/package.json) file. See [Specifying Dependencies](https://docs.cloud.google.com/appengine/docs/standard/nodejs/specifying-dependencies) for more information.
  * App Engine starts your application by running `npm start`.
  * Your server must listen to the port specified by the `process.env.PORT`, an [environment variable](https://docs.cloud.google.com/appengine/docs/standard/nodejs/runtime#environment_variables) set by the App Engine runtime.
  * You need an [`app.yaml`](https://docs.cloud.google.com/appengine/docs/standard/nodejs/configuring-your-app-with-app-yaml) file to deploy your service to App Engine.



## Create a server to listen for HTTP requests

The core of your web service is the HTTP server. The sample code in this guide uses the [Express.js](https://expressjs.com/) framework to handle HTTP requests, but you are free to use a web framework of your choice.

  1. Create a new folder called `my-nodejs-service` for your Node.js service.

  2. Navigate to the folder in your terminal, and create a `package.json` file by running `npm init`.

  3. Add Express as a dependency by running:
         
         npm install express
         

Confirm that Express appears in your `package.json` file's `dependencies` field. Here's an example:
         
         {
           ...
           "dependencies": {
             "express": "^4.16.3"
           }
           ...
         }
         

  4. Add a `start` script to your `package.json` file:
         
         "scripts": {
           "start": "node server.js"
         }
         

  5. Create a file called `server.js` in the same folder and add the following code:
         
         const express = require('express');
         const app = express();
         
         app.get('/', (req, res) => {
           res.send('Hello from App Engine!');
         });
         
         // Listen to the App Engine-specified port, or 8080 otherwise
         const PORT = process.env.PORT || 8080;
         app.listen(PORT, () => {
           console.log(`Server listening on port ${PORT}...`);
         });




This is a very basic web server - it responds to all `GET` requests to the root path (`'/'`) with the text "Hello from App Engine!" Note the last four lines, where the server is set to listen to the port specified by `process.env.PORT`, an [environment variable](https://docs.cloud.google.com/appengine/docs/standard/nodejs/runtime#environment_variables) set by the App Engine runtime. If your server isn't set to listen to this port, it will not receive requests.

Notice that if `process.env.PORT` is not set, port `8080` is used as a default. This is necessary for testing your app locally, because `process.env.PORT` doesn't get set during local runs - it is only set when your app is running on App Engine. You can use whichever port you prefer for testing, but this guide uses `8080`.

## Run the server locally

To run the server locally:

  1. Run `npm start` in your terminal. This will run your `server.js` file.

  2. Point your web browser to `<http://localhost:8080>`.




You should see a page with the text "Hello from App Engine!"

## Create the `app.yaml` file

An `app.yaml` file specifies settings for your App Engine service's runtime environment. Your service will not deploy without this file.

  1. In your `my-nodejs-service` folder, create a file called `app.yaml`.

  2. Add the following contents:
         
         runtime: nodejs24

This is a minimal configuration file, indicating to App Engine the version of the Node.js runtime. The `app.yaml` file can also specify network settings, scaling settings, and more. For more information, see the [`app.yaml` reference](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml).




At this point, you should have a file structure like the following:
    
    
      my-nodejs-service/
      app.yaml
      package.json
      server.js
    

## Next steps

Now that you've created a simple Node.js web server that listens to the correct port and you've specified the runtime in an `app.yaml` file, you're ready to [deploy your service on App Engine](https://docs.cloud.google.com/appengine/docs/standard/nodejs/building-app/deploying-web-service).

##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how App Engine performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try App Engine free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
