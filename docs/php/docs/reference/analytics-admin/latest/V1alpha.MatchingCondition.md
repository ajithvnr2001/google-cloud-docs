---
url: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.MatchingCondition
title: Google Analytics Admin V1alpha Client - Class MatchingCondition (0.34.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:55:23.132743+00:00
---

# Google Analytics Admin V1alpha Client - Class MatchingCondition (0.34.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.MatchingCondition

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Analytics Admin V1alpha Client - Class MatchingCondition (0.34.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.34.3 (latest)  0.33.0  0.32.0  0.31.3  0.30.0  0.29.1  0.28.1  0.27.0  0.26.0  0.25.2  0.24.2  0.23.0  0.22.5  0.20.0  0.19.0  0.18.1  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.2 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Analytics Admin V1alpha Client class MatchingCondition.

Defines a condition for when an Event Edit or Event Creation rule applies to an event.

Generated from protobuf message `google.analytics.admin.v1alpha.MatchingCondition`

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
`↳ field` |  `string`   
Required. The name of the field that is compared against for the condition. If 'event_name' is specified this condition will apply to the name of the event. Otherwise the condition will apply to a parameter with the specified name. This value cannot contain spaces.  
`↳ comparison_type` |  `int`   
Required. The type of comparison to be applied to the value.  
`↳ value` |  `string`   
Required. The value being compared against for this condition. The runtime implementation may perform type coercion of this value to evaluate this condition based on the type of the parameter value.  
`↳ negated` |  `bool`   
Whether or not the result of the comparison should be negated. For example, if `negated` is true, then 'equals' comparisons would function as 'not equals'.  
  
### getField

Required. The name of the field that is compared against for the condition.

If 'event_name' is specified this condition will apply to the name of the event. Otherwise the condition will apply to a parameter with the specified name. This value cannot contain spaces.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setField

Required. The name of the field that is compared against for the condition.

If 'event_name' is specified this condition will apply to the name of the event. Otherwise the condition will apply to a parameter with the specified name. This value cannot contain spaces.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getComparisonType

Required. The type of comparison to be applied to the value.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [ComparisonType](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.MatchingCondition.ComparisonType).  
  
### setComparisonType

Required. The type of comparison to be applied to the value.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [ComparisonType](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.MatchingCondition.ComparisonType).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getValue

Required. The value being compared against for this condition. The runtime implementation may perform type coercion of this value to evaluate this condition based on the type of the parameter value.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setValue

Required. The value being compared against for this condition. The runtime implementation may perform type coercion of this value to evaluate this condition based on the type of the parameter value.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getNegated

Whether or not the result of the comparison should be negated. For example, if `negated` is true, then 'equals' comparisons would function as 'not equals'.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setNegated

Whether or not the result of the comparison should be negated. For example, if `negated` is true, then 'equals' comparisons would function as 'not equals'.

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
