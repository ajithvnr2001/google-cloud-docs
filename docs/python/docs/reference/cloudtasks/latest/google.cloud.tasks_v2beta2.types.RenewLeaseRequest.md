---
url: https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.RenewLeaseRequest
title: Class RenewLeaseRequest (2.26.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:56:14.661084+00:00
---

# Class RenewLeaseRequest (2.26.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.RenewLeaseRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class RenewLeaseRequest (2.26.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.26.0 (latest)  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.3  2.18.0  2.17.1  2.16.5  2.15.1  2.14.2  2.13.2  2.12.1  2.11.0  2.10.4  2.9.1  2.8.1  2.7.2  2.6.0  2.5.3  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.5.2  1.4.0  1.3.0  1.2.1 
    
    
    RenewLeaseRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Request message for renewing a lease using RenewLease.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Required. The task name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID`  
`schedule_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Required. The task's current schedule time, available in the schedule_time returned by LeaseTasks response or RenewLease response. This restriction is to ensure that your worker currently holds the lease.   
`lease_duration` |  `google.protobuf.duration_pb2.Duration`   
Required. The desired new lease duration, starting from now. The maximum lease duration is 1 week. `lease_duration` will be truncated to the nearest second.   
`response_view` |  `[google.cloud.tasks_v2beta2.types.Task.View](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.Task.View)`   
The response_view specifies which subset of the Task will be returned. By default response_view is BASIC; not all information is retrieved by default because some data, such as payloads, might be desirable to return only when needed because of its large size or because of the sensitivity of data that it contains. Authorization for FULL requires `cloudtasks.tasks.fullView` `Google IAM   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
