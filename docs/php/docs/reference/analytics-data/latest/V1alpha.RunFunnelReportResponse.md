---
url: https://docs.cloud.google.com/php/docs/reference/analytics-data/latest/V1alpha.RunFunnelReportResponse
title: Google Analytics Data V1alpha Client - Class RunFunnelReportResponse (0.28.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:29:54.529591+00:00
---

# Google Analytics Data V1alpha Client - Class RunFunnelReportResponse (0.28.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/analytics-data/latest/V1alpha.RunFunnelReportResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Analytics Data V1alpha Client - Class RunFunnelReportResponse (0.28.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.28.0 (latest)  0.24.0  0.23.3  0.22.3  0.21.1  0.20.1  0.19.0  0.18.0  0.17.1  0.16.4  0.14.0  0.13.0  0.12.0  0.11.2  0.10.1  0.9.5 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Analytics Data V1alpha Client class RunFunnelReportResponse.

The funnel report response contains two sub reports. The two sub reports are different combinations of dimensions and metrics.

Generated from protobuf message `google.analytics.data.v1alpha.RunFunnelReportResponse`

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
`↳ funnel_table` |  `[FunnelSubReport](https://docs.cloud.google.com/php/docs/reference/analytics-data/latest/V1alpha.FunnelSubReport)`   
The funnel table is a report with the funnel step, segment, breakdown dimension, active users, completion rate, abandonments, and abandonments rate. The segment dimension is only present in this response if a segment was requested. The breakdown dimension is only present in this response if it was requested.  
`↳ funnel_visualization` |  `[FunnelSubReport](https://docs.cloud.google.com/php/docs/reference/analytics-data/latest/V1alpha.FunnelSubReport)`   
The funnel visualization is a report with the funnel step, segment, date, next action dimension, and active users. The segment dimension is only present in this response if a segment was requested. The date dimension is only present in this response if it was requested through the `TRENDED_FUNNEL` funnel type. The next action dimension is only present in the response if it was requested.  
`↳ property_quota` |  `[PropertyQuota](https://docs.cloud.google.com/php/docs/reference/analytics-data/latest/V1alpha.PropertyQuota)`   
This Analytics Property's quota state including this request.  
`↳ kind` |  `string`   
Identifies what kind of resource this message is. This `kind` is always the fixed string "analyticsData#runFunnelReport". Useful to distinguish between response types in JSON.  
  
### getFunnelTable

The funnel table is a report with the funnel step, segment, breakdown dimension, active users, completion rate, abandonments, and abandonments rate.

The segment dimension is only present in this response if a segment was requested. The breakdown dimension is only present in this response if it was requested.

**Returns**  
---  
**Type** | **Description**  
`[FunnelSubReport](https://docs.cloud.google.com/php/docs/reference/analytics-data/latest/V1alpha.FunnelSubReport)|null` |   
  
### hasFunnelTable

### clearFunnelTable

### setFunnelTable

The funnel table is a report with the funnel step, segment, breakdown dimension, active users, completion rate, abandonments, and abandonments rate.

The segment dimension is only present in this response if a segment was requested. The breakdown dimension is only present in this response if it was requested.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[FunnelSubReport](https://docs.cloud.google.com/php/docs/reference/analytics-data/latest/V1alpha.FunnelSubReport)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getFunnelVisualization

The funnel visualization is a report with the funnel step, segment, date, next action dimension, and active users.

The segment dimension is only present in this response if a segment was requested. The date dimension is only present in this response if it was requested through the `TRENDED_FUNNEL` funnel type. The next action dimension is only present in the response if it was requested.

**Returns**  
---  
**Type** | **Description**  
`[FunnelSubReport](https://docs.cloud.google.com/php/docs/reference/analytics-data/latest/V1alpha.FunnelSubReport)|null` |   
  
### hasFunnelVisualization

### clearFunnelVisualization

### setFunnelVisualization

The funnel visualization is a report with the funnel step, segment, date, next action dimension, and active users.

The segment dimension is only present in this response if a segment was requested. The date dimension is only present in this response if it was requested through the `TRENDED_FUNNEL` funnel type. The next action dimension is only present in the response if it was requested.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[FunnelSubReport](https://docs.cloud.google.com/php/docs/reference/analytics-data/latest/V1alpha.FunnelSubReport)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPropertyQuota

This Analytics Property's quota state including this request.

**Returns**  
---  
**Type** | **Description**  
`[PropertyQuota](https://docs.cloud.google.com/php/docs/reference/analytics-data/latest/V1alpha.PropertyQuota)|null` |   
  
### hasPropertyQuota

### clearPropertyQuota

### setPropertyQuota

This Analytics Property's quota state including this request.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[PropertyQuota](https://docs.cloud.google.com/php/docs/reference/analytics-data/latest/V1alpha.PropertyQuota)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getKind

Identifies what kind of resource this message is. This `kind` is always the fixed string "analyticsData#runFunnelReport". Useful to distinguish between response types in JSON.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setKind

Identifies what kind of resource this message is. This `kind` is always the fixed string "analyticsData#runFunnelReport". Useful to distinguish between response types in JSON.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
