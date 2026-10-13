---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-ListDocumentsRequest/
title: Discovery Engine V1 API - Class Google::Cloud::DiscoveryEngine::V1::ListDocumentsRequest (v2.12.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:02:09.756691+00:00
---

# Discovery Engine V1 API - Class Google::Cloud::DiscoveryEngine::V1::ListDocumentsRequest (v2.12.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-ListDocumentsRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Discovery Engine V1 API - Class Google::Cloud::DiscoveryEngine::V1::ListDocumentsRequest (v2.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.12.0 (latest)  2.11.1  2.10.1  2.9.0  2.8.0  2.7.0  2.6.2  2.5.0  2.4.0  2.3.1  2.2.0  2.1.1  2.0.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.2  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.2  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Discovery Engine V1 API class Google::Cloud::DiscoveryEngine::V1::ListDocumentsRequest.

Request message for [DocumentService.ListDocuments](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-DocumentService-Client#Google__Cloud__DiscoveryEngine__V1__DocumentService__Client_list_documents_instance_ "Google::Cloud::DiscoveryEngine::V1::DocumentService::Client#list_documents \(method\)") method.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — Maximum number of [Document](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Document "Google::Cloud::DiscoveryEngine::V1::Document \(class\)")s to return. If unspecified, defaults to 100. The maximum allowed value is 1000. Values above 1000 are set to 1000.

If this field is negative, an `INVALID_ARGUMENT` error is returned. 




### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Maximum number of [Document](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Document "Google::Cloud::DiscoveryEngine::V1::Document \(class\)")s to return. If unspecified, defaults to 100. The maximum allowed value is 1000. Values above 1000 are set to 1000.

If this field is negative, an `INVALID_ARGUMENT` error is returned. 




**Returns**

  * (::Integer) — Maximum number of [Document](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Document "Google::Cloud::DiscoveryEngine::V1::Document \(class\)")s to return. If unspecified, defaults to 100. The maximum allowed value is 1000. Values above 1000 are set to 1000.

If this field is negative, an `INVALID_ARGUMENT` error is returned. 




### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — A page token [ListDocumentsResponse.next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-ListDocumentsResponse#Google__Cloud__DiscoveryEngine__V1__ListDocumentsResponse_next_page_token_instance_ "Google::Cloud::DiscoveryEngine::V1::ListDocumentsResponse#next_page_token \(method\)"), received from a previous [DocumentService.ListDocuments](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-DocumentService-Client#Google__Cloud__DiscoveryEngine__V1__DocumentService__Client_list_documents_instance_ "Google::Cloud::DiscoveryEngine::V1::DocumentService::Client#list_documents \(method\)") call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to [DocumentService.ListDocuments](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-DocumentService-Client#Google__Cloud__DiscoveryEngine__V1__DocumentService__Client_list_documents_instance_ "Google::Cloud::DiscoveryEngine::V1::DocumentService::Client#list_documents \(method\)") must match the call that provided the page token. Otherwise, an `INVALID_ARGUMENT` error is returned. 




### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — A page token [ListDocumentsResponse.next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-ListDocumentsResponse#Google__Cloud__DiscoveryEngine__V1__ListDocumentsResponse_next_page_token_instance_ "Google::Cloud::DiscoveryEngine::V1::ListDocumentsResponse#next_page_token \(method\)"), received from a previous [DocumentService.ListDocuments](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-DocumentService-Client#Google__Cloud__DiscoveryEngine__V1__DocumentService__Client_list_documents_instance_ "Google::Cloud::DiscoveryEngine::V1::DocumentService::Client#list_documents \(method\)") call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to [DocumentService.ListDocuments](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-DocumentService-Client#Google__Cloud__DiscoveryEngine__V1__DocumentService__Client_list_documents_instance_ "Google::Cloud::DiscoveryEngine::V1::DocumentService::Client#list_documents \(method\)") must match the call that provided the page token. Otherwise, an `INVALID_ARGUMENT` error is returned. 




**Returns**

  * (::String) — A page token [ListDocumentsResponse.next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-ListDocumentsResponse#Google__Cloud__DiscoveryEngine__V1__ListDocumentsResponse_next_page_token_instance_ "Google::Cloud::DiscoveryEngine::V1::ListDocumentsResponse#next_page_token \(method\)"), received from a previous [DocumentService.ListDocuments](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-DocumentService-Client#Google__Cloud__DiscoveryEngine__V1__DocumentService__Client_list_documents_instance_ "Google::Cloud::DiscoveryEngine::V1::DocumentService::Client#list_documents \(method\)") call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to [DocumentService.ListDocuments](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-DocumentService-Client#Google__Cloud__DiscoveryEngine__V1__DocumentService__Client_list_documents_instance_ "Google::Cloud::DiscoveryEngine::V1::DocumentService::Client#list_documents \(method\)") must match the call that provided the page token. Otherwise, an `INVALID_ARGUMENT` error is returned. 




### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The parent branch resource name, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}`. Use `default_branch` as the branch ID, to list documents under the default branch.

If the caller does not have permission to list [Document](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Document "Google::Cloud::DiscoveryEngine::V1::Document \(class\)")s under this branch, regardless of whether or not this branch exists, a `PERMISSION_DENIED` error is returned. 




### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The parent branch resource name, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}`. Use `default_branch` as the branch ID, to list documents under the default branch.

If the caller does not have permission to list [Document](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Document "Google::Cloud::DiscoveryEngine::V1::Document \(class\)")s under this branch, regardless of whether or not this branch exists, a `PERMISSION_DENIED` error is returned. 




**Returns**

  * (::String) — Required. The parent branch resource name, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}`. Use `default_branch` as the branch ID, to list documents under the default branch.

If the caller does not have permission to list [Document](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Document "Google::Cloud::DiscoveryEngine::V1::Document \(class\)")s under this branch, regardless of whether or not this branch exists, a `PERMISSION_DENIED` error is returned. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
