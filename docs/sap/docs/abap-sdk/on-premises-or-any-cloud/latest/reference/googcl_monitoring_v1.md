---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_monitoring_v1/
title: Class /GOOG/CL_MONITORING_V1 \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:59:05.046830+00:00
---

# Class /GOOG/CL_MONITORING_V1  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_monitoring_v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_MONITORING_V1 Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_monitoring_v1)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_monitoring_v1)



## Class
    
    
    /GOOG/CL_MONITORING_V1

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`Cloud Monitoring API v1`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_001` | `Aggregation` | PUBLIC  
`TY_002` | `AggregationFunction` | PUBLIC  
`TY_003` | `AlertChart` | PUBLIC  
`TY_004` | `Axis` | PUBLIC  
`TY_005` | `Breakdown` | PUBLIC  
`TY_006` | `ChartOptions` | PUBLIC  
`TY_007` | `CollapsibleGroup` | PUBLIC  
`TY_008` | `Column` | PUBLIC  
`TY_009` | `ColumnLayout` | PUBLIC  
`TY_010` | `ColumnSettings` | PUBLIC  
`TY_011` | `Dashboard` | PUBLIC  
`TY_012` | `DashboardAnnotations` | PUBLIC  
`TY_013` | `DashboardFilter` | PUBLIC  
`TY_014` | `DataSet` | PUBLIC  
`TY_015` | `Dimension` | PUBLIC  
`TY_017` | `ErrorReportingPanel` | PUBLIC  
`TY_018` | `EventAnnotation` | PUBLIC  
`TY_020` | `GaugeView` | PUBLIC  
`TY_021` | `GridLayout` | PUBLIC  
`TY_022` | `HttpBody` | PUBLIC  
`TY_023` | `IncidentList` | PUBLIC  
`TY_024` | `Interval` | PUBLIC  
`TY_025` | `ListDashboardsResponse` | PUBLIC  
`TY_026` | `ListMetricsScopesByMonitoredProjectResponse` | PUBLIC  
`TY_027` | `LogsPanel` | PUBLIC  
`TY_028` | `Measure` | PUBLIC  
`TY_029` | `MetricsScope` | PUBLIC  
`TY_030` | `MonitoredProject` | PUBLIC  
`TY_031` | `MonitoredResource` | PUBLIC  
`TY_032` | `MosaicLayout` | PUBLIC  
`TY_033` | `Operation` | PUBLIC  
`TY_034` | `OpsAnalyticsQuery` | PUBLIC  
`TY_036` | `Parameter` | PUBLIC  
`TY_037` | `PickTimeSeriesFilter` | PUBLIC  
`TY_038` | `PieChart` | PUBLIC  
`TY_039` | `PieChartDataSet` | PUBLIC  
`TY_040` | `QueryExemplarsRequest` | PUBLIC  
`TY_041` | `QueryInstantRequest` | PUBLIC  
`TY_042` | `QueryLabelsRequest` | PUBLIC  
`TY_043` | `QueryRangeRequest` | PUBLIC  
`TY_044` | `QuerySeriesRequest` | PUBLIC  
`TY_045` | `RatioPart` | PUBLIC  
`TY_046` | `Row` | PUBLIC  
`TY_047` | `RowLayout` | PUBLIC  
`TY_048` | `Scorecard` | PUBLIC  
`TY_049` | `SectionHeader` | PUBLIC  
`TY_050` | `SingleViewGroup` | PUBLIC  
`TY_052` | `SparkChartView` | PUBLIC  
`TY_053` | `StatisticalTimeSeriesFilter` | PUBLIC  
`TY_054` | `Status` | PUBLIC  
`TY_055` | `TableDataSet` | PUBLIC  
`TY_056` | `TableDisplayOptions` | PUBLIC  
`TY_057` | `Text` | PUBLIC  
`TY_058` | `TextStyle` | PUBLIC  
`TY_059` | `Threshold` | PUBLIC  
`TY_060` | `Tile` | PUBLIC  
`TY_061` | `TimeSeriesFilter` | PUBLIC  
`TY_062` | `TimeSeriesFilterRatio` | PUBLIC  
`TY_063` | `TimeSeriesQuery` | PUBLIC  
`TY_064` | `TimeSeriesTable` | PUBLIC  
`TY_065` | `Widget` | PUBLIC  
`TY_066` | `XyChart` | PUBLIC  
`TY_067` | `ColumnSortingOptions` | PUBLIC  
`TY_068` | `StringArray` | PUBLIC  
`TY_069` | `TemplateVariableCondition` | PUBLIC  
`TY_070` | `VisibilityCondition` | PUBLIC  
`TY_T_005` | `Breakdown` | PUBLIC  
`TY_T_008` | `Column` | PUBLIC  
`TY_T_010` | `ColumnSettings` | PUBLIC  
`TY_T_011` | `Dashboard` | PUBLIC  
`TY_T_013` | `DashboardFilter` | PUBLIC  
`TY_T_014` | `DataSet` | PUBLIC  
`TY_T_015` | `Dimension` | PUBLIC  
`TY_T_018` | `EventAnnotation` | PUBLIC  
`TY_T_028` | `Measure` | PUBLIC  
`TY_T_029` | `MetricsScope` | PUBLIC  
`TY_T_030` | `MonitoredProject` | PUBLIC  
`TY_T_031` | `MonitoredResource` | PUBLIC  
`TY_T_036` | `Parameter` | PUBLIC  
`TY_T_039` | `PieChartDataSet` | PUBLIC  
`TY_T_046` | `Row` | PUBLIC  
`TY_T_055` | `TableDataSet` | PUBLIC  
`TY_T_059` | `Threshold` | PUBLIC  
`TY_T_060` | `Tile` | PUBLIC  
`TY_T_065` | `Widget` | PUBLIC  
`TY_T_067` | `ColumnSortingOptions` | PUBLIC  
`TY_T_STRING` | `Table of Strings` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_SUPPORTED_AUTH` | `/GOOG/SUPP_AUTH` | Supported Auth Types | IJIJWW | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | monitoring:v1 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://monitoring.googleapis.com | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20250227 | PUBLIC  
`C_PATH_PREFIX` | `STRING` | API Path Prefix |  | PUBLIC  
`C_ON_PREM_VERSION` | `/GOOG/SDK_VERSION` | Lowest On-premises Version | 1.7 | PUBLIC  
`C_CLOUD_VERSION` | `/GOOG/SDK_VERSION` | Lowest Cloud Version |  | PUBLIC  
  
