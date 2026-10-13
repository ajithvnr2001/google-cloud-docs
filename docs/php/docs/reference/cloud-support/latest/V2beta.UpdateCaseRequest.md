---
url: https://docs.cloud.google.com/php/docs/reference/cloud-support/latest/V2beta.UpdateCaseRequest
title: Google Cloud Support V2beta Client - Class UpdateCaseRequest (1.8.5) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:57:16.907111+00:00
---

# Google Cloud Support V2beta Client - Class UpdateCaseRequest (1.8.5)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-support/latest/V2beta.UpdateCaseRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Support V2beta Client - Class UpdateCaseRequest (1.8.5) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.5 (latest)  1.7.0  1.6.0  1.5.0  1.4.2  1.3.0  1.2.1  1.1.0  1.0.3  0.2.5  0.1.2 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Support V2beta Client class UpdateCaseRequest.

The request message for the UpdateCase endpoint

Generated from protobuf message `google.cloud.support.v2beta.UpdateCaseRequest`

## Namespace

Google \ Cloud \ Support \ V2beta

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ case` |  `[PBCase](https://docs.cloud.google.com/php/docs/reference/cloud-support/latest/V2beta.PBCase)`   
Required. The case to update.  
`↳ update_mask` |  `Google\Protobuf\FieldMask`   
A list of attributes of the case that should be updated. Supported values are `priority`, `display_name`, and `subscriber_email_addresses`. If no fields are specified, all supported fields are updated. Be careful - if you do not provide a field mask, then you might accidentally clear some fields. For example, if you leave the field mask empty and do not provide a value for `subscriber_email_addresses`, then `subscriber_email_addresses` is updated to empty.  
  
### getCase

Required. The case to update.

**Returns**  
---  
**Type** | **Description**  
`[PBCase](https://docs.cloud.google.com/php/docs/reference/cloud-support/latest/V2beta.PBCase)|null` |   
  
### hasCase

### clearCase

### setCase

Required. The case to update.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[PBCase](https://docs.cloud.google.com/php/docs/reference/cloud-support/latest/V2beta.PBCase)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getUpdateMask

A list of attributes of the case that should be updated. Supported values are `priority`, `display_name`, and `subscriber_email_addresses`. If no fields are specified, all supported fields are updated.

Be careful - if you do not provide a field mask, then you might accidentally clear some fields. For example, if you leave the field mask empty and do not provide a value for `subscriber_email_addresses`, then `subscriber_email_addresses` is updated to empty.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\FieldMask|null` |   
  
### hasUpdateMask

### clearUpdateMask

### setUpdateMask

A list of attributes of the case that should be updated. Supported values are `priority`, `display_name`, and `subscriber_email_addresses`. If no fields are specified, all supported fields are updated.

Be careful - if you do not provide a field mask, then you might accidentally clear some fields. For example, if you leave the field mask empty and do not provide a value for `subscriber_email_addresses`, then `subscriber_email_addresses` is updated to empty.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\FieldMask`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### static::build

**Parameters**  
---  
**Name** | **Description**  
`case` |  `[PBCase](https://docs.cloud.google.com/php/docs/reference/cloud-support/latest/V2beta.PBCase)`   
Required. The case to update.  
`updateMask` |  `Google\Protobuf\FieldMask`   
A list of attributes of the case that should be updated. Supported values are `priority`, `display_name`, and `subscriber_email_addresses`. If no fields are specified, all supported fields are updated. Be careful - if you do not provide a field mask, then you might accidentally clear some fields. For example, if you leave the field mask empty and do not provide a value for `subscriber_email_addresses`, then `subscriber_email_addresses` is updated to empty.  
**Returns**  
---  
**Type** | **Description**  
`[UpdateCaseRequest](https://docs.cloud.google.com/php/docs/reference/cloud-support/latest/V2beta.UpdateCaseRequest)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
