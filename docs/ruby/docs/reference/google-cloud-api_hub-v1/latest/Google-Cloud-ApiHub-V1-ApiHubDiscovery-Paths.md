---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-ApiHubDiscovery-Paths/
title: API hub V1 API - Module Google::Cloud::ApiHub::V1::ApiHubDiscovery::Paths (v1.0.3) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:08:41.241938+00:00
---

# API hub V1 API - Module Google::Cloud::ApiHub::V1::ApiHubDiscovery::Paths (v1.0.3)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-ApiHubDiscovery-Paths/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  API hub V1 API - Module Google::Cloud::ApiHub::V1::ApiHubDiscovery::Paths (v1.0.3) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.3 (latest)  1.0.2  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0  0.1.1 

Reference documentation and code samples for the API hub V1 API module Google::Cloud::ApiHub::V1::ApiHubDiscovery::Paths.

Path helper methods for the ApiHubDiscovery API.

## Extended By

  * [Google::Cloud::ApiHub::V1::ApiHubDiscovery::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-ApiHubDiscovery-Paths)



## Included In

  * [Google::Cloud::ApiHub::V1::ApiHubDiscovery::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-ApiHubDiscovery-Paths)
  * [Google::Cloud::ApiHub::V1::ApiHubDiscovery::Rest::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-ApiHubDiscovery-Rest-Client)



## Methods 

### #discovered_api_observation_path
    
    
    def discovered_api_observation_path(project:, location:, discovered_api_observation:) -> ::String

Create a fully-qualified DiscoveredApiObservation resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/discoveredApiObservations/{discovered_api_observation}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **discovered_api_observation** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #discovered_api_operation_path
    
    
    def discovered_api_operation_path(project:, location:, discovered_api_observation:, discovered_api_operation:) -> ::String

Create a fully-qualified DiscoveredApiOperation resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/discoveredApiObservations/{discovered_api_observation}/discoveredApiOperations/{discovered_api_operation}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **discovered_api_observation** (String) 
  * **discovered_api_operation** (String) 



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



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
