---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.errorNotificationConfigs
title: REST Resource: projects.locations.instances.errorNotificationConfigs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:43:36.825945+00:00
---

# REST Resource: projects.locations.instances.errorNotificationConfigs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.errorNotificationConfigs

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  REST Resource: projects.locations.instances.errorNotificationConfigs Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ErrorNotificationConfig
    * JSON representation
  * IngestionCountZeroNotifications
    * JSON representation
  * NotificationConditionIngestionCountZero
    * JSON representation
  * IngestionSizeThresholdNotifications
    * JSON representation
  * NotificationConditionIngestionSizeThreshold
    * JSON representation
  * ComparisonType
  * NormalizationDelayThresholdNotifications
    * JSON representation
  * NotificationConditionNormalizationDelayThreshold
    * JSON representation
  * Methods



## Resource: ErrorNotificationConfig

ErrorNotificationConfig provides ability for customers to configure and receive self serve notifications. An ErrorNotificationConfig will contain a single notification type eg. IngestionCountZeroNotifications. An notification type can have multiple notification conditions to be set for the error notification. Each NotificationCondition will have its own params such as filters (Eg: CollectorID + logType combo). Please refer below link for more <https://cloud.google.com/chronicle/docs/reference/ingestion-metrics-schema> CollectorID can also come from forwarders configurations as well. Please refer link for more details: <https://cloud.google.com/chronicle/docs/install/forwarder-linux#sample_configuration>

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "enabled": boolean,
      "notificationChannels": [
        string
      ],
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "ingestionCountZeroNotifications": {
        object ([IngestionCountZeroNotifications](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.errorNotificationConfigs#IngestionCountZeroNotifications))
      },
      "ingestionSizeThresholdNotifications": {
        object ([IngestionSizeThresholdNotifications](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.errorNotificationConfigs#IngestionSizeThresholdNotifications))
      },
      "normalizationDelayThresholdNotifications": {
        object ([NormalizationDelayThresholdNotifications](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.errorNotificationConfigs#NormalizationDelayThresholdNotifications))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`name` |  `string` Required if the error notification config exists. The resource name for this error notification config. The format is: projects/{project}/locations/{location}/instances/{instance}/errorNotificationConfigs/{ERROR_NOTIFICATION_CONFIG_ID}  
`displayName` |  `string` A short name used to identify the error notification config.  
`enabled` |  `boolean` Used to enable/disable error notification config  
`notificationChannels[]` |  `string` Identifies the notification channels to which notifications should be sent when incidents are opened or closed or when new violations occur. Format: projects/{PROJECT_ID}/notificationChannels/{CHANNEL_ID} More at: <https://cloud.google.com/monitoring/support/notification-options>  
Notification type for the error notification config. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`ingestionCountZeroNotifications` |  `object (`[IngestionCountZeroNotifications](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.errorNotificationConfigs#IngestionCountZeroNotifications)`)` Notifications set for ingestion outages caused by metrics absence.  
`ingestionSizeThresholdNotifications` |  `object (`[IngestionSizeThresholdNotifications](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.errorNotificationConfigs#IngestionSizeThresholdNotifications)`)` Notifications set for ingestion outages caused by metrics not meeting threshold.  
`normalizationDelayThresholdNotifications` |  `object (`[NormalizationDelayThresholdNotifications](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.errorNotificationConfigs#NormalizationDelayThresholdNotifications)`)` Notifications set for normalization delays using threshold type trigger.  
End of mutually exclusive fields.  
  
## IngestionCountZeroNotifications

Notifications set for ingestion outages caused by metrics absence.

JSON representation  
---  
      
    
    {
      "notificationConditions": [
        {
          object ([NotificationConditionIngestionCountZero](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.errorNotificationConfigs#NotificationConditionIngestionCountZero))
        }
      ]
    }  
  
Fields  
---  
`notificationConditions[]` |  `object (`[NotificationConditionIngestionCountZero](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.errorNotificationConfigs#NotificationConditionIngestionCountZero)`)` Notifications conditions present in the ErrorNotificationConfig.  
  
## NotificationConditionIngestionCountZero

Describes parameters for the notification condition.

JSON representation  
---  
      
    
    {
      "collectorId": string,
      "logType": string,
      "missingDuration": string
    }  
  
Fields  
---  
`collectorId` |  `string` CollectorID for which the error notification is set.  
`logType` |  `string` Log type for which the error notification is set.  
`missingDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Number of seconds with no data ingested. Currently, only values that are a multiple of a minute e.g., 0, 60, 120, or 300 seconds are supported.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
## IngestionSizeThresholdNotifications

Notifications set for ingestion outages caused by metrics not meeting threshold.

JSON representation  
---  
      
    
    {
      "notificationConditions": [
        {
          object ([NotificationConditionIngestionSizeThreshold](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.errorNotificationConfigs#NotificationConditionIngestionSizeThreshold))
        }
      ]
    }  
  
Fields  
---  
`notificationConditions[]` |  `object (`[NotificationConditionIngestionSizeThreshold](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.errorNotificationConfigs#NotificationConditionIngestionSizeThreshold)`)` Notifications conditions present in the ErrorNotificationConfig.  
  
## NotificationConditionIngestionSizeThreshold

Describes parameters for the notification condition.

JSON representation  
---  
      
    
    {
      "collectorId": string,
      "logType": string,
      "dataSize": number,
      "monitoredDuration": string,
      "comparisonType": enum ([ComparisonType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.errorNotificationConfigs#ComparisonType))
    }  
  
Fields  
---  
`collectorId` |  `string` CollectorID for which the error notification is set.  
`logType` |  `string` log type for which the error notification is set.  
`dataSize` |  `number` Amount of `dataSize` bytes in the last `monitoredDuration` seconds. The comparison is applied on the time series, with the time series on the left-hand side and the `dataSize` on the right-hand side.  
`monitoredDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Duration of the monitored window as explained above. Currently, only values that are a multiple of a minute e.g., 0, 60, 120, 300 seconds etc. are supported.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`comparisonType` |  `enum (`[ComparisonType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.errorNotificationConfigs#ComparisonType)`)` Comparison type as explained above. Only `COMPARISON_LT` and `COMPARISON_GT` are supported currently.  
  
## ComparisonType

Specifies an ordering relationship on two arguments, called `left` and `right`.

Enums  
---  
`COMPARISON_UNSPECIFIED` | No ordering relationship is specified.  
`COMPARISON_GT` | True if the left argument is greater than the right argument.  
`COMPARISON_GE` | True if the left argument is greater than or equal to the right argument.  
`COMPARISON_LT` | True if the left argument is less than the right argument.  
`COMPARISON_LE` | True if the left argument is less than or equal to the right argument.  
`COMPARISON_EQ` | True if the left argument is equal to the right argument.  
`COMPARISON_NE` | True if the left argument is not equal to the right argument.  
  
## NormalizationDelayThresholdNotifications

Notifications set for normalization delays using threshold type trigger.

JSON representation  
---  
      
    
    {
      "notificationConditions": [
        {
          object ([NotificationConditionNormalizationDelayThreshold](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.errorNotificationConfigs#NotificationConditionNormalizationDelayThreshold))
        }
      ]
    }  
  
Fields  
---  
`notificationConditions[]` |  `object (`[NotificationConditionNormalizationDelayThreshold](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.errorNotificationConfigs#NotificationConditionNormalizationDelayThreshold)`)` Notifications conditions present in the ErrorNotificationConfig.  
  
## NotificationConditionNormalizationDelayThreshold

Describes parameters for the notification condition.

JSON representation  
---  
      
    
    {
      "logType": string,
      "threshold": number
    }  
  
Fields  
---  
`logType` |  `string` log type for which the error notification is set.  
`threshold` |  `number` When the % of normalized events for a log type falls below a certain threshold.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.errorNotificationConfigs/create)`

|  Creates a new error notification config for the customer  
  
### `[delete](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.errorNotificationConfigs/delete)`

|  Deletes an error notification config.  
  
### `[get](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.errorNotificationConfigs/get)`

|  Gets a single error notification config.  
  
### `[list](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.errorNotificationConfigs/list)`

|  Lists error notification configurations for the customer.  
  
### `[patch](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.errorNotificationConfigs/patch)`

|  Updates an error notification config.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
