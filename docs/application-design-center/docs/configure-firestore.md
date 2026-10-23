---
url: https://docs.cloud.google.com/application-design-center/docs/configure-firestore/
title: Configure a Firestore database \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:29.574745+00:00
---

# Configure a Firestore database  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/configure-firestore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)



Send feedback 

#  Configure a Firestore database Stay organized with collections  Save and categorize content based on your preferences. 

App Design Center lets you configure connections and parameters for [Firestore](https://docs.cloud.google.com/firestore/native/docs/overview), a flexible, scalable NoSQL database for mobile, web, and server development. Configurable parameters are based on the [terraform-google-firestore](https://github.com/GoogleCloudPlatform/terraform-google-firestore) Terraform module.

## Component connections

The following table includes the components that you can connect to a Firestore database, and the resulting updates to your application and its generated Terraform code.

Component | Description | Background information  
---|---|---  
[Compute Engine instance templates](https://docs.cloud.google.com/application-design-center/docs/configure-compute-engine-instance) | 

  * Adds the `roles/datastore.user` IAM role to the Compute Engine instance template service account.
  * Adds the Firestore database ID to the Compute Engine instance template's metadata field.

| [Configure per-database access permissions](https://docs.cloud.google.com/firestore/native/docs/manage-databases#configure_per-database_access_permissions)  
[Cloud Run service](https://docs.cloud.google.com/application-design-center/docs/configure-cloud-run) | 

  * Adds the `roles/datastore.user` IAM role to the Cloud Run instance template service account.
  * Adds the Firestore database ID to the Cloud Run service's environment variables.

  
  
## Required configuration parameters

If your template includes a Firestore component, you must configure the following parameters before you deploy.

Parameter name | Description and constraint information | Background information  
---|---|---  
**Project ID** | The project where you want to deploy the Firestore instance. | [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects)  
**Database ID** | The ID of the Firestore database. Defaults to `(default)`. | [Database ID](https://docs.cloud.google.com/firestore/native/docs/manage-databases#database_id)  
**Region** | The location where the Firestore database is deployed. | [Locations](https://docs.cloud.google.com/firestore/docs/locations)  
  
## Optional configuration parameters

The following parameters are optional. To display advanced parameters, in the **Configuration** area, select **Show advanced fields**.

Feature | Parameter name | Description and constraint information | Background information  
---|---|---|---  
| **Database Type** | [DatabaseType](https://docs.cloud.google.com/firestore/docs/reference/rest/v1/projects.databases#databasetype) | [Choosing between Native mode and Datastore mode](https://docs.cloud.google.com/datastore/docs/firestore-or-datastore)  
| **Database Edition** | [DatabaseEdition](https://docs.cloud.google.com/firestore/docs/reference/rest/v1/projects.databases#databaseedition) | [Firestore editions overview](https://docs.cloud.google.com/firestore/native/docs/editions-overview)  
| **Concurrency Mode** | [ConcurrencyMode](https://docs.cloud.google.com/firestore/docs/reference/rest/v1/projects.databases#concurrencymode) | [Concurrency modes](https://docs.cloud.google.com/datastore/docs/concepts/transactions#concurrency_modes)  
| **Delete Protection State** | [DeleteProtectionState](https://docs.cloud.google.com/firestore/docs/reference/rest/v1/projects.databases#deleteprotectionstate) | [Delete protection](https://docs.cloud.google.com/firestore/native/docs/manage-databases#delete_protection)  
| **Kms Key Name** | [kmsKeyName](https://docs.cloud.google.com/firestore/docs/reference/rest/v1/projects.databases#CmekConfig.FIELDS.kms_key_name) | [Customer-managed encryption keys](https://docs.cloud.google.com/firestore/docs/cmek)  
| **Point In Time Recovery Enablement** | [PointInTimeRecoveryEnablement](https://docs.cloud.google.com/firestore/docs/reference/rest/v1/projects.databases#pointintimerecoveryenablement) | [Point-in-time recovery overview](https://docs.cloud.google.com/firestore/docs/pitr)  
| **Deletion Policy** | The deletion policy to be enforced when the Firestore Database is destroyed using Terraform. | [Terraform deletion_policy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/firestore_database#deletion_policy-1)  
Backup Schedule | **Weekly Recurrence Day** | [day](https://docs.cloud.google.com/firestore/docs/reference/rest/v1/projects.databases.backupSchedules#WeeklyRecurrence.FIELDS.day) | [Back up and restore data](https://docs.cloud.google.com/firestore/native/docs/backups)  
**Weekly Recurrence Retention** | [retention](https://docs.cloud.google.com/firestore/docs/reference/rest/v1/projects.databases.backupSchedules#BackupSchedule.FIELDS.retention)  
**Daily Recurrence Retention** | [retention](https://docs.cloud.google.com/firestore/docs/reference/rest/v1/projects.databases.backupSchedules#BackupSchedule.FIELDS.retention)  
Composite Index | **Index ID** | The ID of the composite index. | [Indexing overview](https://docs.cloud.google.com/firestore/native/docs/concepts/index-overview)  
**Collection** | The collection ID.  
**Query Scope** | [queryScope](https://docs.cloud.google.com/firestore/docs/reference/rest/v1/projects.databases.collectionGroups.indexes#Index.FIELDS.query_scope)  
**Api Scope** | [apiScope](https://docs.cloud.google.com/firestore/docs/reference/rest/v1/projects.databases.collectionGroups.indexes#Index.FIELDS.api_scope)  
**Density** | [density](https://docs.cloud.google.com/firestore/docs/reference/rest/v1/projects.databases.collectionGroups.indexes#Index.FIELDS.density)  
**Multikey** | [multikey](https://docs.cloud.google.com/firestore/docs/reference/rest/v1/projects.databases.collectionGroups.indexes#Index.FIELDS.multikey)  
**Field Path** | [fieldPath](https://docs.cloud.google.com/firestore/docs/reference/rest/Shared.Types/FieldOperationMetadata#IndexField.FIELDS.field_path)  
**Order** | [order](https://docs.cloud.google.com/firestore/docs/reference/rest/Shared.Types/FieldOperationMetadata#IndexField.FIELDS.order)  
**Array Config** | [arrayConfig](https://docs.cloud.google.com/firestore/docs/reference/rest/Shared.Types/FieldOperationMetadata#IndexField.FIELDS.array_config)  
**Vector Dimension** | [dimension](https://docs.cloud.google.com/firestore/docs/reference/rest/Shared.Types/FieldOperationMetadata#VectorConfig.FIELDS.dimension)  
Field Configuration | **Collection** | The collection ID. | [Single field indexes](https://docs.cloud.google.com/firestore/native/docs/concepts/index-overview#single-field_indexes)  
**Field** | [field](https://docs.cloud.google.com/firestore/docs/reference/rest/Shared.Types/FieldOperationMetadata#FIELDS.field)  
**TTL Enabled** | [TtlConfig](https://docs.cloud.google.com/firestore/docs/reference/rest/v1/projects.databases.collectionGroups.fields#TtlConfig)  
**Ascending Index Query Scope** | [IndexConfig](https://docs.cloud.google.com/firestore/docs/reference/rest/v1/projects.databases.collectionGroups.fields#IndexConfig)  
**Descending Index Query Scope** | [IndexConfig](https://docs.cloud.google.com/firestore/docs/reference/rest/v1/projects.databases.collectionGroups.fields#IndexConfig)  
**Array Index Query Scope** | [IndexConfig](https://docs.cloud.google.com/firestore/docs/reference/rest/v1/projects.databases.collectionGroups.fields#IndexConfig)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
