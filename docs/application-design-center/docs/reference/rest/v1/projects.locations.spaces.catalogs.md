---
url: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs
title: REST Resource: projects.locations.spaces.catalogs \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:30:15.206740+00:00
---

# REST Resource: projects.locations.spaces.catalogs  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Reference ](https://docs.cloud.google.com/application-design-center/docs/apis)



Send feedback 

#  REST Resource: projects.locations.spaces.catalogs Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Catalog
    * JSON representation
  * Methods



## Resource: Catalog

A collection of templates.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "createTime": string,
      "updateTime": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The catalog name in the following format: `projects/$project/locations/$location/spaces/$space/catalogs/$catalog`  
`displayName` |  `string` Optional. The catalog display name.  
`description` |  `string` Optional. The catalog description.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The catalog creation timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The catalog update timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs/create)`

|  Creates a catalog.  
  
### `[delete](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs/delete)`

|  Deletes a catalog.  
  
### `[get](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs/get)`

|  Gets details about a catalog.  
  
### `[list](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs/list)`

|  Lists catalogs in a given space.  
  
### `[patch](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs/patch)`

|  Updates a catalog.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-13 UTC."],[],[]] 
