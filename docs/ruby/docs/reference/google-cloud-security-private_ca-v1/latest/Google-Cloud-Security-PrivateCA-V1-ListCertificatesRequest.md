---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-ListCertificatesRequest/
title: Certificate Authority Service V1 API - Class Google::Cloud::Security::PrivateCA::V1::ListCertificatesRequest (v2.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:26:28.443924+00:00
---

# Certificate Authority Service V1 API - Class Google::Cloud::Security::PrivateCA::V1::ListCertificatesRequest (v2.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-ListCertificatesRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Certificate Authority Service V1 API - Class Google::Cloud::Security::PrivateCA::V1::ListCertificatesRequest (v2.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.8.1 (latest)  2.8.0  2.7.0  2.6.1  2.5.0  2.4.1  2.3.0  2.2.0  2.1.0  2.0.1  1.2.0  1.1.0  1.0.1  0.13.0  0.12.0  0.11.0  0.10.2  0.9.0  0.8.1  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.1  0.1.6 

Reference documentation and code samples for the Certificate Authority Service V1 API class Google::Cloud::Security::PrivateCA::V1::ListCertificatesRequest.

Request message for [CertificateAuthorityService.ListCertificates](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-CertificateAuthorityService-Client#Google__Cloud__Security__PrivateCA__V1__CertificateAuthorityService__Client_list_certificates_instance_ "Google::Cloud::Security::PrivateCA::V1::CertificateAuthorityService::Client#list_certificates \(method\)").

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

  * (::String) — Optional. Only include resources that match the filter in the response. For details on supported filters and syntax, see [Certificates Filtering documentation](https://cloud.google.com/certificate-authority-service/docs/sorting-filtering-certificates#filtering_support). 



### #filter=
    
    
    def filter=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Only include resources that match the filter in the response. For details on supported filters and syntax, see [Certificates Filtering documentation](https://cloud.google.com/certificate-authority-service/docs/sorting-filtering-certificates#filtering_support). 



**Returns**

  * (::String) — Optional. Only include resources that match the filter in the response. For details on supported filters and syntax, see [Certificates Filtering documentation](https://cloud.google.com/certificate-authority-service/docs/sorting-filtering-certificates#filtering_support). 



### #order_by
    
    
    def order_by() -> ::String

**Returns**

  * (::String) — Optional. Specify how the results should be sorted. For details on supported fields and syntax, see [Certificates Sorting documentation](https://cloud.google.com/certificate-authority-service/docs/sorting-filtering-certificates#sorting_support). 



### #order_by=
    
    
    def order_by=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Specify how the results should be sorted. For details on supported fields and syntax, see [Certificates Sorting documentation](https://cloud.google.com/certificate-authority-service/docs/sorting-filtering-certificates#sorting_support). 



**Returns**

  * (::String) — Optional. Specify how the results should be sorted. For details on supported fields and syntax, see [Certificates Sorting documentation](https://cloud.google.com/certificate-authority-service/docs/sorting-filtering-certificates#sorting_support). 



### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — Optional. Limit on the number of [Certificates](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-Certificate "Google::Cloud::Security::PrivateCA::V1::Certificate \(class\)") to include in the response. Further [Certificates](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-Certificate "Google::Cloud::Security::PrivateCA::V1::Certificate \(class\)") can subsequently be obtained by including the [ListCertificatesResponse.next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-ListCertificatesResponse#Google__Cloud__Security__PrivateCA__V1__ListCertificatesResponse_next_page_token_instance_ "Google::Cloud::Security::PrivateCA::V1::ListCertificatesResponse#next_page_token \(method\)") in a subsequent request. If unspecified, the server will pick an appropriate default. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Limit on the number of [Certificates](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-Certificate "Google::Cloud::Security::PrivateCA::V1::Certificate \(class\)") to include in the response. Further [Certificates](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-Certificate "Google::Cloud::Security::PrivateCA::V1::Certificate \(class\)") can subsequently be obtained by including the [ListCertificatesResponse.next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-ListCertificatesResponse#Google__Cloud__Security__PrivateCA__V1__ListCertificatesResponse_next_page_token_instance_ "Google::Cloud::Security::PrivateCA::V1::ListCertificatesResponse#next_page_token \(method\)") in a subsequent request. If unspecified, the server will pick an appropriate default. 



**Returns**

  * (::Integer) — Optional. Limit on the number of [Certificates](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-Certificate "Google::Cloud::Security::PrivateCA::V1::Certificate \(class\)") to include in the response. Further [Certificates](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-Certificate "Google::Cloud::Security::PrivateCA::V1::Certificate \(class\)") can subsequently be obtained by including the [ListCertificatesResponse.next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-ListCertificatesResponse#Google__Cloud__Security__PrivateCA__V1__ListCertificatesResponse_next_page_token_instance_ "Google::Cloud::Security::PrivateCA::V1::ListCertificatesResponse#next_page_token \(method\)") in a subsequent request. If unspecified, the server will pick an appropriate default. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — Optional. Pagination token, returned earlier via [ListCertificatesResponse.next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-ListCertificatesResponse#Google__Cloud__Security__PrivateCA__V1__ListCertificatesResponse_next_page_token_instance_ "Google::Cloud::Security::PrivateCA::V1::ListCertificatesResponse#next_page_token \(method\)"). 



### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Pagination token, returned earlier via [ListCertificatesResponse.next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-ListCertificatesResponse#Google__Cloud__Security__PrivateCA__V1__ListCertificatesResponse_next_page_token_instance_ "Google::Cloud::Security::PrivateCA::V1::ListCertificatesResponse#next_page_token \(method\)"). 



**Returns**

  * (::String) — Optional. Pagination token, returned earlier via [ListCertificatesResponse.next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-ListCertificatesResponse#Google__Cloud__Security__PrivateCA__V1__ListCertificatesResponse_next_page_token_instance_ "Google::Cloud::Security::PrivateCA::V1::ListCertificatesResponse#next_page_token \(method\)"). 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — 

Required. The resource name of the parent associated with the [Certificates](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-Certificate "Google::Cloud::Security::PrivateCA::V1::Certificate \(class\)"), in the format `projects/*/locations/*/caPools/*`. The parent resource name can be in one of two forms:

    1. **Specific CA Pool:** To list certificates within a single CA Pool: `projects/*/locations/*/caPools/*`

    2. **All CA Pools in a Location:** To list certificates across _all_ CA Pools in a given project and location, use the wildcard character (`-`) in place of the CA Pool ID. Example: `projects/*/locations/*/caPools/-`




### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Required. The resource name of the parent associated with the [Certificates](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-Certificate "Google::Cloud::Security::PrivateCA::V1::Certificate \(class\)"), in the format `projects/*/locations/*/caPools/*`. The parent resource name can be in one of two forms:

    1. **Specific CA Pool:** To list certificates within a single CA Pool: `projects/*/locations/*/caPools/*`

    2. **All CA Pools in a Location:** To list certificates across _all_ CA Pools in a given project and location, use the wildcard character (`-`) in place of the CA Pool ID. Example: `projects/*/locations/*/caPools/-`




**Returns**

  * (::String) — 

Required. The resource name of the parent associated with the [Certificates](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-Certificate "Google::Cloud::Security::PrivateCA::V1::Certificate \(class\)"), in the format `projects/*/locations/*/caPools/*`. The parent resource name can be in one of two forms:

    1. **Specific CA Pool:** To list certificates within a single CA Pool: `projects/*/locations/*/caPools/*`

    2. **All CA Pools in a Location:** To list certificates across _all_ CA Pools in a given project and location, use the wildcard character (`-`) in place of the CA Pool ID. Example: `projects/*/locations/*/caPools/-`




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
