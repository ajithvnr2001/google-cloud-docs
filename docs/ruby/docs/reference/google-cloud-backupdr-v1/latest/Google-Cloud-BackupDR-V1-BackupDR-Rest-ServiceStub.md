---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupDR-Rest-ServiceStub/
title: Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::BackupDR::Rest::ServiceStub (v1.11.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:35:46.543033+00:00
---

# Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::BackupDR::Rest::ServiceStub (v1.11.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupDR-Rest-ServiceStub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::BackupDR::Rest::ServiceStub (v1.11.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.11.2 (latest)  1.11.1  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Backup and DR Service V1 API class Google::Cloud::BackupDR::V1::BackupDR::Rest::ServiceStub.

REST service stub for the BackupDR service. Service stub contains baseline method implementations including transcoding, making the REST call, and deserialing the response.

## Inherits

  * Object 



## Methods 

### #create_backup_plan
    
    
    def create_backup_plan(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the create_backup_plan REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::BackupDR::V1::CreateBackupPlanRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-CreateBackupPlanRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_backup_plan_association
    
    
    def create_backup_plan_association(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the create_backup_plan_association REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::BackupDR::V1::CreateBackupPlanAssociationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-CreateBackupPlanAssociationRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_backup_vault
    
    
    def create_backup_vault(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the create_backup_vault REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::BackupDR::V1::CreateBackupVaultRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-CreateBackupVaultRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_management_server
    
    
    def create_management_server(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the create_management_server REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::BackupDR::V1::CreateManagementServerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-CreateManagementServerRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_backup
    
    
    def delete_backup(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the delete_backup REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::BackupDR::V1::DeleteBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DeleteBackupRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_backup_plan
    
    
    def delete_backup_plan(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the delete_backup_plan REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::BackupDR::V1::DeleteBackupPlanRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DeleteBackupPlanRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_backup_plan_association
    
    
    def delete_backup_plan_association(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the delete_backup_plan_association REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::BackupDR::V1::DeleteBackupPlanAssociationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DeleteBackupPlanAssociationRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_backup_vault
    
    
    def delete_backup_vault(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the delete_backup_vault REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::BackupDR::V1::DeleteBackupVaultRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DeleteBackupVaultRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_management_server
    
    
    def delete_management_server(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the delete_management_server REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::BackupDR::V1::DeleteManagementServerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DeleteManagementServerRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #endpoint
    
    
    def endpoint() -> String

The effective endpoint

**Returns**

  * (String) 



### #fetch_backup_plan_associations_for_resource_type
    
    
    def fetch_backup_plan_associations_for_resource_type(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::BackupDR::V1::FetchBackupPlanAssociationsForResourceTypeResponse

Baseline implementation for the fetch_backup_plan_associations_for_resource_type REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::BackupDR::V1::FetchBackupPlanAssociationsForResourceTypeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-FetchBackupPlanAssociationsForResourceTypeRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::BackupDR::V1::FetchBackupPlanAssociationsForResourceTypeResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-FetchBackupPlanAssociationsForResourceTypeResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::FetchBackupPlanAssociationsForResourceTypeResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-FetchBackupPlanAssociationsForResourceTypeResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #fetch_backups_for_resource_type
    
    
    def fetch_backups_for_resource_type(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::BackupDR::V1::FetchBackupsForResourceTypeResponse

Baseline implementation for the fetch_backups_for_resource_type REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::BackupDR::V1::FetchBackupsForResourceTypeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-FetchBackupsForResourceTypeRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::BackupDR::V1::FetchBackupsForResourceTypeResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-FetchBackupsForResourceTypeResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::FetchBackupsForResourceTypeResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-FetchBackupsForResourceTypeResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #fetch_data_source_references_for_resource_type
    
    
    def fetch_data_source_references_for_resource_type(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::BackupDR::V1::FetchDataSourceReferencesForResourceTypeResponse

Baseline implementation for the fetch_data_source_references_for_resource_type REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::BackupDR::V1::FetchDataSourceReferencesForResourceTypeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-FetchDataSourceReferencesForResourceTypeRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::BackupDR::V1::FetchDataSourceReferencesForResourceTypeResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-FetchDataSourceReferencesForResourceTypeResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::FetchDataSourceReferencesForResourceTypeResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-FetchDataSourceReferencesForResourceTypeResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #fetch_usable_backup_vaults
    
    
    def fetch_usable_backup_vaults(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::BackupDR::V1::FetchUsableBackupVaultsResponse

Baseline implementation for the fetch_usable_backup_vaults REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::BackupDR::V1::FetchUsableBackupVaultsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-FetchUsableBackupVaultsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::BackupDR::V1::FetchUsableBackupVaultsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-FetchUsableBackupVaultsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::FetchUsableBackupVaultsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-FetchUsableBackupVaultsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_backup
    
    
    def get_backup(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::BackupDR::V1::Backup

Baseline implementation for the get_backup REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::BackupDR::V1::GetBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-GetBackupRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::BackupDR::V1::Backup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-Backup)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::Backup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-Backup)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_backup_plan
    
    
    def get_backup_plan(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::BackupDR::V1::BackupPlan

Baseline implementation for the get_backup_plan REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::BackupDR::V1::GetBackupPlanRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-GetBackupPlanRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::BackupDR::V1::BackupPlan](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupPlan)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::BackupPlan](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupPlan)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_backup_plan_association
    
    
    def get_backup_plan_association(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::BackupDR::V1::BackupPlanAssociation

Baseline implementation for the get_backup_plan_association REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::BackupDR::V1::GetBackupPlanAssociationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-GetBackupPlanAssociationRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::BackupDR::V1::BackupPlanAssociation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupPlanAssociation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::BackupPlanAssociation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupPlanAssociation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_backup_plan_revision
    
    
    def get_backup_plan_revision(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::BackupDR::V1::BackupPlanRevision

Baseline implementation for the get_backup_plan_revision REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::BackupDR::V1::GetBackupPlanRevisionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-GetBackupPlanRevisionRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::BackupDR::V1::BackupPlanRevision](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupPlanRevision)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::BackupPlanRevision](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupPlanRevision)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_backup_vault
    
    
    def get_backup_vault(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::BackupDR::V1::BackupVault

Baseline implementation for the get_backup_vault REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::BackupDR::V1::GetBackupVaultRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-GetBackupVaultRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::BackupDR::V1::BackupVault](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupVault)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::BackupVault](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupVault)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_data_source
    
    
    def get_data_source(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::BackupDR::V1::DataSource

Baseline implementation for the get_data_source REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::BackupDR::V1::GetDataSourceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-GetDataSourceRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::BackupDR::V1::DataSource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DataSource)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::DataSource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DataSource)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_data_source_reference
    
    
    def get_data_source_reference(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::BackupDR::V1::DataSourceReference

Baseline implementation for the get_data_source_reference REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::BackupDR::V1::GetDataSourceReferenceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-GetDataSourceReferenceRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::BackupDR::V1::DataSourceReference](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DataSourceReference)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::DataSourceReference](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DataSourceReference)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_management_server
    
    
    def get_management_server(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::BackupDR::V1::ManagementServer

Baseline implementation for the get_management_server REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::BackupDR::V1::GetManagementServerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-GetManagementServerRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::BackupDR::V1::ManagementServer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ManagementServer)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::ManagementServer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ManagementServer)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #initialize_service
    
    
    def initialize_service(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the initialize_service REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::BackupDR::V1::InitializeServiceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-InitializeServiceRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_backup_plan_associations
    
    
    def list_backup_plan_associations(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::BackupDR::V1::ListBackupPlanAssociationsResponse

Baseline implementation for the list_backup_plan_associations REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::BackupDR::V1::ListBackupPlanAssociationsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ListBackupPlanAssociationsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::BackupDR::V1::ListBackupPlanAssociationsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ListBackupPlanAssociationsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::ListBackupPlanAssociationsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ListBackupPlanAssociationsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_backup_plan_revisions
    
    
    def list_backup_plan_revisions(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::BackupDR::V1::ListBackupPlanRevisionsResponse

Baseline implementation for the list_backup_plan_revisions REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::BackupDR::V1::ListBackupPlanRevisionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ListBackupPlanRevisionsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::BackupDR::V1::ListBackupPlanRevisionsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ListBackupPlanRevisionsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::ListBackupPlanRevisionsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ListBackupPlanRevisionsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_backup_plans
    
    
    def list_backup_plans(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::BackupDR::V1::ListBackupPlansResponse

Baseline implementation for the list_backup_plans REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::BackupDR::V1::ListBackupPlansRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ListBackupPlansRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::BackupDR::V1::ListBackupPlansResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ListBackupPlansResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::ListBackupPlansResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ListBackupPlansResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_backup_vaults
    
    
    def list_backup_vaults(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::BackupDR::V1::ListBackupVaultsResponse

Baseline implementation for the list_backup_vaults REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::BackupDR::V1::ListBackupVaultsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ListBackupVaultsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::BackupDR::V1::ListBackupVaultsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ListBackupVaultsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::ListBackupVaultsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ListBackupVaultsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_backups
    
    
    def list_backups(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::BackupDR::V1::ListBackupsResponse

Baseline implementation for the list_backups REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::BackupDR::V1::ListBackupsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ListBackupsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::BackupDR::V1::ListBackupsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ListBackupsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::ListBackupsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ListBackupsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_data_source_references
    
    
    def list_data_source_references(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::BackupDR::V1::ListDataSourceReferencesResponse

Baseline implementation for the list_data_source_references REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::BackupDR::V1::ListDataSourceReferencesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ListDataSourceReferencesRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::BackupDR::V1::ListDataSourceReferencesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ListDataSourceReferencesResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::ListDataSourceReferencesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ListDataSourceReferencesResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_data_sources
    
    
    def list_data_sources(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::BackupDR::V1::ListDataSourcesResponse

Baseline implementation for the list_data_sources REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::BackupDR::V1::ListDataSourcesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ListDataSourcesRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::BackupDR::V1::ListDataSourcesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ListDataSourcesResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::ListDataSourcesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ListDataSourcesResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_management_servers
    
    
    def list_management_servers(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::BackupDR::V1::ListManagementServersResponse

Baseline implementation for the list_management_servers REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::BackupDR::V1::ListManagementServersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ListManagementServersRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::BackupDR::V1::ListManagementServersResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ListManagementServersResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::ListManagementServersResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ListManagementServersResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #logger
    
    
    def logger(stub: false) -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #restore_backup
    
    
    def restore_backup(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the restore_backup REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::BackupDR::V1::RestoreBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-RestoreBackupRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #trigger_backup
    
    
    def trigger_backup(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the trigger_backup REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::BackupDR::V1::TriggerBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-TriggerBackupRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_backup
    
    
    def update_backup(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the update_backup REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::BackupDR::V1::UpdateBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-UpdateBackupRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #update_backup_plan
    
    
    def update_backup_plan(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the update_backup_plan REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::BackupDR::V1::UpdateBackupPlanRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-UpdateBackupPlanRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #update_backup_plan_association
    
    
    def update_backup_plan_association(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the update_backup_plan_association REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::BackupDR::V1::UpdateBackupPlanAssociationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-UpdateBackupPlanAssociationRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #update_backup_vault
    
    
    def update_backup_vault(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the update_backup_vault REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::BackupDR::V1::UpdateBackupVaultRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-UpdateBackupVaultRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #update_data_source
    
    
    def update_data_source(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the update_data_source REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::BackupDR::V1::UpdateDataSourceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-UpdateDataSourceRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
