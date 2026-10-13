---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-Memorystore-Rest-ServiceStub/
title: Memorystore V1 API - Class Google::Cloud::Memorystore::V1::Memorystore::Rest::ServiceStub (v1.11.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:42:39.871860+00:00
---

# Memorystore V1 API - Class Google::Cloud::Memorystore::V1::Memorystore::Rest::ServiceStub (v1.11.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-Memorystore-Rest-ServiceStub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Memorystore V1 API - Class Google::Cloud::Memorystore::V1::Memorystore::Rest::ServiceStub (v1.11.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.11.1 (latest)  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.1  1.0.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Memorystore V1 API class Google::Cloud::Memorystore::V1::Memorystore::Rest::ServiceStub.

REST service stub for the Memorystore service. Service stub contains baseline method implementations including transcoding, making the REST call, and deserialing the response.

## Inherits

  * Object 



## Methods 

### #add_auth_token
    
    
    def add_auth_token(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the add_auth_token REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Memorystore::V1::AddAuthTokenRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-AddAuthTokenRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #add_token_auth_user
    
    
    def add_token_auth_user(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the add_token_auth_user REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Memorystore::V1::AddTokenAuthUserRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-AddTokenAuthUserRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #backup_instance
    
    
    def backup_instance(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the backup_instance REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Memorystore::V1::BackupInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-BackupInstanceRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_instance
    
    
    def create_instance(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the create_instance REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Memorystore::V1::CreateInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-CreateInstanceRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_auth_token
    
    
    def delete_auth_token(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the delete_auth_token REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Memorystore::V1::DeleteAuthTokenRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-DeleteAuthTokenRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_backup
    
    
    def delete_backup(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the delete_backup REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Memorystore::V1::DeleteBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-DeleteBackupRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_instance
    
    
    def delete_instance(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the delete_instance REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Memorystore::V1::DeleteInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-DeleteInstanceRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_token_auth_user
    
    
    def delete_token_auth_user(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the delete_token_auth_user REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Memorystore::V1::DeleteTokenAuthUserRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-DeleteTokenAuthUserRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #endpoint
    
    
    def endpoint() -> String

The effective endpoint

**Returns**

  * (String) 



### #export_backup
    
    
    def export_backup(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the export_backup REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Memorystore::V1::ExportBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-ExportBackupRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #finish_migration
    
    
    def finish_migration(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the finish_migration REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Memorystore::V1::FinishMigrationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-FinishMigrationRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_auth_token
    
    
    def get_auth_token(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Memorystore::V1::AuthToken

Baseline implementation for the get_auth_token REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Memorystore::V1::GetAuthTokenRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-GetAuthTokenRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Memorystore::V1::AuthToken](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-AuthToken)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Memorystore::V1::AuthToken](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-AuthToken)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_backup
    
    
    def get_backup(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Memorystore::V1::Backup

Baseline implementation for the get_backup REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Memorystore::V1::GetBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-GetBackupRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Memorystore::V1::Backup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-Backup)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Memorystore::V1::Backup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-Backup)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_backup_collection
    
    
    def get_backup_collection(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Memorystore::V1::BackupCollection

Baseline implementation for the get_backup_collection REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Memorystore::V1::GetBackupCollectionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-GetBackupCollectionRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Memorystore::V1::BackupCollection](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-BackupCollection)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Memorystore::V1::BackupCollection](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-BackupCollection)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_certificate_authority
    
    
    def get_certificate_authority(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Memorystore::V1::CertificateAuthority

Baseline implementation for the get_certificate_authority REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Memorystore::V1::GetCertificateAuthorityRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-GetCertificateAuthorityRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Memorystore::V1::CertificateAuthority](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-CertificateAuthority)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Memorystore::V1::CertificateAuthority](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-CertificateAuthority)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_instance
    
    
    def get_instance(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Memorystore::V1::Instance

Baseline implementation for the get_instance REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Memorystore::V1::GetInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-GetInstanceRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Memorystore::V1::Instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-Instance)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Memorystore::V1::Instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-Instance)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_shared_regional_certificate_authority
    
    
    def get_shared_regional_certificate_authority(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Memorystore::V1::SharedRegionalCertificateAuthority

Baseline implementation for the get_shared_regional_certificate_authority REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Memorystore::V1::GetSharedRegionalCertificateAuthorityRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-GetSharedRegionalCertificateAuthorityRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Memorystore::V1::SharedRegionalCertificateAuthority](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-SharedRegionalCertificateAuthority)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Memorystore::V1::SharedRegionalCertificateAuthority](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-SharedRegionalCertificateAuthority)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_token_auth_user
    
    
    def get_token_auth_user(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Memorystore::V1::TokenAuthUser

Baseline implementation for the get_token_auth_user REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Memorystore::V1::GetTokenAuthUserRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-GetTokenAuthUserRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Memorystore::V1::TokenAuthUser](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-TokenAuthUser)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Memorystore::V1::TokenAuthUser](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-TokenAuthUser)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_auth_tokens
    
    
    def list_auth_tokens(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Memorystore::V1::ListAuthTokensResponse

Baseline implementation for the list_auth_tokens REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Memorystore::V1::ListAuthTokensRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-ListAuthTokensRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Memorystore::V1::ListAuthTokensResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-ListAuthTokensResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Memorystore::V1::ListAuthTokensResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-ListAuthTokensResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_backup_collections
    
    
    def list_backup_collections(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Memorystore::V1::ListBackupCollectionsResponse

Baseline implementation for the list_backup_collections REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Memorystore::V1::ListBackupCollectionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-ListBackupCollectionsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Memorystore::V1::ListBackupCollectionsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-ListBackupCollectionsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Memorystore::V1::ListBackupCollectionsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-ListBackupCollectionsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_backups
    
    
    def list_backups(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Memorystore::V1::ListBackupsResponse

Baseline implementation for the list_backups REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Memorystore::V1::ListBackupsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-ListBackupsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Memorystore::V1::ListBackupsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-ListBackupsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Memorystore::V1::ListBackupsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-ListBackupsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_instances
    
    
    def list_instances(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Memorystore::V1::ListInstancesResponse

Baseline implementation for the list_instances REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Memorystore::V1::ListInstancesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-ListInstancesRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Memorystore::V1::ListInstancesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-ListInstancesResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Memorystore::V1::ListInstancesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-ListInstancesResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_token_auth_users
    
    
    def list_token_auth_users(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Memorystore::V1::ListTokenAuthUsersResponse

Baseline implementation for the list_token_auth_users REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Memorystore::V1::ListTokenAuthUsersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-ListTokenAuthUsersRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Memorystore::V1::ListTokenAuthUsersResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-ListTokenAuthUsersResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Memorystore::V1::ListTokenAuthUsersResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-ListTokenAuthUsersResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #logger
    
    
    def logger(stub: false) -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #reschedule_maintenance
    
    
    def reschedule_maintenance(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the reschedule_maintenance REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Memorystore::V1::RescheduleMaintenanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-RescheduleMaintenanceRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #start_migration
    
    
    def start_migration(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the start_migration REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Memorystore::V1::StartMigrationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-StartMigrationRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_instance
    
    
    def update_instance(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the update_instance REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Memorystore::V1::UpdateInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-UpdateInstanceRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
