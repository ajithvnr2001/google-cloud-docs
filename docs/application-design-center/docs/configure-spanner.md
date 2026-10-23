---
url: https://docs.cloud.google.com/application-design-center/docs/configure-spanner/
title: Configure a Spanner instance \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:21.015030+00:00
---

# Configure a Spanner instance  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/configure-spanner/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)



Send feedback 

#  Configure a Spanner instance Stay organized with collections  Save and categorize content based on your preferences. 

App Design Center lets you configure connections and parameters for [Spanner instances](https://docs.cloud.google.com/spanner/docs/instances), a fully managed database service that combines relational, graph, key-value, and search capabilities with global transactional consistency and synchronous replication. You can configure instances supporting GoogleSQL or PostgreSQL dialects based on the [terraform-google-cloud-spanner](https://github.com/GoogleCloudPlatform/terraform-google-cloud-spanner) Terraform module.

## Component connections

The following table includes the components that you can connect to a Spanner instance, and the resulting updates to your application and its generated Terraform code.

Connected component | Application updates | Background information  
---|---|---  
[Compute Engine instance template](https://docs.cloud.google.com/application-design-center/docs/configure-compute-engine-instance) | 

  * The Compute Engine instances can read and write data in the Spanner instance.
  * The `roles/spanner.databaseAdmin` role is added to the Compute Engine instance template service account.
  * The Compute Engine service account is added as an IAM user to the Spanner instance.

| [Using Spanner in a virtual machine instance](https://docs.cloud.google.com/spanner/docs/configure-virtual-machine-instance)  
[Service account](https://docs.cloud.google.com/application-design-center/docs/configure-service-account) | 

  * The service account has access to the Spanner instance.
  * The service account is added as an IAM user to the Spanner instance.

| [Configure an instance with a service account](https://docs.cloud.google.com/spanner/docs/configure-virtual-machine-instance#service-account)  
[Cloud Run](https://docs.cloud.google.com/application-design-center/docs/configure-cloud-run) | 

  * The Cloud Run service can manage the Spanner instance.
  * The Spanner connection details are added to the Cloud Run environment variables.
  * The `roles/spanner.databaseAdmin` role is added to the Cloud Run service account.
  * The Cloud Run service account IAM information is added to the Spanner instance.

| [Connect to Google Cloud services](https://docs.cloud.google.com/run/docs/integrate/using-gcp-services)  
  
## Required configuration parameters

If your template contains a Spanner component, you must configure the following parameters before you deploy.

Parameter name | Description and constraints | Background information  
---|---|---  
**Project ID** | The project where you want to deploy the Spanner instance. | [Configure components](https://docs.cloud.google.com/application-design-center/docs/design-application-templates#configure_components)  
**Instance Name** | A unique identifier for the instance, which cannot be changed after the instance is created. The name must be between 6 and 30 characters in length. | [name](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/spanner_instance#name-1)  
**Instance Config** | [config](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances#Instance.FIELDS.config) | [Instance configurations](https://docs.cloud.google.com/spanner/docs/instances#configuration)  
  
## Optional configuration parameters

The following parameters are optional. To display advanced parameters, in the **Configuration** area, select **Show advanced fields**.

Feature | Parameter name | Description and constraint information | Background information  
---|---|---|---  
Instance Size | **Num Nodes** | [nodeCount](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances#Instance.FIELDS.node_count) | [Compute capacity, nodes and processing units](https://docs.cloud.google.com/spanner/docs/compute-capacity)  
**Processing Units** | [processingUnits](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances#Instance.FIELDS.processing_units) | [Compute capacity, nodes and processing units](https://docs.cloud.google.com/spanner/docs/compute-capacity)  
| **Instance Display Name** | [displayName](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances#Instance.FIELDS.display_name) | [Change the display name](https://docs.cloud.google.com/spanner/docs/create-manage-instances#change-display-name)  
| **Create Instance** | By default, a new Spanner instance is created. Clear the checkbox if you want to avoid creating a new instance and use an existing one instead. | [Create and manage instances](https://docs.cloud.google.com/spanner/docs/create-manage-instances)  
| **Enable Autoscaling** | Select to enable autoscaling on the Spanner instance.  | [Autoscaling overview](https://docs.cloud.google.com/spanner/docs/autoscaling-overview)  
| **Instance IAM** | A comma-separated list of permissions on the instance. For example, `user:user1@cymbalgroup.com=>roles/spanner.databaseAdmin, user:user2@cymbalgroup.com=>roles/spanner.databaseAdmin` | [IAM overview](https://docs.cloud.google.com/spanner/docs/iam)  
Instance Labels | **Key** | [labels](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances#Instance.FIELDS.labels) | [Label an instance](https://docs.cloud.google.com/spanner/docs/create-manage-instances#label-instance)  
**Value** | [labels](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances#Instance.FIELDS.labels) | [Label an instance](https://docs.cloud.google.com/spanner/docs/create-manage-instances#label-instance)  
Database Config | **Key** | The `database_config` map object key. | [database_config](https://github.com/GoogleCloudPlatform/terraform-google-cloud-spanner/tree/main?tab=readme-ov-file#inputs)  
**Version Retention Period** | [versionRetentionPeriod](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases#Database.FIELDS.version_retention_period) | [Point-in-time (PITR) recovery overview](https://docs.cloud.google.com/spanner/docs/pitr)  
**DDL** | [ddl](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/spanner_database#ddl-1) | [GoogleSQL](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/data-definition-language#alter-database) or [PostgreSQL](https://docs.cloud.google.com/spanner/docs/reference/postgresql/data-definition-language#alter-database)  
**KMS Key Name** | [kmsKeyName](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases#EncryptionConfig.FIELDS.kms_key_name) | [Customer-managed encryption keys (CMEK) overview](https://docs.cloud.google.com/spanner/docs/cmek)  
**Deletion Protection** | Select to prevent Terraform from deleting the database. | [deletion_protection](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/spanner_database#deletion_protection-1)  
**Database IAM** | A comma-separated list of permissions on the database. For example, `user:user1@cymbalgroup.com=>roles/spanner.databaseAdmin, user:user2@cymbalgroup.com=>roles/spanner.databaseAdmin` | [IAM overview](https://docs.cloud.google.com/spanner/docs/iam)  
**Enable Backup** | By default, an automated database backup is created. If you don't want a backup, clear the checkbox. | [Backups overview](https://docs.cloud.google.com/spanner/docs/backup)  
**Backup Retention** | [retentionDuration](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.backupSchedules#BackupSchedule.FIELDS.retention_duration) | [Incremental backups](https://docs.cloud.google.com/spanner/docs/backup#incremental-backups)  
**Create DB** | By default, a database is created. If you don't want a database, clear the checkbox. | [Databases overview](https://docs.cloud.google.com/spanner/docs/databases)  
| **Cron Spec Text** | [text](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.backupSchedules#CrontabSpec.FIELDS.text) | [Create and manage backup schedules](https://docs.cloud.google.com/spanner/docs/backup/create-manage-backup-schedules)  
| **Min Processing Units** | [minProcessingUnits](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances#AutoscalingLimits.FIELDS.min_processing_units) | [Managed autoscaler](https://docs.cloud.google.com/spanner/docs/managed-autoscaler)  
| **Max Processing Units** | [maxProcessingUnits](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances#AutoscalingLimits.FIELDS.max_processing_units) | [Managed autoscaler](https://docs.cloud.google.com/spanner/docs/managed-autoscaler)  
| **Min Nodes** | [minNodes](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances#AutoscalingLimits.FIELDS.min_nodes) | [Managed autoscaler](https://docs.cloud.google.com/spanner/docs/managed-autoscaler)  
| **Max Nodes** | [maxNodes](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances#AutoscalingLimits.FIELDS.max_nodes) | [Managed autoscaler](https://docs.cloud.google.com/spanner/docs/managed-autoscaler)  
| **High Priority CPU Utilization Percent** | [highPriorityCpuUtilizationPercent](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances#AutoscalingTargets.FIELDS.high_priority_cpu_utilization_percent) | [Managed autoscaler](https://docs.cloud.google.com/spanner/docs/managed-autoscaler)  
| **Storage Utilization Percent** | [storageUtilizationPercent](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances#AutoscalingTargets.FIELDS.storage_utilization_percent) | [Managed autoscaler](https://docs.cloud.google.com/spanner/docs/managed-autoscaler)  
| **Replica Location** | [location](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances#ReplicaSelection.FIELDS.location) | [Asymmetric read-only autoscaling](https://docs.cloud.google.com/spanner/docs/managed-autoscaler#asymmetric-read-only-autoscaling)  
| **Override Min Nodes** | [AutoscalingConfigOverrides](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances#autoscalingconfigoverrides) | [Managed autoscaler parameters](https://docs.cloud.google.com/spanner/docs/managed-autoscaler#autoscaler-parameters)  
| **Override Max Nodes** | [AutoscalingConfigOverrides](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances#autoscalingconfigoverrides) | [Managed autoscaler parameters](https://docs.cloud.google.com/spanner/docs/managed-autoscaler#autoscaler-parameters)  
| **Edition** | [Edition](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances#edition) | [Spanner editions overview](https://docs.cloud.google.com/spanner/docs/editions-overview)  
| **Default Backup Schedule Type** | [defaultBackupScheduleType](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances#Instance.FIELDS.default_backup_schedule_type) | [Default backup schedules](https://docs.cloud.google.com/spanner/docs/backup#default-backup-schedules)  
| **Force Destroy** | Select to delete backups when you delete the Spanner instance. | [force_destroy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/spanner_instance#force_destroy-1)  
| **Use Full Backup Spec** | [fullBackupSpec](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.backupSchedules#BackupSchedule.FIELDS.full_backup_spec) | [Backup schedules](https://docs.cloud.google.com/spanner/docs/backup#how-backup-creation-works)  
| **Use Incremental Backup Spec** | [incrementalBackupSpec](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.backupSchedules#BackupSchedule.FIELDS.incremental_backup_spec) | [Incremental backups](https://docs.cloud.google.com/spanner/docs/backup#incremental-backups)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
