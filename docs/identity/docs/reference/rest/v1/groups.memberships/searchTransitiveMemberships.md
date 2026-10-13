---
url: https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships/searchTransitiveMemberships/
title: Method: groups.memberships.searchTransitiveMemberships \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:38:39.732695+00:00
---

# Method: groups.memberships.searchTransitiveMemberships  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships/searchTransitiveMemberships/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Reference ](https://docs.cloud.google.com/identity/docs/apis)



Send feedback 

#  Method: groups.memberships.searchTransitiveMemberships Stay organized with collections  Save and categorize content based on your preferences. 

Search transitive memberships of a group.

**Note:** This feature is only available to Google Workspace Enterprise Standard, Enterprise Plus, and Enterprise for Education; and Cloud Identity Premium accounts. If the account of the group is not one of these, a 403 (PERMISSION_DENIED) HTTP status code will be returned.

A transitive membership is any direct or indirect membership of a group. Actor must have view permissions to all transitive memberships.

### HTTP request

`GET https://cloudidentity.googleapis.com/v1/{parent=groups/*}/memberships:searchTransitiveMemberships`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` [Resource name](https://cloud.google.com/apis/design/resource_names) of the group to search transitive memberships in.Format: `groups/{group}`, where `group` is the unique ID assigned to the Group.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` The default page size is 200 (max 1000).  
`pageToken` |  `string` The `next_page_token` value returned from a previous list request, if any.  
  
### Request body

The request body must be empty.

### Response body

The response message for `[MembershipsService.SearchTransitiveMemberships](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships/searchTransitiveMemberships#google.apps.cloudidentity.groups.v1.MembershipsService.SearchTransitiveMemberships)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "memberships": [
        {
          object ([MemberRelation](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships/searchTransitiveMemberships#MemberRelation))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`memberships[]` |  `object (`[MemberRelation](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships/searchTransitiveMemberships#MemberRelation)`)` List of transitive members satisfying the query.  
`nextPageToken` |  `string` Token to retrieve the next page of results, or empty if there are no more results.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-identity.groups.readonly`
  * `https://www.googleapis.com/auth/cloud-identity.groups`
  * `https://www.googleapis.com/auth/cloud-identity`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authorization guide](https://developers.google.com/workspace/guides/configure-oauth-consent).

## MemberRelation

Message representing a transitive membership of a group.

JSON representation  
---  
      
    
    {
      "preferredMemberKey": [
        {
          object ([EntityKey](https://docs.cloud.google.com/identity/docs/reference/rest/v1/EntityKey))
        }
      ],
      "member": string,
      "roles": [
        {
          object ([TransitiveMembershipRole](https://docs.cloud.google.com/identity/docs/reference/rest/v1/TransitiveMembershipRole))
        }
      ],
      "relationType": enum ([RelationType](https://docs.cloud.google.com/identity/docs/reference/rest/v1/RelationType))
    }  
  
Fields  
---  
`preferredMemberKey[]` |  `object (`[EntityKey](https://docs.cloud.google.com/identity/docs/reference/rest/v1/EntityKey)`)` Entity key has an id and a namespace. In case of discussion forums, the id will be an email address without a namespace.  
`member` |  `string` Resource name for this member.  
`roles[]` |  `object (`[TransitiveMembershipRole](https://docs.cloud.google.com/identity/docs/reference/rest/v1/TransitiveMembershipRole)`)` The membership role details (i.e name of role and expiry time).  
`relationType` |  `enum (`[RelationType](https://docs.cloud.google.com/identity/docs/reference/rest/v1/RelationType)`)` The relation between the group and the transitive member.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-16 UTC."],[],[]] 
