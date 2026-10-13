---
url: https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.JobStatus.State
title: Class State (0.22.4) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:43:42.208156+00:00
---

# Class State (0.22.4)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.JobStatus.State

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class State (0.22.4) Stay organized with collections  Save and categorize content based on your preferences. 

0.22.4 (latest)  0.22.3  0.21.0  0.20.0  0.19.0  0.18.0  0.17.37  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.1  0.7.0  0.6.0  0.5.0  0.4.1  0.3.2  0.2.0  0.1.2 
    
    
    State(value)

Valid Job states.

## Enums  
  
---  
**Name** | **Description**  
`STATE_UNSPECIFIED` | Job state unspecified.  
`QUEUED` | Job is admitted (validated and persisted) and waiting for resources.  
`SCHEDULED` | Job is scheduled to run as soon as resource allocation is ready. The resource allocation may happen at a later time but with a high chance to succeed.  
`RUNNING` | Resource allocation has been successful. At least one Task in the Job is RUNNING.  
`SUCCEEDED` | All Tasks in the Job have finished successfully.  
`FAILED` | At least one Task in the Job has failed.  
`DELETION_IN_PROGRESS` | The Job will be deleted, but has not been deleted yet. Typically this is because resources used by the Job are still being cleaned up.  
`CANCELLATION_IN_PROGRESS` | The Job cancellation is in progress, this is because the resources used by the Job are still being cleaned up.  
`CANCELLED` | The Job has been cancelled, the task executions were stopped and the resources were cleaned up.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
