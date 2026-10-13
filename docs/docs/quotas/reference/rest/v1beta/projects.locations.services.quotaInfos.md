---
url: https://docs.cloud.google.com/docs/quotas/reference/rest/v1beta/projects.locations.services.quotaInfos
title: REST Resource: projects.locations.services.quotaInfos \u00a0|\u00a0 Cloud Quotas \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:54:54.158642+00:00
---

# REST Resource: projects.locations.services.quotaInfos  |  Cloud Quotas  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/quotas/reference/rest/v1beta/projects.locations.services.quotaInfos

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Quotas ](https://docs.cloud.google.com/docs/quotas)
  * [ Reference ](https://docs.cloud.google.com/docs/quotas/apis)



Send feedback 

#  REST Resource: projects.locations.services.quotaInfos Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: QuotaInfo
    * JSON representation
  * Methods



## Resource: QuotaInfo

QuotaInfo represents information about a particular quota for a given project, folder or organization.

JSON representation  
---  
      
    
    {
      "name": string,
      "quotaId": string,
      "metric": string,
      "service": string,
      "isPrecise": boolean,
      "refreshInterval": string,
      "containerType": enum ([ContainerType](https://docs.cloud.google.com/docs/quotas/reference/rest/v1beta/folders.locations.services.quotaInfos#QuotaInfo.ContainerType)),
      "dimensions": [
        string
      ],
      "metricDisplayName": string,
      "quotaDisplayName": string,
      "metricUnit": string,
      "quotaIncreaseEligibility": {
        object ([QuotaIncreaseEligibility](https://docs.cloud.google.com/docs/quotas/reference/rest/v1beta/folders.locations.services.quotaInfos#QuotaInfo.QuotaIncreaseEligibility))
      },
      "isFixed": boolean,
      "dimensionsInfos": [
        {
          object ([DimensionsInfo](https://docs.cloud.google.com/docs/quotas/reference/rest/v1beta/folders.locations.services.quotaInfos#QuotaInfo.DimensionsInfo))
        }
      ],
      "isConcurrent": boolean,
      "serviceRequestQuotaUri": string
    }  
  
Fields  
---  
`name` |  `string` Resource name of this QuotaInfo. The ID component following "locations/" must be "global". For example, `projects/123/locations/global/services/compute.googleapis.com/quotaInfos/CpusPerProjectPerRegion`  
`quotaId` |  `string` The id of the quota, which is unique within the service. For example, `CpusPerProjectPerRegion`  
`metric` |  `string` The metric of the quota. It specifies the resources consumption the quota is defined for. For example, `compute.googleapis.com/cpus`  
`service` |  `string` The name of the service in which the quota is defined. For example, `compute.googleapis.com`  
`isPrecise` |  `boolean` Whether this is a precise quota. A precise quota is tracked with absolute precision. In contrast, an imprecise quota is not tracked with precision.  
`refreshInterval` |  `string` The reset time interval for the quota. Refresh interval applies to rate quota only. For example, "minute" for per minute, "day" for per day, or "10 seconds" for every 10 seconds.  
`containerType` |  `enum (`[ContainerType](https://docs.cloud.google.com/docs/quotas/reference/rest/v1beta/folders.locations.services.quotaInfos#QuotaInfo.ContainerType)`)` The container type of the QuotaInfo.  
`dimensions[]` |  `string` The dimensions the quota is defined on.  
`metricDisplayName` |  `string` The display name of the quota metric  
`quotaDisplayName` |  `string` The display name of the quota.  
`metricUnit` |  `string` The unit in which the metric value is reported, e.g., "MByte".  
`quotaIncreaseEligibility` |  `object (`[QuotaIncreaseEligibility](https://docs.cloud.google.com/docs/quotas/reference/rest/v1beta/folders.locations.services.quotaInfos#QuotaInfo.QuotaIncreaseEligibility)`)` Whether it is eligible to request a higher quota value for this quota.  
`isFixed` |  `boolean` Whether the quota value is fixed or adjustable  
`dimensionsInfos[]` |  `object (`[DimensionsInfo](https://docs.cloud.google.com/docs/quotas/reference/rest/v1beta/folders.locations.services.quotaInfos#QuotaInfo.DimensionsInfo)`)` The collection of dimensions info ordered by their dimensions from more specific ones to less specific ones.  
`isConcurrent` |  `boolean` Whether the quota is a concurrent quota. Concurrent quotas are enforced on the total number of concurrent operations in flight at any given time.  
`serviceRequestQuotaUri` |  `string` URI to the page where users can request more quota for the cloud service—for example, <https://console.cloud.google.com/iam-admin/quotas>.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/docs/quotas/reference/rest/v1beta/projects.locations.services.quotaInfos/get)`

|  Retrieve the QuotaInfo of a quota for a project, folder or organization.  
  
### `[list](https://docs.cloud.google.com/docs/quotas/reference/rest/v1beta/projects.locations.services.quotaInfos/list)`

|  Lists QuotaInfos of all quotas for a given project, folder or organization.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-21 UTC."],[],[]] 
