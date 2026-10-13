---
url: https://docs.cloud.google.com/python/docs/reference/bigquerylogging/latest/google.cloud.bigquery_logging_v1.types.JobStatistics
title: Class JobStatistics (1.11.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:43:11.660411+00:00
---

# Class JobStatistics (1.11.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/bigquerylogging/latest/google.cloud.bigquery_logging_v1.types.JobStatistics

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class JobStatistics (1.11.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.11.0 (latest)  1.10.0  1.9.0  1.8.0  1.7.0  1.6.3  1.5.0  1.4.5  1.2.2  1.1.0  1.0.7  0.3.0  0.2.2  0.1.1 
    
    
    JobStatistics(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Job statistics that may change after a job starts.

## Attributes  
  
---  
**Name** | **Description**  
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Time when the job was created.   
`start_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Time when the job started.   
`end_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Time when the job ended.   
`total_processed_bytes` |  `int`   
Total bytes processed for a job.   
`total_billed_bytes` |  `int`   
Processed bytes, adjusted by the job's CPU usage.   
`billing_tier` |  `int`   
The tier assigned by CPU-based billing.   
`total_slot_ms` |  `int`   
The total number of slot-ms consumed by the query job.   
`reservation_usage` |  `MutableSequence[[google.cloud.bigquery_logging_v1.types.JobStatistics.ReservationResourceUsage](https://docs.cloud.google.com/python/docs/reference/bigquerylogging/latest/google.cloud.bigquery_logging_v1.types.JobStatistics.ReservationResourceUsage)]`   
Reservation usage. This field reported misleading information and will no longer be populated. Aggregate usage of all jobs submitted to a reservation should provide a more reliable indicator of reservation imbalance.   
`reservation` |  `str`   
Reservation name or "unreserved" for on-demand resource usage.   
`referenced_tables` |  `MutableSequence[[google.cloud.bigquery_logging_v1.types.TableName](https://docs.cloud.google.com/python/docs/reference/bigquerylogging/latest/google.cloud.bigquery_logging_v1.types.TableName)]`   
The first N tables accessed by the query job. Older queries that reference a large number of tables may not have all of their tables in this list. You can use the total_tables_processed count to know how many total tables were read in the query. For new queries, there is currently no limit.   
`total_tables_processed` |  `int`   
Total number of unique tables referenced in the query.   
`referenced_views` |  `MutableSequence[[google.cloud.bigquery_logging_v1.types.TableName](https://docs.cloud.google.com/python/docs/reference/bigquerylogging/latest/google.cloud.bigquery_logging_v1.types.TableName)]`   
The first N views accessed by the query job. Older queries that reference a large number of views may not have all of their views in this list. You can use the total_tables_processed count to know how many total tables were read in the query. For new queries, there is currently no limit.   
`total_views_processed` |  `int`   
Total number of unique views referenced in the query.   
`query_output_row_count` |  `int`   
Number of output rows produced by the query job.   
`total_load_output_bytes` |  `int`   
Total bytes loaded for an import job.   
  
## Classes 

### ReservationResourceUsage
    
    
    ReservationResourceUsage(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Job resource usage breakdown by reservation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
