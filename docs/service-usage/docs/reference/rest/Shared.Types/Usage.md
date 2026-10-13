---
url: https://docs.cloud.google.com/service-usage/docs/reference/rest/Shared.Types/Usage/
title: Service Usage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:48:00.179914+00:00
---

# Service Usage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-usage/docs/reference/rest/Shared.Types/Usage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Service Usage ](https://docs.cloud.google.com/service-usage)
  * [ Reference ](https://docs.cloud.google.com/service-usage/docs/apis)



Send feedback 

#  Usage Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * UsageRule
    * JSON representation



Configuration controlling usage of a service.

JSON representation  
---  
      
    
    {
      "requirements": [
        string
      ],
      "rules": [
        {
          object ([UsageRule](https://docs.cloud.google.com/service-usage/docs/reference/rest/Shared.Types/Usage#UsageRule))
        }
      ],
      "producerNotificationChannel": string
    }  
  
Fields  
---  
`requirements[]` |  `string` Requirements that must be satisfied before a consumer project can use the service. Each requirement is of the form <service.name>/; for example 'serviceusage.googleapis.com/billing-enabled'.For Google APIs, a Terms of Service requirement must be included here. Google Cloud APIs must include "serviceusage.googleapis.com/tos/cloud". Other Google APIs should include "serviceusage.googleapis.com/tos/universal". Additional ToS can be included based on the business needs.  
`rules[]` |  `object (`[UsageRule](https://docs.cloud.google.com/service-usage/docs/reference/rest/Shared.Types/Usage#UsageRule)`)` A list of usage rules that apply to individual API methods.**NOTE:** All service configuration rules follow "last one wins" order.  
`producerNotificationChannel` |  `string` The full resource name of a channel used for sending notifications to the service producer.Google Service Management currently only supports [Google Cloud Pub/Sub](https://cloud.google.com/pubsub) as a notification channel. To use Google Cloud Pub/Sub as the channel, this must be the name of a Cloud Pub/Sub topic that uses the Cloud Pub/Sub topic name format documented in <https://cloud.google.com/pubsub/docs/overview>.  
  
## UsageRule

Usage configuration rules for the service.

JSON representation  
---  
      
    
    {
      "selector": string,
      "allowUnregisteredCalls": boolean,
      "skipServiceControl": boolean
    }  
  
Fields  
---  
`selector` |  `string` Selects the methods to which this rule applies. Use '*' to indicate all methods in all APIs.Refer to `[selector](https://docs.cloud.google.com/service-usage/docs/reference/rest/Shared.Types/Documentation#DocumentationRule.FIELDS.selector)` for syntax details.  
`allowUnregisteredCalls` |  `boolean` Use this rule to configure unregistered calls for the service. Unregistered calls are calls that do not contain consumer project identity. (Example: calls that do not contain an API key).WARNING: By default, API methods do not allow unregistered calls, and each method call must be identified by a consumer project identity.  
`skipServiceControl` |  `boolean` If true, the selected method should skip service control and the control plane features, such as quota and billing, will not be available. This flag is used by Google Cloud Endpoints to bypass checks for internal methods, such as service health check methods.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-11 UTC."],[],[]] 
