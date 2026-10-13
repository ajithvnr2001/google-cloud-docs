---
url: https://docs.cloud.google.com/php/docs/reference/cloud-assured-workloads/latest/V1beta1.Workload.SaaEnrollmentResponse
title: Google Cloud Assured Workloads V1beta1 Client - Class SaaEnrollmentResponse (1.2.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:48:47.553494+00:00
---

# Google Cloud Assured Workloads V1beta1 Client - Class SaaEnrollmentResponse (1.2.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-assured-workloads/latest/V1beta1.Workload.SaaEnrollmentResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Assured Workloads V1beta1 Client - Class SaaEnrollmentResponse (1.2.3) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.3 (latest)  1.1.3  1.0.5  0.11.5  0.10.2  0.9.1  0.8.3  0.7.3 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Assured Workloads V1beta1 Client class SaaEnrollmentResponse.

Signed Access Approvals (SAA) enrollment response.

Generated from protobuf message `google.cloud.assuredworkloads.v1beta1.Workload.SaaEnrollmentResponse`

## Namespace

Google \ Cloud \ AssuredWorkloads \ V1beta1 \ Workload

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ setup_status` |  `int`   
Indicates SAA enrollment status of a given workload.  
`↳ setup_errors` |  `int[]`   
Indicates SAA enrollment setup error if any.  
  
### getSetupStatus

Indicates SAA enrollment status of a given workload.

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### hasSetupStatus

### clearSetupStatus

### setSetupStatus

Indicates SAA enrollment status of a given workload.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSetupErrors

Indicates SAA enrollment setup error if any.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<int>` |   
  
### setSetupErrors

Indicates SAA enrollment setup error if any.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int[]`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
