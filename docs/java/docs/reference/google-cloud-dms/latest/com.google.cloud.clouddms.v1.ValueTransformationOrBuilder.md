---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ValueTransformationOrBuilder
title: Interface ValueTransformationOrBuilder (2.98.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:42:40.629995+00:00
---

# Interface ValueTransformationOrBuilder (2.98.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ValueTransformationOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ValueTransformationOrBuilder (2.98.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.98.0 (latest)  2.94.0  2.93.0  2.92.0  2.90.0  2.87.0  2.86.0  2.84.0  2.82.0  2.81.0  2.80.0  2.79.0  2.77.0  2.75.0  2.74.0  2.73.0  2.72.0  2.71.0  2.69.0  2.67.0  2.66.0  2.63.0  2.62.0  2.61.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.50.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.8  2.1.9 
    
    
    public interface ValueTransformationOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getActionCase()
    
    
    public abstract ValueTransformation.ActionCase getActionCase()

**Returns**  
---  
**Type** | **Description**  
`[ValueTransformation.ActionCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ValueTransformation.ActionCase)` |   
  
### getApplyHash()
    
    
    public abstract ApplyHash getApplyHash()

Optional. Applies a hash function on the data

` .google.cloud.clouddms.v1.ApplyHash apply_hash = 205 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ApplyHash](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ApplyHash)` | The applyHash.  
  
### getApplyHashOrBuilder()
    
    
    public abstract ApplyHashOrBuilder getApplyHashOrBuilder()

Optional. Applies a hash function on the data

` .google.cloud.clouddms.v1.ApplyHash apply_hash = 205 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ApplyHashOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ApplyHashOrBuilder)` |   
  
### getAssignMaxValue()
    
    
    public abstract Empty getAssignMaxValue()

Optional. Set to max_value - if integer or numeric, will use int.maxvalue, etc

`.google.protobuf.Empty assign_max_value = 203 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)` | The assignMaxValue.  
  
### getAssignMaxValueOrBuilder()
    
    
    public abstract EmptyOrBuilder getAssignMaxValueOrBuilder()

Optional. Set to max_value - if integer or numeric, will use int.maxvalue, etc

`.google.protobuf.Empty assign_max_value = 203 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[EmptyOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.EmptyOrBuilder.html)` |   
  
### getAssignMinValue()
    
    
    public abstract Empty getAssignMinValue()

Optional. Set to min_value - if integer or numeric, will use int.minvalue, etc

`.google.protobuf.Empty assign_min_value = 202 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)` | The assignMinValue.  
  
### getAssignMinValueOrBuilder()
    
    
    public abstract EmptyOrBuilder getAssignMinValueOrBuilder()

Optional. Set to min_value - if integer or numeric, will use int.minvalue, etc

`.google.protobuf.Empty assign_min_value = 202 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[EmptyOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.EmptyOrBuilder.html)` |   
  
### getAssignNull()
    
    
    public abstract Empty getAssignNull()

Optional. Set to null

`.google.protobuf.Empty assign_null = 200 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)` | The assignNull.  
  
### getAssignNullOrBuilder()
    
    
    public abstract EmptyOrBuilder getAssignNullOrBuilder()

Optional. Set to null

`.google.protobuf.Empty assign_null = 200 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[EmptyOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.EmptyOrBuilder.html)` |   
  
### getAssignSpecificValue()
    
    
    public abstract AssignSpecificValue getAssignSpecificValue()

Optional. Set to a specific value (value is converted to fit the target data type)

` .google.cloud.clouddms.v1.AssignSpecificValue assign_specific_value = 201 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[AssignSpecificValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.AssignSpecificValue)` | The assignSpecificValue.  
  
### getAssignSpecificValueOrBuilder()
    
    
    public abstract AssignSpecificValueOrBuilder getAssignSpecificValueOrBuilder()

Optional. Set to a specific value (value is converted to fit the target data type)

` .google.cloud.clouddms.v1.AssignSpecificValue assign_specific_value = 201 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[AssignSpecificValueOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.AssignSpecificValueOrBuilder)` |   
  
### getDoubleComparison()
    
    
    public abstract DoubleComparisonFilter getDoubleComparison()

Optional. Filter on relation between source value and compare value of type double.

` .google.cloud.clouddms.v1.DoubleComparisonFilter double_comparison = 103 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[DoubleComparisonFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DoubleComparisonFilter)` | The doubleComparison.  
  
### getDoubleComparisonOrBuilder()
    
    
    public abstract DoubleComparisonFilterOrBuilder getDoubleComparisonOrBuilder()

Optional. Filter on relation between source value and compare value of type double.

` .google.cloud.clouddms.v1.DoubleComparisonFilter double_comparison = 103 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[DoubleComparisonFilterOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.DoubleComparisonFilterOrBuilder)` |   
  
### getFilterCase()
    
    
    public abstract ValueTransformation.FilterCase getFilterCase()

**Returns**  
---  
**Type** | **Description**  
`[ValueTransformation.FilterCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ValueTransformation.FilterCase)` |   
  
### getIntComparison()
    
    
    public abstract IntComparisonFilter getIntComparison()

Optional. Filter on relation between source value and compare value of type integer.

` .google.cloud.clouddms.v1.IntComparisonFilter int_comparison = 102 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[IntComparisonFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.IntComparisonFilter)` | The intComparison.  
  
### getIntComparisonOrBuilder()
    
    
    public abstract IntComparisonFilterOrBuilder getIntComparisonOrBuilder()

Optional. Filter on relation between source value and compare value of type integer.

` .google.cloud.clouddms.v1.IntComparisonFilter int_comparison = 102 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[IntComparisonFilterOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.IntComparisonFilterOrBuilder)` |   
  
### getIsNull()
    
    
    public abstract Empty getIsNull()

Optional. Value is null

`.google.protobuf.Empty is_null = 100 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)` | The isNull.  
  
### getIsNullOrBuilder()
    
    
    public abstract EmptyOrBuilder getIsNullOrBuilder()

Optional. Value is null

`.google.protobuf.Empty is_null = 100 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[EmptyOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.EmptyOrBuilder.html)` |   
  
### getRoundScale()
    
    
    public abstract RoundToScale getRoundScale()

Optional. Allows the data to change scale

` .google.cloud.clouddms.v1.RoundToScale round_scale = 204 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[RoundToScale](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.RoundToScale)` | The roundScale.  
  
### getRoundScaleOrBuilder()
    
    
    public abstract RoundToScaleOrBuilder getRoundScaleOrBuilder()

Optional. Allows the data to change scale

` .google.cloud.clouddms.v1.RoundToScale round_scale = 204 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[RoundToScaleOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.RoundToScaleOrBuilder)` |   
  
### getValueList()
    
    
    public abstract ValueListFilter getValueList()

Optional. Value is found in the specified list.

` .google.cloud.clouddms.v1.ValueListFilter value_list = 101 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ValueListFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ValueListFilter)` | The valueList.  
  
### getValueListOrBuilder()
    
    
    public abstract ValueListFilterOrBuilder getValueListOrBuilder()

Optional. Value is found in the specified list.

` .google.cloud.clouddms.v1.ValueListFilter value_list = 101 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ValueListFilterOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dms/latest/com.google.cloud.clouddms.v1.ValueListFilterOrBuilder)` |   
  
### hasApplyHash()
    
    
    public abstract boolean hasApplyHash()

Optional. Applies a hash function on the data

` .google.cloud.clouddms.v1.ApplyHash apply_hash = 205 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the applyHash field is set.  
  
### hasAssignMaxValue()
    
    
    public abstract boolean hasAssignMaxValue()

Optional. Set to max_value - if integer or numeric, will use int.maxvalue, etc

`.google.protobuf.Empty assign_max_value = 203 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the assignMaxValue field is set.  
  
### hasAssignMinValue()
    
    
    public abstract boolean hasAssignMinValue()

Optional. Set to min_value - if integer or numeric, will use int.minvalue, etc

`.google.protobuf.Empty assign_min_value = 202 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the assignMinValue field is set.  
  
### hasAssignNull()
    
    
    public abstract boolean hasAssignNull()

Optional. Set to null

`.google.protobuf.Empty assign_null = 200 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the assignNull field is set.  
  
### hasAssignSpecificValue()
    
    
    public abstract boolean hasAssignSpecificValue()

Optional. Set to a specific value (value is converted to fit the target data type)

` .google.cloud.clouddms.v1.AssignSpecificValue assign_specific_value = 201 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the assignSpecificValue field is set.  
  
### hasDoubleComparison()
    
    
    public abstract boolean hasDoubleComparison()

Optional. Filter on relation between source value and compare value of type double.

` .google.cloud.clouddms.v1.DoubleComparisonFilter double_comparison = 103 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the doubleComparison field is set.  
  
### hasIntComparison()
    
    
    public abstract boolean hasIntComparison()

Optional. Filter on relation between source value and compare value of type integer.

` .google.cloud.clouddms.v1.IntComparisonFilter int_comparison = 102 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the intComparison field is set.  
  
### hasIsNull()
    
    
    public abstract boolean hasIsNull()

Optional. Value is null

`.google.protobuf.Empty is_null = 100 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the isNull field is set.  
  
### hasRoundScale()
    
    
    public abstract boolean hasRoundScale()

Optional. Allows the data to change scale

` .google.cloud.clouddms.v1.RoundToScale round_scale = 204 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the roundScale field is set.  
  
### hasValueList()
    
    
    public abstract boolean hasValueList()

Optional. Value is found in the specified list.

` .google.cloud.clouddms.v1.ValueListFilter value_list = 101 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the valueList field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
