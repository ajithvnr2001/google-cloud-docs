---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-VirtualMachineConfig/
title: AI Platform Notebooks V1 API - Class Google::Cloud::Notebooks::V1::VirtualMachineConfig (v1.6.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:43:35.575736+00:00
---

# AI Platform Notebooks V1 API - Class Google::Cloud::Notebooks::V1::VirtualMachineConfig (v1.6.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-VirtualMachineConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  AI Platform Notebooks V1 API - Class Google::Cloud::Notebooks::V1::VirtualMachineConfig (v1.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.6.0 (latest)  1.5.0  1.4.0  1.3.1  1.2.0  1.1.0  1.0.1  0.11.0  0.10.0  0.9.1  0.8.2  0.7.0  0.6.1  0.5.0  0.4.2  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the AI Platform Notebooks V1 API class Google::Cloud::Notebooks::V1::VirtualMachineConfig.

The config settings for virtual machine.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #accelerator_config
    
    
    def accelerator_config() -> ::Google::Cloud::Notebooks::V1::RuntimeAcceleratorConfig

**Returns**

  * ([::Google::Cloud::Notebooks::V1::RuntimeAcceleratorConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-RuntimeAcceleratorConfig)) — Optional. The Compute Engine accelerator configuration for this runtime. 



### #accelerator_config=
    
    
    def accelerator_config=(value) -> ::Google::Cloud::Notebooks::V1::RuntimeAcceleratorConfig

**Parameter**

  * **value** ([::Google::Cloud::Notebooks::V1::RuntimeAcceleratorConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-RuntimeAcceleratorConfig)) — Optional. The Compute Engine accelerator configuration for this runtime. 



**Returns**

  * ([::Google::Cloud::Notebooks::V1::RuntimeAcceleratorConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-RuntimeAcceleratorConfig)) — Optional. The Compute Engine accelerator configuration for this runtime. 



### #boot_image
    
    
    def boot_image() -> ::Google::Cloud::Notebooks::V1::VirtualMachineConfig::BootImage

**Returns**

  * ([::Google::Cloud::Notebooks::V1::VirtualMachineConfig::BootImage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-VirtualMachineConfig-BootImage)) — Optional. Boot image metadata used for runtime upgradeability. 



### #boot_image=
    
    
    def boot_image=(value) -> ::Google::Cloud::Notebooks::V1::VirtualMachineConfig::BootImage

**Parameter**

  * **value** ([::Google::Cloud::Notebooks::V1::VirtualMachineConfig::BootImage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-VirtualMachineConfig-BootImage)) — Optional. Boot image metadata used for runtime upgradeability. 



**Returns**

  * ([::Google::Cloud::Notebooks::V1::VirtualMachineConfig::BootImage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-VirtualMachineConfig-BootImage)) — Optional. Boot image metadata used for runtime upgradeability. 



### #container_images
    
    
    def container_images() -> ::Array<::Google::Cloud::Notebooks::V1::ContainerImage>

**Returns**

  * (::Array<[::Google::Cloud::Notebooks::V1::ContainerImage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-ContainerImage)>) — Optional. Use a list of container images to use as Kernels in the notebook instance. 



### #container_images=
    
    
    def container_images=(value) -> ::Array<::Google::Cloud::Notebooks::V1::ContainerImage>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Notebooks::V1::ContainerImage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-ContainerImage)>) — Optional. Use a list of container images to use as Kernels in the notebook instance. 



**Returns**

  * (::Array<[::Google::Cloud::Notebooks::V1::ContainerImage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-ContainerImage)>) — Optional. Use a list of container images to use as Kernels in the notebook instance. 



### #data_disk
    
    
    def data_disk() -> ::Google::Cloud::Notebooks::V1::LocalDisk

**Returns**

  * ([::Google::Cloud::Notebooks::V1::LocalDisk](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-LocalDisk)) — Required. Data disk option configuration settings. 



### #data_disk=
    
    
    def data_disk=(value) -> ::Google::Cloud::Notebooks::V1::LocalDisk

**Parameter**

  * **value** ([::Google::Cloud::Notebooks::V1::LocalDisk](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-LocalDisk)) — Required. Data disk option configuration settings. 



**Returns**

  * ([::Google::Cloud::Notebooks::V1::LocalDisk](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-LocalDisk)) — Required. Data disk option configuration settings. 



