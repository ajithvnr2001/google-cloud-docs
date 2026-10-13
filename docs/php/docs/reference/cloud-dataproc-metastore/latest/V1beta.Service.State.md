---
url: https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Service.State
title: Google Cloud Dataproc Metastore V1beta Client - Class State (1.3.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:51:24.928723+00:00
---

# Google Cloud Dataproc Metastore V1beta Client - Class State (1.3.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Service.State

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Dataproc Metastore V1beta Client - Class State (1.3.3) Stay organized with collections  Save and categorize content based on your preferences. 

1.3.3 (latest)  1.2.4  1.1.1  1.0.4  0.11.5  0.10.2  0.9.0  0.8.1  0.7.0  0.6.1  0.5.1  0.4.1 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Dataproc Metastore V1beta Client class State.

The current state of the metastore service.

Protobuf type `google.cloud.metastore.v1beta.Service.State`

## Namespace

Google \ Cloud \ Metastore \ V1beta \ Service

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

### STATE_UNSPECIFIED
    
    
    Value: 0

The state of the metastore service is unknown.

Generated from protobuf enum `STATE_UNSPECIFIED = 0;`

### CREATING
    
    
    Value: 1

The metastore service is in the process of being created.

Generated from protobuf enum `CREATING = 1;`

### ACTIVE
    
    
    Value: 2

The metastore service is running and ready to serve queries.

Generated from protobuf enum `ACTIVE = 2;`

### SUSPENDING
    
    
    Value: 3

The metastore service is entering suspension. Its query-serving availability may cease unexpectedly.

Generated from protobuf enum `SUSPENDING = 3;`

### SUSPENDED
    
    
    Value: 4

The metastore service is suspended and unable to serve queries.

Generated from protobuf enum `SUSPENDED = 4;`

### UPDATING
    
    
    Value: 5

The metastore service is being updated. It remains usable but cannot accept additional update requests or be deleted at this time.

Generated from protobuf enum `UPDATING = 5;`

### DELETING
    
    
    Value: 6

The metastore service is undergoing deletion. It cannot be used.

Generated from protobuf enum `DELETING = 6;`

### ERROR
    
    
    Value: 7

The metastore service has encountered an error and cannot be used. The metastore service should be deleted.

Generated from protobuf enum `ERROR = 7;`

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
