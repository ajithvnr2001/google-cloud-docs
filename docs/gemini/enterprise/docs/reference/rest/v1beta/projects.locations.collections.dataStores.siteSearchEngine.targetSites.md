---
url: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.siteSearchEngine.targetSites
title: REST Resource: projects.locations.collections.dataStores.siteSearchEngine.targetSites \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:20:03.847043+00:00
---

# REST Resource: projects.locations.collections.dataStores.siteSearchEngine.targetSites  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.siteSearchEngine.targetSites

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Reference ](https://docs.cloud.google.com/gemini/enterprise/docs/apis)



Send feedback 

#  REST Resource: projects.locations.collections.dataStores.siteSearchEngine.targetSites Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: TargetSite
    * JSON representation
    * Type
    * SiteVerificationInfo
      * JSON representation
    * SiteVerificationState
    * IndexingStatus
    * FailureReason
      * JSON representation
    * QuotaFailure
      * JSON representation
  * Methods



## Resource: TargetSite

A target site for the SiteSearchEngine.

JSON representation  
---  
      
    
    {
      "name": string,
      "providedUriPattern": string,
      "type": enum ([Type](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.siteSearchEngine.targetSites#TargetSite.Type)),
      "exactMatch": boolean,
      "generatedUriPattern": string,
      "rootDomainUri": string,
      "siteVerificationInfo": {
        object ([SiteVerificationInfo](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.siteSearchEngine.targetSites#TargetSite.SiteVerificationInfo))
      },
      "indexingStatus": enum ([IndexingStatus](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.siteSearchEngine.targetSites#TargetSite.IndexingStatus)),
      "updateTime": string,
      "failureReason": {
        object ([FailureReason](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.siteSearchEngine.targetSites#TargetSite.FailureReason))
      }
    }  
  
Fields  
---  
`name` |  `string` Output only. The fully qualified resource name of the target site. `projects/{project}/locations/{location}/collections/{collection}/dataStores/{dataStore}/siteSearchEngine/targetSites/{targetSite}` The `target_site_id` is system-generated.  
`providedUriPattern` |  `string` Required. Input only. The user provided URI pattern from which the `generatedUriPattern` is generated.  
`type` |  `enum (`[Type](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.siteSearchEngine.targetSites#TargetSite.Type)`)` The type of the target site, e.g., whether the site is to be included or excluded.  
`exactMatch` |  `boolean` Immutable. If set to false, a uri_pattern is generated to include all pages whose address contains the providedUriPattern. If set to true, an uri_pattern is generated to try to be an exact match of the providedUriPattern or just the specific page if the providedUriPattern is a specific one. providedUriPattern is always normalized to generate the URI pattern to be used by the search engine.  
`generatedUriPattern` |  `string` Output only. This is system-generated based on the providedUriPattern.  
`rootDomainUri` |  `string` Output only. Root domain of the providedUriPattern.  
`siteVerificationInfo` |  `object (`[SiteVerificationInfo](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.siteSearchEngine.targetSites#TargetSite.SiteVerificationInfo)`)` Output only. Site ownership and validity verification status.  
`indexingStatus` |  `enum (`[IndexingStatus](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.siteSearchEngine.targetSites#TargetSite.IndexingStatus)`)` Output only. Indexing status.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The target site's last updated time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`failureReason` |  `object (`[FailureReason](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.siteSearchEngine.targetSites#TargetSite.FailureReason)`)` Output only. Failure reason.  
  
### Type

Possible target site types.

Enums  
---  
`TYPE_UNSPECIFIED` | This value is unused. In this case, server behavior defaults to `[Type.INCLUDE](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.siteSearchEngine.targetSites#TargetSite.Type.ENUM_VALUES.INCLUDE)`.  
`INCLUDE` | Include the target site.  
`EXCLUDE` | Exclude the target site.  
  
### SiteVerificationInfo

Verification information for target sites in advanced site search.

JSON representation  
---  
      
    
    {
      "siteVerificationState": enum ([SiteVerificationState](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.siteSearchEngine.targetSites#TargetSite.SiteVerificationState)),
      "verifyTime": string
    }  
  
Fields  
---  
`siteVerificationState` |  `enum (`[SiteVerificationState](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.siteSearchEngine.targetSites#TargetSite.SiteVerificationState)`)` Site verification state indicating the ownership and validity.  
`verifyTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Latest site verification time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### SiteVerificationState

Site verification state.

Enums  
---  
`SITE_VERIFICATION_STATE_UNSPECIFIED` | Defaults to VERIFIED.  
`VERIFIED` | Site ownership verified.  
`UNVERIFIED` | Site ownership pending verification or verification failed.  
`EXEMPTED` | Site exempt from verification, e.g., a public website that opens to all.  
  
### IndexingStatus

Target site indexing status enumeration.

Enums  
---  
`INDEXING_STATUS_UNSPECIFIED` | Defaults to SUCCEEDED.  
`PENDING` | The target site is in the update queue and will be picked up by indexing pipeline.  
`FAILED` | The target site fails to be indexed.  
`SUCCEEDED` | The target site has been indexed.  
`DELETING` | The previously indexed target site has been marked to be deleted. This is a transitioning state which will resulted in either: 1. target site deleted if unindexing is successful; 2. state reverts to SUCCEEDED if the unindexing fails.  
`CANCELLABLE` | The target site change is pending but cancellable.  
`CANCELLED` | The target site change is cancelled.  
  
### FailureReason

Site search indexing failure reasons.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "quotaFailure": {
        object ([QuotaFailure](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.siteSearchEngine.targetSites#TargetSite.QuotaFailure))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Failure reason. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`quotaFailure` |  `object (`[QuotaFailure](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.siteSearchEngine.targetSites#TargetSite.QuotaFailure)`)` Failed due to insufficient quota.  
End of mutually exclusive fields.  
  
### QuotaFailure

Failed due to insufficient quota.

JSON representation  
---  
      
    
    {
      "totalRequiredQuota": string
    }  
  
Fields  
---  
`totalRequiredQuota` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` This number is an estimation on how much total quota this project needs to successfully complete indexing.  
  
## Methods  
  
---  
  
### `[batchCreate](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.siteSearchEngine.targetSites/batchCreate)`

|  Creates `[TargetSite](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.siteSearchEngine.targetSites#TargetSite)` in a batch.  
  
### `[create](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.siteSearchEngine.targetSites/create)`

|  Creates a `[TargetSite](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.siteSearchEngine.targetSites#TargetSite)`.  
  
### `[delete](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.siteSearchEngine.targetSites/delete)`

|  Deletes a `[TargetSite](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.siteSearchEngine.targetSites#TargetSite)`.  
  
### `[get](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.siteSearchEngine.targetSites/get)`

|  Gets a `[TargetSite](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.siteSearchEngine.targetSites#TargetSite)`.  
  
### `[list](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.siteSearchEngine.targetSites/list)`

|  Gets a list of `[TargetSite](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.siteSearchEngine.targetSites#TargetSite)`s.  
  
### `[patch](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.siteSearchEngine.targetSites/patch)`

|  Updates a `[TargetSite](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.siteSearchEngine.targetSites#TargetSite)`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-03 UTC."],[],[]] 
