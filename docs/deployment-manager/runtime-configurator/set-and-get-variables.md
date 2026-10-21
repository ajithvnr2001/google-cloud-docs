---
url: https://docs.cloud.google.com/deployment-manager/runtime-configurator/set-and-get-variables/
title: Setting and Getting Data \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:46:58.230235+00:00
---

# Setting and Getting Data  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/runtime-configurator/set-and-get-variables/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment)



Send feedback 

#  Setting and Getting Data Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page explains how to set, get, and update variables using the Runtime Configurator. Variables are key value pairs that belong to a RuntimeConfig resource. Each key value pair contains data that you define. After creating a variable, you can set a [watcher](https://docs.cloud.google.com/deployment-manager/runtime-configurator/watching-a-variable) or [waiter](https://docs.cloud.google.com/deployment-manager/runtime-configurator/creating-a-waiter) on it.

To learn more about variables and the Runtime Configurator service, see [Runtime Configurator Fundamentals](https://docs.cloud.google.com/deployment-manager/runtime-configurator) documentation.

To learn how to create a RuntimeConfig resource, see [Creating and Deleting RuntimeConfig Resources](https://docs.cloud.google.com/deployment-manager/runtime-configurator/create-and-delete-runtimeconfig-resources).

## Before you begin

  * If you want to use the command-line examples in this guide, install the [`gcloud` command-line tool](https://docs.cloud.google.com/sdk).
  * If you want to use the API examples in this guide, set up [API access](https://docs.cloud.google.com/deployment-manager/docs/reference/latest).
  * Read [Runtime Configurator Fundamentals](https://docs.cloud.google.com/deployment-manager/runtime-configurator). 
  * Read [Creating and Deleting RuntimeConfig Resources](https://docs.cloud.google.com/deployment-manager/runtime-configurator/create-and-delete-runtimeconfig-resources).



## Creating a variable

A variable is a key value pair. A variable key can be flat or hierarchical. For example, all of the following are valid keys:

  * `status`
  * `users/jane-smith/favorite-color`
  * `users/total`



Only leaf node keys can have values. In the example above, you cannot assign a value to:

  * `users`
  * `users/jane-smith`



This is because both these keys contain other keys beneath them.

To create a variable, use Deployment Manager, the Google Cloud CLI, or the API.

###  Deployment Manager 

To create a variable in Deployment Manager, specify the variable type:
    
    
    runtimeconfig.v1beta1.variable
    

In the properties of the variable, provide the `name`, `location`, and `value` of the variable:
    
    
    - name: [NAME]
      type: runtimeconfig.v1beta1.variable
      properties:
        parent: $(ref.[CONFIG_NAME].name)
        variable: [VARIABLE_KEY]
        [value | text]: [VARIABLE_VALUE]
    

where:

  * `[NAME]` is the arbitrary resource name for this variable. This is not the name of the variable itself.
  * `[CONFIG_NAME]` is the Config resource for this request.
  * `[VARIABLE_KEY]` is the key of this variable. For example, `status` and `users/jane-smith/favorite_color` are valid keys. Variable keys can contain `/`. A variable key can contain digits, letters, dashes, and slashes, and the max length for a name is 256 characters.
  * `[VARIABLE_VALUE]` is the value for this variable. Depending on whether you want to assign a value as plaintext, or as a based64 encoded string, choose either the `value` or `text` property: 
    * `value`: If providing a value as a [base64 encoded](https://en.wikipedia.org/wiki/Base64) string, use the `value` property.
    * `text`: If providing a plaintext string, use the `text` property. The string must be valid UTF-8.



###  gcloud 

To create a variable with the Google Cloud CLI, use the `runtime-config configs variables set` command:
    
    
    gcloud beta runtime-config configs variables set [VARIABLE_KEY] \
        [VARIABLE_VALUE] --config-name [CONFIG_NAME] [--is-text]
    

where:

  * `[VARIABLE_KEY]` is the key of the variable. For example, `status` and `users/jane-smith/favorite_color` are valid keys. Variable keys can contain `/`. A variable key can contain digts, letters, dashes, and slashes, and the max length for a name is 256 characters.
  * `[VARIABLE_VALUE]` is the value of this variable. You can assign a value as plaintext, or as a [based64 encoded](https://en.wikipedia.org/wiki/Base64) string. If specifying a plaintext value, provide the `--is-text` flag; otherwise, the Google Cloud CLI will encode the value in base64 encoding.
        
        gcloud beta runtime-config configs variables set [VARIABLE_KEY] \
              [VARIABLE_VALUE] --config-name [CONFIG_NAME] --is-text
        

You can also supply the variable value from a file. For example:
        
        cat [FILE_NAME] | gcloud beta runtime-config configs variables set [VARIABLE_KEY] --config-name [CONFIG_NAME]
        

**Note:** You do not need to encode this value because `gcloud` will perform the encoding for you.

  * `[CONFIG_NAME]` is the name of the RuntimeConfig resource where this variable should be created in. For example, `frontend-config`.

For example:
        
        gcloud beta runtime-config configs variables set example-variable \
              my-test-value --config-name example-config
        

The gcloud CLI returns a response like:



    
    
    Created [https://runtimeconfig.googleapis.com/v1beta1/projects/[PROJECT_ID]/configs/[CONFIG_NAME]/variables/[VARIABLE_KEY]].
    

By default, any existing variables will be silently overwritten. If you want to preserve a variable that exists, include the `--fail-if-present` flag, which creates the new variable if it doesn't exist.

Similarly, you can also fail the request of the variable is absent by providing the `--fail-if-absent` flag.

For the complete reference for this `gcloud` command, read the [`runtime-config variables set`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/runtime-config/configs/variables/set) reference documentation.

###  API 

In the REST API, make a `POST` request to the following URI to create a new variable:
    
    
    https://runtimeconfig.googleapis.com/v1beta1/projects/[PROJECT_ID]/configs/[CONFIG_NAME]/variables
    

where `[PROJECT_ID]` is the project ID for this request. The request payload contains the URI to the RuntimeConfig resource and either the plaintext value of the key, or the base64 encoded value:
    
    
    {
       "name": "projects/[PROJECT_ID]/configs/[CONFIG_NAME]/variables/[VARIABLE_KEY]"
       "[value | text]": "[VARIABLE_VALUE]" # Choose either 'value' or 'text' but not both
    }
    

where:

  * `[PROJECT_ID]` is the project ID for this request.
  * `[CONFIG_NAME]` is the name of this configuration.
  * `[VARIABLE_KEY]` is the key of the variable. For example, `status` and `users/jane-smith/favorite_color`. Variable keys can contain `/`. A variable key can contain digts, letters, dashes, and slashes, and the max length for a name is 256 characters.
  * `[VARIABLE_VALUE]` is the value for this variable. Depending on whether you want to assign a value as plaintext, or as a based64 encoded string, choose either the `value` or `text` property:

    * `value`: If providing a value as a [base64 encoded](https://en.wikipedia.org/wiki/Base64) string, use the `value` property.
    * `text`: If providing a plaintext string, use the `text` property. The string must be valid UTF-8.

If successful, the API returns a response like:
    
    {
    "name": "projects/[PROJECT_ID]/configs/[CONFIG_NAME]/variables/[VARIABLE_KEY]",
    "value": "dGVhbA==",
    "updateTime": "2016-04-11T21:49:00.773366134Z"
    }

To learn more about the method, read the [`variables().create`](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables/create) documentation.




## Updating a variable

###  Deployment Manager 

To update a variable in Deployment Manager:

  1. Define or update your variable properties as described in Creating a variable.

  2. Follow the steps to [make the update request](https://docs.cloud.google.com/deployment-manager/docs/deployments/updating-deployments#make_the_update_request).




###  gcloud 

Update a variable using the same process to create a variable.

###  API 

In the REST API, make a `PUT` request to the following URI to update a variable:
    
    
    https://runtimeconfig.googleapis.com/v1beta1/projects/[PROJECT_ID]/configs/[CONFIG_NAME]/variables/[VARIABLE_KEY]
    

where:

  * `[PROJECT_ID]` is the project ID for this request.
  * `[CONFIG_NAME]` is the name of this configuration.
  * `[VARIABLE_VALUE]` is the value for this variable. This is a string that has been [base64 encoded](https://en.wikipedia.org/wiki/Base64).



The payload of the request must be:
    
    
    {
       "[value | text]": "[VARIABLE_VALUE]" # Choose either 'value' or 'text' but not both
    }
    

where `[VARIABLE_VALUE]` is the value for this variable. Depending on whether you want to assign a value as plaintext, or as a base64 encoded string, choose either the `value` or `text` property:

  * `value`: If providing a value as a [base64 encoded](https://en.wikipedia.org/wiki/Base64) string, use the `value` property.
  * `text`: If providing a plaintext string, use the `text` property. The string must be valid UTF-8.



If successful, the API returns a response like:
    
    
    {
      "name": "projects/[PROJECT_ID]/configs/[CONFIG_NAME]/variables/[VARIABLE_KEY]",
      "value": "dGVhbA==",
      "updateTime": "2016-04-11T21:46:11.591713370Z",
      "state": "UPDATED"
    }

To learn more about the method, read the [`variables().create`](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables/update) documentation.

## Getting a variable's value

###  Deployment Manager 

Get a variable's value using one of the following methods:

  * [Make a `get` request to the variable](https://docs.cloud.google.com/deployment-manager/docs/reference/latest/resources/get).
  * [View the deployment's manifest](https://docs.cloud.google.com/deployment-manager/docs/deployments/viewing-manifest).



###  gcloud 

To create a variable with the Google Cloud CLI, use the `runtime-config configs variables get-value` command:
    
    
    gcloud beta runtime-config configs variables get-value [VARIABLE_KEY] --config-name [CONFIG_NAME]
    

where:

  * `[VARIABLE_KEY]` is the key of the variable. For example, `status`, `users/jane-smith/favorite_color`.
  * `[CONFIG_NAME]` is the name of the RuntimeConfig resource for this variable. For example, `website`.

The gcloud CLI returns a response like:
        
        example-value




You can also get a list of variables for which you have [`runtimeconfig.variables.get` permission](https://docs.cloud.google.com/deployment-manager/runtime-configurator/access-control#permissions) and their values by using the `list` command and supplying the `--values` flag. For example:
    
    
    gcloud beta runtime-config configs variables list --config-name example-config --values
    

The gcloud CLI returns a list like so:
    
    
    NAME                         UPDATE_TIME                     VALUE
    not-my-favorite-color/shade  2016-04-18T21:14:59.932428461Z  orange
    not-my-favorite-food/group   2016-04-18T21:14:59.932428461Z  vegetables
    

Any variables for which you do not have `get` permission will be omitted. That includes variables where you have `list` permission but not `get` permission.

For the complete reference for this `gcloud` command, read the [`runtime-config variables`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/runtime-config/configs/variables) reference documentation.

###  API 

In the REST API, make a `GET` request to the following URI to get a variable's value:
    
    
    https://runtimeconfig.googleapis.com/v1beta1/projects/[PROJECT_ID]/configs/[CONFIG_NAME]/variables/[VARIABLE_KEY]
    

where:

  * `[PROJECT_ID]` is the project ID for this request.
  * `[CONFIG_NAME]` is the name of this configuration.
  * `[VARIABLE_KEY]` is the name for this request.



If successful, the API returns a response with the base64 encoded value of the variable:
    
    
    {
      "name": "projects/[PROJECT_ID]/configs/[CONFIG_NAME]/variables/[VARIABLE_KEY]",
      "value": "[VARIABLE_VALUE]",
      "updateTime": "2016-04-11T21:49:00.773366134Z"
    }

You must decode the value yourself to get the string. To learn more about the method, read the [`variables().get`](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables/get) documentation.

If you want to get a list of variables for which you have [`runtimeconfig.variables.get` permission](https://docs.cloud.google.com/deployment-manager/runtime-configurator/access-control#permissions) and their values, use the `returnValues` method. For example:
    
    
    GET uri: https://runtimeconfig.googleapis.com/v1beta1/projects/myproject/configs/example-config/variables?returnValues=True
    

The API returns all variables for which you have permission:
    
    
    {
      "variables": [
        {
          "name": "projects/compute-writers-project/configs/example-config/variables/not-my-favorite-color/shade",
          "updateTime": "2016-04-18T21:14:59.932428461Z",
          "value": "b3Jhbmdl"
        }
      ]
    }
    

Similarly, you must decode the value yourself to get the string.

To learn more about the method, read the [`variables().list`](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables/list) documentation.

## What's next?

  * Learn about [Runtime Configurator](https://docs.cloud.google.com/deployment-manager/runtime-configurator).
  * [Watching a Specific Variable](https://docs.cloud.google.com/deployment-manager/runtime-configurator/watching-a-variable).
  * [Creating a Waiter](https://docs.cloud.google.com/deployment-manager/runtime-configurator/creating-a-waiter).
  * [Creating and Deleting RuntimeConfig Resources](https://docs.cloud.google.com/deployment-manager/runtime-configurator/create-and-delete-runtimeconfig-resources).
  * Refer to the [v1beta1 reference](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest).
  * Refer to the [Quotas for Runtime Configurator](https://cloud.google.com/deployment-manager/pricing-and-quotas#runtime_configurator).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
