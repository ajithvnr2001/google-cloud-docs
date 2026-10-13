---
url: https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.SearchAllResourcesRequest
title: Class SearchAllResourcesRequest (4.5.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:35:37.083752+00:00
---

# Class SearchAllResourcesRequest (4.5.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.SearchAllResourcesRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class SearchAllResourcesRequest (4.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.5.0 (latest)  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.30.1  3.29.2  3.28.0  3.27.1  3.26.4  3.25.1  3.24.3  3.23.0  3.22.0  3.21.0  3.20.1  3.19.1  3.18.1  3.17.1  3.16.0  3.15.0  3.14.2  3.13.1  3.12.0  3.11.0  3.10.0  3.9.1  3.8.1  3.7.1  3.6.1  3.5.0  3.4.0  3.3.0  3.2.1  3.1.0  2.2.2  2.1.0  2.0.0  1.3.2  1.2.0  1.1.0  1.0.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0 
    
    
    SearchAllResourcesRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Search all resources request.

## Attributes  
  
---  
**Name** | **Description**  
`scope` |  `str`   
Required. A scope can be a project, a folder, or an organization. The search is limited to the resources within the `scope`. The caller must be granted the ```cloudasset.assets.searchAllResources`` `__ permission on the desired scope. The allowed values are: \- projects/{PROJECT_ID} (e.g., "projects/foo-bar") \- projects/{PROJECT_NUMBER} (e.g., "projects/12345678") \- folders/{FOLDER_NUMBER} (e.g., "folders/1234567") \- organizations/{ORGANIZATION_NUMBER} (e.g., "organizations/123456")   
`query` |  `str`   
Optional. The query statement. See `how to construct a query   
`asset_types` |  `MutableSequence[str]`   
Optional. A list of asset types that this request searches for. If empty, it will search all the asset types `supported by search APIs   
`page_size` |  `int`   
Optional. The page size for search result pagination. Page size is capped at 500 even if a larger value is given. If set to zero or a negative value, server will pick an appropriate default. Returned results may be fewer than requested. When this happens, there could be more results as long as `next_page_token` is returned.   
`page_token` |  `str`   
Optional. If present, then retrieve the next batch of results from the preceding call to this method. `page_token` must be the value of `next_page_token` from the previous response. The values of all other method parameters, must be identical to those in the previous call.   
`order_by` |  `str`   
Optional. A comma-separated list of fields specifying the sorting order of the results. The default order is ascending. Add " DESC" after the field name to indicate descending order. Redundant space characters are ignored. Example: "location DESC, name". Only the following fields in the response are sortable: \- name \- assetType \- project \- displayName \- description \- location \- createTime \- updateTime \- state \- parentFullResourceName \- parentAssetType   
`read_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
Optional. A comma-separated list of fields that you want returned in the results. The following fields are returned by default if not specified: \- `name` \- `assetType` \- `project` \- `folders` \- `organization` \- `displayName` \- `description` \- `location` \- `labels` \- `tags` \- `effectiveTags` \- `networkTags` \- `kmsKeys` \- `createTime` \- `updateTime` \- `state` \- `additionalAttributes` \- `parentFullResourceName` \- `parentAssetType` Some fields of large size, such as `versionedResources`, `attachedResources`, `effectiveTags` etc., are not returned by default, but you can specify them in the `read_mask` parameter if you want to include them. If `"*"` is specified, all `available fields   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
