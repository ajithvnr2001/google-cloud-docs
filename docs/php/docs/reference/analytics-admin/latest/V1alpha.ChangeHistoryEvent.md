---
url: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ChangeHistoryEvent
title: Google Analytics Admin V1alpha Client - Class ChangeHistoryEvent (0.34.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:10:37.476631+00:00
---

# Google Analytics Admin V1alpha Client - Class ChangeHistoryEvent (0.34.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ChangeHistoryEvent

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Analytics Admin V1alpha Client - Class ChangeHistoryEvent (0.34.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.34.3 (latest)  0.33.0  0.32.0  0.31.3  0.30.0  0.29.1  0.28.1  0.27.0  0.26.0  0.25.2  0.24.2  0.23.0  0.22.5  0.20.0  0.19.0  0.18.1  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.2 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Analytics Admin V1alpha Client class ChangeHistoryEvent.

A set of changes within a Google Analytics account or its child properties that resulted from the same cause. Common causes would be updates made in the Google Analytics UI, changes from customer support, or automatic Google Analytics system changes.

Generated from protobuf message `google.analytics.admin.v1alpha.ChangeHistoryEvent`

## Namespace

Google \ Analytics \ Admin \ V1alpha

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ id` |  `string`   
ID of this change history event. This ID is unique across Google Analytics.  
`↳ change_time` |  `Google\Protobuf\Timestamp`   
Time when change was made.  
`↳ actor_type` |  `int`   
The type of actor that made this change.  
`↳ user_actor_email` |  `string`   
Email address of the Google account that made the change. This will be a valid email address if the actor field is set to USER, and empty otherwise. Google accounts that have been deleted will cause an error.  
`↳ changes_filtered` |  `bool`   
If true, then the list of changes returned was filtered, and does not represent all changes that occurred in this event.  
`↳ changes` |  `array<[ChangeHistoryChange](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ChangeHistoryChange)>`   
A list of changes made in this change history event that fit the filters specified in SearchChangeHistoryEventsRequest.  
  
### getId

ID of this change history event. This ID is unique across Google Analytics.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setId

ID of this change history event. This ID is unique across Google Analytics.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getChangeTime

Time when change was made.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasChangeTime

### clearChangeTime

### setChangeTime

Time when change was made.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getActorType

The type of actor that made this change.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [ActorType](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ActorType).  
  
### setActorType

The type of actor that made this change.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [ActorType](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ActorType).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getUserActorEmail

Email address of the Google account that made the change. This will be a valid email address if the actor field is set to USER, and empty otherwise.

Google accounts that have been deleted will cause an error.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setUserActorEmail

Email address of the Google account that made the change. This will be a valid email address if the actor field is set to USER, and empty otherwise.

Google accounts that have been deleted will cause an error.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getChangesFiltered

If true, then the list of changes returned was filtered, and does not represent all changes that occurred in this event.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setChangesFiltered

If true, then the list of changes returned was filtered, and does not represent all changes that occurred in this event.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getChanges

A list of changes made in this change history event that fit the filters specified in SearchChangeHistoryEventsRequest.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<[ChangeHistoryChange](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ChangeHistoryChange)>` |   
  
### setChanges

A list of changes made in this change history event that fit the filters specified in SearchChangeHistoryEventsRequest.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array<[ChangeHistoryChange](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ChangeHistoryChange)>`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
