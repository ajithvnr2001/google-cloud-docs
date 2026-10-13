---
url: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.catalogs.shares
title: REST Resource: projects.locations.spaces.catalogs.shares \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:30:32.947811+00:00
---

# REST Resource: projects.locations.spaces.catalogs.shares  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.catalogs.shares

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Reference ](https://docs.cloud.google.com/application-design-center/docs/apis)



Send feedback 

#  REST Resource: projects.locations.spaces.catalogs.shares Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Share
    * JSON representation
  * State
  * Methods



## Resource: Share

A catalog share between spaces.

JSON representation  
---  
      
    
    {
      "name": string,
      "destinationSpace": string,
      "createTime": string,
      "state": enum ([State](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.catalogs.shares#State))
    }  
  
Fields  
---  
`name` |  `string` Identifier. The share name in the following format: `projects/$project/locations/$location/spaces/$space/catalogs/$catalog/shares/$share`  
`destinationSpace` |  `string` Required. The space resource path to which the catalog is shared. Format is `projects/$project/locations/$location/spaces/$space`  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The share creation timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.catalogs.shares#State)`)` Output only. The state of the share.  
  
## State

The share status, which indicates whether the catalog is in sync.

Enums  
---  
`STATE_UNSPECIFIED` | The state of the share is unknown.  
`IN_SYNC` | The share is in sync with the shared template catalog.  
`OUT_OF_SYNC` | The share is out of sync with the shared template catalog.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.catalogs.shares/create)`

|  Shares a catalog from one space to another space.  
  
### `[delete](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.catalogs.shares/delete)`

|  Deletes a catalog share.  
  
### `[get](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.catalogs.shares/get)`

|  Get catalog share object for the space.  
  
### `[list](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.catalogs.shares/list)`

|  Lists catalog share objects for the space.  
  
### `[sync](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.catalogs.shares/sync)`

|  Synchronizes a share and updates the destination workspace to reflect.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-13 UTC."],[],[]] 
