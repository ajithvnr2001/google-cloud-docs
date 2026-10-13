---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Config-Client/
title: Infrastructure Manager V1 API - Class Google::Cloud::ConfigService::V1::Config::Client (v2.12.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:28:04.251631+00:00
---

# Infrastructure Manager V1 API - Class Google::Cloud::ConfigService::V1::Config::Client (v2.12.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Config-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Infrastructure Manager V1 API - Class Google::Cloud::ConfigService::V1::Config::Client (v2.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.12.0 (latest)  2.11.0  2.10.1  2.9.0  2.8.0  2.7.0  2.6.0  2.5.1  2.4.0  2.3.0  2.2.0  2.1.0  2.0.1  1.3.0  1.2.1  1.1.0  1.0.2  0.6.0  0.5.0  0.4.0  0.3.1  0.2.1  0.1.0 

Reference documentation and code samples for the Infrastructure Manager V1 API class Google::Cloud::ConfigService::V1::Config::Client.

Client for the Config service.

Infrastructure Manager is a managed service that automates the deployment and management of Google Cloud infrastructure resources.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::ConfigService::V1::Config::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Config-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the Config Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Config-Client-Configuration "Google::Cloud::ConfigService::V1::Config::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Config-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Config-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all Config clients
    ::Google::Cloud::ConfigService::V1::Config::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the Config Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Config-Client#Google__Cloud__ConfigService__V1__Config__Client_configure_class_ "Google::Cloud::ConfigService::V1::Config::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Config-Client-Configuration "Google::Cloud::ConfigService::V1::Config::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Config-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Config-Client-Configuration)) 



### #create_deployment
    
    
    def create_deployment(request, options = nil) -> ::Gapic::Operation
    def create_deployment(parent: nil, deployment_id: nil, deployment: nil, request_id: nil) -> ::Gapic::Operation

Creates a [Deployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Deployment "Google::Cloud::ConfigService::V1::Deployment \(class\)").

**Overloads**
    
    
    def create_deployment(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_deployment` via a request object, either of type [Google::Cloud::ConfigService::V1::CreateDeploymentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-CreateDeploymentRequest "Google::Cloud::ConfigService::V1::CreateDeploymentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ConfigService::V1::CreateDeploymentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-CreateDeploymentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_deployment(parent: nil, deployment_id: nil, deployment: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `create_deployment` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent in whose context the Deployment is created. The parent value is in the format: 'projects/{project_id}/locations/{location}'. 
  * **deployment_id** (::String) — Required. The Deployment ID. 
  * **deployment** ([::Google::Cloud::ConfigService::V1::Deployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Deployment), ::Hash) — Required. [Deployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Deployment "Google::Cloud::ConfigService::V1::Deployment \(class\)") resource to be created. 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/config_service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ConfigService::V1::Config::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ConfigService::V1::CreateDeploymentRequest.new
    
    # Call the create_deployment method.
    result = client.create_deployment request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #create_deployment_group
    
    
    def create_deployment_group(request, options = nil) -> ::Gapic::Operation
    def create_deployment_group(parent: nil, deployment_group_id: nil, deployment_group: nil, request_id: nil) -> ::Gapic::Operation

Creates a [DeploymentGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-DeploymentGroup "Google::Cloud::ConfigService::V1::DeploymentGroup \(class\)") The newly created DeploymentGroup will be in the `CREATING` state and can be retrieved via Get and List calls.

**Overloads**
    
    
    def create_deployment_group(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_deployment_group` via a request object, either of type [Google::Cloud::ConfigService::V1::CreateDeploymentGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-CreateDeploymentGroupRequest "Google::Cloud::ConfigService::V1::CreateDeploymentGroupRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ConfigService::V1::CreateDeploymentGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-CreateDeploymentGroupRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_deployment_group(parent: nil, deployment_group_id: nil, deployment_group: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `create_deployment_group` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent in whose context the Deployment Group is created. The parent value is in the format: 'projects/{project_id}/locations/{location}' 
  * **deployment_group_id** (::String) — Required. The deployment group ID. 
  * **deployment_group** ([::Google::Cloud::ConfigService::V1::DeploymentGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-DeploymentGroup), ::Hash) — Required. [Deployment Group][] resource to create 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/config_service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ConfigService::V1::Config::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ConfigService::V1::CreateDeploymentGroupRequest.new
    
    # Call the create_deployment_group method.
    result = client.create_deployment_group request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #create_preview
    
    
    def create_preview(request, options = nil) -> ::Gapic::Operation
    def create_preview(parent: nil, preview_id: nil, preview: nil, request_id: nil) -> ::Gapic::Operation

Creates a [Preview](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Preview "Google::Cloud::ConfigService::V1::Preview \(class\)").

**Overloads**
    
    
    def create_preview(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_preview` via a request object, either of type [Google::Cloud::ConfigService::V1::CreatePreviewRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-CreatePreviewRequest "Google::Cloud::ConfigService::V1::CreatePreviewRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ConfigService::V1::CreatePreviewRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-CreatePreviewRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_preview(parent: nil, preview_id: nil, preview: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `create_preview` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent in whose context the Preview is created. The parent value is in the format: 'projects/{project_id}/locations/{location}'. 
  * **preview_id** (::String) — Optional. The preview ID. 
  * **preview** ([::Google::Cloud::ConfigService::V1::Preview](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Preview), ::Hash) — Required. [Preview](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Preview "Google::Cloud::ConfigService::V1::Preview \(class\)") resource to be created. 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/config_service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ConfigService::V1::Config::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ConfigService::V1::CreatePreviewRequest.new
    
    # Call the create_preview method.
    result = client.create_preview request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_deployment
    
    
    def delete_deployment(request, options = nil) -> ::Gapic::Operation
    def delete_deployment(name: nil, request_id: nil, force: nil, delete_policy: nil) -> ::Gapic::Operation

Deletes a [Deployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Deployment "Google::Cloud::ConfigService::V1::Deployment \(class\)").

**Overloads**
    
    
    def delete_deployment(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_deployment` via a request object, either of type [DeleteDeploymentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-DeleteDeploymentRequest "Google::Cloud::ConfigService::V1::DeleteDeploymentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ConfigService::V1::DeleteDeploymentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-DeleteDeploymentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_deployment(name: nil, request_id: nil, force: nil, delete_policy: nil) -> ::Gapic::Operation

Pass arguments to `delete_deployment` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the Deployment in the format: 'projects/{project_id}/locations/{location}/deployments/{deployment}'. 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

  * **force** (::Boolean) — Optional. If set to true, any revisions for this deployment will also be deleted. (Otherwise, the request will only work if the deployment has no revisions.) 
  * **delete_policy** ([::Google::Cloud::ConfigService::V1::DeleteDeploymentRequest::DeletePolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-DeleteDeploymentRequest-DeletePolicy)) — Optional. Policy on how resources actuated by the deployment should be deleted. If unspecified, the default behavior is to delete the underlying resources. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/config_service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ConfigService::V1::Config::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ConfigService::V1::DeleteDeploymentRequest.new
    
    # Call the delete_deployment method.
    result = client.delete_deployment request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_deployment_group
    
    
    def delete_deployment_group(request, options = nil) -> ::Gapic::Operation
    def delete_deployment_group(name: nil, request_id: nil, force: nil, deployment_reference_policy: nil) -> ::Gapic::Operation

Deletes a [DeploymentGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-DeploymentGroup "Google::Cloud::ConfigService::V1::DeploymentGroup \(class\)")

**Overloads**
    
    
    def delete_deployment_group(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_deployment_group` via a request object, either of type [DeleteDeploymentGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-DeleteDeploymentGroupRequest "Google::Cloud::ConfigService::V1::DeleteDeploymentGroupRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ConfigService::V1::DeleteDeploymentGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-DeleteDeploymentGroupRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_deployment_group(name: nil, request_id: nil, force: nil, deployment_reference_policy: nil) -> ::Gapic::Operation

Pass arguments to `delete_deployment_group` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of DeploymentGroup in the format projects/{project_id}/locations/{location_id}/deploymentGroups/{deploymentGroup} 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

  * **force** (::Boolean) — Optional. If set to true, any revisions for this deployment group will also be deleted. (Otherwise, the request will only work if the deployment group has no revisions.) 
  * **deployment_reference_policy** ([::Google::Cloud::ConfigService::V1::DeleteDeploymentGroupRequest::DeploymentReferencePolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-DeleteDeploymentGroupRequest-DeploymentReferencePolicy)) — Optional. Policy on how to handle referenced deployments when deleting the DeploymentGroup. If unspecified, the default behavior is to fail the deletion if any deployments currently referenced in the `deployment_units` of the DeploymentGroup or in the latest revision are not deleted. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/config_service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ConfigService::V1::Config::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ConfigService::V1::DeleteDeploymentGroupRequest.new
    
    # Call the delete_deployment_group method.
    result = client.delete_deployment_group request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_preview
    
    
    def delete_preview(request, options = nil) -> ::Gapic::Operation
    def delete_preview(name: nil, request_id: nil) -> ::Gapic::Operation

Deletes a [Preview](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Preview "Google::Cloud::ConfigService::V1::Preview \(class\)").

**Overloads**
    
    
    def delete_preview(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_preview` via a request object, either of type [DeletePreviewRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-DeletePreviewRequest "Google::Cloud::ConfigService::V1::DeletePreviewRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ConfigService::V1::DeletePreviewRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-DeletePreviewRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_preview(name: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `delete_preview` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the Preview in the format: 'projects/{project_id}/locations/{location}/previews/{preview}'. 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/config_service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ConfigService::V1::Config::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ConfigService::V1::DeletePreviewRequest.new
    
    # Call the delete_preview method.
    result = client.delete_preview request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_statefile
    
    
    def delete_statefile(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_statefile(name: nil, lock_id: nil) -> ::Google::Protobuf::Empty

Deletes Terraform state file in a given deployment.

**Overloads**
    
    
    def delete_statefile(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_statefile` via a request object, either of type [DeleteStatefileRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-DeleteStatefileRequest "Google::Cloud::ConfigService::V1::DeleteStatefileRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ConfigService::V1::DeleteStatefileRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-DeleteStatefileRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_statefile(name: nil, lock_id: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_statefile` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the deployment in the format: 'projects/{project_id}/locations/{location}/deployments/{deployment}'. 
  * **lock_id** (::Integer) — Required. Lock ID of the lock file to verify that the user who is deleting the state file previously locked the Deployment. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/config_service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ConfigService::V1::Config::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ConfigService::V1::DeleteStatefileRequest.new
    
    # Call the delete_statefile method.
    result = client.delete_statefile request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #deprovision_deployment_group
    
    
    def deprovision_deployment_group(request, options = nil) -> ::Gapic::Operation
    def deprovision_deployment_group(name: nil, force: nil, delete_policy: nil) -> ::Gapic::Operation

Deprovisions a deployment group.

NOTE: As a first step of this operation, Infra Manager will automatically delete any Deployments that were part of the _last successful_ [DeploymentGroupRevision](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-DeploymentGroupRevision "Google::Cloud::ConfigService::V1::DeploymentGroupRevision \(class\)") but are _no longer_ included in the _current_ [DeploymentGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-DeploymentGroup "Google::Cloud::ConfigService::V1::DeploymentGroup \(class\)") definition (e.g., following an `UpdateDeploymentGroup` call), along with their actuated resources.

**Overloads**
    
    
    def deprovision_deployment_group(request, options = nil) -> ::Gapic::Operation

Pass arguments to `deprovision_deployment_group` via a request object, either of type [DeprovisionDeploymentGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-DeprovisionDeploymentGroupRequest "Google::Cloud::ConfigService::V1::DeprovisionDeploymentGroupRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ConfigService::V1::DeprovisionDeploymentGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-DeprovisionDeploymentGroupRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def deprovision_deployment_group(name: nil, force: nil, delete_policy: nil) -> ::Gapic::Operation

Pass arguments to `deprovision_deployment_group` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the deployment group to deprovision. Format: 'projects/{project_id}/locations/{location}/deploymentGroups/{deployment_group}'. 
  * **force** (::Boolean) — Optional. If set to true, this option is propagated to the deletion of each deployment in the group. This corresponds to the 'force' field in DeleteDeploymentRequest. 
  * **delete_policy** ([::Google::Cloud::ConfigService::V1::DeleteDeploymentRequest::DeletePolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-DeleteDeploymentRequest-DeletePolicy)) — Optional. Policy on how resources within each deployment should be handled during deletion. This policy is applied globally to the deletion of all deployments in this group. This corresponds to the 'delete_policy' field in DeleteDeploymentRequest. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/config_service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ConfigService::V1::Config::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ConfigService::V1::DeprovisionDeploymentGroupRequest.new
    
    # Call the deprovision_deployment_group method.
    result = client.deprovision_deployment_group request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #export_deployment_statefile
    
    
    def export_deployment_statefile(request, options = nil) -> ::Google::Cloud::ConfigService::V1::Statefile
    def export_deployment_statefile(parent: nil, draft: nil) -> ::Google::Cloud::ConfigService::V1::Statefile

Exports Terraform state file from a given deployment.

**Overloads**
    
    
    def export_deployment_statefile(request, options = nil) -> ::Google::Cloud::ConfigService::V1::Statefile

Pass arguments to `export_deployment_statefile` via a request object, either of type [ExportDeploymentStatefileRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ExportDeploymentStatefileRequest "Google::Cloud::ConfigService::V1::ExportDeploymentStatefileRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ConfigService::V1::ExportDeploymentStatefileRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ExportDeploymentStatefileRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def export_deployment_statefile(parent: nil, draft: nil) -> ::Google::Cloud::ConfigService::V1::Statefile

Pass arguments to `export_deployment_statefile` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent in whose context the statefile is listed. The parent value is in the format: 'projects/{project_id}/locations/{location}/deployments/{deployment}'. 
  * **draft** (::Boolean) — Optional. If this flag is set to true, the exported deployment state file will be the draft state. This will enable the draft file to be validated before copying it over to the working state on unlock. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::ConfigService::V1::Statefile](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Statefile)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::ConfigService::V1::Statefile](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Statefile)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/config_service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ConfigService::V1::Config::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ConfigService::V1::ExportDeploymentStatefileRequest.new
    
    # Call the export_deployment_statefile method.
    result = client.export_deployment_statefile request
    
    # The returned object is of type Google::Cloud::ConfigService::V1::Statefile.
    p result

### #export_lock_info
    
    
    def export_lock_info(request, options = nil) -> ::Google::Cloud::ConfigService::V1::LockInfo
    def export_lock_info(name: nil) -> ::Google::Cloud::ConfigService::V1::LockInfo

Exports the lock info on a locked deployment.

**Overloads**
    
    
    def export_lock_info(request, options = nil) -> ::Google::Cloud::ConfigService::V1::LockInfo

Pass arguments to `export_lock_info` via a request object, either of type [ExportLockInfoRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ExportLockInfoRequest "Google::Cloud::ConfigService::V1::ExportLockInfoRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ConfigService::V1::ExportLockInfoRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ExportLockInfoRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def export_lock_info(name: nil) -> ::Google::Cloud::ConfigService::V1::LockInfo

Pass arguments to `export_lock_info` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the deployment in the format: 'projects/{project_id}/locations/{location}/deployments/{deployment}'. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::ConfigService::V1::LockInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-LockInfo)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::ConfigService::V1::LockInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-LockInfo)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/config_service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ConfigService::V1::Config::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ConfigService::V1::ExportLockInfoRequest.new
    
    # Call the export_lock_info method.
    result = client.export_lock_info request
    
    # The returned object is of type Google::Cloud::ConfigService::V1::LockInfo.
    p result

### #export_preview_result
    
    
    def export_preview_result(request, options = nil) -> ::Google::Cloud::ConfigService::V1::ExportPreviewResultResponse
    def export_preview_result(parent: nil) -> ::Google::Cloud::ConfigService::V1::ExportPreviewResultResponse

Export [Preview](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Preview "Google::Cloud::ConfigService::V1::Preview \(class\)") results.

**Overloads**
    
    
    def export_preview_result(request, options = nil) -> ::Google::Cloud::ConfigService::V1::ExportPreviewResultResponse

Pass arguments to `export_preview_result` via a request object, either of type [ExportPreviewResultRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ExportPreviewResultRequest "Google::Cloud::ConfigService::V1::ExportPreviewResultRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ConfigService::V1::ExportPreviewResultRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ExportPreviewResultRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def export_preview_result(parent: nil) -> ::Google::Cloud::ConfigService::V1::ExportPreviewResultResponse

Pass arguments to `export_preview_result` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **parent** (::String) — Required. The preview whose results should be exported. The preview value is in the format: 'projects/{project_id}/locations/{location}/previews/{preview}'. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::ConfigService::V1::ExportPreviewResultResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ExportPreviewResultResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::ConfigService::V1::ExportPreviewResultResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ExportPreviewResultResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/config_service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ConfigService::V1::Config::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ConfigService::V1::ExportPreviewResultRequest.new
    
    # Call the export_preview_result method.
    result = client.export_preview_result request
    
    # The returned object is of type Google::Cloud::ConfigService::V1::ExportPreviewResultResponse.
    p result

### #export_revision_statefile
    
    
    def export_revision_statefile(request, options = nil) -> ::Google::Cloud::ConfigService::V1::Statefile
    def export_revision_statefile(parent: nil) -> ::Google::Cloud::ConfigService::V1::Statefile

Exports Terraform state file from a given revision.

**Overloads**
    
    
    def export_revision_statefile(request, options = nil) -> ::Google::Cloud::ConfigService::V1::Statefile

Pass arguments to `export_revision_statefile` via a request object, either of type [ExportRevisionStatefileRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ExportRevisionStatefileRequest "Google::Cloud::ConfigService::V1::ExportRevisionStatefileRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ConfigService::V1::ExportRevisionStatefileRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ExportRevisionStatefileRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def export_revision_statefile(parent: nil) -> ::Google::Cloud::ConfigService::V1::Statefile

Pass arguments to `export_revision_statefile` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **parent** (::String) — Required. The parent in whose context the statefile is listed. The parent value is in the format: 'projects/{project_id}/locations/{location}/deployments/{deployment}/revisions/{revision}'. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::ConfigService::V1::Statefile](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Statefile)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::ConfigService::V1::Statefile](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Statefile)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/config_service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ConfigService::V1::Config::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ConfigService::V1::ExportRevisionStatefileRequest.new
    
    # Call the export_revision_statefile method.
    result = client.export_revision_statefile request
    
    # The returned object is of type Google::Cloud::ConfigService::V1::Statefile.
    p result

### #get_auto_migration_config
    
    
    def get_auto_migration_config(request, options = nil) -> ::Google::Cloud::ConfigService::V1::AutoMigrationConfig
    def get_auto_migration_config(name: nil) -> ::Google::Cloud::ConfigService::V1::AutoMigrationConfig

Get the AutoMigrationConfig for a given project and location.

**Overloads**
    
    
    def get_auto_migration_config(request, options = nil) -> ::Google::Cloud::ConfigService::V1::AutoMigrationConfig

Pass arguments to `get_auto_migration_config` via a request object, either of type [GetAutoMigrationConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-GetAutoMigrationConfigRequest "Google::Cloud::ConfigService::V1::GetAutoMigrationConfigRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ConfigService::V1::GetAutoMigrationConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-GetAutoMigrationConfigRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_auto_migration_config(name: nil) -> ::Google::Cloud::ConfigService::V1::AutoMigrationConfig

Pass arguments to `get_auto_migration_config` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the AutoMigrationConfig. Format: 'projects/{project_id}/locations/{location}/AutoMigrationConfig'. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::ConfigService::V1::AutoMigrationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-AutoMigrationConfig)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::ConfigService::V1::AutoMigrationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-AutoMigrationConfig)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/config_service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ConfigService::V1::Config::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ConfigService::V1::GetAutoMigrationConfigRequest.new
    
    # Call the get_auto_migration_config method.
    result = client.get_auto_migration_config request
    
    # The returned object is of type Google::Cloud::ConfigService::V1::AutoMigrationConfig.
    p result

### #get_deployment
    
    
    def get_deployment(request, options = nil) -> ::Google::Cloud::ConfigService::V1::Deployment
    def get_deployment(name: nil) -> ::Google::Cloud::ConfigService::V1::Deployment

Gets details about a [Deployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Deployment "Google::Cloud::ConfigService::V1::Deployment \(class\)").

**Overloads**
    
    
    def get_deployment(request, options = nil) -> ::Google::Cloud::ConfigService::V1::Deployment

Pass arguments to `get_deployment` via a request object, either of type [GetDeploymentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-GetDeploymentRequest "Google::Cloud::ConfigService::V1::GetDeploymentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ConfigService::V1::GetDeploymentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-GetDeploymentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_deployment(name: nil) -> ::Google::Cloud::ConfigService::V1::Deployment

Pass arguments to `get_deployment` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the deployment. Format: 'projects/{project_id}/locations/{location}/deployments/{deployment}'. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::ConfigService::V1::Deployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Deployment)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::ConfigService::V1::Deployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Deployment)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/config_service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ConfigService::V1::Config::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ConfigService::V1::GetDeploymentRequest.new
    
    # Call the get_deployment method.
    result = client.get_deployment request
    
    # The returned object is of type Google::Cloud::ConfigService::V1::Deployment.
    p result

### #get_deployment_group
    
    
    def get_deployment_group(request, options = nil) -> ::Google::Cloud::ConfigService::V1::DeploymentGroup
    def get_deployment_group(name: nil) -> ::Google::Cloud::ConfigService::V1::DeploymentGroup

Get a DeploymentGroup for a given project and location.

**Overloads**
    
    
    def get_deployment_group(request, options = nil) -> ::Google::Cloud::ConfigService::V1::DeploymentGroup

Pass arguments to `get_deployment_group` via a request object, either of type [GetDeploymentGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-GetDeploymentGroupRequest "Google::Cloud::ConfigService::V1::GetDeploymentGroupRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ConfigService::V1::GetDeploymentGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-GetDeploymentGroupRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_deployment_group(name: nil) -> ::Google::Cloud::ConfigService::V1::DeploymentGroup

Pass arguments to `get_deployment_group` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the deployment group to retrieve. Format: 'projects/{project_id}/locations/{location}/deploymentGroups/{deployment_group}'. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::ConfigService::V1::DeploymentGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-DeploymentGroup)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::ConfigService::V1::DeploymentGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-DeploymentGroup)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/config_service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ConfigService::V1::Config::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ConfigService::V1::GetDeploymentGroupRequest.new
    
    # Call the get_deployment_group method.
    result = client.get_deployment_group request
    
    # The returned object is of type Google::Cloud::ConfigService::V1::DeploymentGroup.
    p result

### #get_deployment_group_revision
    
    
    def get_deployment_group_revision(request, options = nil) -> ::Google::Cloud::ConfigService::V1::DeploymentGroupRevision
    def get_deployment_group_revision(name: nil) -> ::Google::Cloud::ConfigService::V1::DeploymentGroupRevision

Gets details about a [DeploymentGroupRevision](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-DeploymentGroupRevision "Google::Cloud::ConfigService::V1::DeploymentGroupRevision \(class\)").

**Overloads**
    
    
    def get_deployment_group_revision(request, options = nil) -> ::Google::Cloud::ConfigService::V1::DeploymentGroupRevision

Pass arguments to `get_deployment_group_revision` via a request object, either of type [GetDeploymentGroupRevisionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-GetDeploymentGroupRevisionRequest "Google::Cloud::ConfigService::V1::GetDeploymentGroupRevisionRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ConfigService::V1::GetDeploymentGroupRevisionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-GetDeploymentGroupRevisionRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_deployment_group_revision(name: nil) -> ::Google::Cloud::ConfigService::V1::DeploymentGroupRevision

Pass arguments to `get_deployment_group_revision` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the deployment group revision to retrieve. Format: 'projects/{project_id}/locations/{location}/deploymentGroups/{deployment_group}/revisions/{revision}'. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::ConfigService::V1::DeploymentGroupRevision](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-DeploymentGroupRevision)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::ConfigService::V1::DeploymentGroupRevision](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-DeploymentGroupRevision)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/config_service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ConfigService::V1::Config::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ConfigService::V1::GetDeploymentGroupRevisionRequest.new
    
    # Call the get_deployment_group_revision method.
    result = client.get_deployment_group_revision request
    
    # The returned object is of type Google::Cloud::ConfigService::V1::DeploymentGroupRevision.
    p result

### #get_preview
    
    
    def get_preview(request, options = nil) -> ::Google::Cloud::ConfigService::V1::Preview
    def get_preview(name: nil) -> ::Google::Cloud::ConfigService::V1::Preview

Gets details about a [Preview](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Preview "Google::Cloud::ConfigService::V1::Preview \(class\)").

**Overloads**
    
    
    def get_preview(request, options = nil) -> ::Google::Cloud::ConfigService::V1::Preview

Pass arguments to `get_preview` via a request object, either of type [GetPreviewRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-GetPreviewRequest "Google::Cloud::ConfigService::V1::GetPreviewRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ConfigService::V1::GetPreviewRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-GetPreviewRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_preview(name: nil) -> ::Google::Cloud::ConfigService::V1::Preview

Pass arguments to `get_preview` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the preview. Format: 'projects/{project_id}/locations/{location}/previews/{preview}'. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::ConfigService::V1::Preview](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Preview)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::ConfigService::V1::Preview](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Preview)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/config_service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ConfigService::V1::Config::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ConfigService::V1::GetPreviewRequest.new
    
    # Call the get_preview method.
    result = client.get_preview request
    
    # The returned object is of type Google::Cloud::ConfigService::V1::Preview.
    p result

### #get_resource
    
    
    def get_resource(request, options = nil) -> ::Google::Cloud::ConfigService::V1::Resource
    def get_resource(name: nil) -> ::Google::Cloud::ConfigService::V1::Resource

Gets details about a [Resource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Resource "Google::Cloud::ConfigService::V1::Resource \(class\)") deployed by Infra Manager.

**Overloads**
    
    
    def get_resource(request, options = nil) -> ::Google::Cloud::ConfigService::V1::Resource

Pass arguments to `get_resource` via a request object, either of type [GetResourceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-GetResourceRequest "Google::Cloud::ConfigService::V1::GetResourceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ConfigService::V1::GetResourceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-GetResourceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_resource(name: nil) -> ::Google::Cloud::ConfigService::V1::Resource

Pass arguments to `get_resource` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the Resource in the format: 'projects/{project_id}/locations/{location}/deployments/{deployment}/revisions/{revision}/resource/{resource}'. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::ConfigService::V1::Resource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Resource)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::ConfigService::V1::Resource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Resource)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/config_service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ConfigService::V1::Config::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ConfigService::V1::GetResourceRequest.new
    
    # Call the get_resource method.
    result = client.get_resource request
    
    # The returned object is of type Google::Cloud::ConfigService::V1::Resource.
    p result

### #get_resource_change
    
    
    def get_resource_change(request, options = nil) -> ::Google::Cloud::ConfigService::V1::ResourceChange
    def get_resource_change(name: nil) -> ::Google::Cloud::ConfigService::V1::ResourceChange

Get a ResourceChange for a given preview.

**Overloads**
    
    
    def get_resource_change(request, options = nil) -> ::Google::Cloud::ConfigService::V1::ResourceChange

Pass arguments to `get_resource_change` via a request object, either of type [GetResourceChangeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-GetResourceChangeRequest "Google::Cloud::ConfigService::V1::GetResourceChangeRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ConfigService::V1::GetResourceChangeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-GetResourceChangeRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_resource_change(name: nil) -> ::Google::Cloud::ConfigService::V1::ResourceChange

Pass arguments to `get_resource_change` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the resource change to retrieve. Format: 'projects/{project_id}/locations/{location}/previews/{preview}/resourceChanges/{resource_change}'. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::ConfigService::V1::ResourceChange](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ResourceChange)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::ConfigService::V1::ResourceChange](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ResourceChange)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/config_service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ConfigService::V1::Config::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ConfigService::V1::GetResourceChangeRequest.new
    
    # Call the get_resource_change method.
    result = client.get_resource_change request
    
    # The returned object is of type Google::Cloud::ConfigService::V1::ResourceChange.
    p result

### #get_resource_drift
    
    
    def get_resource_drift(request, options = nil) -> ::Google::Cloud::ConfigService::V1::ResourceDrift
    def get_resource_drift(name: nil) -> ::Google::Cloud::ConfigService::V1::ResourceDrift

Get a ResourceDrift for a given preview.

**Overloads**
    
    
    def get_resource_drift(request, options = nil) -> ::Google::Cloud::ConfigService::V1::ResourceDrift

Pass arguments to `get_resource_drift` via a request object, either of type [GetResourceDriftRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-GetResourceDriftRequest "Google::Cloud::ConfigService::V1::GetResourceDriftRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ConfigService::V1::GetResourceDriftRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-GetResourceDriftRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_resource_drift(name: nil) -> ::Google::Cloud::ConfigService::V1::ResourceDrift

Pass arguments to `get_resource_drift` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the resource drift to retrieve. Format: 'projects/{project_id}/locations/{location}/previews/{preview}/resourceDrifts/{resource_drift}'. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::ConfigService::V1::ResourceDrift](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ResourceDrift)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::ConfigService::V1::ResourceDrift](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ResourceDrift)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/config_service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ConfigService::V1::Config::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ConfigService::V1::GetResourceDriftRequest.new
    
    # Call the get_resource_drift method.
    result = client.get_resource_drift request
    
    # The returned object is of type Google::Cloud::ConfigService::V1::ResourceDrift.
    p result

