---
url: https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Instance
title: Class Instance (1.18.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:40:41.271913+00:00
---

# Class Instance (1.18.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Instance

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Instance (1.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.18.0 (latest)  1.17.0  1.16.0  1.15.0  1.14.0  1.13.3  1.12.0  1.11.1  1.10.5  1.9.0  1.8.0  1.7.1  1.6.1  1.5.1  1.4.4  1.3.2  1.2.1  1.1.1  1.0.0  0.4.3  0.3.2  0.2.0  0.1.2 
    
    
    Instance(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The definition of a notebook instance.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Output only. The name of this notebook instance. Format: `projects/{project_id}/locations/{location}/instances/{instance_id}`  
`vm_image` |  `[google.cloud.notebooks_v1.types.VmImage](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.VmImage)`   
Use a Compute Engine VM image to start the notebook instance. This field is a member of `oneof`_ `environment`.   
`container_image` |  `[google.cloud.notebooks_v1.types.ContainerImage](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.ContainerImage)`   
Use a container image to start the notebook instance. This field is a member of `oneof`_ `environment`.   
`post_startup_script` |  `str`   
Path to a Bash script that automatically runs after a notebook instance fully boots up. The path must be a URL or Cloud Storage path (`gs://path-to-file/file-name`).   
`proxy_uri` |  `str`   
Output only. The proxy endpoint that is used to access the Jupyter notebook.   
`instance_owners` |  `MutableSequence[str]`   
Input only. The owner of this instance after creation. Format: `alias@example.com` Currently supports one owner only. If not specified, all of the service account users of your VM instance's service account can use the instance.   
`service_account` |  `str`   
The service account on this instance, giving access to other Google Cloud services. You can use any service account within the same project, but you must have the service account user permission to use the instance. If not specified, the `Compute Engine default service account   
`service_account_scopes` |  `MutableSequence[str]`   
Optional. The URIs of service account scopes to be included in Compute Engine instances. If not specified, the following `scopes `__ are defined: \- https://www.googleapis.com/auth/cloud-platform \- https://www.googleapis.com/auth/userinfo.email If not using default scopes, you need at least: https://www.googleapis.com/auth/compute   
`machine_type` |  `str`   
Required. The `Compute Engine machine type   
`accelerator_config` |  `[google.cloud.notebooks_v1.types.Instance.AcceleratorConfig](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Instance.AcceleratorConfig)`   
The hardware accelerator used on this instance. If you use accelerators, make sure that your configuration has `enough vCPUs and memory to support the `machine_type` you have selected   
`state` |  `[google.cloud.notebooks_v1.types.Instance.State](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Instance.State)`   
Output only. The state of this instance.   
`install_gpu_driver` |  `bool`   
Whether the end user authorizes Google Cloud to install GPU driver on this instance. If this field is empty or set to false, the GPU driver won't be installed. Only applicable to instances with GPUs.   
`custom_gpu_driver_path` |  `str`   
Specify a custom Cloud Storage path where the GPU driver is stored. If not specified, we'll automatically choose from official GPU drivers.   
`boot_disk_type` |  `[google.cloud.notebooks_v1.types.Instance.DiskType](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Instance.DiskType)`   
Input only. The type of the boot disk attached to this instance, defaults to standard persistent disk (`PD_STANDARD`).   
`boot_disk_size_gb` |  `int`   
Input only. The size of the boot disk in GB attached to this instance, up to a maximum of 64000 GB (64 TB). The minimum recommended value is 100 GB. If not specified, this defaults to 100\.   
`data_disk_type` |  `[google.cloud.notebooks_v1.types.Instance.DiskType](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Instance.DiskType)`   
Input only. The type of the data disk attached to this instance, defaults to standard persistent disk (`PD_STANDARD`).   
`data_disk_size_gb` |  `int`   
Input only. The size of the data disk in GB attached to this instance, up to a maximum of 64000 GB (64 TB). You can choose the size of the data disk based on how big your notebooks and data are. If not specified, this defaults to 100\.   
`no_remove_data_disk` |  `bool`   
Input only. If true, the data disk will not be auto deleted when deleting the instance.   
`disk_encryption` |  `[google.cloud.notebooks_v1.types.Instance.DiskEncryption](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Instance.DiskEncryption)`   
Input only. Disk encryption method used on the boot and data disks, defaults to GMEK.   
`kms_key` |  `str`   
Input only. The KMS key used to encrypt the disks, only applicable if disk_encryption is CMEK. Format: `projects/{project_id}/locations/{location}/keyRings/{key_ring_id}/cryptoKeys/{key_id}` Learn more about `using your own encryption keys `__.   
`disks` |  `MutableSequence[[google.cloud.notebooks_v1.types.Instance.Disk](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Instance.Disk)]`   
Output only. Attached disks to notebook instance.   
`shielded_instance_config` |  `[google.cloud.notebooks_v1.types.Instance.ShieldedInstanceConfig](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Instance.ShieldedInstanceConfig)`   
Optional. Shielded VM configuration. `Images using supported Shielded VM features   
`no_public_ip` |  `bool`   
If true, no public IP will be assigned to this instance.   
`no_proxy_access` |  `bool`   
If true, the notebook instance will not register with the proxy.   
`network` |  `str`   
The name of the VPC that this instance is in. Format: `projects/{project_id}/global/networks/{network_id}`  
`subnet` |  `str`   
The name of the subnet that this instance is in. Format: `projects/{project_id}/regions/{region}/subnetworks/{subnetwork_id}`  
`labels` |  `MutableMapping[str, str]`   
Labels to apply to this instance. These can be later modified by the setLabels method.   
`metadata` |  `MutableMapping[str, str]`   
Custom metadata to apply to this instance.   
`tags` |  `MutableSequence[str]`   
Optional. The Compute Engine tags to add to runtime (see `Tagging instances   
`upgrade_history` |  `MutableSequence[[google.cloud.notebooks_v1.types.Instance.UpgradeHistoryEntry](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Instance.UpgradeHistoryEntry)]`   
The upgrade history of this instance.   
`nic_type` |  `[google.cloud.notebooks_v1.types.Instance.NicType](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Instance.NicType)`   
Optional. The type of vNIC to be used on this interface. This may be gVNIC or VirtioNet.   
`reservation_affinity` |  `[google.cloud.notebooks_v1.types.ReservationAffinity](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.ReservationAffinity)`   
Optional. The optional reservation affinity. Setting this field will apply the specified `Zonal Compute Reservation   
`creator` |  `str`   
Output only. Email address of entity that sent original CreateInstance request.   
`can_ip_forward` |  `bool`   
Optional. Flag to enable ip forwarding or not, default false/off. https://cloud.google.com/vpc/docs/using-routes#canipforward   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Instance creation time.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Instance update time.   
  
## Classes 

### AcceleratorConfig
    
    
    AcceleratorConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Definition of a hardware accelerator. Note that not all combinations of `type` and `core_count` are valid. Check `GPUs on Compute Engine <https://cloud.google.com/compute/docs/gpus/#gpus-list>`__ to find a valid combination. TPUs are not supported.

### AcceleratorType
    
    
    AcceleratorType(value)

Definition of the types of hardware accelerators that can be used on this instance.

### Disk
    
    
    Disk(mapping=None, *, ignore_unknown_fields=False, **kwargs)

An instance-attached disk resource.

### DiskEncryption
    
    
    DiskEncryption(value)

Definition of the disk encryption options.

### DiskType
    
    
    DiskType(value)

Possible disk types for notebook instances.

### LabelsEntry
    
    
    LabelsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The abstract base class for a message.

**Parameters**  
---  
**Name** | **Description**  
`kwargs` |  `dict`   
Keys and values corresponding to the fields of the message.  
`mapping` |  `Union[dict, `.Message`]`   
A dictionary or message to be used to determine the values for this message.  
`ignore_unknown_fields` |  `Optional(bool)`   
If True, do not raise errors for unknown fields. Only applied if `mapping` is a mapping type or there are keyword parameters.  
  
### MetadataEntry
    
    
    MetadataEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The abstract base class for a message.

**Parameters**  
---  
**Name** | **Description**  
`kwargs` |  `dict`   
Keys and values corresponding to the fields of the message.  
`mapping` |  `Union[dict, `.Message`]`   
A dictionary or message to be used to determine the values for this message.  
`ignore_unknown_fields` |  `Optional(bool)`   
If True, do not raise errors for unknown fields. Only applied if `mapping` is a mapping type or there are keyword parameters.  
  
### NicType
    
    
    NicType(value)

The type of vNIC driver. Default should be UNSPECIFIED_NIC_TYPE.

### ShieldedInstanceConfig
    
    
    ShieldedInstanceConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A set of Shielded Instance options. Check `Images using supported Shielded VM features <https://cloud.google.com/compute/docs/instances/modifying-shielded-vm>`__. Not all combinations are valid.

### State
    
    
    State(value)

The definition of the states of this instance.

### UpgradeHistoryEntry
    
    
    UpgradeHistoryEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The entry of VM image upgrade history.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
