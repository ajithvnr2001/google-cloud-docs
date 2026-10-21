---
url: https://docs.cloud.google.com/deployment-manager/runtime-configurator/creating-a-waiter/
title: Creating a Waiter \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:46:58.306052+00:00
---

# Creating a Waiter  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/runtime-configurator/creating-a-waiter/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment)



Send feedback 

#  Creating a Waiter Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page explains how to create a Waiter resource. To learn more about waiters, read the [Runtime Configurator Fundamentals](https://docs.cloud.google.com/deployment-manager/runtime-configurator).

A Waiter resource waits for a certain success or failure condition before returning a response. For both success and failure, you set a Cardinality condition, where the waiter waits for some number of variables to be created under a specific path prefix. After the variables have been created, the waiter returns. Your application code can then respond to its success or failure. If the current state of your variables already match either the success or failure end conditions, the waiter will return success or failure immediately.

**Note:** The waiter does not care about the value of the variables under the specific prefix; it only cares that there is the specified number of variables under the desired prefix. Also, cardinality conditions are recursive, so the waiter counts all items under a specific key, including any keys that might, in turn, contain a subtree of keys.

## Before you begin

  * If you want to use the command-line examples in this guide, install the [`gcloud` command-line tool](https://docs.cloud.google.com/sdk).
  * If you want to use the API examples in this guide, set up [API access](https://docs.cloud.google.com/deployment-manager/docs/reference/latest).
  * Read [Runtime Configurator Fundamentals](https://docs.cloud.google.com/deployment-manager/runtime-configurator). 
  * Read [Creating and Deleting RuntimeConfig Resources](https://docs.cloud.google.com/deployment-manager/runtime-configurator/create-and-delete-runtimeconfig-resources).
  * Read [Setting and Getting Data](https://docs.cloud.google.com/deployment-manager/runtime-configurator/set-and-get-variables).



## Creating a waiter

To create a waiter:

  1. Determine your success, and optionally, failure condition for the waiter.

For example, the following sample code sets the conditions for success and failure, where the waiter returns successfully if the number of paths under `/status/success` is three and fails if the path under `/status/failure` is two:
         
         {
             'name': 'projects/[PROJECT_ID]/configs/[CONFIG_NAME]/waiters/[WAITER_NAME]',
             'timeout': '360s',
             'success': {
                'cardinality': {
                   'path': '/status/success',
                   'number': 3
                }
             },
             'failure': {
                'cardinality': {
                   'path': '/status/failure',
                   'number': 2
                }
              }
         }
         

**Best practices for defining a waiter:**

     * Only one success condition and one failure condition is allowed per waiter.
     * You should maintain one waiter per path.
     * Failure conditions are always evaluated before success conditions.
     * Do not overlap path prefixes between conditions.
  2. Create the waiter.

###  Deployment Manager 

To create a waiter in Deployment Manager, specify the waiter type:
         
         runtimeconfig.v1beta1.waiter
         

In the properties of the waiter, provide the `name`, `location`, `timeout`, and the end conditions of the waiter:
         
         - name: [NAME]
           type: runtimeconfig.v1beta1.waiter
           properties:
             parent: $(ref.[CONFIG_NAME].name)
             waiter: [WAITER_NAME]
             timeout: [TIMEOUT_SECS]
             success:
               cardinality:
                 path: [SUCCESS_PATH_PREFIX]
                 number: [SUCCESS_NUMBER]
         

where:

     * `[NAME]` is the resource name.
     * `[CONFIG_NAME]` is the Config resource for this request.
     * `[WAITER_NAME]` is the name for this waiter.
     * `[TIMEOUT_SECS]` is the number of seconds to wait before the waiter times out. For example, for 300 seconds, use `300s`.
     * `[SUCCESS_PATH_PREFIX]` is the path prefix to watch for a success condition.
     * `[SUCCESS_NUMBER]` is the number of variables that exist under this path to be considered successful.

###  gcloud 

With the Google Cloud CLI:
    
    gcloud beta runtime-config configs waiters create [WAITER_NAME] \
        --config-name [CONFIG_NAME] \
        --success-cardinality-path [SUCCESS_PATH_PREFIX] \
        --success-cardinality-number [SUCCESS_NUMBER] --timeout [TIMEOUT_SECS]
    

where:

     * `[WAITER_NAME]` is the name for this waiter.
     * `[CONFIG_NAME]` is the RuntimeConfig resource for this request.
     * `[SUCCESS_PATH_PREFIX]` is the path prefix to watch for a success condition.
     * `[SUCCESS_NUMBER]` is the number of variables that exist under this path to be considered successful.
     * `[TIMEOUT_SECS]` the number of seconds to wait before the waiter times out.

The gcloud CLI returns a response like:

Created [https://runtimeconfig.googleapis.com/v1beta1/projects/[PROJECT_ID]/configs/[CONFIG_NAME]/waiters/example-waiter].

After creating the waiter, the tool polls the related Operations resource until the waiter returns with one of the applicable responses.

For a complete reference for this `gcloud` command, read the [`runtime-config configs waiters`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/runtime-config/configs/waiters) reference documentation.

###  API 

In the API, make a `POST` request to the following URI:
    
    https://runtimeconfig.googleapis.com/v1beta1/projects/[PROJECT_ID]/configs/[CONFIG_NAME]/waiters
    

where:

     * `[PROJECT_ID]` is the project ID for this request.
     * `[CONFIG_NAME]` is the name of the configuration for this request.

The request payload must contain the waiter name, the success condition, and the timeout duration:
    
    {
     'name': 'projects/[PROJECT_ID]/configs/[CONFIG_NAME]/waiters/[WAITER_NAME]',
     'timeout': '[TIMEOUT_SEC]',
     'success': {
        'cardinality': {
           'path': '[SUCCESS_PATH_PREFIX]',
           'number': '[SUCCESS_NUMBER]'
        }
      }
    }
    

where:

     * `[PROJECT_ID]` is the project ID for this request.
     * `[CONFIG_NAME]` is the name of the configuration for this request.
     * `[WAITER_NAME]` is the name of the waiter to create.
     * `[TIMEOUT_SECS]` the number of seconds to wait before the waiter times out.
     * `[SUCCESS_PATH_PREFIX]` is the path prefix to watch for a success condition.
     * `[SUCCESS_NUMBER]` is the number of variables that exist under this path to be considered successful.

If successful, the request returns the name of the operations object that you poll for completion:
    
    {
        "name": "projects/[PROJECT_ID]/[CONFIG_NAME]/operations/waiters/[WAITER_NAME]"
    }
    

Next, poll the waiter to periodically check when the waiter returns.

To learn more about the method, read the [`waiters().create`](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.waiters/create) documentation.




## Polling a waiter

After creating a waiter, poll the related [Operations resource](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.operations) to check whether the waiter has met one of the end conditions. If the waiter has met an end condition or has timed out, the operation returns as `done` and returns a response based on the results of the waiter.

**Note:** If a newly-created waiter's operation finishes immediately, check whether the current state of your variables already match either end condition.

Use `gcloud` or the API to poll a waiter.

###  gcloud 

With the Google Cloud CLI, when you make a request to create a waiter, the tool automatically performs polling and waits for the waiter to return. The tool prints a response like the following while it is polling the waiter:
    
    
    Waiting for waiter [WAITER_NAME] to finish...
    

If you don't want the tool to poll the waiter after creating it, supply the `--async` flag with your creation request.

###  API 

In the REST API, make a `GET` request to the following URI to get the status of the waiter operation:
    
    
    https://runtimeconfig.googleapis.com/v1beta1/projects/[PROJECT_ID]/configs/[CONFIG_NAME]/operations/waiters/[WAITER_NAME]
    

where:

  * `[PROJECT_ID]` is the project ID for this request.
  * `[CONFIG_NAME]` is the name of the configuration for this request.
  * `[WAITER_NAME]` is the name of the waiter to poll.



If the operation is still ongoing, the API returns a response like following, lacking a status:
    
    
    {
      "name": "projects/[PROJECT_NAME]/configs/[CONFIG_NAME]/operations/waiters/[WAITER_NAME]"
    }
    

If the operation is complete, the operation is marked as `done` and returns one of the responses described in the Waiter responses section.

To learn more about the method, read the [`waiters().create`](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.waiters/create) documentation.

## Waiter responses

### Successful end condition

If the waiter has met a **successful** end condition, the operation returns the Waiter resource:
    
    
    {
      "name": "projects/[PROJECT_NAME]/configs/[CONFIG_NAME]/operations/waiters/[WAITER_NAME]",
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.runtimeconfig.v1beta1.Waiter",
        "name": "projects/[PROJECT_NAME]/configs/[CONFIG_NAME]/waiters/[WAITER_NAME]",
        "timeout": "360.000s",
        "failure": {
          "cardinality": {
            "path": "[SUCCESS_PATH_PREFIX]",
            "number": "[SUCCESS_NUMBER]"
          }
        },
        "success": {
          "cardinality": {
            "path": "[FAILURE_PATH_PREFIX]",
            "number": [FAILURE_NUMBER]
          }
        },
        "createTime": "2016-04-12T18:02:13.316695490Z",
        "done": true
      }
    }
    

### Failure condition

If the waiter meets the **failure** end condition or timed out, the operation returns an error.

**Failure condition was met**
    
    
    {
      "name": "projects/[PROJECT_NAME]/configs/[CONFIG_NAME]/operations/waiters/[WAITER_NAME]",
      "done": true,
      "error": {
        "code": 9,
        "message": "Failure condition satisfied."
      }
    }
    

**Waiter timed out**
    
    
    {
      "name": "projects/[PROJECT_NAME]/configs/[CONFIG_NAME]/operations/waiters/[WAITER_NAME]",
      "done": true,
      "error": {
        "code": 4,
        "message": "Timeout expired."
      }
    }
    

## What's next

  * Learn about [Runtime Configurator](https://docs.cloud.google.com/deployment-manager/runtime-configurator).
  * Learn how to [set and get variables](https://docs.cloud.google.com/deployment-manager/runtime-configurator/set-and-get-variables).
  * Set a [Watcher a specific variable](https://docs.cloud.google.com/deployment-manager/runtime-configurator/watching-a-variable).
  * [Create and delete RuntimeConfig Resources](https://docs.cloud.google.com/deployment-manager/runtime-configurator/create-and-delete-runtimeconfig-resources).
  * Refer to the [v1beta1 reference](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest).
  * Refer to the [Quotas for Runtime Configurator](https://cloud.google.com/deployment-manager/pricing-and-quotas#runtime_configurator).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
