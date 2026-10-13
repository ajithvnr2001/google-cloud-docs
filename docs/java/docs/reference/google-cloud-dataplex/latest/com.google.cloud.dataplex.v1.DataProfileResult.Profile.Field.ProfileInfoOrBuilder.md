---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProfileResult.Profile.Field.ProfileInfoOrBuilder
title: Interface DataProfileResult.Profile.Field.ProfileInfoOrBuilder (1.97.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:44:08.238835+00:00
---

# Interface DataProfileResult.Profile.Field.ProfileInfoOrBuilder (1.97.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProfileResult.Profile.Field.ProfileInfoOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface DataProfileResult.Profile.Field.ProfileInfoOrBuilder (1.97.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.97.0 (latest)  1.93.0  1.92.0  1.91.0  1.89.0  1.86.0  1.85.0  1.83.0  1.81.0  1.80.0  1.79.0  1.78.0  1.76.0  1.74.0  1.73.0  1.72.0  1.71.0  1.70.0  1.68.0  1.66.0  1.65.0  1.62.0  1.61.0  1.60.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.2  1.0.1  0.2.2 
    
    
    public static interface DataProfileResult.Profile.Field.ProfileInfoOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getDistinctRatio()
    
    
    public abstract double getDistinctRatio()

Output only. Ratio of rows with distinct values against total scanned rows. Not available for complex non-groupable field type, including RECORD, ARRAY, GEOGRAPHY, and JSON, as well as fields with REPEATABLE mode.

`double distinct_ratio = 3 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The distinctRatio.  
  
### getDoubleProfile()
    
    
    public abstract DataProfileResult.Profile.Field.ProfileInfo.DoubleFieldInfo getDoubleProfile()

Double type field information.

` .google.cloud.dataplex.v1.DataProfileResult.Profile.Field.ProfileInfo.DoubleFieldInfo double_profile = 103; `

**Returns**  
---  
**Type** | **Description**  
`[DataProfileResult.Profile.Field.ProfileInfo.DoubleFieldInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProfileResult.Profile.Field.ProfileInfo.DoubleFieldInfo)` | The doubleProfile.  
  
### getDoubleProfileOrBuilder()
    
    
    public abstract DataProfileResult.Profile.Field.ProfileInfo.DoubleFieldInfoOrBuilder getDoubleProfileOrBuilder()

Double type field information.

` .google.cloud.dataplex.v1.DataProfileResult.Profile.Field.ProfileInfo.DoubleFieldInfo double_profile = 103; `

**Returns**  
---  
**Type** | **Description**  
`[DataProfileResult.Profile.Field.ProfileInfo.DoubleFieldInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProfileResult.Profile.Field.ProfileInfo.DoubleFieldInfoOrBuilder)` |   
  
### getFieldInfoCase()
    
    
    public abstract DataProfileResult.Profile.Field.ProfileInfo.FieldInfoCase getFieldInfoCase()

**Returns**  
---  
**Type** | **Description**  
`[DataProfileResult.Profile.Field.ProfileInfo.FieldInfoCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProfileResult.Profile.Field.ProfileInfo.FieldInfoCase)` |   
  
### getIntegerProfile()
    
    
    public abstract DataProfileResult.Profile.Field.ProfileInfo.IntegerFieldInfo getIntegerProfile()

Integer type field information.

` .google.cloud.dataplex.v1.DataProfileResult.Profile.Field.ProfileInfo.IntegerFieldInfo integer_profile = 102; `

**Returns**  
---  
**Type** | **Description**  
`[DataProfileResult.Profile.Field.ProfileInfo.IntegerFieldInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProfileResult.Profile.Field.ProfileInfo.IntegerFieldInfo)` | The integerProfile.  
  
### getIntegerProfileOrBuilder()
    
    
    public abstract DataProfileResult.Profile.Field.ProfileInfo.IntegerFieldInfoOrBuilder getIntegerProfileOrBuilder()

Integer type field information.

` .google.cloud.dataplex.v1.DataProfileResult.Profile.Field.ProfileInfo.IntegerFieldInfo integer_profile = 102; `

**Returns**  
---  
**Type** | **Description**  
`[DataProfileResult.Profile.Field.ProfileInfo.IntegerFieldInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProfileResult.Profile.Field.ProfileInfo.IntegerFieldInfoOrBuilder)` |   
  
### getNullRatio()
    
    
    public abstract double getNullRatio()

Output only. Ratio of rows with null value against total scanned rows.

`double null_ratio = 2 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The nullRatio.  
  
### getStringProfile()
    
    
    public abstract DataProfileResult.Profile.Field.ProfileInfo.StringFieldInfo getStringProfile()

String type field information.

` .google.cloud.dataplex.v1.DataProfileResult.Profile.Field.ProfileInfo.StringFieldInfo string_profile = 101; `

**Returns**  
---  
**Type** | **Description**  
`[DataProfileResult.Profile.Field.ProfileInfo.StringFieldInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProfileResult.Profile.Field.ProfileInfo.StringFieldInfo)` | The stringProfile.  
  
### getStringProfileOrBuilder()
    
    
    public abstract DataProfileResult.Profile.Field.ProfileInfo.StringFieldInfoOrBuilder getStringProfileOrBuilder()

String type field information.

` .google.cloud.dataplex.v1.DataProfileResult.Profile.Field.ProfileInfo.StringFieldInfo string_profile = 101; `

**Returns**  
---  
**Type** | **Description**  
`[DataProfileResult.Profile.Field.ProfileInfo.StringFieldInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProfileResult.Profile.Field.ProfileInfo.StringFieldInfoOrBuilder)` |   
  
### getTopNValues(int index)
    
    
    public abstract DataProfileResult.Profile.Field.ProfileInfo.TopNValue getTopNValues(int index)

Output only. The list of top N non-null values, frequency and ratio with which they occur in the scanned data. N is 10 or equal to the number of distinct values in the field, whichever is smaller. Not available for complex non-groupable field type, including RECORD, ARRAY, GEOGRAPHY, and JSON, as well as fields with REPEATABLE mode.

` repeated .google.cloud.dataplex.v1.DataProfileResult.Profile.Field.ProfileInfo.TopNValue top_n_values = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataProfileResult.Profile.Field.ProfileInfo.TopNValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProfileResult.Profile.Field.ProfileInfo.TopNValue)` |   
  
### getTopNValuesCount()
    
    
    public abstract int getTopNValuesCount()

Output only. The list of top N non-null values, frequency and ratio with which they occur in the scanned data. N is 10 or equal to the number of distinct values in the field, whichever is smaller. Not available for complex non-groupable field type, including RECORD, ARRAY, GEOGRAPHY, and JSON, as well as fields with REPEATABLE mode.

` repeated .google.cloud.dataplex.v1.DataProfileResult.Profile.Field.ProfileInfo.TopNValue top_n_values = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getTopNValuesList()
    
    
    public abstract List<DataProfileResult.Profile.Field.ProfileInfo.TopNValue> getTopNValuesList()

Output only. The list of top N non-null values, frequency and ratio with which they occur in the scanned data. N is 10 or equal to the number of distinct values in the field, whichever is smaller. Not available for complex non-groupable field type, including RECORD, ARRAY, GEOGRAPHY, and JSON, as well as fields with REPEATABLE mode.

` repeated .google.cloud.dataplex.v1.DataProfileResult.Profile.Field.ProfileInfo.TopNValue top_n_values = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[TopNValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProfileResult.Profile.Field.ProfileInfo.TopNValue)>` |   
  
### getTopNValuesOrBuilder(int index)
    
    
    public abstract DataProfileResult.Profile.Field.ProfileInfo.TopNValueOrBuilder getTopNValuesOrBuilder(int index)

Output only. The list of top N non-null values, frequency and ratio with which they occur in the scanned data. N is 10 or equal to the number of distinct values in the field, whichever is smaller. Not available for complex non-groupable field type, including RECORD, ARRAY, GEOGRAPHY, and JSON, as well as fields with REPEATABLE mode.

` repeated .google.cloud.dataplex.v1.DataProfileResult.Profile.Field.ProfileInfo.TopNValue top_n_values = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataProfileResult.Profile.Field.ProfileInfo.TopNValueOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProfileResult.Profile.Field.ProfileInfo.TopNValueOrBuilder)` |   
  
### getTopNValuesOrBuilderList()
    
    
    public abstract List<? extends DataProfileResult.Profile.Field.ProfileInfo.TopNValueOrBuilder> getTopNValuesOrBuilderList()

Output only. The list of top N non-null values, frequency and ratio with which they occur in the scanned data. N is 10 or equal to the number of distinct values in the field, whichever is smaller. Not available for complex non-groupable field type, including RECORD, ARRAY, GEOGRAPHY, and JSON, as well as fields with REPEATABLE mode.

` repeated .google.cloud.dataplex.v1.DataProfileResult.Profile.Field.ProfileInfo.TopNValue top_n_values = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.dataplex.v1.DataProfileResult.Profile.Field.ProfileInfo.TopNValueOrBuilder>` |   
  
### hasDoubleProfile()
    
    
    public abstract boolean hasDoubleProfile()

Double type field information.

` .google.cloud.dataplex.v1.DataProfileResult.Profile.Field.ProfileInfo.DoubleFieldInfo double_profile = 103; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the doubleProfile field is set.  
  
### hasIntegerProfile()
    
    
    public abstract boolean hasIntegerProfile()

Integer type field information.

` .google.cloud.dataplex.v1.DataProfileResult.Profile.Field.ProfileInfo.IntegerFieldInfo integer_profile = 102; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the integerProfile field is set.  
  
### hasStringProfile()
    
    
    public abstract boolean hasStringProfile()

String type field information.

` .google.cloud.dataplex.v1.DataProfileResult.Profile.Field.ProfileInfo.StringFieldInfo string_profile = 101; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the stringProfile field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
