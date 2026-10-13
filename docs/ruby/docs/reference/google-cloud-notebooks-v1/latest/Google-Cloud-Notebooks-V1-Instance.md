---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-Instance/
title: AI Platform Notebooks V1 API - Class Google::Cloud::Notebooks::V1::Instance (v1.6.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:05:21.402224+00:00
---

# AI Platform Notebooks V1 API - Class Google::Cloud::Notebooks::V1::Instance (v1.6.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-Instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  AI Platform Notebooks V1 API - Class Google::Cloud::Notebooks::V1::Instance (v1.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.6.0 (latest)  1.5.0  1.4.0  1.3.1  1.2.0  1.1.0  1.0.1  0.11.0  0.10.0  0.9.1  0.8.2  0.7.0  0.6.1  0.5.0  0.4.2  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the AI Platform Notebooks V1 API class Google::Cloud::Notebooks::V1::Instance.

The definition of a notebook instance.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #accelerator_config
    
    
    def accelerator_config() -> ::Google::Cloud::Notebooks::V1::Instance::AcceleratorConfig

**Returns**

  * ([::Google::Cloud::Notebooks::V1::Instance::AcceleratorConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-Instance-AcceleratorConfig)) — The hardware accelerator used on this instance. If you use accelerators, make sure that your configuration has [enough vCPUs and memory to support the `machine_type` you have selected](https://cloud.google.com/compute/docs/gpus/#gpus-list). 



### #accelerator_config=
    
    
    def accelerator_config=(value) -> ::Google::Cloud::Notebooks::V1::Instance::AcceleratorConfig

**Parameter**

  * **value** ([::Google::Cloud::Notebooks::V1::Instance::AcceleratorConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-Instance-AcceleratorConfig)) — The hardware accelerator used on this instance. If you use accelerators, make sure that your configuration has [enough vCPUs and memory to support the `machine_type` you have selected](https://cloud.google.com/compute/docs/gpus/#gpus-list). 



**Returns**

  * ([::Google::Cloud::Notebooks::V1::Instance::AcceleratorConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-Instance-AcceleratorConfig)) — The hardware accelerator used on this instance. If you use accelerators, make sure that your configuration has [enough vCPUs and memory to support the `machine_type` you have selected](https://cloud.google.com/compute/docs/gpus/#gpus-list). 



### #boot_disk_size_gb
    
    
    def boot_disk_size_gb() -> ::Integer

**Returns**

  * (::Integer) — Input only. The size of the boot disk in GB attached to this instance, up to a maximum of 64000 GB (64 TB). The minimum recommended value is 100 GB. If not specified, this defaults to 100. 



### #boot_disk_size_gb=
    
    
    def boot_disk_size_gb=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Input only. The size of the boot disk in GB attached to this instance, up to a maximum of 64000 GB (64 TB). The minimum recommended value is 100 GB. If not specified, this defaults to 100. 



**Returns**

  * (::Integer) — Input only. The size of the boot disk in GB attached to this instance, up to a maximum of 64000 GB (64 TB). The minimum recommended value is 100 GB. If not specified, this defaults to 100. 



### #boot_disk_type
    
    
    def boot_disk_type() -> ::Google::Cloud::Notebooks::V1::Instance::DiskType

**Returns**

  * ([::Google::Cloud::Notebooks::V1::Instance::DiskType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-Instance-DiskType)) — Input only. The type of the boot disk attached to this instance, defaults to standard persistent disk (`PD_STANDARD`). 



### #boot_disk_type=
    
    
    def boot_disk_type=(value) -> ::Google::Cloud::Notebooks::V1::Instance::DiskType

**Parameter**

  * **value** ([::Google::Cloud::Notebooks::V1::Instance::DiskType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-Instance-DiskType)) — Input only. The type of the boot disk attached to this instance, defaults to standard persistent disk (`PD_STANDARD`). 



**Returns**

  * ([::Google::Cloud::Notebooks::V1::Instance::DiskType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-Instance-DiskType)) — Input only. The type of the boot disk attached to this instance, defaults to standard persistent disk (`PD_STANDARD`). 



### #can_ip_forward
    
    
    def can_ip_forward() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. Flag to enable ip forwarding or not, default false/off. https://cloud.google.com/vpc/docs/using-routes#canipforward 



### #can_ip_forward=
    
    
    def can_ip_forward=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. Flag to enable ip forwarding or not, default false/off. https://cloud.google.com/vpc/docs/using-routes#canipforward 



**Returns**

  * (::Boolean) — Optional. Flag to enable ip forwarding or not, default false/off. https://cloud.google.com/vpc/docs/using-routes#canipforward 



### #container_image
    
    
    def container_image() -> ::Google::Cloud::Notebooks::V1::ContainerImage

**Returns**

  * ([::Google::Cloud::Notebooks::V1::ContainerImage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-ContainerImage)) — Use a container image to start the notebook instance.

Note: The following fields are mutually exclusive: `container_image`, `vm_image`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #container_image=
    
    
    def container_image=(value) -> ::Google::Cloud::Notebooks::V1::ContainerImage

**Parameter**

  * **value** ([::Google::Cloud::Notebooks::V1::ContainerImage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-ContainerImage)) — Use a container image to start the notebook instance.

Note: The following fields are mutually exclusive: `container_image`, `vm_image`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Notebooks::V1::ContainerImage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-ContainerImage)) — Use a container image to start the notebook instance.

Note: The following fields are mutually exclusive: `container_image`, `vm_image`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Protobuf-Timestamp)) — Output only. Instance creation time. 



