---
url: https://docs.cloud.google.com/php/docs/reference/cloud-cloudcontrolspartner/latest/V1beta.Violation.Remediation
title: Google Cloud Cloud Controls Partner V1beta Client - Class Remediation (0.6.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:12:45.364653+00:00
---

# Google Cloud Cloud Controls Partner V1beta Client - Class Remediation (0.6.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-cloudcontrolspartner/latest/V1beta.Violation.Remediation

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Cloud Controls Partner V1beta Client - Class Remediation (0.6.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.3 (latest)  0.5.3  0.4.1  0.3.0  0.2.2  0.1.4 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Cloud Controls Partner V1beta Client class Remediation.

Represents remediation guidance to resolve compliance violation for AssuredWorkload

Generated from protobuf message `google.cloud.cloudcontrolspartner.v1beta.Violation.Remediation`

## Namespace

Google \ Cloud \ CloudControlsPartner \ V1beta \ Violation

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ instructions` |  `[Remediation\Instructions](https://docs.cloud.google.com/php/docs/reference/cloud-cloudcontrolspartner/latest/V1beta.Violation.Remediation.Instructions)`   
Required. Remediation instructions to resolve violations  
`↳ compliant_values` |  `string[]`   
Values that can resolve the violation For example: for list org policy violations, this will either be the list of allowed or denied values  
`↳ remediation_type` |  `int`   
Output only. Remediation type based on the type of org policy values violated  
  
### getInstructions

Required. Remediation instructions to resolve violations

**Returns**  
---  
**Type** | **Description**  
`[Remediation\Instructions](https://docs.cloud.google.com/php/docs/reference/cloud-cloudcontrolspartner/latest/V1beta.Violation.Remediation.Instructions)|null` |   
  
### hasInstructions

### clearInstructions

### setInstructions

Required. Remediation instructions to resolve violations

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Remediation\Instructions](https://docs.cloud.google.com/php/docs/reference/cloud-cloudcontrolspartner/latest/V1beta.Violation.Remediation.Instructions)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCompliantValues

Values that can resolve the violation For example: for list org policy violations, this will either be the list of allowed or denied values

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<string>` |   
  
### setCompliantValues

Values that can resolve the violation For example: for list org policy violations, this will either be the list of allowed or denied values

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string[]`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getRemediationType

Output only. Remediation type based on the type of org policy values violated

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [RemediationType](https://docs.cloud.google.com/php/docs/reference/cloud-cloudcontrolspartner/latest/V1beta.Violation.Remediation.RemediationType).  
  
### setRemediationType

Output only. Remediation type based on the type of org policy values violated

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [RemediationType](https://docs.cloud.google.com/php/docs/reference/cloud-cloudcontrolspartner/latest/V1beta.Violation.Remediation.RemediationType).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
