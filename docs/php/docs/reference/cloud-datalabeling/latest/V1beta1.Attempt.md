---
url: https://docs.cloud.google.com/php/docs/reference/cloud-datalabeling/latest/V1beta1.Attempt
title: Google Cloud Datalabeling V1beta1 Client - Class Attempt (0.8.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:32:55.557548+00:00
---

# Google Cloud Datalabeling V1beta1 Client - Class Attempt (0.8.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-datalabeling/latest/V1beta1.Attempt

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Datalabeling V1beta1 Client - Class Attempt (0.8.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.3 (latest)  0.7.2  0.6.3  0.5.7  0.4.2  0.3.1  0.2.0  0.1.14 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Datalabeling V1beta1 Client class Attempt.

Records a failed evaluation job run.

Generated from protobuf message `google.cloud.datalabeling.v1beta1.Attempt`

## Namespace

Google \ Cloud \ DataLabeling \ V1beta1

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ attempt_time` |  `Google\Protobuf\Timestamp`   
  
`↳ partial_failures` |  `array<[Google\Rpc\Status](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Rpc.Status.html)>`   
Details of errors that occurred.  
  
### getAttemptTime

Generated from protobuf field `.google.protobuf.Timestamp attempt_time = 1;`

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasAttemptTime

### clearAttemptTime

### setAttemptTime

Generated from protobuf field `.google.protobuf.Timestamp attempt_time = 1;`

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPartialFailures

Details of errors that occurred.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<[Google\Rpc\Status](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Rpc.Status.html)>` |   
  
### setPartialFailures

Details of errors that occurred.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array<[Google\Rpc\Status](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Rpc.Status.html)>`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
