---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/RuleDeployment/
title: RuleDeployment \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:20:02.490658+00:00
---

# RuleDeployment  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/RuleDeployment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  RuleDeployment Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * ScheduleCustomizations
    * JSON representation
  * ExecutionState



The RuleDeployment resource represents the deployment state of a Rule.

JSON representation  
---  
      
    
    {
      "name": string,
      "enabled": boolean,
      "alerting": boolean,
      "archived": boolean,
      "archiveTime": string,
      "runFrequency": enum ([RunFrequency](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.rules#RunFrequency)),
      "scheduleCustomizations": {
        object ([ScheduleCustomizations](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/RuleDeployment#ScheduleCustomizations))
      },
      "executionState": enum ([ExecutionState](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/RuleDeployment#ExecutionState)),
      "producerRules": [
        string
      ],
      "consumerRules": [
        string
      ],
      "lastAlertStatusChangeTime": string,
      "displayName": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the rule deployment. Note that RuleDeployment is a child of the overall Rule, not any individual revision, so the resource ID segment for the Rule resource must not reference a specific revision. Format: `projects/{project}/locations/{location}/instances/{instance}/rules/{rule}/deployment`  
`enabled` |  `boolean` Whether the rule is currently deployed continuously against incoming data.  
`alerting` |  `boolean` Whether detections resulting from this deployment should be considered alerts.  
`archived` |  `boolean` The archive state of the rule deployment. Cannot be set to true unless enabled is set to false. If set to true, alerting will automatically be set to false. If currently set to true, enabled, alerting, and runFrequency cannot be updated.  
`archiveTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the rule deployment archive state was last set to true. If the rule deployment's current archive state is not set to true, the field will be empty.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`runFrequency` |  `enum (`[RunFrequency](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.rules#RunFrequency)`)` The run frequency of the rule deployment.  
`scheduleCustomizations` |  `object (`[ScheduleCustomizations](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/RuleDeployment#ScheduleCustomizations)`)` Optional. The schedule customizations of the rule deployment. Only valid for customizable run frequencies. Note that because schedule customizations are tied to run frequency, they must be updated using the "runFrequency" update mask. There is no separate update mask value specifically for schedule customizations.  
`executionState` |  `enum (`[ExecutionState](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/RuleDeployment#ExecutionState)`)` Output only. The execution state of the rule deployment.  
`producerRules[]` |  `string` Output only. The names of the associated/chained producer rules. Rules are considered producers for this rule if this rule explicitly filters on their ruleid. Format: `projects/{project}/locations/{location}/instances/{instance}/rules/{rule}`  
`consumerRules[]` |  `string` Output only. The names of the associated/chained consumer rules. Rules are considered consumers of this rule if their rule text explicitly filters on this rule's ruleid. Format: `projects/{project}/locations/{location}/instances/{instance}/rules/{rule}`  
`lastAlertStatusChangeTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the rule deployment alert state was lastly changed. This is filled regardless of the current alert state. E.g. if the current alert status is false, this timestamp will be the timestamp when the alert status was changed to false.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`displayName` |  `string` Output only. The display name of the parent rule.  
  
## ScheduleCustomizations

ScheduleCustomizations customize schedules for rules with customizable run frequencies.

JSON representation  
---  
      
    
    {
      "ensureEnrichmentCompleteness": boolean,
      "lateArrivingDataAdjustment": string
    }  
  
Fields  
---  
`ensureEnrichmentCompleteness` |  `boolean` Optional. Indicates whether to add additional delays and runs to rules to ensure enrichment completeness, with the trade-off of higher detection latencies.  
`lateArrivingDataAdjustment` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. Adjust the first rule execution run to account for late-arriving data.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
## ExecutionState

The possible execution states the rule deployment can be in.

Enums  
---  
`EXECUTION_STATE_UNSPECIFIED` | Unspecified or unknown execution state.  
`DEFAULT` | Default execution state.  
`LIMITED` | Rules in limited state may not have their executions guaranteed.  
`PAUSED` | Paused rules are not executed at all.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
