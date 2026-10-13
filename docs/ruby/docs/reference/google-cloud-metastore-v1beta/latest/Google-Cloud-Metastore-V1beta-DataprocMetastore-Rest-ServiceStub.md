---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-DataprocMetastore-Rest-ServiceStub/
title: Dataproc Metastore V1beta API - Class Google::Cloud::Metastore::V1beta::DataprocMetastore::Rest::ServiceStub (v0.22.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:22:04.262312+00:00
---

# Dataproc Metastore V1beta API - Class Google::Cloud::Metastore::V1beta::DataprocMetastore::Rest::ServiceStub (v0.22.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-DataprocMetastore-Rest-ServiceStub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dataproc Metastore V1beta API - Class Google::Cloud::Metastore::V1beta::DataprocMetastore::Rest::ServiceStub (v0.22.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.22.1 (latest)  0.22.0  0.21.0  0.20.0  0.19.1  0.18.0  0.17.0  0.16.1  0.15.0  0.14.0  0.13.1  0.12.2  0.11.0  0.10.0  0.9.0  0.8.1  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.5 

Reference documentation and code samples for the Dataproc Metastore V1beta API class Google::Cloud::Metastore::V1beta::DataprocMetastore::Rest::ServiceStub.

REST service stub for the DataprocMetastore service. Service stub contains baseline method implementations including transcoding, making the REST call, and deserialing the response.

## Inherits

  * Object 



## Methods 

### #alter_metadata_resource_location
    
    
    def alter_metadata_resource_location(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the alter_metadata_resource_location REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Metastore::V1beta::AlterMetadataResourceLocationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-AlterMetadataResourceLocationRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_backup
    
    
    def create_backup(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the create_backup REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Metastore::V1beta::CreateBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-CreateBackupRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_metadata_import
    
    
    def create_metadata_import(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the create_metadata_import REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Metastore::V1beta::CreateMetadataImportRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-CreateMetadataImportRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_service
    
    
    def create_service(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the create_service REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Metastore::V1beta::CreateServiceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-CreateServiceRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_backup
    
    
    def delete_backup(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the delete_backup REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Metastore::V1beta::DeleteBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-DeleteBackupRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_service
    
    
    def delete_service(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the delete_service REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Metastore::V1beta::DeleteServiceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-DeleteServiceRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #endpoint
    
    
    def endpoint() -> String

The effective endpoint

**Returns**

  * (String) 



### #export_metadata
    
    
    def export_metadata(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the export_metadata REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Metastore::V1beta::ExportMetadataRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-ExportMetadataRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_backup
    
    
    def get_backup(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Metastore::V1beta::Backup

Baseline implementation for the get_backup REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Metastore::V1beta::GetBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-GetBackupRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Metastore::V1beta::Backup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-Backup)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Metastore::V1beta::Backup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-Backup)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_metadata_import
    
    
    def get_metadata_import(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Metastore::V1beta::MetadataImport

Baseline implementation for the get_metadata_import REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Metastore::V1beta::GetMetadataImportRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-GetMetadataImportRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Metastore::V1beta::MetadataImport](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-MetadataImport)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Metastore::V1beta::MetadataImport](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-MetadataImport)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_service
    
    
    def get_service(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Metastore::V1beta::Service

Baseline implementation for the get_service REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Metastore::V1beta::GetServiceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-GetServiceRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Metastore::V1beta::Service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-Service)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Metastore::V1beta::Service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-Service)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_backups
    
    
    def list_backups(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Metastore::V1beta::ListBackupsResponse

Baseline implementation for the list_backups REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Metastore::V1beta::ListBackupsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-ListBackupsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Metastore::V1beta::ListBackupsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-ListBackupsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Metastore::V1beta::ListBackupsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-ListBackupsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_metadata_imports
    
    
    def list_metadata_imports(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Metastore::V1beta::ListMetadataImportsResponse

Baseline implementation for the list_metadata_imports REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Metastore::V1beta::ListMetadataImportsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-ListMetadataImportsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Metastore::V1beta::ListMetadataImportsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-ListMetadataImportsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Metastore::V1beta::ListMetadataImportsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-ListMetadataImportsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_services
    
    
    def list_services(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Metastore::V1beta::ListServicesResponse

Baseline implementation for the list_services REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Metastore::V1beta::ListServicesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-ListServicesRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Metastore::V1beta::ListServicesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-ListServicesResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Metastore::V1beta::ListServicesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-ListServicesResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #logger
    
    
    def logger(stub: false) -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #move_table_to_database
    
    
    def move_table_to_database(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the move_table_to_database REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Metastore::V1beta::MoveTableToDatabaseRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-MoveTableToDatabaseRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #query_metadata
    
    
    def query_metadata(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the query_metadata REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Metastore::V1beta::QueryMetadataRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-QueryMetadataRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #remove_iam_policy
    
    
    def remove_iam_policy(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Metastore::V1beta::RemoveIamPolicyResponse

Baseline implementation for the remove_iam_policy REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Metastore::V1beta::RemoveIamPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-RemoveIamPolicyRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Metastore::V1beta::RemoveIamPolicyResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-RemoveIamPolicyResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Metastore::V1beta::RemoveIamPolicyResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-RemoveIamPolicyResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #restore_service
    
    
    def restore_service(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the restore_service REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Metastore::V1beta::RestoreServiceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-RestoreServiceRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_metadata_import
    
    
    def update_metadata_import(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the update_metadata_import REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Metastore::V1beta::UpdateMetadataImportRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-UpdateMetadataImportRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #update_service
    
    
    def update_service(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the update_service REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Metastore::V1beta::UpdateServiceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-UpdateServiceRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
