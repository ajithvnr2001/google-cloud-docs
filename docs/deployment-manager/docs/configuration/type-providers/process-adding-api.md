---
url: https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/process-adding-api/
title: Integrating with Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:11.442939+00:00
---

# Integrating with Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/process-adding-api/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment)



Send feedback 

#  Integrating with Deployment Manager Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Deployment Manager offers the ability to register a third-party API with the Deployment Manager service. After registering an API as a [type provider](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/creating-type-provider) with Deployment Manager, you can use Deployment Manager to deploy resources from the API as types in your configuration.

This document is a one-page guide that describes the process of integrating a third-party API with Deployment Manager. This page does not contain comprehensive instructions for each step of the process but provides an overview and additional links for more information. Use this page to gain a high-level view of the process for adding an API but refer to the detailed documentation for step-by-step instructions.

## Determining if an API is eligible for integrating with Deployment Manager

Deployment Manager has certain expectations of any API that attempts to integrate with it. Specifically:

  * Deployment Manager expects a RESTful API. That is, the API exposes a REST-like interface with Create, Read, Update, and Delete (CRUD) methods.
  * All path and query parameters resolve successfully. All path and query parameters of the API must exist as part of the resource body or exist on all methods of the API, so that Deployment Manager can match the parameter when a user supplies it.
  * The API's descriptor document endpoint must be accessible. Deployment Manager makes an HTTP request to get an API's descriptor document so the document must be hosted somewhere accessible by Deployment Manager. The document must be publicly available or protected by basic authentication.
  * Related to the previous point, the API has either basic authentication, or, if the API is running on Google Kubernetes Engine or Google Cloud Endpoints, the API supports OAuth 2.0 authentication using an access token from the project's service account. Read more about [authentication](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/creating-type-provider#authentication).
  * If your API is complex, you might need to configure additional options to explain to Deployment Manager how to handle less obvious API behavior.



For more information, read the [API Requirements](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/api-requirements) documentation.

## Adding your API to Deployment Manager

After determining that your API matches the requirements above, [add the API as a Type Provider](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/creating-type-provider) resource. You must provide an API descriptor document and optionally, any additional API options using [advanced options](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/advanced-configuration-options). Adding an API as a type provider exposes all resources of that API to Deployment Manager and allows users to create, update, or delete those resources with Deployment Manager.

If your API has subtle API patterns that might not be easily recognizable, you will need to also provide input mappings to Deployment Manager so it can properly handle API requests. For information, read [Advanced API Options](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/advanced-configuration-options).

## Calling a type provider in configuration files

Once an API is registered with Deployment Manager, you can create API resources by calling that API resource as a type in your configuration.

For example, if you named your type provider `example-directory-api` and you want to create an API resource known as `person`, you can specify the type in your configurations like so:
    
    
    resources:
    - name: Jane
      type: my-project/example-directory-api:person
      properties:
      - name: Jane
        website: www.example.com
        ...
    

To compare, this is the same process as calling a Google API and creating an API resource:
    
    
    resource:
    - name: example-instance
      type: compute.v1.instance
      properties:
      - machineType: n1-standard-1
        ...
    

## What's next

  * Read about the [API requirements](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/api-requirements) for adding an API to Deployment Manager
  * Follow the instructions to [add an API](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/creating-type-provider).
  * Learn more about [advanced API options](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/advanced-configuration-options).
  * Learn more about [types](https://docs.cloud.google.com/deployment-manager/docs/fundamentals#types).
  * Read about [creating a configuration](https://docs.cloud.google.com/deployment-manager/docs/configuration).
  * [Create a deployment](https://docs.cloud.google.com/deployment-manager/docs/deployments).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
