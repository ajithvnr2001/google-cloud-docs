---
url: https://docs.cloud.google.com/php/docs/reference/cloud-recommendations-ai/latest/V1beta1.ImportMetadata
title: Google Cloud Recommendation Engine V1beta1 Client - Class ImportMetadata (0.10.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:22:48.935443+00:00
---

# Google Cloud Recommendation Engine V1beta1 Client - Class ImportMetadata (0.10.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-recommendations-ai/latest/V1beta1.ImportMetadata

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Recommendation Engine V1beta1 Client - Class ImportMetadata (0.10.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.3 (latest)  0.9.3  0.8.2  0.7.7  0.6.4  0.5.0  0.4.12 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Recommendation Engine V1beta1 Client class ImportMetadata.

Metadata related to the progress of the Import operation. This will be returned by the google.longrunning.Operation.metadata field.

Generated from protobuf message `google.cloud.recommendationengine.v1beta1.ImportMetadata`

## Namespace

Google \ Cloud \ RecommendationEngine \ V1beta1

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ operation_name` |  `string`   
Name of the operation.  
`↳ request_id` |  `string`   
Id of the request / operation. This is parroting back the requestId that was passed in the request.  
`↳ create_time` |  `Google\Protobuf\Timestamp`   
Operation create time.  
`↳ success_count` |  `int|string`   
Count of entries that were processed successfully.  
`↳ failure_count` |  `int|string`   
Count of entries that encountered errors while processing.  
`↳ update_time` |  `Google\Protobuf\Timestamp`   
Operation last update time. If the operation is done, this is also the finish time.  
  
### getOperationName

Name of the operation.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setOperationName

Name of the operation.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getRequestId

Id of the request / operation. This is parroting back the requestId that was passed in the request.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setRequestId

Id of the request / operation. This is parroting back the requestId that was passed in the request.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCreateTime

Operation create time.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasCreateTime

### clearCreateTime

### setCreateTime

Operation create time.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSuccessCount

Count of entries that were processed successfully.

**Returns**  
---  
**Type** | **Description**  
`int|string` |   
  
### setSuccessCount

Count of entries that were processed successfully.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int|string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getFailureCount

Count of entries that encountered errors while processing.

**Returns**  
---  
**Type** | **Description**  
`int|string` |   
  
### setFailureCount

Count of entries that encountered errors while processing.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int|string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getUpdateTime

Operation last update time. If the operation is done, this is also the finish time.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasUpdateTime

### clearUpdateTime

### setUpdateTime

Operation last update time. If the operation is done, this is also the finish time.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
