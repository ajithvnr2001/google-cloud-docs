---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AcceleratorType/
title: Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::AcceleratorType (v4.0.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:23:49.343089+00:00
---

# Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::AcceleratorType (v4.0.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AcceleratorType/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::AcceleratorType (v4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.12.0  3.10.0  3.9.1  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.22.0  2.21.1  2.20.0  2.19.1  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.2  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.5.0 

Reference documentation and code samples for the Google Cloud Compute V1 API class Google::Cloud::Compute::V1::AcceleratorType.

Represents an Accelerator Type resource.

Google Cloud Platform provides graphics processing units (accelerators) that you can add to VM instances to improve or accelerate performance when working with intensive workloads. For more information, readGPUs on Compute Engine.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #creation_timestamp
    
    
    def creation_timestamp() -> ::String

**Returns**

  * (::String) — [Output Only] Creation timestamp inRFC3339 text format. 



### #creation_timestamp=
    
    
    def creation_timestamp=(value) -> ::String

**Parameter**

  * **value** (::String) — [Output Only] Creation timestamp inRFC3339 text format. 



**Returns**

  * (::String) — [Output Only] Creation timestamp inRFC3339 text format. 



### #deprecated
    
    
    def deprecated() -> ::Google::Cloud::Compute::V1::DeprecationStatus

**Returns**

  * ([::Google::Cloud::Compute::V1::DeprecationStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-DeprecationStatus)) — [Output Only] The deprecation status associated with this accelerator type. 



### #deprecated=
    
    
    def deprecated=(value) -> ::Google::Cloud::Compute::V1::DeprecationStatus

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::DeprecationStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-DeprecationStatus)) — [Output Only] The deprecation status associated with this accelerator type. 



**Returns**

  * ([::Google::Cloud::Compute::V1::DeprecationStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-DeprecationStatus)) — [Output Only] The deprecation status associated with this accelerator type. 



### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — [Output Only] An optional textual description of the resource. 



### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) — [Output Only] An optional textual description of the resource. 



**Returns**

  * (::String) — [Output Only] An optional textual description of the resource. 



### #id
    
    
    def id() -> ::Integer

**Returns**

  * (::Integer) — [Output Only] The unique identifier for the resource. This identifier is defined by the server. 



### #id=
    
    
    def id=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — [Output Only] The unique identifier for the resource. This identifier is defined by the server. 



**Returns**

  * (::Integer) — [Output Only] The unique identifier for the resource. This identifier is defined by the server. 



### #kind
    
    
    def kind() -> ::String

**Returns**

  * (::String) — Output only. [Output Only] The type of the resource. Alwayscompute#acceleratorType for accelerator types. 



### #kind=
    
    
    def kind=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. [Output Only] The type of the resource. Alwayscompute#acceleratorType for accelerator types. 



**Returns**

  * (::String) — Output only. [Output Only] The type of the resource. Alwayscompute#acceleratorType for accelerator types. 



### #maximum_cards_per_instance
    
    
    def maximum_cards_per_instance() -> ::Integer

**Returns**

  * (::Integer) — [Output Only] Maximum number of accelerator cards allowed per instance. 



### #maximum_cards_per_instance=
    
    
    def maximum_cards_per_instance=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — [Output Only] Maximum number of accelerator cards allowed per instance. 



**Returns**

  * (::Integer) — [Output Only] Maximum number of accelerator cards allowed per instance. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — [Output Only] Name of the resource. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — [Output Only] Name of the resource. 



**Returns**

  * (::String) — [Output Only] Name of the resource. 



### #resource_metadata
    
    
    def resource_metadata() -> ::Google::Cloud::Compute::V1::ResourceMetadata

**Returns**

  * ([::Google::Cloud::Compute::V1::ResourceMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ResourceMetadata)) — Output only. Contains standard resource metadata for an AcceleratorType resource. It is populated for each instance of the AcceleratorType resource, and includes the api_version the instance was retrieved through, and its canonical resource_type name. 



### #resource_metadata=
    
    
    def resource_metadata=(value) -> ::Google::Cloud::Compute::V1::ResourceMetadata

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::ResourceMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ResourceMetadata)) — Output only. Contains standard resource metadata for an AcceleratorType resource. It is populated for each instance of the AcceleratorType resource, and includes the api_version the instance was retrieved through, and its canonical resource_type name. 



**Returns**

  * ([::Google::Cloud::Compute::V1::ResourceMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ResourceMetadata)) — Output only. Contains standard resource metadata for an AcceleratorType resource. It is populated for each instance of the AcceleratorType resource, and includes the api_version the instance was retrieved through, and its canonical resource_type name. 



### #self_link
    
    
    def self_link() -> ::String

**Returns**

  * (::String) — Output only. [Output Only] Server-defined, fully qualified URL for this resource. 



### #self_link=
    
    
    def self_link=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. [Output Only] Server-defined, fully qualified URL for this resource. 



**Returns**

  * (::String) — Output only. [Output Only] Server-defined, fully qualified URL for this resource. 



### #zone
    
    
    def zone() -> ::String

**Returns**

  * (::String) — [Output Only] The name of the zone where the accelerator type resides, such as us-central1-a. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. 



### #zone=
    
    
    def zone=(value) -> ::String

**Parameter**

  * **value** (::String) — [Output Only] The name of the zone where the accelerator type resides, such as us-central1-a. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. 



**Returns**

  * (::String) — [Output Only] The name of the zone where the accelerator type resides, such as us-central1-a. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
