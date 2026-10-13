---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-SecurityCenter-Rest-ServiceStub/
title: Security Command Center V2 API - Class Google::Cloud::SecurityCenter::V2::SecurityCenter::Rest::ServiceStub (v1.9.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:26:23.702937+00:00
---

# Security Command Center V2 API - Class Google::Cloud::SecurityCenter::V2::SecurityCenter::Rest::ServiceStub (v1.9.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-SecurityCenter-Rest-ServiceStub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Security Command Center V2 API - Class Google::Cloud::SecurityCenter::V2::SecurityCenter::Rest::ServiceStub (v1.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.9.1 (latest)  1.9.0  1.8.0  1.7.1  1.6.0  1.5.1  1.4.0  1.3.0  1.2.0  1.1.1  1.0.0  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Security Command Center V2 API class Google::Cloud::SecurityCenter::V2::SecurityCenter::Rest::ServiceStub.

REST service stub for the SecurityCenter service. Service stub contains baseline method implementations including transcoding, making the REST call, and deserialing the response.

## Inherits

  * [Object](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-Kubernetes-Object)



## Methods 

### #batch_create_resource_value_configs
    
    
    def batch_create_resource_value_configs(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::SecurityCenter::V2::BatchCreateResourceValueConfigsResponse

Baseline implementation for the batch_create_resource_value_configs REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::SecurityCenter::V2::BatchCreateResourceValueConfigsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-BatchCreateResourceValueConfigsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecurityCenter::V2::BatchCreateResourceValueConfigsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-BatchCreateResourceValueConfigsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecurityCenter::V2::BatchCreateResourceValueConfigsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-BatchCreateResourceValueConfigsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #bulk_mute_findings
    
    
    def bulk_mute_findings(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the bulk_mute_findings REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::SecurityCenter::V2::BulkMuteFindingsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-BulkMuteFindingsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_big_query_export
    
    
    def create_big_query_export(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::SecurityCenter::V2::BigQueryExport

Baseline implementation for the create_big_query_export REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::SecurityCenter::V2::CreateBigQueryExportRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-CreateBigQueryExportRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecurityCenter::V2::BigQueryExport](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-BigQueryExport)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecurityCenter::V2::BigQueryExport](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-BigQueryExport)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_finding
    
    
    def create_finding(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::SecurityCenter::V2::Finding

Baseline implementation for the create_finding REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::SecurityCenter::V2::CreateFindingRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-CreateFindingRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecurityCenter::V2::Finding](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-Finding)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecurityCenter::V2::Finding](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-Finding)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_mute_config
    
    
    def create_mute_config(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::SecurityCenter::V2::MuteConfig

Baseline implementation for the create_mute_config REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::SecurityCenter::V2::CreateMuteConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-CreateMuteConfigRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecurityCenter::V2::MuteConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-MuteConfig)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecurityCenter::V2::MuteConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-MuteConfig)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_notification_config
    
    
    def create_notification_config(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::SecurityCenter::V2::NotificationConfig

Baseline implementation for the create_notification_config REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::SecurityCenter::V2::CreateNotificationConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-CreateNotificationConfigRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecurityCenter::V2::NotificationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-NotificationConfig)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecurityCenter::V2::NotificationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-NotificationConfig)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_source
    
    
    def create_source(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::SecurityCenter::V2::Source

Baseline implementation for the create_source REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::SecurityCenter::V2::CreateSourceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-CreateSourceRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecurityCenter::V2::Source](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-Source)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecurityCenter::V2::Source](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-Source)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_big_query_export
    
    
    def delete_big_query_export(request_pb, options = nil) { |result, operation| ... } -> ::Google::Protobuf::Empty

Baseline implementation for the delete_big_query_export REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::SecurityCenter::V2::DeleteBigQueryExportRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-DeleteBigQueryExportRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Protobuf-Empty)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_mute_config
    
    
    def delete_mute_config(request_pb, options = nil) { |result, operation| ... } -> ::Google::Protobuf::Empty

