---
url: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupPlanRevision
title: Class BackupPlanRevision (0.10.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:17:50.490774+00:00
---

# Class BackupPlanRevision (0.10.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupPlanRevision

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class BackupPlanRevision (0.10.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.3 (latest)  0.10.2  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.5  0.1.7 
    
    
    BackupPlanRevision(mapping=None, *, ignore_unknown_fields=False, **kwargs)

`BackupPlanRevision` represents a snapshot of a `BackupPlan` at a point in time.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Output only. Identifier. The resource name of the `BackupPlanRevision`. Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}/revisions/{revision}`  
`revision_id` |  `str`   
Output only. The user friendly revision ID of the `BackupPlanRevision`. Example: v0, v1, v2, etc.   
`state` |  `[google.cloud.backupdr_v1.types.BackupPlanRevision.State](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupPlanRevision.State)`   
Output only. Resource State   
`backup_plan_snapshot` |  `google.cloud.backupdr_v1.types.BackupPlan`   
The Backup Plan being encompassed by this revision.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The timestamp that the revision was created.   
  
## Classes 

### State
    
    
    State(value)

The state of the `BackupPlanRevision`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
