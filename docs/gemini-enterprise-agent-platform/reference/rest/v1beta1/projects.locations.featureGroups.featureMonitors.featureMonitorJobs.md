---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featureGroups.featureMonitors.featureMonitorJobs
title: REST Resource: projects.locations.featureGroups.featureMonitors.featureMonitorJobs \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:07:44.850063+00:00
---

# REST Resource: projects.locations.featureGroups.featureMonitors.featureMonitorJobs  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featureGroups.featureMonitors.featureMonitorJobs

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  REST Resource: projects.locations.featureGroups.featureMonitors.featureMonitorJobs Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: FeatureMonitorJob

Agent Platform feature Monitor Job.

Fields  
  
`name` `string` Identifier. name of the FeatureMonitorJob. Format: `projects/{project}/locations/{location}/featureGroups/{featureGroup}/featureMonitors/{featureMonitor}/featureMonitorJobs/{featureMonitorJob}`. | `createTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. timestamp when this FeatureMonitorJob was created. Creation of a FeatureMonitorJob means that the job is pending / waiting for sufficient resources but may not have started running yet.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | `finalStatus` `object (`[Status](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ListOperationsResponse#Status)`)` Output only. Final status of the FeatureMonitorJob. | `jobSummary` `object (`[JobSummary](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featureGroups.featureMonitors.featureMonitorJobs#JobSummary)`)` Output only. Summary from the FeatureMonitorJob. | `labels` `map (key: string, value: string)` Optional. The labels with user-defined metadata to organize your FeatureMonitorJob.label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed.See <https://goo.gl/xmQnxf> for more information on and examples of labels. No more than 64 user labels can be associated with one FeatureMonitor(System labels are excluded)." System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable. | `description` `string` Optional. description of the FeatureMonitor. | `driftBaseFeatureMonitorJobId` `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. FeatureMonitorJob id comparing to which the drift is calculated. | `driftBaseSnapshotTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. data snapshot time comparing to which the drift is calculated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | `featureSelectionConfig` `object (`[FeatureSelectionConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/FeatureSelectionConfig)`)` Output only. feature selection config used when creating FeatureMonitorJob. | `triggerType` `enum (`[FeatureMonitorJobTrigger](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featureGroups.featureMonitors.featureMonitorJobs#FeatureMonitorJobTrigger)`)` Output only. Trigger type of the feature Monitor Job. | JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "finalStatus": {
        object ([Status](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ListOperationsResponse#Status))
      },
      "jobSummary": {
        object ([JobSummary](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featureGroups.featureMonitors.featureMonitorJobs#JobSummary))
      },
      "labels": {
        string: string,
        ...
      },
      "description": string,
      "driftBaseFeatureMonitorJobId": string,
      "driftBaseSnapshotTime": string,
      "featureSelectionConfig": {
        object ([FeatureSelectionConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/FeatureSelectionConfig))
      },
      "triggerType": enum ([FeatureMonitorJobTrigger](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featureGroups.featureMonitors.featureMonitorJobs#FeatureMonitorJobTrigger))
    }  
  
## JobSummary

Summary from the FeatureMonitorJob.

Fields  
  
`totalSlotMs` `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. BigQuery slot milliseconds consumed. | `featureStatsAndAnomalies[]` `object (`[FeatureStatsAndAnomaly](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/FeatureStatsAndAnomaly)`)` Output only. Features and their stats and anomalies | JSON representation  
---  
      
    
    {
      "totalSlotMs": string,
      "featureStatsAndAnomalies": [
        {
          object ([FeatureStatsAndAnomaly](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/FeatureStatsAndAnomaly))
        }
      ]
    }  
  
## FeatureMonitorJobTrigger

Choices of the trigger type.

Enums  
---  
`FEATURE_MONITOR_JOB_TRIGGER_UNSPECIFIED` | Trigger type unspecified.  
`FEATURE_MONITOR_JOB_TRIGGER_PERIODIC` | Triggered by periodic schedule.  
`FEATURE_MONITOR_JOB_TRIGGER_ON_DEMAND` | Triggered on demand by featureMonitorJobs.create request.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featureGroups.featureMonitors.featureMonitorJobs/create)`

|  Creates a new feature monitor job.  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featureGroups.featureMonitors.featureMonitorJobs/get)`

|  Get a feature monitor job.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featureGroups.featureMonitors.featureMonitorJobs/list)`

|  List feature monitor jobs.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-22 UTC."],[],[]] 
