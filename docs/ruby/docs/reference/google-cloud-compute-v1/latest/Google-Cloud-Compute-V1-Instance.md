---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Instance/
title: Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::Instance (v4.0.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:25:20.122908+00:00
---

# Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::Instance (v4.0.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::Instance (v4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.12.0  3.10.0  3.9.1  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.22.0  2.21.1  2.20.0  2.19.1  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.2  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.5.0 

Reference documentation and code samples for the Google Cloud Compute V1 API class Google::Cloud::Compute::V1::Instance.

Represents an Instance resource.

An instance is a virtual machine that is hosted on Google Cloud Platform. For more information, readVirtual Machine Instances.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #advanced_machine_features
    
    
    def advanced_machine_features() -> ::Google::Cloud::Compute::V1::AdvancedMachineFeatures

**Returns**

  * ([::Google::Cloud::Compute::V1::AdvancedMachineFeatures](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AdvancedMachineFeatures)) — Controls for advanced machine-related behavior features. 



### #advanced_machine_features=
    
    
    def advanced_machine_features=(value) -> ::Google::Cloud::Compute::V1::AdvancedMachineFeatures

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::AdvancedMachineFeatures](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AdvancedMachineFeatures)) — Controls for advanced machine-related behavior features. 



**Returns**

  * ([::Google::Cloud::Compute::V1::AdvancedMachineFeatures](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AdvancedMachineFeatures)) — Controls for advanced machine-related behavior features. 



### #can_ip_forward
    
    
    def can_ip_forward() -> ::Boolean

**Returns**

  * (::Boolean) — Allows this instance to send and receive packets with non-matching destination or source IPs. This is required if you plan to use this instance to forward routes. For more information, seeEnabling IP Forwarding. 



### #can_ip_forward=
    
    
    def can_ip_forward=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Allows this instance to send and receive packets with non-matching destination or source IPs. This is required if you plan to use this instance to forward routes. For more information, seeEnabling IP Forwarding. 



**Returns**

  * (::Boolean) — Allows this instance to send and receive packets with non-matching destination or source IPs. This is required if you plan to use this instance to forward routes. For more information, seeEnabling IP Forwarding. 



### #confidential_instance_config
    
    
    def confidential_instance_config() -> ::Google::Cloud::Compute::V1::ConfidentialInstanceConfig

**Returns**

  * ([::Google::Cloud::Compute::V1::ConfidentialInstanceConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ConfidentialInstanceConfig)) 



### #confidential_instance_config=
    
    
    def confidential_instance_config=(value) -> ::Google::Cloud::Compute::V1::ConfidentialInstanceConfig

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::ConfidentialInstanceConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ConfidentialInstanceConfig)) 



**Returns**

  * ([::Google::Cloud::Compute::V1::ConfidentialInstanceConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ConfidentialInstanceConfig)) 



### #cpu_platform
    
    
    def cpu_platform() -> ::String

**Returns**

  * (::String) — Output only. [Output Only] The CPU platform used by this instance. 



### #cpu_platform=
    
    
    def cpu_platform=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. [Output Only] The CPU platform used by this instance. 



**Returns**

  * (::String) — Output only. [Output Only] The CPU platform used by this instance. 



### #creation_timestamp
    
    
    def creation_timestamp() -> ::String

**Returns**

  * (::String) — Output only. [Output Only] Creation timestamp inRFC3339 text format. 



### #creation_timestamp=
    
    
    def creation_timestamp=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. [Output Only] Creation timestamp inRFC3339 text format. 



**Returns**

  * (::String) — Output only. [Output Only] Creation timestamp inRFC3339 text format. 



### #deletion_protection
    
    
    def deletion_protection() -> ::Boolean

**Returns**

  * (::Boolean) — Whether the resource should be protected against deletion. 



### #deletion_protection=
    
    
    def deletion_protection=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Whether the resource should be protected against deletion. 



**Returns**

  * (::Boolean) — Whether the resource should be protected against deletion. 



### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — An optional description of this resource. Provide this property when you create the resource. 



### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) — An optional description of this resource. Provide this property when you create the resource. 



**Returns**

  * (::String) — An optional description of this resource. Provide this property when you create the resource. 



### #disks
    
    
    def disks() -> ::Array<::Google::Cloud::Compute::V1::AttachedDisk>