Baseline implementation for the delete_mute_config REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::SecurityCenter::V2::DeleteMuteConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-DeleteMuteConfigRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Protobuf-Empty)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_notification_config
    
    
    def delete_notification_config(request_pb, options = nil) { |result, operation| ... } -> ::Google::Protobuf::Empty

Baseline implementation for the delete_notification_config REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::SecurityCenter::V2::DeleteNotificationConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-DeleteNotificationConfigRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Protobuf-Empty)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_resource_value_config
    
    
    def delete_resource_value_config(request_pb, options = nil) { |result, operation| ... } -> ::Google::Protobuf::Empty

Baseline implementation for the delete_resource_value_config REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::SecurityCenter::V2::DeleteResourceValueConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-DeleteResourceValueConfigRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Protobuf-Empty)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #endpoint
    
    
    def endpoint() -> String

The effective endpoint

**Returns**

  * (String) 



### #get_big_query_export
    
    
    def get_big_query_export(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::SecurityCenter::V2::BigQueryExport

Baseline implementation for the get_big_query_export REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::SecurityCenter::V2::GetBigQueryExportRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-GetBigQueryExportRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecurityCenter::V2::BigQueryExport](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-BigQueryExport)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecurityCenter::V2::BigQueryExport](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-BigQueryExport)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_iam_policy
    
    
    def get_iam_policy(request_pb, options = nil) { |result, operation| ... } -> ::Google::Iam::V1::Policy

Baseline implementation for the get_iam_policy REST call

