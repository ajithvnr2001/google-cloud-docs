---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_analyticsreporting_v4/
title: Class /GOOG/CL_ANALYTICSREPORTING_V4 \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:13:01.296979+00:00
---

# Class /GOOG/CL_ANALYTICSREPORTING_V4  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_analyticsreporting_v4/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_ANALYTICSREPORTING_V4 Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_analyticsreporting_v4)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_analyticsreporting_v4)



## Class
    
    
    /GOOG/CL_ANALYTICSREPORTING_V4

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`Analytics Reporting API v4`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_001` | `Activity` | PUBLIC  
`TY_002` | `Cohort` | PUBLIC  
`TY_003` | `CohortGroup` | PUBLIC  
`TY_004` | `ColumnHeader` | PUBLIC  
`TY_005` | `CustomDimension` | PUBLIC  
`TY_006` | `DateRange` | PUBLIC  
`TY_007` | `DateRangeValues` | PUBLIC  
`TY_008` | `Dimension` | PUBLIC  
`TY_009` | `DimensionFilter` | PUBLIC  
`TY_010` | `DimensionFilterClause` | PUBLIC  
`TY_011` | `DynamicSegment` | PUBLIC  
`TY_012` | `EcommerceData` | PUBLIC  
`TY_013` | `EventData` | PUBLIC  
`TY_014` | `GetReportsRequest` | PUBLIC  
`TY_015` | `GetReportsResponse` | PUBLIC  
`TY_016` | `GoalData` | PUBLIC  
`TY_017` | `GoalSetData` | PUBLIC  
`TY_018` | `Metric` | PUBLIC  
`TY_019` | `MetricFilter` | PUBLIC  
`TY_020` | `MetricFilterClause` | PUBLIC  
`TY_021` | `MetricHeader` | PUBLIC  
`TY_022` | `MetricHeaderEntry` | PUBLIC  
`TY_023` | `OrFiltersForSegment` | PUBLIC  
`TY_024` | `OrderBy` | PUBLIC  
`TY_025` | `PageviewData` | PUBLIC  
`TY_026` | `Pivot` | PUBLIC  
`TY_027` | `PivotHeader` | PUBLIC  
`TY_028` | `PivotHeaderEntry` | PUBLIC  
`TY_029` | `PivotValueRegion` | PUBLIC  
`TY_030` | `ProductData` | PUBLIC  
`TY_031` | `Report` | PUBLIC  
`TY_032` | `ReportData` | PUBLIC  
`TY_033` | `ReportRequest` | PUBLIC  
`TY_034` | `ReportRow` | PUBLIC  
`TY_035` | `ResourceQuotasRemaining` | PUBLIC  
`TY_036` | `ScreenviewData` | PUBLIC  
`TY_037` | `SearchUserActivityRequest` | PUBLIC  
`TY_038` | `SearchUserActivityResponse` | PUBLIC  
`TY_039` | `Segment` | PUBLIC  
`TY_040` | `SegmentDefinition` | PUBLIC  
`TY_041` | `SegmentDimensionFilter` | PUBLIC  
`TY_042` | `SegmentFilter` | PUBLIC  
`TY_043` | `SegmentFilterClause` | PUBLIC  
`TY_044` | `SegmentMetricFilter` | PUBLIC  
`TY_045` | `SegmentSequenceStep` | PUBLIC  
`TY_046` | `SequenceSegment` | PUBLIC  
`TY_047` | `SimpleSegment` | PUBLIC  
`TY_048` | `TransactionData` | PUBLIC  
`TY_049` | `User` | PUBLIC  
`TY_050` | `UserActivitySession` | PUBLIC  
`TY_T_001` | `Activity` | PUBLIC  
`TY_T_002` | `Cohort` | PUBLIC  
`TY_T_005` | `CustomDimension` | PUBLIC  
`TY_T_006` | `DateRange` | PUBLIC  
`TY_T_007` | `DateRangeValues` | PUBLIC  
`TY_T_008` | `Dimension` | PUBLIC  
`TY_T_009` | `DimensionFilter` | PUBLIC  
`TY_T_010` | `DimensionFilterClause` | PUBLIC  
`TY_T_016` | `GoalData` | PUBLIC  
`TY_T_018` | `Metric` | PUBLIC  
`TY_T_019` | `MetricFilter` | PUBLIC  
`TY_T_020` | `MetricFilterClause` | PUBLIC  
`TY_T_022` | `MetricHeaderEntry` | PUBLIC  
`TY_T_023` | `OrFiltersForSegment` | PUBLIC  
`TY_T_024` | `OrderBy` | PUBLIC  
`TY_T_026` | `Pivot` | PUBLIC  
`TY_T_027` | `PivotHeader` | PUBLIC  
`TY_T_028` | `PivotHeaderEntry` | PUBLIC  
`TY_T_029` | `PivotValueRegion` | PUBLIC  
`TY_T_030` | `ProductData` | PUBLIC  
`TY_T_031` | `Report` | PUBLIC  
`TY_T_033` | `ReportRequest` | PUBLIC  
`TY_T_034` | `ReportRow` | PUBLIC  
`TY_T_039` | `Segment` | PUBLIC  
`TY_T_042` | `SegmentFilter` | PUBLIC  
`TY_T_043` | `SegmentFilterClause` | PUBLIC  
`TY_T_045` | `SegmentSequenceStep` | PUBLIC  
`TY_T_050` | `UserActivitySession` | PUBLIC  
`TY_T_STRING` | `Table of Strings` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_CLOUD_VERSION` | `/GOOG/SDK_VERSION` | Lowest Cloud Version | 1.0 | PUBLIC  
`C_ON_PREM_VERSION` | `/GOOG/SDK_VERSION` | Lowest On-premises Version | 1.5 | PUBLIC  
`C_PATH_PREFIX` | `STRING` | API Path Prefix |  | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20240123 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://analyticsreporting.googleapis.com | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | analyticsreporting:v4 | PUBLIC  
`C_SUPPORTED_AUTH` | `/GOOG/SUPP_AUTH` | Supported Auth Types | IJIJWW | PUBLIC  
  
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
  
### BATCH_GET_REPORTS

  * Description: analyticsreporting.reports.batchGet 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IS_INPUT` | IMPORTING | `TY_014` | GetReportsRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_015` | GetReportsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### SEARCH_USER_ACTIVITY

  * Description: analyticsreporting.userActivity.search 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IS_INPUT` | IMPORTING | `TY_037` | SearchUserActivityRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_038` | SearchUserActivityResponse  
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

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
