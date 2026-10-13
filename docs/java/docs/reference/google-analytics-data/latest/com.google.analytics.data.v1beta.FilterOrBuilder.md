---
url: https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.FilterOrBuilder
title: Interface FilterOrBuilder (0.110.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:11:31.852181+00:00
---

# Interface FilterOrBuilder (0.110.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.FilterOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface FilterOrBuilder (0.110.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.110.0 (latest)  0.106.0  0.105.0  0.104.0  0.102.0  0.99.0  0.98.0  0.96.0  0.94.0  0.93.0  0.92.0  0.91.0  0.89.0  0.87.0  0.86.0  0.85.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.75.0  0.74.0  0.73.0  0.71.0  0.70.0  0.69.0  0.68.0  0.67.0  0.66.0  0.65.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0 
    
    
    public interface FilterOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getBetweenFilter()
    
    
    public abstract Filter.BetweenFilter getBetweenFilter()

A filter for two values.

`.google.analytics.data.v1beta.Filter.BetweenFilter between_filter = 6;`

**Returns**  
---  
**Type** | **Description**  
`[Filter.BetweenFilter](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Filter.BetweenFilter)` | The betweenFilter.  
  
### getBetweenFilterOrBuilder()
    
    
    public abstract Filter.BetweenFilterOrBuilder getBetweenFilterOrBuilder()

A filter for two values.

`.google.analytics.data.v1beta.Filter.BetweenFilter between_filter = 6;`

**Returns**  
---  
**Type** | **Description**  
`[Filter.BetweenFilterOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Filter.BetweenFilterOrBuilder)` |   
  
### getEmptyFilter()
    
    
    public abstract Filter.EmptyFilter getEmptyFilter()

A filter for empty values such as "(not set)" and "" values.

`.google.analytics.data.v1beta.Filter.EmptyFilter empty_filter = 8;`

**Returns**  
---  
**Type** | **Description**  
`[Filter.EmptyFilter](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Filter.EmptyFilter)` | The emptyFilter.  
  
### getEmptyFilterOrBuilder()
    
    
    public abstract Filter.EmptyFilterOrBuilder getEmptyFilterOrBuilder()

A filter for empty values such as "(not set)" and "" values.

`.google.analytics.data.v1beta.Filter.EmptyFilter empty_filter = 8;`

**Returns**  
---  
**Type** | **Description**  
`[Filter.EmptyFilterOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Filter.EmptyFilterOrBuilder)` |   
  
### getFieldName()
    
    
    public abstract String getFieldName()

The dimension name or metric name.

In most methods, dimensions & metrics can be used for the first time in this field. However in a RunPivotReportRequest, this field must be additionally specified by name in the RunPivotReportRequest's dimensions or metrics.

`string field_name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The fieldName.  
  
### getFieldNameBytes()
    
    
    public abstract ByteString getFieldNameBytes()

The dimension name or metric name.

In most methods, dimensions & metrics can be used for the first time in this field. However in a RunPivotReportRequest, this field must be additionally specified by name in the RunPivotReportRequest's dimensions or metrics.

`string field_name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for fieldName.  
  
### getInListFilter()
    
    
    public abstract Filter.InListFilter getInListFilter()

A filter for in list values.

`.google.analytics.data.v1beta.Filter.InListFilter in_list_filter = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Filter.InListFilter](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Filter.InListFilter)` | The inListFilter.  
  
### getInListFilterOrBuilder()
    
    
    public abstract Filter.InListFilterOrBuilder getInListFilterOrBuilder()

A filter for in list values.

`.google.analytics.data.v1beta.Filter.InListFilter in_list_filter = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Filter.InListFilterOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Filter.InListFilterOrBuilder)` |   
  
### getNumericFilter()
    
    
    public abstract Filter.NumericFilter getNumericFilter()

A filter for numeric or date values.

`.google.analytics.data.v1beta.Filter.NumericFilter numeric_filter = 5;`

**Returns**  
---  
**Type** | **Description**  
`[Filter.NumericFilter](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Filter.NumericFilter)` | The numericFilter.  
  
### getNumericFilterOrBuilder()
    
    
    public abstract Filter.NumericFilterOrBuilder getNumericFilterOrBuilder()

A filter for numeric or date values.

`.google.analytics.data.v1beta.Filter.NumericFilter numeric_filter = 5;`

**Returns**  
---  
**Type** | **Description**  
`[Filter.NumericFilterOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Filter.NumericFilterOrBuilder)` |   
  
### getOneFilterCase()
    
    
    public abstract Filter.OneFilterCase getOneFilterCase()

**Returns**  
---  
**Type** | **Description**  
`[Filter.OneFilterCase](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Filter.OneFilterCase)` |   
  
### getStringFilter()
    
    
    public abstract Filter.StringFilter getStringFilter()

Strings related filter.

`.google.analytics.data.v1beta.Filter.StringFilter string_filter = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Filter.StringFilter](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Filter.StringFilter)` | The stringFilter.  
  
### getStringFilterOrBuilder()
    
    
    public abstract Filter.StringFilterOrBuilder getStringFilterOrBuilder()

Strings related filter.

`.google.analytics.data.v1beta.Filter.StringFilter string_filter = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Filter.StringFilterOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Filter.StringFilterOrBuilder)` |   
  
### hasBetweenFilter()
    
    
    public abstract boolean hasBetweenFilter()

A filter for two values.

`.google.analytics.data.v1beta.Filter.BetweenFilter between_filter = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the betweenFilter field is set.  
  
### hasEmptyFilter()
    
    
    public abstract boolean hasEmptyFilter()

A filter for empty values such as "(not set)" and "" values.

`.google.analytics.data.v1beta.Filter.EmptyFilter empty_filter = 8;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the emptyFilter field is set.  
  
### hasInListFilter()
    
    
    public abstract boolean hasInListFilter()

A filter for in list values.

`.google.analytics.data.v1beta.Filter.InListFilter in_list_filter = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the inListFilter field is set.  
  
### hasNumericFilter()
    
    
    public abstract boolean hasNumericFilter()

A filter for numeric or date values.

`.google.analytics.data.v1beta.Filter.NumericFilter numeric_filter = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the numericFilter field is set.  
  
### hasStringFilter()
    
    
    public abstract boolean hasStringFilter()

Strings related filter.

`.google.analytics.data.v1beta.Filter.StringFilter string_filter = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the stringFilter field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
