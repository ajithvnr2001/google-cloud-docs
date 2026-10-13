---
url: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupPlanAssociation
title: Class BackupPlanAssociation (0.10.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:30:30.975343+00:00
---

# Class BackupPlanAssociation (0.10.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupPlanAssociation

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class BackupPlanAssociation (0.10.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.3 (latest)  0.10.2  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.5  0.1.7 
    
    
    BackupPlanAssociation(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A BackupPlanAssociation represents a single BackupPlanAssociation which contains details like workload, backup plan etc

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Output only. Identifier. The resource name of BackupPlanAssociation in below format Format : projects/{project}/locations/{location}/backupPlanAssociations/{backupPlanAssociationId}   
`resource_type` |  `str`   
Required. Immutable. Resource type of workload on which backupplan is applied   
`resource` |  `str`   
Required. Immutable. Resource name of workload on which the backup plan is applied. The format can either be the resource name (e.g., "projects/my-project/zones/us-central1-a/instances/my-instance") or the full resource URI (e.g., "https://www.googleapis.com/compute/v1/projects/my-project/zones/us-central1-a/instances/my-instance").   
`backup_plan` |  `str`   
Required. Resource name of backup plan which needs to be applied on workload. Format: projects/{project}/locations/{location}/backupPlans/{backupPlanId}   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time when the instance was created.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time when the instance was updated.   
`state` |  `[google.cloud.backupdr_v1.types.BackupPlanAssociation.State](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupPlanAssociation.State)`   
Output only. The BackupPlanAssociation resource state.   
`rules_config_info` |  `MutableSequence[[google.cloud.backupdr_v1.types.RuleConfigInfo](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.RuleConfigInfo)]`   
Output only. The config info related to backup rules.   
`data_source` |  `str`   
Output only. Resource name of data source which will be used as storage location for backups taken. Format : projects/{project}/locations/{location}/backupVaults/{backupvault}/dataSources/{datasource}   
`cloud_sql_instance_backup_plan_association_properties` |  `[google.cloud.backupdr_v1.types.CloudSqlInstanceBackupPlanAssociationProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.CloudSqlInstanceBackupPlanAssociationProperties)`   
Output only. Cloud SQL instance's backup plan association properties. This field is a member of `oneof`_ `resource_properties`.   
`alloydb_cluster_backup_plan_association_properties` |  `[google.cloud.backupdr_v1.types.AlloyDBClusterBackupPlanAssociationProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.AlloyDBClusterBackupPlanAssociationProperties)`   
Output only. AlloyDB cluster's backup plan association properties. This field is a member of `oneof`_ `resource_properties`.   
`backup_plan_revision_id` |  `str`   
Output only. The user friendly revision ID of the `BackupPlanRevision`. Example: v0, v1, v2, etc.   
`backup_plan_revision_name` |  `str`   
Output only. The resource id of the `BackupPlanRevision`. Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}/revisions/{revision_id}`  
  
## Classes 

### State
    
    
    State(value)

Enum for State of BackupPlan Association

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