### #get_revision
    
    
    def get_revision(request, options = nil) -> ::Google::Cloud::ConfigService::V1::Revision
    def get_revision(name: nil) -> ::Google::Cloud::ConfigService::V1::Revision

Gets details about a [Revision](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Revision "Google::Cloud::ConfigService::V1::Revision \(class\)").

**Overloads**
    
    
    def get_revision(request, options = nil) -> ::Google::Cloud::ConfigService::V1::Revision

Pass arguments to `get_revision` via a request object, either of type [GetRevisionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-GetRevisionRequest "Google::Cloud::ConfigService::V1::GetRevisionRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ConfigService::V1::GetRevisionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-GetRevisionRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_revision(name: nil) -> ::Google::Cloud::ConfigService::V1::Revision

Pass arguments to `get_revision` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the Revision in the format: 'projects/{project_id}/locations/{location}/deployments/{deployment}/revisions/{revision}'. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::ConfigService::V1::Revision](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Revision)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::ConfigService::V1::Revision](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Revision)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/config_service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ConfigService::V1::Config::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ConfigService::V1::GetRevisionRequest.new
    
    # Call the get_revision method.
    result = client.get_revision request
    
    # The returned object is of type Google::Cloud::ConfigService::V1::Revision.
    p result

### #get_terraform_version
    
    
    def get_terraform_version(request, options = nil) -> ::Google::Cloud::ConfigService::V1::TerraformVersion
    def get_terraform_version(name: nil) -> ::Google::Cloud::ConfigService::V1::TerraformVersion

