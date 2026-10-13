---
url: https://docs.cloud.google.com/php/docs/reference/cloud-support/latest/V2beta.FeedItem
title: Google Cloud Support V2beta Client - Class FeedItem (1.8.5) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:52:50.147858+00:00
---

# Google Cloud Support V2beta Client - Class FeedItem (1.8.5)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-support/latest/V2beta.FeedItem

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Support V2beta Client - Class FeedItem (1.8.5) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.5 (latest)  1.7.0  1.6.0  1.5.0  1.4.2  1.3.0  1.2.1  1.1.0  1.0.3  0.2.5  0.1.2 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Support V2beta Client class FeedItem.

A feed item associated with a support case.

Generated from protobuf message `google.cloud.support.v2beta.FeedItem`

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
`↳ comment` |  `[Comment](https://docs.cloud.google.com/php/docs/reference/cloud-support/latest/V2beta.Comment)`   
Output only. A comment added to the case.  
`↳ attachment` |  `[Attachment](https://docs.cloud.google.com/php/docs/reference/cloud-support/latest/V2beta.Attachment)`   
Output only. An attachment attached to the case.  
`↳ email_message` |  `[EmailMessage](https://docs.cloud.google.com/php/docs/reference/cloud-support/latest/V2beta.EmailMessage)`   
Output only. An email message received in reply to the case.  
`↳ deleted_attachment` |  `[Attachment](https://docs.cloud.google.com/php/docs/reference/cloud-support/latest/V2beta.Attachment)`   
Output only. A deleted attachment that used to be associated with the support case.  
`↳ event_time` |  `Google\Protobuf\Timestamp`   
Output only. Time corresponding to the event of this item.  
  
### getComment

Output only. A comment added to the case.

**Returns**  
---  
**Type** | **Description**  
`[Comment](https://docs.cloud.google.com/php/docs/reference/cloud-support/latest/V2beta.Comment)|null` |   
  
### hasComment

### setComment

Output only. A comment added to the case.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Comment](https://docs.cloud.google.com/php/docs/reference/cloud-support/latest/V2beta.Comment)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getAttachment

Output only. An attachment attached to the case.

**Returns**  
---  
**Type** | **Description**  
`[Attachment](https://docs.cloud.google.com/php/docs/reference/cloud-support/latest/V2beta.Attachment)|null` |   
  
### hasAttachment

### setAttachment

Output only. An attachment attached to the case.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Attachment](https://docs.cloud.google.com/php/docs/reference/cloud-support/latest/V2beta.Attachment)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEmailMessage

Output only. An email message received in reply to the case.

**Returns**  
---  
**Type** | **Description**  
`[EmailMessage](https://docs.cloud.google.com/php/docs/reference/cloud-support/latest/V2beta.EmailMessage)|null` |   
  
### hasEmailMessage

### setEmailMessage

Output only. An email message received in reply to the case.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[EmailMessage](https://docs.cloud.google.com/php/docs/reference/cloud-support/latest/V2beta.EmailMessage)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDeletedAttachment

Output only. A deleted attachment that used to be associated with the support case.

**Returns**  
---  
**Type** | **Description**  
`[Attachment](https://docs.cloud.google.com/php/docs/reference/cloud-support/latest/V2beta.Attachment)|null` |   
  
### hasDeletedAttachment

### setDeletedAttachment

Output only. A deleted attachment that used to be associated with the support case.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Attachment](https://docs.cloud.google.com/php/docs/reference/cloud-support/latest/V2beta.Attachment)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEventTime

Output only. Time corresponding to the event of this item.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasEventTime

### clearEventTime

### setEventTime

Output only. Time corresponding to the event of this item.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEventObject

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
