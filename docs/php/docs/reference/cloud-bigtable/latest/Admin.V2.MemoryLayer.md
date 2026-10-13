---
url: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.MemoryLayer
title: Cloud Bigtable V2 Client - Class MemoryLayer (2.31.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:55:51.758472+00:00
---

# Cloud Bigtable V2 Client - Class MemoryLayer (2.31.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.MemoryLayer

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Bigtable V2 Client - Class MemoryLayer (2.31.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.31.0 (latest)  2.30.0  2.29.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.1  2.20.2  2.19.2  2.18.0  2.17.1  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.1  2.9.1  2.8.0  2.7.0  2.6.3  2.5.0  2.4.0  2.3.0  2.2.1  2.1.0  2.0.1  1.32.1  1.31.1  1.30.0  1.29.2  1.28.3  1.27.0  1.26.2  1.25.0  1.24.1  1.23.0  1.22.2  1.21.1  1.20.3 

Reference documentation and code samples for the Cloud Bigtable V2 Client class MemoryLayer.

The memory layer of a cluster. A memory layer serves reads from memory without hitting the backing persistent data store.

Generated from protobuf message `google.bigtable.admin.v2.MemoryLayer`

## Namespace

Google \ Cloud \ Bigtable \ Admin \ V2

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ name` |  `string`   
Identifier. Name of the memory layer. This is always: "projects/{project}/instances/{instance}/clusters/{cluster}/memoryLayer".  
`↳ memory_config` |  `[MemoryLayer\MemoryConfig](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.MemoryLayer.MemoryConfig)`   
The configuration of this memory layer. Set an empty `memory_config` to enable the memory layer. Unset this to disable the memory layer.  
`↳ etag` |  `string`   
Optional. The etag for this memory layer. This may be sent on update requests to ensure that the client has an up-to-date value before proceeding. The server returns an ABORTED error on a mismatched etag.  
`↳ state` |  `int`   
Output only. The current state of the memory layer.  
  
### getName

Identifier. Name of the memory layer. This is always: "projects/{project}/instances/{instance}/clusters/{cluster}/memoryLayer".

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

Identifier. Name of the memory layer. This is always: "projects/{project}/instances/{instance}/clusters/{cluster}/memoryLayer".

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getMemoryConfig

The configuration of this memory layer. Set an empty `memory_config` to enable the memory layer. Unset this to disable the memory layer.

**Returns**  
---  
**Type** | **Description**  
`[MemoryLayer\MemoryConfig](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.MemoryLayer.MemoryConfig)|null` |   
  
### hasMemoryConfig

### clearMemoryConfig

### setMemoryConfig

The configuration of this memory layer. Set an empty `memory_config` to enable the memory layer. Unset this to disable the memory layer.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[MemoryLayer\MemoryConfig](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.MemoryLayer.MemoryConfig)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEtag

Optional. The etag for this memory layer.

This may be sent on update requests to ensure that the client has an up-to-date value before proceeding. The server returns an ABORTED error on a mismatched etag.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setEtag

Optional. The etag for this memory layer.

This may be sent on update requests to ensure that the client has an up-to-date value before proceeding. The server returns an ABORTED error on a mismatched etag.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getState

Output only. The current state of the memory layer.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [State](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.MemoryLayer.State).  
  
### setState

Output only. The current state of the memory layer.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [State](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.MemoryLayer.State).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
