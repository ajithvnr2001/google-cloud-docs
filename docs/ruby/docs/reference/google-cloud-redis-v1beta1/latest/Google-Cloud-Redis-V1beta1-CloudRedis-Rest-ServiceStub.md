---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1beta1/latest/Google-Cloud-Redis-V1beta1-CloudRedis-Rest-ServiceStub/
title: Google Cloud Memorystore for Redis V1beta1 API - Class Google::Cloud::Redis::V1beta1::CloudRedis::Rest::ServiceStub (v0.22.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:48:54.282286+00:00
---

# Google Cloud Memorystore for Redis V1beta1 API - Class Google::Cloud::Redis::V1beta1::CloudRedis::Rest::ServiceStub (v0.22.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1beta1/latest/Google-Cloud-Redis-V1beta1-CloudRedis-Rest-ServiceStub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Memorystore for Redis V1beta1 API - Class Google::Cloud::Redis::V1beta1::CloudRedis::Rest::ServiceStub (v0.22.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.22.0 (latest)  0.21.1  0.20.0  0.19.1  0.18.0  0.17.0  0.16.1  0.15.0  0.14.0  0.13.2  0.12.2  0.11.0  0.10.1  0.9.0  0.8.0  0.7.0  0.6.0  0.5.1 

Reference documentation and code samples for the Google Cloud Memorystore for Redis V1beta1 API class Google::Cloud::Redis::V1beta1::CloudRedis::Rest::ServiceStub.

REST service stub for the CloudRedis service. Service stub contains baseline method implementations including transcoding, making the REST call, and deserialing the response.

## Inherits

  * Object 



## Methods 

### #create_instance
    
    
    def create_instance(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the create_instance REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Redis::V1beta1::CreateInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1beta1/latest/Google-Cloud-Redis-V1beta1-CreateInstanceRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1beta1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1beta1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_instance
    
    
    def delete_instance(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the delete_instance REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Redis::V1beta1::DeleteInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1beta1/latest/Google-Cloud-Redis-V1beta1-DeleteInstanceRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1beta1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1beta1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #endpoint
    
    
    def endpoint() -> String

The effective endpoint

**Returns**

  * (String) 



### #export_instance
    
    
    def export_instance(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the export_instance REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Redis::V1beta1::ExportInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1beta1/latest/Google-Cloud-Redis-V1beta1-ExportInstanceRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1beta1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1beta1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #failover_instance
    
    
    def failover_instance(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the failover_instance REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Redis::V1beta1::FailoverInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1beta1/latest/Google-Cloud-Redis-V1beta1-FailoverInstanceRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1beta1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1beta1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_instance
    
    
    def get_instance(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Redis::V1beta1::Instance

Baseline implementation for the get_instance REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Redis::V1beta1::GetInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1beta1/latest/Google-Cloud-Redis-V1beta1-GetInstanceRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Redis::V1beta1::Instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1beta1/latest/Google-Cloud-Redis-V1beta1-Instance)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Redis::V1beta1::Instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1beta1/latest/Google-Cloud-Redis-V1beta1-Instance)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_instance_auth_string
    
    
    def get_instance_auth_string(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Redis::V1beta1::InstanceAuthString

Baseline implementation for the get_instance_auth_string REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Redis::V1beta1::GetInstanceAuthStringRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1beta1/latest/Google-Cloud-Redis-V1beta1-GetInstanceAuthStringRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Redis::V1beta1::InstanceAuthString](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1beta1/latest/Google-Cloud-Redis-V1beta1-InstanceAuthString)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Redis::V1beta1::InstanceAuthString](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1beta1/latest/Google-Cloud-Redis-V1beta1-InstanceAuthString)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #import_instance
    
    
    def import_instance(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the import_instance REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Redis::V1beta1::ImportInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1beta1/latest/Google-Cloud-Redis-V1beta1-ImportInstanceRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1beta1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1beta1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_instances
    
    
    def list_instances(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Redis::V1beta1::ListInstancesResponse

Baseline implementation for the list_instances REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Redis::V1beta1::ListInstancesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1beta1/latest/Google-Cloud-Redis-V1beta1-ListInstancesRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Redis::V1beta1::ListInstancesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1beta1/latest/Google-Cloud-Redis-V1beta1-ListInstancesResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Redis::V1beta1::ListInstancesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1beta1/latest/Google-Cloud-Redis-V1beta1-ListInstancesResponse)) — A result object deserialized from the server's reply 



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

  * **request_pb** ([::Google::Cloud::Redis::V1beta1::RescheduleMaintenanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1beta1/latest/Google-Cloud-Redis-V1beta1-RescheduleMaintenanceRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1beta1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1beta1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



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

  * **request_pb** ([::Google::Cloud::Redis::V1beta1::UpdateInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1beta1/latest/Google-Cloud-Redis-V1beta1-UpdateInstanceRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1beta1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1beta1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #upgrade_instance
    
    
    def upgrade_instance(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the upgrade_instance REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Redis::V1beta1::UpgradeInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1beta1/latest/Google-Cloud-Redis-V1beta1-UpgradeInstanceRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1beta1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1beta1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
