---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.DashboardChart.Visualization.TableConfigOrBuilder
title: Interface DashboardChart.Visualization.TableConfigOrBuilder (0.37.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:19:03.485489+00:00
---

# Interface DashboardChart.Visualization.TableConfigOrBuilder (0.37.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.DashboardChart.Visualization.TableConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface DashboardChart.Visualization.TableConfigOrBuilder (0.37.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.37.0 (latest)  0.33.0  0.32.0  0.31.0  0.29.0  0.26.0  0.25.0  0.23.0  0.21.0  0.20.0  0.19.0  0.18.0  0.16.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.6.0  0.5.0  0.2.0  0.1.0 
    
    
    public static interface DashboardChart.Visualization.TableConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getColumnRenderTypeSettings(int index)
    
    
    public abstract DashboardChart.Visualization.ColumnRenderTypeSettings getColumnRenderTypeSettings(int index)

Optional. Column render type settings.

` repeated .google.cloud.chronicle.v1.DashboardChart.Visualization.ColumnRenderTypeSettings column_render_type_settings = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DashboardChart.Visualization.ColumnRenderTypeSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.DashboardChart.Visualization.ColumnRenderTypeSettings)` |   
  
### getColumnRenderTypeSettingsCount()
    
    
    public abstract int getColumnRenderTypeSettingsCount()

Optional. Column render type settings.

` repeated .google.cloud.chronicle.v1.DashboardChart.Visualization.ColumnRenderTypeSettings column_render_type_settings = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getColumnRenderTypeSettingsList()
    
    
    public abstract List<DashboardChart.Visualization.ColumnRenderTypeSettings> getColumnRenderTypeSettingsList()

Optional. Column render type settings.

` repeated .google.cloud.chronicle.v1.DashboardChart.Visualization.ColumnRenderTypeSettings column_render_type_settings = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ColumnRenderTypeSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.DashboardChart.Visualization.ColumnRenderTypeSettings)>` |   
  
### getColumnRenderTypeSettingsOrBuilder(int index)
    
    
    public abstract DashboardChart.Visualization.ColumnRenderTypeSettingsOrBuilder getColumnRenderTypeSettingsOrBuilder(int index)

Optional. Column render type settings.

` repeated .google.cloud.chronicle.v1.DashboardChart.Visualization.ColumnRenderTypeSettings column_render_type_settings = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DashboardChart.Visualization.ColumnRenderTypeSettingsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.DashboardChart.Visualization.ColumnRenderTypeSettingsOrBuilder)` |   
  
### getColumnRenderTypeSettingsOrBuilderList()
    
    
    public abstract List<? extends DashboardChart.Visualization.ColumnRenderTypeSettingsOrBuilder> getColumnRenderTypeSettingsOrBuilderList()

Optional. Column render type settings.

` repeated .google.cloud.chronicle.v1.DashboardChart.Visualization.ColumnRenderTypeSettings column_render_type_settings = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.chronicle.v1.DashboardChart.Visualization.ColumnRenderTypeSettingsOrBuilder>` |   
  
### getColumnTooltipSettings(int index)
    
    
    public abstract DashboardChart.Visualization.ColumnTooltipSettings getColumnTooltipSettings(int index)

Optional. Settings for tooltip for column header and cell.

` repeated .google.cloud.chronicle.v1.DashboardChart.Visualization.ColumnTooltipSettings column_tooltip_settings = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DashboardChart.Visualization.ColumnTooltipSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.DashboardChart.Visualization.ColumnTooltipSettings)` |   
  
### getColumnTooltipSettingsCount()
    
    
    public abstract int getColumnTooltipSettingsCount()

Optional. Settings for tooltip for column header and cell.

` repeated .google.cloud.chronicle.v1.DashboardChart.Visualization.ColumnTooltipSettings column_tooltip_settings = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getColumnTooltipSettingsList()
    
    
    public abstract List<DashboardChart.Visualization.ColumnTooltipSettings> getColumnTooltipSettingsList()

Optional. Settings for tooltip for column header and cell.

` repeated .google.cloud.chronicle.v1.DashboardChart.Visualization.ColumnTooltipSettings column_tooltip_settings = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ColumnTooltipSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.DashboardChart.Visualization.ColumnTooltipSettings)>` |   
  
### getColumnTooltipSettingsOrBuilder(int index)
    
    
    public abstract DashboardChart.Visualization.ColumnTooltipSettingsOrBuilder getColumnTooltipSettingsOrBuilder(int index)

Optional. Settings for tooltip for column header and cell.

` repeated .google.cloud.chronicle.v1.DashboardChart.Visualization.ColumnTooltipSettings column_tooltip_settings = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DashboardChart.Visualization.ColumnTooltipSettingsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.DashboardChart.Visualization.ColumnTooltipSettingsOrBuilder)` |   
  
### getColumnTooltipSettingsOrBuilderList()
    
    
    public abstract List<? extends DashboardChart.Visualization.ColumnTooltipSettingsOrBuilder> getColumnTooltipSettingsOrBuilderList()

Optional. Settings for tooltip for column header and cell.

` repeated .google.cloud.chronicle.v1.DashboardChart.Visualization.ColumnTooltipSettings column_tooltip_settings = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.chronicle.v1.DashboardChart.Visualization.ColumnTooltipSettingsOrBuilder>` |   
  
### getEnableTextWrap()
    
    
    public abstract boolean getEnableTextWrap()

Optional. Whether to show the table.

`bool enable_text_wrap = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enableTextWrap.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