### #creator
    
    
    def creator() -> ::String

**Returns**

  * (::String) — Output only. Email address of entity that sent original CreateInstance request. 



### #custom_gpu_driver_path
    
    
    def custom_gpu_driver_path() -> ::String

**Returns**

  * (::String) — Specify a custom Cloud Storage path where the GPU driver is stored. If not specified, we'll automatically choose from official GPU drivers. 



### #custom_gpu_driver_path=
    
    
    def custom_gpu_driver_path=(value) -> ::String

**Parameter**

  * **value** (::String) — Specify a custom Cloud Storage path where the GPU driver is stored. If not specified, we'll automatically choose from official GPU drivers. 



**Returns**

  * (::String) — Specify a custom Cloud Storage path where the GPU driver is stored. If not specified, we'll automatically choose from official GPU drivers. 



### #data_disk_size_gb
    
    
    def data_disk_size_gb() -> ::Integer

**Returns**

  * (::Integer) — Input only. The size of the data disk in GB attached to this instance, up to a maximum of 64000 GB (64 TB). You can choose the size of the data disk based on how big your notebooks and data are. If not specified, this defaults to 100. 



### #data_disk_size_gb=
    
    
    def data_disk_size_gb=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Input only. The size of the data disk in GB attached to this instance, up to a maximum of 64000 GB (64 TB). You can choose the size of the data disk based on how big your notebooks and data are. If not specified, this defaults to 100. 



**Returns**

  * (::Integer) — Input only. The size of the data disk in GB attached to this instance, up to a maximum of 64000 GB (64 TB). You can choose the size of the data disk based on how big your notebooks and data are. If not specified, this defaults to 100. 



### #data_disk_type
    
    
    def data_disk_type() -> ::Google::Cloud::Notebooks::V1::Instance::DiskType

**Returns**

  * ([::Google::Cloud::Notebooks::V1::Instance::DiskType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-Instance-DiskType)) — Input only. The type of the data disk attached to this instance, defaults to standard persistent disk (`PD_STANDARD`). 



### #data_disk_type=
    
    
    def data_disk_type=(value) -> ::Google::Cloud::Notebooks::V1::Instance::DiskType

**Parameter**

  * **value** ([::Google::Cloud::Notebooks::V1::Instance::DiskType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-Instance-DiskType)) — Input only. The type of the data disk attached to this instance, defaults to standard persistent disk (`PD_STANDARD`). 



