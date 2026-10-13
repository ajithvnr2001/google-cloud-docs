---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-InterconnectDiagnostics/
title: Distributed Cloud Edge Network V1 API - Class Google::Cloud::EdgeNetwork::V1::InterconnectDiagnostics (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:03:15.769556+00:00
---

# Distributed Cloud Edge Network V1 API - Class Google::Cloud::EdgeNetwork::V1::InterconnectDiagnostics (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-InterconnectDiagnostics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Distributed Cloud Edge Network V1 API - Class Google::Cloud::EdgeNetwork::V1::InterconnectDiagnostics (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.0  2.3.1  2.2.0  2.1.0  2.0.2  1.2.0  1.1.0  1.0.3  0.5.0  0.4.1  0.3.1  0.2.1  0.1.0 

Reference documentation and code samples for the Distributed Cloud Edge Network V1 API class Google::Cloud::EdgeNetwork::V1::InterconnectDiagnostics.

Diagnostics information about interconnect, contains detailed and current technical information about Google's side of the connection.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #link_layer_addresses
    
    
    def link_layer_addresses() -> ::Array<::Google::Cloud::EdgeNetwork::V1::LinkLayerAddress>

**Returns**

  * (::Array<[::Google::Cloud::EdgeNetwork::V1::LinkLayerAddress](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-LinkLayerAddress)>) — A list of LinkLayerAddress, describing the ip address and corresponding link-layer address of the neighbors for this interconnect. 



### #link_layer_addresses=
    
    
    def link_layer_addresses=(value) -> ::Array<::Google::Cloud::EdgeNetwork::V1::LinkLayerAddress>

**Parameter**

  * **value** (::Array<[::Google::Cloud::EdgeNetwork::V1::LinkLayerAddress](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-LinkLayerAddress)>) — A list of LinkLayerAddress, describing the ip address and corresponding link-layer address of the neighbors for this interconnect. 



**Returns**

  * (::Array<[::Google::Cloud::EdgeNetwork::V1::LinkLayerAddress](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-LinkLayerAddress)>) — A list of LinkLayerAddress, describing the ip address and corresponding link-layer address of the neighbors for this interconnect. 



### #links
    
    
    def links() -> ::Array<::Google::Cloud::EdgeNetwork::V1::InterconnectDiagnostics::LinkStatus>

**Returns**

  * (::Array<[::Google::Cloud::EdgeNetwork::V1::InterconnectDiagnostics::LinkStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-InterconnectDiagnostics-LinkStatus)>) — A list of LinkStatus objects, used to describe the status for each link on the Interconnect. 



### #links=
    
    
    def links=(value) -> ::Array<::Google::Cloud::EdgeNetwork::V1::InterconnectDiagnostics::LinkStatus>

**Parameter**

  * **value** (::Array<[::Google::Cloud::EdgeNetwork::V1::InterconnectDiagnostics::LinkStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-InterconnectDiagnostics-LinkStatus)>) — A list of LinkStatus objects, used to describe the status for each link on the Interconnect. 



**Returns**

  * (::Array<[::Google::Cloud::EdgeNetwork::V1::InterconnectDiagnostics::LinkStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-InterconnectDiagnostics-LinkStatus)>) — A list of LinkStatus objects, used to describe the status for each link on the Interconnect. 



### #mac_address
    
    
    def mac_address() -> ::String

**Returns**

  * (::String) — The MAC address of the Interconnect's bundle interface. 



### #mac_address=
    
    
    def mac_address=(value) -> ::String

**Parameter**

  * **value** (::String) — The MAC address of the Interconnect's bundle interface. 



**Returns**

  * (::String) — The MAC address of the Interconnect's bundle interface. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
