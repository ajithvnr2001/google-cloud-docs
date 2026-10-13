---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1beta/latest/Google-Cloud-CloudQuotas-V1beta-CloudQuotas-Paths/
title: Cloud Quotas V1BETA API - Module Google::Cloud::CloudQuotas::V1beta::CloudQuotas::Paths (v0.10.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:38:33.177666+00:00
---

# Cloud Quotas V1BETA API - Module Google::Cloud::CloudQuotas::V1beta::CloudQuotas::Paths (v0.10.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1beta/latest/Google-Cloud-CloudQuotas-V1beta-CloudQuotas-Paths/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Quotas V1BETA API - Module Google::Cloud::CloudQuotas::V1beta::CloudQuotas::Paths (v0.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.1 (latest)  0.10.0  0.9.0  0.8.0  0.7.0  0.6.2  0.5.0  0.4.0  0.3.2  0.2.0  0.1.0 

Reference documentation and code samples for the Cloud Quotas V1BETA API module Google::Cloud::CloudQuotas::V1beta::CloudQuotas::Paths.

Path helper methods for the CloudQuotas API.

## Extended By

  * [Google::Cloud::CloudQuotas::V1beta::CloudQuotas::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1beta/latest/Google-Cloud-CloudQuotas-V1beta-CloudQuotas-Paths)



## Included In

  * [Google::Cloud::CloudQuotas::V1beta::CloudQuotas::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1beta/latest/Google-Cloud-CloudQuotas-V1beta-CloudQuotas-Client)
  * [Google::Cloud::CloudQuotas::V1beta::CloudQuotas::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1beta/latest/Google-Cloud-CloudQuotas-V1beta-CloudQuotas-Paths)
  * [Google::Cloud::CloudQuotas::V1beta::CloudQuotas::Rest::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1beta/latest/Google-Cloud-CloudQuotas-V1beta-CloudQuotas-Rest-Client)



## Methods 

### #location_path
    
    
    def location_path(project:, location:) -> ::String
    def location_path(folder:, location:) -> ::String
    def location_path(organization:, location:) -> ::String

Create a fully-qualified Location resource string.

**Overloads**
    
    
    def location_path(project:, location:) -> ::String

The resource will be in the following format:

`projects/{project}/locations/{location}`

**Parameters**

  * **project** (String) 
  * **location** (String) 


    
    
    def location_path(folder:, location:) -> ::String

The resource will be in the following format:

`folders/{folder}/locations/{location}`

**Parameters**

  * **folder** (String) 
  * **location** (String) 


    
    
    def location_path(organization:, location:) -> ::String

The resource will be in the following format:

`organizations/{organization}/locations/{location}`

**Parameters**

  * **organization** (String) 
  * **location** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #quota_info_path
    
    
    def quota_info_path(project:, location:, service:, quota_info:) -> ::String
    def quota_info_path(folder:, location:, service:, quota_info:) -> ::String
    def quota_info_path(organization:, location:, service:, quota_info:) -> ::String

Create a fully-qualified QuotaInfo resource string.

**Overloads**
    
    
    def quota_info_path(project:, location:, service:, quota_info:) -> ::String

The resource will be in the following format:

`projects/{project}/locations/{location}/services/{service}/quotaInfos/{quota_info}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **service** (String) 
  * **quota_info** (String) 


    
    
    def quota_info_path(folder:, location:, service:, quota_info:) -> ::String

The resource will be in the following format:

`folders/{folder}/locations/{location}/services/{service}/quotaInfos/{quota_info}`

**Parameters**

  * **folder** (String) 
  * **location** (String) 
  * **service** (String) 
  * **quota_info** (String) 


    
    
    def quota_info_path(organization:, location:, service:, quota_info:) -> ::String

The resource will be in the following format:

`organizations/{organization}/locations/{location}/services/{service}/quotaInfos/{quota_info}`

**Parameters**

  * **organization** (String) 
  * **location** (String) 
  * **service** (String) 
  * **quota_info** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #quota_preference_path
    
    
    def quota_preference_path(project:, location:, quota_preference:) -> ::String
    def quota_preference_path(folder:, location:, quota_preference:) -> ::String
    def quota_preference_path(organization:, location:, quota_preference:) -> ::String

Create a fully-qualified QuotaPreference resource string.

**Overloads**
    
    
    def quota_preference_path(project:, location:, quota_preference:) -> ::String

The resource will be in the following format:

`projects/{project}/locations/{location}/quotaPreferences/{quota_preference}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **quota_preference** (String) 


    
    
    def quota_preference_path(folder:, location:, quota_preference:) -> ::String

The resource will be in the following format:

`folders/{folder}/locations/{location}/quotaPreferences/{quota_preference}`

**Parameters**

  * **folder** (String) 
  * **location** (String) 
  * **quota_preference** (String) 


    
    
    def quota_preference_path(organization:, location:, quota_preference:) -> ::String

The resource will be in the following format:

`organizations/{organization}/locations/{location}/quotaPreferences/{quota_preference}`

**Parameters**

  * **organization** (String) 
  * **location** (String) 
  * **quota_preference** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #service_path
    
    
    def service_path(project:, location:, service:) -> ::String
    def service_path(folder:, location:, service:) -> ::String
    def service_path(organization:, location:, service:) -> ::String

Create a fully-qualified Service resource string.

**Overloads**
    
    
    def service_path(project:, location:, service:) -> ::String

The resource will be in the following format:

`projects/{project}/locations/{location}/services/{service}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **service** (String) 


    
    
    def service_path(folder:, location:, service:) -> ::String

The resource will be in the following format:

`folders/{folder}/locations/{location}/services/{service}`

**Parameters**

  * **folder** (String) 
  * **location** (String) 
  * **service** (String) 


    
    
    def service_path(organization:, location:, service:) -> ::String

The resource will be in the following format:

`organizations/{organization}/locations/{location}/services/{service}`

**Parameters**

  * **organization** (String) 
  * **location** (String) 
  * **service** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
