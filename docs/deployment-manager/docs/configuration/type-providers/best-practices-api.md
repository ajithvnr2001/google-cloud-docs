---
url: https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/best-practices-api/
title: Best Practices for Adding a Type Provider \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:46:57.931826+00:00
---

# Best Practices for Adding a Type Provider  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/best-practices-api/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment)



Send feedback 

#  Best Practices for Adding a Type Provider Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes best practices for creating a new API to add to Deployment Manager as a [Type Provider](https://docs.cloud.google.com/deployment-manager/docs/fundamentals#type_providers) or adding an existing API as a type provider.

Deployment Manager lets you add APIs as type providers to expose the API resources as types that you can call in their configuration. To make the process easier for you, use these best practices when configuring or creating an API.

## Building a new API

If you are building a new API that you intend to integrate with Deployment Manager, use these best practices.

### Use standard Create, Read, Update, and Delete (CRUD) methods and avoid custom methods

Avoid creating custom methods if possible. Stick to standard REST methods such as `GET`, `POST`, `PUT`, and `DELETE` methods. These methods are recognized by Deployment Manager and can be automatically mapped.

For Discovery APIs, you should name your API methods according to the following mapping:

REST method | Recommended API naming  
---|---  
`POST` | `create` or `insert`  
`GET` | `get`  
`PUT` | `update`  
`DELETE` | `delete`  
  
For OpenAPI specifications, you cannot name your API methods differently than the standard REST methods.

### Use predictable resource paths

For OpenAPI specifications, Deployment Manager supports two behaviors to identify a RESTful interface. The first is if all REST methods for a resource belong in the same resource path:
    
    
    /foo/{name}
      post:
      get:
      delete:
      put:
    

If you must separate the methods, use the same resource path. For example, the following is valid because it refers to the same `/foo` resource:
    
    
    /foo/
      post:
    /foo/{id}
      get:
      delete:
      put:
    

However, the following is invalid because it refers to two different resources from the view of Deployment Manager:
    
    
    /foo/
     post:
    /foo-bar/{id}:
     get:
     put:
     delete:
    

For rare cases, you might tempted to name your resource paths like so:
    
    
    foo/create
      post:
    
    foo/delete
      delete:
    

This is invalid from Deployment Manager's view because it cannot identify the RESTful interface.

### Use consistent naming across the interface

Keep input and path names the same between `POST` and `PUT` methods. This also applies for the parameter values as well. That is, keep the syntax for parameter values the same across methods.

For example, if you have a parameter named `email` for the request body of a `POST` request, don't name the same parameter `emailAddress` for the `PUT` request.
    
    
    POST
    {
        “email”: “my-email”
    }
    
    PUT
    {
        “email”: “my-email@gmail.com”
    }
    

If you must add this type of behavior, tell Deployment Manager how to handle this behavior by setting [advanced API options](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/advanced-configuration-options).

In addition, keep the request body for `POST` and `PUT` methods the same. For `GET` and `DELETE` methods, only the path is applicable as there is no request body for these methods.

## Integrating an existing API

Integrating an existing API can be a widely varied process depending on the API. As such, there is no concrete set of best practices that can be applied generically across all APIs. The following is a list of general advice that might help when considering ways to integrate an existing API.

  * Use an API wrapper for non-RESTful APIs.

If an existing API is not a RESTful API, you can create an API wrapper to expose the REST methods only.

  * If the API is almost RESTful, identify and update the API.

If your API is almost RESTful and only has a few non-REST behaviors, you could update the API to resolve these behaviors.

  * Server generated values always requires an input mapping.

If your API has server-generated values that are required by API methods, you will need to set up [input mappings](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/advanced-configuration-options#specifying_input_mappings) to get the server-generated value and map it for each request.




## What's next

  * Read about the [API requirements](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/api-requirements) for adding an API to Deployment Manager
  * Follow the instructions to [add an API](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/creating-type-provider).
  * Learn more about [advanced API options](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/advanced-configuration-options).
  * Learn more about [types](https://docs.cloud.google.com/deployment-manager/docs/fundamentals#types).
  * Read about [creating a configuration](https://docs.cloud.google.com/deployment-manager/docs/configuration).
  * [Create a deployment](https://docs.cloud.google.com/deployment-manager/docs/deployments) using your new type provider



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
