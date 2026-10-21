---
url: https://docs.cloud.google.com/docs/quotas/reference/rest/v1beta/organizations.locations.quotaAdjusterSettings
title: REST Resource: organizations.locations.quotaAdjusterSettings \u00a0|\u00a0 Cloud Quotas \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:06:12.286968+00:00
---

# REST Resource: organizations.locations.quotaAdjusterSettings  |  Cloud Quotas  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/quotas/reference/rest/v1beta/organizations.locations.quotaAdjusterSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Quotas ](https://docs.cloud.google.com/docs/quotas)
  * [ Reference ](https://docs.cloud.google.com/docs/quotas/apis)



Send feedback 

#  REST Resource: organizations.locations.quotaAdjusterSettings Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: QuotaAdjusterSettings
    * JSON representation
  * Methods



## Resource: QuotaAdjusterSettings

The QuotaAdjusterSettings resource defines the settings for the Quota Adjuster.

JSON representation  
---  
      
    
    {
      "name": string,
      "enablement": enum ([Enablement](https://docs.cloud.google.com/docs/quotas/reference/rest/v1beta/folders.locations.quotaAdjusterSettings#QuotaAdjusterSettings.Enablement)),
      "updateTime": string,
      "etag": string,
      "inherited": boolean,
      "inheritedFrom": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. Name of the configuration, in the formats below:

  * For a project: projects/PROJECT_NUMBER/locations/global/quotaAdjusterSettings
  * For a folder: folders/FOLDER_NUMBER/locations/global/quotaAdjusterSettings
  * For an organization: organizations/ORGANIZATION_NUMBER/locations/global/quotaAdjusterSettings

  
`enablement` |  `enum (`[Enablement](https://docs.cloud.google.com/docs/quotas/reference/rest/v1beta/folders.locations.quotaAdjusterSettings#QuotaAdjusterSettings.Enablement)`)` Optional. The configured value of the enablement at the given resource.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the QuotaAdjusterSettings resource was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`etag` |  `string` Optional. The current ETag of the QuotaAdjusterSettings. If an ETag is provided on update and does not match the current server's ETag in the QuotaAdjusterSettings, the request is blocked and returns an ABORTED error. See <https://google.aip.dev/134#etags> for more details on ETags.  
`inherited` |  `boolean` Optional. Indicates whether the setting is inherited or explicitly specified.  
`inheritedFrom` |  `string` Output only. The resource container from which the setting is inherited. This refers to the nearest ancestor with enablement set (either ENABLED or DISABLED). The value can be an organizations/{organization_id}, folders/{folder_id}, or can be 'default' if no ancestor exists with enablement set. The value will be empty when enablement is directly set on this container.  
  
## Methods  
  
---  
  
### `[getQuotaAdjusterSettings](https://docs.cloud.google.com/docs/quotas/reference/rest/v1beta/organizations.locations.quotaAdjusterSettings/getQuotaAdjusterSettings)`

|  Gets the QuotaAdjusterSettings for the specified resource.  
  
### `[updateQuotaAdjusterSettings](https://docs.cloud.google.com/docs/quotas/reference/rest/v1beta/organizations.locations.quotaAdjusterSettings/updateQuotaAdjusterSettings)`

|  Updates the QuotaAdjusterSettings for the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-30 UTC."],[],[]] 
