---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/SendMessageConfiguration/
title: SendMessageConfiguration \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:00:35.026932+00:00
---

# SendMessageConfiguration  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/SendMessageConfiguration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  SendMessageConfiguration Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * TaskPushNotificationConfig
    * JSON representation
  * AuthenticationInfo
    * JSON representation



Configuration of a send message request.

JSON representation  
---  
      
    
    {
      "acceptedOutputModes": [
        string
      ],
      "taskPushNotificationConfig": {
        object ([TaskPushNotificationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/SendMessageConfiguration#TaskPushNotificationConfig))
      },
      "returnImmediately": boolean,
      "historyLength": integer
    }  
  
Fields  
---  
`acceptedOutputModes[]` |  `string` A list of media types the client is prepared to accept for response parts. Agents SHOULD use this to tailor their output.  
`taskPushNotificationConfig` |  `object (`[TaskPushNotificationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/SendMessageConfiguration#TaskPushNotificationConfig)`)` Configuration for the agent to send push notifications for task updates. Task id should be empty when sending this configuration in a `message.send` request.  
`returnImmediately` |  `boolean` If `true`, the operation returns immediately after creating the task, even if processing is still in progress. If `false` (default), the operation MUST wait until the task reaches a terminal (`COMPLETED`, `FAILED`, `CANCELED`, `REJECTED`) or interrupted (`INPUT_REQUIRED`, `AUTH_REQUIRED`) state before returning.  
`historyLength` |  `integer` The maximum number of most recent messages from the task's history to retrieve in the response. An unset value means the client does not impose any limit. A value of zero is a request to not include any messages. The server MUST NOT return more messages than the provided value, but MAY apply a lower limit.  
  
## TaskPushNotificationConfig

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
        object ([AuthenticationInfo](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/SendMessageConfiguration#AuthenticationInfo))
      }
    }  
  
Fields  
---  
`tenant` |  `string` Optional. Opaque routing identifier. Must match the `tenant` value from the selected `AgentInterface` in the Agent Card when that field is set.  
`id` |  `string` The push notification configuration details. A unique identifier (e.g. UUID) for this push notification configuration.  
`taskId` |  `string` The ID of the task this configuration is associated with.  
`url` |  `string` Required. The URL where the notification should be sent.  
`token` |  `string` A token unique for this task or session.  
`authentication` |  `object (`[AuthenticationInfo](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/SendMessageConfiguration#AuthenticationInfo)`)` Authentication information required to send the notification.  
  
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
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-23 UTC."],[],[]] 
