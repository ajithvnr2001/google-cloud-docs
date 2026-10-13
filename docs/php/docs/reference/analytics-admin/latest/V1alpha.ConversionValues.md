---
url: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ConversionValues
title: Google Analytics Admin V1alpha Client - Class ConversionValues (0.34.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:54:55.920742+00:00
---

# Google Analytics Admin V1alpha Client - Class ConversionValues (0.34.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ConversionValues

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Analytics Admin V1alpha Client - Class ConversionValues (0.34.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.34.3 (latest)  0.33.0  0.32.0  0.31.3  0.30.0  0.29.1  0.28.1  0.27.0  0.26.0  0.25.2  0.24.2  0.23.0  0.22.5  0.20.0  0.19.0  0.18.1  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.2 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Analytics Admin V1alpha Client class ConversionValues.

Conversion value settings for a postback window for SKAdNetwork conversion value schema.

Generated from protobuf message `google.analytics.admin.v1alpha.ConversionValues`

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
`↳ display_name` |  `string`   
Display name of the SKAdNetwork conversion value. The max allowed display name length is 50 UTF-16 code units.  
`↳ fine_value` |  `int`   
The fine-grained conversion value. This is applicable only to the first postback window. Its valid values are [0,63], both inclusive. It must be set for postback window 1, and must not be set for postback window 2 & 3\. This value is not guaranteed to be unique. If the configuration for the first postback window is re-used for second or third postback windows this field has no effect.  
`↳ coarse_value` |  `int`   
Required. A coarse grained conversion value. This value is not guaranteed to be unique.  
`↳ event_mappings` |  `array<[EventMapping](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.EventMapping)>`   
Event conditions that must be met for this Conversion Value to be achieved. The conditions in this list are ANDed together. It must have minimum of 1 entry and maximum of 3 entries, if the postback window is enabled.  
`↳ lock_enabled` |  `bool`   
If true, the SDK should lock to this conversion value for the current postback window.  
  
### getDisplayName

Display name of the SKAdNetwork conversion value.

The max allowed display name length is 50 UTF-16 code units.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setDisplayName

Display name of the SKAdNetwork conversion value.

The max allowed display name length is 50 UTF-16 code units.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getFineValue

The fine-grained conversion value. This is applicable only to the first postback window. Its valid values are [0,63], both inclusive. It must be set for postback window 1, and must not be set for postback window 2 & 3.

This value is not guaranteed to be unique. If the configuration for the first postback window is re-used for second or third postback windows this field has no effect.

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### hasFineValue

### clearFineValue

### setFineValue

The fine-grained conversion value. This is applicable only to the first postback window. Its valid values are [0,63], both inclusive. It must be set for postback window 1, and must not be set for postback window 2 & 3.

This value is not guaranteed to be unique. If the configuration for the first postback window is re-used for second or third postback windows this field has no effect.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCoarseValue

Required. A coarse grained conversion value.

This value is not guaranteed to be unique.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [CoarseValue](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CoarseValue).  
  
### setCoarseValue

Required. A coarse grained conversion value.

This value is not guaranteed to be unique.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [CoarseValue](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CoarseValue).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEventMappings

Event conditions that must be met for this Conversion Value to be achieved.

The conditions in this list are ANDed together. It must have minimum of 1 entry and maximum of 3 entries, if the postback window is enabled.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<[EventMapping](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.EventMapping)>` |   
  
### setEventMappings

Event conditions that must be met for this Conversion Value to be achieved.

The conditions in this list are ANDed together. It must have minimum of 1 entry and maximum of 3 entries, if the postback window is enabled.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array<[EventMapping](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.EventMapping)>`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getLockEnabled

If true, the SDK should lock to this conversion value for the current postback window.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setLockEnabled

If true, the SDK should lock to this conversion value for the current postback window.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
