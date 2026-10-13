---
url: https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CheckCompatibilityRequestOrBuilder
title: Interface CheckCompatibilityRequestOrBuilder (0.110.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:11:27.824604+00:00
---

# Interface CheckCompatibilityRequestOrBuilder (0.110.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CheckCompatibilityRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface CheckCompatibilityRequestOrBuilder (0.110.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.110.0 (latest)  0.106.0  0.105.0  0.104.0  0.102.0  0.99.0  0.98.0  0.96.0  0.94.0  0.93.0  0.92.0  0.91.0  0.89.0  0.87.0  0.86.0  0.85.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.75.0  0.74.0  0.73.0  0.71.0  0.70.0  0.69.0  0.68.0  0.67.0  0.66.0  0.65.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0 
    
    
    public interface CheckCompatibilityRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCompatibilityFilter()
    
    
    public abstract Compatibility getCompatibilityFilter()

Filters the dimensions and metrics in the response to just this compatibility. Commonly used as `”compatibilityFilter”: “COMPATIBLE”` to only return compatible dimensions & metrics.

`.google.analytics.data.v1beta.Compatibility compatibility_filter = 6;`

**Returns**  
---  
**Type** | **Description**  
`[Compatibility](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Compatibility)` | The compatibilityFilter.  
  
### getCompatibilityFilterValue()
    
    
    public abstract int getCompatibilityFilterValue()

Filters the dimensions and metrics in the response to just this compatibility. Commonly used as `”compatibilityFilter”: “COMPATIBLE”` to only return compatible dimensions & metrics.

`.google.analytics.data.v1beta.Compatibility compatibility_filter = 6;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for compatibilityFilter.  
  
### getDimensionFilter()
    
    
    public abstract FilterExpression getDimensionFilter()

The filter clause of dimensions. `dimensionFilter` should be the same value as in your `runReport` request.

`.google.analytics.data.v1beta.FilterExpression dimension_filter = 4;`

**Returns**  
---  
**Type** | **Description**  
`[FilterExpression](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.FilterExpression)` | The dimensionFilter.  
  
### getDimensionFilterOrBuilder()
    
    
    public abstract FilterExpressionOrBuilder getDimensionFilterOrBuilder()

The filter clause of dimensions. `dimensionFilter` should be the same value as in your `runReport` request.

`.google.analytics.data.v1beta.FilterExpression dimension_filter = 4;`

**Returns**  
---  
**Type** | **Description**  
`[FilterExpressionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.FilterExpressionOrBuilder)` |   
  
### getDimensions(int index)
    
    
    public abstract Dimension getDimensions(int index)

The dimensions in this report. `dimensions` should be the same value as in your `runReport` request.

`repeated .google.analytics.data.v1beta.Dimension dimensions = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Dimension](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Dimension)` |   
  
### getDimensionsCount()
    
    
    public abstract int getDimensionsCount()

The dimensions in this report. `dimensions` should be the same value as in your `runReport` request.

`repeated .google.analytics.data.v1beta.Dimension dimensions = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getDimensionsList()
    
    
    public abstract List<Dimension> getDimensionsList()

The dimensions in this report. `dimensions` should be the same value as in your `runReport` request.

`repeated .google.analytics.data.v1beta.Dimension dimensions = 2;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Dimension](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Dimension)>` |   
  
### getDimensionsOrBuilder(int index)
    
    
    public abstract DimensionOrBuilder getDimensionsOrBuilder(int index)

The dimensions in this report. `dimensions` should be the same value as in your `runReport` request.

`repeated .google.analytics.data.v1beta.Dimension dimensions = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DimensionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.DimensionOrBuilder)` |   
  
### getDimensionsOrBuilderList()
    
    
    public abstract List<? extends DimensionOrBuilder> getDimensionsOrBuilderList()

The dimensions in this report. `dimensions` should be the same value as in your `runReport` request.

`repeated .google.analytics.data.v1beta.Dimension dimensions = 2;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.analytics.data.v1beta.DimensionOrBuilder>` |   
  
### getMetricFilter()
    
    
    public abstract FilterExpression getMetricFilter()

The filter clause of metrics. `metricFilter` should be the same value as in your `runReport` request

`.google.analytics.data.v1beta.FilterExpression metric_filter = 5;`

**Returns**  
---  
**Type** | **Description**  
`[FilterExpression](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.FilterExpression)` | The metricFilter.  
  
### getMetricFilterOrBuilder()
    
    
    public abstract FilterExpressionOrBuilder getMetricFilterOrBuilder()

The filter clause of metrics. `metricFilter` should be the same value as in your `runReport` request

`.google.analytics.data.v1beta.FilterExpression metric_filter = 5;`

**Returns**  
---  
**Type** | **Description**  
`[FilterExpressionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.FilterExpressionOrBuilder)` |   
  
### getMetrics(int index)
    
    
    public abstract Metric getMetrics(int index)

The metrics in this report. `metrics` should be the same value as in your `runReport` request.

`repeated .google.analytics.data.v1beta.Metric metrics = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Metric](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Metric)` |   
  
### getMetricsCount()
    
    
    public abstract int getMetricsCount()

The metrics in this report. `metrics` should be the same value as in your `runReport` request.

`repeated .google.analytics.data.v1beta.Metric metrics = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getMetricsList()
    
    
    public abstract List<Metric> getMetricsList()

The metrics in this report. `metrics` should be the same value as in your `runReport` request.

`repeated .google.analytics.data.v1beta.Metric metrics = 3;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Metric](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Metric)>` |   
  
### getMetricsOrBuilder(int index)
    
    
    public abstract MetricOrBuilder getMetricsOrBuilder(int index)

The metrics in this report. `metrics` should be the same value as in your `runReport` request.

`repeated .google.analytics.data.v1beta.Metric metrics = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MetricOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.MetricOrBuilder)` |   
  
### getMetricsOrBuilderList()
    
    
    public abstract List<? extends MetricOrBuilder> getMetricsOrBuilderList()

The metrics in this report. `metrics` should be the same value as in your `runReport` request.

`repeated .google.analytics.data.v1beta.Metric metrics = 3;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.analytics.data.v1beta.MetricOrBuilder>` |   
  
### getProperty()
    
    
    public abstract String getProperty()

A Google Analytics property identifier whose events are tracked. To learn more, see [where to find your Property ID](https://developers.google.com/analytics/devguides/reporting/data/v1/property-id). `property` should be the same value as in your `runReport` request.

Example: properties/1234

`string property = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The property.  
  
### getPropertyBytes()
    
    
    public abstract ByteString getPropertyBytes()

A Google Analytics property identifier whose events are tracked. To learn more, see [where to find your Property ID](https://developers.google.com/analytics/devguides/reporting/data/v1/property-id). `property` should be the same value as in your `runReport` request.

Example: properties/1234

`string property = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for property.  
  
### hasDimensionFilter()
    
    
    public abstract boolean hasDimensionFilter()

The filter clause of dimensions. `dimensionFilter` should be the same value as in your `runReport` request.

`.google.analytics.data.v1beta.FilterExpression dimension_filter = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the dimensionFilter field is set.  
  
### hasMetricFilter()
    
    
    public abstract boolean hasMetricFilter()

The filter clause of metrics. `metricFilter` should be the same value as in your `runReport` request

`.google.analytics.data.v1beta.FilterExpression metric_filter = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the metricFilter field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
