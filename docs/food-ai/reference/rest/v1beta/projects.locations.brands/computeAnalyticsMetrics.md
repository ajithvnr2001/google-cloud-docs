---
url: https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands/computeAnalyticsMetrics/
title: Method: projects.locations.brands.computeAnalyticsMetrics \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:34:24.645483+00:00
---

# Method: projects.locations.brands.computeAnalyticsMetrics  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands/computeAnalyticsMetrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Food AI ](https://docs.cloud.google.com/food-ai)



Send feedback 

#  Method: projects.locations.brands.computeAnalyticsMetrics Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * AnalyticsType
  * FeatureGate
    * JSON representation
  * AnalyticsMetrics
    * JSON representation
  * IntervalMetrics
    * JSON representation
  * PredictedFailureCategoryCount
    * JSON representation



Computes analytics metrics for a given brand for specified time period with optional store filter.

### HTTP request

`GET https://foodorderingaiagent.googleapis.com/v1beta/{brand=projects/*/locations/*/brands/*}:computeAnalyticsMetrics`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`brand` |  `string` Required. The brand to get analytics metrics for. Format: projects/{project}/locations/{location}/brands/{brand}  
  
### Query parameters

Parameters  
---  
`timestamps[]` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Required. The timestamps that mark the start of each interval for which analytics metrics are calculated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`storeIds[]` |  `string` Optional. The list of store IDs to get analytics metrics for. If not specified, analytics metrics for all stores will be returned. Needed to query by city or state.  
`analyticsTypes[]` |  `enum (`[AnalyticsType](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands/computeAnalyticsMetrics#AnalyticsType)`)` Optional. The types of analytics to compute. If empty or unspecified, all available analytics types will be computed.  
`featureGate` |  `object (`[FeatureGate](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands/computeAnalyticsMetrics#FeatureGate)`)` Optional. Feature gates.  
  
### Request body

The request body must be empty.

### Response body

Response message for `[MenuService.ComputeAnalyticsMetrics](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands/computeAnalyticsMetrics#google.cloud.foodorderingaiagent.v1beta.MenuService.ComputeAnalyticsMetrics)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "analyticsMetrics": {
        object ([AnalyticsMetrics](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands/computeAnalyticsMetrics#AnalyticsMetrics))
      }
    }  
  
Fields  
---  
`analyticsMetrics` |  `object (`[AnalyticsMetrics](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands/computeAnalyticsMetrics#AnalyticsMetrics)`)` Output only. The analytics metrics for the brand.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## AnalyticsType

The type of analytics to compute.

Enums  
---  
`ANALYTICS_TYPE_UNSPECIFIED` | Unspecified analytics type.  
`GENERIC` | Compute generic/overall metrics (e.g., order count, escalation count, upsell count).  
`DAILY` | Compute daily metrics (e.g., daily order and escalation counts).  
`PREDICTED_FAILURE_CATEGORIES` | Compute predicted failure category metrics (e.g., predicted failure category count).  
  
## FeatureGate

Feature gates to control analytics computation behavior.

JSON representation  
---  
      
    
    {
      "enableAggregationData": boolean
    }  
  
Fields  
---  
`enableAggregationData` |  `boolean` Optional. For limited brands only. If set, compute analytics metrics using aggregation data.  
  
## AnalyticsMetrics

Represents analytics metrics for a given period, with a comparison to a previous period.

JSON representation  
---  
      
    
    {
      "intervalMetrics": [
        {
          object ([IntervalMetrics](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands/computeAnalyticsMetrics#IntervalMetrics))
        }
      ]
    }  
  
Fields  
---  
`intervalMetrics[]` |  `object (`[IntervalMetrics](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands/computeAnalyticsMetrics#IntervalMetrics)`)` Metrics for the intervals.  
  
## IntervalMetrics

Represents analytics metrics for a specific time interval.

JSON representation  
---  
      
    
    {
      "interval": {
        object ([Interval](https://docs.cloud.google.com/food-ai/reference/rest/Shared.Types/Interval))
      },
      "totalOrderCount": string,
      "successOrderCount": string,
      "avgOrderDurationMs": string,
      "upsellSuccessRate": number,
      "upsellRevenue": {
        object ([Money](https://docs.cloud.google.com/food-ai/reference/rest/Shared.Types/Money))
      },
      "escalationCount": string,
      "predictedFailureCategoryCounts": [
        {
          object ([PredictedFailureCategoryCount](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands/computeAnalyticsMetrics#PredictedFailureCategoryCount))
        }
      ],
      "invalidOrderCount": string,
      "crewEscalationCount": string
    }  
  
Fields  
---  
`interval` |  `object (`[Interval](https://docs.cloud.google.com/food-ai/reference/rest/Shared.Types/Interval)`)` The start / end time reflected by these metrics.  
`totalOrderCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The total number of orders.  
`successOrderCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The number of successful orders.  
`avgOrderDurationMs` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The average order duration in ms.  
`upsellSuccessRate` |  `number` Output only. The upsell success rate.  
`upsellRevenue` |  `object (`[Money](https://docs.cloud.google.com/food-ai/reference/rest/Shared.Types/Money)`)` Output only. The upsell revenue.  
`escalationCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The escalation outcome group count.  
`predictedFailureCategoryCounts[]` |  `object (`[PredictedFailureCategoryCount](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands/computeAnalyticsMetrics#PredictedFailureCategoryCount)`)` Output only. The predicted failure category counts.  
`invalidOrderCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The total number of invalid orders.  
`crewEscalationCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The number of crew escalation orders.  
  
## PredictedFailureCategoryCount

Predicted failure category count.

JSON representation  
---  
      
    
    {
      "category": string,
      "count": string
    }  
  
Fields  
---  
`category` |  `string` Output only. The predicted failure category.  
`count` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The count of sessions in this category.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-21 UTC."],[],[]] 
