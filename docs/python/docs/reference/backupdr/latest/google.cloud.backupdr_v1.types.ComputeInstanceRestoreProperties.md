---
url: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ComputeInstanceRestoreProperties
title: Class ComputeInstanceRestoreProperties (0.10.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:12:43.218549+00:00
---

# Class ComputeInstanceRestoreProperties (0.10.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ComputeInstanceRestoreProperties

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ComputeInstanceRestoreProperties (0.10.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.3 (latest)  0.10.2  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.5  0.1.7 
    
    
    ComputeInstanceRestoreProperties(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

ComputeInstanceRestoreProperties represents Compute Engine instance properties to be overridden during restore.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Required. Name of the compute instance. This field is a member of `oneof`_ `_name`.   
`advanced_machine_features` |  `[google.cloud.backupdr_v1.types.AdvancedMachineFeatures](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.AdvancedMachineFeatures)`   
Optional. Controls for advanced machine-related behavior features. This field is a member of `oneof`_ `_advanced_machine_features`.   
`can_ip_forward` |  `bool`   
Optional. Allows this instance to send and receive packets with non-matching destination or source IPs. This field is a member of `oneof`_ `_can_ip_forward`.   
`confidential_instance_config` |  `[google.cloud.backupdr_v1.types.ConfidentialInstanceConfig](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ConfidentialInstanceConfig)`   
Optional. Controls Confidential compute options on the instance This field is a member of `oneof`_ `_confidential_instance_config`.   
`deletion_protection` |  `bool`   
Optional. Whether the resource should be protected against deletion. This field is a member of `oneof`_ `_deletion_protection`.   
`description` |  `str`   
Optional. An optional description of this resource. Provide this property when you create the resource. This field is a member of `oneof`_ `_description`.   
`disks` |  `MutableSequence[[google.cloud.backupdr_v1.types.AttachedDisk](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.AttachedDisk)]`   
Optional. Array of disks associated with this instance. Persistent disks must be created before you can assign them. Source regional persistent disks will be restored with default replica zones if not specified.   
`display_device` |  `[google.cloud.backupdr_v1.types.DisplayDevice](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DisplayDevice)`   
Optional. Enables display device for the instance. This field is a member of `oneof`_ `_display_device`.   
`guest_accelerators` |  `MutableSequence[[google.cloud.backupdr_v1.types.AcceleratorConfig](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.AcceleratorConfig)]`   
Optional. A list of the type and count of accelerator cards attached to the instance.   
`hostname` |  `str`   
Optional. Specifies the hostname of the instance. The specified hostname must be RFC1035 compliant. If hostname is not specified, the default hostname is [INSTANCE_NAME].c.[PROJECT_ID].internal when using the global DNS, and [INSTANCE_NAME].[ZONE].c.[PROJECT_ID].internal when using zonal DNS. This field is a member of `oneof`_ `_hostname`.   
`instance_encryption_key` |  `[google.cloud.backupdr_v1.types.CustomerEncryptionKey](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.CustomerEncryptionKey)`   
Optional. Encrypts suspended data for an instance with a customer-managed encryption key. This field is a member of `oneof`_ `_instance_encryption_key`.   
`key_revocation_action_type` |  `[google.cloud.backupdr_v1.types.KeyRevocationActionType](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.KeyRevocationActionType)`   
Optional. KeyRevocationActionType of the instance. This field is a member of `oneof`_ `_key_revocation_action_type`.   
`labels` |  `MutableMapping[str, str]`   
Optional. Labels to apply to this instance.   
`machine_type` |  `str`   
Optional. Full or partial URL of the machine type resource to use for this instance. This field is a member of `oneof`_ `_machine_type`.   
`metadata` |  `[google.cloud.backupdr_v1.types.Metadata](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.Metadata)`   
Optional. This includes custom metadata and predefined keys. This field is a member of `oneof`_ `_metadata`.   
`min_cpu_platform` |  `str`   
Optional. Minimum CPU platform to use for this instance. This field is a member of `oneof`_ `_min_cpu_platform`.   
`network_interfaces` |  `MutableSequence[[google.cloud.backupdr_v1.types.NetworkInterface](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.NetworkInterface)]`   
Optional. An array of network configurations for this instance. These specify how interfaces are configured to interact with other network services, such as connecting to the internet. Multiple interfaces are supported per instance. Required to restore in different project or region.   
`network_performance_config` |  `[google.cloud.backupdr_v1.types.NetworkPerformanceConfig](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.NetworkPerformanceConfig)`   
Optional. Configure network performance such as egress bandwidth tier. This field is a member of `oneof`_ `_network_performance_config`.   
`params` |  `[google.cloud.backupdr_v1.types.InstanceParams](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.InstanceParams)`   
Input only. Additional params passed with the request, but not persisted as part of resource payload. This field is a member of `oneof`_ `_params`.   
`private_ipv6_google_access` |  `[google.cloud.backupdr_v1.types.ComputeInstanceRestoreProperties.InstancePrivateIpv6GoogleAccess](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ComputeInstanceRestoreProperties.InstancePrivateIpv6GoogleAccess)`   
Optional. The private IPv6 google access type for the VM. If not specified, use INHERIT_FROM_SUBNETWORK as default. This field is a member of `oneof`_ `_private_ipv6_google_access`.   
`allocation_affinity` |  `[google.cloud.backupdr_v1.types.AllocationAffinity](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.AllocationAffinity)`   
Optional. Specifies the reservations that this instance can consume from. This field is a member of `oneof`_ `_allocation_affinity`.   
`resource_policies` |  `MutableSequence[str]`   
Optional. Resource policies applied to this instance. By default, no resource policies will be applied.   
`scheduling` |  `[google.cloud.backupdr_v1.types.Scheduling](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.Scheduling)`   
Optional. Sets the scheduling options for this instance. This field is a member of `oneof`_ `_scheduling`.   
`service_accounts` |  `MutableSequence[[google.cloud.backupdr_v1.types.ServiceAccount](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ServiceAccount)]`   
Optional. A list of service accounts, with their specified scopes, authorized for this instance. Only one service account per VM instance is supported.   
`tags` |  `[google.cloud.backupdr_v1.types.Tags](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.Tags)`   
Optional. Tags to apply to this instance. Tags are used to identify valid sources or targets for network firewalls and are specified by the client during instance creation. This field is a member of `oneof`_ `_tags`.   
  
## Classes 

### InstancePrivateIpv6GoogleAccess
    
    
    InstancePrivateIpv6GoogleAccess(value)

The private IPv6 google access type for the VMs.

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
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
