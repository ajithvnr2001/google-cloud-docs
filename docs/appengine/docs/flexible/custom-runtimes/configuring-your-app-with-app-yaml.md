---
url: https://docs.cloud.google.com/appengine/docs/flexible/custom-runtimes/configuring-your-app-with-app-yaml/
title: Configuring your app with app.yaml \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:44:36.839775+00:00
---

# Configuring your app with app.yaml  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/custom-runtimes/configuring-your-app-with-app-yaml/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Configuring your app with app.yaml Stay organized with collections  Save and categorize content based on your preferences. 

An App Engine app is configured using an `app.yaml` file, that contains CPU, memory, network and disk resources, scaling, and other general settings including environment variables. 

## About `app.yaml` files

You can specify the runtime configuration for your Custom Runtime app, including versions and URLs, in the `app.yaml` file. This file acts as a deployment descriptor of a specific service version. You must first create the `app.yaml` file for the `default` service of your app before you can create and deploy `app.yaml` files for additional services. 
    
    
    runtime: custom
    env: flex
    

Depending on the complexity of your app's service, you might only need to define a few elements in the corresponding `app.yaml` file. The following example demonstrates what a simple Custom Runtime app might require in the flexible environment: 

You can specify a unique name for your `app.yaml` files, but then you must specify the file name with the [deployment command](https://docs.cloud.google.com/appengine/docs/flexible/testing-and-deploying-your-app) as well. For example, if you name your `app.yaml` file `service-name-app.yaml` or `app.flexible.yaml`, then you must deploy your app using either:
    
    
    gcloud app deploy service-name-app.yaml
    gcloud app deploy app.flexible.yaml
    

## All configuration elements

For a complete list of all the supported elements in this configuration file, see the [`app.yaml` reference](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