Gets details about a [TerraformVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-TerraformVersion "Google::Cloud::ConfigService::V1::TerraformVersion \(class\)").

**Overloads**
    
    
    def get_terraform_version(request, options = nil) -> ::Google::Cloud::ConfigService::V1::TerraformVersion

Pass arguments to `get_terraform_version` via a request object, either of type [GetTerraformVersionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-GetTerraformVersionRequest "Google::Cloud::ConfigService::V1::GetTerraformVersionRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ConfigService::V1::GetTerraformVersionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-GetTerraformVersionRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_terraform_version(name: nil) -> ::Google::Cloud::ConfigService::V1::TerraformVersion

Pass arguments to `get_terraform_version` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the TerraformVersion. Format: 'projects/{project_id}/locations/{location}/terraformVersions/{terraform_version}' 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::ConfigService::V1::TerraformVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-TerraformVersion)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::ConfigService::V1::TerraformVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-TerraformVersion)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/config_service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ConfigService::V1::Config::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ConfigService::V1::GetTerraformVersionRequest.new
    
    # Call the get_terraform_version method.
    result = client.get_terraform_version request
    
    # The returned object is of type Google::Cloud::ConfigService::V1::TerraformVersion.
    p result

### #iam_policy_client
    
    
    def iam_policy_client() -> Google::Iam::V1::IAMPolicy::Client