**Returns**

  * (::Array<[::Google::Cloud::Compute::V1::AttachedDisk](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AttachedDisk)>) — Array of disks associated with this instance. Persistent disks must be created before you can assign them. 



### #disks=
    
    
    def disks=(value) -> ::Array<::Google::Cloud::Compute::V1::AttachedDisk>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Compute::V1::AttachedDisk](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AttachedDisk)>) — Array of disks associated with this instance. Persistent disks must be created before you can assign them. 



**Returns**

  * (::Array<[::Google::Cloud::Compute::V1::AttachedDisk](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AttachedDisk)>) — Array of disks associated with this instance. Persistent disks must be created before you can assign them. 



### #display_device
    
    
    def display_device() -> ::Google::Cloud::Compute::V1::DisplayDevice

**Returns**

  * ([::Google::Cloud::Compute::V1::DisplayDevice](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-DisplayDevice)) — Enables display device for the instance. 



### #display_device=
    
    
    def display_device=(value) -> ::Google::Cloud::Compute::V1::DisplayDevice

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::DisplayDevice](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-DisplayDevice)) — Enables display device for the instance. 



**Returns**

  * ([::Google::Cloud::Compute::V1::DisplayDevice](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-DisplayDevice)) — Enables display device for the instance. 



### #fingerprint
    
    
    def fingerprint() -> ::String

**Returns**

  * (::String) — Specifies a fingerprint for this resource, which is essentially a hash of the instance's contents and used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update the instance. You must always provide an up-to-date fingerprint hash in order to update the instance.

To see the latest fingerprint, make get() request to the instance. 




### #fingerprint=
    
    
    def fingerprint=(value) -> ::String

**Parameter**

  * **value** (::String) — Specifies a fingerprint for this resource, which is essentially a hash of the instance's contents and used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update the instance. You must always provide an up-to-date fingerprint hash in order to update the instance.

To see the latest fingerprint, make get() request to the instance. 




**Returns**

  * (::String) — Specifies a fingerprint for this resource, which is essentially a hash of the instance's contents and used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update the instance. You must always provide an up-to-date fingerprint hash in order to update the instance.

To see the latest fingerprint, make get() request to the instance. 




### #guest_accelerators
    
    
    def guest_accelerators() -> ::Array<::Google::Cloud::Compute::V1::AcceleratorConfig>

**Returns**

  * (::Array<[::Google::Cloud::Compute::V1::AcceleratorConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AcceleratorConfig)>) — A list of the type and count of accelerator cards attached to the instance. 



### #guest_accelerators=
    
    
    def guest_accelerators=(value) -> ::Array<::Google::Cloud::Compute::V1::AcceleratorConfig>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Compute::V1::AcceleratorConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AcceleratorConfig)>) — A list of the type and count of accelerator cards attached to the instance. 



**Returns**

  * (::Array<[::Google::Cloud::Compute::V1::AcceleratorConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AcceleratorConfig)>) — A list of the type and count of accelerator cards attached to the instance. 



### #hostname
    
    
    def hostname() -> ::String

**Returns**

  * (::String) — Specifies the hostname of the instance. The specified hostname must be RFC1035 compliant. If hostname is not specified, the default hostname is [INSTANCE_NAME].c.[PROJECT_ID].internal when using the global DNS, and [INSTANCE_NAME].[ZONE].c.[PROJECT_ID].internal when using zonal DNS. 



### #hostname=
    
    
    def hostname=(value) -> ::String

**Parameter**

  * **value** (::String) — Specifies the hostname of the instance. The specified hostname must be RFC1035 compliant. If hostname is not specified, the default hostname is [INSTANCE_NAME].c.[PROJECT_ID].internal when using the global DNS, and [INSTANCE_NAME].[ZONE].c.[PROJECT_ID].internal when using zonal DNS. 



**Returns**

  * (::String) — Specifies the hostname of the instance. The specified hostname must be RFC1035 compliant. If hostname is not specified, the default hostname is [INSTANCE_NAME].c.[PROJECT_ID].internal when using the global DNS, and [INSTANCE_NAME].[ZONE].c.[PROJECT_ID].internal when using zonal DNS. 



### #id
    
    
    def id() -> ::Integer

