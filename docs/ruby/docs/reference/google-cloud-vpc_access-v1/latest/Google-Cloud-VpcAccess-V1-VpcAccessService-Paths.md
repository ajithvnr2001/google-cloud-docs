---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vpc_access-v1/latest/Google-Cloud-VpcAccess-V1-VpcAccessService-Paths/
title: Serverless VPC Access V1 API - Module Google::Cloud::VpcAccess::V1::VpcAccessService::Paths (v1.7.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:09:31.092773+00:00
---

# Serverless VPC Access V1 API - Module Google::Cloud::VpcAccess::V1::VpcAccessService::Paths (v1.7.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vpc_access-v1/latest/Google-Cloud-VpcAccess-V1-VpcAccessService-Paths/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Serverless VPC Access V1 API - Module Google::Cloud::VpcAccess::V1::VpcAccessService::Paths (v1.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.1 (latest)  1.7.0  1.6.1  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.2  0.8.0  0.7.2  0.6.0  0.5.1  0.4.0  0.3.0  0.2.0  0.1.4 

Reference documentation and code samples for the Serverless VPC Access V1 API module Google::Cloud::VpcAccess::V1::VpcAccessService::Paths.

Path helper methods for the VpcAccessService API.

## Extended By

  * [Google::Cloud::VpcAccess::V1::VpcAccessService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vpc_access-v1/latest/Google-Cloud-VpcAccess-V1-VpcAccessService-Paths)



## Included In

  * [Google::Cloud::VpcAccess::V1::VpcAccessService::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vpc_access-v1/latest/Google-Cloud-VpcAccess-V1-VpcAccessService-Client)
  * [Google::Cloud::VpcAccess::V1::VpcAccessService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vpc_access-v1/latest/Google-Cloud-VpcAccess-V1-VpcAccessService-Paths)
  * [Google::Cloud::VpcAccess::V1::VpcAccessService::Rest::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vpc_access-v1/latest/Google-Cloud-VpcAccess-V1-VpcAccessService-Rest-Client)



## Methods 

### #connector_path
    
    
    def connector_path(project:, location:, connector:) -> ::String

Create a fully-qualified Connector resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/connectors/{connector}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **connector** (String) 



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
