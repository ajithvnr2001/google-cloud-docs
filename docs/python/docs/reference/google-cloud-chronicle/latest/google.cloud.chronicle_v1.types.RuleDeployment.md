---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-chronicle/latest/google.cloud.chronicle_v1.types.RuleDeployment
title: Class RuleDeployment (0.6.4) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:07:23.453177+00:00
---

# Class RuleDeployment (0.6.4)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-chronicle/latest/google.cloud.chronicle_v1.types.RuleDeployment

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class RuleDeployment (0.6.4) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.4 (latest)  0.6.3  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    RuleDeployment(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The RuleDeployment resource represents the deployment state of a Rule.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Required. The resource name of the rule deployment. Note that RuleDeployment is a child of the overall Rule, not any individual revision, so the resource ID segment for the Rule resource must not reference a specific revision. Format: `projects/{project}/locations/{location}/instances/{instance}/rules/{rule}/deployment`  
`enabled` |  `bool`   
Whether the rule is currently deployed continuously against incoming data.   
`alerting` |  `bool`   
Whether detections resulting from this deployment should be considered alerts.   
`archived` |  `bool`   
The archive state of the rule deployment. Cannot be set to true unless enabled is set to false. If set to true, alerting will automatically be set to false. If currently set to true, enabled, alerting, and run_frequency cannot be updated.   
`archive_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The timestamp when the rule deployment archive state was last set to true. If the rule deployment's current archive state is not set to true, the field will be empty.   
`run_frequency` |  `[google.cloud.chronicle_v1.types.RunFrequency](https://docs.cloud.google.com/python/docs/reference/google-cloud-chronicle/latest/google.cloud.chronicle_v1.types.RunFrequency)`   
The run frequency of the rule deployment.   
`execution_state` |  `[google.cloud.chronicle_v1.types.RuleDeployment.ExecutionState](https://docs.cloud.google.com/python/docs/reference/google-cloud-chronicle/latest/google.cloud.chronicle_v1.types.RuleDeployment.ExecutionState)`   
Output only. The execution state of the rule deployment.   
`producer_rules` |  `MutableSequence[str]`   
Output only. The names of the associated/chained producer rules. Rules are considered producers for this rule if this rule explicitly filters on their ruleid. Format: `projects/{project}/locations/{location}/instances/{instance}/rules/{rule}`  
`consumer_rules` |  `MutableSequence[str]`   
Output only. The names of the associated/chained consumer rules. Rules are considered consumers of this rule if their rule text explicitly filters on this rule's ruleid. Format: `projects/{project}/locations/{location}/instances/{instance}/rules/{rule}`  
`last_alert_status_change_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The timestamp when the rule deployment alert state was lastly changed. This is filled regardless of the current alert state. E.g. if the current alert status is false, this timestamp will be the timestamp when the alert status was changed to false.   
  
## Classes 

### ExecutionState
    
    
    ExecutionState(value)

The possible execution states the rule deployment can be in.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
