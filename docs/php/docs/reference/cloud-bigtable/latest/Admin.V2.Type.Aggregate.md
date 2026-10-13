---
url: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.Aggregate
title: Cloud Bigtable V2 Client - Class Aggregate (2.31.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:55:55.810448+00:00
---

# Cloud Bigtable V2 Client - Class Aggregate (2.31.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.Aggregate

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Bigtable V2 Client - Class Aggregate (2.31.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.31.0 (latest)  2.30.0  2.29.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.1  2.20.2  2.19.2  2.18.0  2.17.1  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.1  2.9.1  2.8.0  2.7.0  2.6.3  2.5.0  2.4.0  2.3.0  2.2.1  2.1.0  2.0.1  1.32.1  1.31.1  1.30.0  1.29.2  1.28.3  1.27.0  1.26.2  1.25.0  1.24.1  1.23.0  1.22.2  1.21.1  1.20.3 

Reference documentation and code samples for the Cloud Bigtable V2 Client class Aggregate.

A value that combines incremental updates into a summarized value.

Data is never directly written or read using type `Aggregate`. Writes will provide either the `input_type` or `state_type`, and reads will always return the `state_type` .

Generated from protobuf message `google.bigtable.admin.v2.Type.Aggregate`

## Namespace

Google \ Cloud \ Bigtable \ Admin \ V2 \ Type

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ input_type` |  `[Type](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type)`   
Type of the inputs that are accumulated by this `Aggregate`, which must specify a full encoding. Use `AddInput` mutations to accumulate new inputs.  
`↳ state_type` |  `[Type](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type)`   
Output only. Type that holds the internal accumulator state for the `Aggregate`. This is a function of the `input_type` and `aggregator` chosen, and will always specify a full encoding.  
`↳ sum` |  `[Aggregate\Sum](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.Aggregate.Sum)`   
Sum aggregator.  
`↳ hllpp_unique_count` |  `[Aggregate\HyperLogLogPlusPlusUniqueCount](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.Aggregate.HyperLogLogPlusPlusUniqueCount)`   
HyperLogLogPlusPlusUniqueCount aggregator.  
`↳ max` |  `[Aggregate\Max](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.Aggregate.Max)`   
Max aggregator.  
`↳ min` |  `[Aggregate\Min](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.Aggregate.Min)`   
Min aggregator.  
  
### getInputType

Type of the inputs that are accumulated by this `Aggregate`, which must specify a full encoding.

Use `AddInput` mutations to accumulate new inputs.

**Returns**  
---  
**Type** | **Description**  
`[Type](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type)|null` |   
  
### hasInputType

### clearInputType

### setInputType

Type of the inputs that are accumulated by this `Aggregate`, which must specify a full encoding.

Use `AddInput` mutations to accumulate new inputs.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Type](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getStateType

Output only. Type that holds the internal accumulator state for the `Aggregate`. This is a function of the `input_type` and `aggregator` chosen, and will always specify a full encoding.

**Returns**  
---  
**Type** | **Description**  
`[Type](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type)|null` |   
  
### hasStateType

### clearStateType

### setStateType

Output only. Type that holds the internal accumulator state for the `Aggregate`. This is a function of the `input_type` and `aggregator` chosen, and will always specify a full encoding.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Type](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSum

Sum aggregator.

**Returns**  
---  
**Type** | **Description**  
`[Aggregate\Sum](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.Aggregate.Sum)|null` |   
  
### hasSum

### setSum

Sum aggregator.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Aggregate\Sum](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.Aggregate.Sum)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getHllppUniqueCount

HyperLogLogPlusPlusUniqueCount aggregator.

**Returns**  
---  
**Type** | **Description**  
`[Aggregate\HyperLogLogPlusPlusUniqueCount](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.Aggregate.HyperLogLogPlusPlusUniqueCount)|null` |   
  
### hasHllppUniqueCount

### setHllppUniqueCount

HyperLogLogPlusPlusUniqueCount aggregator.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Aggregate\HyperLogLogPlusPlusUniqueCount](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.Aggregate.HyperLogLogPlusPlusUniqueCount)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getMax

Max aggregator.

**Returns**  
---  
**Type** | **Description**  
`[Aggregate\Max](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.Aggregate.Max)|null` |   
  
### hasMax

### setMax

Max aggregator.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Aggregate\Max](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.Aggregate.Max)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getMin

Min aggregator.

**Returns**  
---  
**Type** | **Description**  
`[Aggregate\Min](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.Aggregate.Min)|null` |   
  
### hasMin

### setMin

Min aggregator.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Aggregate\Min](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.Aggregate.Min)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getAggregator

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
