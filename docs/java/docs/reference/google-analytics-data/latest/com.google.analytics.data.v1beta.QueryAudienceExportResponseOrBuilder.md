---
url: https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QueryAudienceExportResponseOrBuilder
title: Interface QueryAudienceExportResponseOrBuilder (0.110.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:11:36.485007+00:00
---

# Interface QueryAudienceExportResponseOrBuilder (0.110.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QueryAudienceExportResponseOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface QueryAudienceExportResponseOrBuilder (0.110.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.110.0 (latest)  0.106.0  0.105.0  0.104.0  0.102.0  0.99.0  0.98.0  0.96.0  0.94.0  0.93.0  0.92.0  0.91.0  0.89.0  0.87.0  0.86.0  0.85.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.75.0  0.74.0  0.73.0  0.71.0  0.70.0  0.69.0  0.68.0  0.67.0  0.66.0  0.65.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0 
    
    
    public interface QueryAudienceExportResponseOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAudienceExport()
    
    
    public abstract AudienceExport getAudienceExport()

Configuration data about AudienceExport being queried. Returned to help interpret the audience rows in this response. For example, the dimensions in this AudienceExport correspond to the columns in the AudienceRows.

`optional .google.analytics.data.v1beta.AudienceExport audience_export = 1;`

**Returns**  
---  
**Type** | **Description**  
`[AudienceExport](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.AudienceExport)` | The audienceExport.  
  
### getAudienceExportOrBuilder()
    
    
    public abstract AudienceExportOrBuilder getAudienceExportOrBuilder()

Configuration data about AudienceExport being queried. Returned to help interpret the audience rows in this response. For example, the dimensions in this AudienceExport correspond to the columns in the AudienceRows.

`optional .google.analytics.data.v1beta.AudienceExport audience_export = 1;`

**Returns**  
---  
**Type** | **Description**  
`[AudienceExportOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.AudienceExportOrBuilder)` |   
  
### getAudienceRows(int index)
    
    
    public abstract AudienceRow getAudienceRows(int index)

Rows for each user in an audience export. The number of rows in this response will be less than or equal to request's page size.

`repeated .google.analytics.data.v1beta.AudienceRow audience_rows = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AudienceRow](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.AudienceRow)` |   
  
### getAudienceRowsCount()
    
    
    public abstract int getAudienceRowsCount()

Rows for each user in an audience export. The number of rows in this response will be less than or equal to request's page size.

`repeated .google.analytics.data.v1beta.AudienceRow audience_rows = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAudienceRowsList()
    
    
    public abstract List<AudienceRow> getAudienceRowsList()

Rows for each user in an audience export. The number of rows in this response will be less than or equal to request's page size.

`repeated .google.analytics.data.v1beta.AudienceRow audience_rows = 2;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[AudienceRow](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.AudienceRow)>` |   
  
### getAudienceRowsOrBuilder(int index)
    
    
    public abstract AudienceRowOrBuilder getAudienceRowsOrBuilder(int index)

Rows for each user in an audience export. The number of rows in this response will be less than or equal to request's page size.

`repeated .google.analytics.data.v1beta.AudienceRow audience_rows = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AudienceRowOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.AudienceRowOrBuilder)` |   
  
### getAudienceRowsOrBuilderList()
    
    
    public abstract List<? extends AudienceRowOrBuilder> getAudienceRowsOrBuilderList()

Rows for each user in an audience export. The number of rows in this response will be less than or equal to request's page size.

`repeated .google.analytics.data.v1beta.AudienceRow audience_rows = 2;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.analytics.data.v1beta.AudienceRowOrBuilder>` |   
  
### getRowCount()
    
    
    public abstract int getRowCount()

The total number of rows in the AudienceExport result. `rowCount` is independent of the number of rows returned in the response, the `limit` request parameter, and the `offset` request parameter. For example if a query returns 175 rows and includes `limit` of 50 in the API request, the response will contain `rowCount` of 175 but only 50 rows.

To learn more about this pagination parameter, see [Pagination](https://developers.google.com/analytics/devguides/reporting/data/v1/basics#pagination).

`optional int32 row_count = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The rowCount.  
  
### hasAudienceExport()
    
    
    public abstract boolean hasAudienceExport()

Configuration data about AudienceExport being queried. Returned to help interpret the audience rows in this response. For example, the dimensions in this AudienceExport correspond to the columns in the AudienceRows.

`optional .google.analytics.data.v1beta.AudienceExport audience_export = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the audienceExport field is set.  
  
### hasRowCount()
    
    
    public abstract boolean hasRowCount()

The total number of rows in the AudienceExport result. `rowCount` is independent of the number of rows returned in the response, the `limit` request parameter, and the `offset` request parameter. For example if a query returns 175 rows and includes `limit` of 50 in the API request, the response will contain `rowCount` of 175 but only 50 rows.

To learn more about this pagination parameter, see [Pagination](https://developers.google.com/analytics/devguides/reporting/data/v1/basics#pagination).

`optional int32 row_count = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the rowCount field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
