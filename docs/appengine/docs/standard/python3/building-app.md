---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/
title: Build a Python app on App Engine \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:59.462175+00:00
---

# Build a Python app on App Engine  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Build a Python app on App Engine Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** If you are deploying a new Python web service to Google Cloud, we recommend getting started with [Cloud Run](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service).

Use this guide to learn the basics of developing and deploying Python web services to the [App Engine standard environment](https://docs.cloud.google.com/appengine/docs/standard).

In this guide, you iterate through building and deploying versions of a web service, starting from a static page and building up to a personalized web page that shows authenticated users their name, their email, and their recent site request times.

The following tasks demonstrate the basic developer flow for creating that web service using [Firestore in Datastore mode (Datastore)](https://docs.cloud.google.com/datastore/docs/concepts/overview) data storage and [Firebase authentication](https://firebase.google.com/docs/auth/):

  1. **[Create your Google Cloud project](https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/creating-gcp-project)**

Learn how to create a Google Cloud project and then set up the App Engine resources for your web service.

  2. **[Write your web service](https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/writing-web-service)**

Learn how to write and locally test a basic web service, and then define the configuration files that you need for deploying that web service to App Engine.

  3. **[Deploy your web service to App Engine](https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/deploying-web-service)**

Learn how to deploy your Python code and then view your web service running on App Engine.

  4. **[Handle Data](https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/storing-and-retrieving-data)**

Learn how to use Datastore to store and retrieve data about site requests.

  5. **[Add Firebase to your web service](https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/adding-firebase)**

Learn how to add [Firebase](https://support.google.com/firebase/answer/6399760) to your Google Cloud project and web service.

  6. **[Authenticate users with Firebase](https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/authenticating-users)**

Learn how to use Firebase Authentication to verify user credentials, serve user information, and allow data access.

  7. **[Personalize data for authenticated users](https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/personalizing-data-for-authenticated-users)**

Learn how to use authentication to personalize data storage and retrieval for authenticated users.

  8. **[Clean up](https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/cleaning-up)**

Learn how to clean up your project and avoid the possibility of incurring charges for resources you aren't using.




This guide assumes that you are already familiar with [Python](https://docs.cloud.google.com/appengine/docs/standard/python3/runtime), the [Flask framework](http://flask.pocoo.org/), and basic web development.

## Costs

Running this sample app alone does not exceed the [free quotas](https://docs.cloud.google.com/appengine/docs/standard/quotas). You will be charged only if you exceed those quotas, for example, by running other samples and adding other services to the same Google Cloud project.

## Let's get started!

[Create your Google Cloud project and set up the App Engine resources](https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/creating-gcp-project).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
