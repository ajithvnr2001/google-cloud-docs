---
url: https://docs.cloud.google.com/appengine/docs/admin-api/deploying-overview/
title: Deploy your apps with the Admin API \u00a0|\u00a0 App Engine Admin API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:03:53.136263+00:00
---

# Deploy your apps with the Admin API  |  App Engine Admin API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/admin-api/deploying-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ App Engine ](https://docs.cloud.google.com/appengine)
  * [ Admin API ](https://docs.cloud.google.com/appengine/docs/admin-api)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/admin-api/apis)



Send feedback 

#  Deploy your apps with the Admin API Stay organized with collections  Save and categorize content based on your preferences. 

To deploy a _version_ of the source code and configuration files that make up a _service_ in your application, you must first stage your files, create a configuration file, and authenticate before you can send the HTTP `POST` request.

The App Engine Admin API requires that you upload and stage all of your version's resources in a [Cloud Storage](https://docs.cloud.google.com/storage) bucket, including the relevant code files, static files, and any Dockerfiles that are used. You must also create a JSON formatted configuration file that contains the definition of your version and a manifest of all your resources in Cloud Storage. The last step before you can deploy your version to your App Engine application is to authenticate with your Google Cloud Platform project.

For more information about versions and how they make up the services in your application, see the [Overview of App Engine](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine).

To manually deploy your app, see [Deploying Your App](https://docs.cloud.google.com/appengine/docs/standard/testing-and-deploying-your-app).

## Before you begin

Before you can deploy your apps, you must be able to authorize your HTTP requests. For more information about configuring your Google Cloud project, creating credentials, and obtaining access tokens, see [Accessing the API](https://docs.cloud.google.com/appengine/docs/admin-api/accessing-the-api).

## Deploying versions to your App Engine application

To deploy a version of your app with the Admin API:

  1. [Upload your app's resources to Cloud Storage.](https://docs.cloud.google.com/storage/docs/uploading-objects#rest-upload-objects)
  2. [Create a configuration file that defines your deployment.](https://docs.cloud.google.com/appengine/docs/admin-api/creating-config-files)
  3. [Create and send the HTTP request for deploying your app.](https://docs.cloud.google.com/appengine/docs/admin-api/apis)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
