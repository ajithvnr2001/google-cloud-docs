---
url: https://docs.cloud.google.com/deployment-manager/runtime-configurator/deleting-a-variable/
title: Deleting a Variable \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:46:58.092742+00:00
---

# Deleting a Variable  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/runtime-configurator/deleting-a-variable/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment)



Send feedback 

#  Deleting a Variable Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page explains how to delete variables. To learn more about variables and the Runtime Configurator service, [Runtime Configurator Fundamentals](https://docs.cloud.google.com/deployment-manager/runtime-configurator).

To learn how to create a variable, see [Setting and Getting Data](https://docs.cloud.google.com/deployment-manager/runtime-configurator/set-and-get-variables).

## Before you begin

  * If you want to use the command-line examples in this guide, install the [`gcloud` command-line tool](https://docs.cloud.google.com/sdk).
  * If you want to use the API examples in this guide, set up [API access](https://docs.cloud.google.com/deployment-manager/docs/reference/latest).
  * Read [Runtime Configurator Fundamentals](https://docs.cloud.google.com/deployment-manager/runtime-configurator). 
  * Read [Creating and Deleting RuntimeConfig Resources](https://docs.cloud.google.com/deployment-manager/runtime-configurator/create-and-delete-runtimeconfig-resources).
  * Read [Setting and Getting Data](https://docs.cloud.google.com/deployment-manager/runtime-configurator/set-and-get-variables).



## Deleting a variable

You can delete a single variable or recursively delete all variables under a specific path.

###  Deployment Manager 

Delete a variable that is part of a deployment using one of the following methods:

  * [Update the deployment](https://docs.cloud.google.com/deployment-manager/docs/deployments/updating-deployments) to omit the variable and redeploy the deployment.
  * [Delete the deployment and the resources it contains](https://docs.cloud.google.com/deployment-manager/docs/deployments/deleting-deployments).



###  gcloud 

To delete a variable with the Google Cloud CLI, use the `runtime-config configs variables delete` command:
    
    
    gcloud beta runtime-config configs variables unset [VARIABLE_KEY] --config-name [CONFIG_NAME]
    

where `[VARIABLE_KEY]` is the key of the variable and `[CONFIG_NAME]` is the name of the config this variable belongs to.

If you want to recursively delete all variables under a certain path, provide the `--recursive` flag.

The gcloud CLI returns a response like:
    
    
    Deleted [https://runtimeconfig.googleapis.com/v1beta1/projects/[PROJECT_ID]/configs/[CONFIG_NAME]/variables/[VARIABLE_KEY].

###  API 

In the REST API, make a `DELETE` request to the following URI to delete a new variable:
    
    
    https://runtimeconfig.googleapis.com/v1beta1/projects/[PROJECT_ID]/configs/[CONFIG_NAME]/variables/[VARIABLE_KEY]
    

where:

  * `[PROJECT_ID]` is the project ID for this request.
  * `[CONFIG_NAME]` is the name for this configuration.
  * `[VARIABLE_KEY]` is the variable to delete.

If you want to recursively delete all variables under a specific pass, provide a payload with your request that has the `recursive` property set to `true`:

{ "recursive": true }

If successful, the API returns an empty response.

To learn more about the method, read the [`variables().delete`](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables/delete) documentation.




## What's next?

  * Learn about [Runtime Configurator](https://docs.cloud.google.com/deployment-manager/runtime-configurator).
  * [Setting and Getting Data](https://docs.cloud.google.com/deployment-manager/runtime-configurator/set-and-get-variables).
  * [Watching a Specific Variable](https://docs.cloud.google.com/deployment-manager/runtime-configurator/watching-a-variable).
  * [Creating a Waiter](https://docs.cloud.google.com/deployment-manager/runtime-configurator/creating-a-waiter).
  * Refer to the [v1beta1 reference](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest).
  * Refer to the [Quotas for Runtime Configurator](https://cloud.google.com/deployment-manager/pricing-and-quotas#runtime_configurator).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
