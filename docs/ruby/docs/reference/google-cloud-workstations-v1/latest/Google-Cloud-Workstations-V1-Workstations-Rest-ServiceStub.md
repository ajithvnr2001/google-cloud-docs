---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Cloud-Workstations-V1-Workstations-Rest-ServiceStub/
title: Cloud Workstations V1 API - Class Google::Cloud::Workstations::V1::Workstations::Rest::ServiceStub (v1.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:24:00.781459+00:00
---

# Cloud Workstations V1 API - Class Google::Cloud::Workstations::V1::Workstations::Rest::ServiceStub (v1.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Cloud-Workstations-V1-Workstations-Rest-ServiceStub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Workstations V1 API - Class Google::Cloud::Workstations::V1::Workstations::Rest::ServiceStub (v1.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.6.1 (latest)  1.6.0  1.5.0  1.4.1  1.3.1  1.2.0  1.1.1  1.0.1  0.3.0  0.2.0  0.1.3 

Reference documentation and code samples for the Cloud Workstations V1 API class Google::Cloud::Workstations::V1::Workstations::Rest::ServiceStub.

REST service stub for the Workstations service. Service stub contains baseline method implementations including transcoding, making the REST call, and deserialing the response.

## Inherits

  * Object 



## Methods 

### #create_workstation
    
    
    def create_workstation(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the create_workstation REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Workstations::V1::CreateWorkstationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Cloud-Workstations-V1-CreateWorkstationRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_workstation_cluster
    
    
    def create_workstation_cluster(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the create_workstation_cluster REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Workstations::V1::CreateWorkstationClusterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Cloud-Workstations-V1-CreateWorkstationClusterRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_workstation_config
    
    
    def create_workstation_config(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the create_workstation_config REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Workstations::V1::CreateWorkstationConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Cloud-Workstations-V1-CreateWorkstationConfigRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_workstation
    
    
    def delete_workstation(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the delete_workstation REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Workstations::V1::DeleteWorkstationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Cloud-Workstations-V1-DeleteWorkstationRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_workstation_cluster
    
    
    def delete_workstation_cluster(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the delete_workstation_cluster REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Workstations::V1::DeleteWorkstationClusterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Cloud-Workstations-V1-DeleteWorkstationClusterRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_workstation_config
    
    
    def delete_workstation_config(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the delete_workstation_config REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Workstations::V1::DeleteWorkstationConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Cloud-Workstations-V1-DeleteWorkstationConfigRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #endpoint
    
    
    def endpoint() -> String

The effective endpoint

**Returns**

  * (String) 



### #generate_access_token
    
    
    def generate_access_token(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Workstations::V1::GenerateAccessTokenResponse

Baseline implementation for the generate_access_token REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Workstations::V1::GenerateAccessTokenRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Cloud-Workstations-V1-GenerateAccessTokenRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Workstations::V1::GenerateAccessTokenResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Cloud-Workstations-V1-GenerateAccessTokenResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Workstations::V1::GenerateAccessTokenResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Cloud-Workstations-V1-GenerateAccessTokenResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_workstation
    
    
    def get_workstation(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Workstations::V1::Workstation

Baseline implementation for the get_workstation REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Workstations::V1::GetWorkstationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Cloud-Workstations-V1-GetWorkstationRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Workstations::V1::Workstation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Cloud-Workstations-V1-Workstation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Workstations::V1::Workstation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Cloud-Workstations-V1-Workstation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_workstation_cluster
    
    
    def get_workstation_cluster(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Workstations::V1::WorkstationCluster

Baseline implementation for the get_workstation_cluster REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Workstations::V1::GetWorkstationClusterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Cloud-Workstations-V1-GetWorkstationClusterRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Workstations::V1::WorkstationCluster](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Cloud-Workstations-V1-WorkstationCluster)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Workstations::V1::WorkstationCluster](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Cloud-Workstations-V1-WorkstationCluster)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_workstation_config
    
    
    def get_workstation_config(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Workstations::V1::WorkstationConfig

Baseline implementation for the get_workstation_config REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Workstations::V1::GetWorkstationConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Cloud-Workstations-V1-GetWorkstationConfigRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Workstations::V1::WorkstationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Cloud-Workstations-V1-WorkstationConfig)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Workstations::V1::WorkstationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Cloud-Workstations-V1-WorkstationConfig)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_usable_workstation_configs
    
    
    def list_usable_workstation_configs(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Workstations::V1::ListUsableWorkstationConfigsResponse

Baseline implementation for the list_usable_workstation_configs REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Workstations::V1::ListUsableWorkstationConfigsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Cloud-Workstations-V1-ListUsableWorkstationConfigsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Workstations::V1::ListUsableWorkstationConfigsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Cloud-Workstations-V1-ListUsableWorkstationConfigsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Workstations::V1::ListUsableWorkstationConfigsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Cloud-Workstations-V1-ListUsableWorkstationConfigsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_usable_workstations
    
    
    def list_usable_workstations(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Workstations::V1::ListUsableWorkstationsResponse

Baseline implementation for the list_usable_workstations REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Workstations::V1::ListUsableWorkstationsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Cloud-Workstations-V1-ListUsableWorkstationsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Workstations::V1::ListUsableWorkstationsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Cloud-Workstations-V1-ListUsableWorkstationsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Workstations::V1::ListUsableWorkstationsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Cloud-Workstations-V1-ListUsableWorkstationsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_workstation_clusters
    
    
    def list_workstation_clusters(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Workstations::V1::ListWorkstationClustersResponse

Baseline implementation for the list_workstation_clusters REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Workstations::V1::ListWorkstationClustersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Cloud-Workstations-V1-ListWorkstationClustersRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Workstations::V1::ListWorkstationClustersResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Cloud-Workstations-V1-ListWorkstationClustersResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Workstations::V1::ListWorkstationClustersResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Cloud-Workstations-V1-ListWorkstationClustersResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_workstation_configs
    
    
    def list_workstation_configs(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Workstations::V1::ListWorkstationConfigsResponse

Baseline implementation for the list_workstation_configs REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Workstations::V1::ListWorkstationConfigsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Cloud-Workstations-V1-ListWorkstationConfigsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Workstations::V1::ListWorkstationConfigsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Cloud-Workstations-V1-ListWorkstationConfigsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Workstations::V1::ListWorkstationConfigsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Cloud-Workstations-V1-ListWorkstationConfigsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_workstations
    
    
    def list_workstations(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Workstations::V1::ListWorkstationsResponse

Baseline implementation for the list_workstations REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Workstations::V1::ListWorkstationsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Cloud-Workstations-V1-ListWorkstationsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Workstations::V1::ListWorkstationsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Cloud-Workstations-V1-ListWorkstationsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Workstations::V1::ListWorkstationsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Cloud-Workstations-V1-ListWorkstationsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #logger
    
    
    def logger(stub: false) -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #start_workstation
    
    
    def start_workstation(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the start_workstation REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Workstations::V1::StartWorkstationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Cloud-Workstations-V1-StartWorkstationRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #stop_workstation
    
    
    def stop_workstation(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the stop_workstation REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Workstations::V1::StopWorkstationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Cloud-Workstations-V1-StopWorkstationRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_workstation
    
    
    def update_workstation(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the update_workstation REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Workstations::V1::UpdateWorkstationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Cloud-Workstations-V1-UpdateWorkstationRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #update_workstation_cluster
    
    
    def update_workstation_cluster(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the update_workstation_cluster REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Workstations::V1::UpdateWorkstationClusterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Cloud-Workstations-V1-UpdateWorkstationClusterRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #update_workstation_config
    
    
    def update_workstation_config(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the update_workstation_config REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Workstations::V1::UpdateWorkstationConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Cloud-Workstations-V1-UpdateWorkstationConfigRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
