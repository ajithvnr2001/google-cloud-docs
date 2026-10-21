---
url: https://docs.cloud.google.com/deployment-manager/docs/configuration/describing-listing-deleting-types/
title: Describing, listing, and deleting types \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:46:55.665447+00:00
---

# Describing, listing, and deleting types  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/docs/configuration/describing-listing-deleting-types/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment)



Send feedback 

#  Describing, listing, and deleting types Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to describe, list, and delete types from your project.

## Before you begin

  * If you want to use the command-line examples in this guide, install the [`gcloud` command-line tool](https://docs.cloud.google.com/sdk).
  * If you want to use the API examples in this guide, set up [API access](https://docs.cloud.google.com/deployment-manager/docs/reference/latest).
  * Set up [v2beta API access](https://docs.cloud.google.com/deployment-manager/docs/reference/v2beta) if you want to use the API examples in this guide.



## Describing Type Providers

A [type provider](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/process-adding-api) is an API that has been integrated with Deployment Manager as a type. You can describe a single type provider, get a list of all type providers, or get a list of all types provided by a type provider.

### Describing a single type provider

You can describe a type provider to get information such as the descriptor document URL and advanced API options that have been set for this API.

[See the list of default Google Cloud type providers](https://docs.cloud.google.com/deployment-manager/docs/configuration/supported-gcp-types).

###  gcloud 

Run the `type-providers describe` command to describe a type provider.
    
    
    gcloud beta deployment-manager type-providers describe PROVIDER_NAME --project PROJECT_ID
    

For example, use this command to describe the Pub/Sub type provider:
    
    
    gcloud beta deployment-manager type-providers describe pubsub-v1 --project gcp-types
    

###  API 

Make a `GET` request to the following URI:
    
    
    https://www.googleapis.com/deploymentmanager/v2beta/projects/[PROJECT_ID]/global/typeProviders/[PROVIDER_NAME]
    

For example, use this URI for the Pub/Sub type provider:
    
    
    https://www.googleapis.com/deploymentmanager/v2beta/projects/gcp-types/global/typeProviders/pubsub-v1
    

### Getting a list of types provided by a type provider

A type provider exposes all resources of the underlying API as base types. You can get a list of base types provided by a type provider.

###  gcloud 

To get a list of base types provided by a type provider:
    
    
    gcloud beta deployment-manager types list --provider [TYPE_PROVIDER] --project [PROJECT_ID]
    

For example, to get a list of base types in the Compute Engine type provider, run this command:
    
    
    gcloud beta deployment-manager types list --provider compute-v1 --project gcp-types
    

###  API 

Make a `GET` request to the following URI:
    
    
    GET https://www.googleapis.com/deploymentmanager/v2beta/projects/[PROJECT_ID]/global/typeProviders/[PROVIDER_NAME]/types
    

For example, for a list of types in the Compute Engine type provider, use this URI:
    
    
    GET https://www.googleapis.com/deploymentmanager/v2beta/projects/gcp-types/global/typeProviders/compute-v1/types
    

### Listing type providers

You can get a list of your type providers using the gcloud CLI, or the API.

###  gcloud 

To list your type providers, make a `type-providers list` request:
    
    
    gcloud beta deployment-manager type-providers list
    

###  API 

In the API, make a `GET` request to the global type providers list:
    
    
    GET https://www.googleapis.com/deploymentmanager/v2/projects/[PROJECT_ID]/global/typeProviders
    

For more information, see the documentation for the [`list`](https://docs.cloud.google.com/deployment-manager/docs/reference/v2beta/typeProviders/list) method.

## Describing composite types

A [composite type](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/create-composite-types) is a set of templates that have been permanently added to Deployment Manager as a type. You can describe a single composite type or get a list of composite types available to the project.

### Describing a single composite type

You can describe a single composite type to get information about the type.

###  gcloud 

Run the `types describe` command to describe a type:
    
    
    gcloud beta deployment-manager types describe [COMPOSITE_TYPE_NAME] --provider composite
    

###  API 

Make a `GET` request to the following URI:
    
    
    https://www.googleapis.com/deploymentmanager/v2beta/projects/[PROJECT_ID]/global/compositeTypes/[COMPOSITE_TYPE_NAME]
    

### Listing composite types

You can get a list of your composite types using the gcloud CLI, or the API.

###  gcloud 

To list your composite types, make a `types list` request:
    
    
    gcloud beta deployment-manager types list --provider composite
    

###  API 

In the API, make a `GET` request to the global types list:
    
    
    GET https://www.googleapis.com/deploymentmanager/v2/projects/[PROJECT_ID]/global/types
    

For more information, see the documentation for the [`list`](https://docs.cloud.google.com/deployment-manager/docs/reference/v2beta/types/list) method.

## Deleting a type provider

###  gcloud 

To delete a type provider, make a `type-providers delete` request. For example:
    
    
    gcloud beta deployment-manager type-providers delete [TYPE_PROVIDER]
    

###  API 

In the API, make a `DELETE` request to the type provider you want to delete:
    
    
    DELETE https://www.googleapis.com/deploymentmanager/v2beta/projects/[PROJECT_ID]/global/typeProviders/[TYPE_PROVIDER]
    

For more information, see the documentation for the [`delete`](https://docs.cloud.google.com/deployment-manager/docs/reference/v2beta/typeProviders/delete) method.

## Deleting a composite type

###  gcloud 

To delete a composite type, make a `types delete` request. For example:
    
    
    gcloud beta deployment-manager types delete [COMPOSITE_TYPE]
    

###  API 

In the API, make a `DELETE` request to the type you want to delete:
    
    
    DELETE https://www.googleapis.com/deploymentmanager/v2beta/projects/[PROJECT_ID]/global/compositeTypes/[COMPOSITE_TYPE]
    

For more information, see the documentation for the [`delete`](https://docs.cloud.google.com/deployment-manager/docs/reference/v2beta/compositeTypes/delete) method.

## What's next

  * Learn how to [use a type provider](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/calling-type-provider).
  * Read about [creating a configuration](https://docs.cloud.google.com/deployment-manager/docs/configuration).
  * [Create a deployment](https://docs.cloud.google.com/deployment-manager/docs/deployments).
  * Learn how to [create a type provider](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/creating-type-provider).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
