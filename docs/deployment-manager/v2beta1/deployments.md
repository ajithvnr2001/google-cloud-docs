---
url: https://docs.cloud.google.com/deployment-manager/v2beta1/deployments/
title: Deployments \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:32:38.521526+00:00
---

# Deployments  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/v2beta1/deployments/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Reference ](https://docs.cloud.google.com/deployment-manager/docs/apis)



Send feedback 

#  Deployments Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** This is a **deprecated** version of the Deployment Manager API. Please use the [latest API version](https://docs.cloud.google.com/deployment-manager/latest) instead.

A deployment is a collection of resources that are deployed and managed together, using a configuration file.

For a list of methods for this resource, see the end of this page.

## Resource representations
    
    
    {
      "id": unsigned long,
      "name": string,
      "description": string,
      "manifest": string,
      "targetConfig": string
    }

Property name | Value | Description | Notes  
---|---|---|---  
`description` | `string` | An optional user-provided description of the deployment. |   
`id` | `unsigned long` | [Output Only] Unique identifier for the resource; defined by the server. |   
`manifest` | `string` | [Output Only] URL of the manifest representing the full configuration of this deployment. |   
`name` | `string` | The name of the deployment, which must be unique within the project. |   
`targetConfig` | `string` | [Input Only] The YAML configuration to use in processing this deployment.   
  
When you create a deployment, the server creates a new manifest with the given YAML configuration and sets the `manifest` property to the URL of the manifest resource. |   
  
## Methods

[delete](https://docs.cloud.google.com/deployment-manager/v2beta1/deployments/delete)
    Deletes a deployment and all associated resources.
[get](https://docs.cloud.google.com/deployment-manager/v2beta1/deployments/get)
    Gets information about a specific deployment.
[insert](https://docs.cloud.google.com/deployment-manager/v2beta1/deployments/insert)
    Creates a deployment and all of the resources described by the deployment manifest.
[list](https://docs.cloud.google.com/deployment-manager/v2beta1/deployments/list)
    Lists all deployments for a given project.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-04-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-04-30 UTC."],[],[]] 
