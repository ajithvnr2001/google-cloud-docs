---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-SecretManagerService-Paths/
title: Secret Manager V1 API - Module Google::Cloud::SecretManager::V1::SecretManagerService::Paths (v1.9.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:40:56.969771+00:00
---

# Secret Manager V1 API - Module Google::Cloud::SecretManager::V1::SecretManagerService::Paths (v1.9.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-SecretManagerService-Paths/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Secret Manager V1 API - Module Google::Cloud::SecretManager::V1::SecretManagerService::Paths (v1.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.9.1 (latest)  1.9.0  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.21.0  0.20.0  0.19.2  0.18.0  0.17.2  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.3 

Reference documentation and code samples for the Secret Manager V1 API module Google::Cloud::SecretManager::V1::SecretManagerService::Paths.

Path helper methods for the SecretManagerService API.

## Extended By

  * [Google::Cloud::SecretManager::V1::SecretManagerService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-SecretManagerService-Paths)



## Included In

  * [Google::Cloud::SecretManager::V1::SecretManagerService::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-SecretManagerService-Client)
  * [Google::Cloud::SecretManager::V1::SecretManagerService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-SecretManagerService-Paths)
  * [Google::Cloud::SecretManager::V1::SecretManagerService::Rest::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-SecretManagerService-Rest-Client)



## Methods 

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



### #project_path
    
    
    def project_path(project:) -> ::String

Create a fully-qualified Project resource string.

The resource will be in the following format:

`projects/{project}`

**Parameter**

  * **project** (String) 



**Returns**

  * (::String) 



### #secret_path
    
    
    def secret_path(project:, secret:) -> ::String
    def secret_path(project:, location:, secret:) -> ::String

Create a fully-qualified Secret resource string.

**Overloads**
    
    
    def secret_path(project:, secret:) -> ::String

The resource will be in the following format:

`projects/{project}/secrets/{secret}`

**Parameters**

  * **project** (String) 
  * **secret** (String) 


    
    
    def secret_path(project:, location:, secret:) -> ::String

The resource will be in the following format:

`projects/{project}/locations/{location}/secrets/{secret}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **secret** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #secret_version_path
    
    
    def secret_version_path(project:, secret:, secret_version:) -> ::String
    def secret_version_path(project:, location:, secret:, secret_version:) -> ::String

Create a fully-qualified SecretVersion resource string.

**Overloads**
    
    
    def secret_version_path(project:, secret:, secret_version:) -> ::String

The resource will be in the following format:

`projects/{project}/secrets/{secret}/versions/{secret_version}`

**Parameters**

  * **project** (String) 
  * **secret** (String) 
  * **secret_version** (String) 


    
    
    def secret_version_path(project:, location:, secret:, secret_version:) -> ::String

The resource will be in the following format:

`projects/{project}/locations/{location}/secrets/{secret}/versions/{secret_version}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **secret** (String) 
  * **secret_version** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #topic_path
    
    
    def topic_path(project:, topic:) -> ::String

Create a fully-qualified Topic resource string.

The resource will be in the following format:

`projects/{project}/topics/{topic}`

**Parameters**

  * **project** (String) 
  * **topic** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
