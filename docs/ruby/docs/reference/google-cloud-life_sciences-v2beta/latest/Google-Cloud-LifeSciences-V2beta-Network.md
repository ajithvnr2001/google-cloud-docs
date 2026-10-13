---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-life_sciences-v2beta/latest/Google-Cloud-LifeSciences-V2beta-Network/
title: Cloud Life Sciences V2beta API - Class Google::Cloud::LifeSciences::V2beta::Network (v0.16.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:45:14.486085+00:00
---

# Cloud Life Sciences V2beta API - Class Google::Cloud::LifeSciences::V2beta::Network (v0.16.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-life_sciences-v2beta/latest/Google-Cloud-LifeSciences-V2beta-Network/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Life Sciences V2beta API - Class Google::Cloud::LifeSciences::V2beta::Network (v0.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.16.0 (latest)  0.15.0  0.14.0  0.13.1  0.12.0  0.11.0  0.10.1  0.9.0  0.8.2  0.7.2  0.6.0  0.5.1  0.4.0  0.3.0  0.2.0  0.1.4 

Reference documentation and code samples for the Cloud Life Sciences V2beta API class Google::Cloud::LifeSciences::V2beta::Network.

VM networking options.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #network
    
    
    def network() -> ::String

**Returns**

  * (::String) — The network name to attach the VM's network interface to. The value will be prefixed with `global/networks/` unless it contains a `/`, in which case it is assumed to be a fully specified network resource URL.

If unspecified, the global default network is used. 




### #network=
    
    
    def network=(value) -> ::String

**Parameter**

  * **value** (::String) — The network name to attach the VM's network interface to. The value will be prefixed with `global/networks/` unless it contains a `/`, in which case it is assumed to be a fully specified network resource URL.

If unspecified, the global default network is used. 




**Returns**

  * (::String) — The network name to attach the VM's network interface to. The value will be prefixed with `global/networks/` unless it contains a `/`, in which case it is assumed to be a fully specified network resource URL.

If unspecified, the global default network is used. 




### #subnetwork
    
    
    def subnetwork() -> ::String

**Returns**

  * (::String) — If the specified network is configured for custom subnet creation, the name of the subnetwork to attach the instance to must be specified here.

The value is prefixed with `regions/*/subnetworks/` unless it contains a `/`, in which case it is assumed to be a fully specified subnetwork resource URL.

If the `*` character appears in the value, it is replaced with the region that the virtual machine has been allocated in. 




### #subnetwork=
    
    
    def subnetwork=(value) -> ::String

**Parameter**

  * **value** (::String) — If the specified network is configured for custom subnet creation, the name of the subnetwork to attach the instance to must be specified here.

The value is prefixed with `regions/*/subnetworks/` unless it contains a `/`, in which case it is assumed to be a fully specified subnetwork resource URL.

If the `*` character appears in the value, it is replaced with the region that the virtual machine has been allocated in. 




**Returns**

  * (::String) — If the specified network is configured for custom subnet creation, the name of the subnetwork to attach the instance to must be specified here.

The value is prefixed with `regions/*/subnetworks/` unless it contains a `/`, in which case it is assumed to be a fully specified subnetwork resource URL.

If the `*` character appears in the value, it is replaced with the region that the virtual machine has been allocated in. 




### #use_private_address
    
    
    def use_private_address() -> ::Boolean

**Returns**

  * (::Boolean) — If set to true, do not attach a public IP address to the VM. Note that without a public IP address, additional configuration is required to allow the VM to access Google services.

See https://cloud.google.com/vpc/docs/configure-private-google-access for more information. 




### #use_private_address=
    
    
    def use_private_address=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — If set to true, do not attach a public IP address to the VM. Note that without a public IP address, additional configuration is required to allow the VM to access Google services.

See https://cloud.google.com/vpc/docs/configure-private-google-access for more information. 




**Returns**

  * (::Boolean) — If set to true, do not attach a public IP address to the VM. Note that without a public IP address, additional configuration is required to allow the VM to access Google services.

See https://cloud.google.com/vpc/docs/configure-private-google-access for more information. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
