---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_container-v1/latest/Google-Cloud-EdgeContainer-V1-VpnConnection-Details/
title: Distributed Cloud Edge Container V1 API - Class Google::Cloud::EdgeContainer::V1::VpnConnection::Details (v1.5.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:51:04.435755+00:00
---

# Distributed Cloud Edge Container V1 API - Class Google::Cloud::EdgeContainer::V1::VpnConnection::Details (v1.5.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_container-v1/latest/Google-Cloud-EdgeContainer-V1-VpnConnection-Details/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Distributed Cloud Edge Container V1 API - Class Google::Cloud::EdgeContainer::V1::VpnConnection::Details (v1.5.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.5.2 (latest)  1.5.1  1.4.0  1.3.1  1.2.0  1.1.0  1.0.1  0.4.0  0.3.0  0.2.0  0.1.1 

Reference documentation and code samples for the Distributed Cloud Edge Container V1 API class Google::Cloud::EdgeContainer::V1::VpnConnection::Details.

The created connection details.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #cloud_router
    
    
    def cloud_router() -> ::Google::Cloud::EdgeContainer::V1::VpnConnection::Details::CloudRouter

**Returns**

  * ([::Google::Cloud::EdgeContainer::V1::VpnConnection::Details::CloudRouter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_container-v1/latest/Google-Cloud-EdgeContainer-V1-VpnConnection-Details-CloudRouter)) — The Cloud Router info. 



### #cloud_router=
    
    
    def cloud_router=(value) -> ::Google::Cloud::EdgeContainer::V1::VpnConnection::Details::CloudRouter

**Parameter**

  * **value** ([::Google::Cloud::EdgeContainer::V1::VpnConnection::Details::CloudRouter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_container-v1/latest/Google-Cloud-EdgeContainer-V1-VpnConnection-Details-CloudRouter)) — The Cloud Router info. 



**Returns**

  * ([::Google::Cloud::EdgeContainer::V1::VpnConnection::Details::CloudRouter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_container-v1/latest/Google-Cloud-EdgeContainer-V1-VpnConnection-Details-CloudRouter)) — The Cloud Router info. 



### #cloud_vpns
    
    
    def cloud_vpns() -> ::Array<::Google::Cloud::EdgeContainer::V1::VpnConnection::Details::CloudVpn>

**Returns**

  * (::Array<[::Google::Cloud::EdgeContainer::V1::VpnConnection::Details::CloudVpn](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_container-v1/latest/Google-Cloud-EdgeContainer-V1-VpnConnection-Details-CloudVpn)>) — Each connection has multiple Cloud VPN gateways. 



### #cloud_vpns=
    
    
    def cloud_vpns=(value) -> ::Array<::Google::Cloud::EdgeContainer::V1::VpnConnection::Details::CloudVpn>

**Parameter**

  * **value** (::Array<[::Google::Cloud::EdgeContainer::V1::VpnConnection::Details::CloudVpn](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_container-v1/latest/Google-Cloud-EdgeContainer-V1-VpnConnection-Details-CloudVpn)>) — Each connection has multiple Cloud VPN gateways. 



**Returns**

  * (::Array<[::Google::Cloud::EdgeContainer::V1::VpnConnection::Details::CloudVpn](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_container-v1/latest/Google-Cloud-EdgeContainer-V1-VpnConnection-Details-CloudVpn)>) — Each connection has multiple Cloud VPN gateways. 



### #error
    
    
    def error() -> ::String

**Returns**

  * (::String) — The error message. This is only populated when state=ERROR. 



### #error=
    
    
    def error=(value) -> ::String

**Parameter**

  * **value** (::String) — The error message. This is only populated when state=ERROR. 



**Returns**

  * (::String) — The error message. This is only populated when state=ERROR. 



### #state
    
    
    def state() -> ::Google::Cloud::EdgeContainer::V1::VpnConnection::Details::State

**Returns**

  * ([::Google::Cloud::EdgeContainer::V1::VpnConnection::Details::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_container-v1/latest/Google-Cloud-EdgeContainer-V1-VpnConnection-Details-State)) — The state of this connection. 



### #state=
    
    
    def state=(value) -> ::Google::Cloud::EdgeContainer::V1::VpnConnection::Details::State

**Parameter**

  * **value** ([::Google::Cloud::EdgeContainer::V1::VpnConnection::Details::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_container-v1/latest/Google-Cloud-EdgeContainer-V1-VpnConnection-Details-State)) — The state of this connection. 



**Returns**

  * ([::Google::Cloud::EdgeContainer::V1::VpnConnection::Details::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_container-v1/latest/Google-Cloud-EdgeContainer-V1-VpnConnection-Details-State)) — The state of this connection. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
