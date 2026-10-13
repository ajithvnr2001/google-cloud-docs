---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-JobService-Paths/
title: Cloud Talent Solution V4 API - Module Google::Cloud::Talent::V4::JobService::Paths (v1.9.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:11:54.500273+00:00
---

# Cloud Talent Solution V4 API - Module Google::Cloud::Talent::V4::JobService::Paths (v1.9.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-JobService-Paths/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Talent Solution V4 API - Module Google::Cloud::Talent::V4::JobService::Paths (v1.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.9.1 (latest)  1.9.0  1.8.1  1.7.0  1.6.1  1.5.0  1.4.0  1.3.1  1.2.0  1.1.0  1.0.1  0.13.0  0.12.2  0.11.0  0.10.1  0.9.1  0.8.1  0.7.0  0.6.4 

Reference documentation and code samples for the Cloud Talent Solution V4 API module Google::Cloud::Talent::V4::JobService::Paths.

Path helper methods for the JobService API.

## Extended By

  * [Google::Cloud::Talent::V4::JobService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-JobService-Paths)



## Included In

  * [Google::Cloud::Talent::V4::JobService::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-JobService-Client)
  * [Google::Cloud::Talent::V4::JobService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-JobService-Paths)
  * [Google::Cloud::Talent::V4::JobService::Rest::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-JobService-Rest-Client)



## Methods 

### #company_path
    
    
    def company_path(project:, tenant:, company:) -> ::String

Create a fully-qualified Company resource string.

The resource will be in the following format:

`projects/{project}/tenants/{tenant}/companies/{company}`

**Parameters**

  * **project** (String) 
  * **tenant** (String) 
  * **company** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #job_path
    
    
    def job_path(project:, tenant:, job:) -> ::String

Create a fully-qualified Job resource string.

The resource will be in the following format:

`projects/{project}/tenants/{tenant}/jobs/{job}`

**Parameters**

  * **project** (String) 
  * **tenant** (String) 
  * **job** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #tenant_path
    
    
    def tenant_path(project:, tenant:) -> ::String

Create a fully-qualified Tenant resource string.

The resource will be in the following format:

`projects/{project}/tenants/{tenant}`

**Parameters**

  * **project** (String) 
  * **tenant** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
