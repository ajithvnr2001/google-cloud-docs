---
url: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DataSourceGcpResource
title: Class DataSourceGcpResource (0.10.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:17:55.342036+00:00
---

# Class DataSourceGcpResource (0.10.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DataSourceGcpResource

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DataSourceGcpResource (0.10.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.3 (latest)  0.10.2  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.5  0.1.7 
    
    
    DataSourceGcpResource(mapping=None, *, ignore_unknown_fields=False, **kwargs)

DataSourceGcpResource is used for protected resources that are Google Cloud Resources. This name is easeier to understand than GcpResourceDataSource or GcpDataSourceResource

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`gcp_resourcename` |  `str`   
Output only. Full resource pathname URL of the source Google Cloud resource.   
`location` |  `str`   
Location of the resource:   
`type_` |  `str`   
The type of the Google Cloud resource. Use the Unified Resource Type, eg. compute.googleapis.com/Instance.   
`compute_instance_datasource_properties` |  `[google.cloud.backupdr_v1.types.ComputeInstanceDataSourceProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ComputeInstanceDataSourceProperties)`   
ComputeInstanceDataSourceProperties has a subset of Compute Instance properties that are useful at the Datasource level. This field is a member of `oneof`_ `gcp_resource_properties`.   
`cloud_sql_instance_datasource_properties` |  `[google.cloud.backupdr_v1.types.CloudSqlInstanceDataSourceProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.CloudSqlInstanceDataSourceProperties)`   
Output only. CloudSqlInstanceDataSourceProperties has a subset of Cloud SQL Instance properties that are useful at the Datasource level. This field is a member of `oneof`_ `gcp_resource_properties`.   
`alloy_db_cluster_datasource_properties` |  `[google.cloud.backupdr_v1.types.AlloyDBClusterDataSourceProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.AlloyDBClusterDataSourceProperties)`   
Output only. AlloyDBClusterDataSourceProperties has a subset of AlloyDB cluster properties that are useful at the Datasource level. This field is a member of `oneof`_ `gcp_resource_properties`.   
`disk_datasource_properties` |  `[google.cloud.backupdr_v1.types.DiskDataSourceProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DiskDataSourceProperties)`   
DiskDataSourceProperties has a subset of Disk properties that are useful at the Datasource level. This field is a member of `oneof`_ `gcp_resource_properties`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
