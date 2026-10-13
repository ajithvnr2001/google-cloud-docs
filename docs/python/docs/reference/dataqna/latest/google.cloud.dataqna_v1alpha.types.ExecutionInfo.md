---
url: https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.ExecutionInfo
title: Class ExecutionInfo (0.14.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:49:24.551515+00:00
---

# Class ExecutionInfo (0.14.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.ExecutionInfo

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ExecutionInfo (0.14.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.14.1 (latest)  0.14.0  0.13.0  0.12.0  0.11.0  0.10.17  0.9.0  0.8.2  0.7.1  0.6.3  0.5.1  0.4.0  0.3.3  0.2.1  0.1.1 
    
    
    ExecutionInfo(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Information about the backend status (such as BigQuery) of the execution.

## Attributes  
  
---  
**Name** | **Description**  
`job_creation_status` |  `google.rpc.status_pb2.Status`   
Status returned by the backend when the job was created.   
`job_execution_state` |  `[google.cloud.dataqna_v1alpha.types.ExecutionInfo.JobExecutionState](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.ExecutionInfo.JobExecutionState)`   
Status of the job execution.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Time when the execution was triggered.   
`bigquery_job` |  `[google.cloud.dataqna_v1alpha.types.BigQueryJob](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.BigQueryJob)`   
BigQuery job information. Future versions will have different backends. Hence, clients must make sure they can handle it when this field is not populated.   
  
## Classes 

### JobExecutionState
    
    
    JobExecutionState(value)

Enum of possible job execution statuses.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
