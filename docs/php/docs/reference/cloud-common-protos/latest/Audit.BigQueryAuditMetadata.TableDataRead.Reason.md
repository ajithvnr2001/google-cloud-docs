---
url: https://docs.cloud.google.com/php/docs/reference/cloud-common-protos/latest/Audit.BigQueryAuditMetadata.TableDataRead.Reason
title: Common Protos for Google Cloud APIs Client - Class Reason (1.0.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:15:19.656689+00:00
---

# Common Protos for Google Cloud APIs Client - Class Reason (1.0.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-common-protos/latest/Audit.BigQueryAuditMetadata.TableDataRead.Reason

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Common Protos for Google Cloud APIs Client - Class Reason (1.0.3) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.3 (latest)  1.0.0  0.8.3  0.7.0  0.6.0  0.5.2  0.4.2  0.3.8 

Reference documentation and code samples for the Common Protos for Google Cloud APIs Client class Reason.

Describes how the table data was read.

Protobuf type `google.cloud.audit.BigQueryAuditMetadata.TableDataRead.Reason`

## Namespace

Google \ Cloud \ Audit \ BigQueryAuditMetadata \ TableDataRead

## Methods 

### static::name

**Parameter**  
---  
**Name** | **Description**  
`value` |  `mixed`   
  
  
### static::value

**Parameter**  
---  
**Name** | **Description**  
`name` |  `mixed`   
  
  
## Constants 

### REASON_UNSPECIFIED
    
    
    Value: 0

Unknown.

Generated from protobuf enum `REASON_UNSPECIFIED = 0;`

### JOB
    
    
    Value: 1

Table was used as a source table during a BigQuery job.

Generated from protobuf enum `JOB = 1;`

### TABLEDATA_LIST_REQUEST
    
    
    Value: 2

Table data was accessed using the tabledata.list API.

Generated from protobuf enum `TABLEDATA_LIST_REQUEST = 2;`

### GET_QUERY_RESULTS_REQUEST
    
    
    Value: 3

Table data was accessed using the jobs.getQueryResults API.

Generated from protobuf enum `GET_QUERY_RESULTS_REQUEST = 3;`

### QUERY_REQUEST
    
    
    Value: 4

Table data was accessed using the jobs.query RPC.

Generated from protobuf enum `QUERY_REQUEST = 4;`

### CREATE_READ_SESSION
    
    
    Value: 5

Table data was accessed using storage.CreateReadSession API.

Generated from protobuf enum `CREATE_READ_SESSION = 5;`

### MATERIALIZED_VIEW_REFRESH
    
    
    Value: 6

Table data was accessed during a materialized view refresh.

Generated from protobuf enum `MATERIALIZED_VIEW_REFRESH = 6;`

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
