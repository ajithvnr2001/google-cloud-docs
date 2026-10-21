---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ModelMonitoringAlertConfig/
title: ModelMonitoringAlertConfig \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:26:27.086326+00:00
---

# ModelMonitoringAlertConfig  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ModelMonitoringAlertConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  ModelMonitoringAlertConfig Stay organized with collections  Save and categorize content based on your preferences. 

The alert config for model monitoring.

Fields  
  
`enableLogging` `boolean` Dump the anomalies to Cloud Logging. The anomalies will be put to json payload encoded from proto `[ModelMonitoringStatsAnomalies](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.batchPredictionJobs#ModelMonitoringStatsAnomalies)`. This can be further synced to Pub/Sub or any other services supported by Cloud Logging. | `notificationChannels[]` `string` Resource names of the NotificationChannels to send alert. Must be of the format `projects/<project_id_or_number>/notificationChannels/<channelId>` | `alert` `Union type`  
  
The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`emailAlertConfig` `object (`[EmailAlertConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ModelMonitoringAlertConfig#EmailAlertConfig)`)` email alert config. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
      "enableLogging": boolean,
      "notificationChannels": [
        string
      ],
    
      // alert
      "emailAlertConfig": {
        object ([EmailAlertConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ModelMonitoringAlertConfig#EmailAlertConfig))
      }
      // Union type
    }  
  
## EmailAlertConfig

The config for email alert.

Fields  
  
`userEmails[]` `string` The email addresses to send the alert. | JSON representation  
---  
      
    
    {
      "userEmails": [
        string
      ]
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
