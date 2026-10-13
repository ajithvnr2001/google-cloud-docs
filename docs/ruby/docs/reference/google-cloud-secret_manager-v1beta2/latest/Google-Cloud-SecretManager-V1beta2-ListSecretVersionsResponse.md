---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-ListSecretVersionsResponse/
title: Secret Manager V1BETA2 API - Class Google::Cloud::SecretManager::V1beta2::ListSecretVersionsResponse (v0.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:19:55.976466+00:00
---

# Secret Manager V1BETA2 API - Class Google::Cloud::SecretManager::V1beta2::ListSecretVersionsResponse (v0.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-ListSecretVersionsResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Secret Manager V1BETA2 API - Class Google::Cloud::SecretManager::V1beta2::ListSecretVersionsResponse (v0.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.1 (latest)  0.8.0  0.7.1  0.6.0  0.5.1  0.4.0  0.3.1  0.2.0  0.1.1 

Reference documentation and code samples for the Secret Manager V1BETA2 API class Google::Cloud::SecretManager::V1beta2::ListSecretVersionsResponse.

Response message for [SecretManagerService.ListSecretVersions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-SecretManagerService-Client#Google__Cloud__SecretManager__V1beta2__SecretManagerService__Client_list_secret_versions_instance_ "Google::Cloud::SecretManager::V1beta2::SecretManagerService::Client#list_secret_versions \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #next_page_token
    
    
    def next_page_token() -> ::String

**Returns**

  * (::String) — A token to retrieve the next page of results. Pass this value in [ListSecretVersionsRequest.page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-ListSecretVersionsRequest#Google__Cloud__SecretManager__V1beta2__ListSecretVersionsRequest_page_token_instance_ "Google::Cloud::SecretManager::V1beta2::ListSecretVersionsRequest#page_token \(method\)") to retrieve the next page. 



### #next_page_token=
    
    
    def next_page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — A token to retrieve the next page of results. Pass this value in [ListSecretVersionsRequest.page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-ListSecretVersionsRequest#Google__Cloud__SecretManager__V1beta2__ListSecretVersionsRequest_page_token_instance_ "Google::Cloud::SecretManager::V1beta2::ListSecretVersionsRequest#page_token \(method\)") to retrieve the next page. 



**Returns**

  * (::String) — A token to retrieve the next page of results. Pass this value in [ListSecretVersionsRequest.page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-ListSecretVersionsRequest#Google__Cloud__SecretManager__V1beta2__ListSecretVersionsRequest_page_token_instance_ "Google::Cloud::SecretManager::V1beta2::ListSecretVersionsRequest#page_token \(method\)") to retrieve the next page. 



### #total_size
    
    
    def total_size() -> ::Integer

**Returns**

  * (::Integer) — The total number of [SecretVersions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-SecretVersion "Google::Cloud::SecretManager::V1beta2::SecretVersion \(class\)") but 0 when the [ListSecretsRequest.filter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-ListSecretsRequest#Google__Cloud__SecretManager__V1beta2__ListSecretsRequest_filter_instance_ "Google::Cloud::SecretManager::V1beta2::ListSecretsRequest#filter \(method\)") field is set. 



### #total_size=
    
    
    def total_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The total number of [SecretVersions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-SecretVersion "Google::Cloud::SecretManager::V1beta2::SecretVersion \(class\)") but 0 when the [ListSecretsRequest.filter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-ListSecretsRequest#Google__Cloud__SecretManager__V1beta2__ListSecretsRequest_filter_instance_ "Google::Cloud::SecretManager::V1beta2::ListSecretsRequest#filter \(method\)") field is set. 



**Returns**

  * (::Integer) — The total number of [SecretVersions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-SecretVersion "Google::Cloud::SecretManager::V1beta2::SecretVersion \(class\)") but 0 when the [ListSecretsRequest.filter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-ListSecretsRequest#Google__Cloud__SecretManager__V1beta2__ListSecretsRequest_filter_instance_ "Google::Cloud::SecretManager::V1beta2::ListSecretsRequest#filter \(method\)") field is set. 



### #versions
    
    
    def versions() -> ::Array<::Google::Cloud::SecretManager::V1beta2::SecretVersion>

**Returns**

  * (::Array<[::Google::Cloud::SecretManager::V1beta2::SecretVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-SecretVersion)>) — The list of [SecretVersions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-SecretVersion "Google::Cloud::SecretManager::V1beta2::SecretVersion \(class\)") sorted in reverse by create_time (newest first). 



### #versions=
    
    
    def versions=(value) -> ::Array<::Google::Cloud::SecretManager::V1beta2::SecretVersion>

**Parameter**

  * **value** (::Array<[::Google::Cloud::SecretManager::V1beta2::SecretVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-SecretVersion)>) — The list of [SecretVersions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-SecretVersion "Google::Cloud::SecretManager::V1beta2::SecretVersion \(class\)") sorted in reverse by create_time (newest first). 



**Returns**

  * (::Array<[::Google::Cloud::SecretManager::V1beta2::SecretVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-SecretVersion)>) — The list of [SecretVersions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager-V1beta2-SecretVersion "Google::Cloud::SecretManager::V1beta2::SecretVersion \(class\)") sorted in reverse by create_time (newest first). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
