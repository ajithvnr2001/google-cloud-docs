---
url: https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/api-requirements/
title: API requirements for Integrating an API \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:12.603642+00:00
---

# API requirements for Integrating an API  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/api-requirements/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment)



Send feedback 

#  API requirements for Integrating an API Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes general requirements of an API that you want to add as a type provider to Deployment Manager. Use these guidelines to understand the traits of an API that Deployment Manager expects. If your API doesn't exactly match the specifications described here, you might be able to resolve these inconsistencies using [Advanced API Options](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/advanced-configuration-options).

## The API has a valid descriptor document

A descriptor document describes an API and it's resources. Only APIs backed by an [OpenAPI specification](https://github.com/OAI/OpenAPI-Specification) or a [Google Discovery](https://developers.google.com/discovery/v1/reference/apis) descriptor document can be integrated with Deployment Manager. For comprehensive information on how to create an OpenAPI specification, see the [OpenAPI GitHub repo](https://github.com/OAI/OpenAPI-Specification).

## API descriptor document endpoint is accessible

Deployment Manager makes an HTTP request to get the descriptor document of the API, so you should make sure to host your descriptor document somewhere that is accessible by Deployment Manager. That can be a publicly available URL or an endpoint protected by basic authentication.

## API accepts basic auth or OAuth2 if hosted on certain Google services

Deployment Manager currently supports basic authentication (username and password) and OAuth 2.0 authentication for certain APIs hosted on Google Kubernetes Engine or on Google Endpoints, you can set up authentication to use the project's service account.

For more information, read [Creating a Type Provider](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/creating-type-provider#authentication).

## Supports Create, Read, Update, Delete (CRUD) operations

The API in question must be a [RESTful](https://.wikipedia.org/wiki/Representational_state_transfer) API that supports CRUD operations. That is, there are methods that perform:

  * Create operations - Creates resources. This must be an `HTTP POST` request.
  * Read operations - Gets information about API resources. This must be an `HTTP GET` request.
  * Update operations - Updates a resource. This must be an `HTTP PUT` request
  * Delete operations - Deletes resources. This must be an `HTTP DELETE` request.



An API that only supports partial CRUD operations will still work but the behavior will be different depending on what operations are available.

Supports `GET` requests  |  Supports `CREATE` requests  |  Supports `UPDATE` requests  |  Supports `DELETE` requests  |  Special API behavior?  | Yes | Yes | Yes | Yes | None.  
---|---|---|---|---  
Yes | Yes | Yes | No | Users can abandon a resource but cannot delete it.   
Yes | Yes | No | Yes | Any changes to an existing resource would fail. Users would need to delete and recreate a resource to update it.  
Yes | Yes | No | No | Both of behaviors described above.  
Yes | No | Yes | Yes | If an API does not support create requests, users can add existing resources to the deployment by updating the deployment with the `ACQUIRE` policy.  
Yes | No | Yes | No | Users can acquire a resource or update a resource after it has been acquired but the resource cannot be deleted.  
Yes | No | No | Yes | Users can delete a resource and get a resource, or can add an existing resource to a deployment.  
Yes | No | No | No | Users can acquire an existing resource or remove it with the `ABANDON` policy.  
  
## All path and query parameters resolve successfully

All path and query parameters of the API must exist as part of the resource body or exist on all methods of the API, so that Deployment Manager can match the parameter when a user supplies it. The following conditions apply to path and query parameters.

**Every path/query parameter for a POST must be a parameter for PUT**

The following is invalid because `myParameter` exists for `POST` but not for `PUT`:
    
    
    POST  /my-api/{myParameter}/resource/{mySecondParameter}
    PUT   /my-api/resource/{mySecondParameter}  # myParameter is not present
    

**Every parameter for non-POST method needs to be present either in all the method interfaces, or as part of the resource, with special considerations if this parameter is generated by the server.**

In a best case scenario, the API might look like this, where the `name` parameter appears for all methods.
    
    
    POST   /my-api/my-resource/{name}
    PUT    /my-api/my-resource/{name}
    GET    /my-api/my-resource/{name}
    DELETE /my-api/my-resource/{name}
    

In another scenario, a field might appear as a path parameter for a method, but not as a path parameter for other methods. In this case, the field should be part of the API resource. For example:
    
    
    POST  /my-api/my-resource ← the 'id' field  is not present on the POST request
    GET   /my-api/my-resource/{id}
    
    schema for my-resource
    type: object
    properties:
    # id is part of the resource so Deployment Manager will use this value for
    # POST requests after creation
      id:
        type: string
    

In this example, the assumption is that `id` is a server-generated value that is present on the resource, but not present when making a `POST` request. If the `id` property was required to make a request to an existing resource, but the property was not on resource or available in the path, this causes friction in porting the API to Deployment Manager.

## Subtle API behavior requires additional configuration

There are certain API behaviors that will require additional API configuration to integrate the API with Deployment Manager. These behaviors include:

  * **Server generated values** : Some API resources have server-generated properties that change after each request or when a certain event happens in the API. You can use advanced API options to tell Deployment Manager to get this new value each time a request is made.

For example, an API might require the latest fingerprint property of a resource before it allows an update request. Use [Advanced API Options](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/advanced-configuration-options) to tell Deployment Manager to get this value each time your user makes a request to update a deployment with this.

  * **Manipulating user input** : For example, if your API requires the value of a field must always be prefixed with a project ID, you can use input mappings to automatically add that information, instead of forcing your users to to add it manually.

  * **Field values that change with each method** : For methods that reuse the same field but with different values, you can use the API options to express to Deployment Manager when to use which value.




For more information, read about [Setting Advanced API Options](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/advanced-configuration-options).

## What's next

  * Learn how to [create a type provider](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/creating-type-provider).
  * Learn how to [use a type provider](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/calling-type-provider).
  * Learn more about [Advanced API Options](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/advanced-configuration-options).
  * Read about [creating a configuration](https://docs.cloud.google.com/deployment-manager/docs/configuration).
  * [Create a deployment](https://docs.cloud.google.com/deployment-manager/docs/deployments).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
