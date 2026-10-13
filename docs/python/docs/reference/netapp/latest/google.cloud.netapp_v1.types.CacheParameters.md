---
url: https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.CacheParameters
title: Class CacheParameters (0.10.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:28:14.885443+00:00
---

# Class CacheParameters (0.10.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.CacheParameters

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class CacheParameters (0.10.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.2 (latest)  0.10.1  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.24  0.2.0  0.1.0 
    
    
    CacheParameters(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Cache Parameters for the volume.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`peer_volume_name` |  `str`   
Required. Name of the origin volume for the cache volume.   
`peer_cluster_name` |  `str`   
Required. Name of the origin volume's ONTAP cluster.   
`peer_svm_name` |  `str`   
Required. Name of the origin volume's SVM.   
`peer_ip_addresses` |  `MutableSequence[str]`   
Required. List of IC LIF addresses of the origin volume's ONTAP cluster.   
`enable_global_file_lock` |  `bool`   
Optional. Indicates whether the cache volume has global file lock enabled. This field is a member of `oneof`_ `_enable_global_file_lock`.   
`cache_config` |  `[google.cloud.netapp_v1.types.CacheConfig](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.CacheConfig)`   
Optional. Configuration of the cache volume.   
`cache_state` |  `[google.cloud.netapp_v1.types.CacheParameters.CacheState](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.CacheParameters.CacheState)`   
Output only. State of the cache volume indicating the peering status.   
`command` |  `str`   
Output only. Copy-paste-able commands to be used on user's ONTAP to accept peering requests.   
`peering_command_expiry_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Optional. Expiration time for the peering command to be executed on user's ONTAP.   
`passphrase` |  `str`   
Output only. Temporary passphrase generated to accept cluster peering command.   
`state_details` |  `str`   
Output only. Detailed description of the current cache state.   
  
## Classes 

### CacheState
    
    
    CacheState(value)

State of the cache volume indicating the peering status.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
