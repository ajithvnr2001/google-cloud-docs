---
url: https://docs.cloud.google.com/deployment-manager/v2beta1/resources/
title: Resources \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:26:40.952147+00:00
---

# Resources  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/v2beta1/resources/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Reference ](https://docs.cloud.google.com/deployment-manager/docs/apis)



Send feedback 

#  Resources Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** This is a **deprecated** version of the Deployment Manager API. Please use the [latest API version](https://docs.cloud.google.com/deployment-manager/latest) instead.

A resource represents a single Google Cloud Platform resource. For example, a Compute Engine instance is a single resource, a BigQuery dataset is a single resource, and so on. You can define a list of resources in your configuration file, which is then deployed using the Deployment Manage service.

For a list of methods for this resource, see the end of this page.

## Resource representations
    
    
    {
      "id": unsigned long,
      "name": string,
      "type": string,
      "manifest": string,
      "url": string,
      "errors": [
        string
      ],
      "state": string,
      "intent": string
    }

Property name | Value | Description | Notes  
---|---|---|---  
`errors[]` | `list` | [Output Only] A list of any errors that occurred during deployment. |   
`id` | `unsigned long` | [Output Only] Unique identifier for the resource; defined by the server. |   
`intent` | `string` | [Output Only] The intended state of the resource. |   
`manifest` | `string` | [Output Only] URL of the manifest representing the current configuration of this resource. |   
`name` | `string` | [Output Only] The name of the resource as it appears in the YAML config. |   
`state` | `string` | [Output Only] The state of the resource. |   
`type` | `string` | [Output Only] The [type](https://docs.cloud.google.com/deployment-manager/v2beta1/types#resource) of the resource, for example: `````compute.v1.instance`, or `````replicaPools.v1beta2.instanceGroupManager.` |   
`url` | `string` | [Output Only] The URL of the actual resource. |   
  
## Methods

[get](https://docs.cloud.google.com/deployment-manager/v2beta1/resources/get)
    Gets information about a single resource.
[list](https://docs.cloud.google.com/deployment-manager/v2beta1/resources/list)
    Lists all resources in a given deployment.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-04-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-04-30 UTC."],[],[]] 
