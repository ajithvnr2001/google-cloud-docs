---
url: https://docs.cloud.google.com/deployment-manager/docs/migrations/custom-types-custom-backends/
title: Creating custom type providers with custom backends \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:10.079053+00:00
---

# Creating custom type providers with custom backends  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/docs/migrations/custom-types-custom-backends/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment)



Send feedback 

#  Creating custom type providers with custom backends Stay organized with collections  Save and categorize content based on your preferences. 

This page describes creating custom types for Google Cloud Deployment Manager that are backed by custom backends.

The [Actions feature](https://docs.cloud.google.com/deployment-manager/docs/migrations/actions) is an alpha feature that expands the range of API methods that Deployment Manager can call. Because this feature is unsupported, we recommend that you [migrate your existing usage](https://docs.cloud.google.com/deployment-manager/docs/migrations/actions#migrating) of Actions to supported alternatives. Some Actions, such as `storage.buckets.setIamPolicy`, correspond to existing Deployment Manager resource types, which you [can use to replace them](https://docs.cloud.google.com/deployment-manager/docs/migrations/storage-buckets-setiampolicy). If your deployment requires the use of Actions that can't be replaced by existing [supported Deployment Manager resource types](https://docs.cloud.google.com/deployment-manager/docs/configuration/supported-resource-types), follow this guide to create a custom type with a custom backend to replace your usage of these Actions.

# Creating your custom type provider

For a high-level overview of integrating a third-party API with Deployment Manager, visit [Integrating with Deployment Manager](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/process-adding-api).

For instructions on adding an API as a type provider, visit [Adding an API as a type provider](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/creating-type-provider).

For advanced configuration options, such as input mappings, visit [Setting advanced API options](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/advanced-configuration-options).

For the requirements to add an API to Deployment Manager, visit [API requirements for integrating an API](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/api-requirements).

# Creating your custom backend

You must create a custom backend to expose the API to your custom type provider. To create a custom backend, you can use one of the following methods:

  * Building and hosting a RESTful service on a platform of your choice. Refer to the [requirements for integrating an API](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/api-requirements).

  * Using one of the following serverless solutions to implement your custom backend:

    * [Cloud Run functions](https://docs.cloud.google.com/functions)

    * [Cloud Run](https://docs.cloud.google.com/run)

    * [App Engine](https://docs.cloud.google.com/appengine), in [standard or flexible mode](https://docs.cloud.google.com/appengine/docs/the-appengine-environments)




One way to reduce the development effort of creating a custom backend is to use [Cloud Run functions](https://docs.cloud.google.com/functions). If you already use other serverless solutions as a part of your development process, it might be more efficient to use those instead. For an overview of using Cloud Run functions as the backend for a custom type provider, visit the [Custom Type Provider](https://github.com/GoogleCloudPlatform/deploymentmanager-samples/blob/fa69cee7cf6cb09e9fc1d6c353c7d438d85ea554/google/resource-snippets/functions-backed-type/readme.md#high-level-approach) example implementation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
