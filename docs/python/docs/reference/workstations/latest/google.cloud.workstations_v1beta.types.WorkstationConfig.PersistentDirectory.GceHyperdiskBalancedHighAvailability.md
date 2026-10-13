---
url: https://docs.cloud.google.com/python/docs/reference/workstations/latest/google.cloud.workstations_v1beta.types.WorkstationConfig.PersistentDirectory.GceHyperdiskBalancedHighAvailability
title: Class GceHyperdiskBalancedHighAvailability (0.8.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:38:04.138094+00:00
---

# Class GceHyperdiskBalancedHighAvailability (0.8.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/workstations/latest/google.cloud.workstations_v1beta.types.WorkstationConfig.PersistentDirectory.GceHyperdiskBalancedHighAvailability

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class GceHyperdiskBalancedHighAvailability (0.8.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.2 (latest)  0.8.1  0.7.0  0.6.0  0.5.13  0.4.1  0.3.0  0.2.1  0.1.1 
    
    
    GceHyperdiskBalancedHighAvailability(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

A Persistent Directory backed by a Compute Engine `Hyperdisk Balanced High Availability Disk <https://cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced-ha>`__. This is a high-availability block storage solution that offers a balance between performance and cost for most general-purpose workloads.

## Attributes  
  
---  
**Name** | **Description**  
`size_gb` |  `int`   
Optional. The GB capacity of a persistent home directory for each workstation created with this configuration. Must be empty if source_snapshot is set. Valid values are `10`, `50`, `100`, `200`, `500`, or `1000`. Defaults to `200`.   
`max_size_gb` |  `int`   
Optional. Maximum size in GB to which this persistent directory can be resized. Defaults to unlimited if not set.   
`source_snapshot` |  `str`   
Optional. Name of the snapshot to use as the source for the disk. If set, size_gb must be empty. Must be formatted as ext4 file system with no partitions.   
`reclaim_policy` |  `[google.cloud.workstations_v1beta.types.WorkstationConfig.PersistentDirectory.GceHyperdiskBalancedHighAvailability.ReclaimPolicy](https://docs.cloud.google.com/python/docs/reference/workstations/latest/google.cloud.workstations_v1beta.types.WorkstationConfig.PersistentDirectory.GceHyperdiskBalancedHighAvailability.ReclaimPolicy)`   
Optional. Whether the persistent disk should be deleted when the workstation is deleted. Valid values are `DELETE` and `RETAIN`. Defaults to `DELETE`.   
`archive_timeout` |  `google.protobuf.duration_pb2.Duration`   
Optional. Number of seconds to wait after initially creating or subsequently shutting down the workstation before converting its disk into a snapshot. This generally saves costs at the expense of greater startup time on next workstation start, as the service will need to create a disk from the archival snapshot. A value of `"0s"` indicates that the disk will never be archived.   
  
## Classes 

### ReclaimPolicy
    
    
    ReclaimPolicy(value)

Value representing what should happen to the disk after the workstation is deleted.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
