---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Network/
title: App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::Network (v1.8.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:48:32.865634+00:00
---

# App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::Network (v1.8.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Network/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::Network (v1.8.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.2 (latest)  1.8.1  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.1  0.5.0  0.4.0  0.3.6 

Reference documentation and code samples for the App Engine Admin V1 API class Google::Cloud::AppEngine::V1::Network.

Extra network settings. Only applicable in the App Engine flexible environment.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #forwarded_ports
    
    
    def forwarded_ports() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — List of ports, or port pairs, to forward from the virtual machine to the application container. Only applicable in the App Engine flexible environment. 



### #forwarded_ports=
    
    
    def forwarded_ports=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — List of ports, or port pairs, to forward from the virtual machine to the application container. Only applicable in the App Engine flexible environment. 



**Returns**

  * (::Array<::String>) — List of ports, or port pairs, to forward from the virtual machine to the application container. Only applicable in the App Engine flexible environment. 



### #instance_tag
    
    
    def instance_tag() -> ::String

**Returns**

  * (::String) — Tag to apply to the instance during creation. Only applicable in the App Engine flexible environment. 



### #instance_tag=
    
    
    def instance_tag=(value) -> ::String

**Parameter**

  * **value** (::String) — Tag to apply to the instance during creation. Only applicable in the App Engine flexible environment. 



**Returns**

  * (::String) — Tag to apply to the instance during creation. Only applicable in the App Engine flexible environment. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Google Compute Engine network where the virtual machines are created. Specify the short name, not the resource path.

Defaults to `default`. 




### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Google Compute Engine network where the virtual machines are created. Specify the short name, not the resource path.

Defaults to `default`. 




**Returns**

  * (::String) — Google Compute Engine network where the virtual machines are created. Specify the short name, not the resource path.

Defaults to `default`. 




### #session_affinity
    
    
    def session_affinity() -> ::Boolean

**Returns**

  * (::Boolean) — Enable session affinity. Only applicable in the App Engine flexible environment. 



### #session_affinity=
    
    
    def session_affinity=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Enable session affinity. Only applicable in the App Engine flexible environment. 



**Returns**

  * (::Boolean) — Enable session affinity. Only applicable in the App Engine flexible environment. 



### #subnetwork_name
    
    
    def subnetwork_name() -> ::String

**Returns**

  * (::String) — Google Cloud Platform sub-network where the virtual machines are created. Specify the short name, not the resource path.

If a subnetwork name is specified, a network name will also be required unless it is for the default network.

    * If the network that the instance is being created in is a Legacy network, then the IP address is allocated from the IPv4Range.
    * If the network that the instance is being created in is an auto Subnet Mode Network, then only network name should be specified (not the subnetwork_name) and the IP address is created from the IPCidrRange of the subnetwork that exists in that zone for that network.
    * If the network that the instance is being created in is a custom Subnet Mode Network, then the subnetwork_name must be specified and the IP address is created from the IPCidrRange of the subnetwork.

If specified, the subnetwork must exist in the same region as the App Engine flexible environment application. 




### #subnetwork_name=
    
    
    def subnetwork_name=(value) -> ::String

**Parameter**

  * **value** (::String) — Google Cloud Platform sub-network where the virtual machines are created. Specify the short name, not the resource path.

If a subnetwork name is specified, a network name will also be required unless it is for the default network.

    * If the network that the instance is being created in is a Legacy network, then the IP address is allocated from the IPv4Range.
    * If the network that the instance is being created in is an auto Subnet Mode Network, then only network name should be specified (not the subnetwork_name) and the IP address is created from the IPCidrRange of the subnetwork that exists in that zone for that network.
    * If the network that the instance is being created in is a custom Subnet Mode Network, then the subnetwork_name must be specified and the IP address is created from the IPCidrRange of the subnetwork.

If specified, the subnetwork must exist in the same region as the App Engine flexible environment application. 




**Returns**

  * (::String) — Google Cloud Platform sub-network where the virtual machines are created. Specify the short name, not the resource path.

If a subnetwork name is specified, a network name will also be required unless it is for the default network.

    * If the network that the instance is being created in is a Legacy network, then the IP address is allocated from the IPv4Range.
    * If the network that the instance is being created in is an auto Subnet Mode Network, then only network name should be specified (not the subnetwork_name) and the IP address is created from the IPCidrRange of the subnetwork that exists in that zone for that network.
    * If the network that the instance is being created in is a custom Subnet Mode Network, then the subnetwork_name must be specified and the IP address is created from the IPCidrRange of the subnetwork.

If specified, the subnetwork must exist in the same region as the App Engine flexible environment application. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
