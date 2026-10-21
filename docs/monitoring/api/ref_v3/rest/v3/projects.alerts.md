---
url: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alerts
title: REST Resource: projects.alerts \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:11.731233+00:00
---

# REST Resource: projects.alerts  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alerts

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  REST Resource: projects.alerts Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Alert
    * JSON representation
  * State
  * MonitoredResourceMetadata
    * JSON representation
  * Metric
    * JSON representation
  * LogMetadata
    * JSON representation
  * PolicySnapshot
    * JSON representation
  * Methods



## Resource: Alert

An alert is the representation of a violation of an alert policy. It is a read-only resource that cannot be modified by the accompanied API.

JSON representation  
---  
      
    
    {
      "name": string,
      "state": enum ([State](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alerts#State)),
      "openTime": string,
      "closeTime": string,
      "resource": {
        object ([MonitoredResource](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/Shared.Types/MonitoredResource))
      },
      "metadata": {
        object ([MonitoredResourceMetadata](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alerts#MonitoredResourceMetadata))
      },
      "metric": {
        object ([Metric](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alerts#Metric))
      },
      "log": {
        object ([LogMetadata](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alerts#LogMetadata))
      },
      "policy": {
        object ([PolicySnapshot](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alerts#PolicySnapshot))
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the alert.The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/alerts/[ALERT_ID]
    

The `[ALERT_ID]` is a system-assigned unique identifier for the alert.  
`state` |  `enum (`[State](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alerts#State)`)` Output only. The current state of the alert.  
`openTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time when the alert was opened.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`closeTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time when the alert was closed.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`resource` |  `object (`[MonitoredResource](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/Shared.Types/MonitoredResource)`)` The monitored resource type and any monitored resource labels preserved from the incident's generating condition.  
`metadata` |  `object (`[MonitoredResourceMetadata](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alerts#MonitoredResourceMetadata)`)` The metadata of the monitored resource.  
`metric` |  `object (`[Metric](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alerts#Metric)`)` The metric type and any metric labels preserved from the incident's generating condition.  
`log` |  `object (`[LogMetadata](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alerts#LogMetadata)`)` The log information associated with the alert. This field is only populated for log-based alerts.  
`policy` |  `object (`[PolicySnapshot](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alerts#PolicySnapshot)`)` The snapshot of the alert policy that generated this alert.  
  
## State

The enumeration of possible states for an alert.

Enums  
---  
`STATE_UNSPECIFIED` | The alert state is unspecified.  
`OPEN` | The alert is open.  
`CLOSED` | The alert is closed.  
  
## MonitoredResourceMetadata

Auxiliary metadata for a `[MonitoredResource](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/Shared.Types/MonitoredResource)` object. `[MonitoredResource](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/Shared.Types/MonitoredResource)` objects contain the minimum set of information to uniquely identify a monitored resource instance. There is some other useful auxiliary metadata. Monitoring and Logging use an ingestion pipeline to extract metadata for cloud resources of all types, and store the metadata in this message.

JSON representation  
---  
      
    
    {
      "systemLabels": {
        object
      },
      "userLabels": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`systemLabels` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Output only. Values for predefined system metadata labels. System labels are a kind of metadata extracted by Google, including "machine_image", "vpc", "subnet_id", "security_group", "name", etc. System label values can be only strings, Boolean values, or a list of strings. For example:
    
    
    { "name": "my-test-instance",
      "security_group": ["a", "b", "c"],
      "spot_instance": false }
      
  
`userLabels` |  `map (key: string, value: string)` Output only. A map of user-defined metadata labels.  
  
## Metric

A specific metric, identified by specifying values for all of the labels of a `[`MetricDescriptor`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricDescriptor)`.

JSON representation  
---  
      
    
    {
      "type": string,
      "labels": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`type` |  `string` An existing metric type, see `[google.api.MetricDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricDescriptor)`. For example, `custom.googleapis.com/invoice/paid/amount`.  
`labels` |  `map (key: string, value: string)` The set of label values that uniquely identify this metric. All labels listed in the `MetricDescriptor` must be assigned values.  
  
## LogMetadata

Information about the log for log-based alerts.

JSON representation  
---  
      
    
    {
      "extractedLabels": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`extractedLabels` |  `map (key: string, value: string)` The labels extracted from the log.  
  
## PolicySnapshot

The state of the policy at the time the alert was generated.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "severity": enum ([Severity](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/Severity)),
      "userLabels": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`name` |  `string` The name of the alert policy resource. In the form of "projects/[PROJECT_ID_OR_NUMBER]/alertPolicies/[ALERT_POLICY_ID]".  
`displayName` |  `string` The display name of the alert policy.  
`severity` |  `enum (`[Severity](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/Severity)`)` The severity of the alert policy.  
`userLabels` |  `map (key: string, value: string)` The user labels for the alert policy.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alerts/get)`

|  Gets a single alert.  
  
### `[list](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alerts/list)`

|  Lists the existing alerts for the metrics scope of the project.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-23 UTC."],[],[]] 
