---
url: https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.registryBooks
title: REST Resource: projects.locations.registryBooks \u00a0|\u00a0 Cloud Number Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:34:13.211805+00:00
---

# REST Resource: projects.locations.registryBooks  |  Cloud Number Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.registryBooks

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Number Registry ](https://docs.cloud.google.com/number-registry)
  * [ Reference ](https://docs.cloud.google.com/number-registry/apis)



Send feedback 

#  REST Resource: projects.locations.registryBooks Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: RegistryBook
    * JSON representation
  * AggregatedData
    * JSON representation
  * Methods



## Resource: RegistryBook

A RegistryBook organizes and manages IP address space. It claims specific scopes (such as projects) and groups related Realms and Ranges.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "labels": {
        string: string,
        ...
      },
      "claimedScopes": [
        string
      ],
      "isDefault": boolean,
      "aggregatedData": {
        object ([AggregatedData](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.registryBooks#AggregatedData))
      }
    }  
  
Fields  
---  
`name` |  `string` Required. Identifier. The resource name of the RegistryBook.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the RegistryBook was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the RegistryBook was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Optional. User-defined labels.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`claimedScopes[]` |  `string` Optional. List of scopes claimed by the RegistryBook. In Preview, Only project scope is supported. Each scope is in the format of projects/{project}. Each scope can only be claimed once.  
`isDefault` |  `boolean` Output only. Whether the RegistryBook is the default one.  
`aggregatedData` |  `object (`[AggregatedData](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.registryBooks#AggregatedData)`)` Output only. Aggregated data for the RegistryBook. Populated only when the view is AGGREGATE.  
  
## AggregatedData

Aggregated data for the RegistryBook.

JSON representation  
---  
      
    
    {
      "uniqueScopesCount": integer,
      "discoveredRealmsCount": integer,
      "discoveredRangesCount": integer,
      "customRealmsCount": integer,
      "customRangesCount": integer
    }  
  
Fields  
---  
`uniqueScopesCount` |  `integer` Output only. Number of scopes unique to the RegistryBook.  
`discoveredRealmsCount` |  `integer` Output only. Number of discovered Realms in the RegistryBook.  
`discoveredRangesCount` |  `integer` Output only. Number of DiscoveredRanges in the RegistryBook.  
`customRealmsCount` |  `integer` Output only. Number of custom Realms in the RegistryBook.  
`customRangesCount` |  `integer` Output only. Number of CustomRanges in the RegistryBook.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.registryBooks/create)`

|  Creates a new RegistryBook in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.registryBooks/delete)`

|  Deletes a single RegistryBook.  
  
### `[get](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.registryBooks/get)`

|  Gets details of a single RegistryBook.  
  
### `[list](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.registryBooks/list)`

|  Lists RegistryBooks in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.registryBooks/patch)`

|  Updates the parameters of a single RegistryBook.  
  
### `[searchIpResources](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.registryBooks/searchIpResources)`

|  Searches IP resources in a given RegistryBook.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-02 UTC."],[],[]] 
