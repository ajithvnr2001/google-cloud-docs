---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/defaultObjectAccessControls/
title: DefaultObjectAccessControls \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:51:39.926258+00:00
---

# DefaultObjectAccessControls  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/defaultObjectAccessControls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  DefaultObjectAccessControls Stay organized with collections  Save and categorize content based on your preferences. 

The DefaultObjectAccessControls resources represent the Access Control Lists (ACLs) applied to a new object within Cloud Storage when no ACL was provided for that object. ACLs let you specify who has access to your data and to what extent. **Important:** The methods for this resource fail with a `400 Bad Request` response for buckets with uniform bucket-level access enabled. Use [`storage.buckets.getIamPolicy`](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/getIamPolicy) and [`storage.buckets.setIamPolicy`](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/setIamPolicy) to control access instead. There are two roles that can be assigned to an entity:   


  * `READER`s can [get](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/get) an object, though the `acl` property will not be revealed.
  * `OWNER`s are `READER`s, and they can get the `acl` property, [update](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/update) an object, and call all objectAccessControls methods on the object.  


For more information, see [Access Control](https://docs.cloud.google.com/storage/docs/accesscontrol), with the caveat that this API uses `READER` and `OWNER` instead of `READ` and `FULL_CONTROL`. 

To try out the methods for this resource, see Methods.

## Resource representations
    
    
    {
      "kind": "storage#objectAccessControl",
      "entity": string,
      "role": string,
      "email": string,
      "entityId": string,
      "domain": string,
      "projectTeam": {
        "projectNumber": string,
        "team": string
      },
      "etag": string
    }

Property name | Value | Description | Notes  
---|---|---|---  
`domain` | `string` | The domain associated with the entity, if any. |   
`email` | `string` | The email address associated with the entity, if any. |   
`entity` | `string` | The entity holding the permission, in one of the following forms: 

  * `user-email`
  * `group-groupId`
  * `group-email`
  * `domain-domain`
  * `project-team-projectId`
  * `allUsers`
  * `allAuthenticatedUsers`

Examples: 
  * The user `liz@example.com` would be `user-liz@example.com`.
  * The group `example@googlegroups.com` would be `group-example@googlegroups.com`.
  * To refer to all members of the domain `example.com`, the entity would be `domain-example.com`.

|  writable   
`entityId` | `string` | The ID for the entity, if any. |   
`etag` | `string` | HTTP 1.1 [Entity tag](https://datatracker.ietf.org/doc/html/rfc7232#section-2.3) for the access-control entry. |   
`kind` | `string` | The kind of item this is. For object access control entries, this is always `storage#objectAccessControl`. |   
`projectTeam` | `object` | The project team associated with the entity, if any. |   
`projectTeam.projectNumber` | `string` | The project number. |   
`projectTeam.team` | `string` | The team.   
  
Acceptable values are: 

  * "`editors`"
  * "`owners`"
  * "`viewers`"

|   
`role` | `string` | The access permission for the entity.   
  
Acceptable values are: 

  * "`OWNER`"
  * "`READER`"

|  writable   
  
## Methods

Buckets in Cloud Storage have an optional default object Access Control List. The methods for working with a bucket's default object access controls are as follows:

[delete](https://docs.cloud.google.com/storage/docs/json_api/v1/defaultObjectAccessControls/delete)
    Permanently deletes the default object ACL entry for the specified entity on the specified [bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets).
[get](https://docs.cloud.google.com/storage/docs/json_api/v1/defaultObjectAccessControls/get)
    Returns the default object ACL entry for the specified entity on the specified [bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets).
[insert](https://docs.cloud.google.com/storage/docs/json_api/v1/defaultObjectAccessControls/insert)
    Creates a new default object ACL entry on the specified [bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets).
[list](https://docs.cloud.google.com/storage/docs/json_api/v1/defaultObjectAccessControls/list)
    Retrieves default object ACL entries on the specified [bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets).
[patch](https://docs.cloud.google.com/storage/docs/json_api/v1/defaultObjectAccessControls/patch)
    Updates a default object ACL entry on the specified [bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets). This method supports [patch](https://docs.cloud.google.com/storage/docs/json_api#patch) semantics.
[update](https://docs.cloud.google.com/storage/docs/json_api/v1/defaultObjectAccessControls/update)
    Updates a default object ACL entry on the specified [bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
