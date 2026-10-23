---
url: https://docs.cloud.google.com/appengine/docs/standard/nodejs/configuring-your-app-with-app-yaml/
title: Defining runtime settings \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:21.424797+00:00
---

# Defining runtime settings  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/nodejs/configuring-your-app-with-app-yaml/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Defining runtime settings Stay organized with collections  Save and categorize content based on your preferences. 

An App Engine app is configured using an `app.yaml` file, that contains the runtime, handlers, scaling, and other general settings including environment variables. 

## About `app.yaml` files

You can specify the runtime configuration for your Node.js app, including versions and URLs, in the `app.yaml` file. This file acts as a deployment descriptor of a specific [service](https://docs.cloud.google.com/appengine/docs/standard/an-overview-of-app-engine) version. 

You must first create the `app.yaml` file for the `default` service of your app before you can create and deploy `app.yaml` files for additional services. 

Generally, your `app.yaml` file requires only the `runtime` element for a simple Node.js app in the standard environment, for example: 
    
    
    runtime: nodejs26
    

App Engine provides default values for all other settings, including the [F1 instance class](https://docs.cloud.google.com/appengine/docs/standard#instance_classes), which determines the memory and CPU resources that are available to your app, and [automatic scaling](https://docs.cloud.google.com/appengine/docs/standard/how-instances-are-managed#scaling_types), which controls how and when new instances of your app are created.

If you need to override the default settings, create an `app.yaml` file and specify the settings you need. For more information, see [`app.yaml` file reference](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml). 

You can specify a unique name for your `app.yaml` files, but then you must specify the file name with the [deployment command](https://docs.cloud.google.com/appengine/docs/standard/testing-and-deploying-your-app) as well. For example, if you name your `app.yaml` file `service-name-app.yaml` or `app.standard.yaml`, then you must deploy your app using either:
    
    
    gcloud app deploy service-name-app.yaml
    gcloud app deploy app.standard.yaml
    

To learn more about structuring multiple services and `app.yaml` files in your app, see [Structuring web services](https://docs.cloud.google.com/appengine/docs/standard/configuration-files). 

## All configuration elements

For a complete list of all the supported elements in this configuration file, see the [`app.yaml` reference](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
