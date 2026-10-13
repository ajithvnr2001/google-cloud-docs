---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ModelMonitoringNotificationSpec/
title: ModelMonitoringNotificationSpec \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:48:31.282974+00:00
---

# ModelMonitoringNotificationSpec  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ModelMonitoringNotificationSpec/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  ModelMonitoringNotificationSpec Stay organized with collections  Save and categorize content based on your preferences. 

Notification spec(email, notification channel) for model monitoring statistics/alerts.

Fields  
  
`emailConfig` `object (`[EmailConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ModelMonitoringNotificationSpec#EmailConfig)`)` email alert config. | `enableCloudLogging` `boolean` Dump the anomalies to Cloud Logging. The anomalies will be put to json payload encoded from proto [google.cloud.aiplatform.logging.ModelMonitoringAnomaliesLogEntry][]. This can be further sinked to Pub/Sub or any other services supported by Cloud Logging. | `notificationChannelConfigs[]` `object (`[NotificationChannelConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ModelMonitoringNotificationSpec#NotificationChannelConfig)`)` Notification channel config. | JSON representation  
---  
      
    
    {
      "emailConfig": {
        object ([EmailConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ModelMonitoringNotificationSpec#EmailConfig))
      },
      "enableCloudLogging": boolean,
      "notificationChannelConfigs": [
        {
          object ([NotificationChannelConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ModelMonitoringNotificationSpec#NotificationChannelConfig))
        }
      ]
    }  
  
## EmailConfig

The config for email alerts.

Fields  
  
`userEmails[]` `string` The email addresses to send the alerts. | JSON representation  
---  
      
    
    {
      "userEmails": [
        string
      ]
    }  
  
## NotificationChannelConfig

Google Cloud Notification channel config.

Fields  
  
`notificationChannel` `string` Resource names of the NotificationChannels. Must be of the format `projects/<project_id_or_number>/notificationChannels/<channelId>` | JSON representation  
---  
      
    
    {
      "notificationChannel": string
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-06 UTC."],[],[]] 
