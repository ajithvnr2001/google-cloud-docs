---
url: https://docs.cloud.google.com/java/docs/reference/google-analytics-admin/latest/com.google.analytics.admin.v1alpha.CalculatedMetricOrBuilder
title: Interface CalculatedMetricOrBuilder (0.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:56:11.602940+00:00
---

# Interface CalculatedMetricOrBuilder (0.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-analytics-admin/latest/com.google.analytics.admin.v1alpha.CalculatedMetricOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface CalculatedMetricOrBuilder (0.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.109.0 (latest)  0.105.0  0.104.0  0.103.0  0.101.0  0.98.0  0.97.0  0.95.0  0.93.0  0.92.0  0.91.0  0.90.0  0.88.0  0.86.0  0.85.0  0.84.0  0.83.0  0.82.0  0.80.0  0.78.0  0.77.0  0.74.0  0.73.0  0.72.0  0.70.0  0.69.0  0.68.0  0.67.0  0.66.0  0.65.0  0.64.0  0.63.0  0.62.0  0.61.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0 
    
    
    public interface CalculatedMetricOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCalculatedMetricId()
    
    
    public abstract String getCalculatedMetricId()

Output only. The ID to use for the calculated metric. In the UI, this is referred to as the "API name."

The calculated_metric_id is used when referencing this calculated metric from external APIs. For example, "calcMetric:{calculated_metric_id}".

`string calculated_metric_id = 4 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The calculatedMetricId.  
  
### getCalculatedMetricIdBytes()
    
    
    public abstract ByteString getCalculatedMetricIdBytes()

Output only. The ID to use for the calculated metric. In the UI, this is referred to as the "API name."

The calculated_metric_id is used when referencing this calculated metric from external APIs. For example, "calcMetric:{calculated_metric_id}".

`string calculated_metric_id = 4 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for calculatedMetricId.  
  
### getDescription()
    
    
    public abstract String getDescription()

Optional. Description for this calculated metric. Max length of 4096 characters.

`string description = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public abstract ByteString getDescriptionBytes()

Optional. Description for this calculated metric. Max length of 4096 characters.

`string description = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getDisplayName()
    
    
    public abstract String getDisplayName()

Required. Display name for this calculated metric as shown in the Google Analytics UI. Max length 82 characters.

`string display_name = 3 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public abstract ByteString getDisplayNameBytes()

Required. Display name for this calculated metric as shown in the Google Analytics UI. Max length 82 characters.

`string display_name = 3 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getFormula()
    
    
    public abstract String getFormula()

Required. The calculated metric's definition. Maximum number of unique referenced custom metrics is 5. Formulas supports the following operations:

  * (addition), - (subtraction), - (negative), * (multiplication), / (division), () (parenthesis). Any valid real numbers are acceptable that fit in a Long (64bit integer) or a Double (64 bit floating point number). Example formula: "( customEvent:parameter_name + cartPurchaseQuantity ) / 2.0"



`string formula = 7 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The formula.  
  
### getFormulaBytes()
    
    
    public abstract ByteString getFormulaBytes()

Required. The calculated metric's definition. Maximum number of unique referenced custom metrics is 5. Formulas supports the following operations:

  * (addition), - (subtraction), - (negative), * (multiplication), / (division), () (parenthesis). Any valid real numbers are acceptable that fit in a Long (64bit integer) or a Double (64 bit floating point number). Example formula: "( customEvent:parameter_name + cartPurchaseQuantity ) / 2.0"



`string formula = 7 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for formula.  
  
### getInvalidMetricReference()
    
    
    public abstract boolean getInvalidMetricReference()

Output only. If true, this calculated metric has a invalid metric reference. Anything using a calculated metric with invalid_metric_reference set to true may fail, produce warnings, or produce unexpected results.

`bool invalid_metric_reference = 9 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The invalidMetricReference.  
  
### getMetricUnit()
    
    
    public abstract CalculatedMetric.MetricUnit getMetricUnit()

Required. The type for the calculated metric's value.

` .google.analytics.admin.v1alpha.CalculatedMetric.MetricUnit metric_unit = 5 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[CalculatedMetric.MetricUnit](https://docs.cloud.google.com/java/docs/reference/google-analytics-admin/latest/com.google.analytics.admin.v1alpha.CalculatedMetric.MetricUnit)` | The metricUnit.  
  
### getMetricUnitValue()
    
    
    public abstract int getMetricUnitValue()

Required. The type for the calculated metric's value.

` .google.analytics.admin.v1alpha.CalculatedMetric.MetricUnit metric_unit = 5 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for metricUnit.  
  
### getName()
    
    
    public abstract String getName()

Identifier. Resource name for this CalculatedMetric. Format: 'properties/{property_id}/calculatedMetrics/{calculated_metric_id}'

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Identifier. Resource name for this CalculatedMetric. Format: 'properties/{property_id}/calculatedMetrics/{calculated_metric_id}'

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getRestrictedMetricType(int index)
    
    
    public abstract CalculatedMetric.RestrictedMetricType getRestrictedMetricType(int index)

Output only. Types of restricted data that this metric contains.

` repeated .google.analytics.admin.v1alpha.CalculatedMetric.RestrictedMetricType restricted_metric_type = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[CalculatedMetric.RestrictedMetricType](https://docs.cloud.google.com/java/docs/reference/google-analytics-admin/latest/com.google.analytics.admin.v1alpha.CalculatedMetric.RestrictedMetricType)` | The restrictedMetricType at the given index.  
  
### getRestrictedMetricTypeCount()
    
    
    public abstract int getRestrictedMetricTypeCount()

Output only. Types of restricted data that this metric contains.

` repeated .google.analytics.admin.v1alpha.CalculatedMetric.RestrictedMetricType restricted_metric_type = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of restrictedMetricType.  
  
### getRestrictedMetricTypeList()
    
    
    public abstract List<CalculatedMetric.RestrictedMetricType> getRestrictedMetricTypeList()

Output only. Types of restricted data that this metric contains.

` repeated .google.analytics.admin.v1alpha.CalculatedMetric.RestrictedMetricType restricted_metric_type = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[RestrictedMetricType](https://docs.cloud.google.com/java/docs/reference/google-analytics-admin/latest/com.google.analytics.admin.v1alpha.CalculatedMetric.RestrictedMetricType)>` | A list containing the restrictedMetricType.  
  
### getRestrictedMetricTypeValue(int index)
    
    
    public abstract int getRestrictedMetricTypeValue(int index)

Output only. Types of restricted data that this metric contains.

` repeated .google.analytics.admin.v1alpha.CalculatedMetric.RestrictedMetricType restricted_metric_type = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire of restrictedMetricType at the given index.  
  
### getRestrictedMetricTypeValueList()
    
    
    public abstract List<Integer> getRestrictedMetricTypeValueList()

Output only. Types of restricted data that this metric contains.

` repeated .google.analytics.admin.v1alpha.CalculatedMetric.RestrictedMetricType restricted_metric_type = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>` | A list containing the enum numeric values on the wire for restrictedMetricType.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
