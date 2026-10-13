---
url: https://docs.cloud.google.com/php/docs/reference/cloud-dataflow/latest/V1beta3.JobType
title: Google Cloud Dataflow V1beta3 Client - Class JobType (0.11.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:14:15.989703+00:00
---

# Google Cloud Dataflow V1beta3 Client - Class JobType (0.11.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-dataflow/latest/V1beta3.JobType

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Dataflow V1beta3 Client - Class JobType (0.11.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.11.3 (latest)  0.10.0  0.9.3  0.8.2  0.7.1  0.6.6  0.5.1  0.4.1  0.3.10 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Dataflow V1beta3 Client class JobType.

Specifies the processing model used by a [google.dataflow.v1beta3.Job], which determines the way the Job is managed by the Cloud Dataflow service (how workers are scheduled, how inputs are sharded, etc).

Protobuf type `google.dataflow.v1beta3.JobType`

## Namespace

Google \ Cloud \ Dataflow \ V1beta3

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

### JOB_TYPE_UNKNOWN
    
    
    Value: 0

The type of the job is unspecified, or unknown.

Generated from protobuf enum `JOB_TYPE_UNKNOWN = 0;`

### JOB_TYPE_BATCH
    
    
    Value: 1

A batch job with a well-defined end point: data is read, data is processed, data is written, and the job is done.

Generated from protobuf enum `JOB_TYPE_BATCH = 1;`

### JOB_TYPE_STREAMING
    
    
    Value: 2

A continuously streaming job with no end: data is read, processed, and written continuously.

Generated from protobuf enum `JOB_TYPE_STREAMING = 2;`

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
