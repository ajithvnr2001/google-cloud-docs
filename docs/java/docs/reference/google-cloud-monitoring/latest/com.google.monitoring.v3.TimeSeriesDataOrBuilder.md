---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.TimeSeriesDataOrBuilder
title: Interface TimeSeriesDataOrBuilder (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:26:38.469812+00:00
---

# Interface TimeSeriesDataOrBuilder (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.TimeSeriesDataOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface TimeSeriesDataOrBuilder (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.6  3.3.6  3.2.10 
    
    
    public interface TimeSeriesDataOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getLabelValues(int index)
    
    
    public abstract LabelValue getLabelValues(int index)

The values of the labels in the time series identifier, given in the same order as the `label_descriptors` field of the TimeSeriesDescriptor associated with this object. Each value must have a value of the type given in the corresponding entry of `label_descriptors`.

`repeated .google.monitoring.v3.LabelValue label_values = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LabelValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.LabelValue)` |   
  
### getLabelValuesCount()
    
    
    public abstract int getLabelValuesCount()

The values of the labels in the time series identifier, given in the same order as the `label_descriptors` field of the TimeSeriesDescriptor associated with this object. Each value must have a value of the type given in the corresponding entry of `label_descriptors`.

`repeated .google.monitoring.v3.LabelValue label_values = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLabelValuesList()
    
    
    public abstract List<LabelValue> getLabelValuesList()

The values of the labels in the time series identifier, given in the same order as the `label_descriptors` field of the TimeSeriesDescriptor associated with this object. Each value must have a value of the type given in the corresponding entry of `label_descriptors`.

`repeated .google.monitoring.v3.LabelValue label_values = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[LabelValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.LabelValue)>` |   
  
### getLabelValuesOrBuilder(int index)
    
    
    public abstract LabelValueOrBuilder getLabelValuesOrBuilder(int index)

The values of the labels in the time series identifier, given in the same order as the `label_descriptors` field of the TimeSeriesDescriptor associated with this object. Each value must have a value of the type given in the corresponding entry of `label_descriptors`.

`repeated .google.monitoring.v3.LabelValue label_values = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LabelValueOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.LabelValueOrBuilder)` |   
  
### getLabelValuesOrBuilderList()
    
    
    public abstract List<? extends LabelValueOrBuilder> getLabelValuesOrBuilderList()

The values of the labels in the time series identifier, given in the same order as the `label_descriptors` field of the TimeSeriesDescriptor associated with this object. Each value must have a value of the type given in the corresponding entry of `label_descriptors`.

`repeated .google.monitoring.v3.LabelValue label_values = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.monitoring.v3.LabelValueOrBuilder>` |   
  
### getPointData(int index)
    
    
    public abstract TimeSeriesData.PointData getPointData(int index)

The points in the time series.

`repeated .google.monitoring.v3.TimeSeriesData.PointData point_data = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TimeSeriesData.PointData](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.TimeSeriesData.PointData)` |   
  
### getPointDataCount()
    
    
    public abstract int getPointDataCount()

The points in the time series.

`repeated .google.monitoring.v3.TimeSeriesData.PointData point_data = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getPointDataList()
    
    
    public abstract List<TimeSeriesData.PointData> getPointDataList()

The points in the time series.

`repeated .google.monitoring.v3.TimeSeriesData.PointData point_data = 2;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[PointData](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.TimeSeriesData.PointData)>` |   
  
### getPointDataOrBuilder(int index)
    
    
    public abstract TimeSeriesData.PointDataOrBuilder getPointDataOrBuilder(int index)

The points in the time series.

`repeated .google.monitoring.v3.TimeSeriesData.PointData point_data = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TimeSeriesData.PointDataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.TimeSeriesData.PointDataOrBuilder)` |   
  
### getPointDataOrBuilderList()
    
    
    public abstract List<? extends TimeSeriesData.PointDataOrBuilder> getPointDataOrBuilderList()

The points in the time series.

`repeated .google.monitoring.v3.TimeSeriesData.PointData point_data = 2;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.monitoring.v3.TimeSeriesData.PointDataOrBuilder>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
