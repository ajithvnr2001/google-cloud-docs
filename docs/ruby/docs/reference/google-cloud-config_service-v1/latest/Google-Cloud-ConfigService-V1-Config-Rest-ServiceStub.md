---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Config-Rest-ServiceStub/
title: Infrastructure Manager V1 API - Class Google::Cloud::ConfigService::V1::Config::Rest::ServiceStub (v2.12.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:47:49.683845+00:00
---

# Infrastructure Manager V1 API - Class Google::Cloud::ConfigService::V1::Config::Rest::ServiceStub (v2.12.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Config-Rest-ServiceStub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Infrastructure Manager V1 API - Class Google::Cloud::ConfigService::V1::Config::Rest::ServiceStub (v2.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.12.0 (latest)  2.11.0  2.10.1  2.9.0  2.8.0  2.7.0  2.6.0  2.5.1  2.4.0  2.3.0  2.2.0  2.1.0  2.0.1  1.3.0  1.2.1  1.1.0  1.0.2  0.6.0  0.5.0  0.4.0  0.3.1  0.2.1  0.1.0 

Reference documentation and code samples for the Infrastructure Manager V1 API class Google::Cloud::ConfigService::V1::Config::Rest::ServiceStub.

REST service stub for the Config service. Service stub contains baseline method implementations including transcoding, making the REST call, and deserialing the response.

## Inherits

  * Object 



## Methods 

### #create_deployment
    
    
    def create_deployment(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the create_deployment REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ConfigService::V1::CreateDeploymentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-CreateDeploymentRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_deployment_group
    
    
    def create_deployment_group(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the create_deployment_group REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ConfigService::V1::CreateDeploymentGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-CreateDeploymentGroupRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_preview
    
    
    def create_preview(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the create_preview REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ConfigService::V1::CreatePreviewRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-CreatePreviewRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_deployment
    
    
    def delete_deployment(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the delete_deployment REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ConfigService::V1::DeleteDeploymentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-DeleteDeploymentRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_deployment_group
    
    
    def delete_deployment_group(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the delete_deployment_group REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ConfigService::V1::DeleteDeploymentGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-DeleteDeploymentGroupRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_preview
    
    
    def delete_preview(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the delete_preview REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ConfigService::V1::DeletePreviewRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-DeletePreviewRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_statefile
    
    
    def delete_statefile(request_pb, options = nil) { |result, operation| ... } -> ::Google::Protobuf::Empty

Baseline implementation for the delete_statefile REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ConfigService::V1::DeleteStatefileRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-DeleteStatefileRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Protobuf-Empty)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #deprovision_deployment_group
    
    
    def deprovision_deployment_group(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the deprovision_deployment_group REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ConfigService::V1::DeprovisionDeploymentGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-DeprovisionDeploymentGroupRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #endpoint
    
    
    def endpoint() -> String

The effective endpoint

**Returns**

  * (String) 



### #export_deployment_statefile
    
    
    def export_deployment_statefile(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::ConfigService::V1::Statefile

Baseline implementation for the export_deployment_statefile REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ConfigService::V1::ExportDeploymentStatefileRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ExportDeploymentStatefileRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::ConfigService::V1::Statefile](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Statefile)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::ConfigService::V1::Statefile](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Statefile)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #export_lock_info
    
    
    def export_lock_info(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::ConfigService::V1::LockInfo

Baseline implementation for the export_lock_info REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ConfigService::V1::ExportLockInfoRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ExportLockInfoRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::ConfigService::V1::LockInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-LockInfo)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::ConfigService::V1::LockInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-LockInfo)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #export_preview_result
    
    
    def export_preview_result(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::ConfigService::V1::ExportPreviewResultResponse

Baseline implementation for the export_preview_result REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ConfigService::V1::ExportPreviewResultRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ExportPreviewResultRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::ConfigService::V1::ExportPreviewResultResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ExportPreviewResultResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::ConfigService::V1::ExportPreviewResultResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ExportPreviewResultResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #export_revision_statefile
    
    
    def export_revision_statefile(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::ConfigService::V1::Statefile

Baseline implementation for the export_revision_statefile REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ConfigService::V1::ExportRevisionStatefileRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ExportRevisionStatefileRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::ConfigService::V1::Statefile](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Statefile)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::ConfigService::V1::Statefile](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Statefile)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_auto_migration_config
    
    
    def get_auto_migration_config(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::ConfigService::V1::AutoMigrationConfig

Baseline implementation for the get_auto_migration_config REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ConfigService::V1::GetAutoMigrationConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-GetAutoMigrationConfigRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::ConfigService::V1::AutoMigrationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-AutoMigrationConfig)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::ConfigService::V1::AutoMigrationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-AutoMigrationConfig)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_deployment
    
    
    def get_deployment(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::ConfigService::V1::Deployment

Baseline implementation for the get_deployment REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ConfigService::V1::GetDeploymentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-GetDeploymentRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::ConfigService::V1::Deployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Deployment)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::ConfigService::V1::Deployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Deployment)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_deployment_group
    
    
    def get_deployment_group(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::ConfigService::V1::DeploymentGroup

Baseline implementation for the get_deployment_group REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ConfigService::V1::GetDeploymentGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-GetDeploymentGroupRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::ConfigService::V1::DeploymentGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-DeploymentGroup)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::ConfigService::V1::DeploymentGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-DeploymentGroup)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_deployment_group_revision
    
    
    def get_deployment_group_revision(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::ConfigService::V1::DeploymentGroupRevision

Baseline implementation for the get_deployment_group_revision REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ConfigService::V1::GetDeploymentGroupRevisionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-GetDeploymentGroupRevisionRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::ConfigService::V1::DeploymentGroupRevision](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-DeploymentGroupRevision)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::ConfigService::V1::DeploymentGroupRevision](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-DeploymentGroupRevision)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_preview
    
    
    def get_preview(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::ConfigService::V1::Preview

Baseline implementation for the get_preview REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ConfigService::V1::GetPreviewRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-GetPreviewRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::ConfigService::V1::Preview](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Preview)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::ConfigService::V1::Preview](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Preview)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_resource
    
    
    def get_resource(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::ConfigService::V1::Resource

Baseline implementation for the get_resource REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ConfigService::V1::GetResourceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-GetResourceRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::ConfigService::V1::Resource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Resource)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::ConfigService::V1::Resource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Resource)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_resource_change
    
    
    def get_resource_change(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::ConfigService::V1::ResourceChange

Baseline implementation for the get_resource_change REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ConfigService::V1::GetResourceChangeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-GetResourceChangeRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::ConfigService::V1::ResourceChange](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ResourceChange)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::ConfigService::V1::ResourceChange](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ResourceChange)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_resource_drift
    
    
    def get_resource_drift(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::ConfigService::V1::ResourceDrift

Baseline implementation for the get_resource_drift REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ConfigService::V1::GetResourceDriftRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-GetResourceDriftRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::ConfigService::V1::ResourceDrift](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ResourceDrift)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::ConfigService::V1::ResourceDrift](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ResourceDrift)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_revision
    
    
    def get_revision(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::ConfigService::V1::Revision

Baseline implementation for the get_revision REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ConfigService::V1::GetRevisionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-GetRevisionRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::ConfigService::V1::Revision](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Revision)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::ConfigService::V1::Revision](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Revision)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_terraform_version
    
    
    def get_terraform_version(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::ConfigService::V1::TerraformVersion

Baseline implementation for the get_terraform_version REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ConfigService::V1::GetTerraformVersionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-GetTerraformVersionRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::ConfigService::V1::TerraformVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-TerraformVersion)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::ConfigService::V1::TerraformVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-TerraformVersion)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #import_statefile
    
    
    def import_statefile(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::ConfigService::V1::Statefile

Baseline implementation for the import_statefile REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ConfigService::V1::ImportStatefileRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ImportStatefileRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::ConfigService::V1::Statefile](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Statefile)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::ConfigService::V1::Statefile](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Statefile)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_deployment_group_revisions
    
    
    def list_deployment_group_revisions(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::ConfigService::V1::ListDeploymentGroupRevisionsResponse

Baseline implementation for the list_deployment_group_revisions REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ConfigService::V1::ListDeploymentGroupRevisionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ListDeploymentGroupRevisionsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::ConfigService::V1::ListDeploymentGroupRevisionsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ListDeploymentGroupRevisionsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::ConfigService::V1::ListDeploymentGroupRevisionsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ListDeploymentGroupRevisionsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_deployment_groups
    
    
    def list_deployment_groups(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::ConfigService::V1::ListDeploymentGroupsResponse

Baseline implementation for the list_deployment_groups REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ConfigService::V1::ListDeploymentGroupsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ListDeploymentGroupsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::ConfigService::V1::ListDeploymentGroupsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ListDeploymentGroupsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::ConfigService::V1::ListDeploymentGroupsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ListDeploymentGroupsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_deployments
    
    
    def list_deployments(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::ConfigService::V1::ListDeploymentsResponse

Baseline implementation for the list_deployments REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ConfigService::V1::ListDeploymentsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ListDeploymentsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::ConfigService::V1::ListDeploymentsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ListDeploymentsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::ConfigService::V1::ListDeploymentsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ListDeploymentsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_previews
    
    
    def list_previews(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::ConfigService::V1::ListPreviewsResponse

Baseline implementation for the list_previews REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ConfigService::V1::ListPreviewsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ListPreviewsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::ConfigService::V1::ListPreviewsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ListPreviewsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::ConfigService::V1::ListPreviewsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ListPreviewsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_resource_changes
    
    
    def list_resource_changes(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::ConfigService::V1::ListResourceChangesResponse

Baseline implementation for the list_resource_changes REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ConfigService::V1::ListResourceChangesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ListResourceChangesRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::ConfigService::V1::ListResourceChangesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ListResourceChangesResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::ConfigService::V1::ListResourceChangesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ListResourceChangesResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_resource_drifts
    
    
    def list_resource_drifts(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::ConfigService::V1::ListResourceDriftsResponse

Baseline implementation for the list_resource_drifts REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ConfigService::V1::ListResourceDriftsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ListResourceDriftsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::ConfigService::V1::ListResourceDriftsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ListResourceDriftsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::ConfigService::V1::ListResourceDriftsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ListResourceDriftsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_resources
    
    
    def list_resources(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::ConfigService::V1::ListResourcesResponse

Baseline implementation for the list_resources REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ConfigService::V1::ListResourcesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ListResourcesRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::ConfigService::V1::ListResourcesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ListResourcesResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::ConfigService::V1::ListResourcesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ListResourcesResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_revisions
    
    
    def list_revisions(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::ConfigService::V1::ListRevisionsResponse

Baseline implementation for the list_revisions REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ConfigService::V1::ListRevisionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ListRevisionsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::ConfigService::V1::ListRevisionsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ListRevisionsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::ConfigService::V1::ListRevisionsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ListRevisionsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_terraform_versions
    
    
    def list_terraform_versions(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::ConfigService::V1::ListTerraformVersionsResponse

Baseline implementation for the list_terraform_versions REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ConfigService::V1::ListTerraformVersionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ListTerraformVersionsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::ConfigService::V1::ListTerraformVersionsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ListTerraformVersionsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::ConfigService::V1::ListTerraformVersionsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ListTerraformVersionsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #lock_deployment
    
    
    def lock_deployment(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the lock_deployment REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ConfigService::V1::LockDeploymentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-LockDeploymentRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #logger
    
    
    def logger(stub: false) -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #provision_deployment_group
    
    
    def provision_deployment_group(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the provision_deployment_group REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ConfigService::V1::ProvisionDeploymentGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ProvisionDeploymentGroupRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #unlock_deployment
    
    
    def unlock_deployment(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the unlock_deployment REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ConfigService::V1::UnlockDeploymentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-UnlockDeploymentRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #update_auto_migration_config
    
    
    def update_auto_migration_config(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the update_auto_migration_config REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ConfigService::V1::UpdateAutoMigrationConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-UpdateAutoMigrationConfigRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #update_deployment
    
    
    def update_deployment(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the update_deployment REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ConfigService::V1::UpdateDeploymentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-UpdateDeploymentRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #update_deployment_group
    
    
    def update_deployment_group(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the update_deployment_group REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ConfigService::V1::UpdateDeploymentGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-UpdateDeploymentGroupRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
