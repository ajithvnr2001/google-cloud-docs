---
url: https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups/list/
title: Method: groups.list \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:38:49.647147+00:00
---

# Method: groups.list  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Reference ](https://docs.cloud.google.com/identity/docs/apis)



Send feedback 

#  Method: groups.list Stay organized with collections  Save and categorize content based on your preferences. 

Lists the `Group` resources under a customer or namespace.

### HTTP request

`GET https://cloudidentity.googleapis.com/v1beta1/groups`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Query parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource under which to list all `Group` resources.Must be of the form `identitysources/{identity_source_id}` for external- identity-mapped groups or `customers/{customer_id}` for Google Groups. The `customer_id` must begin with "C" (for example, 'C046psxkn'). [Find your customer ID.](https://support.google.com/cloudidentity/answer/10070793)  
`view` |  `enum (`[View](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups/list#View)`)` The level of detail to be returned.If unspecified, defaults to `View.BASIC`.  
`pageSize` |  `integer` The maximum number of results to return.Note that the number of results returned may be less than this value even if there are more available results. To fetch all results, clients must continue calling this method repeatedly until the response no longer contains a `next_page_token`.If unspecified, defaults to 200 for `View.BASIC` and to 50 for `View.FULL`.Must not be greater than 1000 for `View.BASIC` or 500 for `View.FULL`.  
`pageToken` |  `string` The `next_page_token` value returned from a previous list request, if any.  
  
### Request body

The request body must be empty.

### Response body

The response message for `[GroupsService.ListGroups](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups/list#google.apps.cloudidentity.groups.v1beta1.GroupsService.ListGroups)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "groups": [
        {
          object ([Group](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups#Group))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`groups[]` |  `object (`[Group](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups#Group)`)` The `Group` resources under the specified `parent`.  
`nextPageToken` |  `string` A continuation token to retrieve the next page of results, or empty if there are no more results available.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-identity.groups.readonly`
  * `https://www.googleapis.com/auth/cloud-identity.groups`
  * `https://www.googleapis.com/auth/cloud-identity`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authorization guide](https://developers.google.com/workspace/guides/configure-oauth-consent).

## View

The view options for the `[GroupsService.ListGroups](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups/list#google.apps.cloudidentity.groups.v1beta1.GroupsService.ListGroups)` method.

Enums  
---  
`VIEW_UNSPECIFIED` | Default. Should not be used.  
`BASIC` | Only basic resource information is returned.  
`FULL` | All resource information is returned.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-16 UTC."],[],[]] 