**Returns**

  * (::Integer) — Output only. [Output Only] The unique identifier for the resource. This identifier is defined by the server. 



### #id=
    
    
    def id=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Output only. [Output Only] The unique identifier for the resource. This identifier is defined by the server. 



**Returns**

  * (::Integer) — Output only. [Output Only] The unique identifier for the resource. This identifier is defined by the server. 



### #instance_encryption_key
    
    
    def instance_encryption_key() -> ::Google::Cloud::Compute::V1::CustomerEncryptionKey

**Returns**

  * ([::Google::Cloud::Compute::V1::CustomerEncryptionKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-CustomerEncryptionKey)) — Encrypts suspended data for an instance with acustomer-managed encryption key.

If you are creating a new instance, this field will encrypt the local SSD and in-memory contents of the instance during the suspend operation.

If you do not provide an encryption key when creating the instance, then the local SSD and in-memory contents will be encrypted using an automatically generated key during the suspend operation. 




### #instance_encryption_key=
    
    
    def instance_encryption_key=(value) -> ::Google::Cloud::Compute::V1::CustomerEncryptionKey

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::CustomerEncryptionKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-CustomerEncryptionKey)) — Encrypts suspended data for an instance with acustomer-managed encryption key.

If you are creating a new instance, this field will encrypt the local SSD and in-memory contents of the instance during the suspend operation.

If you do not provide an encryption key when creating the instance, then the local SSD and in-memory contents will be encrypted using an automatically generated key during the suspend operation. 




**Returns**

  * ([::Google::Cloud::Compute::V1::CustomerEncryptionKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-CustomerEncryptionKey)) — Encrypts suspended data for an instance with acustomer-managed encryption key.

If you are creating a new instance, this field will encrypt the local SSD and in-memory contents of the instance during the suspend operation.

If you do not provide an encryption key when creating the instance, then the local SSD and in-memory contents will be encrypted using an automatically generated key during the suspend operation. 




### #key_revocation_action_type
    
    
    def key_revocation_action_type() -> ::String

**Returns**

  * (::String) — KeyRevocationActionType of the instance. Supported options are "STOP" and "NONE". The default value is "NONE" if it is not specified. Check the KeyRevocationActionType enum for the list of possible values. 



### #key_revocation_action_type=
    
    
    def key_revocation_action_type=(value) -> ::String

**Parameter**

  * **value** (::String) — KeyRevocationActionType of the instance. Supported options are "STOP" and "NONE". The default value is "NONE" if it is not specified. Check the KeyRevocationActionType enum for the list of possible values. 



**Returns**

  * (::String) — KeyRevocationActionType of the instance. Supported options are "STOP" and "NONE". The default value is "NONE" if it is not specified. Check the KeyRevocationActionType enum for the list of possible values. 



### #kind
    
    
    def kind() -> ::String

**Returns**

  * (::String) — Output only. [Output Only] Type of the resource. Always compute#instance for instances. 



### #kind=
    
    
    def kind=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. [Output Only] Type of the resource. Always compute#instance for instances. 



**Returns**

  * (::String) — Output only. [Output Only] Type of the resource. Always compute#instance for instances. 



### #label_fingerprint
    
    
    def label_fingerprint() -> ::String

**Returns**

  * (::String) — A fingerprint for this request, which is essentially a hash of the label's contents and used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update labels. You must always provide an up-to-date fingerprint hash in order to update or change labels.

To see the latest fingerprint, make get() request to the instance. 




### #label_fingerprint=
    
    
    def label_fingerprint=(value) -> ::String

**Parameter**

  * **value** (::String) — A fingerprint for this request, which is essentially a hash of the label's contents and used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update labels. You must always provide an up-to-date fingerprint hash in order to update or change labels.

To see the latest fingerprint, make get() request to the instance. 




**Returns**

  * (::String) — A fingerprint for this request, which is essentially a hash of the label's contents and used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update labels. You must always provide an up-to-date fingerprint hash in order to update or change labels.

To see the latest fingerprint, make get() request to the instance. 




### #labels
    
    
    def labels() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Labels to apply to this instance. These can be later modified by the setLabels method. 



### #labels=
    
    
    def labels=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Labels to apply to this instance. These can be later modified by the setLabels method. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Labels to apply to this instance. These can be later modified by the setLabels method. 