### #encryption_config
    
    
    def encryption_config() -> ::Google::Cloud::Notebooks::V1::EncryptionConfig

**Returns**

  * ([::Google::Cloud::Notebooks::V1::EncryptionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-EncryptionConfig)) — Optional. Encryption settings for virtual machine data disk. 



### #encryption_config=
    
    
    def encryption_config=(value) -> ::Google::Cloud::Notebooks::V1::EncryptionConfig

**Parameter**

  * **value** ([::Google::Cloud::Notebooks::V1::EncryptionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-EncryptionConfig)) — Optional. Encryption settings for virtual machine data disk. 



**Returns**

  * ([::Google::Cloud::Notebooks::V1::EncryptionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-EncryptionConfig)) — Optional. Encryption settings for virtual machine data disk. 



### #guest_attributes
    
    
    def guest_attributes() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Output only. The Compute Engine guest attributes. (see [Project and instance guest attributes](https://cloud.google.com/compute/docs/storing-retrieving-metadata#guest_attributes)). 



### #internal_ip_only
    
    
    def internal_ip_only() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. If true, runtime will only have internal IP addresses. By default, runtimes are not restricted to internal IP addresses, and will have ephemeral external IP addresses assigned to each vm. This `internal_ip_only` restriction can only be enabled for subnetwork enabled networks, and all dependencies must be configured to be accessible without external IP addresses. 



### #internal_ip_only=
    
    
    def internal_ip_only=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. If true, runtime will only have internal IP addresses. By default, runtimes are not restricted to internal IP addresses, and will have ephemeral external IP addresses assigned to each vm. This `internal_ip_only` restriction can only be enabled for subnetwork enabled networks, and all dependencies must be configured to be accessible without external IP addresses. 



**Returns**

  * (::Boolean) — Optional. If true, runtime will only have internal IP addresses. By default, runtimes are not restricted to internal IP addresses, and will have ephemeral external IP addresses assigned to each vm. This `internal_ip_only` restriction can only be enabled for subnetwork enabled networks, and all dependencies must be configured to be accessible without external IP addresses. 



### #labels
    
    
    def labels() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. The labels to associate with this runtime. Label **keys** must contain 1 to 63 characters, and must conform to [RFC 1035](https://www.ietf.org/rfc/rfc1035.txt). Label **values** may be empty, but, if present, must contain 1 to 63 characters, and must conform to [RFC 1035](https://www.ietf.org/rfc/rfc1035.txt). No more than 32 labels can be associated with a cluster. 



### #labels=
    
    
    def labels=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Optional. The labels to associate with this runtime. Label **keys** must contain 1 to 63 characters, and must conform to [RFC 1035](https://www.ietf.org/rfc/rfc1035.txt). Label **values** may be empty, but, if present, must contain 1 to 63 characters, and must conform to [RFC 1035](https://www.ietf.org/rfc/rfc1035.txt). No more than 32 labels can be associated with a cluster. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. The labels to associate with this runtime. Label **keys** must contain 1 to 63 characters, and must conform to [RFC 1035](https://www.ietf.org/rfc/rfc1035.txt). Label **values** may be empty, but, if present, must contain 1 to 63 characters, and must conform to [RFC 1035](https://www.ietf.org/rfc/rfc1035.txt). No more than 32 labels can be associated with a cluster. 



### #machine_type
    
    
    def machine_type() -> ::String

**Returns**

  * (::String) — 

Required. The Compute Engine machine type used for runtimes. Short name is valid. Examples:

    * `n1-standard-2`
    * `e2-standard-8`



### #machine_type=
    
    
    def machine_type=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Required. The Compute Engine machine type used for runtimes. Short name is valid. Examples:

    * `n1-standard-2`
    * `e2-standard-8`



**Returns**

  * (::String) — 

Required. The Compute Engine machine type used for runtimes. Short name is valid. Examples:

    * `n1-standard-2`
    * `e2-standard-8`



### #metadata
    
    
    def metadata() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. The Compute Engine metadata entries to add to virtual machine. (see [Project and instance metadata](https://cloud.google.com/compute/docs/storing-retrieving-metadata#project_and_instance_metadata)). 



### #metadata=
    
    
    def metadata=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Optional. The Compute Engine metadata entries to add to virtual machine. (see [Project and instance metadata](https://cloud.google.com/compute/docs/storing-retrieving-metadata#project_and_instance_metadata)). 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. The Compute Engine metadata entries to add to virtual machine. (see [Project and instance metadata](https://cloud.google.com/compute/docs/storing-retrieving-metadata#project_and_instance_metadata)). 



### #network
    
    
    def network() -> ::String

**Returns**

  * (::String) — 

Optional. The Compute Engine network to be used for machine communications. Cannot be specified with subnetwork. If neither `network` nor `subnet` is specified, the "default" network of the project is used, if it exists.

A full URL or partial URI. Examples:

    * `https://www.googleapis.com/compute/v1/projects/[project_id]/global/networks/default`
    * `projects/[project_id]/global/networks/default`

Runtimes are managed resources inside Google Infrastructure. Runtimes support the following network configurations:

    * Google Managed Network (Network & subnet are empty)
    * Consumer Project VPC (network & subnet are required). Requires configuring Private Service Access.
    * Shared VPC (network & subnet are required). Requires configuring Private Service Access.



### #network=
    
    
    def network=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Optional. The Compute Engine network to be used for machine communications. Cannot be specified with subnetwork. If neither `network` nor `subnet` is specified, the "default" network of the project is used, if it exists.

A full URL or partial URI. Examples:

    * `https://www.googleapis.com/compute/v1/projects/[project_id]/global/networks/default`
    * `projects/[project_id]/global/networks/default`

Runtimes are managed resources inside Google Infrastructure. Runtimes support the following network configurations:

    * Google Managed Network (Network & subnet are empty)
    * Consumer Project VPC (network & subnet are required). Requires configuring Private Service Access.
    * Shared VPC (network & subnet are required). Requires configuring Private Service Access.



**Returns**

  * (::String) — 

Optional. The Compute Engine network to be used for machine communications. Cannot be specified with subnetwork. If neither `network` nor `subnet` is specified, the "default" network of the project is used, if it exists.

A full URL or partial URI. Examples:

    * `https://www.googleapis.com/compute/v1/projects/[project_id]/global/networks/default`
    * `projects/[project_id]/global/networks/default`

Runtimes are managed resources inside Google Infrastructure. Runtimes support the following network configurations:

    * Google Managed Network (Network & subnet are empty)
    * Consumer Project VPC (network & subnet are required). Requires configuring Private Service Access.
    * Shared VPC (network & subnet are required). Requires configuring Private Service Access.



### #nic_type
    
    
    def nic_type() -> ::Google::Cloud::Notebooks::V1::VirtualMachineConfig::NicType

**Returns**

  * ([::Google::Cloud::Notebooks::V1::VirtualMachineConfig::NicType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-VirtualMachineConfig-NicType)) — Optional. The type of vNIC to be used on this interface. This may be gVNIC or VirtioNet. 



### #nic_type=
    
    
    def nic_type=(value) -> ::Google::Cloud::Notebooks::V1::VirtualMachineConfig::NicType

**Parameter**

  * **value** ([::Google::Cloud::Notebooks::V1::VirtualMachineConfig::NicType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-VirtualMachineConfig-NicType)) — Optional. The type of vNIC to be used on this interface. This may be gVNIC or VirtioNet. 



**Returns**

  * ([::Google::Cloud::Notebooks::V1::VirtualMachineConfig::NicType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-VirtualMachineConfig-NicType)) — Optional. The type of vNIC to be used on this interface. This may be gVNIC or VirtioNet. 



### #reserved_ip_range
    
    
    def reserved_ip_range() -> ::String

**Returns**

  * (::String) — Optional. Reserved IP Range name is used for VPC Peering. The subnetwork allocation will use the range _name_ if it's assigned.

Example: managed-notebooks-range-c
        
        PEERING_RANGE_NAME_3=managed-notebooks-range-c
        gcloud compute addresses create $PEERING_RANGE_NAME_3 \
          --global \
          --prefix-length=24 \
          --description="Google Cloud Managed Notebooks Range 24 c" \
          --network=$NETWORK \
          --addresses=192.168.0.0 \
          --purpose=VPC_PEERING
        

Field value will be: `managed-notebooks-range-c`




### #reserved_ip_range=
    
    
    def reserved_ip_range=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Reserved IP Range name is used for VPC Peering. The subnetwork allocation will use the range _name_ if it's assigned.

Example: managed-notebooks-range-c
        
        PEERING_RANGE_NAME_3=managed-notebooks-range-c
        gcloud compute addresses create $PEERING_RANGE_NAME_3 \
          --global \
          --prefix-length=24 \
          --description="Google Cloud Managed Notebooks Range 24 c" \
          --network=$NETWORK \
          --addresses=192.168.0.0 \
          --purpose=VPC_PEERING
        

Field value will be: `managed-notebooks-range-c`




**Returns**

  * (::String) — Optional. Reserved IP Range name is used for VPC Peering. The subnetwork allocation will use the range _name_ if it's assigned.

Example: managed-notebooks-range-c
        
        PEERING_RANGE_NAME_3=managed-notebooks-range-c
        gcloud compute addresses create $PEERING_RANGE_NAME_3 \
          --global \
          --prefix-length=24 \
          --description="Google Cloud Managed Notebooks Range 24 c" \
          --network=$NETWORK \
          --addresses=192.168.0.0 \
          --purpose=VPC_PEERING
        

Field value will be: `managed-notebooks-range-c`




### #shielded_instance_config
    
    
    def shielded_instance_config() -> ::Google::Cloud::Notebooks::V1::RuntimeShieldedInstanceConfig

**Returns**

  * ([::Google::Cloud::Notebooks::V1::RuntimeShieldedInstanceConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-RuntimeShieldedInstanceConfig)) — Optional. Shielded VM Instance configuration settings. 



### #shielded_instance_config=
    
    
    def shielded_instance_config=(value) -> ::Google::Cloud::Notebooks::V1::RuntimeShieldedInstanceConfig

**Parameter**

  * **value** ([::Google::Cloud::Notebooks::V1::RuntimeShieldedInstanceConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-RuntimeShieldedInstanceConfig)) — Optional. Shielded VM Instance configuration settings. 



**Returns**

  * ([::Google::Cloud::Notebooks::V1::RuntimeShieldedInstanceConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-RuntimeShieldedInstanceConfig)) — Optional. Shielded VM Instance configuration settings. 



### #subnet
    
    
    def subnet() -> ::String

**Returns**

  * (::String) — 

Optional. The Compute Engine subnetwork to be used for machine communications. Cannot be specified with network.

A full URL or partial URI are valid. Examples:

    * `https://www.googleapis.com/compute/v1/projects/[project_id]/regions/us-east1/subnetworks/sub0`
    * `projects/[project_id]/regions/us-east1/subnetworks/sub0`



### #subnet=
    
    
    def subnet=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Optional. The Compute Engine subnetwork to be used for machine communications. Cannot be specified with network.

A full URL or partial URI are valid. Examples:

    * `https://www.googleapis.com/compute/v1/projects/[project_id]/regions/us-east1/subnetworks/sub0`
    * `projects/[project_id]/regions/us-east1/subnetworks/sub0`



**Returns**

  * (::String) — 

Optional. The Compute Engine subnetwork to be used for machine communications. Cannot be specified with network.

A full URL or partial URI are valid. Examples:

    * `https://www.googleapis.com/compute/v1/projects/[project_id]/regions/us-east1/subnetworks/sub0`
    * `projects/[project_id]/regions/us-east1/subnetworks/sub0`



### #tags
    
    
    def tags() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Optional. The Compute Engine tags to add to runtime (see [Tagging instances](https://cloud.google.com/compute/docs/label-or-tag-resources#tags)). 



### #tags=
    
    
    def tags=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Optional. The Compute Engine tags to add to runtime (see [Tagging instances](https://cloud.google.com/compute/docs/label-or-tag-resources#tags)). 



**Returns**

  * (::Array<::String>) — Optional. The Compute Engine tags to add to runtime (see [Tagging instances](https://cloud.google.com/compute/docs/label-or-tag-resources#tags)). 



### #zone
    
    
    def zone() -> ::String

**Returns**

  * (::String) — 

Output only. The zone where the virtual machine is located. If using regional request, the notebooks service will pick a location in the corresponding runtime region. On a get request, zone will always be present. Example:

    * `us-central1-b`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
