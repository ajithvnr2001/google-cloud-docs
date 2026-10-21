---
url: https://docs.cloud.google.com/appengine/docs/flexible/ruby/configuring-your-app-with-app-yaml/
title: Configuring your app with app.yaml \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:40:10.435238+00:00
---

# Configuring your app with app.yaml  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/ruby/configuring-your-app-with-app-yaml/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Configuring your app with app.yaml Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Some [Ruby runtimes](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#ruby) have reached [end of support](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/runtime-lifecycle#end_of_support). You cannot re-deploy versions that use runtimes after their end of support date. We recommend that you [upgrade your app](https://docs.cloud.google.com/appengine/docs/flexible/ruby/runtime#newversions) to use the latest version of Ruby. 

An App Engine app is configured using an `app.yaml` file, that contains CPU, memory, network and disk resources, scaling, and other general settings including environment variables. 

## About `app.yaml` files

You can specify the runtime configuration for your Ruby app, including versions and URLs, in the `app.yaml` file. This file acts as a deployment descriptor of a specific [service](https://docs.cloud.google.com/appengine/docs/flexible/an-overview-of-app-engine) version. 

You must first create the `app.yaml` file for the `default` service of your app before you can create and deploy `app.yaml` files for additional services. 

The following `app.yaml` demonstrates how to configure your app to use the latest Ruby version. To use any other [supported version](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#ruby) of Ruby, you must update your `app.yaml` file. For more information, see [Ruby runtime](https://docs.cloud.google.com/appengine/docs/flexible/ruby/runtime).
    
    
    runtime: ruby
    env: flex
    entrypoint: bundle exec ruby app.rb
    
    runtime_config:
      operating_system: ubuntu22
    
    # This sample incurs costs to run on the App Engine flexible environment.
    # The settings below are to reduce costs during testing and are not appropriate
    # for production use. For more information, see:
    # https://cloud.google.com/appengine/docs/flexible/ruby/configuring-your-app-with-app-yaml
    manual_scaling:
      instances: 1
    resources:
      cpu: 1
      memory_gb: 0.5
      disk_size_gb: 10
    

Depending on the complexity of your app's service, you might only need to define a few elements in the corresponding `app.yaml` file. The following example demonstrates what a simple Ruby app might require in the flexible environment: 

You can specify a unique name for your `app.yaml` files, but then you must specify the file name with the [deployment command](https://docs.cloud.google.com/appengine/docs/flexible/testing-and-deploying-your-app) as well. For example, if you name your `app.yaml` file `service-name-app.yaml` or `app.flexible.yaml`, then you must deploy your app using either:
    
    
    gcloud app deploy service-name-app.yaml
    gcloud app deploy app.flexible.yaml
    

To learn more about structuring multiple services and `app.yaml` files in your app, see [Structuring web services](https://docs.cloud.google.com/appengine/docs/flexible/configuration-files). 

## All configuration elements

For a complete list of all the supported elements in this configuration file, see the [`app.yaml` reference](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
