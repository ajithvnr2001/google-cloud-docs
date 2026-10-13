---
url: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1beta.RunAccessReportResponse
title: Google Analytics Admin V1beta Client - Class RunAccessReportResponse (0.34.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:46:01.605261+00:00
---

# Google Analytics Admin V1beta Client - Class RunAccessReportResponse (0.34.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1beta.RunAccessReportResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Analytics Admin V1beta Client - Class RunAccessReportResponse (0.34.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.34.3 (latest)  0.33.0  0.32.0  0.31.3  0.30.0  0.29.1  0.28.1  0.27.0  0.26.0  0.25.2  0.24.2  0.23.0  0.22.5  0.20.0  0.19.0  0.18.1  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.2 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Analytics Admin V1beta Client class RunAccessReportResponse.

The customized Data Access Record Report response.

Generated from protobuf message `google.analytics.admin.v1beta.RunAccessReportResponse`

## Namespace

Google \ Analytics \ Admin \ V1beta

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ dimension_headers` |  `array<[AccessDimensionHeader](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1beta.AccessDimensionHeader)>`   
The header for a column in the report that corresponds to a specific dimension. The number of DimensionHeaders and ordering of DimensionHeaders matches the dimensions present in rows.  
`↳ metric_headers` |  `array<[AccessMetricHeader](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1beta.AccessMetricHeader)>`   
The header for a column in the report that corresponds to a specific metric. The number of MetricHeaders and ordering of MetricHeaders matches the metrics present in rows.  
`↳ rows` |  `array<[AccessRow](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1beta.AccessRow)>`   
Rows of dimension value combinations and metric values in the report.  
`↳ row_count` |  `int`   
The total number of rows in the query result. `rowCount` is independent of the number of rows returned in the response, the `limit` request parameter, and the `offset` request parameter. For example if a query returns 175 rows and includes `limit` of 50 in the API request, the response will contain `rowCount` of 175 but only 50 rows. To learn more about this pagination parameter, see [Pagination](https://developers.google.com/analytics/devguides/reporting/data/v1/basics#pagination).  
`↳ quota` |  `[AccessQuota](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1beta.AccessQuota)`   
The quota state for this Analytics property including this request. This field doesn't work with account-level requests.  
  
### getDimensionHeaders

The header for a column in the report that corresponds to a specific dimension. The number of DimensionHeaders and ordering of DimensionHeaders matches the dimensions present in rows.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<[AccessDimensionHeader](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1beta.AccessDimensionHeader)>` |   
  
### setDimensionHeaders

The header for a column in the report that corresponds to a specific dimension. The number of DimensionHeaders and ordering of DimensionHeaders matches the dimensions present in rows.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array<[AccessDimensionHeader](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1beta.AccessDimensionHeader)>`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getMetricHeaders

The header for a column in the report that corresponds to a specific metric. The number of MetricHeaders and ordering of MetricHeaders matches the metrics present in rows.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<[AccessMetricHeader](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1beta.AccessMetricHeader)>` |   
  
### setMetricHeaders

The header for a column in the report that corresponds to a specific metric. The number of MetricHeaders and ordering of MetricHeaders matches the metrics present in rows.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array<[AccessMetricHeader](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1beta.AccessMetricHeader)>`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getRows

Rows of dimension value combinations and metric values in the report.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<[AccessRow](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1beta.AccessRow)>` |   
  
### setRows

Rows of dimension value combinations and metric values in the report.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array<[AccessRow](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1beta.AccessRow)>`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getRowCount

The total number of rows in the query result. `rowCount` is independent of the number of rows returned in the response, the `limit` request parameter, and the `offset` request parameter. For example if a query returns 175 rows and includes `limit` of 50 in the API request, the response will contain `rowCount` of 175 but only 50 rows.

To learn more about this pagination parameter, see [Pagination](https://developers.google.com/analytics/devguides/reporting/data/v1/basics#pagination).

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### setRowCount

The total number of rows in the query result. `rowCount` is independent of the number of rows returned in the response, the `limit` request parameter, and the `offset` request parameter. For example if a query returns 175 rows and includes `limit` of 50 in the API request, the response will contain `rowCount` of 175 but only 50 rows.

To learn more about this pagination parameter, see [Pagination](https://developers.google.com/analytics/devguides/reporting/data/v1/basics#pagination).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getQuota

The quota state for this Analytics property including this request. This field doesn't work with account-level requests.

**Returns**  
---  
**Type** | **Description**  
`[AccessQuota](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1beta.AccessQuota)|null` |   
  
### hasQuota

### clearQuota

### setQuota

The quota state for this Analytics property including this request. This field doesn't work with account-level requests.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[AccessQuota](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1beta.AccessQuota)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