### #last_start_timestamp
    
    
    def last_start_timestamp() -> ::String

**Returns**

  * (::String) — Output only. [Output Only] Last start timestamp inRFC3339 text format. 



### #last_start_timestamp=
    
    
    def last_start_timestamp=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. [Output Only] Last start timestamp inRFC3339 text format. 



**Returns**

  * (::String) — Output only. [Output Only] Last start timestamp inRFC3339 text format. 



### #last_stop_timestamp
    
    
    def last_stop_timestamp() -> ::String

**Returns**

  * (::String) — Output only. [Output Only] Last stop timestamp inRFC3339 text format. 



### #last_stop_timestamp=
    
    
    def last_stop_timestamp=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. [Output Only] Last stop timestamp inRFC3339 text format. 



**Returns**

  * (::String) — Output only. [Output Only] Last stop timestamp inRFC3339 text format. 



### #last_suspended_timestamp
    
    
    def last_suspended_timestamp() -> ::String

**Returns**

  * (::String) — Output only. [Output Only] Last suspended timestamp inRFC3339 text format. 



### #last_suspended_timestamp=
    
    
    def last_suspended_timestamp=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. [Output Only] Last suspended timestamp inRFC3339 text format. 



**Returns**

  * (::String) — Output only. [Output Only] Last suspended timestamp inRFC3339 text format. 



### #local_ssd_encryption_mode
    
    
    def local_ssd_encryption_mode() -> ::String

**Returns**

  * (::String) — Specifies which method should be used for encrypting the Local SSDs attached to the VM. Check the LocalSsdEncryptionMode enum for the list of possible values. 



### #local_ssd_encryption_mode=
    
    
    def local_ssd_encryption_mode=(value) -> ::String

**Parameter**

  * **value** (::String) — Specifies which method should be used for encrypting the Local SSDs attached to the VM. Check the LocalSsdEncryptionMode enum for the list of possible values. 



**Returns**

  * (::String) — Specifies which method should be used for encrypting the Local SSDs attached to the VM. Check the LocalSsdEncryptionMode enum for the list of possible values. 



### #machine_type
    
    
    def machine_type() -> ::String

**Returns**

  * (::String) — Full or partial URL of the machine type resource to use for this instance, in the format:zones/zone/machineTypes/machine-type. This is provided by the client when the instance is created. For example, the following is a valid partial url to a predefined machine type:

zones/us-central1-f/machineTypes/n1-standard-1

To create acustom machine type, provide a URL to a machine type in the following format, where CPUS is 1 or an even number up to 32 (2, 4, 6, ... 24, etc), and MEMORY is the total memory for this instance. Memory must be a multiple of 256 MB and must be supplied in MB (e.g. 5 GB of memory is 5120 MB):

zones/zone/machineTypes/custom-CPUS-MEMORY

For example: zones/us-central1-f/machineTypes/custom-4-5120

For a full list of restrictions, read theSpecifications for custom machine types. 




### #machine_type=
    
    
    def machine_type=(value) -> ::String

**Parameter**

  * **value** (::String) — Full or partial URL of the machine type resource to use for this instance, in the format:zones/zone/machineTypes/machine-type. This is provided by the client when the instance is created. For example, the following is a valid partial url to a predefined machine type:

zones/us-central1-f/machineTypes/n1-standard-1

To create acustom machine type, provide a URL to a machine type in the following format, where CPUS is 1 or an even number up to 32 (2, 4, 6, ... 24, etc), and MEMORY is the total memory for this instance. Memory must be a multiple of 256 MB and must be supplied in MB (e.g. 5 GB of memory is 5120 MB):

zones/zone/machineTypes/custom-CPUS-MEMORY

For example: zones/us-central1-f/machineTypes/custom-4-5120

For a full list of restrictions, read theSpecifications for custom machine types. 




**Returns**

  * (::String) — Full or partial URL of the machine type resource to use for this instance, in the format:zones/zone/machineTypes/machine-type. This is provided by the client when the instance is created. For example, the following is a valid partial url to a predefined machine type:

zones/us-central1-f/machineTypes/n1-standard-1

To create acustom machine type, provide a URL to a machine type in the following format, where CPUS is 1 or an even number up to 32 (2, 4, 6, ... 24, etc), and MEMORY is the total memory for this instance. Memory must be a multiple of 256 MB and must be supplied in MB (e.g. 5 GB of memory is 5120 MB):

