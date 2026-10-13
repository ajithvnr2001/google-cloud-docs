---
url: https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups/
title: REST Resource: groups \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:38:36.730299+00:00
---

# REST Resource: groups  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Reference ](https://docs.cloud.google.com/identity/docs/apis)



Send feedback 

#  REST Resource: groups Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: Group

A group within the Cloud Identity Groups API.

A `Group` is a collection of entities, where each entity is either a user, another group, or a service account.

JSON representation  
---  
      
    
    {
      "name": string,
      "groupKey": {
        object ([EntityKey](https://docs.cloud.google.com/identity/docs/reference/rest/v1/EntityKey))
      },
      "additionalGroupKeys": [
        {
          object ([EntityKey](https://docs.cloud.google.com/identity/docs/reference/rest/v1/EntityKey))
        }
      ],
      "parent": string,
      "displayName": string,
      "description": string,
      "createTime": string,
      "updateTime": string,
      "labels": {
        string: string,
        ...
      },
      "dynamicGroupMetadata": {
        object ([DynamicGroupMetadata](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups#DynamicGroupMetadata))
      },
      "externalIds": [
        {
          object ([ExternalId](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups#ExternalId))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Output only. The [resource name](https://cloud.google.com/apis/design/resource_names) of the `Group`.Shall be of the form `groups/{group}`.  
`groupKey` |  `object (`[EntityKey](https://docs.cloud.google.com/identity/docs/reference/rest/v1/EntityKey)`)` Required. The `EntityKey` of the `Group`.  
`additionalGroupKeys[]` |  `object (`[EntityKey](https://docs.cloud.google.com/identity/docs/reference/rest/v1/EntityKey)`)` Output only. Additional group keys associated with the Group.  
`parent` |  `string` Required. Immutable. The resource name of the entity under which this `Group` resides in the Cloud Identity resource hierarchy.Must be of the form `identitysources/{identity_source}` for external [identity-mapped groups](https://support.google.com/a/answer/9039510) or `customers/{customerId}` for Google Groups. The `customerId` must begin with "C" (for example, 'C046psxkn'). [Find your customer ID.](https://support.google.com/cloudidentity/answer/10070793)  
`displayName` |  `string` The display name of the `Group`.  
`description` |  `string` An extended description to help users determine the purpose of a `Group`.Must not be longer than 4,096 characters.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the `Group` was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the `Group` was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Required. One or more label entries that apply to the Group. Labels contain a key with an empty value.Google Groups are the default type of group and have a label with a key of `cloudidentity.googleapis.com/groups.discussion_forum` and an empty value.Existing Google Groups can have an additional label with a key of `cloudidentity.googleapis.com/groups.security` and an empty value added to them. **This is an immutable change and the security label cannot be removed once added.** Dynamic groups have a label with a key of `cloudidentity.googleapis.com/groups.dynamic`.Identity-mapped groups for Cloud Search have a label with a key of `system/groups/external` and an empty value.Google Groups can be [locked](https://support.google.com/a?p=locked-groups). To lock a group, add a label with a key of `cloudidentity.googleapis.com/groups.locked` and an empty value. Doing so locks the group. To unlock the group, remove this label.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`dynamicGroupMetadata` |  `object (`[DynamicGroupMetadata](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups#DynamicGroupMetadata)`)` Optional. Dynamic group metadata like queries and status.  
`externalIds[]` |  `object (`[ExternalId](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups#ExternalId)`)` Optional. External identifiers associated with the `Group`.Let external identity providers and directory sync tools link their native unique identifiers with this group.The only supported namespace is `system/external`.  
  
## DynamicGroupMetadata

Dynamic group metadata like queries and status.

JSON representation  
---  
      
    
    {
      "queries": [
        {
          object ([DynamicGroupQuery](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups#DynamicGroupQuery))
        }
      ],
      "status": {
        object ([DynamicGroupStatus](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups#DynamicGroupStatus))
      }
    }  
  
Fields  
---  
`queries[]` |  `object (`[DynamicGroupQuery](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups#DynamicGroupQuery)`)` Memberships will be the union of all queries. Only one entry with USER resource is currently supported. Customers can create up to 500 dynamic groups.  
`status` |  `object (`[DynamicGroupStatus](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups#DynamicGroupStatus)`)` Output only. Status of the dynamic group.  
  
## DynamicGroupQuery

Defines a query on a resource.

JSON representation  
---  
      
    
    {
      "resourceType": enum ([ResourceType](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups#ResourceType)),
      "query": string
    }  
  
Fields  
---  
`resourceType` |  `enum (`[ResourceType](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups#ResourceType)`)` Resource type for the Dynamic Group Query  
`query` |  `string` Query that determines the memberships of the dynamic group.Examples: All users with at least one `organizations.department` of engineering.`user.organizations.exists(org, org.department=='engineering')`All users with at least one location that has `area` of `foo` and `building_id` of `bar`.`user.locations.exists(loc, loc.area=='foo' && loc.building_id=='bar')`All users with any variation of the name John Doe (case-insensitive queries add `equalsIgnoreCase()` to the value being queried).`user.name.value.equalsIgnoreCase('jOhn DoE')`  
  
## ResourceType

Resources supported for dynamic groups.

Enums  
---  
`RESOURCE_TYPE_UNSPECIFIED` | Default value (not valid)  
`USER` | For queries on User  
  
## DynamicGroupStatus

The current status of a dynamic group along with timestamp.

JSON representation  
---  
      
    
    {
      "status": enum ([Status](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups#Status)),
      "statusTime": string
    }  
  
Fields  
---  
`status` |  `enum (`[Status](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups#Status)`)` Status of the dynamic group.  
`statusTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The latest time at which the dynamic group is guaranteed to be in the given status. If status is `UP_TO_DATE`, the latest time at which the dynamic group was confirmed to be up-to-date. If status is `UPDATING_MEMBERSHIPS`, the time at which dynamic group was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## Status

All possible statuses of a dynamic group.

Enums  
---  
`STATUS_UNSPECIFIED` | Default.  
`UP_TO_DATE` | The dynamic group is up-to-date.  
`UPDATING_MEMBERSHIPS` | The dynamic group has just been created and memberships are being updated.  
`INVALID_QUERY` | Group is in an unrecoverable state and its memberships can't be updated.  
  
## ExternalId

Represents an external identifier that links a `[Group](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups#Group)` in the Cloud Identity Groups API with a corresponding entity in an external directory or identity provider.

JSON representation  
---  
      
    
    {
      "id": string,
      "namespace": string
    }  
  
Fields  
---  
`id` |  `string` Required. The unique identifier assigned by the external identity provider.The API does not enforce unique IDs across entities, but clients **must** ensure IDs are unique within their namespace.  
`namespace` |  `string` Required. The namespace in which the entity exists.The only supported namespace is `system/external`.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups/create)`

|  Creates a Group.  
  
### `[delete](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups/delete)`

|  Deletes a `Group`.  
  
### `[get](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups/get)`

|  Retrieves a `Group`.  
  
### `[getSecuritySettings](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups/getSecuritySettings)`

|  Get Security Settings  
  
### `[list](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups/list)`

|  Lists the `Group` resources under a customer or namespace.  
  
### `[lookup](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups/lookup)`

|  Looks up the [resource name](https://cloud.google.com/apis/design/resource_names) of a `Group` by its `EntityKey`.  
  
### `[patch](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups/patch)`

|  Updates a `Group`.  
  
### `[search](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups/search)`

|  Searches for `Group` resources matching a specified query.  
  
### `[updateSecuritySettings](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups/updateSecuritySettings)`

|  Update Security Settings  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
