---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-EnableCertificateAuthorityRequest/
title: Certificate Authority Service V1beta1 API - Class Google::Cloud::Security::PrivateCA::V1beta1::EnableCertificateAuthorityRequest (v0.18.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:10:05.428908+00:00
---

# Certificate Authority Service V1beta1 API - Class Google::Cloud::Security::PrivateCA::V1beta1::EnableCertificateAuthorityRequest (v0.18.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-EnableCertificateAuthorityRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Certificate Authority Service V1beta1 API - Class Google::Cloud::Security::PrivateCA::V1beta1::EnableCertificateAuthorityRequest (v0.18.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.18.1 (latest)  0.18.0  0.17.1  0.16.0  0.15.1  0.14.0  0.13.0  0.12.1  0.11.0  0.10.0  0.9.1  0.8.2  0.7.0  0.6.1  0.5.0  0.4.0  0.3.6 

Reference documentation and code samples for the Certificate Authority Service V1beta1 API class Google::Cloud::Security::PrivateCA::V1beta1::EnableCertificateAuthorityRequest.

Request message for [CertificateAuthorityService.EnableCertificateAuthority](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthorityService-Client#Google__Cloud__Security__PrivateCA__V1beta1__CertificateAuthorityService__Client_enable_certificate_authority_instance_ "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthorityService::Client#enable_certificate_authority \(method\)").

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

  * (::String) — Required. The resource name for this [CertificateAuthority](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthority "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority \(class\)") in the format `projects/*/locations/*/certificateAuthorities/*`. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The resource name for this [CertificateAuthority](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthority "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority \(class\)") in the format `projects/*/locations/*/certificateAuthorities/*`. 



**Returns**

  * (::String) — Required. The resource name for this [CertificateAuthority](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthority "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority \(class\)") in the format `projects/*/locations/*/certificateAuthorities/*`. 



### #request_id
    
    
    def request_id() -> ::String

**Returns**

  * (::String) — Optional. An ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and t he request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




### #request_id=
    
    
    def request_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. An ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and t he request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




**Returns**

  * (::String) — Optional. An ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and t he request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
