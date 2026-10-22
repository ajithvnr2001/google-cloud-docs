---
url: https://docs.cloud.google.com/deployment-manager/runtime-configurator/
title: Runtime Configurator Fundamentals \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:43:08.083580+00:00
---

# Runtime Configurator Fundamentals  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/runtime-configurator/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment)



Send feedback 

#  Runtime Configurator Fundamentals Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document provides an overview of the Runtime Configurator feature and describes the key concepts related to Runtime Configurator. To learn how to create a RuntimeConfig resource, read [Creating and Deleting RuntimeConfig Resources](https://docs.cloud.google.com/deployment-manager/runtime-configurator/create-and-delete-runtimeconfig-resources).

## What is Runtime Configurator?

The Runtime Configurator feature lets you define and store data as a hierarchy of key value pairs in Google Cloud Platform. You can use these key value pairs as a way to:

  * Dynamically configure services
  * Communicate service states
  * Send notification of changes to data
  * Share information between multiple tiers of services



For example, imagine a scenario where you have a cluster of nodes that run a startup procedure. During startup, you can configure your nodes to report their status to the Runtime Configurator, and then have another application query the Runtime Configurator and run specific tasks based on the status of the nodes.

The Runtime Configurator also offers a Watcher service and a Waiter service. The Watcher service watches a specific key pair and returns when the value of the key pair changes, while the Waiter service waits for a specific end condition and returns a response once that end condition has been met.

You use Runtime Configurator through using the gcloud CLI, or as a standalone API.

## Concepts

  * **Config resource**

A Config resource contains a hierarchical list of variables. You can create different configurations for different purposes. For example, you can separate configurations based on environment (prod, dev, test), based on different tiers of applications or services (back end, front end), or based on entities (one configuration per user of your application).

  * **Variables**

Variables are key value pairs that belong to a RuntimeConfig resource. Variable keys have the following format:
        
        projects/[project_id]/configs/[CONFIG_ID]/variables/[VARIABLE_NAME]
        

You can set, get, and watch variable values to communicate information to your applications, to signal a completed state, to send notification of data changes, and more. Variables are hierarchical, so your variable key could have several levels. For example, sample variable keys could be:
        
        webserver-1/users/name
        webserver-1/users/favorite_color
        

  * **Watchers**

You can use the `watch()` method to watch a variable and return when the variable changes, the watcher times out, or the watcher is deleted. Use the `watch()` functionality to dynamically configure your applications based on changes in your data.

  * **Waiters**

If you create a Waiter resource to watch a specific path prefix, the waiter returns once the number of variables under the prefix reaches a particular amount. This is referred to as a [Cardinality condition](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.waiters#Cardinality).

For example, if you set a condition for the path `/foo` and the number of paths is set to 2, the following setup would meet the condition:

    * `/foo/variable1 = "value1"`
    * `/foo/variable2 = "value2"`
    * `/bar/variable3 = "value3" # Not /foo path`

A waiter has both a failure and success condition that you can set.

After you create a Waiter, the service returns an operation object that you poll for completion. The operation is complete when the one of the following occurs:

    * The `success` condition is met.
    * The `failure` condition is met.
    * The Waiter reached the timeout deadline specified in the initial request.

Using a waiter is ideal for startup scenarios, where you might need to pause a deployment until a certain number of services is running.




## What's next

  * [Creating a RuntimeConfig resource](https://docs.cloud.google.com/deployment-manager/runtime-configurator/create-and-delete-runtimeconfig-resources).
  * [Setting and Getting Data](https://docs.cloud.google.com/deployment-manager/runtime-configurator/set-and-get-variables).
  * [Watching a Specific Variable](https://docs.cloud.google.com/deployment-manager/runtime-configurator/watching-a-variable).
  * [Creating a Waiter](https://docs.cloud.google.com/deployment-manager/runtime-configurator/creating-a-waiter).
  * Refer to the [v1beta1 reference](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest).
  * Refer to the [Quotas for Runtime Configurator](https://cloud.google.com/deployment-manager/pricing-and-quotas#runtime_configurator).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