zones/zone/machineTypes/custom-CPUS-MEMORY

For example: zones/us-central1-f/machineTypes/custom-4-5120

For a full list of restrictions, read theSpecifications for custom machine types. 




### #metadata
    
    
    def metadata() -> ::Google::Cloud::Compute::V1::Metadata

**Returns**

  * ([::Google::Cloud::Compute::V1::Metadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Metadata)) — The metadata key/value pairs assigned to this instance. This includes metadata keys that were explicitly defined for the instance. 



### #metadata=
    
    
    def metadata=(value) -> ::Google::Cloud::Compute::V1::Metadata

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::Metadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Metadata)) — The metadata key/value pairs assigned to this instance. This includes metadata keys that were explicitly defined for the instance. 



**Returns**

  * ([::Google::Cloud::Compute::V1::Metadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Metadata)) — The metadata key/value pairs assigned to this instance. This includes metadata keys that were explicitly defined for the instance. 



### #min_cpu_platform
    
    
    def min_cpu_platform() -> ::String

**Returns**

  * (::String) — Specifies aminimum CPU platform for the VM instance. Applicable values are the friendly names of CPU platforms, such as minCpuPlatform: "Intel Haswell" or minCpuPlatform: "Intel Sandy Bridge". 



### #min_cpu_platform=
    
    
    def min_cpu_platform=(value) -> ::String

**Parameter**

  * **value** (::String) — Specifies aminimum CPU platform for the VM instance. Applicable values are the friendly names of CPU platforms, such as minCpuPlatform: "Intel Haswell" or minCpuPlatform: "Intel Sandy Bridge". 



**Returns**

  * (::String) — Specifies aminimum CPU platform for the VM instance. Applicable values are the friendly names of CPU platforms, such as minCpuPlatform: "Intel Haswell" or minCpuPlatform: "Intel Sandy Bridge". 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — The name of the resource, provided by the client when initially creating the resource. The resource name must be 1-63 characters long, and comply withRFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — The name of the resource, provided by the client when initially creating the resource. The resource name must be 1-63 characters long, and comply withRFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. 



**Returns**

  * (::String) — The name of the resource, provided by the client when initially creating the resource. The resource name must be 1-63 characters long, and comply withRFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. 



### #network_interfaces
    
    
    def network_interfaces() -> ::Array<::Google::Cloud::Compute::V1::NetworkInterface>

**Returns**

  * (::Array<[::Google::Cloud::Compute::V1::NetworkInterface](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-NetworkInterface)>) — An array of network configurations for this instance. These specify how interfaces are configured to interact with other network services, such as connecting to the internet. Multiple interfaces are supported per instance. 



### #network_interfaces=
    
    
    def network_interfaces=(value) -> ::Array<::Google::Cloud::Compute::V1::NetworkInterface>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Compute::V1::NetworkInterface](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-NetworkInterface)>) — An array of network configurations for this instance. These specify how interfaces are configured to interact with other network services, such as connecting to the internet. Multiple interfaces are supported per instance. 



**Returns**

  * (::Array<[::Google::Cloud::Compute::V1::NetworkInterface](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-NetworkInterface)>) — An array of network configurations for this instance. These specify how interfaces are configured to interact with other network services, such as connecting to the internet. Multiple interfaces are supported per instance. 



### #network_performance_config
    
    
    def network_performance_config() -> ::Google::Cloud::Compute::V1::NetworkPerformanceConfig

**Returns**

  * ([::Google::Cloud::Compute::V1::NetworkPerformanceConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-NetworkPerformanceConfig)) 



### #network_performance_config=
    
    
    def network_performance_config=(value) -> ::Google::Cloud::Compute::V1::NetworkPerformanceConfig

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::NetworkPerformanceConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-NetworkPerformanceConfig)) 



**Returns**

  * ([::Google::Cloud::Compute::V1::NetworkPerformanceConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-NetworkPerformanceConfig)) 



### #params
    
    
    def params() -> ::Google::Cloud::Compute::V1::InstanceParams

**Returns**

  * ([::Google::Cloud::Compute::V1::InstanceParams](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InstanceParams)) — Input only. [Input Only] Additional params passed with the request, but not persisted as part of resource payload. 



