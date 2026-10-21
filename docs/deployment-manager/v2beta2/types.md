---
url: https://docs.cloud.google.com/deployment-manager/v2beta2/types/
title: Types \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:52:58.266159+00:00
---

# Types  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/v2beta2/types/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Reference ](https://docs.cloud.google.com/deployment-manager/docs/apis)



Send feedback 

#  Types Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** This is a **deprecated** version of the Deployment Manager API. Please use the [latest API version](https://docs.cloud.google.com/deployment-manager/latest) instead.

The Types resource lists all valid Google Cloud Platform types that can be deployed by Deployment Manager. For example, `compute.v1.instance` is a type.

For a list of methods for this resource, see the end of this page.

## Resource representations

A resource type supported by Deployment Manager.   
  

    
    
    {
      "id": unsigned long,
      "selfLink": string,
      "insertTime": string,
      "name": string
    }

Property name | Value | Description | Notes  
---|---|---|---  
`id` | `unsigned long` | [Output Only] Unique identifier for the resource; defined by the server. |   
`insertTime` | `string` | [Output Only] Timestamp when the type was created, in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format. |   
`name` | `string` | Name of the type. |   
`selfLink` | `string` | [Output Only] Self link for the type. |   
  
## Methods

[list](https://docs.cloud.google.com/deployment-manager/v2beta2/types/list)
    Lists all resource types for Deployment Manager.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-04-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-04-30 UTC."],[],[]] 
