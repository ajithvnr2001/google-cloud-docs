---
url: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.EventMapping
title: Google Analytics Admin V1alpha Client - Class EventMapping (0.34.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:55:06.460625+00:00
---

# Google Analytics Admin V1alpha Client - Class EventMapping (0.34.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.EventMapping

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Analytics Admin V1alpha Client - Class EventMapping (0.34.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.34.3 (latest)  0.33.0  0.32.0  0.31.3  0.30.0  0.29.1  0.28.1  0.27.0  0.26.0  0.25.2  0.24.2  0.23.0  0.22.5  0.20.0  0.19.0  0.18.1  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.2 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Analytics Admin V1alpha Client class EventMapping.

Event setting conditions to match an event.

Generated from protobuf message `google.analytics.admin.v1alpha.EventMapping`

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
`↳ event_name` |  `string`   
Required. Name of the Google Analytics event. It must always be set. The max allowed display name length is 40 UTF-16 code units.  
`↳ min_event_count` |  `int|string`   
At least one of the following four min/max values must be set. The values set will be ANDed together to qualify an event. The minimum number of times the event occurred. If not set, minimum event count won't be checked.  
`↳ max_event_count` |  `int|string`   
The maximum number of times the event occurred. If not set, maximum event count won't be checked.  
`↳ min_event_value` |  `float`   
The minimum revenue generated due to the event. Revenue currency will be defined at the property level. If not set, minimum event value won't be checked.  
`↳ max_event_value` |  `float`   
The maximum revenue generated due to the event. Revenue currency will be defined at the property level. If not set, maximum event value won't be checked.  
  
### getEventName

Required. Name of the Google Analytics event. It must always be set.

The max allowed display name length is 40 UTF-16 code units.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setEventName

Required. Name of the Google Analytics event. It must always be set.

The max allowed display name length is 40 UTF-16 code units.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getMinEventCount

At least one of the following four min/max values must be set. The values set will be ANDed together to qualify an event.

The minimum number of times the event occurred. If not set, minimum event count won't be checked.

**Returns**  
---  
**Type** | **Description**  
`int|string` |   
  
### hasMinEventCount

### clearMinEventCount

### setMinEventCount

At least one of the following four min/max values must be set. The values set will be ANDed together to qualify an event.

The minimum number of times the event occurred. If not set, minimum event count won't be checked.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int|string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getMaxEventCount

The maximum number of times the event occurred. If not set, maximum event count won't be checked.

**Returns**  
---  
**Type** | **Description**  
`int|string` |   
  
### hasMaxEventCount

### clearMaxEventCount

### setMaxEventCount

The maximum number of times the event occurred. If not set, maximum event count won't be checked.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int|string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getMinEventValue

The minimum revenue generated due to the event. Revenue currency will be defined at the property level. If not set, minimum event value won't be checked.

**Returns**  
---  
**Type** | **Description**  
`float` |   
  
### hasMinEventValue

### clearMinEventValue

### setMinEventValue

The minimum revenue generated due to the event. Revenue currency will be defined at the property level. If not set, minimum event value won't be checked.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `float`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getMaxEventValue

The maximum revenue generated due to the event. Revenue currency will be defined at the property level. If not set, maximum event value won't be checked.

**Returns**  
---  
**Type** | **Description**  
`float` |   
  
### hasMaxEventValue

### clearMaxEventValue

### setMaxEventValue

The maximum revenue generated due to the event. Revenue currency will be defined at the property level. If not set, maximum event value won't be checked.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `float`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
