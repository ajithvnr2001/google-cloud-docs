---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.DashboardDefinition.ChartConfigOrBuilder
title: Interface DashboardDefinition.ChartConfigOrBuilder (0.37.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:55:51.552893+00:00
---

# Interface DashboardDefinition.ChartConfigOrBuilder (0.37.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.DashboardDefinition.ChartConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface DashboardDefinition.ChartConfigOrBuilder (0.37.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.37.0 (latest)  0.33.0  0.32.0  0.31.0  0.29.0  0.26.0  0.25.0  0.23.0  0.21.0  0.20.0  0.19.0  0.18.0  0.16.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.6.0  0.5.0  0.2.0  0.1.0 
    
    
    public static interface DashboardDefinition.ChartConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getChartLayout()
    
    
    public abstract DashboardDefinition.ChartConfig.ChartLayout getChartLayout()

` .google.cloud.chronicle.v1.DashboardDefinition.ChartConfig.ChartLayout chart_layout = 2; `

**Returns**  
---  
**Type** | **Description**  
`[DashboardDefinition.ChartConfig.ChartLayout](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.DashboardDefinition.ChartConfig.ChartLayout)` | The chartLayout.  
  
### getChartLayoutOrBuilder()
    
    
    public abstract DashboardDefinition.ChartConfig.ChartLayoutOrBuilder getChartLayoutOrBuilder()

` .google.cloud.chronicle.v1.DashboardDefinition.ChartConfig.ChartLayout chart_layout = 2; `

**Returns**  
---  
**Type** | **Description**  
`[DashboardDefinition.ChartConfig.ChartLayoutOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.DashboardDefinition.ChartConfig.ChartLayoutOrBuilder)` |   
  
### getDashboardChart()
    
    
    public abstract String getDashboardChart()

` string dashboard_chart = 1 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The dashboardChart.  
  
### getDashboardChartBytes()
    
    
    public abstract ByteString getDashboardChartBytes()

` string dashboard_chart = 1 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for dashboardChart.  
  
### getFiltersIds(int index)
    
    
    public abstract String getFiltersIds(int index)

Dashboard filters applied to the chart.

`repeated string filters_ids = 4;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The filtersIds at the given index.  
  
### getFiltersIdsBytes(int index)
    
    
    public abstract ByteString getFiltersIdsBytes(int index)

Dashboard filters applied to the chart.

`repeated string filters_ids = 4;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the filtersIds at the given index.  
  
### getFiltersIdsCount()
    
    
    public abstract int getFiltersIdsCount()

Dashboard filters applied to the chart.

`repeated string filters_ids = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of filtersIds.  
  
### getFiltersIdsList()
    
    
    public abstract List<String> getFiltersIdsList()

Dashboard filters applied to the chart.

`repeated string filters_ids = 4;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the filtersIds.  
  
### hasChartLayout()
    
    
    public abstract boolean hasChartLayout()

` .google.cloud.chronicle.v1.DashboardDefinition.ChartConfig.ChartLayout chart_layout = 2; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the chartLayout field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
