---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.modelMonitors/searchModelMonitoringAlerts/
title: Method: modelMonitors.searchModelMonitoringAlerts \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:58:27.998719+00:00
---

# Method: modelMonitors.searchModelMonitoringAlerts  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.modelMonitors/searchModelMonitoringAlerts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: modelMonitors.searchModelMonitoringAlerts Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.modelMonitors.searchModelMonitoringAlerts

Returns the Model Monitoring alerts.

### Endpoint

post  `https://{service-endpoint}/v1beta1/{modelMonitor}:searchModelMonitoringAlerts`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`modelMonitor` `string` Required. ModelMonitor resource name. Format: `projects/{project}/locations/{location}/modelMonitors/{modelMonitor}`

### Request body

The request body contains data with the following structure: | Fields  
  
`modelMonitoringJob` `string` If non-empty, returns the alerts of this model monitoring job. | `alertTimeInterval` `object (`[Interval](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/Interval)`)` If non-empty, returns the alerts in this time interval. | `statsName` `string` If non-empty, returns the alerts of this statsName. | `objectiveType` `string` If non-empty, returns the alerts of this objective type. Supported monitoring objectives: `raw-feature-drift` `prediction-output-drift` `feature-attribution` | `pageSize` `integer` The standard list page size. | `pageToken` `string` A page token received from a previous `[ModelMonitoringService.SearchModelMonitoringAlerts](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.modelMonitors/searchModelMonitoringAlerts#google.cloud.aiplatform.v1beta1.ModelMonitoringService.SearchModelMonitoringAlerts)` call.

### Response body

Response message for `[ModelMonitoringService.SearchModelMonitoringAlerts](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.modelMonitors/searchModelMonitoringAlerts#google.cloud.aiplatform.v1beta1.ModelMonitoringService.SearchModelMonitoringAlerts)`. If successful, the response body contains data with the following structure: | Fields  
  
`modelMonitoringAlerts[]` `object (`[ModelMonitoringAlert](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.modelMonitors/searchModelMonitoringAlerts#ModelMonitoringAlert)`)` Alerts retrieved for the requested objectives. Sorted by alert time descendingly. | `totalNumberAlerts` `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The total number of alerts retrieved by the requested objectives. | `nextPageToken` `string` The page token that can be used by the next `[ModelMonitoringService.SearchModelMonitoringAlerts](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.modelMonitors/searchModelMonitoringAlerts#google.cloud.aiplatform.v1beta1.ModelMonitoringService.SearchModelMonitoringAlerts)` call. | JSON representation  
---  
      
    
    {
      "modelMonitoringAlerts": [
        {
          object ([ModelMonitoringAlert](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.modelMonitors/searchModelMonitoringAlerts#ModelMonitoringAlert))
        }
      ],
      "totalNumberAlerts": string,
      "nextPageToken": string
    }  
  
### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `modelMonitor` resource:

  * `aiplatform.modelMonitors.searchModelMonitoringAlerts`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## ModelMonitoringAlert

Represents a single monitoring alert. This is currently used in the modelMonitors.searchModelMonitoringAlerts api, thus the alert wrapped in this message belongs to the resource asked in the request.

Fields  
  
`statsName` `string` The stats name. | `objectiveType` `string` One of the supported monitoring objectives: `raw-feature-drift` `prediction-output-drift` `feature-attribution` | `alertTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Alert creation time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | `anomaly` `object (`[ModelMonitoringAnomaly](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.modelMonitors/searchModelMonitoringAlerts#ModelMonitoringAnomaly)`)` Anomaly details. | JSON representation  
---  
      
    
    {
      "statsName": string,
      "objectiveType": string,
      "alertTime": string,
      "anomaly": {
        object ([ModelMonitoringAnomaly](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.modelMonitors/searchModelMonitoringAlerts#ModelMonitoringAnomaly))
      }
    }  
  
## ModelMonitoringAnomaly

Represents a single model monitoring anomaly.

Fields  
  
`modelMonitoringJob` `string` Model monitoring job resource name. | `algorithm` `string` algorithm used to calculated the metrics, eg: jensen_shannon_divergence, l_infinity. | `anomaly` `Union type`  
  
The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`tabularAnomaly` `object (`[TabularAnomaly](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.modelMonitors/searchModelMonitoringAlerts#TabularAnomaly)`)` Tabular anomaly. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
      "modelMonitoringJob": string,
      "algorithm": string,
    
      // anomaly
      "tabularAnomaly": {
        object ([TabularAnomaly](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.modelMonitors/searchModelMonitoringAlerts#TabularAnomaly))
      }
      // Union type
    }  
  
## TabularAnomaly

Tabular anomaly details.

Fields  
  
`anomalyUri` `string` Additional anomaly information. e.g. Google Cloud Storage uri. | `summary` `string` Overview of this anomaly. | `anomaly` `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` Anomaly body. | `triggerTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time the anomaly was triggered.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | `condition` `object (`[ModelMonitoringAlertCondition](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/TabularObjective#ModelMonitoringAlertCondition)`)` The alert condition associated with this anomaly. | JSON representation  
---  
      
    
    {
      "anomalyUri": string,
      "summary": string,
      "anomaly": value,
      "triggerTime": string,
      "condition": {
        object ([ModelMonitoringAlertCondition](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/TabularObjective#ModelMonitoringAlertCondition))
      }
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