### #params=
    
    
    def params=(value) -> ::Google::Cloud::Compute::V1::InstanceParams

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::InstanceParams](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InstanceParams)) — Input only. [Input Only] Additional params passed with the request, but not persisted as part of resource payload. 



**Returns**

  * ([::Google::Cloud::Compute::V1::InstanceParams](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InstanceParams)) — Input only. [Input Only] Additional params passed with the request, but not persisted as part of resource payload. 



### #private_ipv6_google_access
    
    
    def private_ipv6_google_access() -> ::String

**Returns**

  * (::String) — The private IPv6 google access type for the VM. If not specified, use INHERIT_FROM_SUBNETWORK as default. Check the PrivateIpv6GoogleAccess enum for the list of possible values. 



### #private_ipv6_google_access=
    
    
    def private_ipv6_google_access=(value) -> ::String

**Parameter**

  * **value** (::String) — The private IPv6 google access type for the VM. If not specified, use INHERIT_FROM_SUBNETWORK as default. Check the PrivateIpv6GoogleAccess enum for the list of possible values. 



**Returns**

  * (::String) — The private IPv6 google access type for the VM. If not specified, use INHERIT_FROM_SUBNETWORK as default. Check the PrivateIpv6GoogleAccess enum for the list of possible values. 



### #reservation_affinity
    
    
    def reservation_affinity() -> ::Google::Cloud::Compute::V1::ReservationAffinity

**Returns**

  * ([::Google::Cloud::Compute::V1::ReservationAffinity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ReservationAffinity)) — Specifies the reservations that this instance can consume from. 



### #reservation_affinity=
    
    
    def reservation_affinity=(value) -> ::Google::Cloud::Compute::V1::ReservationAffinity

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::ReservationAffinity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ReservationAffinity)) — Specifies the reservations that this instance can consume from. 



**Returns**

  * ([::Google::Cloud::Compute::V1::ReservationAffinity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ReservationAffinity)) — Specifies the reservations that this instance can consume from. 



### #resource_policies
    
    
    def resource_policies() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Resource policies applied to this instance. 



### #resource_policies=
    
    
    def resource_policies=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Resource policies applied to this instance. 



**Returns**

  * (::Array<::String>) — Resource policies applied to this instance. 



### #resource_status
    
    
    def resource_status() -> ::Google::Cloud::Compute::V1::ResourceStatus

**Returns**

  * ([::Google::Cloud::Compute::V1::ResourceStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ResourceStatus)) — Output only. [Output Only] Specifies values set for instance attributes as compared to the values requested by user in the corresponding input only field. 



### #resource_status=
    
    
    def resource_status=(value) -> ::Google::Cloud::Compute::V1::ResourceStatus

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::ResourceStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ResourceStatus)) — Output only. [Output Only] Specifies values set for instance attributes as compared to the values requested by user in the corresponding input only field. 



**Returns**

  * ([::Google::Cloud::Compute::V1::ResourceStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ResourceStatus)) — Output only. [Output Only] Specifies values set for instance attributes as compared to the values requested by user in the corresponding input only field. 



### #satisfies_pzi
    
    
    def satisfies_pzi() -> ::Boolean

**Returns**

  * (::Boolean) — Output only. [Output Only] Reserved for future use. 



### #satisfies_pzi=
    
    
    def satisfies_pzi=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Output only. [Output Only] Reserved for future use. 



**Returns**

  * (::Boolean) — Output only. [Output Only] Reserved for future use. 



### #satisfies_pzs
    
    
    def satisfies_pzs() -> ::Boolean

**Returns**

  * (::Boolean) — Output only. [Output Only] Reserved for future use. 



### #satisfies_pzs=
    
    
    def satisfies_pzs=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Output only. [Output Only] Reserved for future use. 



**Returns**

  * (::Boolean) — Output only. [Output Only] Reserved for future use. 



### #scheduling
    
    
    def scheduling() -> ::Google::Cloud::Compute::V1::Scheduling

**Returns**

  * ([::Google::Cloud::Compute::V1::Scheduling](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Scheduling)) — Sets the scheduling options for this instance. 



