---
url: https://docs.cloud.google.com/deployment-manager/runtime-configurator/watching-a-variable/
title: Watching a Variable for Changes \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:56.294164+00:00
---

# Watching a Variable for Changes  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/runtime-configurator/watching-a-variable/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment)



Send feedback 

#  Watching a Variable for Changes Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page explains how to create a watcher for a variable. To learn more about watchers, see [Runtime Configurator Fundamentals](https://docs.cloud.google.com/deployment-manager/runtime-configurator).

## Before you begin

  * If you want to use the command-line examples in this guide, install the [`gcloud` command-line tool](https://docs.cloud.google.com/sdk).
  * If you want to use the API examples in this guide, set up [API access](https://docs.cloud.google.com/deployment-manager/docs/reference/latest).
  * Read [Runtime Configurator Fundamentals](https://docs.cloud.google.com/deployment-manager/runtime-configurator). 
  * Read [Creating and Deleting RuntimeConfig Resources](https://docs.cloud.google.com/deployment-manager/runtime-configurator/create-and-delete-runtimeconfig-resources).
  * Read [Setting and Getting Data](https://docs.cloud.google.com/deployment-manager/runtime-configurator/set-and-get-variables).



## Watching a variable for change

You can watch a variable for changes by calling the [`variables().watch`](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables/watch) method. The method watches the variable for 60 seconds and returns if the variable value changes. If the value doesn't change within 60 seconds, the method terminates and returns with variable `state=VARIABLE_STATE_UNSPECIFIED`. If the variable is deleted, the method returns with a variable `state=DELETED` and the last known variable value.

To set a watcher, use Deployment Manager, the Google Cloud CLI, or the API.

###  Deployment Manager 

This is not supported in Deployment Manager. Create a [waiter](https://docs.cloud.google.com/deployment-manager/runtime-configurator/creating-a-waiter) instead.

###  gcloud 

With the Google Cloud CLI:
    
    
    gcloud beta runtime-config configs variables watch [VARIABLE_KEY] --max-wait [TIMEOUT_SEC] --config-name [CONFIG_NAME]
    

where:

  * `[VARIABLE_KEY]` is the key to watch.
  * `[TIMEOUT_SEC]` is the time in seconds to wait. The default and maximum amount is 60 seconds.



The gcloud CLI watches the variable and returns after it reaches the specified timeout period or the variable changes. If the variable changed, the response contains one of the applicable [variable states](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables#VariableState).

###  API 

In the API, make a `POST` request to the following URI:
    
    
    https://runtimeconfig.googleapis.com/v1beta1/projects/[PROJECT_ID]/configs/[CONFIG_NAME]/variables/[VARIABLE_KEY]:watch
    

where:

  * `[PROJECT_ID]` is the project ID for this request.
  * `[CONFIG_NAME]` is the name of the RuntimeConfig resource for this request.
  * `[VARIABLE_KEY]` is the key to watch.

Optionally, you can provide a request payload with the `newerThan` property:

{ "newerThan": "[TIMESTAMP]" }

where `[TIMESTAMP]` is a timestamp in RFC 3339 since the epoch in UTC "Zulu" format. For example:

2014-10-02T15:01:23.045123456Z

If you provide the `newerThan` property, the method returns immediately if the current timestamp for the variable is newer than the specified timestamp. Use the `newerThan` property to make sure you didn't miss any changes between `watch()` calls.

The method returns with one of applicable [variable states](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables#VariableState).

To learn more about the method, read the [`variables().watch`](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables/watch) documentation.




## What's next

  * Learn about [Runtime Configurator](https://docs.cloud.google.com/deployment-manager/runtime-configurator).
  * [Setting and Getting Data](https://docs.cloud.google.com/deployment-manager/runtime-configurator/set-and-get-variables).
  * [Creating a Waiter](https://docs.cloud.google.com/deployment-manager/runtime-configurator/creating-a-waiter).
  * [Creating and Deleting RuntimeConfig Resources](https://docs.cloud.google.com/deployment-manager/runtime-configurator/create-and-delete-runtimeconfig-resources).
  * Refer to the [v1beta1 reference](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest).
  * Refer to the [Quotas for Runtime Configurator](https://cloud.google.com/deployment-manager/pricing-and-quotas#runtime_configurator).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
