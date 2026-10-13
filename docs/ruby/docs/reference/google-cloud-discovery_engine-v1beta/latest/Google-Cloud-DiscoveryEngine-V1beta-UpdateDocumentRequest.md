---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-UpdateDocumentRequest/
title: Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::UpdateDocumentRequest (v0.30.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:51:08.541551+00:00
---

# Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::UpdateDocumentRequest (v0.30.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-UpdateDocumentRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::UpdateDocumentRequest (v0.30.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.30.0 (latest)  0.29.0  0.28.1  0.27.0  0.26.0  0.25.0  0.24.0  0.23.1  0.22.0  0.21.0  0.20.1  0.19.1  0.18.0  0.17.0  0.16.0  0.15.0  0.14.2  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.2  0.6.0  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Discovery Engine V1BETA API class Google::Cloud::DiscoveryEngine::V1beta::UpdateDocumentRequest.

Request message for [DocumentService.UpdateDocument](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-DocumentService-Client#Google__Cloud__DiscoveryEngine__V1beta__DocumentService__Client_update_document_instance_ "Google::Cloud::DiscoveryEngine::V1beta::DocumentService::Client#update_document \(method\)") method.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #allow_missing
    
    
    def allow_missing() -> ::Boolean

**Returns**

  * (::Boolean) — If set to `true` and the [Document](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Document "Google::Cloud::DiscoveryEngine::V1beta::Document \(class\)") is not found, a new [Document](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Document "Google::Cloud::DiscoveryEngine::V1beta::Document \(class\)") is be created. 



### #allow_missing=
    
    
    def allow_missing=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — If set to `true` and the [Document](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Document "Google::Cloud::DiscoveryEngine::V1beta::Document \(class\)") is not found, a new [Document](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Document "Google::Cloud::DiscoveryEngine::V1beta::Document \(class\)") is be created. 



**Returns**

  * (::Boolean) — If set to `true` and the [Document](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Document "Google::Cloud::DiscoveryEngine::V1beta::Document \(class\)") is not found, a new [Document](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Document "Google::Cloud::DiscoveryEngine::V1beta::Document \(class\)") is be created. 



### #document
    
    
    def document() -> ::Google::Cloud::DiscoveryEngine::V1beta::Document

**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::Document](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Document)) — Required. The document to update/create.

If the caller does not have permission to update the [Document](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Document "Google::Cloud::DiscoveryEngine::V1beta::Document \(class\)"), regardless of whether or not it exists, a `PERMISSION_DENIED` error is returned.

If the [Document](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Document "Google::Cloud::DiscoveryEngine::V1beta::Document \(class\)") to update does not exist and [allow_missing](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-UpdateDocumentRequest#Google__Cloud__DiscoveryEngine__V1beta__UpdateDocumentRequest_allow_missing_instance_ "Google::Cloud::DiscoveryEngine::V1beta::UpdateDocumentRequest#allow_missing \(method\)") is not set, a `NOT_FOUND` error is returned. 




### #document=
    
    
    def document=(value) -> ::Google::Cloud::DiscoveryEngine::V1beta::Document

**Parameter**

  * **value** ([::Google::Cloud::DiscoveryEngine::V1beta::Document](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Document)) — Required. The document to update/create.

If the caller does not have permission to update the [Document](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Document "Google::Cloud::DiscoveryEngine::V1beta::Document \(class\)"), regardless of whether or not it exists, a `PERMISSION_DENIED` error is returned.

If the [Document](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Document "Google::Cloud::DiscoveryEngine::V1beta::Document \(class\)") to update does not exist and [allow_missing](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-UpdateDocumentRequest#Google__Cloud__DiscoveryEngine__V1beta__UpdateDocumentRequest_allow_missing_instance_ "Google::Cloud::DiscoveryEngine::V1beta::UpdateDocumentRequest#allow_missing \(method\)") is not set, a `NOT_FOUND` error is returned. 




**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::Document](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Document)) — Required. The document to update/create.

If the caller does not have permission to update the [Document](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Document "Google::Cloud::DiscoveryEngine::V1beta::Document \(class\)"), regardless of whether or not it exists, a `PERMISSION_DENIED` error is returned.

If the [Document](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Document "Google::Cloud::DiscoveryEngine::V1beta::Document \(class\)") to update does not exist and [allow_missing](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-UpdateDocumentRequest#Google__Cloud__DiscoveryEngine__V1beta__UpdateDocumentRequest_allow_missing_instance_ "Google::Cloud::DiscoveryEngine::V1beta::UpdateDocumentRequest#allow_missing \(method\)") is not set, a `NOT_FOUND` error is returned. 




### #update_mask
    
    
    def update_mask() -> ::Google::Protobuf::FieldMask

**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Protobuf-FieldMask)) — Indicates which fields in the provided imported 'document' to update. If not set, by default updates all fields. 



### #update_mask=
    
    
    def update_mask=(value) -> ::Google::Protobuf::FieldMask

**Parameter**

  * **value** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Protobuf-FieldMask)) — Indicates which fields in the provided imported 'document' to update. If not set, by default updates all fields. 



**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Protobuf-FieldMask)) — Indicates which fields in the provided imported 'document' to update. If not set, by default updates all fields. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
