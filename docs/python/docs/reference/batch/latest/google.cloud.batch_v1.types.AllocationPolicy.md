---
url: https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy
title: Class AllocationPolicy (0.22.4) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:43:24.030513+00:00
---

# Class AllocationPolicy (0.22.4)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AllocationPolicy (0.22.4) Stay organized with collections  Save and categorize content based on your preferences. 

0.22.4 (latest)  0.22.3  0.21.0  0.20.0  0.19.0  0.18.0  0.17.37  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.1  0.7.0  0.6.0  0.5.0  0.4.1  0.3.2  0.2.0  0.1.2 
    
    
    AllocationPolicy(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A Job's resource allocation policy describes when, where, and how compute resources should be allocated for the Job.

## Attributes  
  
---  
**Name** | **Description**  
`location` |  `[google.cloud.batch_v1.types.AllocationPolicy.LocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.LocationPolicy)`   
Location where compute resources should be allocated for the Job.   
`instances` |  `MutableSequence[[google.cloud.batch_v1.types.AllocationPolicy.InstancePolicyOrTemplate](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.InstancePolicyOrTemplate)]`   
Describe instances that can be created by this AllocationPolicy. Only instances[0] is supported now.   
`service_account` |  `[google.cloud.batch_v1.types.ServiceAccount](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.ServiceAccount)`   
Defines the service account for Batch-created VMs. If omitted, the `default Compute Engine service account   
`labels` |  `MutableMapping[str, str]`   
Custom labels to apply to the job and all the Compute Engine resources that both are created by this allocation policy and support labels. Use labels to group and describe the resources they are applied to. Batch automatically applies predefined labels and supports multiple `labels` fields for each job, which each let you apply custom labels to various resources. Label names that start with "goog-" or "google-" are reserved for predefined labels. For more information about labels with Batch, see `Organize resources using labels   
`network` |  `[google.cloud.batch_v1.types.AllocationPolicy.NetworkPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.NetworkPolicy)`   
The network policy. If you define an instance template in the `InstancePolicyOrTemplate` field, Batch will use the network settings in the instance template instead of this field.   
`placement` |  `[google.cloud.batch_v1.types.AllocationPolicy.PlacementPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.PlacementPolicy)`   
The placement policy.   
`tags` |  `MutableSequence[str]`   
Optional. Tags applied to the VM instances. The tags identify valid sources or targets for network firewalls. Each tag must be 1-63 characters long, and comply with `RFC1035 `__.   
  
## Classes 

### Accelerator
    
    
    Accelerator(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Accelerator describes Compute Engine accelerators to be attached to the VM.

### AttachedDisk
    
    
    AttachedDisk(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A new or an existing persistent disk (PD) or a local ssd attached to a VM instance.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### Disk
    
    
    Disk(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A new persistent disk or a local ssd. A VM can only have one local SSD setting but multiple local SSD partitions. See <https://cloud.google.com/compute/docs/disks#pdspecs> and <https://cloud.google.com/compute/docs/disks#localssds>.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### InstancePolicy
    
    
    InstancePolicy(mapping=None, *, ignore_unknown_fields=False, **kwargs)

InstancePolicy describes an instance type and resources attached to each VM created by this InstancePolicy.

### InstancePolicyOrTemplate
    
    
    InstancePolicyOrTemplate(mapping=None, *, ignore_unknown_fields=False, **kwargs)

InstancePolicyOrTemplate lets you define the type of resources to use for this job either with an InstancePolicy or an instance template. If undefined, Batch picks the type of VM to use and doesn't include optional VM resources such as GPUs and extra disks.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

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
  
### LocationPolicy
    
    
    LocationPolicy(mapping=None, *, ignore_unknown_fields=False, **kwargs)

### NetworkInterface
    
    
    NetworkInterface(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A network interface.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### NetworkPolicy
    
    
    NetworkPolicy(mapping=None, *, ignore_unknown_fields=False, **kwargs)

NetworkPolicy describes VM instance network configurations.

### PlacementPolicy
    
    
    PlacementPolicy(mapping=None, *, ignore_unknown_fields=False, **kwargs)

PlacementPolicy describes a group placement policy for the VMs controlled by this AllocationPolicy.

### ProvisioningModel
    
    
    ProvisioningModel(value)

Compute Engine VM instance provisioning model.
    
    
        Above SPOT VM is the preferable model for
        preemptible VM instances: the old preemptible VM
        model (indicated by this field) is the older
        model, and has been migrated to use the SPOT
        model as the underlying technology. This old
        model will still be supported.
    RESERVATION_BOUND (4):
        Bound to the lifecycle of the reservation in
        which it is provisioned.
    FLEX_START (5):
        Instance is provisioned with DWS Flex Start
        and has limited max run duration.
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
