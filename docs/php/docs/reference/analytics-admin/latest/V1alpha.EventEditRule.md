---
url: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.EventEditRule
title: Google Analytics Admin V1alpha Client - Class EventEditRule (0.34.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:55:06.085476+00:00
---

# Google Analytics Admin V1alpha Client - Class EventEditRule (0.34.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.EventEditRule

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Analytics Admin V1alpha Client - Class EventEditRule (0.34.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.34.3 (latest)  0.33.0  0.32.0  0.31.3  0.30.0  0.29.1  0.28.1  0.27.0  0.26.0  0.25.2  0.24.2  0.23.0  0.22.5  0.20.0  0.19.0  0.18.1  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.2 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Analytics Admin V1alpha Client class EventEditRule.

An Event Edit Rule defines conditions that will trigger the creation of an entirely new event based upon matched criteria of a source event. Additional mutations of the parameters from the source event can be defined.

Unlike Event Create rules, Event Edit Rules are applied in their defined order. Event Edit rules can't be used to modify an event created from an Event Create rule.

Generated from protobuf message `google.analytics.admin.v1alpha.EventEditRule`

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
Identifier. Resource name for this EventEditRule resource. Format: properties/{property}/dataStreams/{data_stream}/eventEditRules/{event_edit_rule}  
`↳ display_name` |  `string`   
Required. The display name of this event edit rule. Maximum of 255 characters.  
`↳ event_conditions` |  `array<[MatchingCondition](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.MatchingCondition)>`   
Required. Conditions on the source event must match for this rule to be applied. Must have at least one condition, and can have up to 10 max.  
`↳ parameter_mutations` |  `array<[ParameterMutation](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ParameterMutation)>`   
Required. Parameter mutations define parameter behavior on the new event, and are applied in order. A maximum of 20 mutations can be applied.  
`↳ processing_order` |  `int|string`   
Output only. The order for which this rule will be processed. Rules with an order value lower than this will be processed before this rule, rules with an order value higher than this will be processed after this rule. New event edit rules will be assigned an order value at the end of the order. This value does not apply to event create rules.  
  
### getName

Identifier. Resource name for this EventEditRule resource.

Format: properties/{property}/dataStreams/{data_stream}/eventEditRules/{event_edit_rule}

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

Identifier. Resource name for this EventEditRule resource.

Format: properties/{property}/dataStreams/{data_stream}/eventEditRules/{event_edit_rule}

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDisplayName

Required. The display name of this event edit rule. Maximum of 255 characters.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setDisplayName

Required. The display name of this event edit rule. Maximum of 255 characters.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEventConditions

Required. Conditions on the source event must match for this rule to be applied. Must have at least one condition, and can have up to 10 max.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<[MatchingCondition](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.MatchingCondition)>` |   
  
### setEventConditions

Required. Conditions on the source event must match for this rule to be applied. Must have at least one condition, and can have up to 10 max.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array<[MatchingCondition](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.MatchingCondition)>`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getParameterMutations

Required. Parameter mutations define parameter behavior on the new event, and are applied in order. A maximum of 20 mutations can be applied.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<[ParameterMutation](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ParameterMutation)>` |   
  
### setParameterMutations

Required. Parameter mutations define parameter behavior on the new event, and are applied in order. A maximum of 20 mutations can be applied.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array<[ParameterMutation](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ParameterMutation)>`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getProcessingOrder

Output only. The order for which this rule will be processed. Rules with an order value lower than this will be processed before this rule, rules with an order value higher than this will be processed after this rule. New event edit rules will be assigned an order value at the end of the order.

This value does not apply to event create rules.

**Returns**  
---  
**Type** | **Description**  
`int|string` |   
  
### setProcessingOrder

Output only. The order for which this rule will be processed. Rules with an order value lower than this will be processed before this rule, rules with an order value higher than this will be processed after this rule. New event edit rules will be assigned an order value at the end of the order.

This value does not apply to event create rules.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int|string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