Get the associated client for mix-in of the IAMPolicy.

**Returns**

  * (Google::Iam::V1::IAMPolicy::Client) 



### #import_statefile
    
    
    def import_statefile(request, options = nil) -> ::Google::Cloud::ConfigService::V1::Statefile
    def import_statefile(parent: nil, lock_id: nil, skip_draft: nil) -> ::Google::Cloud::ConfigService::V1::Statefile

Imports Terraform state file in a given deployment. The state file does not take effect until the Deployment has been unlocked.

**Overloads**
    
    
    def import_statefile(request, options = nil) -> ::Google::Cloud::ConfigService::V1::Statefile

Pass arguments to `import_statefile` via a request object, either of type [ImportStatefileRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ImportStatefileRequest "Google::Cloud::ConfigService::V1::ImportStatefileRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ConfigService::V1::ImportStatefileRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ImportStatefileRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def import_statefile(parent: nil, lock_id: nil, skip_draft: nil) -> ::Google::Cloud::ConfigService::V1::Statefile

Pass arguments to `import_statefile` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent in whose context the statefile is listed. The parent value is in the format: 'projects/{project_id}/locations/{location}/deployments/{deployment}'. 
  * **lock_id** (::Integer) — Required. Lock ID of the lock file to verify that the user who is importing the state file previously locked the Deployment. 
  * **skip_draft** (::Boolean) — Optional. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::ConfigService::V1::Statefile](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Statefile)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::ConfigService::V1::Statefile](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Statefile)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/config_service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ConfigService::V1::Config::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ConfigService::V1::ImportStatefileRequest.new
    
    # Call the import_statefile method.
    result = client.import_statefile request
    
    # The returned object is of type Google::Cloud::ConfigService::V1::Statefile.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new Config client object.

