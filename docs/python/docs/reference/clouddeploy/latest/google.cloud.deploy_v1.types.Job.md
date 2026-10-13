---
url: https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Job
title: Class Job (2.12.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:42:54.901908+00:00
---

# Class Job (2.12.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Job

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Job (2.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.12.0 (latest)  2.11.0  2.10.0  2.9.0  2.8.0  2.7.1  2.6.3  2.5.0  2.4.1  2.3.0  2.2.0  2.1.0  2.0.0  1.19.1  1.18.1  1.17.3  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.1  1.10.1  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.1  1.3.1  1.2.1  1.1.1  1.0.0  0.3.2  0.2.0  0.1.1 
    
    
    Job(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Job represents an operation for a `Rollout`.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`id` |  `str`   
Output only. The ID of the Job.   
`state` |  `[google.cloud.deploy_v1.types.Job.State](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Job.State)`   
Output only. The current state of the Job.   
`skip_message` |  `str`   
Output only. Additional information on why the Job was skipped, if available.   
`job_run` |  `str`   
Output only. The name of the `JobRun` responsible for the most recent invocation of this Job.   
`deploy_job` |  `[google.cloud.deploy_v1.types.DeployJob](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeployJob)`   
Output only. A deploy Job. This field is a member of `oneof`_ `job_type`.   
`verify_job` |  `[google.cloud.deploy_v1.types.VerifyJob](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.VerifyJob)`   
Output only. A verify Job. This field is a member of `oneof`_ `job_type`.   
`predeploy_job` |  `[google.cloud.deploy_v1.types.PredeployJob](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.PredeployJob)`   
Output only. A predeploy Job. This field is a member of `oneof`_ `job_type`.   
`postdeploy_job` |  `[google.cloud.deploy_v1.types.PostdeployJob](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.PostdeployJob)`   
Output only. A postdeploy Job. This field is a member of `oneof`_ `job_type`.   
`create_child_rollout_job` |  `[google.cloud.deploy_v1.types.CreateChildRolloutJob](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CreateChildRolloutJob)`   
Output only. A createChildRollout Job. This field is a member of `oneof`_ `job_type`.   
`advance_child_rollout_job` |  `[google.cloud.deploy_v1.types.AdvanceChildRolloutJob](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.AdvanceChildRolloutJob)`   
Output only. An advanceChildRollout Job. This field is a member of `oneof`_ `job_type`.   
  
## Classes 

### State
    
    
    State(value)

Valid states of a Job.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
