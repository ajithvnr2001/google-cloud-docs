---
url: https://docs.cloud.google.com/php/docs/reference/cloud-common-protos/latest/Audit.BigQueryAuditMetadata.Model
title: Common Protos for Google Cloud APIs Client - Class Model (1.0.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:48:03.202997+00:00
---

# Common Protos for Google Cloud APIs Client - Class Model (1.0.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-common-protos/latest/Audit.BigQueryAuditMetadata.Model

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Common Protos for Google Cloud APIs Client - Class Model (1.0.3) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.3 (latest)  1.0.0  0.8.3  0.7.0  0.6.0  0.5.2  0.4.2  0.3.8 

Reference documentation and code samples for the Common Protos for Google Cloud APIs Client class Model.

Trained BigQuery ML model.

Generated from protobuf message `google.cloud.audit.BigQueryAuditMetadata.Model`

## Namespace

Google \ Cloud \ Audit \ BigQueryAuditMetadata

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ model_name` |  `string`   
Model URI. Format: `projects/<project_id>/datasets/<dataset_id>/models/<model_id>`.  
`↳ model_info` |  `[EntityInfo](https://docs.cloud.google.com/php/docs/reference/cloud-common-protos/latest/Audit.BigQueryAuditMetadata.EntityInfo)`   
User-provided metadata for the model.  
`↳ expire_time` |  `[Google\Protobuf\Timestamp](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Timestamp.html)`   
Model expiration time.  
`↳ create_time` |  `[Google\Protobuf\Timestamp](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Timestamp.html)`   
Model creation time.  
`↳ update_time` |  `[Google\Protobuf\Timestamp](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Timestamp.html)`   
Model last update time.  
`↳ encryption` |  `[EncryptionInfo](https://docs.cloud.google.com/php/docs/reference/cloud-common-protos/latest/Audit.BigQueryAuditMetadata.EncryptionInfo)`   
Model encryption information. Set when non-default encryption is used.  
  
### getModelName

Model URI.

Format: `projects/<project_id>/datasets/<dataset_id>/models/<model_id>`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setModelName

Model URI.

Format: `projects/<project_id>/datasets/<dataset_id>/models/<model_id>`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getModelInfo

User-provided metadata for the model.

**Returns**  
---  
**Type** | **Description**  
`[EntityInfo](https://docs.cloud.google.com/php/docs/reference/cloud-common-protos/latest/Audit.BigQueryAuditMetadata.EntityInfo)|null` |   
  
### hasModelInfo

### clearModelInfo

### setModelInfo

User-provided metadata for the model.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[EntityInfo](https://docs.cloud.google.com/php/docs/reference/cloud-common-protos/latest/Audit.BigQueryAuditMetadata.EntityInfo)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getExpireTime

Model expiration time.

**Returns**  
---  
**Type** | **Description**  
`[Google\Protobuf\Timestamp](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Timestamp.html)|null` |   
  
### hasExpireTime

### clearExpireTime

### setExpireTime

Model expiration time.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Protobuf\Timestamp](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Timestamp.html)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCreateTime

Model creation time.

**Returns**  
---  
**Type** | **Description**  
`[Google\Protobuf\Timestamp](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Timestamp.html)|null` |   
  
### hasCreateTime

### clearCreateTime

### setCreateTime

Model creation time.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Protobuf\Timestamp](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Timestamp.html)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getUpdateTime

Model last update time.

**Returns**  
---  
**Type** | **Description**  
`[Google\Protobuf\Timestamp](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Timestamp.html)|null` |   
  
### hasUpdateTime

### clearUpdateTime

### setUpdateTime

Model last update time.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Protobuf\Timestamp](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Timestamp.html)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEncryption

Model encryption information. Set when non-default encryption is used.

**Returns**  
---  
**Type** | **Description**  
`[EncryptionInfo](https://docs.cloud.google.com/php/docs/reference/cloud-common-protos/latest/Audit.BigQueryAuditMetadata.EncryptionInfo)|null` |   
  
### hasEncryption

### clearEncryption

### setEncryption

Model encryption information. Set when non-default encryption is used.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[EncryptionInfo](https://docs.cloud.google.com/php/docs/reference/cloud-common-protos/latest/Audit.BigQueryAuditMetadata.EncryptionInfo)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
