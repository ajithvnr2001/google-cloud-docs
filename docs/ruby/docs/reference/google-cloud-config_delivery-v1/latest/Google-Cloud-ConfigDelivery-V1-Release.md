---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_delivery-v1/latest/Google-Cloud-ConfigDelivery-V1-Release/
title: Config Delivery V1 API - Class Google::Cloud::ConfigDelivery::V1::Release (v1.0.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:18:37.650349+00:00
---

# Config Delivery V1 API - Class Google::Cloud::ConfigDelivery::V1::Release (v1.0.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_delivery-v1/latest/Google-Cloud-ConfigDelivery-V1-Release/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Config Delivery V1 API - Class Google::Cloud::ConfigDelivery::V1::Release (v1.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.1 (latest)  1.0.0  0.6.0  0.5.0  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Config Delivery V1 API class Google::Cloud::ConfigDelivery::V1::Release.

`Release` represents a versioned release containing kubernetes manifests.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_delivery-v1/latest/Google-Protobuf-Timestamp)) — Output only. Time `Release` was created. 



### #info
    
    
    def info() -> ::Google::Cloud::ConfigDelivery::V1::ReleaseInfo

**Returns**

  * ([::Google::Cloud::ConfigDelivery::V1::ReleaseInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_delivery-v1/latest/Google-Cloud-ConfigDelivery-V1-ReleaseInfo)) — Optional. `ResourceBundle` Release extra information e.g., artifact registry image path. 



### #info=
    
    
    def info=(value) -> ::Google::Cloud::ConfigDelivery::V1::ReleaseInfo

**Parameter**

  * **value** ([::Google::Cloud::ConfigDelivery::V1::ReleaseInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_delivery-v1/latest/Google-Cloud-ConfigDelivery-V1-ReleaseInfo)) — Optional. `ResourceBundle` Release extra information e.g., artifact registry image path. 



**Returns**

  * ([::Google::Cloud::ConfigDelivery::V1::ReleaseInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_delivery-v1/latest/Google-Cloud-ConfigDelivery-V1-ReleaseInfo)) — Optional. `ResourceBundle` Release extra information e.g., artifact registry image path. 



### #labels
    
    
    def labels() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. Labels as key value pairs. 



### #labels=
    
    
    def labels=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Optional. Labels as key value pairs. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. Labels as key value pairs. 



### #lifecycle
    
    
    def lifecycle() -> ::Google::Cloud::ConfigDelivery::V1::Release::Lifecycle

**Returns**

  * ([::Google::Cloud::ConfigDelivery::V1::Release::Lifecycle](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_delivery-v1/latest/Google-Cloud-ConfigDelivery-V1-Release-Lifecycle)) — Optional. lifecycle of the `Release`. 



### #lifecycle=
    
    
    def lifecycle=(value) -> ::Google::Cloud::ConfigDelivery::V1::Release::Lifecycle

**Parameter**

  * **value** ([::Google::Cloud::ConfigDelivery::V1::Release::Lifecycle](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_delivery-v1/latest/Google-Cloud-ConfigDelivery-V1-Release-Lifecycle)) — Optional. lifecycle of the `Release`. 



**Returns**

  * ([::Google::Cloud::ConfigDelivery::V1::Release::Lifecycle](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_delivery-v1/latest/Google-Cloud-ConfigDelivery-V1-Release-Lifecycle)) — Optional. lifecycle of the `Release`. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Identifier. Name of the Release. Format is `projects/{project}/locations/location}/resourceBundles/{resource_bundle}/release/[a-z][a-z0-9\-]{0,62}`. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Identifier. Name of the Release. Format is `projects/{project}/locations/location}/resourceBundles/{resource_bundle}/release/[a-z][a-z0-9\-]{0,62}`. 



**Returns**

  * (::String) — Identifier. Name of the Release. Format is `projects/{project}/locations/location}/resourceBundles/{resource_bundle}/release/[a-z][a-z0-9\-]{0,62}`. 



### #publish_time
    
    
    def publish_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_delivery-v1/latest/Google-Protobuf-Timestamp)) — Output only. Time the `Release` was published. 



### #update_time
    
    
    def update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_delivery-v1/latest/Google-Protobuf-Timestamp)) — Output only. Time `Release` was last updated. 



### #version
    
    
    def version() -> ::String

**Returns**

  * (::String) — Required. version of the `Release`. This must be v



### #version=
    
    
    def version=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. version of the `Release`. This must be v



**Returns**

  * (::String) — Required. version of the `Release`. This must be v



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
