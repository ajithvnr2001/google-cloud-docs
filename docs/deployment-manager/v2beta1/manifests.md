---
url: https://docs.cloud.google.com/deployment-manager/v2beta1/manifests/
title: Manifests \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:59:03.489773+00:00
---

# Manifests  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/v2beta1/manifests/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Reference ](https://docs.cloud.google.com/deployment-manager/docs/apis)



Send feedback 

#  Manifests Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** This is a **deprecated** version of the Deployment Manager API. Please use the [latest API version](https://docs.cloud.google.com/deployment-manager/latest) instead.

A manifest is a read-only fully-expanded list of all resources for a deployment. For each deployment, there is a single manifest file.

For a list of methods for this resource, see the end of this page.

## Resource representations
    
    
    {
      "id": unsigned long,
      "selfLink": string,
      "name": string,
      "config": string,
      "evaluatedConfig": string
    }

Property name | Value | Description | Notes  
---|---|---|---  
`config` | `string` | [Output Only] The YAML configuration for this manifest. |   
`evaluatedConfig` | `string` | [Output Only] The fully-expanded configuration file, including any templates and references. |   
`id` | `unsigned long` | [Output Only] Unique identifier for the resource; defined by the server. |   
`name` | `string` | [Output Only] The name of the manifest. |   
`selfLink` | `string` | [Output Only] Self link for the manifest. |   
  
## Methods

[get](https://docs.cloud.google.com/deployment-manager/v2beta1/manifests/get)
    Gets information about a specific manifest.
[list](https://docs.cloud.google.com/deployment-manager/v2beta1/manifests/list)
    Lists all manifests for a given deployment.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-04-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-04-30 UTC."],[],[]] 
