---
url: https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships/modifyMembershipRoles/
title: Method: groups.memberships.modifyMembershipRoles \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:36:09.400486+00:00
---

# Method: groups.memberships.modifyMembershipRoles  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships/modifyMembershipRoles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Reference ](https://docs.cloud.google.com/identity/docs/apis)



Send feedback 

#  Method: groups.memberships.modifyMembershipRoles Stay organized with collections  Save and categorize content based on your preferences. 

Modifies the `MembershipRole`s of a `Membership`.

### HTTP request

`POST https://cloudidentity.googleapis.com/v1/{name=groups/*/memberships/*}:modifyMembershipRoles`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The [resource name](https://cloud.google.com/apis/design/resource_names) of the `Membership` whose roles are to be modified.Must be of the form `groups/{group}/memberships/{membership}`.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "addRoles": [
        {
          object ([MembershipRole](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships#MembershipRole))
        }
      ],
      "removeRoles": [
        string
      ],
      "updateRolesParams": [
        {
          object ([UpdateMembershipRolesParams](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships/modifyMembershipRoles#UpdateMembershipRolesParams))
        }
      ]
    }  
  
Fields  
---  
`addRoles[]` |  `object (`[MembershipRole](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships#MembershipRole)`)` The `MembershipRole`s to be added.Adding or removing roles in the same request as updating roles is not supported.Must not be set if `update_roles_params` is set.  
`removeRoles[]` |  `string` The `name`s of the `MembershipRole`s to be removed.Adding or removing roles in the same request as updating roles is not supported.It is not possible to remove the `MEMBER` `MembershipRole`. If you wish to delete a `Membership`, call `[MembershipsService.DeleteMembership](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships/delete#google.apps.cloudidentity.groups.v1.MembershipsService.DeleteMembership)` instead.Must not contain `MEMBER`. Must not be set if `update_roles_params` is set.  
`updateRolesParams[]` |  `object (`[UpdateMembershipRolesParams](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships/modifyMembershipRoles#UpdateMembershipRolesParams)`)` The `MembershipRole`s to be updated.Updating roles in the same request as adding or removing roles is not supported.Must not be set if either `add_roles` or `remove_roles` is set.  
  
### Response body

The response message for `[MembershipsService.ModifyMembershipRoles](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships/modifyMembershipRoles#google.apps.cloudidentity.groups.v1.MembershipsService.ModifyMembershipRoles)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "membership": {
        object ([Membership](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships#Membership))
      }
    }  
  
Fields  
---  
`membership` |  `object (`[Membership](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships#Membership)`)` The `Membership` resource after modifying its `MembershipRole`s.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-identity.groups`
  * `https://www.googleapis.com/auth/cloud-identity`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authorization guide](https://developers.google.com/workspace/guides/configure-oauth-consent).

## UpdateMembershipRolesParams

The details of an update to a `MembershipRole`.

JSON representation  
---  
      
    
    {
      "fieldMask": string,
      "membershipRole": {
        object ([MembershipRole](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships#MembershipRole))
      }
    }  
  
Fields  
---  
`fieldMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` The fully-qualified names of fields to update.May only contain the field `expiry_detail.expire_time`.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
`membershipRole` |  `object (`[MembershipRole](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships#MembershipRole)`)` The `MembershipRole`s to be updated.Only `MEMBER` `MembershipRole` can currently be updated.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-16 UTC."],[],[]] 
