---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-AddressGroupService-Paths/
title: Network Security V1 API - Module Google::Cloud::NetworkSecurity::V1::AddressGroupService::Paths (v0.1.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:25:23.688885+00:00
---

# Network Security V1 API - Module Google::Cloud::NetworkSecurity::V1::AddressGroupService::Paths (v0.1.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-AddressGroupService-Paths/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Network Security V1 API - Module Google::Cloud::NetworkSecurity::V1::AddressGroupService::Paths (v0.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

Reference documentation and code samples for the Network Security V1 API module Google::Cloud::NetworkSecurity::V1::AddressGroupService::Paths.

Path helper methods for the AddressGroupService API.

## Extended By

  * [Google::Cloud::NetworkSecurity::V1::AddressGroupService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-AddressGroupService-Paths)



## Included In

  * [Google::Cloud::NetworkSecurity::V1::AddressGroupService::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-AddressGroupService-Client)
  * [Google::Cloud::NetworkSecurity::V1::AddressGroupService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-AddressGroupService-Paths)



## Methods 

### #address_group_path
    
    
    def address_group_path(project:, location:, address_group:) -> ::String
    def address_group_path(organization:, location:, address_group:) -> ::String

Create a fully-qualified AddressGroup resource string.

**Overloads**
    
    
    def address_group_path(project:, location:, address_group:) -> ::String

The resource will be in the following format:

`projects/{project}/locations/{location}/addressGroups/{address_group}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **address_group** (String) 


    
    
    def address_group_path(organization:, location:, address_group:) -> ::String

The resource will be in the following format:

`organizations/{organization}/locations/{location}/addressGroups/{address_group}`

**Parameters**

  * **organization** (String) 
  * **location** (String) 
  * **address_group** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #location_path
    
    
    def location_path(project:, location:) -> ::String

Create a fully-qualified Location resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}`

**Parameters**

  * **project** (String) 
  * **location** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #organization_location_path
    
    
    def organization_location_path(organization:, location:) -> ::String

Create a fully-qualified OrganizationLocation resource string.

The resource will be in the following format:

`organizations/{organization}/locations/{location}`

**Parameters**

  * **organization** (String) 
  * **location** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-07 UTC."],[],[]] 
