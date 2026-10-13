---
url: https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/V1beta1.TransactionOptions
title: Cloud Firestore V1beta1 Client - Class TransactionOptions (2.2.0-RC1) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:12:34.230052+00:00
---

# Cloud Firestore V1beta1 Client - Class TransactionOptions (2.2.0-RC1)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/V1beta1.TransactionOptions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Firestore V1beta1 Client - Class TransactionOptions (2.2.0-RC1) Stay organized with collections  Save and categorize content based on your preferences. 

2.3.3 (latest)  2.2.0-RC1  2.1.0  2.0.2-RC1  1.55.0  1.54.4  1.53.1  1.52.0  1.51.0  1.50.0  1.48.1  1.47.3  1.46.0  1.45.2  1.44.1  1.43.3  1.40.0  1.39.0  1.38.0  1.37.7  1.36.1  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.28.0  1.27.3 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Cloud Firestore V1beta1 Client class TransactionOptions.

Options for creating a new transaction.

Generated from protobuf message `google.firestore.v1beta1.TransactionOptions`

## Namespace

Google \ Cloud \ Firestore \ V1beta1

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ read_only` |  `[TransactionOptions\PBReadOnly](https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/V1beta1.TransactionOptions.PBReadOnly)`   
The transaction can only be used for read operations.  
`↳ read_write` |  `[TransactionOptions\ReadWrite](https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/V1beta1.TransactionOptions.ReadWrite)`   
The transaction can be used for both read and write operations.  
  
### getReadOnly

The transaction can only be used for read operations.

**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions\PBReadOnly](https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/V1beta1.TransactionOptions.PBReadOnly)|null` |   
  
### hasReadOnly

### setReadOnly

The transaction can only be used for read operations.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[TransactionOptions\PBReadOnly](https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/V1beta1.TransactionOptions.PBReadOnly)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getReadWrite

The transaction can be used for both read and write operations.

**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions\ReadWrite](https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/V1beta1.TransactionOptions.ReadWrite)|null` |   
  
### hasReadWrite

### setReadWrite

The transaction can be used for both read and write operations.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[TransactionOptions\ReadWrite](https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/V1beta1.TransactionOptions.ReadWrite)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getMode

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