**Returns**

  * ([::Google::Cloud::Notebooks::V1::Instance::DiskType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-Instance-DiskType)) — Input only. The type of the data disk attached to this instance, defaults to standard persistent disk (`PD_STANDARD`). 



### #disk_encryption
    
    
    def disk_encryption() -> ::Google::Cloud::Notebooks::V1::Instance::DiskEncryption

**Returns**

  * ([::Google::Cloud::Notebooks::V1::Instance::DiskEncryption](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-Instance-DiskEncryption)) — Input only. Disk encryption method used on the boot and data disks, defaults to GMEK. 



### #disk_encryption=
    
    
    def disk_encryption=(value) -> ::Google::Cloud::Notebooks::V1::Instance::DiskEncryption

**Parameter**

  * **value** ([::Google::Cloud::Notebooks::V1::Instance::DiskEncryption](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-Instance-DiskEncryption)) — Input only. Disk encryption method used on the boot and data disks, defaults to GMEK. 



**Returns**

  * ([::Google::Cloud::Notebooks::V1::Instance::DiskEncryption](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-Instance-DiskEncryption)) — Input only. Disk encryption method used on the boot and data disks, defaults to GMEK. 



### #disks
    
    
    def disks() -> ::Array<::Google::Cloud::Notebooks::V1::Instance::Disk>

**Returns**

  * (::Array<[::Google::Cloud::Notebooks::V1::Instance::Disk](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-Instance-Disk)>) — Output only. Attached disks to notebook instance. 



### #install_gpu_driver
    
    
    def install_gpu_driver() -> ::Boolean

**Returns**

  * (::Boolean) — Whether the end user authorizes Google Cloud to install GPU driver on this instance. If this field is empty or set to false, the GPU driver won't be installed. Only applicable to instances with GPUs. 



### #install_gpu_driver=
    
    
    def install_gpu_driver=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Whether the end user authorizes Google Cloud to install GPU driver on this instance. If this field is empty or set to false, the GPU driver won't be installed. Only applicable to instances with GPUs. 



**Returns**

  * (::Boolean) — Whether the end user authorizes Google Cloud to install GPU driver on this instance. If this field is empty or set to false, the GPU driver won't be installed. Only applicable to instances with GPUs. 



### #instance_owners
    
    
    def instance_owners() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Input only. The owner of this instance after creation. Format: `alias@example.com`

Currently supports one owner only. If not specified, all of the service account users of your VM instance's service account can use the instance. 




### #instance_owners=
    
    
    def instance_owners=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Input only. The owner of this instance after creation. Format: `alias@example.com`

Currently supports one owner only. If not specified, all of the service account users of your VM instance's service account can use the instance. 




**Returns**

  * (::Array<::String>) — Input only. The owner of this instance after creation. Format: `alias@example.com`

Currently supports one owner only. If not specified, all of the service account users of your VM instance's service account can use the instance. 




### #kms_key
    
    
    def kms_key() -> ::String

**Returns**

  * (::String) — Input only. The KMS key used to encrypt the disks, only applicable if disk_encryption is CMEK. Format: `projects/{project_id}/locations/{location}/keyRings/{key_ring_id}/cryptoKeys/{key_id}`

