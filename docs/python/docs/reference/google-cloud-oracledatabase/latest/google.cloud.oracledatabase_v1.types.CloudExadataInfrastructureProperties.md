---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-oracledatabase/latest/google.cloud.oracledatabase_v1.types.CloudExadataInfrastructureProperties
title: Class CloudExadataInfrastructureProperties (0.6.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:51:06.455548+00:00
---

# Class CloudExadataInfrastructureProperties (0.6.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-oracledatabase/latest/google.cloud.oracledatabase_v1.types.CloudExadataInfrastructureProperties

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class CloudExadataInfrastructureProperties (0.6.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.3 (latest)  0.6.2  0.5.0  0.4.0  0.3.0  0.2.0  0.1.10 
    
    
    CloudExadataInfrastructureProperties(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

Various properties of Exadata Infrastructure.

## Attributes  
  
---  
**Name** | **Description**  
`ocid` |  `str`   
Output only. OCID of created infra. https://docs.oracle.com/en-us/iaas/Content/General/Concepts/identifiers.htm#Oracle   
`compute_count` |  `int`   
Optional. The number of compute servers for the Exadata Infrastructure.   
`storage_count` |  `int`   
Optional. The number of Cloud Exadata storage servers for the Exadata Infrastructure.   
`total_storage_size_gb` |  `int`   
Optional. The total storage allocated to the Exadata Infrastructure resource, in gigabytes (GB).   
`available_storage_size_gb` |  `int`   
Output only. The available storage can be allocated to the Exadata Infrastructure resource, in gigabytes (GB).   
`maintenance_window` |  `[google.cloud.oracledatabase_v1.types.MaintenanceWindow](https://docs.cloud.google.com/python/docs/reference/google-cloud-oracledatabase/latest/google.cloud.oracledatabase_v1.types.MaintenanceWindow)`   
Optional. Maintenance window for repair.   
`state` |  `[google.cloud.oracledatabase_v1.types.CloudExadataInfrastructureProperties.State](https://docs.cloud.google.com/python/docs/reference/google-cloud-oracledatabase/latest/google.cloud.oracledatabase_v1.types.CloudExadataInfrastructureProperties.State)`   
Output only. The current lifecycle state of the Exadata Infrastructure.   
`shape` |  `str`   
Required. The shape of the Exadata Infrastructure. The shape determines the amount of CPU, storage, and memory resources allocated to the instance.   
`oci_url` |  `str`   
Output only. Deep link to the OCI console to view this resource.   
`cpu_count` |  `int`   
Output only. The number of enabled CPU cores.   
`max_cpu_count` |  `int`   
Output only. The total number of CPU cores available.   
`memory_size_gb` |  `int`   
Output only. The memory allocated in GBs.   
`max_memory_gb` |  `int`   
Output only. The total memory available in GBs.   
`db_node_storage_size_gb` |  `int`   
Output only. The local node storage allocated in GBs.   
`max_db_node_storage_size_gb` |  `int`   
Output only. The total local node storage available in GBs.   
`data_storage_size_tb` |  `float`   
Output only. Size, in terabytes, of the DATA disk group.   
`max_data_storage_tb` |  `float`   
Output only. The total available DATA disk group size.   
`activated_storage_count` |  `int`   
Output only. The requested number of additional storage servers activated for the Exadata Infrastructure.   
`additional_storage_count` |  `int`   
Output only. The requested number of additional storage servers for the Exadata Infrastructure.   
`db_server_version` |  `str`   
Output only. The software version of the database servers (dom0) in the Exadata Infrastructure.   
`storage_server_version` |  `str`   
Output only. The software version of the storage servers (cells) in the Exadata Infrastructure.   
`next_maintenance_run_id` |  `str`   
Output only. The OCID of the next maintenance run.   
`next_maintenance_run_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time when the next maintenance run will occur.   
`next_security_maintenance_run_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time when the next security maintenance run will occur.   
`customer_contacts` |  `MutableSequence[[google.cloud.oracledatabase_v1.types.CustomerContact](https://docs.cloud.google.com/python/docs/reference/google-cloud-oracledatabase/latest/google.cloud.oracledatabase_v1.types.CustomerContact)]`   
Optional. The list of customer contacts.   
`monthly_storage_server_version` |  `str`   
Output only. The monthly software version of the storage servers (cells) in the Exadata Infrastructure. Example: 20.1.15   
`monthly_db_server_version` |  `str`   
Output only. The monthly software version of the database servers (dom0) in the Exadata Infrastructure. Example: 20.1.15   
`compute_model` |  `[google.cloud.oracledatabase_v1.types.ComputeModel](https://docs.cloud.google.com/python/docs/reference/google-cloud-oracledatabase/latest/google.cloud.oracledatabase_v1.types.ComputeModel)`   
Output only. The compute model of the Exadata Infrastructure.   
`database_server_type` |  `str`   
Optional. The database server type of the Exadata Infrastructure.   
`storage_server_type` |  `str`   
Optional. The storage server type of the Exadata Infrastructure.   
`exascale_config` |  `[google.cloud.oracledatabase_v1.types.ExascaleConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-oracledatabase/latest/google.cloud.oracledatabase_v1.types.ExascaleConfig)`   
Output only. The Exascale configuration for the Exadata Infrastructure.   
  
## Classes 

### State
    
    
    State(value)

The various lifecycle states of the Exadata Infrastructure.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
