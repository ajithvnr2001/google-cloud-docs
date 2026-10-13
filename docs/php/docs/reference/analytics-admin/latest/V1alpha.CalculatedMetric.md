---
url: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CalculatedMetric
title: Google Analytics Admin V1alpha Client - Class CalculatedMetric (0.34.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:54:53.349068+00:00
---

# Google Analytics Admin V1alpha Client - Class CalculatedMetric (0.34.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CalculatedMetric

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Analytics Admin V1alpha Client - Class CalculatedMetric (0.34.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.34.3 (latest)  0.33.0  0.32.0  0.31.3  0.30.0  0.29.1  0.28.1  0.27.0  0.26.0  0.25.2  0.24.2  0.23.0  0.22.5  0.20.0  0.19.0  0.18.1  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.2 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Analytics Admin V1alpha Client class CalculatedMetric.

A definition for a calculated metric.

Generated from protobuf message `google.analytics.admin.v1alpha.CalculatedMetric`

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
Identifier. Resource name for this CalculatedMetric. Format: 'properties/{property_id}/calculatedMetrics/{calculated_metric_id}'  
`↳ description` |  `string`   
Optional. Description for this calculated metric. Max length of 4096 characters.  
`↳ display_name` |  `string`   
Required. Display name for this calculated metric as shown in the Google Analytics UI. Max length 82 characters.  
`↳ calculated_metric_id` |  `string`   
Output only. The ID to use for the calculated metric. In the UI, this is referred to as the "API name." The calculated_metric_id is used when referencing this calculated metric from external APIs. For example, "calcMetric:{calculated_metric_id}".  
`↳ metric_unit` |  `int`   
Required. The type for the calculated metric's value.  
`↳ restricted_metric_type` |  `int[]`   
Output only. Types of restricted data that this metric contains.  
`↳ formula` |  `string`   
Required. The calculated metric's definition. Maximum number of unique referenced custom metrics is 5. Formulas supports the following operations: + (addition), - (subtraction), - (negative), * (multiplication), / (division), () (parenthesis). Any valid real numbers are acceptable that fit in a Long (64bit integer) or a Double (64 bit floating point number). Example formula: "( customEvent:parameter_name + cartPurchaseQuantity ) / 2.0"  
`↳ invalid_metric_reference` |  `bool`   
Output only. If true, this calculated metric has a invalid metric reference. Anything using a calculated metric with invalid_metric_reference set to true may fail, produce warnings, or produce unexpected results.  
  
### getName

Identifier. Resource name for this CalculatedMetric.

Format: 'properties/{property_id}/calculatedMetrics/{calculated_metric_id}'

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

Identifier. Resource name for this CalculatedMetric.

Format: 'properties/{property_id}/calculatedMetrics/{calculated_metric_id}'

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDescription

Optional. Description for this calculated metric.

Max length of 4096 characters.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setDescription

Optional. Description for this calculated metric.

Max length of 4096 characters.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDisplayName

Required. Display name for this calculated metric as shown in the Google Analytics UI. Max length 82 characters.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setDisplayName

Required. Display name for this calculated metric as shown in the Google Analytics UI. Max length 82 characters.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCalculatedMetricId

Output only. The ID to use for the calculated metric. In the UI, this is referred to as the "API name." The calculated_metric_id is used when referencing this calculated metric from external APIs. For example, "calcMetric:{calculated_metric_id}".

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setCalculatedMetricId

Output only. The ID to use for the calculated metric. In the UI, this is referred to as the "API name." The calculated_metric_id is used when referencing this calculated metric from external APIs. For example, "calcMetric:{calculated_metric_id}".

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getMetricUnit

Required. The type for the calculated metric's value.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [MetricUnit](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CalculatedMetric.MetricUnit).  
  
### setMetricUnit

Required. The type for the calculated metric's value.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [MetricUnit](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CalculatedMetric.MetricUnit).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getRestrictedMetricType

Output only. Types of restricted data that this metric contains.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<int>` |   
  
### setRestrictedMetricType

Output only. Types of restricted data that this metric contains.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int[]`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getFormula

Required. The calculated metric's definition. Maximum number of unique referenced custom metrics is 5. Formulas supports the following operations:

  * (addition), - (subtraction), - (negative), * (multiplication), / (division), () (parenthesis). Any valid real numbers are acceptable that fit in a Long (64bit integer) or a Double (64 bit floating point number).



Example formula: "( customEvent:parameter_name + cartPurchaseQuantity ) / 2.0"

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setFormula

Required. The calculated metric's definition. Maximum number of unique referenced custom metrics is 5. Formulas supports the following operations:

  * (addition), - (subtraction), - (negative), * (multiplication), / (division), () (parenthesis). Any valid real numbers are acceptable that fit in a Long (64bit integer) or a Double (64 bit floating point number).



Example formula: "( customEvent:parameter_name + cartPurchaseQuantity ) / 2.0"

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getInvalidMetricReference

Output only. If true, this calculated metric has a invalid metric reference. Anything using a calculated metric with invalid_metric_reference set to true may fail, produce warnings, or produce unexpected results.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setInvalidMetricReference

Output only. If true, this calculated metric has a invalid metric reference. Anything using a calculated metric with invalid_metric_reference set to true may fail, produce warnings, or produce unexpected results.

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