**Yields**

  * (config) — Configure the Config client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Config-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Config-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::ConfigService::V1::Config::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::ConfigService::V1::Config::Client.new do |config|
      config.timeout = 10.0
    end

### #list_deployment_group_revisions
    
    
    def list_deployment_group_revisions(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ConfigService::V1::DeploymentGroupRevision>
    def list_deployment_group_revisions(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ConfigService::V1::DeploymentGroupRevision>

Lists {::Google::Cloud::ConfigService::V1::DeploymentGroupRevision DeploymentGroupRevision}s in a given [DeploymentGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-DeploymentGroup "Google::Cloud::ConfigService::V1::DeploymentGroup \(class\)").

**Overloads**
    
    
    def list_deployment_group_revisions(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ConfigService::V1::DeploymentGroupRevision>

Pass arguments to `list_deployment_group_revisions` via a request object, either of type [ListDeploymentGroupRevisionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ListDeploymentGroupRevisionsRequest "Google::Cloud::ConfigService::V1::ListDeploymentGroupRevisionsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ConfigService::V1::ListDeploymentGroupRevisionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ListDeploymentGroupRevisionsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_deployment_group_revisions(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ConfigService::V1::DeploymentGroupRevision>

Pass arguments to `list_deployment_group_revisions` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent, which owns this collection of deployment group revisions. Format: 'projects/{project_id}/locations/{location}/deploymentGroups/{deployment_group}'. 
  * **page_size** (::Integer) — Optional. When requesting a page of resources, 'page_size' specifies number of resources to return. If unspecified, a sensible default will be used by the server. The maximum value is 1000; values above 1000 will be coerced to 1000\. 
  * **page_token** (::String) — Optional. Token returned by previous call to 'ListDeploymentGroupRevisions' which specifies the position in the list from where to continue listing the deployment group revisions. All other parameters provided to `ListDeploymentGroupRevisions` must match the call that provided the page token. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::ConfigService::V1::DeploymentGroupRevision](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-DeploymentGroupRevision)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::ConfigService::V1::DeploymentGroupRevision](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-DeploymentGroupRevision)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/config_service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ConfigService::V1::Config::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ConfigService::V1::ListDeploymentGroupRevisionsRequest.new
    
    # Call the list_deployment_group_revisions method.
    result = client.list_deployment_group_revisions request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::ConfigService::V1::DeploymentGroupRevision.
      p item
    end

### #list_deployment_groups
    
    
    def list_deployment_groups(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ConfigService::V1::DeploymentGroup>
    def list_deployment_groups(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ConfigService::V1::DeploymentGroup>

List DeploymentGroups for a given project and location.

**Overloads**
    
    
    def list_deployment_groups(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ConfigService::V1::DeploymentGroup>

Pass arguments to `list_deployment_groups` via a request object, either of type [ListDeploymentGroupsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ListDeploymentGroupsRequest "Google::Cloud::ConfigService::V1::ListDeploymentGroupsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ConfigService::V1::ListDeploymentGroupsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ListDeploymentGroupsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_deployment_groups(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ConfigService::V1::DeploymentGroup>

Pass arguments to `list_deployment_groups` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent, which owns this collection of deployment groups. Format: 'projects/{project_id}/locations/{location}'. 
  * **page_size** (::Integer) — Optional. When requesting a page of resources, 'page_size' specifies number of resources to return. If unspecified, at most 500 will be returned. The maximum value is 1000. 
  * **page_token** (::String) — Optional. Token returned by previous call to 'ListDeploymentGroups' which specifies the position in the list from where to continue listing the deployment groups. 
  * **filter** (::String) — 

Optional. Lists the DeploymentGroups that match the filter expression. A filter expression filters the deployment groups listed in the response. The expression must be of the form '{field} {operator} {value}' where operators: '<', '>', '<=', '>=', '!=', '=', ':' are supported (colon ':' represents a HAS operator which is roughly synonymous with equality). {field} can refer to a proto or JSON field, or a synthetic field. Field names can be camelCase or snake_case.

Examples:

    * Filter by name: name = "projects/foo/locations/us-central1/deploymentGroups/bar"

    * Filter by labels:

      * Resources that have a key called 'foo' labels.foo:*
      * Resources that have a key called 'foo' whose value is 'bar' labels.foo = bar
    * Filter by state:

      * DeploymentGroups in CREATING state. state=CREATING
  * **order_by** (::String) — Optional. Field to use to sort the list. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::ConfigService::V1::DeploymentGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-DeploymentGroup)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::ConfigService::V1::DeploymentGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-DeploymentGroup)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/config_service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ConfigService::V1::Config::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ConfigService::V1::ListDeploymentGroupsRequest.new
    
    # Call the list_deployment_groups method.
    result = client.list_deployment_groups request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::ConfigService::V1::DeploymentGroup.
      p item
    end

### #list_deployments
    
    
    def list_deployments(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ConfigService::V1::Deployment>
    def list_deployments(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ConfigService::V1::Deployment>

Lists {::Google::Cloud::ConfigService::V1::Deployment Deployment}s in a given project and location.

**Overloads**
    
    
    def list_deployments(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ConfigService::V1::Deployment>

Pass arguments to `list_deployments` via a request object, either of type [ListDeploymentsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ListDeploymentsRequest "Google::Cloud::ConfigService::V1::ListDeploymentsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ConfigService::V1::ListDeploymentsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ListDeploymentsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_deployments(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ConfigService::V1::Deployment>

Pass arguments to `list_deployments` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent in whose context the Deployments are listed. The parent value is in the format: 'projects/{project_id}/locations/{location}'. 
  * **page_size** (::Integer) — When requesting a page of resources, 'page_size' specifies number of resources to return. If unspecified, at most 500 will be returned. The maximum value is 1000. 
  * **page_token** (::String) — Token returned by previous call to 'ListDeployments' which specifies the position in the list from where to continue listing the resources. 
  * **filter** (::String) — 

Lists the Deployments that match the filter expression. A filter expression filters the resources listed in the response. The expression must be of the form '{field} {operator} {value}' where operators: '<', '>', '<=', '>=', '!=', '=', ':' are supported (colon ':' represents a HAS operator which is roughly synonymous with equality). {field} can refer to a proto or JSON field, or a synthetic field. Field names can be camelCase or snake_case.

Examples:

    * Filter by name: name = "projects/foo/locations/us-central1/deployments/bar

    * Filter by labels:

      * Resources that have a key called 'foo' labels.foo:*
      * Resources that have a key called 'foo' whose value is 'bar' labels.foo = bar
    * Filter by state:

      * Deployments in CREATING state. state=CREATING
  * **order_by** (::String) — Field to use to sort the list. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::ConfigService::V1::Deployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Deployment)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::ConfigService::V1::Deployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Deployment)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/config_service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ConfigService::V1::Config::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ConfigService::V1::ListDeploymentsRequest.new
    
    # Call the list_deployments method.
    result = client.list_deployments request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::ConfigService::V1::Deployment.
      p item
    end

### #list_previews
    
    
    def list_previews(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ConfigService::V1::Preview>
    def list_previews(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ConfigService::V1::Preview>

Lists {::Google::Cloud::ConfigService::V1::Preview Preview}s in a given project and location.

**Overloads**
    
    
    def list_previews(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ConfigService::V1::Preview>

Pass arguments to `list_previews` via a request object, either of type [ListPreviewsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ListPreviewsRequest "Google::Cloud::ConfigService::V1::ListPreviewsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ConfigService::V1::ListPreviewsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ListPreviewsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_previews(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ConfigService::V1::Preview>

Pass arguments to `list_previews` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent in whose context the Previews are listed. The parent value is in the format: 'projects/{project_id}/locations/{location}'. 
  * **page_size** (::Integer) — Optional. When requesting a page of resources, 'page_size' specifies number of resources to return. If unspecified, at most 500 will be returned. The maximum value is 1000. 
  * **page_token** (::String) — Optional. Token returned by previous call to 'ListDeployments' which specifies the position in the list from where to continue listing the resources. 
  * **filter** (::String) — 

Optional. Lists the Deployments that match the filter expression. A filter expression filters the resources listed in the response. The expression must be of the form '{field} {operator} {value}' where operators: '<', '>', '<=', '>=', '!=', '=', ':' are supported (colon ':' represents a HAS operator which is roughly synonymous with equality). {field} can refer to a proto or JSON field, or a synthetic field. Field names can be camelCase or snake_case.

Examples:

    * Filter by name: name = "projects/foo/locations/us-central1/deployments/bar

    * Filter by labels:

      * Resources that have a key called 'foo' labels.foo:*
      * Resources that have a key called 'foo' whose value is 'bar' labels.foo = bar
    * Filter by state:

      * Deployments in CREATING state. state=CREATING
  * **order_by** (::String) — Optional. Field to use to sort the list. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::ConfigService::V1::Preview](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Preview)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::ConfigService::V1::Preview](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Preview)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/config_service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ConfigService::V1::Config::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ConfigService::V1::ListPreviewsRequest.new
    
    # Call the list_previews method.
    result = client.list_previews request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::ConfigService::V1::Preview.
      p item
    end

### #list_resource_changes
    
    
    def list_resource_changes(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ConfigService::V1::ResourceChange>
    def list_resource_changes(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ConfigService::V1::ResourceChange>

Lists ResourceChanges for a given preview.

**Overloads**
    
    
    def list_resource_changes(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ConfigService::V1::ResourceChange>

Pass arguments to `list_resource_changes` via a request object, either of type [ListResourceChangesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ListResourceChangesRequest "Google::Cloud::ConfigService::V1::ListResourceChangesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ConfigService::V1::ListResourceChangesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ListResourceChangesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_resource_changes(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ConfigService::V1::ResourceChange>

Pass arguments to `list_resource_changes` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent in whose context the ResourceChanges are listed. The parent value is in the format: 'projects/{project_id}/locations/{location}/previews/{preview}'. 
  * **page_size** (::Integer) — Optional. When requesting a page of resource changes, 'page_size' specifies number of resource changes to return. If unspecified, at most 500 will be returned. The maximum value is 1000. 
  * **page_token** (::String) — Optional. Token returned by previous call to 'ListResourceChanges' which specifies the position in the list from where to continue listing the resource changes. 
  * **filter** (::String) — 

Optional. Lists the resource changes that match the filter expression. A filter expression filters the resource changes listed in the response. The expression must be of the form '{field} {operator} {value}' where operators: '<', '>', '<=', '>=', '!=', '=', ':' are supported (colon ':' represents a HAS operator which is roughly synonymous with equality). {field} can refer to a proto or JSON field, or a synthetic field. Field names can be camelCase or snake_case.

Examples:

    * Filter by name: name = "projects/foo/locations/us-central1/previews/dep/resourceChanges/baz
  * **order_by** (::String) — Optional. Field to use to sort the list. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::ConfigService::V1::ResourceChange](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ResourceChange)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::ConfigService::V1::ResourceChange](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ResourceChange)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/config_service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ConfigService::V1::Config::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ConfigService::V1::ListResourceChangesRequest.new
    
    # Call the list_resource_changes method.
    result = client.list_resource_changes request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::ConfigService::V1::ResourceChange.
      p item
    end

### #list_resource_drifts
    
    
    def list_resource_drifts(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ConfigService::V1::ResourceDrift>
    def list_resource_drifts(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ConfigService::V1::ResourceDrift>

List ResourceDrifts for a given preview.

**Overloads**
    
    
    def list_resource_drifts(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ConfigService::V1::ResourceDrift>

Pass arguments to `list_resource_drifts` via a request object, either of type [ListResourceDriftsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ListResourceDriftsRequest "Google::Cloud::ConfigService::V1::ListResourceDriftsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ConfigService::V1::ListResourceDriftsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ListResourceDriftsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_resource_drifts(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ConfigService::V1::ResourceDrift>

Pass arguments to `list_resource_drifts` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent in whose context the ResourceDrifts are listed. The parent value is in the format: 'projects/{project_id}/locations/{location}/previews/{preview}'. 
  * **page_size** (::Integer) — Optional. When requesting a page of resource drifts, 'page_size' specifies number of resource drifts to return. If unspecified, at most 500 will be returned. The maximum value is 1000. 
  * **page_token** (::String) — Optional. Token returned by previous call to 'ListResourceDrifts' which specifies the position in the list from where to continue listing the resource drifts. 
  * **filter** (::String) — 

Optional. Lists the resource drifts that match the filter expression. A filter expression filters the resource drifts listed in the response. The expression must be of the form '{field} {operator} {value}' where operators: '<', '>', '<=', '>=', '!=', '=', ':' are supported (colon ':' represents a HAS operator which is roughly synonymous with equality). {field} can refer to a proto or JSON field, or a synthetic field. Field names can be camelCase or snake_case.

Examples:

    * Filter by name: name = "projects/foo/locations/us-central1/previews/dep/resourceDrifts/baz
  * **order_by** (::String) — Optional. Field to use to sort the list. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::ConfigService::V1::ResourceDrift](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ResourceDrift)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::ConfigService::V1::ResourceDrift](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ResourceDrift)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/config_service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ConfigService::V1::Config::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ConfigService::V1::ListResourceDriftsRequest.new
    
    # Call the list_resource_drifts method.
    result = client.list_resource_drifts request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::ConfigService::V1::ResourceDrift.
      p item
    end

### #list_resources
    
    
    def list_resources(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ConfigService::V1::Resource>
    def list_resources(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ConfigService::V1::Resource>

Lists [Resources](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Resource "Google::Cloud::ConfigService::V1::Resource \(class\)") in a given revision.

**Overloads**
    
    
    def list_resources(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ConfigService::V1::Resource>

Pass arguments to `list_resources` via a request object, either of type [ListResourcesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ListResourcesRequest "Google::Cloud::ConfigService::V1::ListResourcesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ConfigService::V1::ListResourcesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ListResourcesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_resources(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ConfigService::V1::Resource>

Pass arguments to `list_resources` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent in whose context the Resources are listed. The parent value is in the format: 'projects/{project_id}/locations/{location}/deployments/{deployment}/revisions/{revision}'. 
  * **page_size** (::Integer) — When requesting a page of resources, 'page_size' specifies number of resources to return. If unspecified, at most 500 will be returned. The maximum value is 1000. 
  * **page_token** (::String) — Token returned by previous call to 'ListResources' which specifies the position in the list from where to continue listing the resources. 
  * **filter** (::String) — 

Lists the Resources that match the filter expression. A filter expression filters the resources listed in the response. The expression must be of the form '{field} {operator} {value}' where operators: '<', '>', '<=', '>=', '!=', '=', ':' are supported (colon ':' represents a HAS operator which is roughly synonymous with equality). {field} can refer to a proto or JSON field, or a synthetic field. Field names can be camelCase or snake_case.

Examples:

    * Filter by name: name = "projects/foo/locations/us-central1/deployments/dep/revisions/bar/resources/baz
  * **order_by** (::String) — Field to use to sort the list. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::ConfigService::V1::Resource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Resource)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::ConfigService::V1::Resource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Resource)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/config_service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ConfigService::V1::Config::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ConfigService::V1::ListResourcesRequest.new
    
    # Call the list_resources method.
    result = client.list_resources request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::ConfigService::V1::Resource.
      p item
    end

### #list_revisions
    
    
    def list_revisions(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ConfigService::V1::Revision>
    def list_revisions(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ConfigService::V1::Revision>

Lists {::Google::Cloud::ConfigService::V1::Revision Revision}s of a deployment.

**Overloads**
    
    
    def list_revisions(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ConfigService::V1::Revision>

Pass arguments to `list_revisions` via a request object, either of type [ListRevisionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ListRevisionsRequest "Google::Cloud::ConfigService::V1::ListRevisionsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ConfigService::V1::ListRevisionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ListRevisionsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_revisions(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ConfigService::V1::Revision>

Pass arguments to `list_revisions` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent in whose context the Revisions are listed. The parent value is in the format: 'projects/{project_id}/locations/{location}/deployments/{deployment}'. 
  * **page_size** (::Integer) — When requesting a page of resources, `page_size` specifies number of resources to return. If unspecified, at most 500 will be returned. The maximum value is 1000. 
  * **page_token** (::String) — Token returned by previous call to 'ListRevisions' which specifies the position in the list from where to continue listing the resources. 
  * **filter** (::String) — 

Lists the Revisions that match the filter expression. A filter expression filters the resources listed in the response. The expression must be of the form '{field} {operator} {value}' where operators: '<', '>', '<=', '>=', '!=', '=', ':' are supported (colon ':' represents a HAS operator which is roughly synonymous with equality). {field} can refer to a proto or JSON field, or a synthetic field. Field names can be camelCase or snake_case.

Examples:

    * Filter by name: name = "projects/foo/locations/us-central1/deployments/dep/revisions/bar

    * Filter by labels:

      * Resources that have a key called 'foo' labels.foo:*
      * Resources that have a key called 'foo' whose value is 'bar' labels.foo = bar
    * Filter by state:

      * Revisions in CREATING state. state=CREATING
  * **order_by** (::String) — Field to use to sort the list. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::ConfigService::V1::Revision](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Revision)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::ConfigService::V1::Revision](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Revision)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/config_service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ConfigService::V1::Config::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ConfigService::V1::ListRevisionsRequest.new
    
    # Call the list_revisions method.
    result = client.list_revisions request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::ConfigService::V1::Revision.
      p item
    end

### #list_terraform_versions
    
    
    def list_terraform_versions(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ConfigService::V1::TerraformVersion>
    def list_terraform_versions(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ConfigService::V1::TerraformVersion>

Lists {::Google::Cloud::ConfigService::V1::TerraformVersion TerraformVersion}s in a given project and location.

**Overloads**
    
    
    def list_terraform_versions(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ConfigService::V1::TerraformVersion>

Pass arguments to `list_terraform_versions` via a request object, either of type [ListTerraformVersionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ListTerraformVersionsRequest "Google::Cloud::ConfigService::V1::ListTerraformVersionsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ConfigService::V1::ListTerraformVersionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ListTerraformVersionsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_terraform_versions(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ConfigService::V1::TerraformVersion>

Pass arguments to `list_terraform_versions` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent in whose context the TerraformVersions are listed. The parent value is in the format: 'projects/{project_id}/locations/{location}'. 
  * **page_size** (::Integer) — Optional. When requesting a page of terraform versions, 'page_size' specifies number of terraform versions to return. If unspecified, at most 500 will be returned. The maximum value is 1000. 
  * **page_token** (::String) — Optional. Token returned by previous call to 'ListTerraformVersions' which specifies the position in the list from where to continue listing the terraform versions. 
  * **filter** (::String) — Optional. Lists the TerraformVersions that match the filter expression. A filter expression filters the resources listed in the response. The expression must be of the form '{field} {operator} {value}' where operators: '<', '>', '<=', '>=', '!=', '=', ':' are supported (colon ':' represents a HAS operator which is roughly synonymous with equality). {field} can refer to a proto or JSON field, or a synthetic field. Field names can be camelCase or snake_case. 
  * **order_by** (::String) — Optional. Field to use to sort the list. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::ConfigService::V1::TerraformVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-TerraformVersion)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::ConfigService::V1::TerraformVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-TerraformVersion)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/config_service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ConfigService::V1::Config::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ConfigService::V1::ListTerraformVersionsRequest.new
    
    # Call the list_terraform_versions method.
    result = client.list_terraform_versions request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::ConfigService::V1::TerraformVersion.
      p item
    end

### #location_client
    
    
    def location_client() -> Google::Cloud::Location::Locations::Client

Get the associated client for mix-in of the Locations.

**Returns**

  * (Google::Cloud::Location::Locations::Client) 



### #lock_deployment
    
    
    def lock_deployment(request, options = nil) -> ::Gapic::Operation
    def lock_deployment(name: nil) -> ::Gapic::Operation

Locks a deployment.

**Overloads**
    
    
    def lock_deployment(request, options = nil) -> ::Gapic::Operation

Pass arguments to `lock_deployment` via a request object, either of type [LockDeploymentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-LockDeploymentRequest "Google::Cloud::ConfigService::V1::LockDeploymentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ConfigService::V1::LockDeploymentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-LockDeploymentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def lock_deployment(name: nil) -> ::Gapic::Operation

Pass arguments to `lock_deployment` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the deployment in the format: 'projects/{project_id}/locations/{location}/deployments/{deployment}'. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/config_service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ConfigService::V1::Config::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ConfigService::V1::LockDeploymentRequest.new
    
    # Call the lock_deployment method.
    result = client.lock_deployment request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #logger
    
    
    def logger() -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #operations_client
    
    
    def operations_client() -> ::Google::Cloud::ConfigService::V1::Config::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::ConfigService::V1::Config::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Config-Operations)) 



### #provision_deployment_group
    
    
    def provision_deployment_group(request, options = nil) -> ::Gapic::Operation
    def provision_deployment_group(name: nil, deployment_specs: nil) -> ::Gapic::Operation

Provisions a deployment group.

NOTE: As a first step of this operation, Infra Manager will automatically delete any Deployments that were part of the _last successful_ [DeploymentGroupRevision](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-DeploymentGroupRevision "Google::Cloud::ConfigService::V1::DeploymentGroupRevision \(class\)") but are _no longer_ included in the _current_ [DeploymentGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-DeploymentGroup "Google::Cloud::ConfigService::V1::DeploymentGroup \(class\)") definition (e.g., following an `UpdateDeploymentGroup` call), along with their actuated resources.

**Overloads**
    
    
    def provision_deployment_group(request, options = nil) -> ::Gapic::Operation

Pass arguments to `provision_deployment_group` via a request object, either of type [ProvisionDeploymentGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ProvisionDeploymentGroupRequest "Google::Cloud::ConfigService::V1::ProvisionDeploymentGroupRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ConfigService::V1::ProvisionDeploymentGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-ProvisionDeploymentGroupRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def provision_deployment_group(name: nil, deployment_specs: nil) -> ::Gapic::Operation

Pass arguments to `provision_deployment_group` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the deployment group to provision. Format: 'projects/{project_id}/locations/{location}/deploymentGroups/{deployment_group}'. 
  * **deployment_specs** (::Hash{::String => ::Google::Cloud::ConfigService::V1::DeploymentSpec, ::Hash}) — Optional. The deployment specs of the deployment units to be created within the same project and location of the deployment group. The key is the unit ID, and the value is the `DeploymentSpec`. Provisioning will fail if a `deployment_spec` has a `deployment_id` that matches an existing deployment in the same project and location. If an existing deployment was part of the last successful revision but is no longer in the current DeploymentGroup's `deployment_units`, it will be recreated if included in `deployment_specs`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/config_service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ConfigService::V1::Config::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ConfigService::V1::ProvisionDeploymentGroupRequest.new
    
    # Call the provision_deployment_group method.
    result = client.provision_deployment_group request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #unlock_deployment
    
    
    def unlock_deployment(request, options = nil) -> ::Gapic::Operation
    def unlock_deployment(name: nil, lock_id: nil) -> ::Gapic::Operation

Unlocks a locked deployment.

**Overloads**
    
    
    def unlock_deployment(request, options = nil) -> ::Gapic::Operation

Pass arguments to `unlock_deployment` via a request object, either of type [UnlockDeploymentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-UnlockDeploymentRequest "Google::Cloud::ConfigService::V1::UnlockDeploymentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ConfigService::V1::UnlockDeploymentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-UnlockDeploymentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def unlock_deployment(name: nil, lock_id: nil) -> ::Gapic::Operation

Pass arguments to `unlock_deployment` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the deployment in the format: 'projects/{project_id}/locations/{location}/deployments/{deployment}'. 
  * **lock_id** (::Integer) — Required. Lock ID of the lock file to be unlocked. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/config_service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ConfigService::V1::Config::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ConfigService::V1::UnlockDeploymentRequest.new
    
    # Call the unlock_deployment method.
    result = client.unlock_deployment request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #update_auto_migration_config
    
    
    def update_auto_migration_config(request, options = nil) -> ::Gapic::Operation
    def update_auto_migration_config(update_mask: nil, auto_migration_config: nil) -> ::Gapic::Operation

Updates the AutoMigrationConfig for a given project and location.

**Overloads**
    
    
    def update_auto_migration_config(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_auto_migration_config` via a request object, either of type [UpdateAutoMigrationConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-UpdateAutoMigrationConfigRequest "Google::Cloud::ConfigService::V1::UpdateAutoMigrationConfigRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ConfigService::V1::UpdateAutoMigrationConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-UpdateAutoMigrationConfigRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_auto_migration_config(update_mask: nil, auto_migration_config: nil) -> ::Gapic::Operation

Pass arguments to `update_auto_migration_config` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. The update mask applies to the resource. See [google.protobuf.FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Protobuf-FieldMask "Google::Protobuf::FieldMask \(class\)"). 
  * **auto_migration_config** ([::Google::Cloud::ConfigService::V1::AutoMigrationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-AutoMigrationConfig), ::Hash) — Required. The AutoMigrationConfig to update. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/config_service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ConfigService::V1::Config::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ConfigService::V1::UpdateAutoMigrationConfigRequest.new
    
    # Call the update_auto_migration_config method.
    result = client.update_auto_migration_config request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #update_deployment
    
    
    def update_deployment(request, options = nil) -> ::Gapic::Operation
    def update_deployment(update_mask: nil, deployment: nil, request_id: nil) -> ::Gapic::Operation

Updates a [Deployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Deployment "Google::Cloud::ConfigService::V1::Deployment \(class\)").

**Overloads**
    
    
    def update_deployment(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_deployment` via a request object, either of type [UpdateDeploymentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-UpdateDeploymentRequest "Google::Cloud::ConfigService::V1::UpdateDeploymentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ConfigService::V1::UpdateDeploymentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-UpdateDeploymentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_deployment(update_mask: nil, deployment: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `update_deployment` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. Field mask used to specify the fields to be overwritten in the Deployment resource by the update.

The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. 

  * **deployment** ([::Google::Cloud::ConfigService::V1::Deployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Deployment), ::Hash) — Required. [Deployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-Deployment "Google::Cloud::ConfigService::V1::Deployment \(class\)") to update.

The deployment's `name` field is used to identify the resource to be updated. Format: `projects/{project}/locations/{location}/deployments/{deployment}`

  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/config_service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ConfigService::V1::Config::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ConfigService::V1::UpdateDeploymentRequest.new
    
    # Call the update_deployment method.
    result = client.update_deployment request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #update_deployment_group
    
    
    def update_deployment_group(request, options = nil) -> ::Gapic::Operation
    def update_deployment_group(update_mask: nil, deployment_group: nil, request_id: nil) -> ::Gapic::Operation

Updates a [DeploymentGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-DeploymentGroup "Google::Cloud::ConfigService::V1::DeploymentGroup \(class\)")

**Overloads**
    
    
    def update_deployment_group(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_deployment_group` via a request object, either of type [UpdateDeploymentGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-UpdateDeploymentGroupRequest "Google::Cloud::ConfigService::V1::UpdateDeploymentGroupRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ConfigService::V1::UpdateDeploymentGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-UpdateDeploymentGroupRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_deployment_group(update_mask: nil, deployment_group: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `update_deployment_group` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. Field mask used to specify the fields to be overwritten in the Deployment Group resource by the update.

The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. 

  * **deployment_group** ([::Google::Cloud::ConfigService::V1::DeploymentGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-DeploymentGroup), ::Hash) — Required. [DeploymentGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_service-v1/latest/Google-Cloud-ConfigService-V1-DeploymentGroup "Google::Cloud::ConfigService::V1::DeploymentGroup \(class\)") to update.

The deployment group's `name` field is used to identify the resource to be updated. Format: `projects/{project}/locations/{location}/deploymentGroups/{deployment_group_id}`

  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/config_service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ConfigService::V1::Config::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ConfigService::V1::UpdateDeploymentGroupRequest.new
    
    # Call the update_deployment_group method.
    result = client.update_deployment_group request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
