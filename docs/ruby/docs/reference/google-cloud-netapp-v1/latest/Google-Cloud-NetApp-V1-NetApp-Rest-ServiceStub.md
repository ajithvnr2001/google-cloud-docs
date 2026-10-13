---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-NetApp-Rest-ServiceStub/
title: NetApp V1 API - Class Google::Cloud::NetApp::V1::NetApp::Rest::ServiceStub (v2.12.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:52:28.053653+00:00
---

# NetApp V1 API - Class Google::Cloud::NetApp::V1::NetApp::Rest::ServiceStub (v2.12.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-NetApp-Rest-ServiceStub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  NetApp V1 API - Class Google::Cloud::NetApp::V1::NetApp::Rest::ServiceStub (v2.12.2) Stay organized with collections  Save and categorize content based on your preferences. 

2.12.2 (latest)  2.12.1  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.1  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.2  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.1  1.0.0  0.6.0  0.5.2  0.4.2  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the NetApp V1 API class Google::Cloud::NetApp::V1::NetApp::Rest::ServiceStub.

REST service stub for the NetApp service. Service stub contains baseline method implementations including transcoding, making the REST call, and deserialing the response.

## Inherits

  * Object 



## Methods 

### #create_active_directory
    
    
    def create_active_directory(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the create_active_directory REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::CreateActiveDirectoryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-CreateActiveDirectoryRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_backup
    
    
    def create_backup(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the create_backup REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::CreateBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-CreateBackupRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_backup_policy
    
    
    def create_backup_policy(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the create_backup_policy REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::CreateBackupPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-CreateBackupPolicyRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_backup_vault
    
    
    def create_backup_vault(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the create_backup_vault REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::CreateBackupVaultRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-CreateBackupVaultRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_host_group
    
    
    def create_host_group(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the create_host_group REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::CreateHostGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-CreateHostGroupRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_kms_config
    
    
    def create_kms_config(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the create_kms_config REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::CreateKmsConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-CreateKmsConfigRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_quota_rule
    
    
    def create_quota_rule(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the create_quota_rule REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::CreateQuotaRuleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-CreateQuotaRuleRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_replication
    
    
    def create_replication(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the create_replication REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::CreateReplicationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-CreateReplicationRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_snapshot
    
    
    def create_snapshot(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the create_snapshot REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::CreateSnapshotRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-CreateSnapshotRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_storage_pool
    
    
    def create_storage_pool(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the create_storage_pool REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::CreateStoragePoolRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-CreateStoragePoolRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_volume
    
    
    def create_volume(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the create_volume REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::CreateVolumeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-CreateVolumeRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_active_directory
    
    
    def delete_active_directory(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the delete_active_directory REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::DeleteActiveDirectoryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-DeleteActiveDirectoryRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_backup
    
    
    def delete_backup(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the delete_backup REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::DeleteBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-DeleteBackupRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_backup_policy
    
    
    def delete_backup_policy(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the delete_backup_policy REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::DeleteBackupPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-DeleteBackupPolicyRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_backup_vault
    
    
    def delete_backup_vault(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the delete_backup_vault REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::DeleteBackupVaultRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-DeleteBackupVaultRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_host_group
    
    
    def delete_host_group(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the delete_host_group REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::DeleteHostGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-DeleteHostGroupRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_kms_config
    
    
    def delete_kms_config(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the delete_kms_config REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::DeleteKmsConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-DeleteKmsConfigRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_quota_rule
    
    
    def delete_quota_rule(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the delete_quota_rule REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::DeleteQuotaRuleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-DeleteQuotaRuleRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_replication
    
    
    def delete_replication(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the delete_replication REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::DeleteReplicationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-DeleteReplicationRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_snapshot
    
    
    def delete_snapshot(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the delete_snapshot REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::DeleteSnapshotRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-DeleteSnapshotRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_storage_pool
    
    
    def delete_storage_pool(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the delete_storage_pool REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::DeleteStoragePoolRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-DeleteStoragePoolRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_volume
    
    
    def delete_volume(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the delete_volume REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::DeleteVolumeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-DeleteVolumeRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #encrypt_volumes
    
    
    def encrypt_volumes(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the encrypt_volumes REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::EncryptVolumesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-EncryptVolumesRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #endpoint
    
    
    def endpoint() -> String

The effective endpoint

**Returns**

  * (String) 



### #establish_peering
    
    
    def establish_peering(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the establish_peering REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::EstablishPeeringRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-EstablishPeeringRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #establish_volume_peering
    
    
    def establish_volume_peering(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the establish_volume_peering REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::EstablishVolumePeeringRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-EstablishVolumePeeringRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #execute_ontap_delete
    
    
    def execute_ontap_delete(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::NetApp::V1::ExecuteOntapDeleteResponse

Baseline implementation for the execute_ontap_delete REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::ExecuteOntapDeleteRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ExecuteOntapDeleteRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::NetApp::V1::ExecuteOntapDeleteResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ExecuteOntapDeleteResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::NetApp::V1::ExecuteOntapDeleteResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ExecuteOntapDeleteResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #execute_ontap_get
    
    
    def execute_ontap_get(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::NetApp::V1::ExecuteOntapGetResponse

Baseline implementation for the execute_ontap_get REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::ExecuteOntapGetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ExecuteOntapGetRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::NetApp::V1::ExecuteOntapGetResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ExecuteOntapGetResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::NetApp::V1::ExecuteOntapGetResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ExecuteOntapGetResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #execute_ontap_patch
    
    
    def execute_ontap_patch(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::NetApp::V1::ExecuteOntapPatchResponse

Baseline implementation for the execute_ontap_patch REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::ExecuteOntapPatchRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ExecuteOntapPatchRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::NetApp::V1::ExecuteOntapPatchResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ExecuteOntapPatchResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::NetApp::V1::ExecuteOntapPatchResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ExecuteOntapPatchResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #execute_ontap_post
    
    
    def execute_ontap_post(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::NetApp::V1::ExecuteOntapPostResponse

Baseline implementation for the execute_ontap_post REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::ExecuteOntapPostRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ExecuteOntapPostRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::NetApp::V1::ExecuteOntapPostResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ExecuteOntapPostResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::NetApp::V1::ExecuteOntapPostResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ExecuteOntapPostResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_active_directory
    
    
    def get_active_directory(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::NetApp::V1::ActiveDirectory

Baseline implementation for the get_active_directory REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::GetActiveDirectoryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-GetActiveDirectoryRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::NetApp::V1::ActiveDirectory](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ActiveDirectory)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::NetApp::V1::ActiveDirectory](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ActiveDirectory)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_backup
    
    
    def get_backup(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::NetApp::V1::Backup

Baseline implementation for the get_backup REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::GetBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-GetBackupRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::NetApp::V1::Backup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-Backup)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::NetApp::V1::Backup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-Backup)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_backup_policy
    
    
    def get_backup_policy(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::NetApp::V1::BackupPolicy

Baseline implementation for the get_backup_policy REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::GetBackupPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-GetBackupPolicyRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::NetApp::V1::BackupPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-BackupPolicy)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::NetApp::V1::BackupPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-BackupPolicy)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_backup_vault
    
    
    def get_backup_vault(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::NetApp::V1::BackupVault

Baseline implementation for the get_backup_vault REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::GetBackupVaultRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-GetBackupVaultRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::NetApp::V1::BackupVault](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-BackupVault)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::NetApp::V1::BackupVault](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-BackupVault)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_host_group
    
    
    def get_host_group(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::NetApp::V1::HostGroup

Baseline implementation for the get_host_group REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::GetHostGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-GetHostGroupRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::NetApp::V1::HostGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-HostGroup)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::NetApp::V1::HostGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-HostGroup)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_kms_config
    
    
    def get_kms_config(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::NetApp::V1::KmsConfig

Baseline implementation for the get_kms_config REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::GetKmsConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-GetKmsConfigRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::NetApp::V1::KmsConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-KmsConfig)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::NetApp::V1::KmsConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-KmsConfig)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_quota_rule
    
    
    def get_quota_rule(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::NetApp::V1::QuotaRule

Baseline implementation for the get_quota_rule REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::GetQuotaRuleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-GetQuotaRuleRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::NetApp::V1::QuotaRule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-QuotaRule)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::NetApp::V1::QuotaRule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-QuotaRule)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_replication
    
    
    def get_replication(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::NetApp::V1::Replication

Baseline implementation for the get_replication REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::GetReplicationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-GetReplicationRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::NetApp::V1::Replication](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-Replication)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::NetApp::V1::Replication](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-Replication)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_snapshot
    
    
    def get_snapshot(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::NetApp::V1::Snapshot

Baseline implementation for the get_snapshot REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::GetSnapshotRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-GetSnapshotRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::NetApp::V1::Snapshot](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-Snapshot)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::NetApp::V1::Snapshot](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-Snapshot)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_storage_pool
    
    
    def get_storage_pool(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::NetApp::V1::StoragePool

Baseline implementation for the get_storage_pool REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::GetStoragePoolRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-GetStoragePoolRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::NetApp::V1::StoragePool](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-StoragePool)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::NetApp::V1::StoragePool](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-StoragePool)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_volume
    
    
    def get_volume(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::NetApp::V1::Volume

Baseline implementation for the get_volume REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::GetVolumeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-GetVolumeRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::NetApp::V1::Volume](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-Volume)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::NetApp::V1::Volume](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-Volume)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_active_directories
    
    
    def list_active_directories(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::NetApp::V1::ListActiveDirectoriesResponse

Baseline implementation for the list_active_directories REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::ListActiveDirectoriesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ListActiveDirectoriesRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::NetApp::V1::ListActiveDirectoriesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ListActiveDirectoriesResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::NetApp::V1::ListActiveDirectoriesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ListActiveDirectoriesResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_backup_policies
    
    
    def list_backup_policies(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::NetApp::V1::ListBackupPoliciesResponse

Baseline implementation for the list_backup_policies REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::ListBackupPoliciesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ListBackupPoliciesRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::NetApp::V1::ListBackupPoliciesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ListBackupPoliciesResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::NetApp::V1::ListBackupPoliciesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ListBackupPoliciesResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_backup_vaults
    
    
    def list_backup_vaults(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::NetApp::V1::ListBackupVaultsResponse

Baseline implementation for the list_backup_vaults REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::ListBackupVaultsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ListBackupVaultsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::NetApp::V1::ListBackupVaultsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ListBackupVaultsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::NetApp::V1::ListBackupVaultsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ListBackupVaultsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_backups
    
    
    def list_backups(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::NetApp::V1::ListBackupsResponse

Baseline implementation for the list_backups REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::ListBackupsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ListBackupsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::NetApp::V1::ListBackupsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ListBackupsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::NetApp::V1::ListBackupsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ListBackupsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_host_groups
    
    
    def list_host_groups(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::NetApp::V1::ListHostGroupsResponse

Baseline implementation for the list_host_groups REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::ListHostGroupsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ListHostGroupsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::NetApp::V1::ListHostGroupsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ListHostGroupsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::NetApp::V1::ListHostGroupsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ListHostGroupsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_kms_configs
    
    
    def list_kms_configs(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::NetApp::V1::ListKmsConfigsResponse

Baseline implementation for the list_kms_configs REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::ListKmsConfigsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ListKmsConfigsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::NetApp::V1::ListKmsConfigsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ListKmsConfigsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::NetApp::V1::ListKmsConfigsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ListKmsConfigsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_quota_rules
    
    
    def list_quota_rules(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::NetApp::V1::ListQuotaRulesResponse

Baseline implementation for the list_quota_rules REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::ListQuotaRulesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ListQuotaRulesRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::NetApp::V1::ListQuotaRulesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ListQuotaRulesResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::NetApp::V1::ListQuotaRulesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ListQuotaRulesResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_replications
    
    
    def list_replications(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::NetApp::V1::ListReplicationsResponse

Baseline implementation for the list_replications REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::ListReplicationsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ListReplicationsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::NetApp::V1::ListReplicationsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ListReplicationsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::NetApp::V1::ListReplicationsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ListReplicationsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_snapshots
    
    
    def list_snapshots(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::NetApp::V1::ListSnapshotsResponse

Baseline implementation for the list_snapshots REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::ListSnapshotsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ListSnapshotsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::NetApp::V1::ListSnapshotsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ListSnapshotsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::NetApp::V1::ListSnapshotsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ListSnapshotsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_storage_pools
    
    
    def list_storage_pools(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::NetApp::V1::ListStoragePoolsResponse

Baseline implementation for the list_storage_pools REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::ListStoragePoolsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ListStoragePoolsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::NetApp::V1::ListStoragePoolsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ListStoragePoolsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::NetApp::V1::ListStoragePoolsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ListStoragePoolsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_volumes
    
    
    def list_volumes(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::NetApp::V1::ListVolumesResponse

Baseline implementation for the list_volumes REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::ListVolumesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ListVolumesRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::NetApp::V1::ListVolumesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ListVolumesResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::NetApp::V1::ListVolumesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ListVolumesResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #logger
    
    
    def logger(stub: false) -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #restore_backup_files
    
    
    def restore_backup_files(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the restore_backup_files REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::RestoreBackupFilesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-RestoreBackupFilesRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #resume_replication
    
    
    def resume_replication(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the resume_replication REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::ResumeReplicationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ResumeReplicationRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #reverse_replication_direction
    
    
    def reverse_replication_direction(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the reverse_replication_direction REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::ReverseReplicationDirectionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ReverseReplicationDirectionRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #revert_volume
    
    
    def revert_volume(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the revert_volume REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::RevertVolumeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-RevertVolumeRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #stop_replication
    
    
    def stop_replication(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the stop_replication REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::StopReplicationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-StopReplicationRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #switch_active_replica_zone
    
    
    def switch_active_replica_zone(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the switch_active_replica_zone REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::SwitchActiveReplicaZoneRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-SwitchActiveReplicaZoneRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #sync_replication
    
    
    def sync_replication(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the sync_replication REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::SyncReplicationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-SyncReplicationRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_active_directory
    
    
    def update_active_directory(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the update_active_directory REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::UpdateActiveDirectoryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-UpdateActiveDirectoryRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #update_backup
    
    
    def update_backup(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the update_backup REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::UpdateBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-UpdateBackupRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #update_backup_policy
    
    
    def update_backup_policy(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the update_backup_policy REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::UpdateBackupPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-UpdateBackupPolicyRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #update_backup_vault
    
    
    def update_backup_vault(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the update_backup_vault REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::UpdateBackupVaultRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-UpdateBackupVaultRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #update_host_group
    
    
    def update_host_group(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the update_host_group REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::UpdateHostGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-UpdateHostGroupRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #update_kms_config
    
    
    def update_kms_config(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the update_kms_config REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::UpdateKmsConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-UpdateKmsConfigRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #update_quota_rule
    
    
    def update_quota_rule(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the update_quota_rule REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::UpdateQuotaRuleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-UpdateQuotaRuleRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #update_replication
    
    
    def update_replication(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the update_replication REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::UpdateReplicationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-UpdateReplicationRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #update_snapshot
    
    
    def update_snapshot(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the update_snapshot REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::UpdateSnapshotRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-UpdateSnapshotRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #update_storage_pool
    
    
    def update_storage_pool(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the update_storage_pool REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::UpdateStoragePoolRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-UpdateStoragePoolRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #update_volume
    
    
    def update_volume(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the update_volume REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::UpdateVolumeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-UpdateVolumeRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #validate_directory_service
    
    
    def validate_directory_service(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the validate_directory_service REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::ValidateDirectoryServiceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ValidateDirectoryServiceRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #verify_kms_config
    
    
    def verify_kms_config(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::NetApp::V1::VerifyKmsConfigResponse

Baseline implementation for the verify_kms_config REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::NetApp::V1::VerifyKmsConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-VerifyKmsConfigRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::NetApp::V1::VerifyKmsConfigResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-VerifyKmsConfigResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::NetApp::V1::VerifyKmsConfigResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-VerifyKmsConfigResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
