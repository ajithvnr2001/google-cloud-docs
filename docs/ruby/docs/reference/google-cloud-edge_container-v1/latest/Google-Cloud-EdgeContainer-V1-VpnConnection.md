---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_container-v1/latest/Google-Cloud-EdgeContainer-V1-VpnConnection/
title: Distributed Cloud Edge Container V1 API - Class Google::Cloud::EdgeContainer::V1::VpnConnection (v1.5.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:46:37.727111+00:00
---

# Distributed Cloud Edge Container V1 API - Class Google::Cloud::EdgeContainer::V1::VpnConnection (v1.5.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_container-v1/latest/Google-Cloud-EdgeContainer-V1-VpnConnection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Distributed Cloud Edge Container V1 API - Class Google::Cloud::EdgeContainer::V1::VpnConnection (v1.5.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.5.2 (latest)  1.5.1  1.4.0  1.3.1  1.2.0  1.1.0  1.0.1  0.4.0  0.3.0  0.2.0  0.1.1 

Reference documentation and code samples for the Distributed Cloud Edge Container V1 API class Google::Cloud::EdgeContainer::V1::VpnConnection.

A VPN connection .

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #bgp_routing_mode
    
    
    def bgp_routing_mode() -> ::Google::Cloud::EdgeContainer::V1::VpnConnection::BgpRoutingMode

**Returns**

  * ([::Google::Cloud::EdgeContainer::V1::VpnConnection::BgpRoutingMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_container-v1/latest/Google-Cloud-EdgeContainer-V1-VpnConnection-BgpRoutingMode)) — Dynamic routing mode of the VPC network, `regional` or `global`. 



### #bgp_routing_mode=
    
    
    def bgp_routing_mode=(value) -> ::Google::Cloud::EdgeContainer::V1::VpnConnection::BgpRoutingMode

**Parameter**

  * **value** ([::Google::Cloud::EdgeContainer::V1::VpnConnection::BgpRoutingMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_container-v1/latest/Google-Cloud-EdgeContainer-V1-VpnConnection-BgpRoutingMode)) — Dynamic routing mode of the VPC network, `regional` or `global`. 



**Returns**

  * ([::Google::Cloud::EdgeContainer::V1::VpnConnection::BgpRoutingMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_container-v1/latest/Google-Cloud-EdgeContainer-V1-VpnConnection-BgpRoutingMode)) — Dynamic routing mode of the VPC network, `regional` or `global`. 



### #cluster
    
    
    def cluster() -> ::String

**Returns**

  * (::String) — The canonical Cluster name to connect to. It is in the form of projects/{project}/locations/{location}/clusters/{cluster}. 



### #cluster=
    
    
    def cluster=(value) -> ::String

**Parameter**

  * **value** (::String) — The canonical Cluster name to connect to. It is in the form of projects/{project}/locations/{location}/clusters/{cluster}. 



**Returns**

  * (::String) — The canonical Cluster name to connect to. It is in the form of projects/{project}/locations/{location}/clusters/{cluster}. 



### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_container-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time when the VPN connection was created. 



### #details
    
    
    def details() -> ::Google::Cloud::EdgeContainer::V1::VpnConnection::Details

**Returns**

  * ([::Google::Cloud::EdgeContainer::V1::VpnConnection::Details](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_container-v1/latest/Google-Cloud-EdgeContainer-V1-VpnConnection-Details)) — Output only. The created connection details. 



### #enable_high_availability
    
    
    def enable_high_availability() -> ::Boolean

**Returns**

  * (::Boolean) — Whether this VPN connection has HA enabled on cluster side. If enabled, when creating VPN connection we will attempt to use 2 ANG floating IPs. 



### #enable_high_availability=
    
    
    def enable_high_availability=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Whether this VPN connection has HA enabled on cluster side. If enabled, when creating VPN connection we will attempt to use 2 ANG floating IPs. 



**Returns**

  * (::Boolean) — Whether this VPN connection has HA enabled on cluster side. If enabled, when creating VPN connection we will attempt to use 2 ANG floating IPs. 



### #labels
    
    
    def labels() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Labels associated with this resource. 



### #labels=
    
    
    def labels=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Labels associated with this resource. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Labels associated with this resource. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Required. The resource name of VPN connection 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The resource name of VPN connection 



**Returns**

  * (::String) — Required. The resource name of VPN connection 



### #nat_gateway_ip
    
    
    def nat_gateway_ip() -> ::String

**Returns**

  * (::String) — NAT gateway IP, or WAN IP address. If a customer has multiple NAT IPs, the customer needs to configure NAT such that only one external IP maps to the GMEC Anthos cluster. This is empty if NAT is not used. 



### #nat_gateway_ip=
    
    
    def nat_gateway_ip=(value) -> ::String

**Parameter**

  * **value** (::String) — NAT gateway IP, or WAN IP address. If a customer has multiple NAT IPs, the customer needs to configure NAT such that only one external IP maps to the GMEC Anthos cluster. This is empty if NAT is not used. 



**Returns**

  * (::String) — NAT gateway IP, or WAN IP address. If a customer has multiple NAT IPs, the customer needs to configure NAT such that only one external IP maps to the GMEC Anthos cluster. This is empty if NAT is not used. 



### #router
    
    
    def router() -> ::String

**Returns**

  * (::String) — Optional. The VPN connection Cloud Router name. 



### #router=
    
    
    def router=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The VPN connection Cloud Router name. 



**Returns**

  * (::String) — Optional. The VPN connection Cloud Router name. 



### #update_time
    
    
    def update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_container-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time when the VPN connection was last updated. 



### #vpc
    
    
    def vpc() -> ::String

**Returns**

  * (::String) — The network ID of VPC to connect to. 



### #vpc=
    
    
    def vpc=(value) -> ::String

**Parameter**

  * **value** (::String) — The network ID of VPC to connect to. 



**Returns**

  * (::String) — The network ID of VPC to connect to. 



### #vpc_project
    
    
    def vpc_project() -> ::Google::Cloud::EdgeContainer::V1::VpnConnection::VpcProject

**Returns**

  * ([::Google::Cloud::EdgeContainer::V1::VpnConnection::VpcProject](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_container-v1/latest/Google-Cloud-EdgeContainer-V1-VpnConnection-VpcProject)) — Optional. Project detail of the VPC network. Required if VPC is in a different project than the cluster project. 



### #vpc_project=
    
    
    def vpc_project=(value) -> ::Google::Cloud::EdgeContainer::V1::VpnConnection::VpcProject

**Parameter**

  * **value** ([::Google::Cloud::EdgeContainer::V1::VpnConnection::VpcProject](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_container-v1/latest/Google-Cloud-EdgeContainer-V1-VpnConnection-VpcProject)) — Optional. Project detail of the VPC network. Required if VPC is in a different project than the cluster project. 



**Returns**

  * ([::Google::Cloud::EdgeContainer::V1::VpnConnection::VpcProject](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_container-v1/latest/Google-Cloud-EdgeContainer-V1-VpnConnection-VpcProject)) — Optional. Project detail of the VPC network. Required if VPC is in a different project than the cluster project. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
