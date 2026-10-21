---
url: https://docs.cloud.google.com/docs/quotas/reference/rest/v1beta/projects.locations.quotaPreferences
title: REST Resource: projects.locations.quotaPreferences \u00a0|\u00a0 Cloud Quotas \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:06:13.969901+00:00
---

# REST Resource: projects.locations.quotaPreferences  |  Cloud Quotas  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/quotas/reference/rest/v1beta/projects.locations.quotaPreferences

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Quotas ](https://docs.cloud.google.com/docs/quotas)
  * [ Reference ](https://docs.cloud.google.com/docs/quotas/apis)



Send feedback 

#  REST Resource: projects.locations.quotaPreferences Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: QuotaPreference
    * JSON representation
  * Methods



## Resource: QuotaPreference

QuotaPreference represents the preferred quota configuration specified for a project, folder or organization. There is only one QuotaPreference resource for a quota value targeting a unique set of dimensions.

JSON representation  
---  
      
    
    {
      "name": string,
      "dimensions": {
        string: string,
        ...
      },
      "quotaConfig": {
        object ([QuotaConfig](https://docs.cloud.google.com/docs/quotas/reference/rest/v1beta/folders.locations.quotaPreferences#QuotaPreference.QuotaConfig))
      },
      "etag": string,
      "createTime": string,
      "updateTime": string,
      "service": string,
      "quotaId": string,
      "reconciling": boolean,
      "justification": string,
      "contactEmail": string
    }  
  
Fields  
---  
`name` |  `string` Required except in the CREATE requests. The resource name of the quota preference. The path that follows `/locations` must be `/global`. For example: `projects/123/locations/global/quotaPreferences/my-config-for-us-east1`  
`dimensions` |  `map (key: string, value: string)` Immutable. The dimensions that this quota preference applies to. The key of the map entry is the name of a dimension, such as `region`, `zone`, `network_id`, and the value of the map entry is the dimension value.If a dimension is missing from the map of dimensions, the quota preference applies to all the dimension values except for those that have other quota preferences configured for the specific value.Note: QuotaPreferences can only be applied across all values of `user` and `resource` dimension. Do not set values for `user` or `resource` in the dimension map.For example: `{"provider" : "Example Organization"}` where `provider` is a service-specific quota dimension and `Example Organization` is the provider name.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`quotaConfig` |  `object (`[QuotaConfig](https://docs.cloud.google.com/docs/quotas/reference/rest/v1beta/folders.locations.quotaPreferences#QuotaPreference.QuotaConfig)`)` Required. Preferred quota configuration.  
`etag` |  `string` Optional. The current etag of the quota preference. If an etag is provided on update and does not match the current server's etag of the quota preference, the request will be blocked and an ABORTED error will be returned. See <https://google.aip.dev/134#etags> for more details on etags.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Create time stampUses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Update time stampUses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`service` |  `string` Required. The name of the service to which the quota preference is applied.  
`quotaId` |  `string` Required. The id of the quota to which the quota preference is applied. A quota name is unique in the service. For example, `CpusPerProjectPerRegion`  
`reconciling` |  `boolean` Output only. Is the quota preference pending Google Cloud approval and fulfillment.  
`justification` |  `string` The reason / justification for this quota preference.  
`contactEmail` |  `string` Input only. An email address that can be used to contact the user, in case Google Cloud needs more information to make a decision before additional quota can be granted.When requesting a quota increase, the email address is required. When requesting a quota decrease, the email address is optional. For example, the email address is optional when the `QuotaConfig.preferred_value` is smaller than the `QuotaDetails.reset_value`.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/docs/quotas/reference/rest/v1beta/projects.locations.quotaPreferences/create)`

|  Creates a new QuotaPreference that declares the desired value for a quota.  
  
### `[get](https://docs.cloud.google.com/docs/quotas/reference/rest/v1beta/projects.locations.quotaPreferences/get)`

|  Gets details of a single QuotaPreference.  
  
### `[list](https://docs.cloud.google.com/docs/quotas/reference/rest/v1beta/projects.locations.quotaPreferences/list)`

|  Lists QuotaPreferences in a given project, folder or organization.  
  
### `[patch](https://docs.cloud.google.com/docs/quotas/reference/rest/v1beta/projects.locations.quotaPreferences/patch)`

|  Updates the parameters of a single QuotaPreference.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
