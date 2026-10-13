---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-Environments-Rest-ServiceStub/
title: Cloud Composer V1 API - Class Google::Cloud::Orchestration::Airflow::Service::V1::Environments::Rest::ServiceStub (v1.9.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:35:09.268705+00:00
---

# Cloud Composer V1 API - Class Google::Cloud::Orchestration::Airflow::Service::V1::Environments::Rest::ServiceStub (v1.9.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-Environments-Rest-ServiceStub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Composer V1 API - Class Google::Cloud::Orchestration::Airflow::Service::V1::Environments::Rest::ServiceStub (v1.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.9.0 (latest)  1.8.0  1.7.0  1.6.1  1.5.0  1.4.0  1.3.4  1.2.0  1.1.0  1.0.1  0.11.0  0.10.0  0.9.2  0.8.0  0.7.0  0.6.1  0.5.0  0.4.0  0.3.1  0.2.0  0.1.2 

Reference documentation and code samples for the Cloud Composer V1 API class Google::Cloud::Orchestration::Airflow::Service::V1::Environments::Rest::ServiceStub.

REST service stub for the Environments service. Service stub contains baseline method implementations including transcoding, making the REST call, and deserialing the response.

## Inherits

  * Object 



## Methods 

### #check_upgrade
    
    
    def check_upgrade(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the check_upgrade REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Orchestration::Airflow::Service::V1::CheckUpgradeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-CheckUpgradeRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_environment
    
    
    def create_environment(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the create_environment REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Orchestration::Airflow::Service::V1::CreateEnvironmentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-CreateEnvironmentRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_user_workloads_config_map
    
    
    def create_user_workloads_config_map(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsConfigMap

Baseline implementation for the create_user_workloads_config_map REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Orchestration::Airflow::Service::V1::CreateUserWorkloadsConfigMapRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-CreateUserWorkloadsConfigMapRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsConfigMap](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-UserWorkloadsConfigMap)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsConfigMap](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-UserWorkloadsConfigMap)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_user_workloads_secret
    
    
    def create_user_workloads_secret(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsSecret

Baseline implementation for the create_user_workloads_secret REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Orchestration::Airflow::Service::V1::CreateUserWorkloadsSecretRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-CreateUserWorkloadsSecretRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsSecret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-UserWorkloadsSecret)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsSecret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-UserWorkloadsSecret)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #database_failover
    
    
    def database_failover(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the database_failover REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Orchestration::Airflow::Service::V1::DatabaseFailoverRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-DatabaseFailoverRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_environment
    
    
    def delete_environment(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the delete_environment REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Orchestration::Airflow::Service::V1::DeleteEnvironmentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-DeleteEnvironmentRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_user_workloads_config_map
    
    
    def delete_user_workloads_config_map(request_pb, options = nil) { |result, operation| ... } -> ::Google::Protobuf::Empty

Baseline implementation for the delete_user_workloads_config_map REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Orchestration::Airflow::Service::V1::DeleteUserWorkloadsConfigMapRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-DeleteUserWorkloadsConfigMapRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Protobuf-Empty)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_user_workloads_secret
    
    
    def delete_user_workloads_secret(request_pb, options = nil) { |result, operation| ... } -> ::Google::Protobuf::Empty

Baseline implementation for the delete_user_workloads_secret REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Orchestration::Airflow::Service::V1::DeleteUserWorkloadsSecretRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-DeleteUserWorkloadsSecretRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Protobuf-Empty)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #endpoint
    
    
    def endpoint() -> String

The effective endpoint

**Returns**

  * (String) 



### #execute_airflow_command
    
    
    def execute_airflow_command(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Orchestration::Airflow::Service::V1::ExecuteAirflowCommandResponse

Baseline implementation for the execute_airflow_command REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Orchestration::Airflow::Service::V1::ExecuteAirflowCommandRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-ExecuteAirflowCommandRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Orchestration::Airflow::Service::V1::ExecuteAirflowCommandResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-ExecuteAirflowCommandResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Orchestration::Airflow::Service::V1::ExecuteAirflowCommandResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-ExecuteAirflowCommandResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #fetch_database_properties
    
    
    def fetch_database_properties(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Orchestration::Airflow::Service::V1::FetchDatabasePropertiesResponse

Baseline implementation for the fetch_database_properties REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Orchestration::Airflow::Service::V1::FetchDatabasePropertiesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-FetchDatabasePropertiesRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Orchestration::Airflow::Service::V1::FetchDatabasePropertiesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-FetchDatabasePropertiesResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Orchestration::Airflow::Service::V1::FetchDatabasePropertiesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-FetchDatabasePropertiesResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_environment
    
    
    def get_environment(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Orchestration::Airflow::Service::V1::Environment

Baseline implementation for the get_environment REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Orchestration::Airflow::Service::V1::GetEnvironmentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-GetEnvironmentRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Orchestration::Airflow::Service::V1::Environment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-Environment)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Orchestration::Airflow::Service::V1::Environment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-Environment)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_user_workloads_config_map
    
    
    def get_user_workloads_config_map(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsConfigMap

Baseline implementation for the get_user_workloads_config_map REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Orchestration::Airflow::Service::V1::GetUserWorkloadsConfigMapRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-GetUserWorkloadsConfigMapRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsConfigMap](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-UserWorkloadsConfigMap)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsConfigMap](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-UserWorkloadsConfigMap)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_user_workloads_secret
    
    
    def get_user_workloads_secret(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsSecret

Baseline implementation for the get_user_workloads_secret REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Orchestration::Airflow::Service::V1::GetUserWorkloadsSecretRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-GetUserWorkloadsSecretRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsSecret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-UserWorkloadsSecret)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsSecret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-UserWorkloadsSecret)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_environments
    
    
    def list_environments(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Orchestration::Airflow::Service::V1::ListEnvironmentsResponse

Baseline implementation for the list_environments REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Orchestration::Airflow::Service::V1::ListEnvironmentsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-ListEnvironmentsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Orchestration::Airflow::Service::V1::ListEnvironmentsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-ListEnvironmentsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Orchestration::Airflow::Service::V1::ListEnvironmentsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-ListEnvironmentsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_user_workloads_config_maps
    
    
    def list_user_workloads_config_maps(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Orchestration::Airflow::Service::V1::ListUserWorkloadsConfigMapsResponse

Baseline implementation for the list_user_workloads_config_maps REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Orchestration::Airflow::Service::V1::ListUserWorkloadsConfigMapsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-ListUserWorkloadsConfigMapsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Orchestration::Airflow::Service::V1::ListUserWorkloadsConfigMapsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-ListUserWorkloadsConfigMapsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Orchestration::Airflow::Service::V1::ListUserWorkloadsConfigMapsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-ListUserWorkloadsConfigMapsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_user_workloads_secrets
    
    
    def list_user_workloads_secrets(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Orchestration::Airflow::Service::V1::ListUserWorkloadsSecretsResponse

Baseline implementation for the list_user_workloads_secrets REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Orchestration::Airflow::Service::V1::ListUserWorkloadsSecretsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-ListUserWorkloadsSecretsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Orchestration::Airflow::Service::V1::ListUserWorkloadsSecretsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-ListUserWorkloadsSecretsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Orchestration::Airflow::Service::V1::ListUserWorkloadsSecretsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-ListUserWorkloadsSecretsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_workloads
    
    
    def list_workloads(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Orchestration::Airflow::Service::V1::ListWorkloadsResponse

Baseline implementation for the list_workloads REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Orchestration::Airflow::Service::V1::ListWorkloadsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-ListWorkloadsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Orchestration::Airflow::Service::V1::ListWorkloadsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-ListWorkloadsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Orchestration::Airflow::Service::V1::ListWorkloadsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-ListWorkloadsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #load_snapshot
    
    
    def load_snapshot(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the load_snapshot REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Orchestration::Airflow::Service::V1::LoadSnapshotRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-LoadSnapshotRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #logger
    
    
    def logger(stub: false) -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #poll_airflow_command
    
    
    def poll_airflow_command(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Orchestration::Airflow::Service::V1::PollAirflowCommandResponse

Baseline implementation for the poll_airflow_command REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Orchestration::Airflow::Service::V1::PollAirflowCommandRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-PollAirflowCommandRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Orchestration::Airflow::Service::V1::PollAirflowCommandResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-PollAirflowCommandResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Orchestration::Airflow::Service::V1::PollAirflowCommandResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-PollAirflowCommandResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #save_snapshot
    
    
    def save_snapshot(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the save_snapshot REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Orchestration::Airflow::Service::V1::SaveSnapshotRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-SaveSnapshotRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #stop_airflow_command
    
    
    def stop_airflow_command(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Orchestration::Airflow::Service::V1::StopAirflowCommandResponse

Baseline implementation for the stop_airflow_command REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Orchestration::Airflow::Service::V1::StopAirflowCommandRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-StopAirflowCommandRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Orchestration::Airflow::Service::V1::StopAirflowCommandResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-StopAirflowCommandResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Orchestration::Airflow::Service::V1::StopAirflowCommandResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-StopAirflowCommandResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_environment
    
    
    def update_environment(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the update_environment REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Orchestration::Airflow::Service::V1::UpdateEnvironmentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-UpdateEnvironmentRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #update_user_workloads_config_map
    
    
    def update_user_workloads_config_map(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsConfigMap

Baseline implementation for the update_user_workloads_config_map REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Orchestration::Airflow::Service::V1::UpdateUserWorkloadsConfigMapRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-UpdateUserWorkloadsConfigMapRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsConfigMap](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-UserWorkloadsConfigMap)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsConfigMap](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-UserWorkloadsConfigMap)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #update_user_workloads_secret
    
    
    def update_user_workloads_secret(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsSecret

Baseline implementation for the update_user_workloads_secret REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Orchestration::Airflow::Service::V1::UpdateUserWorkloadsSecretRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-UpdateUserWorkloadsSecretRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsSecret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-UserWorkloadsSecret)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsSecret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-UserWorkloadsSecret)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
