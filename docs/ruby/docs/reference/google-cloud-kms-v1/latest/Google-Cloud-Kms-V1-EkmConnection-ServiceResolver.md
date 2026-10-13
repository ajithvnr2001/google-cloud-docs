---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-EkmConnection-ServiceResolver/
title: Cloud Key Management Service (KMS) V1 API - Class Google::Cloud::Kms::V1::EkmConnection::ServiceResolver (v1.16.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:01:56.660353+00:00
---

# Cloud Key Management Service (KMS) V1 API - Class Google::Cloud::Kms::V1::EkmConnection::ServiceResolver (v1.16.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-EkmConnection-ServiceResolver/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Key Management Service (KMS) V1 API - Class Google::Cloud::Kms::V1::EkmConnection::ServiceResolver (v1.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.16.0 (latest)  1.15.2  1.14.0  1.13.0  1.12.1  1.11.0  1.10.0  1.9.2  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.2  1.2.1  1.1.0  1.0.2  0.27.0  0.26.0  0.25.1  0.24.3  0.23.0  0.22.1  0.21.0  0.20.0  0.19.0  0.18.1  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.2 

Reference documentation and code samples for the Cloud Key Management Service (KMS) V1 API class Google::Cloud::Kms::V1::EkmConnection::ServiceResolver.

A [ServiceResolver](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-EkmConnection-ServiceResolver "Google::Cloud::Kms::V1::EkmConnection::ServiceResolver \(class\)") represents an EKM replica that can be reached within an [EkmConnection](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-EkmConnection "Google::Cloud::Kms::V1::EkmConnection \(class\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #endpoint_filter
    
    
    def endpoint_filter() -> ::String

**Returns**

  * (::String) — Optional. The filter applied to the endpoints of the resolved service. If no filter is specified, all endpoints will be considered. An endpoint will be chosen arbitrarily from the filtered list for each request.

For endpoint filter syntax and examples, see https://cloud.google.com/service-directory/docs/reference/rpc/google.cloud.servicedirectory.v1#resolveservicerequest. 




### #endpoint_filter=
    
    
    def endpoint_filter=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The filter applied to the endpoints of the resolved service. If no filter is specified, all endpoints will be considered. An endpoint will be chosen arbitrarily from the filtered list for each request.

For endpoint filter syntax and examples, see https://cloud.google.com/service-directory/docs/reference/rpc/google.cloud.servicedirectory.v1#resolveservicerequest. 




**Returns**

  * (::String) — Optional. The filter applied to the endpoints of the resolved service. If no filter is specified, all endpoints will be considered. An endpoint will be chosen arbitrarily from the filtered list for each request.

For endpoint filter syntax and examples, see https://cloud.google.com/service-directory/docs/reference/rpc/google.cloud.servicedirectory.v1#resolveservicerequest. 




### #hostname
    
    
    def hostname() -> ::String

**Returns**

  * (::String) — Required. The hostname of the EKM replica used at TLS and HTTP layers. 



### #hostname=
    
    
    def hostname=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The hostname of the EKM replica used at TLS and HTTP layers. 



**Returns**

  * (::String) — Required. The hostname of the EKM replica used at TLS and HTTP layers. 



### #server_certificates
    
    
    def server_certificates() -> ::Array<::Google::Cloud::Kms::V1::Certificate>

**Returns**

  * (::Array<[::Google::Cloud::Kms::V1::Certificate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-Certificate)>) — Required. A list of leaf server certificates used to authenticate HTTPS connections to the EKM replica. Currently, a maximum of 10 [Certificate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-Certificate "Google::Cloud::Kms::V1::Certificate \(class\)") is supported. 



### #server_certificates=
    
    
    def server_certificates=(value) -> ::Array<::Google::Cloud::Kms::V1::Certificate>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Kms::V1::Certificate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-Certificate)>) — Required. A list of leaf server certificates used to authenticate HTTPS connections to the EKM replica. Currently, a maximum of 10 [Certificate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-Certificate "Google::Cloud::Kms::V1::Certificate \(class\)") is supported. 



**Returns**

  * (::Array<[::Google::Cloud::Kms::V1::Certificate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-Certificate)>) — Required. A list of leaf server certificates used to authenticate HTTPS connections to the EKM replica. Currently, a maximum of 10 [Certificate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-Certificate "Google::Cloud::Kms::V1::Certificate \(class\)") is supported. 



### #service_directory_service
    
    
    def service_directory_service() -> ::String

**Returns**

  * (::String) — Required. The resource name of the Service Directory service pointing to an EKM replica, in the format `projects/*/locations/*/namespaces/*/services/*`. 



### #service_directory_service=
    
    
    def service_directory_service=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The resource name of the Service Directory service pointing to an EKM replica, in the format `projects/*/locations/*/namespaces/*/services/*`. 



**Returns**

  * (::String) — Required. The resource name of the Service Directory service pointing to an EKM replica, in the format `projects/*/locations/*/namespaces/*/services/*`. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
