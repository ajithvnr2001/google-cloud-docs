---
url: https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.MetadataOrBuilder
title: Interface MetadataOrBuilder (0.110.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:11:33.076664+00:00
---

# Interface MetadataOrBuilder (0.110.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.MetadataOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface MetadataOrBuilder (0.110.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.110.0 (latest)  0.106.0  0.105.0  0.104.0  0.102.0  0.99.0  0.98.0  0.96.0  0.94.0  0.93.0  0.92.0  0.91.0  0.89.0  0.87.0  0.86.0  0.85.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.75.0  0.74.0  0.73.0  0.71.0  0.70.0  0.69.0  0.68.0  0.67.0  0.66.0  0.65.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0 
    
    
    public interface MetadataOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getComparisons(int index)
    
    
    public abstract ComparisonMetadata getComparisons(int index)

The comparison descriptions.

`repeated .google.analytics.data.v1beta.ComparisonMetadata comparisons = 4;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ComparisonMetadata](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.ComparisonMetadata)` |   
  
### getComparisonsCount()
    
    
    public abstract int getComparisonsCount()

The comparison descriptions.

`repeated .google.analytics.data.v1beta.ComparisonMetadata comparisons = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getComparisonsList()
    
    
    public abstract List<ComparisonMetadata> getComparisonsList()

The comparison descriptions.

`repeated .google.analytics.data.v1beta.ComparisonMetadata comparisons = 4;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ComparisonMetadata](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.ComparisonMetadata)>` |   
  
### getComparisonsOrBuilder(int index)
    
    
    public abstract ComparisonMetadataOrBuilder getComparisonsOrBuilder(int index)

The comparison descriptions.

`repeated .google.analytics.data.v1beta.ComparisonMetadata comparisons = 4;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ComparisonMetadataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.ComparisonMetadataOrBuilder)` |   
  
### getComparisonsOrBuilderList()
    
    
    public abstract List<? extends ComparisonMetadataOrBuilder> getComparisonsOrBuilderList()

The comparison descriptions.

`repeated .google.analytics.data.v1beta.ComparisonMetadata comparisons = 4;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.analytics.data.v1beta.ComparisonMetadataOrBuilder>` |   
  
### getDimensions(int index)
    
    
    public abstract DimensionMetadata getDimensions(int index)

The dimension descriptions.

`repeated .google.analytics.data.v1beta.DimensionMetadata dimensions = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DimensionMetadata](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.DimensionMetadata)` |   
  
### getDimensionsCount()
    
    
    public abstract int getDimensionsCount()

The dimension descriptions.

`repeated .google.analytics.data.v1beta.DimensionMetadata dimensions = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getDimensionsList()
    
    
    public abstract List<DimensionMetadata> getDimensionsList()

The dimension descriptions.

`repeated .google.analytics.data.v1beta.DimensionMetadata dimensions = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[DimensionMetadata](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.DimensionMetadata)>` |   
  
### getDimensionsOrBuilder(int index)
    
    
    public abstract DimensionMetadataOrBuilder getDimensionsOrBuilder(int index)

The dimension descriptions.

`repeated .google.analytics.data.v1beta.DimensionMetadata dimensions = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DimensionMetadataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.DimensionMetadataOrBuilder)` |   
  
### getDimensionsOrBuilderList()
    
    
    public abstract List<? extends DimensionMetadataOrBuilder> getDimensionsOrBuilderList()

The dimension descriptions.

`repeated .google.analytics.data.v1beta.DimensionMetadata dimensions = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.analytics.data.v1beta.DimensionMetadataOrBuilder>` |   
  
### getMetrics(int index)
    
    
    public abstract MetricMetadata getMetrics(int index)

The metric descriptions.

`repeated .google.analytics.data.v1beta.MetricMetadata metrics = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MetricMetadata](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.MetricMetadata)` |   
  
### getMetricsCount()
    
    
    public abstract int getMetricsCount()

The metric descriptions.

`repeated .google.analytics.data.v1beta.MetricMetadata metrics = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getMetricsList()
    
    
    public abstract List<MetricMetadata> getMetricsList()

The metric descriptions.

`repeated .google.analytics.data.v1beta.MetricMetadata metrics = 2;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[MetricMetadata](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.MetricMetadata)>` |   
  
### getMetricsOrBuilder(int index)
    
    
    public abstract MetricMetadataOrBuilder getMetricsOrBuilder(int index)

The metric descriptions.

`repeated .google.analytics.data.v1beta.MetricMetadata metrics = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MetricMetadataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.MetricMetadataOrBuilder)` |   
  
### getMetricsOrBuilderList()
    
    
    public abstract List<? extends MetricMetadataOrBuilder> getMetricsOrBuilderList()

The metric descriptions.

`repeated .google.analytics.data.v1beta.MetricMetadata metrics = 2;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.analytics.data.v1beta.MetricMetadataOrBuilder>` |   
  
### getName()
    
    
    public abstract String getName()

Resource name of this metadata.

`string name = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Resource name of this metadata.

`string name = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
