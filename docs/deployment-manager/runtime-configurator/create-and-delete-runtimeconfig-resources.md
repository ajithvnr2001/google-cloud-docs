---
url: https://docs.cloud.google.com/deployment-manager/runtime-configurator/create-and-delete-runtimeconfig-resources/
title: Creating and Deleting RuntimeConfig Resources \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:56.956363+00:00
---

# Creating and Deleting RuntimeConfig Resources  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/runtime-configurator/create-and-delete-runtimeconfig-resources/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment)



Send feedback 

#  Creating and Deleting RuntimeConfig Resources Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page explains how to create a Config resource. A Config resource is an API object that stores variables as key value pairs. You need a Config resource before you can set and get variables. After creating a Config resource, you can create arbitrary variables that you can use to store data.

To learn more about configurations, variables, and the Runtime Configurator service, see [Runtime Configurator Fundamentals](https://docs.cloud.google.com/deployment-manager/runtime-configurator).

## Before you begin

  * If you want to use the command-line examples in this guide, install the [`gcloud` command-line tool](https://docs.cloud.google.com/sdk).
  * If you want to use the API examples in this guide, set up [API access](https://docs.cloud.google.com/deployment-manager/docs/reference/latest).
  * Read [Runtime Configurator Fundamentals](https://docs.cloud.google.com/deployment-manager/runtime-configurator).
  * Enable the [Runtime Configurator API](https://console.cloud.google.com/apis/api/runtimeconfig.googleapis.com/overview).



## Creating a config

You can create a Config resource with Deployment Manager, the `gcloud` command-line tool, or directly using the Runtime Configurator API.

###  Deployment Manager 

To create a config in Deployment Manager, specify the RuntimeConfig type:
    
    
    runtimeconfig.v1beta1.config
    

In the `properties` of the resource, provide the `name` and other optional properties if desired:
    
    
    resources:
    - name: [CONFIG_NAME]
      type: runtimeconfig.v1beta1.config
      properties:
        config: [CONFIG_NAME]
        description: [DESCRIPTION]
    

where:

  * `[CONFIG_NAME]` is the name for this config.
  * `[DESCRIPTION]` is the description of this config (optional).



###  gcloud 

With the Google Cloud CLI, use the `gcloud beta runtime-config configs create` command:
    
    
    gcloud beta runtime-config configs create [CONFIG_NAME] --description [DESCRIPTION]
    

where:

  * `[CONFIG_NAME]` is the name for this config.
  * `[DESCRIPTION]` is the description of this config (optional).



`gcloud` returns a response like:
    
    
    Created [https://runtimeconfig.googleapis.com/v1beta1/projects/[PROJECT_ID]/configs/[CONFIG_NAME]].
    

For a complete reference for this `gcloud` command, read the [`runtime-config configs create`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/runtime-config/configs/create) reference documentation.

###  API 

In the REST API, make a `POST` request to the following URI:
    
    
    https://runtimeconfig.googleapis.com/v1beta1/projects/[PROJECT_ID]/configs/
    

where `[PROJECT_ID]` is the project ID for this request. The payload for the request looks like this:
    
    
    {
       "name": "projects/[PROJECT_ID]/configs/[CONFIG_NAME]",
       "description": "[DESCRIPTION]"
    
    }
    

where:

  * `[PROJECT_ID]` is the project ID for this request.
  * `[CONFIG_NAME]` is the name of this RuntimeConfig.
  * `[DESCRIPTION]` is the description of this config (optional).

To learn more about this method, read the [`configs().create`](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs/create) documentation.




## Deleting a RuntimeConfig resource

Deleting a RuntimeConfig resource deletes all resources contained by that resource, including all variables and waiters.

###  Deployment Manager 

Delete a RuntimeConfig resource that is part of a deployment using one of the following methods:

  * [Update the deployment](https://docs.cloud.google.com/deployment-manager/docs/deployments/updating-deployments) to omit the config and redeploy the deployment.
  * [Delete the deployment and the resources it contains](https://docs.cloud.google.com/deployment-manager/docs/deployments/deleting-deployments).



###  gcloud 

With the Google Cloud CLI, use the `gcloud beta runtime-config configs delete` command:
    
    
    gcloud beta runtime-config configs delete [CONFIG_NAME]
    

where `[CONFIG_NAME]` is the name of the configuration object.

The gcloud CLI returns a response like:
    
    
    Deleted [https://runtimeconfig.googleapis.com/v1beta1/projects/[PROJECT_ID]/configs/[CONFIG_NAME]].

For the full `gcloud` reference, read the [`runtime-config configs delete`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/runtime-config/configs/delete) reference documentation.

###  API 

In the REST API, make a `DELETE` request to the following URI:
    
    
    https://runtimeconfig.googleapis.com/v1beta1/projects/[PROJECT_ID]/configs/[CONFIG_NAME]
    

where:

  * `[PROJECT_ID]` is the project ID for this request.
  * `[CONFIG_NAME]` is the name of this configuration.

To learn more about this method, read the [`configs().delete`](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs/delete) documentation.




## What's next

  * Next, create some variables and learn how to [set and get data](https://docs.cloud.google.com/deployment-manager/runtime-configurator/set-and-get-variables).
  * Learn how to set a [Watcher on a specific variable](https://docs.cloud.google.com/deployment-manager/runtime-configurator/watching-a-variable).
  * [Create a Waiter](https://docs.cloud.google.com/deployment-manager/runtime-configurator/creating-a-waiter) that returns when a variable reaches a Cardinality condition.
  * Refer to the [v1beta1 reference](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest).
  * Refer to the [Quotas for Runtime Configurator](https://cloud.google.com/deployment-manager/pricing-and-quotas#runtime_configurator).
  * Learn about [Runtime Configurator](https://docs.cloud.google.com/deployment-manager/runtime-configurator).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
