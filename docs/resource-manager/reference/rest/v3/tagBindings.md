---
url: https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagBindings/
title: REST Resource: tagBindings \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:08:31.158849+00:00
---

# REST Resource: tagBindings  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagBindings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager)
  * [ Reference ](https://docs.cloud.google.com/resource-manager/reference/rest)



Send feedback 

#  REST Resource: tagBindings Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: TagBinding
    * JSON representation
  * Methods



## Resource: TagBinding

A TagBinding represents a connection between a TagValue and a cloud resource Once a TagBinding is created, the TagValue is applied to all the descendants of the Google Cloud resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "parent": string,
      "tagValue": string,
      "tagValueNamespacedName": string
    }  
  
Fields  
---  
`name` |  `string` Output only. The name of the TagBinding. This is a String of the form: `tagBindings/{full-resource-name}/{tag-value-name}` (e.g. `tagBindings/%2F%2Fcloudresourcemanager.googleapis.com%2Fprojects%2F123/tagValues/456`).  
`parent` |  `string` The full resource name of the resource the TagValue is bound to. E.g. `//cloudresourcemanager.googleapis.com/projects/123`  
`tagValue` |  `string` The TagValue of the TagBinding. Must be of the form `tagValues/456`.  
`tagValueNamespacedName` |  `string` The namespaced name for the TagValue of the TagBinding. Must be in the format `{parent_id}/{tag_key_short_name}/{shortName}`.For methods that support TagValue namespaced name, only one of tagValueNamespacedName or tagValue may be filled. Requests with both fields will be rejected.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagBindings/create)`

|  Creates a TagBinding between a TagValue and a Google Cloud resource.  
  
### `[delete](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagBindings/delete)`

|  Deletes a TagBinding.  
  
### `[list](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagBindings/list)`

|  Lists the TagBindings for the given Google Cloud resource, as specified with `parent`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-11 UTC."],[],[]] 
