---
url: https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagValues/
title: REST Resource: tagValues \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:08:32.798506+00:00
---

# REST Resource: tagValues  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagValues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager)
  * [ Reference ](https://docs.cloud.google.com/resource-manager/reference/rest)



Send feedback 

#  REST Resource: tagValues Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: TagValue
    * JSON representation
  * Methods



## Resource: TagValue

A TagValue is a child of a particular TagKey. This is used to group cloud resources for the purpose of controlling them using policies.

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
      "etag": string
    }  
  
Fields  
---  
`name` |  `string` Immutable. Resource name for TagValue in the format `tagValues/456`.  
`parent` |  `string` Immutable. The resource name of the new TagValue's parent TagKey. Must be of the form `tagKeys/{tag_key_id}`.  
`shortName` |  `string` Required. Immutable. User-assigned short name for TagValue. The short name should be unique for TagValues within the same parent TagKey.The short name must be 256 characters or less, beginning and ending with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots (.), and alphanumerics between.  
`namespacedName` |  `string` Output only. The namespaced name of the TagValue. Can be in the form `{organizationId}/{tag_key_short_name}/{tag_value_short_name}` or `{projectId}/{tag_key_short_name}/{tag_value_short_name}` or `{projectNumber}/{tag_key_short_name}/{tag_value_short_name}`.  
`description` |  `string` Optional. User-assigned description of the TagValue. Must not exceed 256 characters.Read-write.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Creation time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Update time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`etag` |  `string` Optional. Entity tag which users can pass to prevent race conditions. This field is always set in server responses. See UpdateTagValueRequest for details.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagValues/create)`

|  Creates a TagValue as a child of the specified TagKey.  
  
### `[delete](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagValues/delete)`

|  Deletes a TagValue.  
  
### `[get](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagValues/get)`

|  Retrieves a TagValue.  
  
### `[getIamPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagValues/getIamPolicy)`

|  Gets the access control policy for a TagValue.  
  
### `[getNamespaced](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagValues/getNamespaced)`

|  Retrieves a TagValue by its namespaced name.  
  
### `[list](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagValues/list)`

|  Lists all TagValues for a specific TagKey.  
  
### `[patch](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagValues/patch)`

|  Updates the attributes of the TagValue resource.  
  
### `[setIamPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagValues/setIamPolicy)`

|  Sets the access control policy on a TagValue, replacing any existing policy.  
  
### `[testIamPermissions](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagValues/testIamPermissions)`

|  Returns permissions that a caller has on the specified TagValue.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-09 UTC."],[],[]] 
