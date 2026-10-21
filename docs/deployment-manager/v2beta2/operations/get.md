---
url: https://docs.cloud.google.com/deployment-manager/v2beta2/operations/get/
title: Operations: get \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:32:38.079649+00:00
---

# Operations: get  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/v2beta2/operations/get/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Reference ](https://docs.cloud.google.com/deployment-manager/docs/apis)



Send feedback 

#  Operations: get Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** This is a **deprecated** version of the Deployment Manager API. Please use the [latest API version](https://docs.cloud.google.com/deployment-manager/latest) instead.

**Requiresauthorization**

Gets information about a specific operation. Try it now. 

## Request

### HTTP request
    
    
    GET https://www.googleapis.com/deploymentmanager/v2beta2/projects/project/global/operations/operation

### Parameters

Parameter name | Value | Description  
---|---|---  
**Path parameters**  
`operation` | `string` |  The name of the operation for this request.   
`project` | `string` |  The project ID for this request.   
  
### Authorization

This request requires authorization with at least one of the following scopes ([read more about authentication and authorization](https://docs.cloud.google.com/deployment-manager/docs/reference/latest/authorization)).

Scope  
---  
`https://www.googleapis.com/auth/ndev.cloudman.readonly`  
`https://www.googleapis.com/auth/cloud-platform`  
`https://www.googleapis.com/auth/ndev.cloudman`  
`https://www.googleapis.com/auth/cloud-platform.read-only`  
  
### Request body

Do not supply a request body with this method.

## Response

If successful, this method returns an [Operations resource](https://docs.cloud.google.com/deployment-manager/v2beta2/operations#resource) in the response body.

## Try it!

Use the APIs Explorer below to call this method on live data and see the response. Alternatively, try the [standalone Explorer](https://developers.google.com/apis-explorer/#p/deploymentmanager/v2beta2/deploymentmanager.operations.get). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-04-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-04-30 UTC."],[],[]] 
