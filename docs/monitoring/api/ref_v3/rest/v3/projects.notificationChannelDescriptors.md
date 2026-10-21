---
url: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors
title: REST Resource: projects.notificationChannelDescriptors \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:12.814213+00:00
---

# REST Resource: projects.notificationChannelDescriptors  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  REST Resource: projects.notificationChannelDescriptors Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: NotificationChannelDescriptor
    * JSON representation
  * Methods



## Resource: NotificationChannelDescriptor

A description of a notification channel. The descriptor includes the properties of the channel and the set of labels or fields that must be specified to configure channels of a given type.

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
`name` |  `string` The full REST resource name for this descriptor. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/notificationChannelDescriptors/[TYPE]
    

In the above, `[TYPE]` is the value of the `type` field.  
`type` |  `string` The type of notification channel, such as "email" and "sms". To view the full list of channels, see [Channel descriptors](https://cloud.google.com/monitoring/alerts/using-channels-api#ncd). Notification channel types are globally unique.  
`displayName` |  `string` A human-readable name for the notification channel type. This form of the name is suitable for a user interface.  
`description` |  `string` A human-readable description of the notification channel type. The description may include a description of the properties of the channel and pointers to external documentation.  
`labels[]` |  `object (`[LabelDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/LabelDescriptor)`)` The set of labels that must be defined to identify a particular channel of the corresponding type. Each label includes a description for how that field should be populated.  
`launchStage` |  `enum (`[LaunchStage](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/LaunchStage)`)` The product launch stage for channels of this type.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors/get)`

|  Gets a single channel descriptor.  
  
### `[list](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors/list)`

|  Lists the descriptors for supported channel types.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-23 UTC."],[],[]] 
