---
url: https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.JobRun
title: Class JobRun (2.12.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:42:55.715531+00:00
---

# Class JobRun (2.12.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.JobRun

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class JobRun (2.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.12.0 (latest)  2.11.0  2.10.0  2.9.0  2.8.0  2.7.1  2.6.3  2.5.0  2.4.1  2.3.0  2.2.0  2.1.0  2.0.0  1.19.1  1.18.1  1.17.3  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.1  1.10.1  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.1  1.3.1  1.2.1  1.1.1  1.0.0  0.3.2  0.2.0  0.1.1 
    
    
    JobRun(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A `JobRun` resource in the Cloud Deploy API.

A `JobRun` contains information of a single `Rollout` job evaluation.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Output only. Name of the `JobRun`. Format is `projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}/releases/{releases}/rollouts/{rollouts}/jobRuns/{uuid}`.   
`uid` |  `str`   
Output only. Unique identifier of the `JobRun`.   
`phase_id` |  `str`   
Output only. ID of the `Rollout` phase this `JobRun` belongs in.   
`job_id` |  `str`   
Output only. ID of the `Rollout` job this `JobRun` corresponds to.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Time at which the `JobRun` was created.   
`start_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Time at which the `JobRun` was started.   
`end_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Time at which the `JobRun` ended.   
`state` |  `[google.cloud.deploy_v1.types.JobRun.State](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.JobRun.State)`   
Output only. The current state of the `JobRun`.   
`deploy_job_run` |  `[google.cloud.deploy_v1.types.DeployJobRun](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeployJobRun)`   
Output only. Information specific to a deploy `JobRun`. This field is a member of `oneof`_ `job_run`.   
`verify_job_run` |  `[google.cloud.deploy_v1.types.VerifyJobRun](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.VerifyJobRun)`   
Output only. Information specific to a verify `JobRun`. This field is a member of `oneof`_ `job_run`.   
`predeploy_job_run` |  `[google.cloud.deploy_v1.types.PredeployJobRun](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.PredeployJobRun)`   
Output only. Information specific to a predeploy `JobRun`. This field is a member of `oneof`_ `job_run`.   
`postdeploy_job_run` |  `[google.cloud.deploy_v1.types.PostdeployJobRun](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.PostdeployJobRun)`   
Output only. Information specific to a postdeploy `JobRun`. This field is a member of `oneof`_ `job_run`.   
`create_child_rollout_job_run` |  `[google.cloud.deploy_v1.types.CreateChildRolloutJobRun](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CreateChildRolloutJobRun)`   
Output only. Information specific to a createChildRollout `JobRun`. This field is a member of `oneof`_ `job_run`.   
`advance_child_rollout_job_run` |  `[google.cloud.deploy_v1.types.AdvanceChildRolloutJobRun](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.AdvanceChildRolloutJobRun)`   
Output only. Information specific to an advanceChildRollout `JobRun` This field is a member of `oneof`_ `job_run`.   
`etag` |  `str`   
Output only. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.   
  
## Classes 

### State
    
    
    State(value)

Valid states of a `JobRun`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
