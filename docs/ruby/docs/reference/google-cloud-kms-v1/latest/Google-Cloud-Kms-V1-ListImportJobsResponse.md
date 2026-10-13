---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-ListImportJobsResponse/
title: Cloud Key Management Service (KMS) V1 API - Class Google::Cloud::Kms::V1::ListImportJobsResponse (v1.16.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:35:19.503469+00:00
---

# Cloud Key Management Service (KMS) V1 API - Class Google::Cloud::Kms::V1::ListImportJobsResponse (v1.16.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-ListImportJobsResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Key Management Service (KMS) V1 API - Class Google::Cloud::Kms::V1::ListImportJobsResponse (v1.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.16.0 (latest)  1.15.2  1.14.0  1.13.0  1.12.1  1.11.0  1.10.0  1.9.2  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.2  1.2.1  1.1.0  1.0.2  0.27.0  0.26.0  0.25.1  0.24.3  0.23.0  0.22.1  0.21.0  0.20.0  0.19.0  0.18.1  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.2 

Reference documentation and code samples for the Cloud Key Management Service (KMS) V1 API class Google::Cloud::Kms::V1::ListImportJobsResponse.

Response message for [KeyManagementService.ListImportJobs](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-KeyManagementService-Client#Google__Cloud__Kms__V1__KeyManagementService__Client_list_import_jobs_instance_ "Google::Cloud::Kms::V1::KeyManagementService::Client#list_import_jobs \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #import_jobs
    
    
    def import_jobs() -> ::Array<::Google::Cloud::Kms::V1::ImportJob>

**Returns**

  * (::Array<[::Google::Cloud::Kms::V1::ImportJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-ImportJob)>) — The list of [ImportJobs](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-ImportJob "Google::Cloud::Kms::V1::ImportJob \(class\)"). 



### #import_jobs=
    
    
    def import_jobs=(value) -> ::Array<::Google::Cloud::Kms::V1::ImportJob>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Kms::V1::ImportJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-ImportJob)>) — The list of [ImportJobs](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-ImportJob "Google::Cloud::Kms::V1::ImportJob \(class\)"). 



**Returns**

  * (::Array<[::Google::Cloud::Kms::V1::ImportJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-ImportJob)>) — The list of [ImportJobs](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-ImportJob "Google::Cloud::Kms::V1::ImportJob \(class\)"). 



### #next_page_token
    
    
    def next_page_token() -> ::String

**Returns**

  * (::String) — A token to retrieve next page of results. Pass this value in [ListImportJobsRequest.page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-ListImportJobsRequest#Google__Cloud__Kms__V1__ListImportJobsRequest_page_token_instance_ "Google::Cloud::Kms::V1::ListImportJobsRequest#page_token \(method\)") to retrieve the next page of results. 



### #next_page_token=
    
    
    def next_page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — A token to retrieve next page of results. Pass this value in [ListImportJobsRequest.page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-ListImportJobsRequest#Google__Cloud__Kms__V1__ListImportJobsRequest_page_token_instance_ "Google::Cloud::Kms::V1::ListImportJobsRequest#page_token \(method\)") to retrieve the next page of results. 



**Returns**

  * (::String) — A token to retrieve next page of results. Pass this value in [ListImportJobsRequest.page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-ListImportJobsRequest#Google__Cloud__Kms__V1__ListImportJobsRequest_page_token_instance_ "Google::Cloud::Kms::V1::ListImportJobsRequest#page_token \(method\)") to retrieve the next page of results. 



### #total_size
    
    
    def total_size() -> ::Integer

**Returns**

  * (::Integer) — The total number of [ImportJobs](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-ImportJob "Google::Cloud::Kms::V1::ImportJob \(class\)") that matched the query.

This field is not populated if [ListImportJobsRequest.filter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-ListImportJobsRequest#Google__Cloud__Kms__V1__ListImportJobsRequest_filter_instance_ "Google::Cloud::Kms::V1::ListImportJobsRequest#filter \(method\)") is applied. 




### #total_size=
    
    
    def total_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The total number of [ImportJobs](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-ImportJob "Google::Cloud::Kms::V1::ImportJob \(class\)") that matched the query.

This field is not populated if [ListImportJobsRequest.filter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-ListImportJobsRequest#Google__Cloud__Kms__V1__ListImportJobsRequest_filter_instance_ "Google::Cloud::Kms::V1::ListImportJobsRequest#filter \(method\)") is applied. 




**Returns**

  * (::Integer) — The total number of [ImportJobs](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-ImportJob "Google::Cloud::Kms::V1::ImportJob \(class\)") that matched the query.

This field is not populated if [ListImportJobsRequest.filter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-ListImportJobsRequest#Google__Cloud__Kms__V1__ListImportJobsRequest_filter_instance_ "Google::Cloud::Kms::V1::ListImportJobsRequest#filter \(method\)") is applied. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
