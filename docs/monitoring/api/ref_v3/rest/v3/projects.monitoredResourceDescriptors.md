---
url: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.monitoredResourceDescriptors
title: REST Resource: projects.monitoredResourceDescriptors \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:12.620843+00:00
---

# REST Resource: projects.monitoredResourceDescriptors  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.monitoredResourceDescriptors

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  REST Resource: projects.monitoredResourceDescriptors Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: MonitoredResourceDescriptor
    * JSON representation
  * Methods



## Resource: MonitoredResourceDescriptor

An object that describes the schema of a `[MonitoredResource](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/Shared.Types/MonitoredResource)` object using a type name and a set of labels. For example, the monitored resource descriptor for Google Compute Engine VM instances has a type of `"gce_instance"` and specifies the use of the labels `"instance_id"` and `"zone"` to identify particular VM instances.

Different APIs can support different monitored resource types. APIs generally provide a `list` method that returns the monitored resource descriptors used by the API.

JSON representation  
---  
      
    
    {
      "name": string,
      "type": string,
      "displayName": string,
      "description": string,
      "labels": [
        {
          object ([LabelDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/LabelDescriptor))
        }
      ],
      "launchStage": enum ([LaunchStage](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/LaunchStage))
    }  
  
Fields  
---  
`name` |  `string` Optional. The resource name of the monitored resource descriptor: `"projects/{projectId}/monitoredResourceDescriptors/{type}"` where {type} is the value of the `type` field in this object and {projectId} is a project ID that provides API-specific context for accessing the type. APIs that do not use project information can use the resource name format `"monitoredResourceDescriptors/{type}"`.  
`type` |  `string` Required. The monitored resource type. For example, the type `"cloudsql_database"` represents databases in Google Cloud SQL. For a list of types, see [Monitored resource types](https://cloud.google.com/monitoring/api/resources) and [Logging resource types](https://cloud.google.com/logging/docs/api/v2/resource-list).  
`displayName` |  `string` Optional. A concise name for the monitored resource type that might be displayed in user interfaces. It should be a Title Cased Noun Phrase, without any article or other determiners. For example, `"Google Cloud SQL Database"`.  
`description` |  `string` Optional. A detailed description of the monitored resource type that might be used in documentation.  
`labels[]` |  `object (`[LabelDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/LabelDescriptor)`)` Required. A set of labels used to describe instances of this monitored resource type. For example, an individual Google Cloud SQL database is identified by values for the labels `"database_id"` and `"zone"`.  
`launchStage` |  `enum (`[LaunchStage](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/LaunchStage)`)` Optional. The launch stage of the monitored resource definition.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.monitoredResourceDescriptors/get)`

|  Gets a single monitored resource descriptor.  
  
### `[list](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.monitoredResourceDescriptors/list)`

|  Lists monitored resource descriptors that match a filter.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-23 UTC."],[],[]] 
