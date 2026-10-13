---
url: https://docs.cloud.google.com/php/docs/reference/analytics-data/latest/V1alpha.SheetExportAudienceListRequest
title: Google Analytics Data V1alpha Client - Class SheetExportAudienceListRequest (0.24.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:21:17.353805+00:00
---

# Google Analytics Data V1alpha Client - Class SheetExportAudienceListRequest (0.24.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/analytics-data/latest/V1alpha.SheetExportAudienceListRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Analytics Data V1alpha Client - Class SheetExportAudienceListRequest (0.24.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.28.0 (latest)  0.24.0  0.23.3  0.22.3  0.21.1  0.20.1  0.19.0  0.18.0  0.17.1  0.16.4  0.14.0  0.13.0  0.12.0  0.11.2  0.10.1  0.9.5 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Analytics Data V1alpha Client class SheetExportAudienceListRequest.

A request to export users in an audience list to a Google Sheet.

Generated from protobuf message `google.analytics.data.v1alpha.SheetExportAudienceListRequest`

## Namespace

Google \ Analytics \ Data \ V1alpha

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ name` |  `string`   
Required. The name of the audience list to retrieve users from. Format: `properties/{property}/audienceLists/{audience_list}`  
`↳ offset` |  `int|string`   
Optional. The row count of the start row. The first row is counted as row 0. When paging, the first request does not specify offset; or equivalently, sets offset to 0; the first request returns the first `limit` of rows. The second request sets offset to the `limit` of the first request; the second request returns the second `limit` of rows. To learn more about this pagination parameter, see [Pagination](https://developers.google.com/analytics/devguides/reporting/data/v1/basics#pagination).  
`↳ limit` |  `int|string`   
Optional. The number of rows to return. If unspecified, 10,000 rows are returned. The API returns a maximum of 250,000 rows per request, no matter how many you ask for. `limit` must be positive. The API can also return fewer rows than the requested `limit`, if there aren't as many dimension values as the `limit`. To learn more about this pagination parameter, see [Pagination](https://developers.google.com/analytics/devguides/reporting/data/v1/basics#pagination).  
  
### getName

Required. The name of the audience list to retrieve users from.

Format: `properties/{property}/audienceLists/{audience_list}`

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

Required. The name of the audience list to retrieve users from.

Format: `properties/{property}/audienceLists/{audience_list}`

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getOffset

Optional. The row count of the start row. The first row is counted as row 0.

When paging, the first request does not specify offset; or equivalently, sets offset to 0; the first request returns the first `limit` of rows. The second request sets offset to the `limit` of the first request; the second request returns the second `limit` of rows. To learn more about this pagination parameter, see [Pagination](https://developers.google.com/analytics/devguides/reporting/data/v1/basics#pagination).

**Returns**  
---  
**Type** | **Description**  
`int|string` |   
  
### setOffset

Optional. The row count of the start row. The first row is counted as row 0.

When paging, the first request does not specify offset; or equivalently, sets offset to 0; the first request returns the first `limit` of rows. The second request sets offset to the `limit` of the first request; the second request returns the second `limit` of rows. To learn more about this pagination parameter, see [Pagination](https://developers.google.com/analytics/devguides/reporting/data/v1/basics#pagination).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int|string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getLimit

Optional. The number of rows to return. If unspecified, 10,000 rows are returned. The API returns a maximum of 250,000 rows per request, no matter how many you ask for. `limit` must be positive.

The API can also return fewer rows than the requested `limit`, if there aren't as many dimension values as the `limit`. To learn more about this pagination parameter, see [Pagination](https://developers.google.com/analytics/devguides/reporting/data/v1/basics#pagination).

**Returns**  
---  
**Type** | **Description**  
`int|string` |   
  
### setLimit

Optional. The number of rows to return. If unspecified, 10,000 rows are returned. The API returns a maximum of 250,000 rows per request, no matter how many you ask for. `limit` must be positive.

The API can also return fewer rows than the requested `limit`, if there aren't as many dimension values as the `limit`. To learn more about this pagination parameter, see [Pagination](https://developers.google.com/analytics/devguides/reporting/data/v1/basics#pagination).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int|string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### static::build

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
Required. The name of the audience list to retrieve users from. Format: `properties/{property}/audienceLists/{audience_list}` Please see AlphaAnalyticsDataClient::audienceListName() for help formatting this field.  
**Returns**  
---  
**Type** | **Description**  
`[SheetExportAudienceListRequest](https://docs.cloud.google.com/php/docs/reference/analytics-data/latest/V1alpha.SheetExportAudienceListRequest)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
