---
url: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Audience
title: Google Analytics Admin V1alpha Client - Class Audience (0.34.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:54:49.421743+00:00
---

# Google Analytics Admin V1alpha Client - Class Audience (0.34.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Audience

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Analytics Admin V1alpha Client - Class Audience (0.34.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.34.3 (latest)  0.33.0  0.32.0  0.31.3  0.30.0  0.29.1  0.28.1  0.27.0  0.26.0  0.25.2  0.24.2  0.23.0  0.22.5  0.20.0  0.19.0  0.18.1  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.2 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Analytics Admin V1alpha Client class Audience.

A resource message representing an Audience.

Generated from protobuf message `google.analytics.admin.v1alpha.Audience`

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
`↳ name` |  `string`   
Output only. The resource name for this Audience resource. Format: properties/{propertyId}/audiences/{audienceId}  
`↳ display_name` |  `string`   
Required. The display name of the Audience.  
`↳ description` |  `string`   
Required. The description of the Audience.  
`↳ membership_duration_days` |  `int`   
Required. Immutable. The duration a user should stay in an Audience. It cannot be set to more than 540 days.  
`↳ ads_personalization_enabled` |  `bool`   
Output only. It is automatically set by GA to false if this is an NPA Audience and is excluded from ads personalization.  
`↳ event_trigger` |  `[AudienceEventTrigger](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AudienceEventTrigger)`   
Optional. Specifies an event to log when a user joins the Audience. If not set, no event is logged when a user joins the Audience.  
`↳ exclusion_duration_mode` |  `int`   
Immutable. Specifies how long an exclusion lasts for users that meet the exclusion filter. It is applied to all EXCLUDE filter clauses and is ignored when there is no EXCLUDE filter clause in the Audience.  
`↳ filter_clauses` |  `array<[AudienceFilterClause](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AudienceFilterClause)>`   
Required. Immutable. Unordered list. Filter clauses that define the Audience. All clauses will be AND’ed together.  
`↳ create_time` |  `Google\Protobuf\Timestamp`   
Output only. Time when the Audience was created.  
  
### getName

Output only. The resource name for this Audience resource.

Format: properties/{propertyId}/audiences/{audienceId}

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

Output only. The resource name for this Audience resource.

Format: properties/{propertyId}/audiences/{audienceId}

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDisplayName

Required. The display name of the Audience.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setDisplayName

Required. The display name of the Audience.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDescription

Required. The description of the Audience.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setDescription

Required. The description of the Audience.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getMembershipDurationDays

Required. Immutable. The duration a user should stay in an Audience. It cannot be set to more than 540 days.

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### setMembershipDurationDays

Required. Immutable. The duration a user should stay in an Audience. It cannot be set to more than 540 days.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getAdsPersonalizationEnabled

Output only. It is automatically set by GA to false if this is an NPA Audience and is excluded from ads personalization.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setAdsPersonalizationEnabled

Output only. It is automatically set by GA to false if this is an NPA Audience and is excluded from ads personalization.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEventTrigger

Optional. Specifies an event to log when a user joins the Audience. If not set, no event is logged when a user joins the Audience.

**Returns**  
---  
**Type** | **Description**  
`[AudienceEventTrigger](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AudienceEventTrigger)|null` |   
  
### hasEventTrigger

### clearEventTrigger

### setEventTrigger

Optional. Specifies an event to log when a user joins the Audience. If not set, no event is logged when a user joins the Audience.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[AudienceEventTrigger](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AudienceEventTrigger)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getExclusionDurationMode

Immutable. Specifies how long an exclusion lasts for users that meet the exclusion filter. It is applied to all EXCLUDE filter clauses and is ignored when there is no EXCLUDE filter clause in the Audience.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [AudienceExclusionDurationMode](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Audience.AudienceExclusionDurationMode).  
  
### setExclusionDurationMode

Immutable. Specifies how long an exclusion lasts for users that meet the exclusion filter. It is applied to all EXCLUDE filter clauses and is ignored when there is no EXCLUDE filter clause in the Audience.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [AudienceExclusionDurationMode](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.Audience.AudienceExclusionDurationMode).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getFilterClauses

Required. Immutable. Unordered list. Filter clauses that define the Audience. All clauses will be AND’ed together.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<[AudienceFilterClause](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AudienceFilterClause)>` |   
  
### setFilterClauses

Required. Immutable. Unordered list. Filter clauses that define the Audience. All clauses will be AND’ed together.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array<[AudienceFilterClause](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AudienceFilterClause)>`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCreateTime

Output only. Time when the Audience was created.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasCreateTime

### clearCreateTime

### setCreateTime

Output only. Time when the Audience was created.

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

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
