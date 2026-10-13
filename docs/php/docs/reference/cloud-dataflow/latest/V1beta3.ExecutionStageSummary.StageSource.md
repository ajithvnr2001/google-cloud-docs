---
url: https://docs.cloud.google.com/php/docs/reference/cloud-dataflow/latest/V1beta3.ExecutionStageSummary.StageSource
title: Google Cloud Dataflow V1beta3 Client - Class StageSource (0.11.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:09:38.772202+00:00
---

# Google Cloud Dataflow V1beta3 Client - Class StageSource (0.11.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-dataflow/latest/V1beta3.ExecutionStageSummary.StageSource

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Dataflow V1beta3 Client - Class StageSource (0.11.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.11.3 (latest)  0.10.0  0.9.3  0.8.2  0.7.1  0.6.6  0.5.1  0.4.1  0.3.10 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Dataflow V1beta3 Client class StageSource.

Description of an input or output of an execution stage.

Generated from protobuf message `google.dataflow.v1beta3.ExecutionStageSummary.StageSource`

## Namespace

Google \ Cloud \ Dataflow \ V1beta3 \ ExecutionStageSummary

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ user_name` |  `string`   
Human-readable name for this source; may be user or system generated.  
`↳ name` |  `string`   
Dataflow service generated name for this source.  
`↳ original_transform_or_collection` |  `string`   
User name for the original user transform or collection with which this source is most closely associated.  
`↳ size_bytes` |  `int|string`   
Size of the source, if measurable.  
  
### getUserName

Human-readable name for this source; may be user or system generated.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setUserName

Human-readable name for this source; may be user or system generated.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getName

Dataflow service generated name for this source.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

Dataflow service generated name for this source.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getOriginalTransformOrCollection

User name for the original user transform or collection with which this source is most closely associated.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setOriginalTransformOrCollection

User name for the original user transform or collection with which this source is most closely associated.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSizeBytes

Size of the source, if measurable.

**Returns**  
---  
**Type** | **Description**  
`int|string` |   
  
### setSizeBytes

Size of the source, if measurable.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int|string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
