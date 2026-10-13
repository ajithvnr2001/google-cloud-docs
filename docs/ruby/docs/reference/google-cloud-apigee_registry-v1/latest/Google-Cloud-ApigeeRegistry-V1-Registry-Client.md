---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Registry-Client/
title: Apigee Registry V1 API - Class Google::Cloud::ApigeeRegistry::V1::Registry::Client (v0.16.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:24:19.629993+00:00
---

# Apigee Registry V1 API - Class Google::Cloud::ApigeeRegistry::V1::Registry::Client (v0.16.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Registry-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Apigee Registry V1 API - Class Google::Cloud::ApigeeRegistry::V1::Registry::Client (v0.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.17.0 (latest)  0.16.0  0.15.0  0.14.0  0.13.1  0.12.0  0.11.0  0.10.1  0.9.0  0.8.1  0.7.2  0.6.0  0.5.0  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Apigee Registry V1 API class Google::Cloud::ApigeeRegistry::V1::Registry::Client.

Client for the Registry service.

The Registry service allows teams to manage descriptions of APIs.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::ApigeeRegistry::V1::Registry::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Registry-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the Registry Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Registry-Client-Configuration "Google::Cloud::ApigeeRegistry::V1::Registry::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Registry-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Registry-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all Registry clients
    ::Google::Cloud::ApigeeRegistry::V1::Registry::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the Registry Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Registry-Client#Google__Cloud__ApigeeRegistry__V1__Registry__Client_configure_class_ "Google::Cloud::ApigeeRegistry::V1::Registry::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Registry-Client-Configuration "Google::Cloud::ApigeeRegistry::V1::Registry::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Registry-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Registry-Client-Configuration)) 



### #create_api
    
    
    def create_api(request, options = nil) -> ::Google::Cloud::ApigeeRegistry::V1::Api
    def create_api(parent: nil, api: nil, api_id: nil) -> ::Google::Cloud::ApigeeRegistry::V1::Api

Creates a specified API.

**Overloads**
    
    
    def create_api(request, options = nil) -> ::Google::Cloud::ApigeeRegistry::V1::Api

Pass arguments to `create_api` via a request object, either of type [CreateApiRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-CreateApiRequest "Google::Cloud::ApigeeRegistry::V1::CreateApiRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApigeeRegistry::V1::CreateApiRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-CreateApiRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_api(parent: nil, api: nil, api_id: nil) -> ::Google::Cloud::ApigeeRegistry::V1::Api

Pass arguments to `create_api` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent, which owns this collection of APIs. Format: `projects/*/locations/*`
  * **api** ([::Google::Cloud::ApigeeRegistry::V1::Api](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Api), ::Hash) — Required. The API to create. 
  * **api_id** (::String) — Required. The ID to use for the API, which will become the final component of the API's resource name.

This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/.

Following AIP-162, IDs must not have the form of a UUID. 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::ApigeeRegistry::V1::Api](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Api)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::ApigeeRegistry::V1::Api](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Api)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/apigee_registry/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApigeeRegistry::V1::Registry::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApigeeRegistry::V1::CreateApiRequest.new
    
    # Call the create_api method.
    result = client.create_api request
    
    # The returned object is of type Google::Cloud::ApigeeRegistry::V1::Api.
    p result

