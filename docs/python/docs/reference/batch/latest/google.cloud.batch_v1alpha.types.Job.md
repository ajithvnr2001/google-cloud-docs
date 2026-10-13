---
url: https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.Job
title: Class Job (0.22.4) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:43:39.950330+00:00
---

# Class Job (0.22.4)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.Job

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Job (0.22.4) Stay organized with collections  Save and categorize content based on your preferences. 

0.22.4 (latest)  0.22.3  0.21.0  0.20.0  0.19.0  0.18.0  0.17.37  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.1  0.7.0  0.6.0  0.5.0  0.4.1  0.3.2  0.2.0  0.1.2 
    
    
    Job(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The Cloud Batch Job description.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Output only. Job name. For example: "projects/123456/locations/us-central1/jobs/job01".   
`uid` |  `str`   
Output only. A system generated unique ID for the Job.   
`priority` |  `int`   
Priority of the Job. The valid value range is [0, 100). Default value is 0. Higher value indicates higher priority. A job with higher priority value is more likely to run earlier if all other requirements are satisfied.   
`task_groups` |  `MutableSequence[[google.cloud.batch_v1alpha.types.TaskGroup](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.TaskGroup)]`   
Required. TaskGroups in the Job. Only one TaskGroup is supported now.   
`scheduling_policy` |  `[google.cloud.batch_v1alpha.types.Job.SchedulingPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.Job.SchedulingPolicy)`   
Scheduling policy for TaskGroups in the job.   
`dependencies` |  `MutableSequence[[google.cloud.batch_v1alpha.types.JobDependency](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.JobDependency)]`   
At least one of the dependencies must be satisfied before the Job is scheduled to run. Only one JobDependency is supported now. Not yet implemented.   
`allocation_policy` |  `[google.cloud.batch_v1alpha.types.AllocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.AllocationPolicy)`   
Compute resource allocation for all TaskGroups in the Job.   
`labels` |  `MutableMapping[str, str]`   
Custom labels to apply to the job and any Cloud Logging `LogEntry `__ that it generates. Use labels to group and describe the resources they are applied to. Batch automatically applies predefined labels and supports multiple `labels` fields for each job, which each let you apply custom labels to various resources. Label names that start with "goog-" or "google-" are reserved for predefined labels. For more information about labels with Batch, see `Organize resources using labels   
`status` |  `[google.cloud.batch_v1alpha.types.JobStatus](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.JobStatus)`   
Output only. Job status. It is read only for users.   
`notification` |  `[google.cloud.batch_v1alpha.types.JobNotification](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.JobNotification)`   
Deprecated: please use notifications instead.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. When the Job was created.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The last time the Job was updated.   
`logs_policy` |  `[google.cloud.batch_v1alpha.types.LogsPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.LogsPolicy)`   
Log preservation policy for the Job.   
`notifications` |  `MutableSequence[[google.cloud.batch_v1alpha.types.JobNotification](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.JobNotification)]`   
Notification configurations.   
  
## Classes 

### LabelsEntry
    
    
    LabelsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The abstract base class for a message.

**Parameters**  
---  
**Name** | **Description**  
`kwargs` |  `dict`   
Keys and values corresponding to the fields of the message.  
`mapping` |  `Union[dict, `.Message`]`   
A dictionary or message to be used to determine the values for this message.  
`ignore_unknown_fields` |  `Optional(bool)`   
If True, do not raise errors for unknown fields. Only applied if `mapping` is a mapping type or there are keyword parameters.  
  
### SchedulingPolicy
    
    
    SchedulingPolicy(value)

The order that TaskGroups are scheduled relative to each other. Not yet implemented.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