**Parameters**

  * **request_pb** ([::Google::Iam::V1::GetIamPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Iam-V1-GetIamPolicyRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Iam::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Iam-V1-Policy)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Iam::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Iam-V1-Policy)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_mute_config
    
    
    def get_mute_config(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::SecurityCenter::V2::MuteConfig

Baseline implementation for the get_mute_config REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::SecurityCenter::V2::GetMuteConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-GetMuteConfigRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecurityCenter::V2::MuteConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-MuteConfig)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecurityCenter::V2::MuteConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-MuteConfig)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_notification_config
    
    
    def get_notification_config(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::SecurityCenter::V2::NotificationConfig

Baseline implementation for the get_notification_config REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::SecurityCenter::V2::GetNotificationConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-GetNotificationConfigRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecurityCenter::V2::NotificationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-NotificationConfig)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecurityCenter::V2::NotificationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-NotificationConfig)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_resource_value_config
    
    
    def get_resource_value_config(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::SecurityCenter::V2::ResourceValueConfig

Baseline implementation for the get_resource_value_config REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::SecurityCenter::V2::GetResourceValueConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-GetResourceValueConfigRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecurityCenter::V2::ResourceValueConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-ResourceValueConfig)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecurityCenter::V2::ResourceValueConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-ResourceValueConfig)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_simulation
    
    
    def get_simulation(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::SecurityCenter::V2::Simulation

Baseline implementation for the get_simulation REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::SecurityCenter::V2::GetSimulationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-GetSimulationRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecurityCenter::V2::Simulation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-Simulation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecurityCenter::V2::Simulation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-Simulation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_source
    
    
    def get_source(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::SecurityCenter::V2::Source

Baseline implementation for the get_source REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::SecurityCenter::V2::GetSourceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-GetSourceRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecurityCenter::V2::Source](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-Source)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecurityCenter::V2::Source](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-Source)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_valued_resource
    
    
    def get_valued_resource(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::SecurityCenter::V2::ValuedResource

Baseline implementation for the get_valued_resource REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::SecurityCenter::V2::GetValuedResourceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-GetValuedResourceRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecurityCenter::V2::ValuedResource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-ValuedResource)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecurityCenter::V2::ValuedResource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-ValuedResource)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #group_findings
    
    
    def group_findings(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::SecurityCenter::V2::GroupFindingsResponse

Baseline implementation for the group_findings REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::SecurityCenter::V2::GroupFindingsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-GroupFindingsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecurityCenter::V2::GroupFindingsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-GroupFindingsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecurityCenter::V2::GroupFindingsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-GroupFindingsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_attack_paths
    
    
    def list_attack_paths(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::SecurityCenter::V2::ListAttackPathsResponse

Baseline implementation for the list_attack_paths REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::SecurityCenter::V2::ListAttackPathsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-ListAttackPathsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecurityCenter::V2::ListAttackPathsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-ListAttackPathsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecurityCenter::V2::ListAttackPathsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-ListAttackPathsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_big_query_exports
    
    
    def list_big_query_exports(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::SecurityCenter::V2::ListBigQueryExportsResponse

Baseline implementation for the list_big_query_exports REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::SecurityCenter::V2::ListBigQueryExportsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-ListBigQueryExportsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecurityCenter::V2::ListBigQueryExportsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-ListBigQueryExportsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecurityCenter::V2::ListBigQueryExportsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-ListBigQueryExportsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_findings
    
    
    def list_findings(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::SecurityCenter::V2::ListFindingsResponse

Baseline implementation for the list_findings REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::SecurityCenter::V2::ListFindingsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-ListFindingsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecurityCenter::V2::ListFindingsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-ListFindingsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecurityCenter::V2::ListFindingsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-ListFindingsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_mute_configs
    
    
    def list_mute_configs(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::SecurityCenter::V2::ListMuteConfigsResponse

Baseline implementation for the list_mute_configs REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::SecurityCenter::V2::ListMuteConfigsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-ListMuteConfigsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecurityCenter::V2::ListMuteConfigsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-ListMuteConfigsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecurityCenter::V2::ListMuteConfigsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-ListMuteConfigsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_notification_configs
    
    
    def list_notification_configs(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::SecurityCenter::V2::ListNotificationConfigsResponse

Baseline implementation for the list_notification_configs REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::SecurityCenter::V2::ListNotificationConfigsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-ListNotificationConfigsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecurityCenter::V2::ListNotificationConfigsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-ListNotificationConfigsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecurityCenter::V2::ListNotificationConfigsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-ListNotificationConfigsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_resource_value_configs
    
    
    def list_resource_value_configs(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::SecurityCenter::V2::ListResourceValueConfigsResponse

Baseline implementation for the list_resource_value_configs REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::SecurityCenter::V2::ListResourceValueConfigsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-ListResourceValueConfigsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecurityCenter::V2::ListResourceValueConfigsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-ListResourceValueConfigsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecurityCenter::V2::ListResourceValueConfigsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-ListResourceValueConfigsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_sources
    
    
    def list_sources(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::SecurityCenter::V2::ListSourcesResponse

Baseline implementation for the list_sources REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::SecurityCenter::V2::ListSourcesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-ListSourcesRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecurityCenter::V2::ListSourcesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-ListSourcesResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecurityCenter::V2::ListSourcesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-ListSourcesResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_valued_resources
    
    
    def list_valued_resources(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::SecurityCenter::V2::ListValuedResourcesResponse

Baseline implementation for the list_valued_resources REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::SecurityCenter::V2::ListValuedResourcesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-ListValuedResourcesRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecurityCenter::V2::ListValuedResourcesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-ListValuedResourcesResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecurityCenter::V2::ListValuedResourcesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-ListValuedResourcesResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #logger
    
    
    def logger(stub: false) -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #set_finding_state
    
    
    def set_finding_state(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::SecurityCenter::V2::Finding

Baseline implementation for the set_finding_state REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::SecurityCenter::V2::SetFindingStateRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-SetFindingStateRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecurityCenter::V2::Finding](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-Finding)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecurityCenter::V2::Finding](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-Finding)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #set_iam_policy
    
    
    def set_iam_policy(request_pb, options = nil) { |result, operation| ... } -> ::Google::Iam::V1::Policy

Baseline implementation for the set_iam_policy REST call

**Parameters**

  * **request_pb** ([::Google::Iam::V1::SetIamPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Iam-V1-SetIamPolicyRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Iam::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Iam-V1-Policy)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Iam::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Iam-V1-Policy)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #set_mute
    
    
    def set_mute(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::SecurityCenter::V2::Finding

Baseline implementation for the set_mute REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::SecurityCenter::V2::SetMuteRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-SetMuteRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecurityCenter::V2::Finding](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-Finding)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecurityCenter::V2::Finding](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-Finding)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #test_iam_permissions
    
    
    def test_iam_permissions(request_pb, options = nil) { |result, operation| ... } -> ::Google::Iam::V1::TestIamPermissionsResponse

Baseline implementation for the test_iam_permissions REST call

**Parameters**

  * **request_pb** ([::Google::Iam::V1::TestIamPermissionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Iam-V1-TestIamPermissionsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Iam::V1::TestIamPermissionsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Iam-V1-TestIamPermissionsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Iam::V1::TestIamPermissionsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Iam-V1-TestIamPermissionsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_big_query_export
    
    
    def update_big_query_export(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::SecurityCenter::V2::BigQueryExport

Baseline implementation for the update_big_query_export REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::SecurityCenter::V2::UpdateBigQueryExportRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-UpdateBigQueryExportRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecurityCenter::V2::BigQueryExport](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-BigQueryExport)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecurityCenter::V2::BigQueryExport](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-BigQueryExport)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #update_external_system
    
    
    def update_external_system(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::SecurityCenter::V2::ExternalSystem

Baseline implementation for the update_external_system REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::SecurityCenter::V2::UpdateExternalSystemRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-UpdateExternalSystemRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecurityCenter::V2::ExternalSystem](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-ExternalSystem)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecurityCenter::V2::ExternalSystem](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-ExternalSystem)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #update_finding
    
    
    def update_finding(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::SecurityCenter::V2::Finding

Baseline implementation for the update_finding REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::SecurityCenter::V2::UpdateFindingRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-UpdateFindingRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecurityCenter::V2::Finding](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-Finding)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecurityCenter::V2::Finding](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-Finding)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #update_mute_config
    
    
    def update_mute_config(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::SecurityCenter::V2::MuteConfig

Baseline implementation for the update_mute_config REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::SecurityCenter::V2::UpdateMuteConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-UpdateMuteConfigRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecurityCenter::V2::MuteConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-MuteConfig)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecurityCenter::V2::MuteConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-MuteConfig)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #update_notification_config
    
    
    def update_notification_config(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::SecurityCenter::V2::NotificationConfig

Baseline implementation for the update_notification_config REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::SecurityCenter::V2::UpdateNotificationConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-UpdateNotificationConfigRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecurityCenter::V2::NotificationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-NotificationConfig)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecurityCenter::V2::NotificationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-NotificationConfig)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #update_resource_value_config
    
    
    def update_resource_value_config(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::SecurityCenter::V2::ResourceValueConfig

Baseline implementation for the update_resource_value_config REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::SecurityCenter::V2::UpdateResourceValueConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-UpdateResourceValueConfigRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecurityCenter::V2::ResourceValueConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-ResourceValueConfig)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecurityCenter::V2::ResourceValueConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-ResourceValueConfig)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #update_security_marks
    
    
    def update_security_marks(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::SecurityCenter::V2::SecurityMarks

Baseline implementation for the update_security_marks REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::SecurityCenter::V2::UpdateSecurityMarksRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-UpdateSecurityMarksRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecurityCenter::V2::SecurityMarks](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-SecurityMarks)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecurityCenter::V2::SecurityMarks](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-SecurityMarks)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #update_source
    
    
    def update_source(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::SecurityCenter::V2::Source

Baseline implementation for the update_source REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::SecurityCenter::V2::UpdateSourceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-UpdateSourceRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecurityCenter::V2::Source](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-Source)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecurityCenter::V2::Source](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-Source)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
