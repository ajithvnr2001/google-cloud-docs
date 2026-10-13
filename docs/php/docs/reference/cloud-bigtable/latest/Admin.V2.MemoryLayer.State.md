---
url: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.MemoryLayer.State
title: Cloud Bigtable V2 Client - Class State (2.31.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:56:07.658532+00:00
---

# Cloud Bigtable V2 Client - Class State (2.31.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.MemoryLayer.State

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Bigtable V2 Client - Class State (2.31.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.31.0 (latest)  2.30.0  2.29.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.1  2.20.2  2.19.2  2.18.0  2.17.1  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.1  2.9.1  2.8.0  2.7.0  2.6.3  2.5.0  2.4.0  2.3.0  2.2.1  2.1.0  2.0.1  1.32.1  1.31.1  1.30.0  1.29.2  1.28.3  1.27.0  1.26.2  1.25.0  1.24.1  1.23.0  1.22.2  1.21.1  1.20.3 

Reference documentation and code samples for the Cloud Bigtable V2 Client class State.

Possible states of a memory layer.

Protobuf type `google.bigtable.admin.v2.MemoryLayer.State`

## Namespace

Google \ Cloud \ Bigtable \ Admin \ V2 \ MemoryLayer

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

### STATE_NOT_KNOWN
    
    
    Value: 0

The state of the memory layer could not be determined.

Generated from protobuf enum `STATE_NOT_KNOWN = 0;`

### READY
    
    
    Value: 1

The memory layer has been successfully enabled and is ready to serve requests.

Generated from protobuf enum `READY = 1;`

### ENABLING
    
    
    Value: 2

The memory layer is currently being enabled, and may be disabled if the enablement process encounters an error. A cluster may not be able to serve requests from the memory layer while being enabled.

Generated from protobuf enum `ENABLING = 2;`

### RESIZING
    
    
    Value: 3

The memory layer is currently being resized, and may revert to its previous storage size if the process encounters an error. The memory layer is still capable of serving requests while being resized, but may exhibit performance as if its number of allocated nodes is between the starting and requested states.

Generated from protobuf enum `RESIZING = 3;`

### DISABLED
    
    
    Value: 4

The memory layer is disabled. The default state for a cluster without a memory layer.

Generated from protobuf enum `DISABLED = 4;`

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
