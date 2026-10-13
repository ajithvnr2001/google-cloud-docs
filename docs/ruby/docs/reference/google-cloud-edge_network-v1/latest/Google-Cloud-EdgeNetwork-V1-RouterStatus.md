---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-RouterStatus/
title: Distributed Cloud Edge Network V1 API - Class Google::Cloud::EdgeNetwork::V1::RouterStatus (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:52:00.646333+00:00
---

# Distributed Cloud Edge Network V1 API - Class Google::Cloud::EdgeNetwork::V1::RouterStatus (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-RouterStatus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Distributed Cloud Edge Network V1 API - Class Google::Cloud::EdgeNetwork::V1::RouterStatus (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.0  2.3.1  2.2.0  2.1.0  2.0.2  1.2.0  1.1.0  1.0.3  0.5.0  0.4.1  0.3.1  0.2.1  0.1.0 

Reference documentation and code samples for the Distributed Cloud Edge Network V1 API class Google::Cloud::EdgeNetwork::V1::RouterStatus.

Describing the current status of a router.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #bgp_peer_status
    
    
    def bgp_peer_status() -> ::Array<::Google::Cloud::EdgeNetwork::V1::RouterStatus::BgpPeerStatus>

**Returns**

  * (::Array<[::Google::Cloud::EdgeNetwork::V1::RouterStatus::BgpPeerStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-RouterStatus-BgpPeerStatus)>) — A list of BgpPeerStatus objects, describing all BGP peers related to this router. 



### #bgp_peer_status=
    
    
    def bgp_peer_status=(value) -> ::Array<::Google::Cloud::EdgeNetwork::V1::RouterStatus::BgpPeerStatus>

**Parameter**

  * **value** (::Array<[::Google::Cloud::EdgeNetwork::V1::RouterStatus::BgpPeerStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-RouterStatus-BgpPeerStatus)>) — A list of BgpPeerStatus objects, describing all BGP peers related to this router. 



**Returns**

  * (::Array<[::Google::Cloud::EdgeNetwork::V1::RouterStatus::BgpPeerStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-RouterStatus-BgpPeerStatus)>) — A list of BgpPeerStatus objects, describing all BGP peers related to this router. 



### #network
    
    
    def network() -> ::String

**Returns**

  * (::String) — The canonical name of the network to which this router belongs. 



### #network=
    
    
    def network=(value) -> ::String

**Parameter**

  * **value** (::String) — The canonical name of the network to which this router belongs. 



**Returns**

  * (::String) — The canonical name of the network to which this router belongs. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