### #scheduling=
    
    
    def scheduling=(value) -> ::Google::Cloud::Compute::V1::Scheduling

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::Scheduling](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Scheduling)) — Sets the scheduling options for this instance. 



**Returns**

  * ([::Google::Cloud::Compute::V1::Scheduling](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Scheduling)) — Sets the scheduling options for this instance. 



### #self_link
    
    
    def self_link() -> ::String

**Returns**

  * (::String) — Output only. [Output Only] Server-defined URL for this resource. 



### #self_link=
    
    
    def self_link=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. [Output Only] Server-defined URL for this resource. 



**Returns**

  * (::String) — Output only. [Output Only] Server-defined URL for this resource. 



### #service_accounts
    
    
    def service_accounts() -> ::Array<::Google::Cloud::Compute::V1::ServiceAccount>

**Returns**

  * (::Array<[::Google::Cloud::Compute::V1::ServiceAccount](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ServiceAccount)>) — A list of service accounts, with their specified scopes, authorized for this instance. Only one service account per VM instance is supported.

Service accounts generate access tokens that can be accessed through the metadata server and used to authenticate applications on the instance. SeeService Accounts for more information. 




### #service_accounts=
    
    
    def service_accounts=(value) -> ::Array<::Google::Cloud::Compute::V1::ServiceAccount>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Compute::V1::ServiceAccount](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ServiceAccount)>) — A list of service accounts, with their specified scopes, authorized for this instance. Only one service account per VM instance is supported.

Service accounts generate access tokens that can be accessed through the metadata server and used to authenticate applications on the instance. SeeService Accounts for more information. 




**Returns**

  * (::Array<[::Google::Cloud::Compute::V1::ServiceAccount](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ServiceAccount)>) — A list of service accounts, with their specified scopes, authorized for this instance. Only one service account per VM instance is supported.

Service accounts generate access tokens that can be accessed through the metadata server and used to authenticate applications on the instance. SeeService Accounts for more information. 




### #shielded_instance_config
    
    
    def shielded_instance_config() -> ::Google::Cloud::Compute::V1::ShieldedInstanceConfig

**Returns**

  * ([::Google::Cloud::Compute::V1::ShieldedInstanceConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ShieldedInstanceConfig)) 



### #shielded_instance_config=
    
    
    def shielded_instance_config=(value) -> ::Google::Cloud::Compute::V1::ShieldedInstanceConfig

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::ShieldedInstanceConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ShieldedInstanceConfig)) 



**Returns**

  * ([::Google::Cloud::Compute::V1::ShieldedInstanceConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ShieldedInstanceConfig)) 



### #shielded_instance_integrity_policy
    
    
    def shielded_instance_integrity_policy() -> ::Google::Cloud::Compute::V1::ShieldedInstanceIntegrityPolicy

**Returns**

  * ([::Google::Cloud::Compute::V1::ShieldedInstanceIntegrityPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ShieldedInstanceIntegrityPolicy)) 



### #shielded_instance_integrity_policy=
    
    
    def shielded_instance_integrity_policy=(value) -> ::Google::Cloud::Compute::V1::ShieldedInstanceIntegrityPolicy

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::ShieldedInstanceIntegrityPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ShieldedInstanceIntegrityPolicy)) 



**Returns**

  * ([::Google::Cloud::Compute::V1::ShieldedInstanceIntegrityPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ShieldedInstanceIntegrityPolicy)) 



### #source_machine_image
    
    
    def source_machine_image() -> ::String

**Returns**

  * (::String) — Source machine image 



### #source_machine_image=
    
    
    def source_machine_image=(value) -> ::String

**Parameter**

  * **value** (::String) — Source machine image 



**Returns**

  * (::String) — Source machine image 



### #source_machine_image_encryption_key
    
    
    def source_machine_image_encryption_key() -> ::Google::Cloud::Compute::V1::CustomerEncryptionKey

**Returns**

  * ([::Google::Cloud::Compute::V1::CustomerEncryptionKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-CustomerEncryptionKey)) — Source machine image encryption key when creating an instance from a machine image. 



### #source_machine_image_encryption_key=
    
    
    def source_machine_image_encryption_key=(value) -> ::Google::Cloud::Compute::V1::CustomerEncryptionKey

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::CustomerEncryptionKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-CustomerEncryptionKey)) — Source machine image encryption key when creating an instance from a machine image. 



