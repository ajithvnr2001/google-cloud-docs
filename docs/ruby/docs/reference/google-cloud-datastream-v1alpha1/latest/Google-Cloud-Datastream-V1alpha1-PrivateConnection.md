---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-PrivateConnection/
title: Datastream V1alpha1 API - Class Google::Cloud::Datastream::V1alpha1::PrivateConnection (v0.15.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:42:58.234163+00:00
---

# Datastream V1alpha1 API - Class Google::Cloud::Datastream::V1alpha1::PrivateConnection (v0.15.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-PrivateConnection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Datastream V1alpha1 API - Class Google::Cloud::Datastream::V1alpha1::PrivateConnection (v0.15.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.1 (latest)  0.15.0  0.14.0  0.13.1  0.12.0  0.11.1  0.10.1  0.9.0  0.8.0  0.7.1  0.6.2  0.5.0  0.4.0  0.3.0  0.2.0  0.1.2 

Reference documentation and code samples for the Datastream V1alpha1 API class Google::Cloud::Datastream::V1alpha1::PrivateConnection.

The PrivateConnection resource is used to establish private connectivity between Datastream and a customer's network.

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

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Protobuf-Timestamp)) — Output only. The create time of the resource. 



### #display_name
    
    
    def display_name() -> ::String

**Returns**

  * (::String) — Required. Display name. 



### #display_name=
    
    
    def display_name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Display name. 



**Returns**

  * (::String) — Required. Display name. 



### #error
    
    
    def error() -> ::Google::Cloud::Datastream::V1alpha1::Error

**Returns**

  * ([::Google::Cloud::Datastream::V1alpha1::Error](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-Error)) — Output only. In case of error, the details of the error in a user-friendly format. 



### #labels
    
    
    def labels() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Labels. 



### #labels=
    
    
    def labels=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Labels. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Labels. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Output only. The resource's name. 



### #state
    
    
    def state() -> ::Google::Cloud::Datastream::V1alpha1::PrivateConnection::State

**Returns**

  * ([::Google::Cloud::Datastream::V1alpha1::PrivateConnection::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-PrivateConnection-State)) — Output only. The state of the Private Connection. 



### #update_time
    
    
    def update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Protobuf-Timestamp)) — Output only. The update time of the resource. 



### #vpc_peering_config
    
    
    def vpc_peering_config() -> ::Google::Cloud::Datastream::V1alpha1::VpcPeeringConfig

**Returns**

  * ([::Google::Cloud::Datastream::V1alpha1::VpcPeeringConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-VpcPeeringConfig)) — VPC Peering Config 



### #vpc_peering_config=
    
    
    def vpc_peering_config=(value) -> ::Google::Cloud::Datastream::V1alpha1::VpcPeeringConfig

**Parameter**

  * **value** ([::Google::Cloud::Datastream::V1alpha1::VpcPeeringConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-VpcPeeringConfig)) — VPC Peering Config 



**Returns**

  * ([::Google::Cloud::Datastream::V1alpha1::VpcPeeringConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-VpcPeeringConfig)) — VPC Peering Config 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
