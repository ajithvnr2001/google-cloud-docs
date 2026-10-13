---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-ListCertificateAuthoritiesRequest/
title: Certificate Authority Service V1beta1 API - Class Google::Cloud::Security::PrivateCA::V1beta1::ListCertificateAuthoritiesRequest (v0.18.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:52:59.567054+00:00
---

# Certificate Authority Service V1beta1 API - Class Google::Cloud::Security::PrivateCA::V1beta1::ListCertificateAuthoritiesRequest (v0.18.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-ListCertificateAuthoritiesRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Certificate Authority Service V1beta1 API - Class Google::Cloud::Security::PrivateCA::V1beta1::ListCertificateAuthoritiesRequest (v0.18.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.18.1 (latest)  0.18.0  0.17.1  0.16.0  0.15.1  0.14.0  0.13.0  0.12.1  0.11.0  0.10.0  0.9.1  0.8.2  0.7.0  0.6.1  0.5.0  0.4.0  0.3.6 

Reference documentation and code samples for the Certificate Authority Service V1beta1 API class Google::Cloud::Security::PrivateCA::V1beta1::ListCertificateAuthoritiesRequest.

Request message for [CertificateAuthorityService.ListCertificateAuthorities](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthorityService-Client#Google__Cloud__Security__PrivateCA__V1beta1__CertificateAuthorityService__Client_list_certificate_authorities_instance_ "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthorityService::Client#list_certificate_authorities \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #filter
    
    
    def filter() -> ::String

**Returns**

  * (::String) — Optional. Only include resources that match the filter in the response. 



### #filter=
    
    
    def filter=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Only include resources that match the filter in the response. 



**Returns**

  * (::String) — Optional. Only include resources that match the filter in the response. 



### #order_by
    
    
    def order_by() -> ::String

**Returns**

  * (::String) — Optional. Specify how the results should be sorted. 



### #order_by=
    
    
    def order_by=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Specify how the results should be sorted. 



**Returns**

  * (::String) — Optional. Specify how the results should be sorted. 



### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — Optional. Limit on the number of [CertificateAuthorities](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthority "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority \(class\)") to include in the response. Further [CertificateAuthorities](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthority "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority \(class\)") can subsequently be obtained by including the [ListCertificateAuthoritiesResponse.next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-ListCertificateAuthoritiesResponse#Google__Cloud__Security__PrivateCA__V1beta1__ListCertificateAuthoritiesResponse_next_page_token_instance_ "Google::Cloud::Security::PrivateCA::V1beta1::ListCertificateAuthoritiesResponse#next_page_token \(method\)") in a subsequent request. If unspecified, the server will pick an appropriate default. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Limit on the number of [CertificateAuthorities](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthority "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority \(class\)") to include in the response. Further [CertificateAuthorities](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthority "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority \(class\)") can subsequently be obtained by including the [ListCertificateAuthoritiesResponse.next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-ListCertificateAuthoritiesResponse#Google__Cloud__Security__PrivateCA__V1beta1__ListCertificateAuthoritiesResponse_next_page_token_instance_ "Google::Cloud::Security::PrivateCA::V1beta1::ListCertificateAuthoritiesResponse#next_page_token \(method\)") in a subsequent request. If unspecified, the server will pick an appropriate default. 



**Returns**

  * (::Integer) — Optional. Limit on the number of [CertificateAuthorities](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthority "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority \(class\)") to include in the response. Further [CertificateAuthorities](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthority "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority \(class\)") can subsequently be obtained by including the [ListCertificateAuthoritiesResponse.next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-ListCertificateAuthoritiesResponse#Google__Cloud__Security__PrivateCA__V1beta1__ListCertificateAuthoritiesResponse_next_page_token_instance_ "Google::Cloud::Security::PrivateCA::V1beta1::ListCertificateAuthoritiesResponse#next_page_token \(method\)") in a subsequent request. If unspecified, the server will pick an appropriate default. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — Optional. Pagination token, returned earlier via [ListCertificateAuthoritiesResponse.next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-ListCertificateAuthoritiesResponse#Google__Cloud__Security__PrivateCA__V1beta1__ListCertificateAuthoritiesResponse_next_page_token_instance_ "Google::Cloud::Security::PrivateCA::V1beta1::ListCertificateAuthoritiesResponse#next_page_token \(method\)"). 



### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Pagination token, returned earlier via [ListCertificateAuthoritiesResponse.next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-ListCertificateAuthoritiesResponse#Google__Cloud__Security__PrivateCA__V1beta1__ListCertificateAuthoritiesResponse_next_page_token_instance_ "Google::Cloud::Security::PrivateCA::V1beta1::ListCertificateAuthoritiesResponse#next_page_token \(method\)"). 



**Returns**

  * (::String) — Optional. Pagination token, returned earlier via [ListCertificateAuthoritiesResponse.next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-ListCertificateAuthoritiesResponse#Google__Cloud__Security__PrivateCA__V1beta1__ListCertificateAuthoritiesResponse_next_page_token_instance_ "Google::Cloud::Security::PrivateCA::V1beta1::ListCertificateAuthoritiesResponse#next_page_token \(method\)"). 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The resource name of the location associated with the [CertificateAuthorities](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthority "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority \(class\)"), in the format `projects/*/locations/*`. 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The resource name of the location associated with the [CertificateAuthorities](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthority "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority \(class\)"), in the format `projects/*/locations/*`. 



**Returns**

  * (::String) — Required. The resource name of the location associated with the [CertificateAuthorities](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthority "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority \(class\)"), in the format `projects/*/locations/*`. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
