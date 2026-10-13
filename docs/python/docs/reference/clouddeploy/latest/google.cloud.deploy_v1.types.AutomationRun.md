---
url: https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.AutomationRun
title: Class AutomationRun (2.12.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:42:43.142760+00:00
---

# Class AutomationRun (2.12.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.AutomationRun

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AutomationRun (2.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.12.0 (latest)  2.11.0  2.10.0  2.9.0  2.8.0  2.7.1  2.6.3  2.5.0  2.4.1  2.3.0  2.2.0  2.1.0  2.0.0  1.19.1  1.18.1  1.17.3  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.1  1.10.1  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.1  1.3.1  1.2.1  1.1.1  1.0.0  0.3.2  0.2.0  0.1.1 
    
    
    AutomationRun(mapping=None, *, ignore_unknown_fields=False, **kwargs)

An `AutomationRun` resource in the Cloud Deploy API.

An `AutomationRun` represents an execution instance of an automation rule.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Output only. Name of the `AutomationRun`. Format is `projects/{project}/locations/{location}/deliveryPipelines/{delivery_pipeline}/automationRuns/{automation_run}`.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Time at which the `AutomationRun` was created.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Time at which the automationRun was updated.   
`etag` |  `str`   
Output only. The weak etag of the `AutomationRun` resource. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.   
`service_account` |  `str`   
Output only. Email address of the user-managed IAM service account that performs the operations against Cloud Deploy resources.   
`automation_snapshot` |  `google.cloud.deploy_v1.types.Automation`   
Output only. Snapshot of the Automation taken at AutomationRun creation time.   
`target_id` |  `str`   
Output only. The ID of the source target that initiates the `AutomationRun`. The value of this field is the last segment of a target name.   
`state` |  `[google.cloud.deploy_v1.types.AutomationRun.State](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.AutomationRun.State)`   
Output only. Current state of the `AutomationRun`.   
`state_description` |  `str`   
Output only. Explains the current state of the `AutomationRun`. Present only when an explanation is needed.   
`policy_violation` |  `[google.cloud.deploy_v1.types.PolicyViolation](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.PolicyViolation)`   
Output only. Contains information about what policies prevented the `AutomationRun` from proceeding.   
`expire_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Time the `AutomationRun` expires. An `AutomationRun` expires after 14 days from its creation date.   
`rule_id` |  `str`   
Output only. The ID of the automation rule that initiated the operation.   
`automation_id` |  `str`   
Output only. The ID of the automation that initiated the operation.   
`promote_release_operation` |  `[google.cloud.deploy_v1.types.PromoteReleaseOperation](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.PromoteReleaseOperation)`   
Output only. Promotes a release to a specified 'Target'. This field is a member of `oneof`_ `operation`.   
`advance_rollout_operation` |  `[google.cloud.deploy_v1.types.AdvanceRolloutOperation](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.AdvanceRolloutOperation)`   
Output only. Advances a rollout to the next phase. This field is a member of `oneof`_ `operation`.   
`repair_rollout_operation` |  `[google.cloud.deploy_v1.types.RepairRolloutOperation](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.RepairRolloutOperation)`   
Output only. Repairs a failed 'Rollout'. This field is a member of `oneof`_ `operation`.   
`timed_promote_release_operation` |  `[google.cloud.deploy_v1.types.TimedPromoteReleaseOperation](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.TimedPromoteReleaseOperation)`   
Output only. Promotes a release to a specified 'Target' as defined in a Timed Promote Release rule. This field is a member of `oneof`_ `operation`.   
`wait_until_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Earliest time the `AutomationRun` will attempt to resume. Wait-time is configured by `wait` in automation rule.   
  
## Classes 

### State
    
    
    State(value)

Valid state of an `AutomationRun`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
