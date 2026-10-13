---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-Container/
title: Security Command Center V2 API - Class Google::Cloud::SecurityCenter::V2::Container (v1.9.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:30:10.735284+00:00
---

# Security Command Center V2 API - Class Google::Cloud::SecurityCenter::V2::Container (v1.9.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-Container/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Security Command Center V2 API - Class Google::Cloud::SecurityCenter::V2::Container (v1.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.9.1 (latest)  1.9.0  1.8.0  1.7.1  1.6.0  1.5.1  1.4.0  1.3.0  1.2.0  1.1.1  1.0.0  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Security Command Center V2 API class Google::Cloud::SecurityCenter::V2::Container.

Container associated with the finding.

## Inherits

  * [Object](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-Kubernetes-Object)



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Protobuf-Timestamp)) — The time that the container was created. 



### #create_time=
    
    
    def create_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Protobuf-Timestamp)) — The time that the container was created. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Protobuf-Timestamp)) — The time that the container was created. 



### #image_id
    
    
    def image_id() -> ::String

**Returns**

  * (::String) — Optional container image ID, if provided by the container runtime. Uniquely identifies the container image launched using a container image digest. 



### #image_id=
    
    
    def image_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional container image ID, if provided by the container runtime. Uniquely identifies the container image launched using a container image digest. 



**Returns**

  * (::String) — Optional container image ID, if provided by the container runtime. Uniquely identifies the container image launched using a container image digest. 



### #labels
    
    
    def labels() -> ::Array<::Google::Cloud::SecurityCenter::V2::Label>

**Returns**

  * (::Array<[::Google::Cloud::SecurityCenter::V2::Label](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-Label)>) — Container labels, as provided by the container runtime. 



### #labels=
    
    
    def labels=(value) -> ::Array<::Google::Cloud::SecurityCenter::V2::Label>

**Parameter**

  * **value** (::Array<[::Google::Cloud::SecurityCenter::V2::Label](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-Label)>) — Container labels, as provided by the container runtime. 



**Returns**

  * (::Array<[::Google::Cloud::SecurityCenter::V2::Label](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-Label)>) — Container labels, as provided by the container runtime. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Name of the container. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Name of the container. 



**Returns**

  * (::String) — Name of the container. 



### #uri
    
    
    def uri() -> ::String

**Returns**

  * (::String) — Container image URI provided when configuring a pod or container. This string can identify a container image version using mutable tags. 



### #uri=
    
    
    def uri=(value) -> ::String

**Parameter**

  * **value** (::String) — Container image URI provided when configuring a pod or container. This string can identify a container image version using mutable tags. 



**Returns**

  * (::String) — Container image URI provided when configuring a pod or container. This string can identify a container image version using mutable tags. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
