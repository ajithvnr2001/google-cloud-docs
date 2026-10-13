---
url: https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups.memberships
title: REST Resource: groups.memberships \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:38:50.913574+00:00
---

# REST Resource: groups.memberships  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups.memberships

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Reference ](https://docs.cloud.google.com/identity/docs/apis)



Send feedback 

#  REST Resource: groups.memberships Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: Membership

A membership within the Cloud Identity Groups API.

A `Membership` defines a relationship between a `Group` and an entity belonging to that `Group`, referred to as a "member".

JSON representation  
---  
      
    
    {
      "name": string,
      "memberKey": {
        object ([EntityKey](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/EntityKey))
      },
      "createTime": string,
      "updateTime": string,
      "roles": [
        {
          object ([MembershipRole](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups.memberships#MembershipRole))
        }
      ],
      "preferredMemberKey": {
        object ([EntityKey](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/EntityKey))
      },
      "type": enum ([Type](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups.memberships#Type)),
      "deliverySetting": enum ([DeliverySetting](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups.memberships#DeliverySetting))
    }  
  
Fields  
---  
`name` |  `string` Output only. The [resource name](https://cloud.google.com/apis/design/resource_names) of the `Membership`.Shall be of the form `groups/{groupId}/memberships/{membership_id}`.  
`memberKey` |  `object (`[EntityKey](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/EntityKey)`)` Immutable. The `EntityKey` of the member.Either `memberKey` or `preferredMemberKey` must be set when calling `[MembershipsService.CreateMembership](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups.memberships/create#google.apps.cloudidentity.groups.v1beta1.MembershipsService.CreateMembership)` but not both; both shall be set when returned.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the `Membership` was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the `Membership` was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`roles[]` |  `object (`[MembershipRole](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups.memberships#MembershipRole)`)` The `MembershipRole`s that apply to the `Membership`.If unspecified, defaults to a single `MembershipRole` with `name` `MEMBER`.Must not contain duplicate `MembershipRole`s with the same `name`.  
`preferredMemberKey` |  `object (`[EntityKey](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/EntityKey)`)` Required. Immutable. The `EntityKey` of the member.Either `memberKey` or `preferredMemberKey` must be set when calling `[MembershipsService.CreateMembership](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups.memberships/create#google.apps.cloudidentity.groups.v1beta1.MembershipsService.CreateMembership)` but not both; both shall be set when returned.  
`type` |  `enum (`[Type](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups.memberships#Type)`)` Output only. The type of the membership.  
`deliverySetting` |  `enum (`[DeliverySetting](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups.memberships#DeliverySetting)`)` Output only. Delivery setting associated with the membership.  
  
## MembershipRole

A membership role within the Cloud Identity Groups API.

A `MembershipRole` defines the privileges granted to a `Membership`.

JSON representation  
---  
      
    
    {
      "name": string,
      "expiryDetail": {
        object ([ExpiryDetail](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups.memberships#ExpiryDetail))
      },
      "restrictionEvaluations": {
        object ([RestrictionEvaluations](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups.memberships#RestrictionEvaluations))
      }
    }  
  
Fields  
---  
`name` |  `string` The name of the `MembershipRole`.Must be one of `OWNER`, `MANAGER`, `MEMBER`.  
`expiryDetail` |  `object (`[ExpiryDetail](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups.memberships#ExpiryDetail)`)` The expiry details of the `MembershipRole`.Expiry details are only supported for `MEMBER` `MembershipRoles`.May be set if `name` is `MEMBER`. Must not be set if `name` is any other value.  
`restrictionEvaluations` |  `object (`[RestrictionEvaluations](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups.memberships#RestrictionEvaluations)`)` Evaluations of restrictions applied to parent group on this membership.  
  
## ExpiryDetail

The `MembershipRole` expiry details.

JSON representation  
---  
      
    
    {
      "expireTime": string
    }  
  
Fields  
---  
`expireTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time at which the `MembershipRole` will expire.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## RestrictionEvaluations

Evaluations of restrictions applied to parent group on this membership.

JSON representation  
---  
      
    
    {
      "memberRestrictionEvaluation": {
        object ([RestrictionEvaluation](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups.memberships#RestrictionEvaluation))
      }
    }  
  
Fields  
---  
`memberRestrictionEvaluation` |  `object (`[RestrictionEvaluation](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups.memberships#RestrictionEvaluation)`)` Evaluation of the member restriction applied to this membership.Empty if the user lacks permission to view the restriction evaluation.  
  
## RestrictionEvaluation

The evaluated state of this restriction.

JSON representation  
---  
      
    
    {
      "state": enum ([State](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups.memberships#State))
    }  
  
Fields  
---  
`state` |  `enum (`[State](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups.memberships#State)`)` Output only. The current state of the restriction  
  
## State

All possible states of a restriction.

Enums  
---  
`STATE_UNSPECIFIED` | Default. Should not be used.  
`COMPLIANT` | The member adheres to the parent group's restriction.  
`FORWARD_COMPLIANT` | The group-group membership might be currently violating some parent group's restriction but in future, it will never allow any new member in the child group which can violate parent group's restriction.  
`NON_COMPLIANT` | The member violates the parent group's restriction.  
`EVALUATING` | The state of the membership is under evaluation.  
  
## Type

Enums  
---  
`TYPE_UNSPECIFIED` | Default. Should not be used.  
`USER` | Represents user type.  
`SERVICE_ACCOUNT` | Represents service account type.  
`GROUP` | Represents group type.  
`SHARED_DRIVE` | Represents Shared drive.  
`CBCM_BROWSER` | Represents a CBCM-managed Chrome Browser type.  
`CHROME_OS_DEVICE` | Represents a ChromeOS-managed ChromeOS device type.  
`OTHER` | Represents other type.  
  
## DeliverySetting

Delivery setting associated with the membership.

Enums  
---  
`DELIVERY_SETTING_UNSPECIFIED` | Default. Should not be used.  
`ALL_MAIL` | Represents each mail should be delivered  
`DIGEST` | Represents 1 email for every 25 messages.  
`DAILY` | Represents daily summary of messages.  
`NONE` | Represents no delivery.  
`DISABLED` | Represents disabled state.  
  
## Methods  
  
---  
  
### `[checkTransitiveMembership](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups.memberships/checkTransitiveMembership)`

|  Check a potential member for membership in a group.  
  
### `[create](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups.memberships/create)`

|  Creates a `Membership`.  
  
### `[delete](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups.memberships/delete)`

|  Deletes a `Membership`.  
  
### `[get](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups.memberships/get)`

|  Retrieves a `Membership`.  
  
### `[getMembershipGraph](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups.memberships/getMembershipGraph)`

|  Get a membership graph of just a member or both a member and a group.  
  
### `[list](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups.memberships/list)`

|  Lists the `Membership`s within a `Group`.  
  
### `[lookup](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups.memberships/lookup)`

|  Looks up the [resource name](https://cloud.google.com/apis/design/resource_names) of a `Membership` by its `EntityKey`.  
  
### `[modifyMembershipRoles](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups.memberships/modifyMembershipRoles)`

|  Modifies the `MembershipRole`s of a `Membership`.  
  
### `[searchDirectGroups](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups.memberships/searchDirectGroups)`

|  Searches direct groups of a member.  
  
### `[searchTransitiveGroups](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups.memberships/searchTransitiveGroups)`

|  Search transitive groups of a member.  
  
### `[searchTransitiveMemberships](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups.memberships/searchTransitiveMemberships)`

|  Search transitive memberships of a group.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
