---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-batch-v1/latest/Google-Cloud-Batch-V1-AllocationPolicy-NetworkInterface/
title: Batch V1 API - Class Google::Cloud::Batch::V1::AllocationPolicy::NetworkInterface (v1.9.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:15:01.318739+00:00
---

# Batch V1 API - Class Google::Cloud::Batch::V1::AllocationPolicy::NetworkInterface (v1.9.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-batch-v1/latest/Google-Cloud-Batch-V1-AllocationPolicy-NetworkInterface/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Batch V1 API - Class Google::Cloud::Batch::V1::AllocationPolicy::NetworkInterface (v1.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.9.0 (latest)  1.8.2  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.1  1.0.0  0.21.0  0.20.1  0.19.2  0.18.3  0.17.4  0.16.2  0.15.1  0.14.0  0.13.1  0.12.0  0.11.1  0.10.5  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.3  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Batch V1 API class Google::Cloud::Batch::V1::AllocationPolicy::NetworkInterface.

A network interface.

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

  * (::String) — 

The URL of an existing network resource. You can specify the network as a full or partial URL.

For example, the following are all valid URLs:

    * https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}
    * projects/{project}/global/networks/{network}
    * global/networks/{network}



### #network=
    
    
    def network=(value) -> ::String

**Parameter**

  * **value** (::String) — 

The URL of an existing network resource. You can specify the network as a full or partial URL.

For example, the following are all valid URLs:

    * https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}
    * projects/{project}/global/networks/{network}
    * global/networks/{network}



**Returns**

  * (::String) — 

The URL of an existing network resource. You can specify the network as a full or partial URL.

For example, the following are all valid URLs:

    * https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}
    * projects/{project}/global/networks/{network}
    * global/networks/{network}



### #nic_type
    
    
    def nic_type() -> ::Google::Cloud::Batch::V1::AllocationPolicy::NetworkInterface::NicType

**Returns**

  * ([::Google::Cloud::Batch::V1::AllocationPolicy::NetworkInterface::NicType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-batch-v1/latest/Google-Cloud-Batch-V1-AllocationPolicy-NetworkInterface-NicType)) — Optional. The NIC type of the network interface. 



### #nic_type=
    
    
    def nic_type=(value) -> ::Google::Cloud::Batch::V1::AllocationPolicy::NetworkInterface::NicType

**Parameter**

  * **value** ([::Google::Cloud::Batch::V1::AllocationPolicy::NetworkInterface::NicType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-batch-v1/latest/Google-Cloud-Batch-V1-AllocationPolicy-NetworkInterface-NicType)) — Optional. The NIC type of the network interface. 



**Returns**

  * ([::Google::Cloud::Batch::V1::AllocationPolicy::NetworkInterface::NicType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-batch-v1/latest/Google-Cloud-Batch-V1-AllocationPolicy-NetworkInterface-NicType)) — Optional. The NIC type of the network interface. 



### #no_external_ip_address
    
    
    def no_external_ip_address() -> ::Boolean

**Returns**

  * (::Boolean) — Default is false (with an external IP address). Required if no external public IP address is attached to the VM. If no external public IP address, additional configuration is required to allow the VM to access Google Services. See https://cloud.google.com/vpc/docs/configure-private-google-access and https://cloud.google.com/nat/docs/gce-example#create-nat for more information. 



### #no_external_ip_address=
    
    
    def no_external_ip_address=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Default is false (with an external IP address). Required if no external public IP address is attached to the VM. If no external public IP address, additional configuration is required to allow the VM to access Google Services. See https://cloud.google.com/vpc/docs/configure-private-google-access and https://cloud.google.com/nat/docs/gce-example#create-nat for more information. 



**Returns**

  * (::Boolean) — Default is false (with an external IP address). Required if no external public IP address is attached to the VM. If no external public IP address, additional configuration is required to allow the VM to access Google Services. See https://cloud.google.com/vpc/docs/configure-private-google-access and https://cloud.google.com/nat/docs/gce-example#create-nat for more information. 



### #subnetwork
    
    
    def subnetwork() -> ::String

**Returns**

  * (::String) — 

The URL of an existing subnetwork resource in the network. You can specify the subnetwork as a full or partial URL.

For example, the following are all valid URLs:

    * https://www.googleapis.com/compute/v1/projects/{project}/regions/{region}/subnetworks/{subnetwork}
    * projects/{project}/regions/{region}/subnetworks/{subnetwork}
    * regions/{region}/subnetworks/{subnetwork}



### #subnetwork=
    
    
    def subnetwork=(value) -> ::String

**Parameter**

  * **value** (::String) — 

The URL of an existing subnetwork resource in the network. You can specify the subnetwork as a full or partial URL.

For example, the following are all valid URLs:

    * https://www.googleapis.com/compute/v1/projects/{project}/regions/{region}/subnetworks/{subnetwork}
    * projects/{project}/regions/{region}/subnetworks/{subnetwork}
    * regions/{region}/subnetworks/{subnetwork}



**Returns**

  * (::String) — 

The URL of an existing subnetwork resource in the network. You can specify the subnetwork as a full or partial URL.

For example, the following are all valid URLs:

    * https://www.googleapis.com/compute/v1/projects/{project}/regions/{region}/subnetworks/{subnetwork}
    * projects/{project}/regions/{region}/subnetworks/{subnetwork}
    * regions/{region}/subnetworks/{subnetwork}



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
