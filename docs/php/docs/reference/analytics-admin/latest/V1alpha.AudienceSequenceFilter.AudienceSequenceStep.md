---
url: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AudienceSequenceFilter.AudienceSequenceStep
title: Google Analytics Admin V1alpha Client - Class AudienceSequenceStep (0.34.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:54:51.609781+00:00
---

# Google Analytics Admin V1alpha Client - Class AudienceSequenceStep (0.34.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AudienceSequenceFilter.AudienceSequenceStep

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Analytics Admin V1alpha Client - Class AudienceSequenceStep (0.34.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.34.3 (latest)  0.33.0  0.32.0  0.31.3  0.30.0  0.29.1  0.28.1  0.27.0  0.26.0  0.25.2  0.24.2  0.23.0  0.22.5  0.20.0  0.19.0  0.18.1  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.2 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Analytics Admin V1alpha Client class AudienceSequenceStep.

A condition that must occur in the specified step order for this user to match the sequence.

Generated from protobuf message `google.analytics.admin.v1alpha.AudienceSequenceFilter.AudienceSequenceStep`

## Namespace

Google \ Analytics \ Admin \ V1alpha \ AudienceSequenceFilter

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ scope` |  `int`   
Required. Immutable. Specifies the scope for this step.  
`↳ immediately_follows` |  `bool`   
Optional. If true, the event satisfying this step must be the very next event after the event satisfying the last step. If unset or false, this step indirectly follows the prior step; for example, there may be events between the prior step and this step. It is ignored for the first step.  
`↳ constraint_duration` |  `Google\Protobuf\Duration`   
Optional. When set, this step must be satisfied within the constraint_duration of the previous step (For example, t[i] - t[i-1] <= constraint_duration). If not set, there is no duration requirement (the duration is effectively unlimited). It is ignored for the first step.  
`↳ filter_expression` |  `[Google\Analytics\Admin\V1alpha\AudienceFilterExpression](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AudienceFilterExpression)`   
Required. Immutable. A logical expression of Audience dimension, metric, or event filters in each step.  
  
### getScope

Required. Immutable. Specifies the scope for this step.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [AudienceFilterScope](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AudienceFilterScope).  
  
### setScope

Required. Immutable. Specifies the scope for this step.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [AudienceFilterScope](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AudienceFilterScope).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getImmediatelyFollows

Optional. If true, the event satisfying this step must be the very next event after the event satisfying the last step. If unset or false, this step indirectly follows the prior step; for example, there may be events between the prior step and this step. It is ignored for the first step.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setImmediatelyFollows

Optional. If true, the event satisfying this step must be the very next event after the event satisfying the last step. If unset or false, this step indirectly follows the prior step; for example, there may be events between the prior step and this step. It is ignored for the first step.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getConstraintDuration

Optional. When set, this step must be satisfied within the constraint_duration of the previous step (For example, t[i] - t[i-1] <= constraint_duration). If not set, there is no duration requirement (the duration is effectively unlimited). It is ignored for the first step.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Duration|null` |   
  
### hasConstraintDuration

### clearConstraintDuration

### setConstraintDuration

Optional. When set, this step must be satisfied within the constraint_duration of the previous step (For example, t[i] - t[i-1] <= constraint_duration). If not set, there is no duration requirement (the duration is effectively unlimited). It is ignored for the first step.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Duration`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getFilterExpression

Required. Immutable. A logical expression of Audience dimension, metric, or event filters in each step.

**Returns**  
---  
**Type** | **Description**  
`[Google\Analytics\Admin\V1alpha\AudienceFilterExpression](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AudienceFilterExpression)|null` |   
  
### hasFilterExpression

### clearFilterExpression

### setFilterExpression

Required. Immutable. A logical expression of Audience dimension, metric, or event filters in each step.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Analytics\Admin\V1alpha\AudienceFilterExpression](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AudienceFilterExpression)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
