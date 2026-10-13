---
url: https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1alpha.types.OSPolicy
title: Class OSPolicy (1.26.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:56:30.132623+00:00
---

# Class OSPolicy (1.26.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1alpha.types.OSPolicy

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class OSPolicy (1.26.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.26.0 (latest)  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.2  1.19.0  1.18.1  1.17.5  1.16.0  1.15.3  1.14.1  1.13.0  1.12.4  1.11.2  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.2  1.4.0  1.3.2  1.2.0  1.1.0  1.0.0  0.1.2 
    
    
    OSPolicy(mapping=None, *, ignore_unknown_fields=False, **kwargs)

An OS policy defines the desired state configuration for a VM.

## Attributes  
  
---  
**Name** | **Description**  
`id` |  `str`   
Required. The id of the OS policy with the following restrictions: \- Must contain only lowercase letters, numbers, and hyphens. \- Must start with a letter. \- Must be between 1-63 characters. \- Must end with a number or a letter. \- Must be unique within the assignment.   
`description` |  `str`   
Policy description. Length of the description is limited to 1024 characters.   
`mode` |  `[google.cloud.osconfig_v1alpha.types.OSPolicy.Mode](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1alpha.types.OSPolicy.Mode)`   
Required. Policy mode   
`resource_groups` |  `MutableSequence[[google.cloud.osconfig_v1alpha.types.OSPolicy.ResourceGroup](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1alpha.types.OSPolicy.ResourceGroup)]`   
Required. List of resource groups for the policy. For a particular VM, resource groups are evaluated in the order specified and the first resource group that is applicable is selected and the rest are ignored. If none of the resource groups are applicable for a VM, the VM is considered to be non-compliant w.r.t this policy. This behavior can be toggled by the flag `allow_no_resource_group_match`  
`allow_no_resource_group_match` |  `bool`   
This flag determines the OS policy compliance status when none of the resource groups within the policy are applicable for a VM. Set this value to `true` if the policy needs to be reported as compliant even if the policy has nothing to validate or enforce.   
  
## Classes 

### InventoryFilter
    
    
    InventoryFilter(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Filtering criteria to select VMs based on inventory details.

### Mode
    
    
    Mode(value)

Policy mode

### OSFilter
    
    
    OSFilter(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Filtering criteria to select VMs based on OS details.

### Resource
    
    
    Resource(mapping=None, *, ignore_unknown_fields=False, **kwargs)

An OS policy resource is used to define the desired state configuration and provides a specific functionality like installing/removing packages, executing a script etc.

The system ensures that resources are always in their desired state by taking necessary actions if they have drifted from their desired state.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### ResourceGroup
    
    
    ResourceGroup(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Resource groups provide a mechanism to group OS policy resources.

Resource groups enable OS policy authors to create a single OS policy to be applied to VMs running different operating Systems.

When the OS policy is applied to a target VM, the appropriate resource group within the OS policy is selected based on the `OSFilter` specified within the resource group.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
