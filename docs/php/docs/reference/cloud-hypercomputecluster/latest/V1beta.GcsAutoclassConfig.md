---
url: https://docs.cloud.google.com/php/docs/reference/cloud-hypercomputecluster/latest/V1beta.GcsAutoclassConfig
title: Google Cloud Hypercompute Cluster V1beta Client - Class GcsAutoclassConfig (0.4.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:33:17.414701+00:00
---

# Google Cloud Hypercompute Cluster V1beta Client - Class GcsAutoclassConfig (0.4.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-hypercomputecluster/latest/V1beta.GcsAutoclassConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Hypercompute Cluster V1beta Client - Class GcsAutoclassConfig (0.4.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.4.3 (latest)  0.3.1  0.2.0  0.1.1 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Hypercompute Cluster V1beta Client class GcsAutoclassConfig.

Message describing Google Cloud Storage autoclass configuration

Generated from protobuf message `google.cloud.hypercomputecluster.v1beta.GcsAutoclassConfig`

## Namespace

Google \ Cloud \ HypercomputeCluster \ V1beta

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ enabled` |  `bool`   
Required. Enables Auto-class feature.  
`↳ terminal_storage_class` |  `int`   
Optional. Terminal storage class of the autoclass bucket  
  
### getEnabled

Required. Enables Auto-class feature.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setEnabled

Required. Enables Auto-class feature.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getTerminalStorageClass

Optional. Terminal storage class of the autoclass bucket

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [TerminalStorageClass](https://docs.cloud.google.com/php/docs/reference/cloud-hypercomputecluster/latest/V1beta.GcsAutoclassConfig.TerminalStorageClass).  
  
### setTerminalStorageClass

Optional. Terminal storage class of the autoclass bucket

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [TerminalStorageClass](https://docs.cloud.google.com/php/docs/reference/cloud-hypercomputecluster/latest/V1beta.GcsAutoclassConfig.TerminalStorageClass).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