## Methods

For general information about a method in ABAP SDK for Google Cloud, see [API method](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#api_method). 

### CONSTRUCTOR

  * Description: Constructor 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_KEY_NAME` | IMPORTING | `/GOOG/KEYNAME` | Google Cloud Key Name  
`IV_LOG_OBJ` | IMPORTING | `BALOBJ_D` | Application log: Object name (Application code)  
`IV_LOG_SUBOBJ` | IMPORTING | `BALSUBOBJ` | Application Log: Subobject  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_DASHBOARDS

  * Description: monitoring.projects.dashboards.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_VALIDATEONLY` | IMPORTING | `STRING` | validateOnly  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IS_INPUT` | IMPORTING | `TY_011` | Dashboard  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_011` | Dashboard  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_PROJECTS

  * Description: monitoring.locations.global.metricsScopes.projects.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_METRICS_SCOPES_ID` | IMPORTING | `STRING` | metricsScopesId  
`IS_INPUT` | IMPORTING | `TY_030` | MonitoredProject  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_033` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_DASHBOARDS

  * Description: monitoring.projects.dashboards.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_DASHBOARDS_ID` | IMPORTING | `STRING` | dashboardsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `DATA` | Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_PROJECTS

  * Description: monitoring.locations.global.metricsScopes.projects.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_METRICS_SCOPES_ID` | IMPORTING | `STRING` | metricsScopesId  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_033` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_DASHBOARDS

  * Description: monitoring.projects.dashboards.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_DASHBOARDS_ID` | IMPORTING | `STRING` | dashboardsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_011` | Dashboard  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_METRICS_SCOPES

  * Description: monitoring.locations.global.metricsScopes.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_METRICS_SCOPES_ID` | IMPORTING | `STRING` | metricsScopesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_029` | MetricsScope  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_OPERATIONS

  * Description: monitoring.operations.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_OPERATIONS_ID` | IMPORTING | `STRING` | operationsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_033` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LABELS_V1

  * Description: monitoring.projects.location.prometheus.api.v1.labels 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_LOCATION` | IMPORTING | `STRING` | location  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IS_INPUT` | IMPORTING | `TY_042` | QueryLabelsRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_022` | HttpBody  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_DASHBOARDS

  * Description: monitoring.projects.dashboards.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_025` | ListDashboardsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_METADATA

  * Description: projects.location.prometheus.api.v1.metadata.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_LIMIT` | IMPORTING | `STRING` | limit  
`IV_Q_METRIC` | IMPORTING | `STRING` | metric  
`IV_P_LOCATION` | IMPORTING | `STRING` | location  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_022` | HttpBody  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_METRICS_SCOPES_BY_MONI

  * Description: global.metricsScopes.listMetricsScopesByMonitoredProject 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_MONITOREDRESOURCECONTAINE` | IMPORTING | `STRING` | monitoredResourceContainer  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_026` | ListMetricsScopesByMonitoredProjectResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_DASHBOARDS

  * Description: monitoring.projects.dashboards.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_VALIDATEONLY` | IMPORTING | `STRING` | validateOnly  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_DASHBOARDS_ID` | IMPORTING | `STRING` | dashboardsId  
`IS_INPUT` | IMPORTING | `TY_011` | Dashboard  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_011` | Dashboard  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### QUERY_EXEMPLARS_V1

  * Description: projects.location.prometheus.api.v1.query_exemplars 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_LOCATION` | IMPORTING | `STRING` | location  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IS_INPUT` | IMPORTING | `TY_040` | QueryExemplarsRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_022` | HttpBody  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### QUERY_RANGE_V1

  * Description: monitoring.projects.location.prometheus.api.v1.query_range 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_LOCATION` | IMPORTING | `STRING` | location  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IS_INPUT` | IMPORTING | `TY_043` | QueryRangeRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_022` | HttpBody  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### QUERY_V1

  * Description: monitoring.projects.location.prometheus.api.v1.query 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_LOCATION` | IMPORTING | `STRING` | location  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IS_INPUT` | IMPORTING | `TY_041` | QueryInstantRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_022` | HttpBody  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### SERIES_V1

  * Description: monitoring.projects.location.prometheus.api.v1.series 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_LOCATION` | IMPORTING | `STRING` | location  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IS_INPUT` | IMPORTING | `TY_044` | QuerySeriesRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_022` | HttpBody  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### VALUES_LABEL

  * Description: monitoring.projects.location.prometheus.api.v1.label.values 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_END` | IMPORTING | `STRING` | end  
`IV_Q_MATCH` | IMPORTING | `STRING` | match  
`IV_Q_START` | IMPORTING | `STRING` | start  
`IV_P_LABEL` | IMPORTING | `STRING` | label  
`IV_P_LOCATION` | IMPORTING | `STRING` | location  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_022` | HttpBody  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CLOSE

  * Description: Close Connection 
  * Visibility: PUBLIC 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
