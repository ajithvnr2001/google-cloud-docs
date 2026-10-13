---
url: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.Scheduling
title: Class Scheduling (0.10.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:18:09.099573+00:00
---

# Class Scheduling (0.10.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.Scheduling

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Scheduling (0.10.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.3 (latest)  0.10.2  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.5  0.1.7 
    
    
    Scheduling(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Sets the scheduling options for an Instance.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`on_host_maintenance` |  `[google.cloud.backupdr_v1.types.Scheduling.OnHostMaintenance](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.Scheduling.OnHostMaintenance)`   
Optional. Defines the maintenance behavior for this instance. This field is a member of `oneof`_ `_on_host_maintenance`.   
`automatic_restart` |  `bool`   
Optional. Specifies whether the instance should be automatically restarted if it is terminated by Compute Engine (not terminated by a user). This field is a member of `oneof`_ `_automatic_restart`.   
`preemptible` |  `bool`   
Optional. Defines whether the instance is preemptible. This field is a member of `oneof`_ `_preemptible`.   
`node_affinities` |  `MutableSequence[[google.cloud.backupdr_v1.types.Scheduling.NodeAffinity](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.Scheduling.NodeAffinity)]`   
Optional. A set of node affinity and anti-affinity configurations. Overrides reservationAffinity.   
`min_node_cpus` |  `int`   
Optional. The minimum number of virtual CPUs this instance will consume when running on a sole-tenant node. This field is a member of `oneof`_ `_min_node_cpus`.   
`provisioning_model` |  `[google.cloud.backupdr_v1.types.Scheduling.ProvisioningModel](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.Scheduling.ProvisioningModel)`   
Optional. Specifies the provisioning model of the instance. This field is a member of `oneof`_ `_provisioning_model`.   
`instance_termination_action` |  `[google.cloud.backupdr_v1.types.Scheduling.InstanceTerminationAction](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.Scheduling.InstanceTerminationAction)`   
Optional. Specifies the termination action for the instance. This field is a member of `oneof`_ `_instance_termination_action`.   
`local_ssd_recovery_timeout` |  `[google.cloud.backupdr_v1.types.SchedulingDuration](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.SchedulingDuration)`   
Optional. Specifies the maximum amount of time a Local Ssd Vm should wait while recovery of the Local Ssd state is attempted. Its value should be in between 0 and 168 hours with hour granularity and the default value being 1 hour. This field is a member of `oneof`_ `_local_ssd_recovery_timeout`.   
  
## Classes 

### InstanceTerminationAction
    
    
    InstanceTerminationAction(value)

Defines the supported termination actions for an instance.

### NodeAffinity
    
    
    NodeAffinity(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Node Affinity: the configuration of desired nodes onto which this Instance could be scheduled.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### OnHostMaintenance
    
    
    OnHostMaintenance(value)

Defines the maintenance behavior for this instance=

### ProvisioningModel
    
    
    ProvisioningModel(value)

Defines the provisioning model for an instance.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
