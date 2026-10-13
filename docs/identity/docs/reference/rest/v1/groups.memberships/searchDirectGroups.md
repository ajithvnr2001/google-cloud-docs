---
url: https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships/searchDirectGroups/
title: Method: groups.memberships.searchDirectGroups \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:38:39.582464+00:00
---

# Method: groups.memberships.searchDirectGroups  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships/searchDirectGroups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Reference ](https://docs.cloud.google.com/identity/docs/apis)



Send feedback 

#  Method: groups.memberships.searchDirectGroups Stay organized with collections  Save and categorize content based on your preferences. 

Searches direct groups of a member.

Groups for which the actor does not have the permission to view memberships are silently filtered out.

### HTTP request

`GET https://cloudidentity.googleapis.com/v1/{parent=groups/*}/memberships:searchDirectGroups`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` [Resource name](https://cloud.google.com/apis/design/resource_names) of the group to search transitive memberships in.Format: groups/{groupId}, where groupId is always '-' as this API will search across all groups for a given member.  
  
### Query parameters

Parameters  
---  
`query` |  `string` Required. A CEL expression that MUST include member specification AND label(s).Users can search on label attributes of groups. CONTAINS match ('in') is supported on labels. Identity-mapped groups are uniquely identified by both a `member_key_id` and a `member_key_namespace`, which requires an additional query input: `member_key_namespace`.Example query: `member_key_id == 'member_key_id_value' && 'label_value' in labels`  
`pageSize` |  `integer` The default page size is 200 (max 1000).  
`pageToken` |  `string` The `next_page_token` value returned from a previous list request, if any  
`orderBy` |  `string` The ordering of membership relation for the display name or email in the response. The syntax for this field can be found at <https://cloud.google.com/apis/design/design_patterns#sorting_order>. Example: Sort by the ascending display name: order_by="group_name" or order_by="group_name asc". Sort by the descending display name: order_by="group_name desc". Sort by the ascending group key: order_by="group_key" or order_by="group_key asc". Sort by the descending group key: order_by="group_key desc".  
  
### Request body

The request body must be empty.

### Response body

The response message for `[MembershipsService.SearchDirectGroups](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships/searchDirectGroups#google.apps.cloudidentity.groups.v1.MembershipsService.SearchDirectGroups)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "memberships": [
        {
          object ([MembershipRelation](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships/searchDirectGroups#MembershipRelation))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`memberships[]` |  `object (`[MembershipRelation](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships/searchDirectGroups#MembershipRelation)`)` List of direct groups satisfying the query.  
`nextPageToken` |  `string` Token to retrieve the next page of results, or empty if there are no more results available for listing.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-identity.groups.readonly`
  * `https://www.googleapis.com/auth/cloud-identity.groups`
  * `https://www.googleapis.com/auth/cloud-identity`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authorization guide](https://developers.google.com/workspace/guides/configure-oauth-consent).

## MembershipRelation

Message containing membership relation.

JSON representation  
---  
      
    
    {
      "membership": string,
      "roles": [
        {
          object ([MembershipRole](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships#MembershipRole))
        }
      ],
      "group": string,
      "groupKey": {
        object ([EntityKey](https://docs.cloud.google.com/identity/docs/reference/rest/v1/EntityKey))
      },
      "displayName": string,
      "labels": {
        string: string,
        ...
      },
      "description": string
    }  
  
Fields  
---  
`membership` |  `string` The [resource name](https://cloud.google.com/apis/design/resource_names) of the `Membership`.Shall be of the form `groups/{group_id}/memberships/{membership_id}`.  
`roles[]` |  `object (`[MembershipRole](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships#MembershipRole)`)` The `MembershipRole`s that apply to the `Membership`.  
`group` |  `string` The [resource name](https://cloud.google.com/apis/design/resource_names) of the `Group`.Shall be of the form `groups/{group_id}`.  
`groupKey` |  `object (`[EntityKey](https://docs.cloud.google.com/identity/docs/reference/rest/v1/EntityKey)`)` The `EntityKey` of the `Group`.  
`displayName` |  `string` The display name of the `Group`.  
`labels` |  `map (key: string, value: string)` One or more label entries that apply to the Group. Currently supported labels contain a key with an empty value.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`description` |  `string` An extended description to help users determine the purpose of a `Group`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
