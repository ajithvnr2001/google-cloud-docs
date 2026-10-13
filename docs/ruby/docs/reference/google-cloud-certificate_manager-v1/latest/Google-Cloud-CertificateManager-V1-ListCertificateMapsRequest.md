---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-certificate_manager-v1/latest/Google-Cloud-CertificateManager-V1-ListCertificateMapsRequest/
title: Certificate Manager V1 API - Class Google::Cloud::CertificateManager::V1::ListCertificateMapsRequest (v1.5.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:52:11.921379+00:00
---

# Certificate Manager V1 API - Class Google::Cloud::CertificateManager::V1::ListCertificateMapsRequest (v1.5.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-certificate_manager-v1/latest/Google-Cloud-CertificateManager-V1-ListCertificateMapsRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Certificate Manager V1 API - Class Google::Cloud::CertificateManager::V1::ListCertificateMapsRequest (v1.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.5.1 (latest)  1.5.0  1.4.0  1.3.1  1.2.0  1.1.0  1.0.1  0.12.0  0.11.0  0.10.1  0.9.0  0.8.2  0.7.0  0.6.0  0.5.0  0.4.2  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Certificate Manager V1 API class Google::Cloud::CertificateManager::V1::ListCertificateMapsRequest.

Request for the `ListCertificateMaps` method.

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

  * (::String) — Filter expression to restrict the Certificates Maps returned. 



### #filter=
    
    
    def filter=(value) -> ::String

**Parameter**

  * **value** (::String) — Filter expression to restrict the Certificates Maps returned. 



**Returns**

  * (::String) — Filter expression to restrict the Certificates Maps returned. 



### #order_by
    
    
    def order_by() -> ::String

**Returns**

  * (::String) — A list of Certificate Map field names used to specify the order of the returned results. The default sorting order is ascending. To specify descending order for a field, add a suffix `" desc"`. 



### #order_by=
    
    
    def order_by=(value) -> ::String

**Parameter**

  * **value** (::String) — A list of Certificate Map field names used to specify the order of the returned results. The default sorting order is ascending. To specify descending order for a field, add a suffix `" desc"`. 



**Returns**

  * (::String) — A list of Certificate Map field names used to specify the order of the returned results. The default sorting order is ascending. To specify descending order for a field, add a suffix `" desc"`. 



### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — Maximum number of certificate maps to return per call. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Maximum number of certificate maps to return per call. 



**Returns**

  * (::Integer) — Maximum number of certificate maps to return per call. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — The value returned by the last `ListCertificateMapsResponse`. Indicates that this is a continuation of a prior `ListCertificateMaps` call, and that the system should return the next page of data. 



### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — The value returned by the last `ListCertificateMapsResponse`. Indicates that this is a continuation of a prior `ListCertificateMaps` call, and that the system should return the next page of data. 



**Returns**

  * (::String) — The value returned by the last `ListCertificateMapsResponse`. Indicates that this is a continuation of a prior `ListCertificateMaps` call, and that the system should return the next page of data. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The project and location from which the certificate maps should be listed, specified in the format `projects/*/locations/*`. 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The project and location from which the certificate maps should be listed, specified in the format `projects/*/locations/*`. 



**Returns**

  * (::String) — Required. The project and location from which the certificate maps should be listed, specified in the format `projects/*/locations/*`. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