Learn more about [using your own encryption keys](https://docs.cloud.google.com/kms/docs/quickstart). 




### #kms_key=
    
    
    def kms_key=(value) -> ::String

**Parameter**

  * **value** (::String) — Input only. The KMS key used to encrypt the disks, only applicable if disk_encryption is CMEK. Format: `projects/{project_id}/locations/{location}/keyRings/{key_ring_id}/cryptoKeys/{key_id}`

Learn more about [using your own encryption keys](https://docs.cloud.google.com/kms/docs/quickstart). 




**Returns**

  * (::String) — Input only. The KMS key used to encrypt the disks, only applicable if disk_encryption is CMEK. Format: `projects/{project_id}/locations/{location}/keyRings/{key_ring_id}/cryptoKeys/{key_id}`

Learn more about [using your own encryption keys](https://docs.cloud.google.com/kms/docs/quickstart). 




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



### #machine_type
    
    
    def machine_type() -> ::String

**Returns**

  * (::String) — Required. The [Compute Engine machine type](https://cloud.google.com/compute/docs/machine-types) of this instance. 



### #machine_type=
    
    
    def machine_type=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The [Compute Engine machine type](https://cloud.google.com/compute/docs/machine-types) of this instance. 



**Returns**

  * (::String) — Required. The [Compute Engine machine type](https://cloud.google.com/compute/docs/machine-types) of this instance. 



### #metadata
    
    
    def metadata() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Custom metadata to apply to this instance. 



### #metadata=
    
    
    def metadata=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Custom metadata to apply to this instance. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Custom metadata to apply to this instance. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Output only. The name of this notebook instance. Format: `projects/{project_id}/locations/{location}/instances/{instance_id}`



### #network
    
    
    def network() -> ::String

**Returns**

  * (::String) — The name of the VPC that this instance is in. Format: `projects/{project_id}/global/networks/{network_id}`



### #network=
    
    
    def network=(value) -> ::String

**Parameter**

  * **value** (::String) — The name of the VPC that this instance is in. Format: `projects/{project_id}/global/networks/{network_id}`



**Returns**

  * (::String) — The name of the VPC that this instance is in. Format: `projects/{project_id}/global/networks/{network_id}`



### #nic_type
    
    
    def nic_type() -> ::Google::Cloud::Notebooks::V1::Instance::NicType

**Returns**

  * ([::Google::Cloud::Notebooks::V1::Instance::NicType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-Instance-NicType)) — Optional. The type of vNIC to be used on this interface. This may be gVNIC or VirtioNet. 



### #nic_type=
    
    
    def nic_type=(value) -> ::Google::Cloud::Notebooks::V1::Instance::NicType

**Parameter**

  * **value** ([::Google::Cloud::Notebooks::V1::Instance::NicType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-Instance-NicType)) — Optional. The type of vNIC to be used on this interface. This may be gVNIC or VirtioNet. 



**Returns**

  * ([::Google::Cloud::Notebooks::V1::Instance::NicType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-Instance-NicType)) — Optional. The type of vNIC to be used on this interface. This may be gVNIC or VirtioNet. 



### #no_proxy_access
    
    
    def no_proxy_access() -> ::Boolean

**Returns**

  * (::Boolean) — If true, the notebook instance will not register with the proxy. 



### #no_proxy_access=
    
    
    def no_proxy_access=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — If true, the notebook instance will not register with the proxy. 



**Returns**

  * (::Boolean) — If true, the notebook instance will not register with the proxy. 



### #no_public_ip
    
    
    def no_public_ip() -> ::Boolean

**Returns**

  * (::Boolean) — If true, no public IP will be assigned to this instance. 



### #no_public_ip=
    
    
    def no_public_ip=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — If true, no public IP will be assigned to this instance. 



**Returns**

  * (::Boolean) — If true, no public IP will be assigned to this instance. 



### #no_remove_data_disk
    
    
    def no_remove_data_disk() -> ::Boolean

**Returns**

  * (::Boolean) — Input only. If true, the data disk will not be auto deleted when deleting the instance. 



### #no_remove_data_disk=
    
    
    def no_remove_data_disk=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Input only. If true, the data disk will not be auto deleted when deleting the instance. 



**Returns**

  * (::Boolean) — Input only. If true, the data disk will not be auto deleted when deleting the instance. 



### #post_startup_script
    
    
    def post_startup_script() -> ::String

**Returns**

  * (::String) — Path to a Bash script that automatically runs after a notebook instance fully boots up. The path must be a URL or Cloud Storage path (`gs://path-to-file/file-name`). 



### #post_startup_script=
    
    
    def post_startup_script=(value) -> ::String

**Parameter**

  * **value** (::String) — Path to a Bash script that automatically runs after a notebook instance fully boots up. The path must be a URL or Cloud Storage path (`gs://path-to-file/file-name`). 



**Returns**

  * (::String) — Path to a Bash script that automatically runs after a notebook instance fully boots up. The path must be a URL or Cloud Storage path (`gs://path-to-file/file-name`). 



### #proxy_uri
    
    
    def proxy_uri() -> ::String

**Returns**

  * (::String) — Output only. The proxy endpoint that is used to access the Jupyter notebook. 



### #reservation_affinity
    
    
    def reservation_affinity() -> ::Google::Cloud::Notebooks::V1::ReservationAffinity

**Returns**

  * ([::Google::Cloud::Notebooks::V1::ReservationAffinity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-ReservationAffinity)) — Optional. The optional reservation affinity. Setting this field will apply the specified [Zonal Compute Reservation](https://cloud.google.com/compute/docs/instances/reserving-zonal-resources) to this notebook instance. 



### #reservation_affinity=
    
    
    def reservation_affinity=(value) -> ::Google::Cloud::Notebooks::V1::ReservationAffinity

**Parameter**

  * **value** ([::Google::Cloud::Notebooks::V1::ReservationAffinity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-ReservationAffinity)) — Optional. The optional reservation affinity. Setting this field will apply the specified [Zonal Compute Reservation](https://cloud.google.com/compute/docs/instances/reserving-zonal-resources) to this notebook instance. 



**Returns**

  * ([::Google::Cloud::Notebooks::V1::ReservationAffinity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-ReservationAffinity)) — Optional. The optional reservation affinity. Setting this field will apply the specified [Zonal Compute Reservation](https://cloud.google.com/compute/docs/instances/reserving-zonal-resources) to this notebook instance. 



### #service_account
    
    
    def service_account() -> ::String

**Returns**

  * (::String) — The service account on this instance, giving access to other Google Cloud services. You can use any service account within the same project, but you must have the service account user permission to use the instance.

If not specified, the [Compute Engine default service account](https://cloud.google.com/compute/docs/access/service-accounts#default_service_account) is used. 




### #service_account=
    
    
    def service_account=(value) -> ::String

**Parameter**

  * **value** (::String) — The service account on this instance, giving access to other Google Cloud services. You can use any service account within the same project, but you must have the service account user permission to use the instance.

If not specified, the [Compute Engine default service account](https://cloud.google.com/compute/docs/access/service-accounts#default_service_account) is used. 




**Returns**

  * (::String) — The service account on this instance, giving access to other Google Cloud services. You can use any service account within the same project, but you must have the service account user permission to use the instance.

If not specified, the [Compute Engine default service account](https://cloud.google.com/compute/docs/access/service-accounts#default_service_account) is used. 




### #service_account_scopes
    
    
    def service_account_scopes() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — 

Optional. The URIs of service account scopes to be included in Compute Engine instances.

If not specified, the following [scopes](https://cloud.google.com/compute/docs/access/service-accounts#accesscopesiam) are defined:

    * https://www.googleapis.com/auth/cloud-platform
    * https://www.googleapis.com/auth/userinfo.email If not using default scopes, you need at least: https://www.googleapis.com/auth/compute



### #service_account_scopes=
    
    
    def service_account_scopes=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — 

Optional. The URIs of service account scopes to be included in Compute Engine instances.

If not specified, the following [scopes](https://cloud.google.com/compute/docs/access/service-accounts#accesscopesiam) are defined:

    * https://www.googleapis.com/auth/cloud-platform
    * https://www.googleapis.com/auth/userinfo.email If not using default scopes, you need at least: https://www.googleapis.com/auth/compute



**Returns**

  * (::Array<::String>) — 

Optional. The URIs of service account scopes to be included in Compute Engine instances.

If not specified, the following [scopes](https://cloud.google.com/compute/docs/access/service-accounts#accesscopesiam) are defined:

    * https://www.googleapis.com/auth/cloud-platform
    * https://www.googleapis.com/auth/userinfo.email If not using default scopes, you need at least: https://www.googleapis.com/auth/compute



### #shielded_instance_config
    
    
    def shielded_instance_config() -> ::Google::Cloud::Notebooks::V1::Instance::ShieldedInstanceConfig

**Returns**

  * ([::Google::Cloud::Notebooks::V1::Instance::ShieldedInstanceConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-Instance-ShieldedInstanceConfig)) — Optional. Shielded VM configuration. [Images using supported Shielded VM features](https://cloud.google.com/compute/docs/instances/modifying-shielded-vm). 



### #shielded_instance_config=
    
    
    def shielded_instance_config=(value) -> ::Google::Cloud::Notebooks::V1::Instance::ShieldedInstanceConfig

**Parameter**

  * **value** ([::Google::Cloud::Notebooks::V1::Instance::ShieldedInstanceConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-Instance-ShieldedInstanceConfig)) — Optional. Shielded VM configuration. [Images using supported Shielded VM features](https://cloud.google.com/compute/docs/instances/modifying-shielded-vm). 



**Returns**

  * ([::Google::Cloud::Notebooks::V1::Instance::ShieldedInstanceConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-Instance-ShieldedInstanceConfig)) — Optional. Shielded VM configuration. [Images using supported Shielded VM features](https://cloud.google.com/compute/docs/instances/modifying-shielded-vm). 



### #state
    
    
    def state() -> ::Google::Cloud::Notebooks::V1::Instance::State

**Returns**

  * ([::Google::Cloud::Notebooks::V1::Instance::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-Instance-State)) — Output only. The state of this instance. 



### #subnet
    
    
    def subnet() -> ::String

**Returns**

  * (::String) — The name of the subnet that this instance is in. Format: `projects/{project_id}/regions/{region}/subnetworks/{subnetwork_id}`



### #subnet=
    
    
    def subnet=(value) -> ::String

**Parameter**

  * **value** (::String) — The name of the subnet that this instance is in. Format: `projects/{project_id}/regions/{region}/subnetworks/{subnetwork_id}`



**Returns**

  * (::String) — The name of the subnet that this instance is in. Format: `projects/{project_id}/regions/{region}/subnetworks/{subnetwork_id}`



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



### #update_time
    
    
    def update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Protobuf-Timestamp)) — Output only. Instance update time. 



### #upgrade_history
    
    
    def upgrade_history() -> ::Array<::Google::Cloud::Notebooks::V1::Instance::UpgradeHistoryEntry>

**Returns**

  * (::Array<[::Google::Cloud::Notebooks::V1::Instance::UpgradeHistoryEntry](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-Instance-UpgradeHistoryEntry)>) — The upgrade history of this instance. 



### #upgrade_history=
    
    
    def upgrade_history=(value) -> ::Array<::Google::Cloud::Notebooks::V1::Instance::UpgradeHistoryEntry>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Notebooks::V1::Instance::UpgradeHistoryEntry](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-Instance-UpgradeHistoryEntry)>) — The upgrade history of this instance. 



**Returns**

  * (::Array<[::Google::Cloud::Notebooks::V1::Instance::UpgradeHistoryEntry](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-Instance-UpgradeHistoryEntry)>) — The upgrade history of this instance. 



### #vm_image
    
    
    def vm_image() -> ::Google::Cloud::Notebooks::V1::VmImage

**Returns**

  * ([::Google::Cloud::Notebooks::V1::VmImage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-VmImage)) — Use a Compute Engine VM image to start the notebook instance.

Note: The following fields are mutually exclusive: `vm_image`, `container_image`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #vm_image=
    
    
    def vm_image=(value) -> ::Google::Cloud::Notebooks::V1::VmImage

**Parameter**

  * **value** ([::Google::Cloud::Notebooks::V1::VmImage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-VmImage)) — Use a Compute Engine VM image to start the notebook instance.

Note: The following fields are mutually exclusive: `vm_image`, `container_image`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Notebooks::V1::VmImage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-VmImage)) — Use a Compute Engine VM image to start the notebook instance.

Note: The following fields are mutually exclusive: `vm_image`, `container_image`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
