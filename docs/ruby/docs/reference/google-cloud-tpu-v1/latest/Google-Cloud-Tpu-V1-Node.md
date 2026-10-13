---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tpu-v1/latest/Google-Cloud-Tpu-V1-Node/
title: Cloud TPU V1 API - Class Google::Cloud::Tpu::V1::Node (v1.7.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:12:33.611231+00:00
---

# Cloud TPU V1 API - Class Google::Cloud::Tpu::V1::Node (v1.7.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tpu-v1/latest/Google-Cloud-Tpu-V1-Node/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud TPU V1 API - Class Google::Cloud::Tpu::V1::Node (v1.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.1 (latest)  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.7.0  0.6.2  0.5.0  0.4.1  0.3.0  0.2.0  0.1.4 

Reference documentation and code samples for the Cloud TPU V1 API class Google::Cloud::Tpu::V1::Node.

A TPU instance.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #accelerator_type
    
    
    def accelerator_type() -> ::String

**Returns**

  * (::String) — Required. The type of hardware accelerators associated with this node. 



### #accelerator_type=
    
    
    def accelerator_type=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The type of hardware accelerators associated with this node. 



**Returns**

  * (::String) — Required. The type of hardware accelerators associated with this node. 



### #api_version
    
    
    def api_version() -> ::Google::Cloud::Tpu::V1::Node::ApiVersion

**Returns**

  * ([::Google::Cloud::Tpu::V1::Node::ApiVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tpu-v1/latest/Google-Cloud-Tpu-V1-Node-ApiVersion)) — Output only. The API version that created this Node. 



### #cidr_block
    
    
    def cidr_block() -> ::String

**Returns**

  * (::String) — The CIDR block that the TPU node will use when selecting an IP address. This CIDR block must be a /29 block; the Compute Engine networks API forbids a smaller block, and using a larger block would be wasteful (a node can only consume one IP address). Errors will occur if the CIDR block has already been used for a currently existing TPU node, the CIDR block conflicts with any subnetworks in the user's provided network, or the provided network is peered with another network that is using that CIDR block. 



### #cidr_block=
    
    
    def cidr_block=(value) -> ::String

**Parameter**

  * **value** (::String) — The CIDR block that the TPU node will use when selecting an IP address. This CIDR block must be a /29 block; the Compute Engine networks API forbids a smaller block, and using a larger block would be wasteful (a node can only consume one IP address). Errors will occur if the CIDR block has already been used for a currently existing TPU node, the CIDR block conflicts with any subnetworks in the user's provided network, or the provided network is peered with another network that is using that CIDR block. 



**Returns**

  * (::String) — The CIDR block that the TPU node will use when selecting an IP address. This CIDR block must be a /29 block; the Compute Engine networks API forbids a smaller block, and using a larger block would be wasteful (a node can only consume one IP address). Errors will occur if the CIDR block has already been used for a currently existing TPU node, the CIDR block conflicts with any subnetworks in the user's provided network, or the provided network is peered with another network that is using that CIDR block. 



### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tpu-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time when the node was created. 



### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — The user-supplied description of the TPU. Maximum of 512 characters. 



### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) — The user-supplied description of the TPU. Maximum of 512 characters. 



**Returns**

  * (::String) — The user-supplied description of the TPU. Maximum of 512 characters. 



### #health
    
    
    def health() -> ::Google::Cloud::Tpu::V1::Node::Health

**Returns**

  * ([::Google::Cloud::Tpu::V1::Node::Health](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tpu-v1/latest/Google-Cloud-Tpu-V1-Node-Health)) — The health status of the TPU node. 



### #health=
    
    
    def health=(value) -> ::Google::Cloud::Tpu::V1::Node::Health

**Parameter**

  * **value** ([::Google::Cloud::Tpu::V1::Node::Health](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tpu-v1/latest/Google-Cloud-Tpu-V1-Node-Health)) — The health status of the TPU node. 



**Returns**

  * ([::Google::Cloud::Tpu::V1::Node::Health](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tpu-v1/latest/Google-Cloud-Tpu-V1-Node-Health)) — The health status of the TPU node. 



### #health_description
    
    
    def health_description() -> ::String

**Returns**

  * (::String) — Output only. If this field is populated, it contains a description of why the TPU Node is unhealthy. 



### #ip_address
    
    
    def ip_address() -> ::String

**Returns**

  * (::String) — Output only. DEPRECATED! Use network_endpoints instead. The network address for the TPU Node as visible to Compute Engine instances. 



### #ip_address=
    
    
    def ip_address=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. DEPRECATED! Use network_endpoints instead. The network address for the TPU Node as visible to Compute Engine instances. 



**Returns**

  * (::String) — Output only. DEPRECATED! Use network_endpoints instead. The network address for the TPU Node as visible to Compute Engine instances. 



### #labels
    
    
    def labels() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Resource labels to represent user-provided metadata. 



### #labels=
    
    
    def labels=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Resource labels to represent user-provided metadata. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Resource labels to represent user-provided metadata. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Output only. Immutable. The name of the TPU 



### #network
    
    
    def network() -> ::String

**Returns**

  * (::String) — The name of a network they wish to peer the TPU node to. It must be a preexisting Compute Engine network inside of the project on which this API has been activated. If none is provided, "default" will be used. 



### #network=
    
    
    def network=(value) -> ::String

**Parameter**

  * **value** (::String) — The name of a network they wish to peer the TPU node to. It must be a preexisting Compute Engine network inside of the project on which this API has been activated. If none is provided, "default" will be used. 



**Returns**

  * (::String) — The name of a network they wish to peer the TPU node to. It must be a preexisting Compute Engine network inside of the project on which this API has been activated. If none is provided, "default" will be used. 



### #network_endpoints
    
    
    def network_endpoints() -> ::Array<::Google::Cloud::Tpu::V1::NetworkEndpoint>

**Returns**

  * (::Array<[::Google::Cloud::Tpu::V1::NetworkEndpoint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tpu-v1/latest/Google-Cloud-Tpu-V1-NetworkEndpoint)>) — Output only. The network endpoints where TPU workers can be accessed and sent work. It is recommended that Tensorflow clients of the node reach out to the 0th entry in this map first. 



### #port
    
    
    def port() -> ::String

**Returns**

  * (::String) — Output only. DEPRECATED! Use network_endpoints instead. The network port for the TPU Node as visible to Compute Engine instances. 



### #port=
    
    
    def port=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. DEPRECATED! Use network_endpoints instead. The network port for the TPU Node as visible to Compute Engine instances. 



**Returns**

  * (::String) — Output only. DEPRECATED! Use network_endpoints instead. The network port for the TPU Node as visible to Compute Engine instances. 



### #scheduling_config
    
    
    def scheduling_config() -> ::Google::Cloud::Tpu::V1::SchedulingConfig

**Returns**

  * ([::Google::Cloud::Tpu::V1::SchedulingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tpu-v1/latest/Google-Cloud-Tpu-V1-SchedulingConfig)) — The scheduling options for this node. 



### #scheduling_config=
    
    
    def scheduling_config=(value) -> ::Google::Cloud::Tpu::V1::SchedulingConfig

**Parameter**

  * **value** ([::Google::Cloud::Tpu::V1::SchedulingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tpu-v1/latest/Google-Cloud-Tpu-V1-SchedulingConfig)) — The scheduling options for this node. 



**Returns**

  * ([::Google::Cloud::Tpu::V1::SchedulingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tpu-v1/latest/Google-Cloud-Tpu-V1-SchedulingConfig)) — The scheduling options for this node. 



### #service_account
    
    
    def service_account() -> ::String

**Returns**

  * (::String) — Output only. The service account used to run the tensor flow services within the node. To share resources, including Google Cloud Storage data, with the Tensorflow job running in the Node, this account must have permissions to that data. 



### #state
    
    
    def state() -> ::Google::Cloud::Tpu::V1::Node::State

**Returns**

  * ([::Google::Cloud::Tpu::V1::Node::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tpu-v1/latest/Google-Cloud-Tpu-V1-Node-State)) — Output only. The current state for the TPU Node. 



### #symptoms
    
    
    def symptoms() -> ::Array<::Google::Cloud::Tpu::V1::Symptom>

**Returns**

  * (::Array<[::Google::Cloud::Tpu::V1::Symptom](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tpu-v1/latest/Google-Cloud-Tpu-V1-Symptom)>) — Output only. The Symptoms that have occurred to the TPU Node. 



### #tensorflow_version
    
    
    def tensorflow_version() -> ::String

**Returns**

  * (::String) — Required. The version of Tensorflow running in the Node. 



### #tensorflow_version=
    
    
    def tensorflow_version=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The version of Tensorflow running in the Node. 



**Returns**

  * (::String) — Required. The version of Tensorflow running in the Node. 



### #use_service_networking
    
    
    def use_service_networking() -> ::Boolean

**Returns**

  * (::Boolean) — Whether the VPC peering for the node is set up through Service Networking API. The VPC Peering should be set up before provisioning the node. If this field is set, cidr_block field should not be specified. If the network, that you want to peer the TPU Node to, is Shared VPC networks, the node must be created with this this field enabled. 



### #use_service_networking=
    
    
    def use_service_networking=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Whether the VPC peering for the node is set up through Service Networking API. The VPC Peering should be set up before provisioning the node. If this field is set, cidr_block field should not be specified. If the network, that you want to peer the TPU Node to, is Shared VPC networks, the node must be created with this this field enabled. 



**Returns**

  * (::Boolean) — Whether the VPC peering for the node is set up through Service Networking API. The VPC Peering should be set up before provisioning the node. If this field is set, cidr_block field should not be specified. If the network, that you want to peer the TPU Node to, is Shared VPC networks, the node must be created with this this field enabled. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
