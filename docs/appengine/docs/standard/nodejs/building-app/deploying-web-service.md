---
url: https://docs.cloud.google.com/appengine/docs/standard/nodejs/building-app/deploying-web-service/
title: Deploy Your Web Service \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:47:33.595983+00:00
---

# Deploy Your Web Service  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/nodejs/building-app/deploying-web-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Deploy Your Web Service Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** If you are deploying a new Node.js web service to Google Cloud, we recommend getting started with [Cloud Run](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-nodejs-service).

### Region ID

The `REGION_ID` is an abbreviated code that Google assigns based on the region you select when you create your app. The code does not correspond to a country or province, even though some region IDs may appear similar to commonly used country and province codes. For apps created after February 2020, `REGION_ID.r` is included in App Engine URLs. For existing apps created before this date, the region ID is optional in the URL.

Learn more [about region IDs](https://docs.cloud.google.com/appengine/docs/standard/nodejs/how-requests-are-routed#region-id). 

OK

This section of the guide shows how to use the gcloud CLI to deploy your Node.js web service on App Engine. To learn more about the Node.js runtime environment, see [Node.js Runtime Environment](https://docs.cloud.google.com/appengine/docs/standard/nodejs/runtime).

## Before you begin

  1. [Create a Google Cloud project with an App Engine app](https://docs.cloud.google.com/appengine/docs/standard/nodejs/building-app/creating-project).
  2. [Write a Node.js web server ready to deploy on App Engine](https://docs.cloud.google.com/appengine/docs/standard/nodejs/building-app/writing-web-service).
  3. [Install Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install), which provides the `gcloud` command-line tool. Ensure `gcloud` is configured to use the Google Cloud project you want to deploy to.



## Key points

Use `gcloud app deploy` and `gcloud app browse` to deploy and view your service.

## Deploy your service

In your `my-nodejs-service` folder, where the `app.yaml` file is located, run the following command in your terminal:
    
    
    gcloud app deploy
    

Your source files are then uploaded to Google Cloud Storage. Cloud Build builds your app and deploys it to App Engine.

For information about other ways to build and deploy your app, see [Testing and deploying your app](https://docs.cloud.google.com/appengine/docs/standard/testing-and-deploying-your-app).

**Note:** Files listed in your [`.gcloudignore`](https://docs.cloud.google.com/sdk/gcloud/reference/topic/gcloudignore) file will not be uploaded.

If you don't have one, a `.gcloudignore` file is created to ensure that your `node_modules` folder is not uploaded.

Node.js modules are installed in the cloud as listed in your `package.json` and `package-lock.json` files and your service is started by using `npm start`.

**Important:** For the best performance, your `start` script should be lightweight, because it runs whenever a new instance of your application is created.

### Deploy multiple services

You can add [multiple services](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine#services) in your project by creating an `app.yaml` file for each service. Include the `service` attribute in each `app.yaml` file to specify the name of the service. To learn more about structuring your app using multiple services, see [Structuring Web Services in App Engine](https://docs.cloud.google.com/appengine/docs/standard/configuration-files#directory_structure).

To deploy multiple services, follow [these instructions](https://docs.cloud.google.com/appengine/docs/standard/testing-and-deploying-your-app#deploying_multiple_services). Each deployed service will have its own assigned URL.

## View your service

To quickly launch your browser and access your web service at `https://PROJECT_ID.REGION_ID.r.appspot.com`, use the following command:
    
    
    gcloud app browse
    

## Services and versions

You've just created and deployed a service on App Engine. You can specify the name of your service in the `app.yaml` file. If the name is omitted, it is treated as `default`. The first service you deploy must be the default service.

You can update your service at any time by running the `gcloud app deploy` command again. Each time you deploy, a new version is created and traffic is automatically routed to the latest version.

To confirm that your service has been created and a version has been deployed:

  1. View your App Engine services in the Google Cloud console:

[View services](https://console.cloud.google.com/appengine/services)

You should see one service listed, named `default`. The default service is publicly accessible at the following URL:

`https://PROJECT_ID.REGION_ID.r.appspot.com`

  2. View your versions:

[View versions](https://console.cloud.google.com/appengine/versions)

You should see one timestamped version listed, corresponding to your deployment.




To learn how to send requests to specific services and versions, see [How Requests are Routed](https://docs.cloud.google.com/appengine/docs/standard/how-requests-are-routed).

## Next steps

Now that you have a Node.js server running on App Engine, [learn how to make updates to your web service](https://docs.cloud.google.com/appengine/docs/standard/nodejs/building-app/updating-web-service).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
