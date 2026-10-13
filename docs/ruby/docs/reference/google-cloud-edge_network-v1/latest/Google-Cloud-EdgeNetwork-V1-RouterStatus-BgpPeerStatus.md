---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-RouterStatus-BgpPeerStatus/
title: Distributed Cloud Edge Network V1 API - Class Google::Cloud::EdgeNetwork::V1::RouterStatus::BgpPeerStatus (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:58:12.929303+00:00
---

# Distributed Cloud Edge Network V1 API - Class Google::Cloud::EdgeNetwork::V1::RouterStatus::BgpPeerStatus (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-RouterStatus-BgpPeerStatus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Distributed Cloud Edge Network V1 API - Class Google::Cloud::EdgeNetwork::V1::RouterStatus::BgpPeerStatus (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.0  2.3.1  2.2.0  2.1.0  2.0.2  1.2.0  1.1.0  1.0.3  0.5.0  0.4.1  0.3.1  0.2.1  0.1.0 

Reference documentation and code samples for the Distributed Cloud Edge Network V1 API class Google::Cloud::EdgeNetwork::V1::RouterStatus::BgpPeerStatus.

Status of a BGP peer.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #ip_address
    
    
    def ip_address() -> ::String

**Returns**

  * (::String) — IP address of the local BGP interface. 



### #ip_address=
    
    
    def ip_address=(value) -> ::String

**Parameter**

  * **value** (::String) — IP address of the local BGP interface. 



**Returns**

  * (::String) — IP address of the local BGP interface. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Name of this BGP peer. Unique within the Routers resource. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Name of this BGP peer. Unique within the Routers resource. 



**Returns**

  * (::String) — Name of this BGP peer. Unique within the Routers resource. 



### #peer_ip_address
    
    
    def peer_ip_address() -> ::String

**Returns**

  * (::String) — IP address of the remote BGP interface. 



### #peer_ip_address=
    
    
    def peer_ip_address=(value) -> ::String

**Parameter**

  * **value** (::String) — IP address of the remote BGP interface. 



**Returns**

  * (::String) — IP address of the remote BGP interface. 



### #prefix_counter
    
    
    def prefix_counter() -> ::Google::Cloud::EdgeNetwork::V1::RouterStatus::PrefixCounter

**Returns**

  * ([::Google::Cloud::EdgeNetwork::V1::RouterStatus::PrefixCounter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-RouterStatus-PrefixCounter)) — A collection of counts for prefixes. 



### #prefix_counter=
    
    
    def prefix_counter=(value) -> ::Google::Cloud::EdgeNetwork::V1::RouterStatus::PrefixCounter

**Parameter**

  * **value** ([::Google::Cloud::EdgeNetwork::V1::RouterStatus::PrefixCounter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-RouterStatus-PrefixCounter)) — A collection of counts for prefixes. 



**Returns**

  * ([::Google::Cloud::EdgeNetwork::V1::RouterStatus::PrefixCounter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-RouterStatus-PrefixCounter)) — A collection of counts for prefixes. 



### #state
    
    
    def state() -> ::String

**Returns**

  * (::String) — BGP state as specified in RFC1771. 



### #state=
    
    
    def state=(value) -> ::String

**Parameter**

  * **value** (::String) — BGP state as specified in RFC1771. 



**Returns**

  * (::String) — BGP state as specified in RFC1771. 



### #status
    
    
    def status() -> ::Google::Cloud::EdgeNetwork::V1::RouterStatus::BgpPeerStatus::BgpStatus

**Returns**

  * ([::Google::Cloud::EdgeNetwork::V1::RouterStatus::BgpPeerStatus::BgpStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-RouterStatus-BgpPeerStatus-BgpStatus)) — The current status of BGP. 



### #status=
    
    
    def status=(value) -> ::Google::Cloud::EdgeNetwork::V1::RouterStatus::BgpPeerStatus::BgpStatus

**Parameter**

  * **value** ([::Google::Cloud::EdgeNetwork::V1::RouterStatus::BgpPeerStatus::BgpStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-RouterStatus-BgpPeerStatus-BgpStatus)) — The current status of BGP. 



**Returns**

  * ([::Google::Cloud::EdgeNetwork::V1::RouterStatus::BgpPeerStatus::BgpStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-RouterStatus-BgpPeerStatus-BgpStatus)) — The current status of BGP. 



### #uptime
    
    
    def uptime() -> ::String

**Returns**

  * (::String) — Time this session has been up. Format: 14 years, 51 weeks, 6 days, 23 hours, 59 minutes, 59 seconds 



### #uptime=
    
    
    def uptime=(value) -> ::String

**Parameter**

  * **value** (::String) — Time this session has been up. Format: 14 years, 51 weeks, 6 days, 23 hours, 59 minutes, 59 seconds 



**Returns**

  * (::String) — Time this session has been up. Format: 14 years, 51 weeks, 6 days, 23 hours, 59 minutes, 59 seconds 



### #uptime_seconds
    
    
    def uptime_seconds() -> ::Integer

**Returns**

  * (::Integer) — Time this session has been up, in seconds. 



### #uptime_seconds=
    
    
    def uptime_seconds=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Time this session has been up, in seconds. 



**Returns**

  * (::Integer) — Time this session has been up, in seconds. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
