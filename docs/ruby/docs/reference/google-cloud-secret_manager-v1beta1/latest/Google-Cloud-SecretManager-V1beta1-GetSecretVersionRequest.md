---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta1/latest/Google-Cloud-SecretManager-V1beta1-GetSecretVersionRequest/
title: Secret Manager V1beta1 API - Class Google::Cloud::SecretManager::V1beta1::GetSecretVersionRequest (v0.22.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:01:12.775183+00:00
---

# Secret Manager V1beta1 API - Class Google::Cloud::SecretManager::V1beta1::GetSecretVersionRequest (v0.22.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta1/latest/Google-Cloud-SecretManager-V1beta1-GetSecretVersionRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Secret Manager V1beta1 API - Class Google::Cloud::SecretManager::V1beta1::GetSecretVersionRequest (v0.22.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.22.1 (latest)  0.22.0  0.21.0  0.20.0  0.19.1  0.18.0  0.17.2  0.16.0  0.15.1  0.14.2  0.13.0  0.12.2  0.11.0  0.10.0  0.9.0  0.8.5 

Reference documentation and code samples for the Secret Manager V1beta1 API class Google::Cloud::SecretManager::V1beta1::GetSecretVersionRequest.

Request message for [SecretManagerService.GetSecretVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta1/latest/Google-Cloud-SecretManager-V1beta1-SecretManagerService-Client#Google__Cloud__SecretManager__V1beta1__SecretManagerService__Client_get_secret_version_instance_ "Google::Cloud::SecretManager::V1beta1::SecretManagerService::Client#get_secret_version \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Required. The resource name of the [SecretVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta1/latest/Google-Cloud-SecretManager-V1beta1-SecretVersion "Google::Cloud::SecretManager::V1beta1::SecretVersion \(class\)") in the format `projects/*/secrets/*/versions/*`. `projects/*/secrets/*/versions/latest` is an alias to the `latest` [SecretVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta1/latest/Google-Cloud-SecretManager-V1beta1-SecretVersion "Google::Cloud::SecretManager::V1beta1::SecretVersion \(class\)"). 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The resource name of the [SecretVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta1/latest/Google-Cloud-SecretManager-V1beta1-SecretVersion "Google::Cloud::SecretManager::V1beta1::SecretVersion \(class\)") in the format `projects/*/secrets/*/versions/*`. `projects/*/secrets/*/versions/latest` is an alias to the `latest` [SecretVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta1/latest/Google-Cloud-SecretManager-V1beta1-SecretVersion "Google::Cloud::SecretManager::V1beta1::SecretVersion \(class\)"). 



**Returns**

  * (::String) — Required. The resource name of the [SecretVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta1/latest/Google-Cloud-SecretManager-V1beta1-SecretVersion "Google::Cloud::SecretManager::V1beta1::SecretVersion \(class\)") in the format `projects/*/secrets/*/versions/*`. `projects/*/secrets/*/versions/latest` is an alias to the `latest` [SecretVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta1/latest/Google-Cloud-SecretManager-V1beta1-SecretVersion "Google::Cloud::SecretManager::V1beta1::SecretVersion \(class\)"). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
