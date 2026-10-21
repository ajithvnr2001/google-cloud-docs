---
url: https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.customRanges
title: REST Resource: projects.locations.customRanges \u00a0|\u00a0 Cloud Number Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:34:06.525505+00:00
---

# REST Resource: projects.locations.customRanges  |  Cloud Number Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.customRanges

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Number Registry ](https://docs.cloud.google.com/number-registry)
  * [ Reference ](https://docs.cloud.google.com/number-registry/apis)



Send feedback 

#  REST Resource: projects.locations.customRanges Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: CustomRange
    * JSON representation
  * Methods



## Resource: CustomRange

A CustomRange represents a user-defined IP address range.

JSON representation  
---  
      
    
    {
      "name": string,
      "realm": string,
      "parentRange": string,
      "registryBook": string,
      "attributes": [
        {
          object ([Attribute](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/Attribute))
        }
      ],
      "description": string,
      "labels": {
        string: string,
        ...
      },
    
      // Union field ip_cidr_range can be only one of the following:
      "ipv4CidrRange": string,
      "ipv6CidrRange": string
      // End of list of possible types for union field ip_cidr_range.
    }  
  
Fields  
---  
`name` |  `string` Required. Identifier. The resource name of the CustomRange, in the format `projects/{project}/locations/{location}/customRanges/{customRange}`.  
`realm` |  `string` Optional. The resource name of the Realm associated with the CustomRange, in the format `projects/{project}/locations/{location}/realms/{realm}`. The Realm must be in the same project as the CustomRange. This field must not be set if the `parentRange` field is set, as the Realm will be inherited from the parent CustomRange.  
`parentRange` |  `string` Optional. The resource name of the parent CustomRange, in the format `projects/{project}/locations/{location}/customRanges/{customRange}`. If specified, the parent CustomRange must be in the same RegistryBook. This field is mutually exclusive with the `realm` field, as the Realm is inherited from the parent CustomRange.  
`registryBook` |  `string` Output only. The RegistryBook of the CustomRange. This field is inherited from the Realm or parent CustomRange depending on which one is specified.  
`attributes[]` |  `object (`[Attribute](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/Attribute)`)` Optional. The attributes of the CustomRange.  
`description` |  `string` Optional. The description of the CustomRange.  
`labels` |  `map (key: string, value: string)` Optional. User-defined labels.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
Union field `ip_cidr_range`. The IP CIDR range of the CustomRange. `ip_cidr_range` can be only one of the following:  
`ipv4CidrRange` |  `string` Optional. The IPv4 CIDR range of the CustomRange.  
`ipv6CidrRange` |  `string` Optional. The IPv6 CIDR range of the CustomRange.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.customRanges/create)`

|  Creates a new CustomRange in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.customRanges/delete)`

|  Deletes a single CustomRange.  
  
### `[findFreeIpRanges](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.customRanges/findFreeIpRanges)`

|  Finds free IP ranges in a single CustomRange.  
  
### `[get](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.customRanges/get)`

|  Gets details of a single CustomRange.  
  
### `[list](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.customRanges/list)`

|  Lists CustomRanges in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.customRanges/patch)`

|  Updates the parameters of a single CustomRange.  
  
### `[showUtilization](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.customRanges/showUtilization)`

|  Gets the details of a single CustomRange and its utilization.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-02 UTC."],[],[]] 