**Returns**

  * ([::Google::Cloud::Compute::V1::CustomerEncryptionKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-CustomerEncryptionKey)) — Source machine image encryption key when creating an instance from a machine image. 



### #start_restricted
    
    
    def start_restricted() -> ::Boolean

**Returns**

  * (::Boolean) — Output only. [Output Only] Whether a VM has been restricted for start because Compute Engine has detected suspicious activity. 



### #start_restricted=
    
    
    def start_restricted=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Output only. [Output Only] Whether a VM has been restricted for start because Compute Engine has detected suspicious activity. 



**Returns**

  * (::Boolean) — Output only. [Output Only] Whether a VM has been restricted for start because Compute Engine has detected suspicious activity. 



### #status
    
    
    def status() -> ::String

**Returns**

  * (::String) — Output only. [Output Only] The status of the instance. One of the following values: PROVISIONING, STAGING,RUNNING, STOPPING, SUSPENDING,SUSPENDED, REPAIRING, andTERMINATED. For more information about the status of the instance, see Instance life cycle. Check the Status enum for the list of possible values. 



### #status=
    
    
    def status=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. [Output Only] The status of the instance. One of the following values: PROVISIONING, STAGING,RUNNING, STOPPING, SUSPENDING,SUSPENDED, REPAIRING, andTERMINATED. For more information about the status of the instance, see Instance life cycle. Check the Status enum for the list of possible values. 



**Returns**

  * (::String) — Output only. [Output Only] The status of the instance. One of the following values: PROVISIONING, STAGING,RUNNING, STOPPING, SUSPENDING,SUSPENDED, REPAIRING, andTERMINATED. For more information about the status of the instance, see Instance life cycle. Check the Status enum for the list of possible values. 



### #status_message
    
    
    def status_message() -> ::String

**Returns**

  * (::String) — Output only. [Output Only] An optional, human-readable explanation of the status. 



### #status_message=
    
    
    def status_message=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. [Output Only] An optional, human-readable explanation of the status. 



**Returns**

  * (::String) — Output only. [Output Only] An optional, human-readable explanation of the status. 



### #tags
    
    
    def tags() -> ::Google::Cloud::Compute::V1::Tags

**Returns**

  * ([::Google::Cloud::Compute::V1::Tags](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Tags)) — Tags to apply to this instance. Tags are used to identify valid sources or targets for network firewalls and are specified by the client during instance creation. The tags can be later modified by the setTags method. Each tag within the list must comply withRFC1035. Multiple tags can be specified via the 'tags.items' field. 



### #tags=
    
    
    def tags=(value) -> ::Google::Cloud::Compute::V1::Tags

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::Tags](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Tags)) — Tags to apply to this instance. Tags are used to identify valid sources or targets for network firewalls and are specified by the client during instance creation. The tags can be later modified by the setTags method. Each tag within the list must comply withRFC1035. Multiple tags can be specified via the 'tags.items' field. 



**Returns**

  * ([::Google::Cloud::Compute::V1::Tags](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Tags)) — Tags to apply to this instance. Tags are used to identify valid sources or targets for network firewalls and are specified by the client during instance creation. The tags can be later modified by the setTags method. Each tag within the list must comply withRFC1035. Multiple tags can be specified via the 'tags.items' field. 



### #workload_identity_config
    
    
    def workload_identity_config() -> ::Google::Cloud::Compute::V1::WorkloadIdentityConfig

**Returns**

  * ([::Google::Cloud::Compute::V1::WorkloadIdentityConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-WorkloadIdentityConfig)) 



### #workload_identity_config=
    
    
    def workload_identity_config=(value) -> ::Google::Cloud::Compute::V1::WorkloadIdentityConfig

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::WorkloadIdentityConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-WorkloadIdentityConfig)) 



**Returns**

  * ([::Google::Cloud::Compute::V1::WorkloadIdentityConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-WorkloadIdentityConfig)) 



### #zone
    
    
    def zone() -> ::String

**Returns**

  * (::String) — Output only. [Output Only] URL of the zone where the instance resides. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. 



### #zone=
    
    
    def zone=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. [Output Only] URL of the zone where the instance resides. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. 



**Returns**

  * (::String) — Output only. [Output Only] URL of the zone where the instance resides. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
