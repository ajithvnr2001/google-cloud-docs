---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.types.MaintenanceSummary
title: Class MaintenanceSummary (0.4.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:31:22.062952+00:00
---

# Class MaintenanceSummary (0.4.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.types.MaintenanceSummary

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class MaintenanceSummary (0.4.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.4.2 (latest)  0.4.1  0.3.0  0.2.0  0.1.1 
    
    
    MaintenanceSummary(mapping=None, *, ignore_unknown_fields=False, **kwargs)

MaintenanceSummary contains maintenance statistics calculated based on ResourceMaintenances within the scope: project and location.

## Attributes  
  
---  
**Name** | **Description**  
`maintenance_name` |  `str`   
Output only. The name of the maintenance.   
`title` |  `str`   
Output only. The title of the maintenance.   
`description` |  `str`   
Output only. The description of the maintenance.   
`category` |  `[google.cloud.maintenance_api_v1.types.MaintenanceCategory](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.types.MaintenanceCategory)`   
Output only. The category of the maintenance event.   
`maintenance_scheduled_start_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Scheduled start time of the maintenance. The maintenance will start at `maintenanceScheduledStartTime` or later, with best effort to finish before `maintenanceScheduledEndTime`.   
`maintenance_scheduled_end_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. An estimated (best effort, not guaranteed) end time of the scheduled maintenance.   
`maintenance_start_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Actual date when the maintenance started. Field present only after the state changed to `RUNNING`.   
`maintenance_end_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Actual date when the maintenance successfully completed. Field present only after the state changed to `SUCCEEDED`.   
`user_controllable` |  `bool`   
Output only. Indicates whether the user has some control over that maintenance, either proactively before maintenance was scheduled with maintenance policy or with reactive controls after it was scheduled (see controls field).   
`controls` |  `MutableSequence[[google.cloud.maintenance_api_v1.types.MaintenanceControl](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.types.MaintenanceControl)]`   
Output only. Control available for that Maintenance (might not be available for every resource that maintenance is applied to).   
`stats` |  `MutableSequence[[google.cloud.maintenance_api_v1.types.MaintenanceSummary.Stats](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.types.MaintenanceSummary.Stats)]`   
Output only. Stats is a field of ResourceMaintenance used to aggregate the stats.   
  
## Classes 

### Aggregate
    
    
    Aggregate(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Aggregate is a <group, count> pair.

### Stats
    
    
    Stats(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Stats indicates the type of aggregate and the corresponding aggregates.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
