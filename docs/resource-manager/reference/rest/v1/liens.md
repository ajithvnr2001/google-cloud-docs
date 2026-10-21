---
url: https://docs.cloud.google.com/resource-manager/reference/rest/v1/liens/
title: REST Resource: liens \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:08:18.696107+00:00
---

# REST Resource: liens  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/reference/rest/v1/liens/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager)
  * [ Reference ](https://docs.cloud.google.com/resource-manager/reference/rest)



Send feedback 

#  REST Resource: liens Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Lien
    * JSON representation
  * Methods



## Resource: Lien

A Lien represents an encumbrance on the actions that can be performed on a resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "parent": string,
      "restrictions": [
        string
      ],
      "reason": string,
      "origin": string,
      "createTime": string
    }  
  
Fields  
---  
`name` |  `string` A system-generated unique identifier for this Lien.Example: `liens/1234abcd`  
`parent` |  `string` A reference to the resource this Lien is attached to. The server will validate the parent against those for which Liens are supported.Example: `projects/1234`  
`restrictions[]` |  `string` The types of operations which should be blocked as a result of this Lien. Each value should correspond to an IAM permission. The server will validate the permissions against those for which Liens are supported.An empty list is meaningless and will be rejected.Example: ['resourcemanager.projects.delete']  
`reason` |  `string` Concise user-visible strings indicating why an action cannot be performed on a resource. Maximum length of 200 characters.Example: 'Holds production API key'  
`origin` |  `string` A stable, user-visible/meaningful string identifying the origin of the Lien, intended to be inspected programmatically. Maximum length of 200 characters.Example: 'compute.googleapis.com'  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The creation time of this Lien.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/resource-manager/reference/rest/v1/liens/create)`

|  Create a Lien which applies to the resource denoted by the `parent` field.  
  
### `[delete](https://docs.cloud.google.com/resource-manager/reference/rest/v1/liens/delete)`

|  Delete a Lien by `name`.  
  
### `[get](https://docs.cloud.google.com/resource-manager/reference/rest/v1/liens/get)`

|  Retrieve a Lien by `name`.  
  
### `[list](https://docs.cloud.google.com/resource-manager/reference/rest/v1/liens/list)`

|  List all Liens applied to the `parent` resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-09 UTC."],[],[]] 
