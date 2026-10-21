---
url: https://docs.cloud.google.com/resource-manager/reference/rest/v3/locations.tagBindingCollections
title: REST Resource: locations.tagBindingCollections \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:57:46.176020+00:00
---

# REST Resource: locations.tagBindingCollections  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/reference/rest/v3/locations.tagBindingCollections

  * [ Home ](https://docs.cloud.google.com/)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager)
  * [ Reference ](https://docs.cloud.google.com/resource-manager/reference/rest)



Send feedback 

#  REST Resource: locations.tagBindingCollections Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: TagBindingCollection
    * JSON representation
  * Methods



## Resource: TagBindingCollection

Represents a collection of tags directly bound to a Google Cloud resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "fullResourceName": string,
      "tags": {
        string: string,
        ...
      },
      "etag": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the TagBindingCollection, following the convention: `locations/{location}/tagBindingCollections/{encoded-full-resource-name}` where the encoded-full-resource-name is the UTF-8 encoded name of the Google Cloud resource the TagBindings are bound to. "locations/global/tagBindingCollections/%2f%2fcloudresourcemanager.googleapis.com%2fprojects%2f123"  
`fullResourceName` |  `string` The full resource name of the resource the TagBindings are bound to. E.g. `//cloudresourcemanager.googleapis.com/projects/123`  
`tags` |  `map (key: string, value: string)` Tag keys/values directly bound to this resource, specified in namespaced format. For example: "123/environment": "production"  
`etag` |  `string` Optional. A checksum based on the current bindings which can be passed to prevent race conditions. This field is always set in server responses.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/resource-manager/reference/rest/v3/locations.tagBindingCollections/get)`

|  Returns tag bindings directly attached to a Google Cloud resource.  
  
### `[patch](https://docs.cloud.google.com/resource-manager/reference/rest/v3/locations.tagBindingCollections/patch)`

|  Updates tag bindings directly attached to a Google Cloud resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-01 UTC."],[],[]] 
