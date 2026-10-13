---
url: https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships/searchTransitiveGroups/
title: Method: groups.memberships.searchTransitiveGroups \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:38:40.198416+00:00
---

# Method: groups.memberships.searchTransitiveGroups  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships/searchTransitiveGroups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Reference ](https://docs.cloud.google.com/identity/docs/apis)



Send feedback 

#  Method: groups.memberships.searchTransitiveGroups Stay organized with collections  Save and categorize content based on your preferences. 

Search transitive groups of a member.

**Note:** This feature is only available to Google Workspace Enterprise Standard, Enterprise Plus, and Enterprise for Education; and Cloud Identity Premium accounts. If the account of the member is not one of these, a 403 (PERMISSION_DENIED) HTTP status code will be returned.

A transitive group is any group that has a direct or indirect membership to the member. Actor must have view permissions all transitive groups.

### HTTP request

`GET https://cloudidentity.googleapis.com/v1/{parent=groups/*}/memberships:searchTransitiveGroups`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` [Resource name](https://cloud.google.com/apis/design/resource_names) of the group to search transitive memberships in.Format: `groups/{group}`, where `group` is always '-' as this API will search across all groups for a given member.  
  
### Query parameters

Parameters  
---  
`query` |  `string` Required. A CEL expression that MUST include member specification AND label(s). This is a `required` field.Users can search on label attributes of groups. CONTAINS match ('in') is supported on labels. Identity-mapped groups are uniquely identified by both a `member_key_id` and a `member_key_namespace`, which requires an additional query input: `member_key_namespace`.Example query: `member_key_id == 'member_key_id_value' && <label_value> in labels`Query may optionally contain equality operators on the parent of the group restricting the search within a particular customer, e.g. `parent == 'customers/{customer_id}'`. The `customer_id` must begin with "C" (for example, 'C046psxkn'). This filtering is only supported for Admins with groups read permissions on the input customer.Example query: `member_key_id == 'member_key_id_value' && <label_value> in labels && parent == 'customers/C046psxkn'`  
`pageSize` |  `integer` The default page size is 200 (max 1000).  
`pageToken` |  `string` The `nextPageToken` value returned from a previous list request, if any.  
  
### Request body

The request body must be empty.

### Response body

The response message for `[MembershipsService.SearchTransitiveGroups](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships/searchTransitiveGroups#google.apps.cloudidentity.groups.v1.MembershipsService.SearchTransitiveGroups)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "memberships": [
        {
          object ([GroupRelation](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships/searchTransitiveGroups#GroupRelation))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`memberships[]` |  `object (`[GroupRelation](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships/searchTransitiveGroups#GroupRelation)`)` List of transitive groups satisfying the query.  
`nextPageToken` |  `string` Token to retrieve the next page of results, or empty if there are no more results available for listing.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-identity.groups.readonly`
  * `https://www.googleapis.com/auth/cloud-identity.groups`
  * `https://www.googleapis.com/auth/cloud-identity`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authorization guide](https://developers.google.com/workspace/guides/configure-oauth-consent).

## GroupRelation

Message representing a transitive group of a user or a group.

JSON representation  
---  
      
    
    {
      "groupKey": {
        object ([EntityKey](https://docs.cloud.google.com/identity/docs/reference/rest/v1/EntityKey))
      },
      "group": string,
      "displayName": string,
      "roles": [
        {
          object ([TransitiveMembershipRole](https://docs.cloud.google.com/identity/docs/reference/rest/v1/TransitiveMembershipRole))
        }
      ],
      "relationType": enum ([RelationType](https://docs.cloud.google.com/identity/docs/reference/rest/v1/RelationType)),
      "labels": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`groupKey` |  `object (`[EntityKey](https://docs.cloud.google.com/identity/docs/reference/rest/v1/EntityKey)`)` Entity key has an id and a namespace. In case of discussion forums, the id will be an email address without a namespace.  
`group` |  `string` Resource name for this group.  
`displayName` |  `string` Display name for this group.  
`roles[]` |  `object (`[TransitiveMembershipRole](https://docs.cloud.google.com/identity/docs/reference/rest/v1/TransitiveMembershipRole)`)` Membership roles of the member for the group.  
`relationType` |  `enum (`[RelationType](https://docs.cloud.google.com/identity/docs/reference/rest/v1/RelationType)`)` The relation between the member and the transitive group.  
`labels` |  `map (key: string, value: string)` Labels for Group resource.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-16 UTC."],[],[]] 
