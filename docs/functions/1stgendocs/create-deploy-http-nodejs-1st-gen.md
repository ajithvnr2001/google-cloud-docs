---
url: https://docs.cloud.google.com/functions/1stgendocs/create-deploy-http-nodejs-1st-gen/
title: Quickstart: Create and deploy a HTTP Cloud Run function by using Node.js (1st gen) \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:27.829067+00:00
---

# Quickstart: Create and deploy a HTTP Cloud Run function by using Node.js (1st gen)  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/create-deploy-http-nodejs-1st-gen/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create and deploy an HTTP Cloud Run function by using Node.js (1st gen)

This guide takes you through the process of writing a Cloud Run function using the Node.js runtime. There are two types of Cloud Run functions:

  * An HTTP function, which you invoke from standard HTTP requests.
  * An event-driven function, which you use to handle events from your Cloud infrastructure, such as messages on a Pub/Sub topic, or changes in a Cloud Storage bucket.



The sample shows how to create a simple HTTP function.

**Learn more** : For more details, read about [HTTP functions](https://docs.cloud.google.com/functions/1stgendocs/writing/write-http-functions) and [event-driven functions](https://docs.cloud.google.com/functions/1stgendocs/writing/write-event-driven-functions). 

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Cloud Functions and Cloud Build APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable cloudfunctions cloudbuild.googleapis.com

  8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  9. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  10. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  11. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  12. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  13. Enable the Cloud Functions and Cloud Build APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable cloudfunctions cloudbuild.googleapis.com

  14. Prepare your development environment. 

[ Go to the Node.js setup guide ](https://docs.cloud.google.com/nodejs/docs/setup)




## Create a function

  1. Create a directory on your local system for the function code:

### Linux or Mac OS X
         
         mkdir ~/helloworld
         cd ~/helloworld
         

### Windows
         
         mkdir %HOMEPATH%\helloworld
         cd %HOMEPATH%\helloworld
         

  2. Create an `index.js` file in the `helloworld` directory with the following contents:
         
         const functions = require('@google-cloud/functions-framework');
         const escapeHtml = require('escape-html');
         
         /**
          * Responds to an HTTP request using data from the request body parsed according
          * to the "content-type" header.
          *
          * @param {Object} req Cloud Function request context.
          * @param {Object} res Cloud Function response context.
          */
         functions.http('helloHttp', (req, res) => {
           const name =
             (req.query && req.query.name) || (req.body && req.body.name) || 'World';
         
           res.send(`Hello ${escapeHtml(name)}!`);
         });

This example function takes a name supplied in the HTTP request and returns a greeting, or "Hello World!" when no name is supplied.

**Note:** Cloud Run functions looks for deployable functions in `index.js` by default. Use the [`--source`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--source) flag when deploying your function via `gcloud` to specify a different directory containing an `index.js` file.



## Specify dependencies

Dependencies in Node.js are stored in a file called [`package.json`](https://docs.npmjs.com/files/package.json). You can create this file manually or with the [npm](https://docs.npmjs.com/) command.

  * To create your `package.json` dependency file by using `npm`, run these commands:
        
        npm init
        npm install c8 gaxios mocha sinon supertest wait-port --save-dev
        npm install @google-cloud/functions-framework escape-html
        

  * If you prefer to build your `package.json`file manually, create a `package.json` file in the `helloworld` directory with the following contents:
        
        {
          "name": "nodejs-docs-samples-functions-hello-world-http",
          "version": "0.0.1",
          "private": true,
          "license": "Apache-2.0",
          "author": "Google Inc.",
          "repository": {
            "type": "git",
            "url": "https://github.com/GoogleCloudPlatform/nodejs-docs-samples.git"
          },
          "engines": {
            "node": ">=20.0.0"
          },
          "scripts": {
            "unit-test": "c8 mocha -p -j 2 test/index.test.js test/*unit*test.js test/*integration*test.js --timeout=6000 --exit",
            "system-test": "c8 mocha -p -j 2 test/*system*test.js --timeout=600000 --exit",
            "all-test": "npm run unit-test && npm run system-test",
            "test": "npm -- run unit-test"
          },
          "dependencies": {
            "@google-cloud/functions-framework": "^5.0.0",
            "escape-html": "^1.0.3"
          },
          "devDependencies": {
            "c8": "^12.0.0",
            "gaxios": "^7.0.0",
            "mocha": "^10.0.0",
            "sinon": "^18.0.0",
            "supertest": "^7.0.0",
            "wait-port": "^1.0.4"
          }
        }
        

**Note:** Node.js client libraries are available for a variety of Google Cloud products, and can be installed as dependencies. See the list [here](https://github.com/googleapis/google-cloud-node#google-cloud-nodejs-client-libraries).

**Learn more** : For more details, read about [specifying dependencies](https://docs.cloud.google.com/functions/1stgendocs/writing/specifying-dependencies-nodejs). 

## Deploy the function

To deploy the function with an HTTP trigger, run the following command in the `helloworld` directory:
    
    
    gcloud functions deploy helloHttp --no-gen2 --runtime nodejs22 --trigger-http --allow-unauthenticated
    

The `--allow-unauthenticated` flag lets you reach the function [without authentication](https://docs.cloud.google.com/functions/1stgendocs/securing/managing-access-iam#allowing_unauthenticated_http_function_invocation). To require [authentication](https://docs.cloud.google.com/functions/1stgendocs/securing/authenticating#developers), omit the flag.

**Learn more** : For more details, read about [deploying Cloud Run functions](https://docs.cloud.google.com/functions/1stgendocs/deploy#basics). 

## Test the function

  1. When the function finishes deploying, take note of the `httpsTrigger.url` property or find it using the following command:
         
         gcloud functions describe helloHttp
         

It should look like this:
         
         https://GCP_REGION-PROJECT_ID.cloudfunctions.net/helloHttp

  2. Visit this URL in your browser. You should see a "Hello World!" message.

Try passing a name in the HTTP request, for example by using the following URL:
         
         https://GCP_REGION-PROJECT_ID.cloudfunctions.net/helloHttp?name=NAME

You should see the message "Hello `NAME`!"




## View logs

Logs for Cloud Run functions are viewable using the Google Cloud CLI, and in the Cloud Logging UI.

### Use the command-line tool

To view logs for your function with the gcloud CLI, use the [`logs read`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/logs/read) command, followed by the name of the function:
    
    
    gcloud functions logs read helloHttp

The output should resemble the following:
    
    
    LEVEL  NAME       EXECUTION_ID  TIME_UTC                 LOG
    D      helloHttp  rvb9j0axfclb  2019-09-18 22:06:25.983  Function execution started
    D      helloHttp  rvb9j0axfclb  2019-09-18 22:06:26.001  Function execution took 19 ms, finished with status code: 200

**Note:** There is typically a slight delay between when log entries are created and when they show up in Cloud Logging.

### Use the Logging dashboard

You can also view logs for Cloud Run functions from the [Google Cloud console](https://console.cloud.google.com/project/_/logs?service=cloudfunctions.googleapis.com).

**Learn more** : For more details, read about [writing, viewing, and responding to logs](https://docs.cloud.google.com/functions/1stgendocs/monitoring/logging). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
