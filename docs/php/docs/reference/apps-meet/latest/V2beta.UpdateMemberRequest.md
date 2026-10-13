---
url: https://docs.cloud.google.com/php/docs/reference/apps-meet/latest/V2beta.UpdateMemberRequest
title: Google Apps Meet V2beta Client - Class UpdateMemberRequest (0.7.1) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:44:22.104110+00:00
---

# Google Apps Meet V2beta Client - Class UpdateMemberRequest (0.7.1)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/apps-meet/latest/V2beta.UpdateMemberRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Apps Meet V2beta Client - Class UpdateMemberRequest (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.1 (latest)  0.5.4  0.4.1  0.3.0  0.2.6  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Apps Meet V2beta Client class UpdateMemberRequest.

Request to update a member.

Generated from protobuf message `google.apps.meet.v2beta.UpdateMemberRequest`

## Namespace

Google \ Apps \ Meet \ V2beta

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ member` |  `[Member](https://docs.cloud.google.com/php/docs/reference/apps-meet/latest/V2beta.Member)`   
Required. The Member to update. Format: spaces/{space}/members/{member}  
`↳ update_mask` |  `Google\Protobuf\FieldMask`   
Optional. Field mask used to specify the fields to be updated in the member. If update_mask isn't provided(not set, set with empty paths, or only has "" as paths), it defaults to update all fields provided with values in the request. Using "*" as update_mask will update all fields, including deleting fields not set in the request. In case of BatchUpdate, it must be absent or the same as the update_mask in BatchUpdateMembersRequest when UpdateMemberRequest is built as a child request of BatchUpdateMembersRequest.  
  
### getMember

Required. The Member to update.

Format: spaces/{space}/members/{member}

**Returns**  
---  
**Type** | **Description**  
`[Member](https://docs.cloud.google.com/php/docs/reference/apps-meet/latest/V2beta.Member)|null` |   
  
### hasMember

### clearMember

### setMember

Required. The Member to update.

Format: spaces/{space}/members/{member}

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Member](https://docs.cloud.google.com/php/docs/reference/apps-meet/latest/V2beta.Member)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getUpdateMask

Optional. Field mask used to specify the fields to be updated in the member. If update_mask isn't provided(not set, set with empty paths, or only has "" as paths), it defaults to update all fields provided with values in the request. Using "*" as update_mask will update all fields, including deleting fields not set in the request. In case of BatchUpdate, it must be absent or the same as the update_mask in BatchUpdateMembersRequest when UpdateMemberRequest is built as a child request of BatchUpdateMembersRequest.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\FieldMask|null` |   
  
### hasUpdateMask

### clearUpdateMask

### setUpdateMask

Optional. Field mask used to specify the fields to be updated in the member. If update_mask isn't provided(not set, set with empty paths, or only has "" as paths), it defaults to update all fields provided with values in the request. Using "*" as update_mask will update all fields, including deleting fields not set in the request. In case of BatchUpdate, it must be absent or the same as the update_mask in BatchUpdateMembersRequest when UpdateMemberRequest is built as a child request of BatchUpdateMembersRequest.

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
`member` |  `[Member](https://docs.cloud.google.com/php/docs/reference/apps-meet/latest/V2beta.Member)`   
Required. The Member to update. Format: spaces/{space}/members/{member}  
`updateMask` |  `Google\Protobuf\FieldMask`   
Optional. Field mask used to specify the fields to be updated in the member. If update_mask isn't provided(not set, set with empty paths, or only has "" as paths), it defaults to update all fields provided with values in the request. Using "*" as update_mask will update all fields, including deleting fields not set in the request. In case of BatchUpdate, it must be absent or the same as the update_mask in BatchUpdateMembersRequest when UpdateMemberRequest is built as a child request of BatchUpdateMembersRequest.  
**Returns**  
---  
**Type** | **Description**  
`[UpdateMemberRequest](https://docs.cloud.google.com/php/docs/reference/apps-meet/latest/V2beta.UpdateMemberRequest)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
