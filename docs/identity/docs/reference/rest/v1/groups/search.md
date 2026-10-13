---
url: https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups/search/
title: Method: groups.search \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:38:38.775368+00:00
---

# Method: groups.search  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups/search/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Reference ](https://docs.cloud.google.com/identity/docs/apis)



Send feedback 

#  Method: groups.search Stay organized with collections  Save and categorize content based on your preferences. 

Searches for `Group` resources matching a specified query.

### HTTP request

`GET https://cloudidentity.googleapis.com/v1/groups:search`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Query parameters

Parameters  
---  
`query` |  `string` Required. The search query.

  * Must be specified in [Common Expression Language](https://opensource.google/projects/cel).
  * Must contain equality operators on the parent, e.g. `parent == 'customers/{customer_id}'`. The `customer_id` must begin with "C" (for example, 'C046psxkn'). [Find your customer ID.](https://support.google.com/cloudidentity/answer/10070793)
  * Can contain optional inclusion operators on `labels` such as `'cloudidentity.googleapis.com/groups.discussion_forum' in labels`).
  * Can contain an optional equality operator on `domain_name`. e.g. `domain_name == 'examplepetstore.com'`
  * Can contain optional `startsWith/contains/equality` operators on `group_key`, e.g. `group_key.startsWith('dev')`, `group_key.contains('dev'), group_key == 'dev@examplepetstore.com'`
  * Can contain optional `startsWith/contains/equality` operators on `display_name`, such as `display_name.startsWith('dev')` , `display_name.contains('dev')`, `display_name == 'dev'`

  
`view` |  `enum (`[View](https://docs.cloud.google.com/identity/docs/reference/rest/v1/View)`)` The level of detail to be returned.If unspecified, defaults to `View.BASIC`.  
`pageSize` |  `integer` The maximum number of results to return.Note that the number of results returned may be less than this value even if there are more available results. To fetch all results, clients must continue calling this method repeatedly until the response no longer contains a `next_page_token`.If unspecified, defaults to 200 for `GroupView.BASIC` and 50 for `GroupView.FULL`.Must not be greater than 1000 for `GroupView.BASIC` or 500 for `GroupView.FULL`.  
`pageToken` |  `string` The `next_page_token` value returned from a previous search request, if any.  
  
### Request body

The request body must be empty.

### Response body

The response message for `[GroupsService.SearchGroups](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups/search#google.apps.cloudidentity.groups.v1.GroupsService.SearchGroups)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "groups": [
        {
          object ([Group](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups#Group))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`groups[]` |  `object (`[Group](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups#Group)`)` The `Group` resources that match the search query.  
`nextPageToken` |  `string` A continuation token to retrieve the next page of results, or empty if there are no more results available.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-identity.groups.readonly`
  * `https://www.googleapis.com/auth/cloud-identity.groups`
  * `https://www.googleapis.com/auth/cloud-identity`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authorization guide](https://developers.google.com/workspace/guides/configure-oauth-consent).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-16 UTC."],[],[]] 
