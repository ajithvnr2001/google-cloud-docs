---
url: https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.JobNotification
title: Class JobNotification (0.22.4) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:43:42.049925+00:00
---

# Class JobNotification (0.22.4)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.JobNotification

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class JobNotification (0.22.4) Stay organized with collections  Save and categorize content based on your preferences. 

0.22.4 (latest)  0.22.3  0.21.0  0.20.0  0.19.0  0.18.0  0.17.37  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.1  0.7.0  0.6.0  0.5.0  0.4.1  0.3.2  0.2.0  0.1.2 
    
    
    JobNotification(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Notification configurations.

## Attributes  
  
---  
**Name** | **Description**  
`pubsub_topic` |  `str`   
The Pub/Sub topic where notifications for the job, like state changes, will be published. If undefined, no Pub/Sub notifications are sent for this job. Specify the topic using the following format: `projects/{project}/topics/{topic}`. Notably, if you want to specify a Pub/Sub topic that is in a different project than the job, your administrator must grant your project's Batch service agent permission to publish to that topic. For more information about configuring Pub/Sub notifications for a job, see https://cloud.google.com/batch/docs/enable-notifications.   
`message` |  `[google.cloud.batch_v1alpha.types.JobNotification.Message](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.JobNotification.Message)`   
The attribute requirements of messages to be sent to this Pub/Sub topic. Without this field, no message will be sent.   
  
## Classes 

### Message
    
    
    Message(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Message details. Describe the conditions under which messages will be sent. If no attribute is defined, no message will be sent by default. One message should specify either the job or the task level attributes, but not both. For example, job level: JOB_STATE_CHANGED and/or a specified new_job_state; task level: TASK_STATE_CHANGED and/or a specified new_task_state.

### Type
    
    
    Type(value)

The message type.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
