---
url: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.KeyEvent
title: Google Analytics Admin V1alpha Client - Class KeyEvent (0.34.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:55:14.263123+00:00
---

# Google Analytics Admin V1alpha Client - Class KeyEvent (0.34.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.KeyEvent

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Analytics Admin V1alpha Client - Class KeyEvent (0.34.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.34.3 (latest)  0.33.0  0.32.0  0.31.3  0.30.0  0.29.1  0.28.1  0.27.0  0.26.0  0.25.2  0.24.2  0.23.0  0.22.5  0.20.0  0.19.0  0.18.1  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.2 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Analytics Admin V1alpha Client class KeyEvent.

A key event in a Google Analytics property.

Generated from protobuf message `google.analytics.admin.v1alpha.KeyEvent`

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
Output only. Resource name of this key event. Format: properties/{property}/keyEvents/{key_event}  
`↳ event_name` |  `string`   
Immutable. The event name for this key event. Examples: 'click', 'purchase'  
`↳ create_time` |  `Google\Protobuf\Timestamp`   
Output only. Time when this key event was created in the property.  
`↳ deletable` |  `bool`   
Output only. If set to true, this event can be deleted.  
`↳ custom` |  `bool`   
Output only. If set to true, this key event refers to a custom event. If set to false, this key event refers to a default event in GA. Default events typically have special meaning in GA. Default events are usually created for you by the GA system, but in some cases can be created by property admins. Custom events count towards the maximum number of custom key events that may be created per property.  
`↳ counting_method` |  `int`   
Required. The method by which Key Events will be counted across multiple events within a session.  
`↳ default_value` |  `[KeyEvent\DefaultValue](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.KeyEvent.DefaultValue)`   
Optional. Defines a default value/currency for a key event.  
  
### getName

Output only. Resource name of this key event.

Format: properties/{property}/keyEvents/{key_event}

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

Output only. Resource name of this key event.

Format: properties/{property}/keyEvents/{key_event}

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEventName

Immutable. The event name for this key event.

Examples: 'click', 'purchase'

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setEventName

Immutable. The event name for this key event.

Examples: 'click', 'purchase'

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCreateTime

Output only. Time when this key event was created in the property.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasCreateTime

### clearCreateTime

### setCreateTime

Output only. Time when this key event was created in the property.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDeletable

Output only. If set to true, this event can be deleted.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setDeletable

Output only. If set to true, this event can be deleted.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCustom

Output only. If set to true, this key event refers to a custom event. If set to false, this key event refers to a default event in GA. Default events typically have special meaning in GA. Default events are usually created for you by the GA system, but in some cases can be created by property admins. Custom events count towards the maximum number of custom key events that may be created per property.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setCustom

Output only. If set to true, this key event refers to a custom event. If set to false, this key event refers to a default event in GA. Default events typically have special meaning in GA. Default events are usually created for you by the GA system, but in some cases can be created by property admins. Custom events count towards the maximum number of custom key events that may be created per property.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCountingMethod

Required. The method by which Key Events will be counted across multiple events within a session.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [CountingMethod](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.KeyEvent.CountingMethod).  
  
### setCountingMethod

Required. The method by which Key Events will be counted across multiple events within a session.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [CountingMethod](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.KeyEvent.CountingMethod).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDefaultValue

Optional. Defines a default value/currency for a key event.

**Returns**  
---  
**Type** | **Description**  
`[KeyEvent\DefaultValue](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.KeyEvent.DefaultValue)|null` |   
  
### hasDefaultValue

### clearDefaultValue

### setDefaultValue

Optional. Defines a default value/currency for a key event.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[KeyEvent\DefaultValue](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.KeyEvent.DefaultValue)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
