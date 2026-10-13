---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.DashboardChart.Visualization.VisualMapOrBuilder
title: Interface DashboardChart.Visualization.VisualMapOrBuilder (0.37.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:43:53.354982+00:00
---

# Interface DashboardChart.Visualization.VisualMapOrBuilder (0.37.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.DashboardChart.Visualization.VisualMapOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface DashboardChart.Visualization.VisualMapOrBuilder (0.37.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.37.0 (latest)  0.33.0  0.32.0  0.31.0  0.29.0  0.26.0  0.25.0  0.23.0  0.21.0  0.20.0  0.19.0  0.18.0  0.16.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.6.0  0.5.0  0.2.0  0.1.0 
    
    
    public static interface DashboardChart.Visualization.VisualMapOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getPieces(int index)
    
    
    public abstract DashboardChart.Visualization.VisualMap.VisualMapPiece getPieces(int index)

Optional. Pieces of the visual map.

` repeated .google.cloud.chronicle.v1.DashboardChart.Visualization.VisualMap.VisualMapPiece pieces = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DashboardChart.Visualization.VisualMap.VisualMapPiece](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.DashboardChart.Visualization.VisualMap.VisualMapPiece)` |   
  
### getPiecesCount()
    
    
    public abstract int getPiecesCount()

Optional. Pieces of the visual map.

` repeated .google.cloud.chronicle.v1.DashboardChart.Visualization.VisualMap.VisualMapPiece pieces = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getPiecesList()
    
    
    public abstract List<DashboardChart.Visualization.VisualMap.VisualMapPiece> getPiecesList()

Optional. Pieces of the visual map.

` repeated .google.cloud.chronicle.v1.DashboardChart.Visualization.VisualMap.VisualMapPiece pieces = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[VisualMapPiece](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.DashboardChart.Visualization.VisualMap.VisualMapPiece)>` |   
  
### getPiecesOrBuilder(int index)
    
    
    public abstract DashboardChart.Visualization.VisualMap.VisualMapPieceOrBuilder getPiecesOrBuilder(int index)

Optional. Pieces of the visual map.

` repeated .google.cloud.chronicle.v1.DashboardChart.Visualization.VisualMap.VisualMapPiece pieces = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DashboardChart.Visualization.VisualMap.VisualMapPieceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.DashboardChart.Visualization.VisualMap.VisualMapPieceOrBuilder)` |   
  
### getPiecesOrBuilderList()
    
    
    public abstract List<? extends DashboardChart.Visualization.VisualMap.VisualMapPieceOrBuilder> getPiecesOrBuilderList()

Optional. Pieces of the visual map.

` repeated .google.cloud.chronicle.v1.DashboardChart.Visualization.VisualMap.VisualMapPiece pieces = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.chronicle.v1.DashboardChart.Visualization.VisualMap.VisualMapPieceOrBuilder>` |   
  
### getVisualMapType()
    
    
    public abstract VisualMapType getVisualMapType()

Optional. Contains one of the valid visual map types such as 'continuous' or 'piecewise'.

` .google.cloud.chronicle.v1.VisualMapType visual_map_type = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[VisualMapType](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.VisualMapType)` | The visualMapType.  
  
### getVisualMapTypeValue()
    
    
    public abstract int getVisualMapTypeValue()

Optional. Contains one of the valid visual map types such as 'continuous' or 'piecewise'.

` .google.cloud.chronicle.v1.VisualMapType visual_map_type = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for visualMapType.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
