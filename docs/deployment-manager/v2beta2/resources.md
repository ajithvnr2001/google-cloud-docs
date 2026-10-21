---
url: https://docs.cloud.google.com/deployment-manager/v2beta2/resources/
title: Resources \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:32:38.234557+00:00
---

# Resources  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/v2beta2/resources/

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

A resource represents a single Google Cloud Platform entity, such as a Compute Engine instance, a BigQuery dataset, and so on. You define a list of resources in your configuration file, which is then deployed using the Deployment Manager service.

For a list of methods for this resource, see the end of this page.

## Resource representations

  
  

    
    
    {
      "id": unsigned long,
      "insertTime": string,
      "updateTime": string,
      "name": string,
      "type": string,
      "manifest": string,
      "url": string,
      "properties": string,
      "finalProperties": string,
      "update": {
        "manifest": string,
        "errors": [
          string
        ],
        "state": string,
        "intent": string,
        "properties": string,
        "finalProperties": string
      }
    }

Property name | Value | Description | Notes  
---|---|---|---  
`finalProperties` | `string` | [Output Only] The evaluated properties of the resource with references expanded. Returned as serialized YAML. |   
`id` | `unsigned long` | [Output Only] Unique identifier for the resource; defined by the server. |   
`insertTime` | `string` | [Output Only] Timestamp when the resource was created or acquired, in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format . |   
`manifest` | `string` | [Output Only] URL of the manifest representing the current configuration of this resource. |   
`name` | `string` | [Output Only] The name of the resource as it appears in the YAML config. |   
`properties` | `string` | [Output Only] The current properties of the resource before any references have been filled in. Returned as serialized YAML. |   
`type` | `string` | [Output Only] The type of the resource, for example `compute.v1.instance`, or `replicaPools.v1beta2.instanceGroupManager`. |   
`update` | `nested object` | [Output Only] If Deployment Manager is currently updating or previewing an update to this resource, the updated configuration appears here. |   
`update.errors[]` | `list` | [Output Only] List of all errors encountered while trying to enact `update.intent`. |   
`update.finalProperties` | `string` | [Output Only] The expanded properties of the resource with reference values expanded. Returned as serialized YAML. |   
`update.intent` | `string` | [Output Only] The intent of the resource: `PREVIEW`, `UPDATE`, or `CANCEL`. |   
`update.manifest` | `string` | [Output Only] URL of the manifest representing the update configuration of this resource. |   
`update.properties` | `string` | [Output Only] The set of updated properties for this resource, before references are expanded. Returned as serialized YAML. |   
`update.state` | `string` | [Output Only] The state of the resource. |   
`updateTime` | `string` | [Output Only] Timestamp when the resource was updated, in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format . |   
`url` | `string` | [Output Only] The URL of the actual resource. |   
  
## Methods

[get](https://docs.cloud.google.com/deployment-manager/v2beta2/resources/get)
    Gets information about a single resource.
[list](https://docs.cloud.google.com/deployment-manager/v2beta2/resources/list)
    Lists all resources in a given deployment.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-04-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-04-30 UTC."],[],[]] 
