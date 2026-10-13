---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupDR-Paths/
title: Backup and DR Service V1 API - Module Google::Cloud::BackupDR::V1::BackupDR::Paths (v1.11.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:47:32.351111+00:00
---

# Backup and DR Service V1 API - Module Google::Cloud::BackupDR::V1::BackupDR::Paths (v1.11.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupDR-Paths/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Backup and DR Service V1 API - Module Google::Cloud::BackupDR::V1::BackupDR::Paths (v1.11.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.11.2 (latest)  1.11.1  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Backup and DR Service V1 API module Google::Cloud::BackupDR::V1::BackupDR::Paths.

Path helper methods for the BackupDR API.

## Extended By

  * [Google::Cloud::BackupDR::V1::BackupDR::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupDR-Paths)



## Included In

  * [Google::Cloud::BackupDR::V1::BackupDR::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupDR-Client)
  * [Google::Cloud::BackupDR::V1::BackupDR::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupDR-Paths)
  * [Google::Cloud::BackupDR::V1::BackupDR::Rest::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupDR-Rest-Client)



## Methods 

### #backup_path
    
    
    def backup_path(project:, location:, backupvault:, datasource:, backup:) -> ::String

Create a fully-qualified Backup resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/backupVaults/{backupvault}/dataSources/{datasource}/backups/{backup}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **backupvault** (String) 
  * **datasource** (String) 
  * **backup** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #backup_plan_association_path
    
    
    def backup_plan_association_path(project:, location:, backup_plan_association:) -> ::String

Create a fully-qualified BackupPlanAssociation resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/backupPlanAssociations/{backup_plan_association}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **backup_plan_association** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #backup_plan_path
    
    
    def backup_plan_path(project:, location:, backup_plan:) -> ::String

Create a fully-qualified BackupPlan resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/backupPlans/{backup_plan}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **backup_plan** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #backup_plan_revision_path
    
    
    def backup_plan_revision_path(project:, location:, backup_plan:, revision:) -> ::String

Create a fully-qualified BackupPlanRevision resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/backupPlans/{backup_plan}/revisions/{revision}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **backup_plan** (String) 
  * **revision** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #backup_vault_path
    
    
    def backup_vault_path(project:, location:, backupvault:) -> ::String

Create a fully-qualified BackupVault resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/backupVaults/{backupvault}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **backupvault** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #cluster_path
    
    
    def cluster_path(project:, location:, cluster:) -> ::String

Create a fully-qualified Cluster resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/clusters/{cluster}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **cluster** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #crypto_key_path
    
    
    def crypto_key_path(project:, location:, ring:, key:) -> ::String

Create a fully-qualified CryptoKey resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/keyRings/{ring}/cryptoKeys/{key}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **ring** (String) 
  * **key** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #crypto_key_version_path
    
    
    def crypto_key_version_path(project:, location:, key_ring:, crypto_key:, crypto_key_version:) -> ::String

Create a fully-qualified CryptoKeyVersion resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}/cryptoKeyVersions/{crypto_key_version}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **key_ring** (String) 
  * **crypto_key** (String) 
  * **crypto_key_version** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #data_source_path
    
    
    def data_source_path(project:, location:, backupvault:, datasource:) -> ::String

Create a fully-qualified DataSource resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/backupVaults/{backupvault}/dataSources/{datasource}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **backupvault** (String) 
  * **datasource** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #data_source_reference_path
    
    
    def data_source_reference_path(project:, location:, data_source_reference:) -> ::String

Create a fully-qualified DataSourceReference resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/dataSourceReferences/{data_source_reference}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **data_source_reference** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #instance_path
    
    
    def instance_path(project:, instance:) -> ::String

Create a fully-qualified Instance resource string.

The resource will be in the following format:

`projects/{project}/instances/{instance}`

**Parameters**

  * **project** (String) 
  * **instance** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #location_path
    
    
    def location_path(project:, location:) -> ::String

Create a fully-qualified Location resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}`

**Parameters**

  * **project** (String) 
  * **location** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #management_server_path
    
    
    def management_server_path(project:, location:, managementserver:) -> ::String

Create a fully-qualified ManagementServer resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/managementServers/{managementserver}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **managementserver** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #storage_pool_path
    
    
    def storage_pool_path(project:, zone:, storage_pool:) -> ::String

Create a fully-qualified StoragePool resource string.

The resource will be in the following format:

`projects/{project}/zones/{zone}/storagePools/{storage_pool}`

**Parameters**

  * **project** (String) 
  * **zone** (String) 
  * **storage_pool** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
