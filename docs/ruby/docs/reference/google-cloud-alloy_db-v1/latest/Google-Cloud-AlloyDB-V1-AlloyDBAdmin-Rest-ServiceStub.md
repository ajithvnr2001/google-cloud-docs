---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-AlloyDBAdmin-Rest-ServiceStub/
title: AlloyDB V1 API - Class Google::Cloud::AlloyDB::V1::AlloyDBAdmin::Rest::ServiceStub (v1.10.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:09:37.300940+00:00
---

# AlloyDB V1 API - Class Google::Cloud::AlloyDB::V1::AlloyDBAdmin::Rest::ServiceStub (v1.10.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-AlloyDBAdmin-Rest-ServiceStub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  AlloyDB V1 API - Class Google::Cloud::AlloyDB::V1::AlloyDBAdmin::Rest::ServiceStub (v1.10.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.10.2 (latest)  1.10.1  1.9.0  1.7.0  1.6.2  1.5.0  1.4.0  1.3.1  1.2.0  1.1.0  1.0.1  0.12.0  0.11.0  0.10.0  0.9.2  0.8.2  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the AlloyDB V1 API class Google::Cloud::AlloyDB::V1::AlloyDBAdmin::Rest::ServiceStub.

REST service stub for the AlloyDBAdmin service. Service stub contains baseline method implementations including transcoding, making the REST call, and deserialing the response.

## Inherits

  * Object 



## Methods 

### #batch_create_instances
    
    
    def batch_create_instances(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the batch_create_instances REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::AlloyDB::V1::BatchCreateInstancesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-BatchCreateInstancesRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_backup
    
    
    def create_backup(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the create_backup REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::AlloyDB::V1::CreateBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-CreateBackupRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_cluster
    
    
    def create_cluster(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the create_cluster REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::AlloyDB::V1::CreateClusterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-CreateClusterRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_instance
    
    
    def create_instance(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the create_instance REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::AlloyDB::V1::CreateInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-CreateInstanceRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_secondary_cluster
    
    
    def create_secondary_cluster(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the create_secondary_cluster REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::AlloyDB::V1::CreateSecondaryClusterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-CreateSecondaryClusterRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_secondary_instance
    
    
    def create_secondary_instance(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the create_secondary_instance REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::AlloyDB::V1::CreateSecondaryInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-CreateSecondaryInstanceRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_user
    
    
    def create_user(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::AlloyDB::V1::User

Baseline implementation for the create_user REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::AlloyDB::V1::CreateUserRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-CreateUserRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AlloyDB::V1::User](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-User)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AlloyDB::V1::User](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-User)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_backup
    
    
    def delete_backup(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the delete_backup REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::AlloyDB::V1::DeleteBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-DeleteBackupRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_cluster
    
    
    def delete_cluster(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the delete_cluster REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::AlloyDB::V1::DeleteClusterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-DeleteClusterRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_instance
    
    
    def delete_instance(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the delete_instance REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::AlloyDB::V1::DeleteInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-DeleteInstanceRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_user
    
    
    def delete_user(request_pb, options = nil) { |result, operation| ... } -> ::Google::Protobuf::Empty

Baseline implementation for the delete_user REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::AlloyDB::V1::DeleteUserRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-DeleteUserRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Protobuf-Empty)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #endpoint
    
    
    def endpoint() -> String

The effective endpoint

**Returns**

  * (String) 



### #execute_sql
    
    
    def execute_sql(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::AlloyDB::V1::ExecuteSqlResponse

Baseline implementation for the execute_sql REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::AlloyDB::V1::ExecuteSqlRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-ExecuteSqlRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AlloyDB::V1::ExecuteSqlResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-ExecuteSqlResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AlloyDB::V1::ExecuteSqlResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-ExecuteSqlResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #export_cluster
    
    
    def export_cluster(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the export_cluster REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::AlloyDB::V1::ExportClusterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-ExportClusterRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #failover_instance
    
    
    def failover_instance(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the failover_instance REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::AlloyDB::V1::FailoverInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-FailoverInstanceRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #generate_client_certificate
    
    
    def generate_client_certificate(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::AlloyDB::V1::GenerateClientCertificateResponse

Baseline implementation for the generate_client_certificate REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::AlloyDB::V1::GenerateClientCertificateRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-GenerateClientCertificateRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AlloyDB::V1::GenerateClientCertificateResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-GenerateClientCertificateResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AlloyDB::V1::GenerateClientCertificateResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-GenerateClientCertificateResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_backup
    
    
    def get_backup(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::AlloyDB::V1::Backup

Baseline implementation for the get_backup REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::AlloyDB::V1::GetBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-GetBackupRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AlloyDB::V1::Backup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-Backup)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AlloyDB::V1::Backup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-Backup)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_cluster
    
    
    def get_cluster(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::AlloyDB::V1::Cluster

Baseline implementation for the get_cluster REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::AlloyDB::V1::GetClusterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-GetClusterRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AlloyDB::V1::Cluster](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-Cluster)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AlloyDB::V1::Cluster](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-Cluster)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_connection_info
    
    
    def get_connection_info(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::AlloyDB::V1::ConnectionInfo

Baseline implementation for the get_connection_info REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::AlloyDB::V1::GetConnectionInfoRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-GetConnectionInfoRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AlloyDB::V1::ConnectionInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-ConnectionInfo)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AlloyDB::V1::ConnectionInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-ConnectionInfo)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_instance
    
    
    def get_instance(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::AlloyDB::V1::Instance

Baseline implementation for the get_instance REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::AlloyDB::V1::GetInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-GetInstanceRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AlloyDB::V1::Instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-Instance)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AlloyDB::V1::Instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-Instance)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_user
    
    
    def get_user(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::AlloyDB::V1::User

Baseline implementation for the get_user REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::AlloyDB::V1::GetUserRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-GetUserRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AlloyDB::V1::User](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-User)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AlloyDB::V1::User](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-User)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #import_cluster
    
    
    def import_cluster(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the import_cluster REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::AlloyDB::V1::ImportClusterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-ImportClusterRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #inject_fault
    
    
    def inject_fault(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the inject_fault REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::AlloyDB::V1::InjectFaultRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-InjectFaultRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_backups
    
    
    def list_backups(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::AlloyDB::V1::ListBackupsResponse

Baseline implementation for the list_backups REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::AlloyDB::V1::ListBackupsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-ListBackupsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AlloyDB::V1::ListBackupsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-ListBackupsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AlloyDB::V1::ListBackupsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-ListBackupsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_clusters
    
    
    def list_clusters(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::AlloyDB::V1::ListClustersResponse

Baseline implementation for the list_clusters REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::AlloyDB::V1::ListClustersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-ListClustersRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AlloyDB::V1::ListClustersResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-ListClustersResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AlloyDB::V1::ListClustersResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-ListClustersResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_databases
    
    
    def list_databases(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::AlloyDB::V1::ListDatabasesResponse

Baseline implementation for the list_databases REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::AlloyDB::V1::ListDatabasesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-ListDatabasesRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AlloyDB::V1::ListDatabasesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-ListDatabasesResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AlloyDB::V1::ListDatabasesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-ListDatabasesResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_instances
    
    
    def list_instances(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::AlloyDB::V1::ListInstancesResponse

Baseline implementation for the list_instances REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::AlloyDB::V1::ListInstancesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-ListInstancesRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AlloyDB::V1::ListInstancesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-ListInstancesResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AlloyDB::V1::ListInstancesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-ListInstancesResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_supported_database_flags
    
    
    def list_supported_database_flags(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::AlloyDB::V1::ListSupportedDatabaseFlagsResponse

Baseline implementation for the list_supported_database_flags REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::AlloyDB::V1::ListSupportedDatabaseFlagsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-ListSupportedDatabaseFlagsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AlloyDB::V1::ListSupportedDatabaseFlagsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-ListSupportedDatabaseFlagsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AlloyDB::V1::ListSupportedDatabaseFlagsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-ListSupportedDatabaseFlagsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_users
    
    
    def list_users(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::AlloyDB::V1::ListUsersResponse

Baseline implementation for the list_users REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::AlloyDB::V1::ListUsersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-ListUsersRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AlloyDB::V1::ListUsersResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-ListUsersResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AlloyDB::V1::ListUsersResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-ListUsersResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #logger
    
    
    def logger(stub: false) -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #promote_cluster
    
    
    def promote_cluster(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the promote_cluster REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::AlloyDB::V1::PromoteClusterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-PromoteClusterRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #restart_instance
    
    
    def restart_instance(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the restart_instance REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::AlloyDB::V1::RestartInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-RestartInstanceRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #restore_cluster
    
    
    def restore_cluster(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the restore_cluster REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::AlloyDB::V1::RestoreClusterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-RestoreClusterRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #switchover_cluster
    
    
    def switchover_cluster(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the switchover_cluster REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::AlloyDB::V1::SwitchoverClusterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-SwitchoverClusterRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



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

  * **request_pb** ([::Google::Cloud::AlloyDB::V1::UpdateBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-UpdateBackupRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #update_cluster
    
    
    def update_cluster(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the update_cluster REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::AlloyDB::V1::UpdateClusterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-UpdateClusterRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #update_instance
    
    
    def update_instance(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the update_instance REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::AlloyDB::V1::UpdateInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-UpdateInstanceRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #update_user
    
    
    def update_user(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::AlloyDB::V1::User

Baseline implementation for the update_user REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::AlloyDB::V1::UpdateUserRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-UpdateUserRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AlloyDB::V1::User](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-User)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AlloyDB::V1::User](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-User)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #upgrade_cluster
    
    
    def upgrade_cluster(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the upgrade_cluster REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::AlloyDB::V1::UpgradeClusterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-UpgradeClusterRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
