---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-chronicle/latest/google.cloud.chronicle_v1.types.DashboardChart
title: Class DashboardChart (0.6.4) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:11:24.855519+00:00
---

# Class DashboardChart (0.6.4)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-chronicle/latest/google.cloud.chronicle_v1.types.DashboardChart

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DashboardChart (0.6.4) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.4 (latest)  0.6.3  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    DashboardChart(mapping=None, *, ignore_unknown_fields=False, **kwargs)

DashboardChart resource.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Output only. Name of the dashboardChart.   
`display_name` |  `str`   
Required. Display name/Title of the dashboardChart visible to users.   
`description` |  `str`   
Optional. Description of the dashboardChart.   
`native_dashboard` |  `str`   
Output only. NativeDashboard this chart belongs to.   
`tile_type` |  `[google.cloud.chronicle_v1.types.TileType](https://docs.cloud.google.com/python/docs/reference/google-cloud-chronicle/latest/google.cloud.chronicle_v1.types.TileType)`   
Optional. Type of tile i.e., visualization, button or text.   
`chart_datasource` |  `[google.cloud.chronicle_v1.types.DashboardChart.ChartDatasource](https://docs.cloud.google.com/python/docs/reference/google-cloud-chronicle/latest/google.cloud.chronicle_v1.types.DashboardChart.ChartDatasource)`   
Optional. Query and datasource used in the chart. Should be empty for Button Tiles.   
`visualization` |  `[google.cloud.chronicle_v1.types.DashboardChart.Visualization](https://docs.cloud.google.com/python/docs/reference/google-cloud-chronicle/latest/google.cloud.chronicle_v1.types.DashboardChart.Visualization)`   
Required. Depending on tile_type one of below fields will be required.   
`etag` |  `str`   
Optional. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.   
`drill_down_config` |  `[google.cloud.chronicle_v1.types.DashboardChart.DrillDownConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-chronicle/latest/google.cloud.chronicle_v1.types.DashboardChart.DrillDownConfig)`   
Optional. Drill down configuration.   
`tokens` |  `MutableSequence[str]`   
Optional. List of Advanced Filter tokens used in this chart's query (e.g., "hostname", "ip"). This allows the UI to identify dependencies without parsing the query text. The tokens are stored without the wrapping '$' characters. The number of tokens are not expected to be more than 10.   
  
## Classes 

### ChartDatasource
    
    
    ChartDatasource(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Datasource of the chart including the query reference and source name.

### DrillDownConfig
    
    
    DrillDownConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Drill down configuration.

### Visualization
    
    
    Visualization(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Visualization config for a chart. <https://echarts.apache.org/en/option.html#series>

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
