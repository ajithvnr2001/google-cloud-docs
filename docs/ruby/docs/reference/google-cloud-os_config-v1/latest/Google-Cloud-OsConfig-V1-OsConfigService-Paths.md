---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1/latest/Google-Cloud-OsConfig-V1-OsConfigService-Paths/
title: Cloud OS Config V1 API - Module Google::Cloud::OsConfig::V1::OsConfigService::Paths (v1.9.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:57:45.614854+00:00
---

# Cloud OS Config V1 API - Module Google::Cloud::OsConfig::V1::OsConfigService::Paths (v1.9.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1/latest/Google-Cloud-OsConfig-V1-OsConfigService-Paths/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud OS Config V1 API - Module Google::Cloud::OsConfig::V1::OsConfigService::Paths (v1.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.9.0 (latest)  1.8.1  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.16.0  0.15.2  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.1 

Reference documentation and code samples for the Cloud OS Config V1 API module Google::Cloud::OsConfig::V1::OsConfigService::Paths.

Path helper methods for the OsConfigService API.

## Extended By

  * [Google::Cloud::OsConfig::V1::OsConfigService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1/latest/Google-Cloud-OsConfig-V1-OsConfigService-Paths)



## Included In

  * [Google::Cloud::OsConfig::V1::OsConfigService::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1/latest/Google-Cloud-OsConfig-V1-OsConfigService-Client)
  * [Google::Cloud::OsConfig::V1::OsConfigService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1/latest/Google-Cloud-OsConfig-V1-OsConfigService-Paths)
  * [Google::Cloud::OsConfig::V1::OsConfigService::Rest::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1/latest/Google-Cloud-OsConfig-V1-OsConfigService-Rest-Client)



## Methods 

### #patch_deployment_path
    
    
    def patch_deployment_path(project:, patch_deployment:) -> ::String

Create a fully-qualified PatchDeployment resource string.

The resource will be in the following format:

`projects/{project}/patchDeployments/{patch_deployment}`

**Parameters**

  * **project** (String) 
  * **patch_deployment** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #patch_job_path
    
    
    def patch_job_path(project:, patch_job:) -> ::String

Create a fully-qualified PatchJob resource string.

The resource will be in the following format:

`projects/{project}/patchJobs/{patch_job}`

**Parameters**

  * **project** (String) 
  * **patch_job** (String) 



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



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
