---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/tasks.pushNotificationConfigs
title: REST Resource: tasks.pushNotificationConfigs \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:23:45.907108+00:00
---

# REST Resource: tasks.pushNotificationConfigs  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/tasks.pushNotificationConfigs

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  REST Resource: tasks.pushNotificationConfigs Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: TaskPushNotificationConfig
    * JSON representation
  * AuthenticationInfo
    * JSON representation
  * Methods



## Resource: TaskPushNotificationConfig

A container associating a push notification configuration with a specific task.

JSON representation  
---  
      
    
    {
      "tenant": string,
      "id": string,
      "taskId": string,
      "url": string,
      "token": string,
      "authentication": {
        object ([AuthenticationInfo](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/tasks.pushNotificationConfigs#AuthenticationInfo))
      }
    }  
  
Fields  
---  
`tenant` |  `string` Optional. Opaque routing identifier. Must match the `tenant` value from the selected `AgentInterface` in the Agent Card when that field is set.  
`id` |  `string` The push notification configuration details. A unique identifier (e.g. UUID) for this push notification configuration.  
`taskId` |  `string` The ID of the task this configuration is associated with.  
`url` |  `string` Required. The URL where the notification should be sent.  
`token` |  `string` A token unique for this task or session.  
`authentication` |  `object (`[AuthenticationInfo](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/tasks.pushNotificationConfigs#AuthenticationInfo)`)` Authentication information required to send the notification.  
  
## AuthenticationInfo

Defines authentication details, used for push notifications.

JSON representation  
---  
      
    
    {
      "scheme": string,
      "credentials": string
    }  
  
Fields  
---  
`scheme` |  `string` Required. HTTP Authentication Scheme from the [IANA registry](https://www.iana.org/assignments/http-authschemes/). Examples: `Bearer`, `Basic`, `Digest`. Scheme names are case-insensitive per [RFC 9110 Section 11.1](https://www.rfc-editor.org/rfc/rfc9110#section-11.1).  
`credentials` |  `string` Push Notification credentials. Format depends on the scheme (e.g., token for Bearer).  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/tasks.pushNotificationConfigs/create)`

|  Creates a push notification config for a task.  
  
### `[delete](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/tasks.pushNotificationConfigs/delete)`

|  Deletes a push notification config for a task.  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/tasks.pushNotificationConfigs/get)`

|  Gets a push notification config for a task.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/tasks.pushNotificationConfigs/list)`

|  Get a list of push notifications configured for a task.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-23 UTC."],[],[]] 
