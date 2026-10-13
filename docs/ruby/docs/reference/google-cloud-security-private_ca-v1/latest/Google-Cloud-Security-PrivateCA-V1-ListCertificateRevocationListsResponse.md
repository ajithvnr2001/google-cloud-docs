---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-ListCertificateRevocationListsResponse/
title: Certificate Authority Service V1 API - Class Google::Cloud::Security::PrivateCA::V1::ListCertificateRevocationListsResponse (v2.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:10:22.239969+00:00
---

# Certificate Authority Service V1 API - Class Google::Cloud::Security::PrivateCA::V1::ListCertificateRevocationListsResponse (v2.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-ListCertificateRevocationListsResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Certificate Authority Service V1 API - Class Google::Cloud::Security::PrivateCA::V1::ListCertificateRevocationListsResponse (v2.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.8.1 (latest)  2.8.0  2.7.0  2.6.1  2.5.0  2.4.1  2.3.0  2.2.0  2.1.0  2.0.1  1.2.0  1.1.0  1.0.1  0.13.0  0.12.0  0.11.0  0.10.2  0.9.0  0.8.1  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.1  0.1.6 

Reference documentation and code samples for the Certificate Authority Service V1 API class Google::Cloud::Security::PrivateCA::V1::ListCertificateRevocationListsResponse.

Response message for [CertificateAuthorityService.ListCertificateRevocationLists](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-CertificateAuthorityService-Client#Google__Cloud__Security__PrivateCA__V1__CertificateAuthorityService__Client_list_certificate_revocation_lists_instance_ "Google::Cloud::Security::PrivateCA::V1::CertificateAuthorityService::Client#list_certificate_revocation_lists \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #certificate_revocation_lists
    
    
    def certificate_revocation_lists() -> ::Array<::Google::Cloud::Security::PrivateCA::V1::CertificateRevocationList>

**Returns**

  * (::Array<[::Google::Cloud::Security::PrivateCA::V1::CertificateRevocationList](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-CertificateRevocationList)>) — The list of [CertificateRevocationLists](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-CertificateRevocationList "Google::Cloud::Security::PrivateCA::V1::CertificateRevocationList \(class\)"). 



### #certificate_revocation_lists=
    
    
    def certificate_revocation_lists=(value) -> ::Array<::Google::Cloud::Security::PrivateCA::V1::CertificateRevocationList>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Security::PrivateCA::V1::CertificateRevocationList](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-CertificateRevocationList)>) — The list of [CertificateRevocationLists](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-CertificateRevocationList "Google::Cloud::Security::PrivateCA::V1::CertificateRevocationList \(class\)"). 



**Returns**

  * (::Array<[::Google::Cloud::Security::PrivateCA::V1::CertificateRevocationList](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-CertificateRevocationList)>) — The list of [CertificateRevocationLists](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-CertificateRevocationList "Google::Cloud::Security::PrivateCA::V1::CertificateRevocationList \(class\)"). 



### #next_page_token
    
    
    def next_page_token() -> ::String

**Returns**

  * (::String) — A token to retrieve next page of results. Pass this value in [ListCertificateRevocationListsRequest.page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-ListCertificateRevocationListsRequest#Google__Cloud__Security__PrivateCA__V1__ListCertificateRevocationListsRequest_page_token_instance_ "Google::Cloud::Security::PrivateCA::V1::ListCertificateRevocationListsRequest#page_token \(method\)") to retrieve the next page of results. 



### #next_page_token=
    
    
    def next_page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — A token to retrieve next page of results. Pass this value in [ListCertificateRevocationListsRequest.page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-ListCertificateRevocationListsRequest#Google__Cloud__Security__PrivateCA__V1__ListCertificateRevocationListsRequest_page_token_instance_ "Google::Cloud::Security::PrivateCA::V1::ListCertificateRevocationListsRequest#page_token \(method\)") to retrieve the next page of results. 



**Returns**

  * (::String) — A token to retrieve next page of results. Pass this value in [ListCertificateRevocationListsRequest.page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-ListCertificateRevocationListsRequest#Google__Cloud__Security__PrivateCA__V1__ListCertificateRevocationListsRequest_page_token_instance_ "Google::Cloud::Security::PrivateCA::V1::ListCertificateRevocationListsRequest#page_token \(method\)") to retrieve the next page of results. 



### #unreachable
    
    
    def unreachable() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — A list of locations (e.g. "us-west1") that could not be reached. 



### #unreachable=
    
    
    def unreachable=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — A list of locations (e.g. "us-west1") that could not be reached. 



**Returns**

  * (::Array<::String>) — A list of locations (e.g. "us-west1") that could not be reached. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