### #create_api_deployment
    
    
    def create_api_deployment(request, options = nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiDeployment
    def create_api_deployment(parent: nil, api_deployment: nil, api_deployment_id: nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiDeployment

Creates a specified deployment.

**Overloads**
    
    
    def create_api_deployment(request, options = nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiDeployment

Pass arguments to `create_api_deployment` via a request object, either of type [CreateApiDeploymentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-CreateApiDeploymentRequest "Google::Cloud::ApigeeRegistry::V1::CreateApiDeploymentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApigeeRegistry::V1::CreateApiDeploymentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-CreateApiDeploymentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_api_deployment(parent: nil, api_deployment: nil, api_deployment_id: nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiDeployment

Pass arguments to `create_api_deployment` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent, which owns this collection of deployments. Format: `projects/*/locations/*/apis/*`
  * **api_deployment** ([::Google::Cloud::ApigeeRegistry::V1::ApiDeployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ApiDeployment), ::Hash) — Required. The deployment to create. 
  * **api_deployment_id** (::String) — Required. The ID to use for the deployment, which will become the final component of the deployment's resource name.

This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/.

Following AIP-162, IDs must not have the form of a UUID. 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::ApigeeRegistry::V1::ApiDeployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ApiDeployment)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::ApigeeRegistry::V1::ApiDeployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ApiDeployment)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/apigee_registry/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApigeeRegistry::V1::Registry::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApigeeRegistry::V1::CreateApiDeploymentRequest.new
    
    # Call the create_api_deployment method.
    result = client.create_api_deployment request
    
    # The returned object is of type Google::Cloud::ApigeeRegistry::V1::ApiDeployment.
    p result

### #create_api_spec
    
    
    def create_api_spec(request, options = nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiSpec
    def create_api_spec(parent: nil, api_spec: nil, api_spec_id: nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiSpec

Creates a specified spec.

**Overloads**
    
    
    def create_api_spec(request, options = nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiSpec

Pass arguments to `create_api_spec` via a request object, either of type [CreateApiSpecRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-CreateApiSpecRequest "Google::Cloud::ApigeeRegistry::V1::CreateApiSpecRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApigeeRegistry::V1::CreateApiSpecRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-CreateApiSpecRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_api_spec(parent: nil, api_spec: nil, api_spec_id: nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiSpec

Pass arguments to `create_api_spec` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent, which owns this collection of specs. Format: `projects/*/locations/*/apis/*/versions/*`
  * **api_spec** ([::Google::Cloud::ApigeeRegistry::V1::ApiSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ApiSpec), ::Hash) — Required. The spec to create. 
  * **api_spec_id** (::String) — Required. The ID to use for the spec, which will become the final component of the spec's resource name.

This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/.

Following AIP-162, IDs must not have the form of a UUID. 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::ApigeeRegistry::V1::ApiSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ApiSpec)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::ApigeeRegistry::V1::ApiSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ApiSpec)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/apigee_registry/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApigeeRegistry::V1::Registry::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApigeeRegistry::V1::CreateApiSpecRequest.new
    
    # Call the create_api_spec method.
    result = client.create_api_spec request
    
    # The returned object is of type Google::Cloud::ApigeeRegistry::V1::ApiSpec.
    p result

### #create_api_version
    
    
    def create_api_version(request, options = nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiVersion
    def create_api_version(parent: nil, api_version: nil, api_version_id: nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiVersion

Creates a specified version.

**Overloads**
    
    
    def create_api_version(request, options = nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiVersion

Pass arguments to `create_api_version` via a request object, either of type [CreateApiVersionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-CreateApiVersionRequest "Google::Cloud::ApigeeRegistry::V1::CreateApiVersionRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApigeeRegistry::V1::CreateApiVersionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-CreateApiVersionRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_api_version(parent: nil, api_version: nil, api_version_id: nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiVersion

Pass arguments to `create_api_version` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent, which owns this collection of versions. Format: `projects/*/locations/*/apis/*`
  * **api_version** ([::Google::Cloud::ApigeeRegistry::V1::ApiVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ApiVersion), ::Hash) — Required. The version to create. 
  * **api_version_id** (::String) — Required. The ID to use for the version, which will become the final component of the version's resource name.

This value should be 1-63 characters, and valid characters are /[a-z][0-9]-/.

Following AIP-162, IDs must not have the form of a UUID. 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::ApigeeRegistry::V1::ApiVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ApiVersion)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::ApigeeRegistry::V1::ApiVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ApiVersion)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/apigee_registry/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApigeeRegistry::V1::Registry::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApigeeRegistry::V1::CreateApiVersionRequest.new
    
    # Call the create_api_version method.
    result = client.create_api_version request
    
    # The returned object is of type Google::Cloud::ApigeeRegistry::V1::ApiVersion.
    p result

### #create_artifact
    
    
    def create_artifact(request, options = nil) -> ::Google::Cloud::ApigeeRegistry::V1::Artifact
    def create_artifact(parent: nil, artifact: nil, artifact_id: nil) -> ::Google::Cloud::ApigeeRegistry::V1::Artifact

Creates a specified artifact.

**Overloads**
    
    
    def create_artifact(request, options = nil) -> ::Google::Cloud::ApigeeRegistry::V1::Artifact

Pass arguments to `create_artifact` via a request object, either of type [CreateArtifactRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-CreateArtifactRequest "Google::Cloud::ApigeeRegistry::V1::CreateArtifactRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApigeeRegistry::V1::CreateArtifactRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-CreateArtifactRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_artifact(parent: nil, artifact: nil, artifact_id: nil) -> ::Google::Cloud::ApigeeRegistry::V1::Artifact

Pass arguments to `create_artifact` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent, which owns this collection of artifacts. Format: `{parent}`
  * **artifact** ([::Google::Cloud::ApigeeRegistry::V1::Artifact](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Artifact), ::Hash) — Required. The artifact to create. 
  * **artifact_id** (::String) — Required. The ID to use for the artifact, which will become the final component of the artifact's resource name.

This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/.

Following AIP-162, IDs must not have the form of a UUID. 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::ApigeeRegistry::V1::Artifact](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Artifact)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::ApigeeRegistry::V1::Artifact](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Artifact)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/apigee_registry/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApigeeRegistry::V1::Registry::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApigeeRegistry::V1::CreateArtifactRequest.new
    
    # Call the create_artifact method.
    result = client.create_artifact request
    
    # The returned object is of type Google::Cloud::ApigeeRegistry::V1::Artifact.
    p result

### #delete_api
    
    
    def delete_api(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_api(name: nil, force: nil) -> ::Google::Protobuf::Empty

Removes a specified API and all of the resources that it owns.

**Overloads**
    
    
    def delete_api(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_api` via a request object, either of type [DeleteApiRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-DeleteApiRequest "Google::Cloud::ApigeeRegistry::V1::DeleteApiRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApigeeRegistry::V1::DeleteApiRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-DeleteApiRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_api(name: nil, force: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_api` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the API to delete. Format: `projects/*/locations/*/apis/*`
  * **force** (::Boolean) — If set to true, any child resources will also be deleted. (Otherwise, the request will only work if there are no child resources.) 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/apigee_registry/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApigeeRegistry::V1::Registry::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApigeeRegistry::V1::DeleteApiRequest.new
    
    # Call the delete_api method.
    result = client.delete_api request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #delete_api_deployment
    
    
    def delete_api_deployment(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_api_deployment(name: nil, force: nil) -> ::Google::Protobuf::Empty

Removes a specified deployment, all revisions, and all child resources (e.g., artifacts).

**Overloads**
    
    
    def delete_api_deployment(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_api_deployment` via a request object, either of type [DeleteApiDeploymentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-DeleteApiDeploymentRequest "Google::Cloud::ApigeeRegistry::V1::DeleteApiDeploymentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApigeeRegistry::V1::DeleteApiDeploymentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-DeleteApiDeploymentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_api_deployment(name: nil, force: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_api_deployment` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the deployment to delete. Format: `projects/*/locations/*/apis/*/deployments/*`
  * **force** (::Boolean) — If set to true, any child resources will also be deleted. (Otherwise, the request will only work if there are no child resources.) 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/apigee_registry/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApigeeRegistry::V1::Registry::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApigeeRegistry::V1::DeleteApiDeploymentRequest.new
    
    # Call the delete_api_deployment method.
    result = client.delete_api_deployment request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #delete_api_deployment_revision
    
    
    def delete_api_deployment_revision(request, options = nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiDeployment
    def delete_api_deployment_revision(name: nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiDeployment

Deletes a revision of a deployment.

**Overloads**
    
    
    def delete_api_deployment_revision(request, options = nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiDeployment

Pass arguments to `delete_api_deployment_revision` via a request object, either of type [DeleteApiDeploymentRevisionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-DeleteApiDeploymentRevisionRequest "Google::Cloud::ApigeeRegistry::V1::DeleteApiDeploymentRevisionRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApigeeRegistry::V1::DeleteApiDeploymentRevisionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-DeleteApiDeploymentRevisionRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_api_deployment_revision(name: nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiDeployment

Pass arguments to `delete_api_deployment_revision` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the deployment revision to be deleted, with a revision ID explicitly included.

Example: `projects/sample/locations/global/apis/petstore/deployments/prod@c7cfa2a8`




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::ApigeeRegistry::V1::ApiDeployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ApiDeployment)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::ApigeeRegistry::V1::ApiDeployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ApiDeployment)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/apigee_registry/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApigeeRegistry::V1::Registry::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApigeeRegistry::V1::DeleteApiDeploymentRevisionRequest.new
    
    # Call the delete_api_deployment_revision method.
    result = client.delete_api_deployment_revision request
    
    # The returned object is of type Google::Cloud::ApigeeRegistry::V1::ApiDeployment.
    p result

### #delete_api_spec
    
    
    def delete_api_spec(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_api_spec(name: nil, force: nil) -> ::Google::Protobuf::Empty

Removes a specified spec, all revisions, and all child resources (e.g., artifacts).

**Overloads**
    
    
    def delete_api_spec(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_api_spec` via a request object, either of type [DeleteApiSpecRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-DeleteApiSpecRequest "Google::Cloud::ApigeeRegistry::V1::DeleteApiSpecRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApigeeRegistry::V1::DeleteApiSpecRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-DeleteApiSpecRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_api_spec(name: nil, force: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_api_spec` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the spec to delete. Format: `projects/*/locations/*/apis/*/versions/*/specs/*`
  * **force** (::Boolean) — If set to true, any child resources will also be deleted. (Otherwise, the request will only work if there are no child resources.) 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/apigee_registry/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApigeeRegistry::V1::Registry::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApigeeRegistry::V1::DeleteApiSpecRequest.new
    
    # Call the delete_api_spec method.
    result = client.delete_api_spec request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #delete_api_spec_revision
    
    
    def delete_api_spec_revision(request, options = nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiSpec
    def delete_api_spec_revision(name: nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiSpec

Deletes a revision of a spec.

**Overloads**
    
    
    def delete_api_spec_revision(request, options = nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiSpec

Pass arguments to `delete_api_spec_revision` via a request object, either of type [DeleteApiSpecRevisionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-DeleteApiSpecRevisionRequest "Google::Cloud::ApigeeRegistry::V1::DeleteApiSpecRevisionRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApigeeRegistry::V1::DeleteApiSpecRevisionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-DeleteApiSpecRevisionRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_api_spec_revision(name: nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiSpec

Pass arguments to `delete_api_spec_revision` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the spec revision to be deleted, with a revision ID explicitly included.

Example: `projects/sample/locations/global/apis/petstore/versions/1.0.0/specs/openapi.yaml@c7cfa2a8`




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::ApigeeRegistry::V1::ApiSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ApiSpec)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::ApigeeRegistry::V1::ApiSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ApiSpec)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/apigee_registry/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApigeeRegistry::V1::Registry::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApigeeRegistry::V1::DeleteApiSpecRevisionRequest.new
    
    # Call the delete_api_spec_revision method.
    result = client.delete_api_spec_revision request
    
    # The returned object is of type Google::Cloud::ApigeeRegistry::V1::ApiSpec.
    p result

### #delete_api_version
    
    
    def delete_api_version(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_api_version(name: nil, force: nil) -> ::Google::Protobuf::Empty

Removes a specified version and all of the resources that it owns.

**Overloads**
    
    
    def delete_api_version(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_api_version` via a request object, either of type [DeleteApiVersionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-DeleteApiVersionRequest "Google::Cloud::ApigeeRegistry::V1::DeleteApiVersionRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApigeeRegistry::V1::DeleteApiVersionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-DeleteApiVersionRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_api_version(name: nil, force: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_api_version` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the version to delete. Format: `projects/*/locations/*/apis/*/versions/*`
  * **force** (::Boolean) — If set to true, any child resources will also be deleted. (Otherwise, the request will only work if there are no child resources.) 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/apigee_registry/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApigeeRegistry::V1::Registry::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApigeeRegistry::V1::DeleteApiVersionRequest.new
    
    # Call the delete_api_version method.
    result = client.delete_api_version request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #delete_artifact
    
    
    def delete_artifact(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_artifact(name: nil) -> ::Google::Protobuf::Empty

Removes a specified artifact.

**Overloads**
    
    
    def delete_artifact(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_artifact` via a request object, either of type [DeleteArtifactRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-DeleteArtifactRequest "Google::Cloud::ApigeeRegistry::V1::DeleteArtifactRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApigeeRegistry::V1::DeleteArtifactRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-DeleteArtifactRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_artifact(name: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_artifact` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the artifact to delete. Format: `{parent}/artifacts/*`



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/apigee_registry/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApigeeRegistry::V1::Registry::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApigeeRegistry::V1::DeleteArtifactRequest.new
    
    # Call the delete_artifact method.
    result = client.delete_artifact request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #get_api
    
    
    def get_api(request, options = nil) -> ::Google::Cloud::ApigeeRegistry::V1::Api
    def get_api(name: nil) -> ::Google::Cloud::ApigeeRegistry::V1::Api

Returns a specified API.

**Overloads**
    
    
    def get_api(request, options = nil) -> ::Google::Cloud::ApigeeRegistry::V1::Api

Pass arguments to `get_api` via a request object, either of type [GetApiRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-GetApiRequest "Google::Cloud::ApigeeRegistry::V1::GetApiRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApigeeRegistry::V1::GetApiRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-GetApiRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_api(name: nil) -> ::Google::Cloud::ApigeeRegistry::V1::Api

Pass arguments to `get_api` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the API to retrieve. Format: `projects/*/locations/*/apis/*`



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::ApigeeRegistry::V1::Api](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Api)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::ApigeeRegistry::V1::Api](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Api)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/apigee_registry/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApigeeRegistry::V1::Registry::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApigeeRegistry::V1::GetApiRequest.new
    
    # Call the get_api method.
    result = client.get_api request
    
    # The returned object is of type Google::Cloud::ApigeeRegistry::V1::Api.
    p result

### #get_api_deployment
    
    
    def get_api_deployment(request, options = nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiDeployment
    def get_api_deployment(name: nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiDeployment

Returns a specified deployment.

**Overloads**
    
    
    def get_api_deployment(request, options = nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiDeployment

Pass arguments to `get_api_deployment` via a request object, either of type [GetApiDeploymentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-GetApiDeploymentRequest "Google::Cloud::ApigeeRegistry::V1::GetApiDeploymentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApigeeRegistry::V1::GetApiDeploymentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-GetApiDeploymentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_api_deployment(name: nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiDeployment

Pass arguments to `get_api_deployment` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the deployment to retrieve. Format: `projects/*/locations/*/apis/*/deployments/*`



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::ApigeeRegistry::V1::ApiDeployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ApiDeployment)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::ApigeeRegistry::V1::ApiDeployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ApiDeployment)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/apigee_registry/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApigeeRegistry::V1::Registry::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApigeeRegistry::V1::GetApiDeploymentRequest.new
    
    # Call the get_api_deployment method.
    result = client.get_api_deployment request
    
    # The returned object is of type Google::Cloud::ApigeeRegistry::V1::ApiDeployment.
    p result

### #get_api_spec
    
    
    def get_api_spec(request, options = nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiSpec
    def get_api_spec(name: nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiSpec

Returns a specified spec.

**Overloads**
    
    
    def get_api_spec(request, options = nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiSpec

Pass arguments to `get_api_spec` via a request object, either of type [GetApiSpecRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-GetApiSpecRequest "Google::Cloud::ApigeeRegistry::V1::GetApiSpecRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApigeeRegistry::V1::GetApiSpecRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-GetApiSpecRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_api_spec(name: nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiSpec

Pass arguments to `get_api_spec` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the spec to retrieve. Format: `projects/*/locations/*/apis/*/versions/*/specs/*`



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::ApigeeRegistry::V1::ApiSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ApiSpec)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::ApigeeRegistry::V1::ApiSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ApiSpec)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/apigee_registry/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApigeeRegistry::V1::Registry::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApigeeRegistry::V1::GetApiSpecRequest.new
    
    # Call the get_api_spec method.
    result = client.get_api_spec request
    
    # The returned object is of type Google::Cloud::ApigeeRegistry::V1::ApiSpec.
    p result

### #get_api_spec_contents
    
    
    def get_api_spec_contents(request, options = nil) -> ::Google::Api::HttpBody
    def get_api_spec_contents(name: nil) -> ::Google::Api::HttpBody

Returns the contents of a specified spec. If specs are stored with GZip compression, the default behavior is to return the spec uncompressed (the mime_type response field indicates the exact format returned).

**Overloads**
    
    
    def get_api_spec_contents(request, options = nil) -> ::Google::Api::HttpBody

Pass arguments to `get_api_spec_contents` via a request object, either of type [GetApiSpecContentsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-GetApiSpecContentsRequest "Google::Cloud::ApigeeRegistry::V1::GetApiSpecContentsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApigeeRegistry::V1::GetApiSpecContentsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-GetApiSpecContentsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_api_spec_contents(name: nil) -> ::Google::Api::HttpBody

Pass arguments to `get_api_spec_contents` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the spec whose contents should be retrieved. Format: `projects/*/locations/*/apis/*/versions/*/specs/*`



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Api::HttpBody](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Api-HttpBody)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Api::HttpBody](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Api-HttpBody)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/apigee_registry/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApigeeRegistry::V1::Registry::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApigeeRegistry::V1::GetApiSpecContentsRequest.new
    
    # Call the get_api_spec_contents method.
    result = client.get_api_spec_contents request
    
    # The returned object is of type Google::Api::HttpBody.
    p result

### #get_api_version
    
    
    def get_api_version(request, options = nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiVersion
    def get_api_version(name: nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiVersion

Returns a specified version.

**Overloads**
    
    
    def get_api_version(request, options = nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiVersion

Pass arguments to `get_api_version` via a request object, either of type [GetApiVersionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-GetApiVersionRequest "Google::Cloud::ApigeeRegistry::V1::GetApiVersionRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApigeeRegistry::V1::GetApiVersionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-GetApiVersionRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_api_version(name: nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiVersion

Pass arguments to `get_api_version` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the version to retrieve. Format: `projects/*/locations/*/apis/*/versions/*`



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::ApigeeRegistry::V1::ApiVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ApiVersion)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::ApigeeRegistry::V1::ApiVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ApiVersion)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/apigee_registry/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApigeeRegistry::V1::Registry::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApigeeRegistry::V1::GetApiVersionRequest.new
    
    # Call the get_api_version method.
    result = client.get_api_version request
    
    # The returned object is of type Google::Cloud::ApigeeRegistry::V1::ApiVersion.
    p result

### #get_artifact
    
    
    def get_artifact(request, options = nil) -> ::Google::Cloud::ApigeeRegistry::V1::Artifact
    def get_artifact(name: nil) -> ::Google::Cloud::ApigeeRegistry::V1::Artifact

Returns a specified artifact.

**Overloads**
    
    
    def get_artifact(request, options = nil) -> ::Google::Cloud::ApigeeRegistry::V1::Artifact

Pass arguments to `get_artifact` via a request object, either of type [GetArtifactRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-GetArtifactRequest "Google::Cloud::ApigeeRegistry::V1::GetArtifactRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApigeeRegistry::V1::GetArtifactRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-GetArtifactRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_artifact(name: nil) -> ::Google::Cloud::ApigeeRegistry::V1::Artifact

Pass arguments to `get_artifact` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the artifact to retrieve. Format: `{parent}/artifacts/*`



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::ApigeeRegistry::V1::Artifact](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Artifact)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::ApigeeRegistry::V1::Artifact](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Artifact)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/apigee_registry/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApigeeRegistry::V1::Registry::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApigeeRegistry::V1::GetArtifactRequest.new
    
    # Call the get_artifact method.
    result = client.get_artifact request
    
    # The returned object is of type Google::Cloud::ApigeeRegistry::V1::Artifact.
    p result

### #get_artifact_contents
    
    
    def get_artifact_contents(request, options = nil) -> ::Google::Api::HttpBody
    def get_artifact_contents(name: nil) -> ::Google::Api::HttpBody

Returns the contents of a specified artifact. If artifacts are stored with GZip compression, the default behavior is to return the artifact uncompressed (the mime_type response field indicates the exact format returned).

**Overloads**
    
    
    def get_artifact_contents(request, options = nil) -> ::Google::Api::HttpBody

Pass arguments to `get_artifact_contents` via a request object, either of type [GetArtifactContentsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-GetArtifactContentsRequest "Google::Cloud::ApigeeRegistry::V1::GetArtifactContentsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApigeeRegistry::V1::GetArtifactContentsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-GetArtifactContentsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_artifact_contents(name: nil) -> ::Google::Api::HttpBody

Pass arguments to `get_artifact_contents` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the artifact whose contents should be retrieved. Format: `{parent}/artifacts/*`



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Api::HttpBody](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Api-HttpBody)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Api::HttpBody](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Api-HttpBody)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/apigee_registry/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApigeeRegistry::V1::Registry::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApigeeRegistry::V1::GetArtifactContentsRequest.new
    
    # Call the get_artifact_contents method.
    result = client.get_artifact_contents request
    
    # The returned object is of type Google::Api::HttpBody.
    p result

### #iam_policy_client
    
    
    def iam_policy_client() -> Google::Iam::V1::IAMPolicy::Client

Get the associated client for mix-in of the IAMPolicy.

**Returns**

  * (Google::Iam::V1::IAMPolicy::Client) 



### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new Registry client object.

**Yields**

  * (config) — Configure the Registry client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Registry-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Registry-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::ApigeeRegistry::V1::Registry::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::ApigeeRegistry::V1::Registry::Client.new do |config|
      config.timeout = 10.0
    end

### #list_api_deployment_revisions
    
    
    def list_api_deployment_revisions(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ApigeeRegistry::V1::ApiDeployment>
    def list_api_deployment_revisions(name: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ApigeeRegistry::V1::ApiDeployment>

Lists all revisions of a deployment. Revisions are returned in descending order of revision creation time.

**Overloads**
    
    
    def list_api_deployment_revisions(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ApigeeRegistry::V1::ApiDeployment>

Pass arguments to `list_api_deployment_revisions` via a request object, either of type [ListApiDeploymentRevisionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ListApiDeploymentRevisionsRequest "Google::Cloud::ApigeeRegistry::V1::ListApiDeploymentRevisionsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApigeeRegistry::V1::ListApiDeploymentRevisionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ListApiDeploymentRevisionsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_api_deployment_revisions(name: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ApigeeRegistry::V1::ApiDeployment>

Pass arguments to `list_api_deployment_revisions` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the deployment to list revisions for. 
  * **page_size** (::Integer) — The maximum number of revisions to return per page. 
  * **page_token** (::String) — The page token, received from a previous ListApiDeploymentRevisions call. Provide this to retrieve the subsequent page. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::ApigeeRegistry::V1::ApiDeployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ApiDeployment)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::ApigeeRegistry::V1::ApiDeployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ApiDeployment)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/apigee_registry/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApigeeRegistry::V1::Registry::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApigeeRegistry::V1::ListApiDeploymentRevisionsRequest.new
    
    # Call the list_api_deployment_revisions method.
    result = client.list_api_deployment_revisions request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::ApigeeRegistry::V1::ApiDeployment.
      p item
    end

### #list_api_deployments
    
    
    def list_api_deployments(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ApigeeRegistry::V1::ApiDeployment>
    def list_api_deployments(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ApigeeRegistry::V1::ApiDeployment>

Returns matching deployments.

**Overloads**
    
    
    def list_api_deployments(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ApigeeRegistry::V1::ApiDeployment>

Pass arguments to `list_api_deployments` via a request object, either of type [ListApiDeploymentsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ListApiDeploymentsRequest "Google::Cloud::ApigeeRegistry::V1::ListApiDeploymentsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApigeeRegistry::V1::ListApiDeploymentsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ListApiDeploymentsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_api_deployments(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ApigeeRegistry::V1::ApiDeployment>

Pass arguments to `list_api_deployments` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent, which owns this collection of deployments. Format: `projects/*/locations/*/apis/*`
  * **page_size** (::Integer) — The maximum number of deployments to return. The service may return fewer than this value. If unspecified, at most 50 values will be returned. The maximum is 1000; values above 1000 will be coerced to 1000. 
  * **page_token** (::String) — A page token, received from a previous `ListApiDeployments` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `ListApiDeployments` must match the call that provided the page token. 

  * **filter** (::String) — An expression that can be used to filter the list. Filters use the Common Expression Language and can refer to all message fields. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::ApigeeRegistry::V1::ApiDeployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ApiDeployment)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::ApigeeRegistry::V1::ApiDeployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ApiDeployment)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/apigee_registry/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApigeeRegistry::V1::Registry::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApigeeRegistry::V1::ListApiDeploymentsRequest.new
    
    # Call the list_api_deployments method.
    result = client.list_api_deployments request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::ApigeeRegistry::V1::ApiDeployment.
      p item
    end

### #list_api_spec_revisions
    
    
    def list_api_spec_revisions(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ApigeeRegistry::V1::ApiSpec>
    def list_api_spec_revisions(name: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ApigeeRegistry::V1::ApiSpec>

Lists all revisions of a spec. Revisions are returned in descending order of revision creation time.

**Overloads**
    
    
    def list_api_spec_revisions(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ApigeeRegistry::V1::ApiSpec>

Pass arguments to `list_api_spec_revisions` via a request object, either of type [ListApiSpecRevisionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ListApiSpecRevisionsRequest "Google::Cloud::ApigeeRegistry::V1::ListApiSpecRevisionsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApigeeRegistry::V1::ListApiSpecRevisionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ListApiSpecRevisionsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_api_spec_revisions(name: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ApigeeRegistry::V1::ApiSpec>

Pass arguments to `list_api_spec_revisions` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the spec to list revisions for. 
  * **page_size** (::Integer) — The maximum number of revisions to return per page. 
  * **page_token** (::String) — The page token, received from a previous ListApiSpecRevisions call. Provide this to retrieve the subsequent page. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::ApigeeRegistry::V1::ApiSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ApiSpec)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::ApigeeRegistry::V1::ApiSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ApiSpec)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/apigee_registry/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApigeeRegistry::V1::Registry::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApigeeRegistry::V1::ListApiSpecRevisionsRequest.new
    
    # Call the list_api_spec_revisions method.
    result = client.list_api_spec_revisions request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::ApigeeRegistry::V1::ApiSpec.
      p item
    end

### #list_api_specs
    
    
    def list_api_specs(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ApigeeRegistry::V1::ApiSpec>
    def list_api_specs(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ApigeeRegistry::V1::ApiSpec>

Returns matching specs.

**Overloads**
    
    
    def list_api_specs(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ApigeeRegistry::V1::ApiSpec>

Pass arguments to `list_api_specs` via a request object, either of type [ListApiSpecsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ListApiSpecsRequest "Google::Cloud::ApigeeRegistry::V1::ListApiSpecsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApigeeRegistry::V1::ListApiSpecsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ListApiSpecsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_api_specs(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ApigeeRegistry::V1::ApiSpec>

Pass arguments to `list_api_specs` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent, which owns this collection of specs. Format: `projects/*/locations/*/apis/*/versions/*`
  * **page_size** (::Integer) — The maximum number of specs to return. The service may return fewer than this value. If unspecified, at most 50 values will be returned. The maximum is 1000; values above 1000 will be coerced to 1000. 
  * **page_token** (::String) — A page token, received from a previous `ListApiSpecs` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `ListApiSpecs` must match the call that provided the page token. 

  * **filter** (::String) — An expression that can be used to filter the list. Filters use the Common Expression Language and can refer to all message fields except contents. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::ApigeeRegistry::V1::ApiSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ApiSpec)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::ApigeeRegistry::V1::ApiSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ApiSpec)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/apigee_registry/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApigeeRegistry::V1::Registry::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApigeeRegistry::V1::ListApiSpecsRequest.new
    
    # Call the list_api_specs method.
    result = client.list_api_specs request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::ApigeeRegistry::V1::ApiSpec.
      p item
    end

### #list_api_versions
    
    
    def list_api_versions(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ApigeeRegistry::V1::ApiVersion>
    def list_api_versions(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ApigeeRegistry::V1::ApiVersion>

Returns matching versions.

**Overloads**
    
    
    def list_api_versions(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ApigeeRegistry::V1::ApiVersion>

Pass arguments to `list_api_versions` via a request object, either of type [ListApiVersionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ListApiVersionsRequest "Google::Cloud::ApigeeRegistry::V1::ListApiVersionsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApigeeRegistry::V1::ListApiVersionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ListApiVersionsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_api_versions(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ApigeeRegistry::V1::ApiVersion>

Pass arguments to `list_api_versions` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent, which owns this collection of versions. Format: `projects/*/locations/*/apis/*`
  * **page_size** (::Integer) — The maximum number of versions to return. The service may return fewer than this value. If unspecified, at most 50 values will be returned. The maximum is 1000; values above 1000 will be coerced to 1000. 
  * **page_token** (::String) — A page token, received from a previous `ListApiVersions` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `ListApiVersions` must match the call that provided the page token. 

  * **filter** (::String) — An expression that can be used to filter the list. Filters use the Common Expression Language and can refer to all message fields. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::ApigeeRegistry::V1::ApiVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ApiVersion)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::ApigeeRegistry::V1::ApiVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ApiVersion)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/apigee_registry/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApigeeRegistry::V1::Registry::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApigeeRegistry::V1::ListApiVersionsRequest.new
    
    # Call the list_api_versions method.
    result = client.list_api_versions request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::ApigeeRegistry::V1::ApiVersion.
      p item
    end

### #list_apis
    
    
    def list_apis(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ApigeeRegistry::V1::Api>
    def list_apis(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ApigeeRegistry::V1::Api>

Returns matching APIs.

**Overloads**
    
    
    def list_apis(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ApigeeRegistry::V1::Api>

Pass arguments to `list_apis` via a request object, either of type [ListApisRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ListApisRequest "Google::Cloud::ApigeeRegistry::V1::ListApisRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApigeeRegistry::V1::ListApisRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ListApisRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_apis(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ApigeeRegistry::V1::Api>

Pass arguments to `list_apis` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent, which owns this collection of APIs. Format: `projects/*/locations/*`
  * **page_size** (::Integer) — The maximum number of APIs to return. The service may return fewer than this value. If unspecified, at most 50 values will be returned. The maximum is 1000; values above 1000 will be coerced to 1000. 
  * **page_token** (::String) — A page token, received from a previous `ListApis` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `ListApis` must match the call that provided the page token. 

  * **filter** (::String) — An expression that can be used to filter the list. Filters use the Common Expression Language and can refer to all message fields. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::ApigeeRegistry::V1::Api](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Api)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::ApigeeRegistry::V1::Api](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Api)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/apigee_registry/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApigeeRegistry::V1::Registry::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApigeeRegistry::V1::ListApisRequest.new
    
    # Call the list_apis method.
    result = client.list_apis request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::ApigeeRegistry::V1::Api.
      p item
    end

### #list_artifacts
    
    
    def list_artifacts(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ApigeeRegistry::V1::Artifact>
    def list_artifacts(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ApigeeRegistry::V1::Artifact>

Returns matching artifacts.

**Overloads**
    
    
    def list_artifacts(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ApigeeRegistry::V1::Artifact>

Pass arguments to `list_artifacts` via a request object, either of type [ListArtifactsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ListArtifactsRequest "Google::Cloud::ApigeeRegistry::V1::ListArtifactsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApigeeRegistry::V1::ListArtifactsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ListArtifactsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_artifacts(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ApigeeRegistry::V1::Artifact>

Pass arguments to `list_artifacts` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent, which owns this collection of artifacts. Format: `{parent}`
  * **page_size** (::Integer) — The maximum number of artifacts to return. The service may return fewer than this value. If unspecified, at most 50 values will be returned. The maximum is 1000; values above 1000 will be coerced to 1000. 
  * **page_token** (::String) — A page token, received from a previous `ListArtifacts` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `ListArtifacts` must match the call that provided the page token. 

  * **filter** (::String) — An expression that can be used to filter the list. Filters use the Common Expression Language and can refer to all message fields except contents. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::ApigeeRegistry::V1::Artifact](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Artifact)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::ApigeeRegistry::V1::Artifact](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Artifact)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/apigee_registry/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApigeeRegistry::V1::Registry::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApigeeRegistry::V1::ListArtifactsRequest.new
    
    # Call the list_artifacts method.
    result = client.list_artifacts request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::ApigeeRegistry::V1::Artifact.
      p item
    end

### #location_client
    
    
    def location_client() -> Google::Cloud::Location::Locations::Client

Get the associated client for mix-in of the Locations.

**Returns**

  * (Google::Cloud::Location::Locations::Client) 



### #logger
    
    
    def logger() -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #replace_artifact
    
    
    def replace_artifact(request, options = nil) -> ::Google::Cloud::ApigeeRegistry::V1::Artifact
    def replace_artifact(artifact: nil) -> ::Google::Cloud::ApigeeRegistry::V1::Artifact

Used to replace a specified artifact.

**Overloads**
    
    
    def replace_artifact(request, options = nil) -> ::Google::Cloud::ApigeeRegistry::V1::Artifact

Pass arguments to `replace_artifact` via a request object, either of type [Google::Cloud::ApigeeRegistry::V1::ReplaceArtifactRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ReplaceArtifactRequest "Google::Cloud::ApigeeRegistry::V1::ReplaceArtifactRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApigeeRegistry::V1::ReplaceArtifactRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ReplaceArtifactRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def replace_artifact(artifact: nil) -> ::Google::Cloud::ApigeeRegistry::V1::Artifact

Pass arguments to `replace_artifact` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **artifact** ([::Google::Cloud::ApigeeRegistry::V1::Artifact](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Artifact), ::Hash) — Required. The artifact to replace.

The `name` field is used to identify the artifact to replace. Format: `{parent}/artifacts/*`




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::ApigeeRegistry::V1::Artifact](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Artifact)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::ApigeeRegistry::V1::Artifact](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Artifact)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/apigee_registry/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApigeeRegistry::V1::Registry::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApigeeRegistry::V1::ReplaceArtifactRequest.new
    
    # Call the replace_artifact method.
    result = client.replace_artifact request
    
    # The returned object is of type Google::Cloud::ApigeeRegistry::V1::Artifact.
    p result

### #rollback_api_deployment
    
    
    def rollback_api_deployment(request, options = nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiDeployment
    def rollback_api_deployment(name: nil, revision_id: nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiDeployment

Sets the current revision to a specified prior revision. Note that this creates a new revision with a new revision ID.

**Overloads**
    
    
    def rollback_api_deployment(request, options = nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiDeployment

Pass arguments to `rollback_api_deployment` via a request object, either of type [Google::Cloud::ApigeeRegistry::V1::RollbackApiDeploymentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-RollbackApiDeploymentRequest "Google::Cloud::ApigeeRegistry::V1::RollbackApiDeploymentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApigeeRegistry::V1::RollbackApiDeploymentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-RollbackApiDeploymentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def rollback_api_deployment(name: nil, revision_id: nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiDeployment

Pass arguments to `rollback_api_deployment` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The deployment being rolled back. 
  * **revision_id** (::String) — Required. The revision ID to roll back to. It must be a revision of the same deployment.

Example: `c7cfa2a8`




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::ApigeeRegistry::V1::ApiDeployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ApiDeployment)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::ApigeeRegistry::V1::ApiDeployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ApiDeployment)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/apigee_registry/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApigeeRegistry::V1::Registry::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApigeeRegistry::V1::RollbackApiDeploymentRequest.new
    
    # Call the rollback_api_deployment method.
    result = client.rollback_api_deployment request
    
    # The returned object is of type Google::Cloud::ApigeeRegistry::V1::ApiDeployment.
    p result

### #rollback_api_spec
    
    
    def rollback_api_spec(request, options = nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiSpec
    def rollback_api_spec(name: nil, revision_id: nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiSpec

Sets the current revision to a specified prior revision. Note that this creates a new revision with a new revision ID.

**Overloads**
    
    
    def rollback_api_spec(request, options = nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiSpec

Pass arguments to `rollback_api_spec` via a request object, either of type [Google::Cloud::ApigeeRegistry::V1::RollbackApiSpecRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-RollbackApiSpecRequest "Google::Cloud::ApigeeRegistry::V1::RollbackApiSpecRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApigeeRegistry::V1::RollbackApiSpecRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-RollbackApiSpecRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def rollback_api_spec(name: nil, revision_id: nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiSpec

Pass arguments to `rollback_api_spec` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The spec being rolled back. 
  * **revision_id** (::String) — Required. The revision ID to roll back to. It must be a revision of the same spec.

Example: `c7cfa2a8`




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::ApigeeRegistry::V1::ApiSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ApiSpec)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::ApigeeRegistry::V1::ApiSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ApiSpec)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/apigee_registry/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApigeeRegistry::V1::Registry::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApigeeRegistry::V1::RollbackApiSpecRequest.new
    
    # Call the rollback_api_spec method.
    result = client.rollback_api_spec request
    
    # The returned object is of type Google::Cloud::ApigeeRegistry::V1::ApiSpec.
    p result

### #tag_api_deployment_revision
    
    
    def tag_api_deployment_revision(request, options = nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiDeployment
    def tag_api_deployment_revision(name: nil, tag: nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiDeployment

Adds a tag to a specified revision of a deployment.

**Overloads**
    
    
    def tag_api_deployment_revision(request, options = nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiDeployment

Pass arguments to `tag_api_deployment_revision` via a request object, either of type [TagApiDeploymentRevisionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-TagApiDeploymentRevisionRequest "Google::Cloud::ApigeeRegistry::V1::TagApiDeploymentRevisionRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApigeeRegistry::V1::TagApiDeploymentRevisionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-TagApiDeploymentRevisionRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def tag_api_deployment_revision(name: nil, tag: nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiDeployment

Pass arguments to `tag_api_deployment_revision` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the deployment to be tagged, including the revision ID. 
  * **tag** (::String) — Required. The tag to apply. The tag should be at most 40 characters, and match `[a-z][a-z0-9-]{3,39}`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::ApigeeRegistry::V1::ApiDeployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ApiDeployment)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::ApigeeRegistry::V1::ApiDeployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ApiDeployment)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/apigee_registry/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApigeeRegistry::V1::Registry::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApigeeRegistry::V1::TagApiDeploymentRevisionRequest.new
    
    # Call the tag_api_deployment_revision method.
    result = client.tag_api_deployment_revision request
    
    # The returned object is of type Google::Cloud::ApigeeRegistry::V1::ApiDeployment.
    p result

### #tag_api_spec_revision
    
    
    def tag_api_spec_revision(request, options = nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiSpec
    def tag_api_spec_revision(name: nil, tag: nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiSpec

Adds a tag to a specified revision of a spec.

**Overloads**
    
    
    def tag_api_spec_revision(request, options = nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiSpec

Pass arguments to `tag_api_spec_revision` via a request object, either of type [TagApiSpecRevisionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-TagApiSpecRevisionRequest "Google::Cloud::ApigeeRegistry::V1::TagApiSpecRevisionRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApigeeRegistry::V1::TagApiSpecRevisionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-TagApiSpecRevisionRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def tag_api_spec_revision(name: nil, tag: nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiSpec

Pass arguments to `tag_api_spec_revision` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the spec to be tagged, including the revision ID. 
  * **tag** (::String) — Required. The tag to apply. The tag should be at most 40 characters, and match `[a-z][a-z0-9-]{3,39}`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::ApigeeRegistry::V1::ApiSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ApiSpec)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::ApigeeRegistry::V1::ApiSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ApiSpec)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/apigee_registry/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApigeeRegistry::V1::Registry::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApigeeRegistry::V1::TagApiSpecRevisionRequest.new
    
    # Call the tag_api_spec_revision method.
    result = client.tag_api_spec_revision request
    
    # The returned object is of type Google::Cloud::ApigeeRegistry::V1::ApiSpec.
    p result

### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_api
    
    
    def update_api(request, options = nil) -> ::Google::Cloud::ApigeeRegistry::V1::Api
    def update_api(api: nil, update_mask: nil, allow_missing: nil) -> ::Google::Cloud::ApigeeRegistry::V1::Api

Used to modify a specified API.

**Overloads**
    
    
    def update_api(request, options = nil) -> ::Google::Cloud::ApigeeRegistry::V1::Api

Pass arguments to `update_api` via a request object, either of type [UpdateApiRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-UpdateApiRequest "Google::Cloud::ApigeeRegistry::V1::UpdateApiRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApigeeRegistry::V1::UpdateApiRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-UpdateApiRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_api(api: nil, update_mask: nil, allow_missing: nil) -> ::Google::Cloud::ApigeeRegistry::V1::Api

Pass arguments to `update_api` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **api** ([::Google::Cloud::ApigeeRegistry::V1::Api](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Api), ::Hash) — Required. The API to update.

The `name` field is used to identify the API to update. Format: `projects/*/locations/*/apis/*`

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Protobuf-FieldMask), ::Hash) — The list of fields to be updated. If omitted, all fields are updated that are set in the request message (fields set to default values are ignored). If an asterisk "*" is specified, all fields are updated, including fields that are unspecified/default in the request. 
  * **allow_missing** (::Boolean) — If set to true, and the API is not found, a new API will be created. In this situation, `update_mask` is ignored. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::ApigeeRegistry::V1::Api](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Api)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::ApigeeRegistry::V1::Api](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Api)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/apigee_registry/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApigeeRegistry::V1::Registry::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApigeeRegistry::V1::UpdateApiRequest.new
    
    # Call the update_api method.
    result = client.update_api request
    
    # The returned object is of type Google::Cloud::ApigeeRegistry::V1::Api.
    p result

### #update_api_deployment
    
    
    def update_api_deployment(request, options = nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiDeployment
    def update_api_deployment(api_deployment: nil, update_mask: nil, allow_missing: nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiDeployment

Used to modify a specified deployment.

**Overloads**
    
    
    def update_api_deployment(request, options = nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiDeployment

Pass arguments to `update_api_deployment` via a request object, either of type [UpdateApiDeploymentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-UpdateApiDeploymentRequest "Google::Cloud::ApigeeRegistry::V1::UpdateApiDeploymentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApigeeRegistry::V1::UpdateApiDeploymentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-UpdateApiDeploymentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_api_deployment(api_deployment: nil, update_mask: nil, allow_missing: nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiDeployment

Pass arguments to `update_api_deployment` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **api_deployment** ([::Google::Cloud::ApigeeRegistry::V1::ApiDeployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ApiDeployment), ::Hash) — Required. The deployment to update.

The `name` field is used to identify the deployment to update. Format: `projects/*/locations/*/apis/*/deployments/*`

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Protobuf-FieldMask), ::Hash) — The list of fields to be updated. If omitted, all fields are updated that are set in the request message (fields set to default values are ignored). If an asterisk "*" is specified, all fields are updated, including fields that are unspecified/default in the request. 
  * **allow_missing** (::Boolean) — If set to true, and the deployment is not found, a new deployment will be created. In this situation, `update_mask` is ignored. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::ApigeeRegistry::V1::ApiDeployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ApiDeployment)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::ApigeeRegistry::V1::ApiDeployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ApiDeployment)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/apigee_registry/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApigeeRegistry::V1::Registry::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApigeeRegistry::V1::UpdateApiDeploymentRequest.new
    
    # Call the update_api_deployment method.
    result = client.update_api_deployment request
    
    # The returned object is of type Google::Cloud::ApigeeRegistry::V1::ApiDeployment.
    p result

### #update_api_spec
    
    
    def update_api_spec(request, options = nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiSpec
    def update_api_spec(api_spec: nil, update_mask: nil, allow_missing: nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiSpec

Used to modify a specified spec.

**Overloads**
    
    
    def update_api_spec(request, options = nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiSpec

Pass arguments to `update_api_spec` via a request object, either of type [UpdateApiSpecRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-UpdateApiSpecRequest "Google::Cloud::ApigeeRegistry::V1::UpdateApiSpecRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApigeeRegistry::V1::UpdateApiSpecRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-UpdateApiSpecRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_api_spec(api_spec: nil, update_mask: nil, allow_missing: nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiSpec

Pass arguments to `update_api_spec` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **api_spec** ([::Google::Cloud::ApigeeRegistry::V1::ApiSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ApiSpec), ::Hash) — Required. The spec to update.

The `name` field is used to identify the spec to update. Format: `projects/*/locations/*/apis/*/versions/*/specs/*`

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Protobuf-FieldMask), ::Hash) — The list of fields to be updated. If omitted, all fields are updated that are set in the request message (fields set to default values are ignored). If an asterisk "*" is specified, all fields are updated, including fields that are unspecified/default in the request. 
  * **allow_missing** (::Boolean) — If set to true, and the spec is not found, a new spec will be created. In this situation, `update_mask` is ignored. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::ApigeeRegistry::V1::ApiSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ApiSpec)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::ApigeeRegistry::V1::ApiSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ApiSpec)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/apigee_registry/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApigeeRegistry::V1::Registry::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApigeeRegistry::V1::UpdateApiSpecRequest.new
    
    # Call the update_api_spec method.
    result = client.update_api_spec request
    
    # The returned object is of type Google::Cloud::ApigeeRegistry::V1::ApiSpec.
    p result

### #update_api_version
    
    
    def update_api_version(request, options = nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiVersion
    def update_api_version(api_version: nil, update_mask: nil, allow_missing: nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiVersion

Used to modify a specified version.

**Overloads**
    
    
    def update_api_version(request, options = nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiVersion

Pass arguments to `update_api_version` via a request object, either of type [UpdateApiVersionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-UpdateApiVersionRequest "Google::Cloud::ApigeeRegistry::V1::UpdateApiVersionRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApigeeRegistry::V1::UpdateApiVersionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-UpdateApiVersionRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_api_version(api_version: nil, update_mask: nil, allow_missing: nil) -> ::Google::Cloud::ApigeeRegistry::V1::ApiVersion

Pass arguments to `update_api_version` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **api_version** ([::Google::Cloud::ApigeeRegistry::V1::ApiVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ApiVersion), ::Hash) — Required. The version to update.

The `name` field is used to identify the version to update. Format: `projects/*/locations/*/apis/*/versions/*`

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Protobuf-FieldMask), ::Hash) — The list of fields to be updated. If omitted, all fields are updated that are set in the request message (fields set to default values are ignored). If an asterisk "*" is specified, all fields are updated, including fields that are unspecified/default in the request. 
  * **allow_missing** (::Boolean) — If set to true, and the version is not found, a new version will be created. In this situation, `update_mask` is ignored. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::ApigeeRegistry::V1::ApiVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ApiVersion)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::ApigeeRegistry::V1::ApiVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ApiVersion)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/apigee_registry/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApigeeRegistry::V1::Registry::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApigeeRegistry::V1::UpdateApiVersionRequest.new
    
    # Call the update_api_version method.
    result = client.update_api_version request
    
    # The returned object is of type Google::Cloud::ApigeeRegistry::V1::ApiVersion.
    p result

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
