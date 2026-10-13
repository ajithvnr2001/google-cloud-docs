---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-UpdateCompletionConfigRequest/
title: Retail V2 API - Class Google::Cloud::Retail::V2::UpdateCompletionConfigRequest (v2.10.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:23:12.565829+00:00
---

# Retail V2 API - Class Google::Cloud::Retail::V2::UpdateCompletionConfigRequest (v2.10.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-UpdateCompletionConfigRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Retail V2 API - Class Google::Cloud::Retail::V2::UpdateCompletionConfigRequest (v2.10.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.10.0 (latest)  2.9.0  2.8.1  2.7.0  2.6.1  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.3.0  1.2.0  1.1.0  1.0.1  0.21.0  0.20.0  0.19.0  0.18.2  0.17.0  0.16.1  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.4 

Reference documentation and code samples for the Retail V2 API class Google::Cloud::Retail::V2::UpdateCompletionConfigRequest.

Request for [CatalogService.UpdateCompletionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-CatalogService-Client#Google__Cloud__Retail__V2__CatalogService__Client_update_completion_config_instance_ "Google::Cloud::Retail::V2::CatalogService::Client#update_completion_config \(method\)") method.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #completion_config
    
    
    def completion_config() -> ::Google::Cloud::Retail::V2::CompletionConfig

**Returns**

  * ([::Google::Cloud::Retail::V2::CompletionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-CompletionConfig)) — Required. The [CompletionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-CompletionConfig "Google::Cloud::Retail::V2::CompletionConfig \(class\)") to update.

If the caller does not have permission to update the [CompletionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-CompletionConfig "Google::Cloud::Retail::V2::CompletionConfig \(class\)"), then a PERMISSION_DENIED error is returned.

If the [CompletionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-CompletionConfig "Google::Cloud::Retail::V2::CompletionConfig \(class\)") to update does not exist, a NOT_FOUND error is returned. 




### #completion_config=
    
    
    def completion_config=(value) -> ::Google::Cloud::Retail::V2::CompletionConfig

**Parameter**

  * **value** ([::Google::Cloud::Retail::V2::CompletionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-CompletionConfig)) — Required. The [CompletionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-CompletionConfig "Google::Cloud::Retail::V2::CompletionConfig \(class\)") to update.

If the caller does not have permission to update the [CompletionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-CompletionConfig "Google::Cloud::Retail::V2::CompletionConfig \(class\)"), then a PERMISSION_DENIED error is returned.

If the [CompletionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-CompletionConfig "Google::Cloud::Retail::V2::CompletionConfig \(class\)") to update does not exist, a NOT_FOUND error is returned. 




**Returns**

  * ([::Google::Cloud::Retail::V2::CompletionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-CompletionConfig)) — Required. The [CompletionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-CompletionConfig "Google::Cloud::Retail::V2::CompletionConfig \(class\)") to update.

If the caller does not have permission to update the [CompletionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-CompletionConfig "Google::Cloud::Retail::V2::CompletionConfig \(class\)"), then a PERMISSION_DENIED error is returned.

If the [CompletionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-CompletionConfig "Google::Cloud::Retail::V2::CompletionConfig \(class\)") to update does not exist, a NOT_FOUND error is returned. 




### #update_mask
    
    
    def update_mask() -> ::Google::Protobuf::FieldMask

**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Protobuf-FieldMask)) — Indicates which fields in the provided [CompletionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-CompletionConfig "Google::Cloud::Retail::V2::CompletionConfig \(class\)") to update. The following are the only supported fields:

    * [CompletionConfig.matching_order](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-CompletionConfig#Google__Cloud__Retail__V2__CompletionConfig_matching_order_instance_ "Google::Cloud::Retail::V2::CompletionConfig#matching_order \(method\)")
    * [CompletionConfig.max_suggestions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-CompletionConfig#Google__Cloud__Retail__V2__CompletionConfig_max_suggestions_instance_ "Google::Cloud::Retail::V2::CompletionConfig#max_suggestions \(method\)")
    * [CompletionConfig.min_prefix_length](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-CompletionConfig#Google__Cloud__Retail__V2__CompletionConfig_min_prefix_length_instance_ "Google::Cloud::Retail::V2::CompletionConfig#min_prefix_length \(method\)")
    * [CompletionConfig.auto_learning](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-CompletionConfig#Google__Cloud__Retail__V2__CompletionConfig_auto_learning_instance_ "Google::Cloud::Retail::V2::CompletionConfig#auto_learning \(method\)")

If not set, all supported fields are updated. 




### #update_mask=
    
    
    def update_mask=(value) -> ::Google::Protobuf::FieldMask

**Parameter**

  * **value** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Protobuf-FieldMask)) — Indicates which fields in the provided [CompletionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-CompletionConfig "Google::Cloud::Retail::V2::CompletionConfig \(class\)") to update. The following are the only supported fields:

    * [CompletionConfig.matching_order](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-CompletionConfig#Google__Cloud__Retail__V2__CompletionConfig_matching_order_instance_ "Google::Cloud::Retail::V2::CompletionConfig#matching_order \(method\)")
    * [CompletionConfig.max_suggestions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-CompletionConfig#Google__Cloud__Retail__V2__CompletionConfig_max_suggestions_instance_ "Google::Cloud::Retail::V2::CompletionConfig#max_suggestions \(method\)")
    * [CompletionConfig.min_prefix_length](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-CompletionConfig#Google__Cloud__Retail__V2__CompletionConfig_min_prefix_length_instance_ "Google::Cloud::Retail::V2::CompletionConfig#min_prefix_length \(method\)")
    * [CompletionConfig.auto_learning](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-CompletionConfig#Google__Cloud__Retail__V2__CompletionConfig_auto_learning_instance_ "Google::Cloud::Retail::V2::CompletionConfig#auto_learning \(method\)")

If not set, all supported fields are updated. 




**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Protobuf-FieldMask)) — Indicates which fields in the provided [CompletionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-CompletionConfig "Google::Cloud::Retail::V2::CompletionConfig \(class\)") to update. The following are the only supported fields:

    * [CompletionConfig.matching_order](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-CompletionConfig#Google__Cloud__Retail__V2__CompletionConfig_matching_order_instance_ "Google::Cloud::Retail::V2::CompletionConfig#matching_order \(method\)")
    * [CompletionConfig.max_suggestions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-CompletionConfig#Google__Cloud__Retail__V2__CompletionConfig_max_suggestions_instance_ "Google::Cloud::Retail::V2::CompletionConfig#max_suggestions \(method\)")
    * [CompletionConfig.min_prefix_length](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-CompletionConfig#Google__Cloud__Retail__V2__CompletionConfig_min_prefix_length_instance_ "Google::Cloud::Retail::V2::CompletionConfig#min_prefix_length \(method\)")
    * [CompletionConfig.auto_learning](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-CompletionConfig#Google__Cloud__Retail__V2__CompletionConfig_auto_learning_instance_ "Google::Cloud::Retail::V2::CompletionConfig#auto_learning \(method\)")

If not set, all supported fields are updated. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
