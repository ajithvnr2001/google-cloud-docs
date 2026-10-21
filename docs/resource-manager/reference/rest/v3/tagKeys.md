---
url: https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagKeys/
title: REST Resource: tagKeys \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:08:31.750158+00:00
---

# REST Resource: tagKeys  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagKeys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager)
  * [ Reference ](https://docs.cloud.google.com/resource-manager/reference/rest)



Send feedback 

#  REST Resource: tagKeys Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: TagKey
    * JSON representation
  * Purpose
  * Methods



## Resource: TagKey

A TagKey, used to group a set of TagValues.

JSON representation  
---  
      
    
    {
      "name": string,
      "parent": string,
      "shortName": string,
      "namespacedName": string,
      "description": string,
      "createTime": string,
      "updateTime": string,
      "etag": string,
      "purpose": enum ([Purpose](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagKeys#Purpose)),
      "purposeData": {
        string: string,
        ...
      },
      "allowedValuesRegex": string
    }  
  
Fields  
---  
`name` |  `string` Immutable. The resource name for a TagKey. Must be in the format `tagKeys/{tag_key_id}`, where `tag_key_id` is the generated numeric id for the TagKey.  
`parent` |  `string` Immutable. The resource name of the TagKey's parent. A TagKey can be parented by an Organization or a Project. For a TagKey parented by an Organization, its parent must be in the form `organizations/{org_id}`. For a TagKey parented by a Project, its parent can be in the form `projects/{projectId}` or `projects/{projectNumber}`.  
`shortName` |  `string` Required. Immutable. The user friendly name for a TagKey. The short name should be unique for TagKeys within the same tag namespace.The short name must be 1-256 characters, beginning and ending with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots (.), and alphanumerics between.  
`namespacedName` |  `string` Output only. Immutable. Namespaced name of the TagKey.  
`description` |  `string` Optional. User-assigned description of the TagKey. Must not exceed 256 characters.Read-write.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Creation time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Update time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`etag` |  `string` Optional. Entity tag which users can pass to prevent race conditions. This field is always set in server responses. See UpdateTagKeyRequest for details.  
`purpose` |  `enum (`[Purpose](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagKeys#Purpose)`)` Optional. A purpose denotes that this Tag is intended for use in policies of a specific policy engine, and will involve that policy engine in management operations involving this Tag. A purpose does not grant a policy engine exclusive rights to the Tag, and it may be referenced by other policy engines.A purpose cannot be changed once set.  
`purposeData` |  `map (key: string, value: string)` Optional. Purpose data corresponds to the policy system that the tag is intended for. See documentation for `Purpose` for formatting of this field.Purpose data cannot be changed once set.  
`allowedValuesRegex` |  `string` Optional. Regular expression constraint for freeform tag values. If present, it implicitly allows freeform values (constrained by the regex).  
  
## Purpose

A purpose for each policy engine requiring such an integration. A single policy engine may have multiple purposes defined, however a TagKey may only specify a single purpose.

Enums  
---  
`PURPOSE_UNSPECIFIED` | Unspecified purpose.  
`GCE_FIREWALL` | Purpose for Compute Engine firewalls. A corresponding `purposeData` should be set for the network the tag is intended for. The key should be `network` and the value should be in`https://www.googleapis.com/compute/{compute_version}/projects/{projectId}/global/networks/{network_id}` \- `{projectId}/{network_name}` `https://www.googleapis.com/compute/staging_v1/projects/fail-closed-load-testing/global/networks/6992953698831725600` \- `fail-closed-load-testing/load-testing-network`  
`DATA_GOVERNANCE` | Purpose for data governance. Tag Values created under a key with this purpose may have Tag Value children. No `purposeData` should be set.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagKeys/create)`

|  Creates a new TagKey.  
  
### `[delete](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagKeys/delete)`

|  Deletes a TagKey.  
  
### `[get](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagKeys/get)`

|  Retrieves a TagKey.  
  
### `[getIamPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagKeys/getIamPolicy)`

|  Gets the access control policy for a TagKey.  
  
### `[getNamespaced](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagKeys/getNamespaced)`

|  Retrieves a TagKey by its namespaced name.  
  
### `[list](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagKeys/list)`

|  Lists all TagKeys for a parent resource.  
  
### `[patch](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagKeys/patch)`

|  Updates the attributes of the TagKey resource.  
  
### `[setIamPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagKeys/setIamPolicy)`

|  Sets the access control policy on a TagKey, replacing any existing policy.  
  
### `[testIamPermissions](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagKeys/testIamPermissions)`

|  Returns permissions that a caller has on the specified TagKey.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-09 UTC."],[],[]] 
