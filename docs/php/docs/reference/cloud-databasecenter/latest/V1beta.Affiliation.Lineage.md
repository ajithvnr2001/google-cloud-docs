---
url: https://docs.cloud.google.com/php/docs/reference/cloud-databasecenter/latest/V1beta.Affiliation.Lineage
title: Google Cloud Database Center V1beta Client - Class Lineage (0.8.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:31:21.182481+00:00
---

# Google Cloud Database Center V1beta Client - Class Lineage (0.8.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-databasecenter/latest/V1beta.Affiliation.Lineage

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Database Center V1beta Client - Class Lineage (0.8.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.3 (latest)  0.7.0  0.6.0  0.5.0  0.4.1  0.3.1  0.2.0  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Database Center V1beta Client class Lineage.

lineage information of the affiliated resources This captures source, target and process which created the lineage.

Generated from protobuf message `google.cloud.databasecenter.v1beta.Affiliation.Lineage`

## Namespace

Google \ Cloud \ DatabaseCenter \ V1beta \ Affiliation

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ source_fqn` |  `string`   
Optional. FQN of source table / column  
`↳ target_fqn` |  `string`   
Optional. FQN of target table / column  
`↳ process_fqn` |  `string`   
Optional. FQN of process which created the lineage i.e. dataplex, datastream etc.  
`↳ process_type` |  `int`   
Optional. Type of process which created the lineage.  
  
### getSourceFqn

Optional. FQN of source table / column

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setSourceFqn

Optional. FQN of source table / column

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getTargetFqn

Optional. FQN of target table / column

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setTargetFqn

Optional. FQN of target table / column

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getProcessFqn

Optional. FQN of process which created the lineage i.e. dataplex, datastream etc.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setProcessFqn

Optional. FQN of process which created the lineage i.e. dataplex, datastream etc.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getProcessType

Optional. Type of process which created the lineage.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [ProcessType](https://docs.cloud.google.com/php/docs/reference/cloud-databasecenter/latest/V1beta.Affiliation.ProcessType).  
  
### setProcessType

Optional. Type of process which created the lineage.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [ProcessType](https://docs.cloud.google.com/php/docs/reference/cloud-databasecenter/latest/V1beta.Affiliation.ProcessType).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
