---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.metricDefinitions
title: REST Resource: projects.locations.instances.metricDefinitions \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:34:42.430330+00:00
---

# REST Resource: projects.locations.instances.metricDefinitions  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.metricDefinitions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  REST Resource: projects.locations.instances.metricDefinitions Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: MetricDefinition
    * JSON representation
  * MetricDefinitionState
  * Methods



## Resource: MetricDefinition

A MetricDefinition represents a specification for a type of aggregated metric value that Google should compute based on logs. The computed values can be used in various Google SecOps features.

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "textDefinition": string,
      "author": string,
      "createTime": string,
      "updateTime": string,
      "lastUpdater": string,
      "state": enum ([MetricDefinitionState](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.metricDefinitions#MetricDefinitionState)),
      "computationNotification": {
        object ([Status](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/ListOperationsResponse#Status))
      },
      "matchVariables": [
        string
      ],
      "matchWindowLength": string,
      "outcomeVariables": [
        string
      ]
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique resource name of the MetricDefinition. Format: `projects/{project}/locations/{location}/instances/{instance}/metricDefinitions/{metricDefinition}` The resource ID will be used as a display name in the SecOps UI. This ID can be at most 63 characters long, must begin with a letter, and may only contain lowercase alphanumeric characters and underscores, i.e. it must match a regular expression of `[a-z][_a-z0-9]{0,61}[a-z0-9]`. Only Google-defined MetricDefinitions may begin with "google_".  
`description` |  `string` Output only. A description of the MetricDefinition as extracted from the `textDefinition` field.  
`textDefinition` |  `string` Required. Immutable. The full text of this MetricDefinition. For guidelines on writing a metric definition in YARA-L 2.0.  
`author` |  `string` Output only. The username (e.g: email address) of the author of the MetricDefinition.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp at which the MetricDefinition was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp at which the MetricDefinition was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastUpdater` |  `string` Output only. The username (e.g: email address) of the user that most recently updated the MetricDefinition.  
`state` |  `enum (`[MetricDefinitionState](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.metricDefinitions#MetricDefinitionState)`)` Optional. The state of the MetricDefinition. When a MetricDefinition is created, the state `ENABLED` will be applied by default if none is provided.  
`computationNotification` |  `object (`[Status](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/ListOperationsResponse#Status)`)` Output only. The most recent notification which arose for this MetricDefinition during computation, if there is one. Notifications may be errors or warnings.  
`matchVariables[]` |  `string` Output only. The match variables of this MetricDefinition. This will be extracted from the `textDefinition` field.  
`matchWindowLength` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Output only. The duration over which values for this MetricDefinition will be computed. This will be extracted from the `textDefinition` field.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`outcomeVariables[]` |  `string` Output only. The names of the outcomes of this Metric. These outcome variables can be used in rules, searches, and dashboards in Google SecOps. This will be extracted from the `text` field.  
  
## MetricDefinitionState

The state of a MetricDefinition.

Enums  
---  
`METRIC_DEFINITION_STATE_UNSPECIFIED` | The MetricDefinition state is unspecified.  
`ENABLED` | The MetricDefinition is enabled and can be used in other Google SecOps features.  
`DISABLED` | The MetricDefinition is disabled and cannot be used in other Google SecOps features.  
`PAUSED` | The MetricDefinition had a problem and had to be paused by Google. Paused metric definitions will be un-paused by Google once the issue is resolved, and cannot leave this state in any other way.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.metricDefinitions/create)`

|  Creates a new MetricDefinition.  
  
### `[get](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.metricDefinitions/get)`

|  Get a MetricDefinition for a given instance and metric definition resourcename.  
  
### `[list](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.metricDefinitions/list)`

|  List all MetricDefinitions for a given instance.  
  
### `[patch](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.metricDefinitions/patch)`

|  Updates a MetricDefinition.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-07 UTC."],[],[]] 
