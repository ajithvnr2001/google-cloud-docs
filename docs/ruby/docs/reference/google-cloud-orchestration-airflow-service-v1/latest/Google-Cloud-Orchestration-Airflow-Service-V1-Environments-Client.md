---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-Environments-Client/
title: Cloud Composer V1 API - Class Google::Cloud::Orchestration::Airflow::Service::V1::Environments::Client (v1.9.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:17:09.032194+00:00
---

# Cloud Composer V1 API - Class Google::Cloud::Orchestration::Airflow::Service::V1::Environments::Client (v1.9.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-Environments-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Composer V1 API - Class Google::Cloud::Orchestration::Airflow::Service::V1::Environments::Client (v1.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.9.0 (latest)  1.8.0  1.7.0  1.6.1  1.5.0  1.4.0  1.3.4  1.2.0  1.1.0  1.0.1  0.11.0  0.10.0  0.9.2  0.8.0  0.7.0  0.6.1  0.5.0  0.4.0  0.3.1  0.2.0  0.1.2 

Reference documentation and code samples for the Cloud Composer V1 API class Google::Cloud::Orchestration::Airflow::Service::V1::Environments::Client.

Client for the Environments service.

Managed Apache Airflow Environments.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::Orchestration::Airflow::Service::V1::Environments::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-Environments-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the Environments Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-Environments-Client-Configuration "Google::Cloud::Orchestration::Airflow::Service::V1::Environments::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-Environments-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-Environments-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all Environments clients
    ::Google::Cloud::Orchestration::Airflow::Service::V1::Environments::Client.configure do |config|
      config.timeout = 10.0
    end

### #check_upgrade
    
    
    def check_upgrade(request, options = nil) -> ::Gapic::Operation
    def check_upgrade(environment: nil, image_version: nil) -> ::Gapic::Operation

Check if an upgrade operation on the environment will succeed.

In case of problems detailed info can be found in the returned Operation.

**Overloads**
    
    
    def check_upgrade(request, options = nil) -> ::Gapic::Operation

Pass arguments to `check_upgrade` via a request object, either of type [CheckUpgradeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-CheckUpgradeRequest "Google::Cloud::Orchestration::Airflow::Service::V1::CheckUpgradeRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Orchestration::Airflow::Service::V1::CheckUpgradeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-CheckUpgradeRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def check_upgrade(environment: nil, image_version: nil) -> ::Gapic::Operation

Pass arguments to `check_upgrade` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **environment** (::String) — Required. The resource name of the environment to check upgrade for, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}" 
  * **image_version** (::String) — Optional. The version of the software running in the environment. This encapsulates both the version of Cloud Composer functionality and the version of Apache Airflow. It must match the regular expression `composer-([0-9]+(\.[0-9]+\.[0-9]+(-preview\.[0-9]+)?)?|latest)-airflow-([0-9]+(\.[0-9]+(\.[0-9]+)?)?)`. When used as input, the server also checks if the provided version is supported and denies the request for an unsupported version.

The Cloud Composer portion of the image version is a full [semantic version](https://semver.org), or an alias in the form of major version number or `latest`. When an alias is provided, the server replaces it with the current Cloud Composer version that satisfies the alias.

The Apache Airflow portion of the image version is a full semantic version that points to one of the supported Apache Airflow versions, or an alias in the form of only major or major.minor versions specified. When an alias is provided, the server replaces it with the latest Apache Airflow version that satisfies the alias and is supported in the given Cloud Composer version.

In all cases, the resolved image version is stored in the same field.

See also [version list](https://docs.cloud.google.com/composer/docs/concepts/versioning/composer-versions) and [versioning overview](https://docs.cloud.google.com/composer/docs/concepts/versioning/composer-versioning-overview). 




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
    
    
    require "google/cloud/orchestration/airflow/service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Orchestration::Airflow::Service::V1::Environments::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Orchestration::Airflow::Service::V1::CheckUpgradeRequest.new
    
    # Call the check_upgrade method.
    result = client.check_upgrade request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the Environments Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-Environments-Client#Google__Cloud__Orchestration__Airflow__Service__V1__Environments__Client_configure_class_ "Google::Cloud::Orchestration::Airflow::Service::V1::Environments::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-Environments-Client-Configuration "Google::Cloud::Orchestration::Airflow::Service::V1::Environments::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-Environments-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-Environments-Client-Configuration)) 



### #create_environment
    
    
    def create_environment(request, options = nil) -> ::Gapic::Operation
    def create_environment(parent: nil, environment: nil) -> ::Gapic::Operation

Create a new environment.

**Overloads**
    
    
    def create_environment(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_environment` via a request object, either of type [CreateEnvironmentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-CreateEnvironmentRequest "Google::Cloud::Orchestration::Airflow::Service::V1::CreateEnvironmentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Orchestration::Airflow::Service::V1::CreateEnvironmentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-CreateEnvironmentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_environment(parent: nil, environment: nil) -> ::Gapic::Operation

Pass arguments to `create_environment` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — The parent must be of the form "projects/{projectId}/locations/{locationId}". 
  * **environment** ([::Google::Cloud::Orchestration::Airflow::Service::V1::Environment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-Environment), ::Hash) — The environment to create. 



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
    
    
    require "google/cloud/orchestration/airflow/service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Orchestration::Airflow::Service::V1::Environments::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Orchestration::Airflow::Service::V1::CreateEnvironmentRequest.new
    
    # Call the create_environment method.
    result = client.create_environment request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #create_user_workloads_config_map
    
    
    def create_user_workloads_config_map(request, options = nil) -> ::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsConfigMap
    def create_user_workloads_config_map(parent: nil, user_workloads_config_map: nil) -> ::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsConfigMap

Creates a user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Overloads**
    
    
    def create_user_workloads_config_map(request, options = nil) -> ::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsConfigMap

Pass arguments to `create_user_workloads_config_map` via a request object, either of type [CreateUserWorkloadsConfigMapRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-CreateUserWorkloadsConfigMapRequest "Google::Cloud::Orchestration::Airflow::Service::V1::CreateUserWorkloadsConfigMapRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Orchestration::Airflow::Service::V1::CreateUserWorkloadsConfigMapRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-CreateUserWorkloadsConfigMapRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_user_workloads_config_map(parent: nil, user_workloads_config_map: nil) -> ::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsConfigMap

Pass arguments to `create_user_workloads_config_map` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The environment name to create a ConfigMap for, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}" 
  * **user_workloads_config_map** ([::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsConfigMap](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-UserWorkloadsConfigMap), ::Hash) — Required. User workloads ConfigMap to create. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsConfigMap](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-UserWorkloadsConfigMap)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsConfigMap](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-UserWorkloadsConfigMap)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/orchestration/airflow/service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Orchestration::Airflow::Service::V1::Environments::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Orchestration::Airflow::Service::V1::CreateUserWorkloadsConfigMapRequest.new
    
    # Call the create_user_workloads_config_map method.
    result = client.create_user_workloads_config_map request
    
    # The returned object is of type Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsConfigMap.
    p result

### #create_user_workloads_secret
    
    
    def create_user_workloads_secret(request, options = nil) -> ::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsSecret
    def create_user_workloads_secret(parent: nil, user_workloads_secret: nil) -> ::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsSecret

Creates a user workloads Secret.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Overloads**
    
    
    def create_user_workloads_secret(request, options = nil) -> ::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsSecret

Pass arguments to `create_user_workloads_secret` via a request object, either of type [CreateUserWorkloadsSecretRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-CreateUserWorkloadsSecretRequest "Google::Cloud::Orchestration::Airflow::Service::V1::CreateUserWorkloadsSecretRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Orchestration::Airflow::Service::V1::CreateUserWorkloadsSecretRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-CreateUserWorkloadsSecretRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_user_workloads_secret(parent: nil, user_workloads_secret: nil) -> ::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsSecret

Pass arguments to `create_user_workloads_secret` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The environment name to create a Secret for, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}" 
  * **user_workloads_secret** ([::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsSecret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-UserWorkloadsSecret), ::Hash) — Required. User workloads Secret to create. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsSecret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-UserWorkloadsSecret)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsSecret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-UserWorkloadsSecret)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/orchestration/airflow/service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Orchestration::Airflow::Service::V1::Environments::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Orchestration::Airflow::Service::V1::CreateUserWorkloadsSecretRequest.new
    
    # Call the create_user_workloads_secret method.
    result = client.create_user_workloads_secret request
    
    # The returned object is of type Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsSecret.
    p result

### #database_failover
    
    
    def database_failover(request, options = nil) -> ::Gapic::Operation
    def database_failover(environment: nil) -> ::Gapic::Operation

Triggers database failover (only for highly resilient environments).

**Overloads**
    
    
    def database_failover(request, options = nil) -> ::Gapic::Operation

Pass arguments to `database_failover` via a request object, either of type [DatabaseFailoverRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-DatabaseFailoverRequest "Google::Cloud::Orchestration::Airflow::Service::V1::DatabaseFailoverRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Orchestration::Airflow::Service::V1::DatabaseFailoverRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-DatabaseFailoverRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def database_failover(environment: nil) -> ::Gapic::Operation

Pass arguments to `database_failover` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **environment** (::String) — Target environment: "projects/{projectId}/locations/{locationId}/environments/{environmentId}" 



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
    
    
    require "google/cloud/orchestration/airflow/service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Orchestration::Airflow::Service::V1::Environments::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Orchestration::Airflow::Service::V1::DatabaseFailoverRequest.new
    
    # Call the database_failover method.
    result = client.database_failover request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_environment
    
    
    def delete_environment(request, options = nil) -> ::Gapic::Operation
    def delete_environment(name: nil) -> ::Gapic::Operation

Delete an environment.

**Overloads**
    
    
    def delete_environment(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_environment` via a request object, either of type [DeleteEnvironmentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-DeleteEnvironmentRequest "Google::Cloud::Orchestration::Airflow::Service::V1::DeleteEnvironmentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Orchestration::Airflow::Service::V1::DeleteEnvironmentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-DeleteEnvironmentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_environment(name: nil) -> ::Gapic::Operation

Pass arguments to `delete_environment` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — The environment to delete, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}" 



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
    
    
    require "google/cloud/orchestration/airflow/service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Orchestration::Airflow::Service::V1::Environments::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Orchestration::Airflow::Service::V1::DeleteEnvironmentRequest.new
    
    # Call the delete_environment method.
    result = client.delete_environment request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_user_workloads_config_map
    
    
    def delete_user_workloads_config_map(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_user_workloads_config_map(name: nil) -> ::Google::Protobuf::Empty

Deletes a user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Overloads**
    
    
    def delete_user_workloads_config_map(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_user_workloads_config_map` via a request object, either of type [DeleteUserWorkloadsConfigMapRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-DeleteUserWorkloadsConfigMapRequest "Google::Cloud::Orchestration::Airflow::Service::V1::DeleteUserWorkloadsConfigMapRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Orchestration::Airflow::Service::V1::DeleteUserWorkloadsConfigMapRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-DeleteUserWorkloadsConfigMapRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_user_workloads_config_map(name: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_user_workloads_config_map` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The ConfigMap to delete, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}/userWorkloadsConfigMaps/{userWorkloadsConfigMapId}" 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/orchestration/airflow/service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Orchestration::Airflow::Service::V1::Environments::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Orchestration::Airflow::Service::V1::DeleteUserWorkloadsConfigMapRequest.new
    
    # Call the delete_user_workloads_config_map method.
    result = client.delete_user_workloads_config_map request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #delete_user_workloads_secret
    
    
    def delete_user_workloads_secret(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_user_workloads_secret(name: nil) -> ::Google::Protobuf::Empty

Deletes a user workloads Secret.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Overloads**
    
    
    def delete_user_workloads_secret(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_user_workloads_secret` via a request object, either of type [DeleteUserWorkloadsSecretRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-DeleteUserWorkloadsSecretRequest "Google::Cloud::Orchestration::Airflow::Service::V1::DeleteUserWorkloadsSecretRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Orchestration::Airflow::Service::V1::DeleteUserWorkloadsSecretRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-DeleteUserWorkloadsSecretRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_user_workloads_secret(name: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_user_workloads_secret` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The Secret to delete, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}/userWorkloadsSecrets/{userWorkloadsSecretId}" 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/orchestration/airflow/service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Orchestration::Airflow::Service::V1::Environments::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Orchestration::Airflow::Service::V1::DeleteUserWorkloadsSecretRequest.new
    
    # Call the delete_user_workloads_secret method.
    result = client.delete_user_workloads_secret request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #execute_airflow_command
    
    
    def execute_airflow_command(request, options = nil) -> ::Google::Cloud::Orchestration::Airflow::Service::V1::ExecuteAirflowCommandResponse
    def execute_airflow_command(environment: nil, command: nil, subcommand: nil, parameters: nil) -> ::Google::Cloud::Orchestration::Airflow::Service::V1::ExecuteAirflowCommandResponse

Executes Airflow CLI command.

**Overloads**
    
    
    def execute_airflow_command(request, options = nil) -> ::Google::Cloud::Orchestration::Airflow::Service::V1::ExecuteAirflowCommandResponse

Pass arguments to `execute_airflow_command` via a request object, either of type [Google::Cloud::Orchestration::Airflow::Service::V1::ExecuteAirflowCommandRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-ExecuteAirflowCommandRequest "Google::Cloud::Orchestration::Airflow::Service::V1::ExecuteAirflowCommandRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Orchestration::Airflow::Service::V1::ExecuteAirflowCommandRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-ExecuteAirflowCommandRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def execute_airflow_command(environment: nil, command: nil, subcommand: nil, parameters: nil) -> ::Google::Cloud::Orchestration::Airflow::Service::V1::ExecuteAirflowCommandResponse

Pass arguments to `execute_airflow_command` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **environment** (::String) — The resource name of the environment in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}". 
  * **command** (::String) — Airflow command. 
  * **subcommand** (::String) — Airflow subcommand. 
  * **parameters** (::Array<::String>) — Parameters for the Airflow command/subcommand as an array of arguments. It may contain positional arguments like `["my-dag-id"]`, key-value parameters like `["--foo=bar"]` or `["--foo","bar"]`, or other flags like `["-f"]`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Orchestration::Airflow::Service::V1::ExecuteAirflowCommandResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-ExecuteAirflowCommandResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Orchestration::Airflow::Service::V1::ExecuteAirflowCommandResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-ExecuteAirflowCommandResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/orchestration/airflow/service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Orchestration::Airflow::Service::V1::Environments::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Orchestration::Airflow::Service::V1::ExecuteAirflowCommandRequest.new
    
    # Call the execute_airflow_command method.
    result = client.execute_airflow_command request
    
    # The returned object is of type Google::Cloud::Orchestration::Airflow::Service::V1::ExecuteAirflowCommandResponse.
    p result

### #fetch_database_properties
    
    
    def fetch_database_properties(request, options = nil) -> ::Google::Cloud::Orchestration::Airflow::Service::V1::FetchDatabasePropertiesResponse
    def fetch_database_properties(environment: nil) -> ::Google::Cloud::Orchestration::Airflow::Service::V1::FetchDatabasePropertiesResponse

Fetches database properties.

**Overloads**
    
    
    def fetch_database_properties(request, options = nil) -> ::Google::Cloud::Orchestration::Airflow::Service::V1::FetchDatabasePropertiesResponse

Pass arguments to `fetch_database_properties` via a request object, either of type [FetchDatabasePropertiesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-FetchDatabasePropertiesRequest "Google::Cloud::Orchestration::Airflow::Service::V1::FetchDatabasePropertiesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Orchestration::Airflow::Service::V1::FetchDatabasePropertiesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-FetchDatabasePropertiesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def fetch_database_properties(environment: nil) -> ::Google::Cloud::Orchestration::Airflow::Service::V1::FetchDatabasePropertiesResponse

Pass arguments to `fetch_database_properties` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **environment** (::String) — Required. The resource name of the environment, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}" 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Orchestration::Airflow::Service::V1::FetchDatabasePropertiesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-FetchDatabasePropertiesResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Orchestration::Airflow::Service::V1::FetchDatabasePropertiesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-FetchDatabasePropertiesResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/orchestration/airflow/service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Orchestration::Airflow::Service::V1::Environments::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Orchestration::Airflow::Service::V1::FetchDatabasePropertiesRequest.new
    
    # Call the fetch_database_properties method.
    result = client.fetch_database_properties request
    
    # The returned object is of type Google::Cloud::Orchestration::Airflow::Service::V1::FetchDatabasePropertiesResponse.
    p result

### #get_environment
    
    
    def get_environment(request, options = nil) -> ::Google::Cloud::Orchestration::Airflow::Service::V1::Environment
    def get_environment(name: nil) -> ::Google::Cloud::Orchestration::Airflow::Service::V1::Environment

Get an existing environment.

**Overloads**
    
    
    def get_environment(request, options = nil) -> ::Google::Cloud::Orchestration::Airflow::Service::V1::Environment

Pass arguments to `get_environment` via a request object, either of type [GetEnvironmentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-GetEnvironmentRequest "Google::Cloud::Orchestration::Airflow::Service::V1::GetEnvironmentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Orchestration::Airflow::Service::V1::GetEnvironmentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-GetEnvironmentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_environment(name: nil) -> ::Google::Cloud::Orchestration::Airflow::Service::V1::Environment

Pass arguments to `get_environment` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — The resource name of the environment to get, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}" 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Orchestration::Airflow::Service::V1::Environment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-Environment)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Orchestration::Airflow::Service::V1::Environment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-Environment)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/orchestration/airflow/service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Orchestration::Airflow::Service::V1::Environments::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Orchestration::Airflow::Service::V1::GetEnvironmentRequest.new
    
    # Call the get_environment method.
    result = client.get_environment request
    
    # The returned object is of type Google::Cloud::Orchestration::Airflow::Service::V1::Environment.
    p result

### #get_user_workloads_config_map
    
    
    def get_user_workloads_config_map(request, options = nil) -> ::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsConfigMap
    def get_user_workloads_config_map(name: nil) -> ::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsConfigMap

Gets an existing user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Overloads**
    
    
    def get_user_workloads_config_map(request, options = nil) -> ::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsConfigMap

Pass arguments to `get_user_workloads_config_map` via a request object, either of type [GetUserWorkloadsConfigMapRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-GetUserWorkloadsConfigMapRequest "Google::Cloud::Orchestration::Airflow::Service::V1::GetUserWorkloadsConfigMapRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Orchestration::Airflow::Service::V1::GetUserWorkloadsConfigMapRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-GetUserWorkloadsConfigMapRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_user_workloads_config_map(name: nil) -> ::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsConfigMap

Pass arguments to `get_user_workloads_config_map` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The resource name of the ConfigMap to get, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}/userWorkloadsConfigMaps/{userWorkloadsConfigMapId}" 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsConfigMap](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-UserWorkloadsConfigMap)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsConfigMap](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-UserWorkloadsConfigMap)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/orchestration/airflow/service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Orchestration::Airflow::Service::V1::Environments::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Orchestration::Airflow::Service::V1::GetUserWorkloadsConfigMapRequest.new
    
    # Call the get_user_workloads_config_map method.
    result = client.get_user_workloads_config_map request
    
    # The returned object is of type Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsConfigMap.
    p result

### #get_user_workloads_secret
    
    
    def get_user_workloads_secret(request, options = nil) -> ::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsSecret
    def get_user_workloads_secret(name: nil) -> ::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsSecret

Gets an existing user workloads Secret. Values of the "data" field in the response are cleared.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Overloads**
    
    
    def get_user_workloads_secret(request, options = nil) -> ::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsSecret

Pass arguments to `get_user_workloads_secret` via a request object, either of type [GetUserWorkloadsSecretRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-GetUserWorkloadsSecretRequest "Google::Cloud::Orchestration::Airflow::Service::V1::GetUserWorkloadsSecretRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Orchestration::Airflow::Service::V1::GetUserWorkloadsSecretRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-GetUserWorkloadsSecretRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_user_workloads_secret(name: nil) -> ::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsSecret

Pass arguments to `get_user_workloads_secret` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The resource name of the Secret to get, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}/userWorkloadsSecrets/{userWorkloadsSecretId}" 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsSecret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-UserWorkloadsSecret)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsSecret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-UserWorkloadsSecret)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/orchestration/airflow/service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Orchestration::Airflow::Service::V1::Environments::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Orchestration::Airflow::Service::V1::GetUserWorkloadsSecretRequest.new
    
    # Call the get_user_workloads_secret method.
    result = client.get_user_workloads_secret request
    
    # The returned object is of type Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsSecret.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new Environments client object.

**Yields**

  * (config) — Configure the Environments client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-Environments-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-Environments-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Orchestration::Airflow::Service::V1::Environments::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Orchestration::Airflow::Service::V1::Environments::Client.new do |config|
      config.timeout = 10.0
    end

### #list_environments
    
    
    def list_environments(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Orchestration::Airflow::Service::V1::Environment>
    def list_environments(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Orchestration::Airflow::Service::V1::Environment>

List environments.

**Overloads**
    
    
    def list_environments(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Orchestration::Airflow::Service::V1::Environment>

Pass arguments to `list_environments` via a request object, either of type [ListEnvironmentsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-ListEnvironmentsRequest "Google::Cloud::Orchestration::Airflow::Service::V1::ListEnvironmentsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Orchestration::Airflow::Service::V1::ListEnvironmentsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-ListEnvironmentsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_environments(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Orchestration::Airflow::Service::V1::Environment>

Pass arguments to `list_environments` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — List environments in the given project and location, in the form: "projects/{projectId}/locations/{locationId}" 
  * **page_size** (::Integer) — The maximum number of environments to return. 
  * **page_token** (::String) — The next_page_token value returned from a previous List request, if any. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Orchestration::Airflow::Service::V1::Environment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-Environment)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Orchestration::Airflow::Service::V1::Environment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-Environment)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/orchestration/airflow/service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Orchestration::Airflow::Service::V1::Environments::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Orchestration::Airflow::Service::V1::ListEnvironmentsRequest.new
    
    # Call the list_environments method.
    result = client.list_environments request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Orchestration::Airflow::Service::V1::Environment.
      p item
    end

### #list_user_workloads_config_maps
    
    
    def list_user_workloads_config_maps(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsConfigMap>
    def list_user_workloads_config_maps(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsConfigMap>

Lists user workloads ConfigMaps.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Overloads**
    
    
    def list_user_workloads_config_maps(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsConfigMap>

Pass arguments to `list_user_workloads_config_maps` via a request object, either of type [ListUserWorkloadsConfigMapsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-ListUserWorkloadsConfigMapsRequest "Google::Cloud::Orchestration::Airflow::Service::V1::ListUserWorkloadsConfigMapsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Orchestration::Airflow::Service::V1::ListUserWorkloadsConfigMapsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-ListUserWorkloadsConfigMapsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_user_workloads_config_maps(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsConfigMap>

Pass arguments to `list_user_workloads_config_maps` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. List ConfigMaps in the given environment, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}" 
  * **page_size** (::Integer) — Optional. The maximum number of ConfigMaps to return. 
  * **page_token** (::String) — Optional. The next_page_token value returned from a previous List request, if any. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsConfigMap](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-UserWorkloadsConfigMap)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsConfigMap](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-UserWorkloadsConfigMap)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/orchestration/airflow/service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Orchestration::Airflow::Service::V1::Environments::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Orchestration::Airflow::Service::V1::ListUserWorkloadsConfigMapsRequest.new
    
    # Call the list_user_workloads_config_maps method.
    result = client.list_user_workloads_config_maps request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsConfigMap.
      p item
    end

### #list_user_workloads_secrets
    
    
    def list_user_workloads_secrets(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsSecret>
    def list_user_workloads_secrets(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsSecret>

Lists user workloads Secrets.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Overloads**
    
    
    def list_user_workloads_secrets(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsSecret>

Pass arguments to `list_user_workloads_secrets` via a request object, either of type [ListUserWorkloadsSecretsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-ListUserWorkloadsSecretsRequest "Google::Cloud::Orchestration::Airflow::Service::V1::ListUserWorkloadsSecretsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Orchestration::Airflow::Service::V1::ListUserWorkloadsSecretsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-ListUserWorkloadsSecretsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_user_workloads_secrets(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsSecret>

Pass arguments to `list_user_workloads_secrets` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. List Secrets in the given environment, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}" 
  * **page_size** (::Integer) — Optional. The maximum number of Secrets to return. 
  * **page_token** (::String) — Optional. The next_page_token value returned from a previous List request, if any. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsSecret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-UserWorkloadsSecret)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsSecret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-UserWorkloadsSecret)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/orchestration/airflow/service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Orchestration::Airflow::Service::V1::Environments::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Orchestration::Airflow::Service::V1::ListUserWorkloadsSecretsRequest.new
    
    # Call the list_user_workloads_secrets method.
    result = client.list_user_workloads_secrets request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsSecret.
      p item
    end

### #list_workloads
    
    
    def list_workloads(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Orchestration::Airflow::Service::V1::ListWorkloadsResponse::ComposerWorkload>
    def list_workloads(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Orchestration::Airflow::Service::V1::ListWorkloadsResponse::ComposerWorkload>

Lists workloads in a Cloud Composer environment. Workload is a unit that runs a single Composer component.

This method is supported for Cloud Composer environments in versions composer-2._._ -airflow-_._.* and newer.

**Overloads**
    
    
    def list_workloads(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Orchestration::Airflow::Service::V1::ListWorkloadsResponse::ComposerWorkload>

Pass arguments to `list_workloads` via a request object, either of type [ListWorkloadsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-ListWorkloadsRequest "Google::Cloud::Orchestration::Airflow::Service::V1::ListWorkloadsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Orchestration::Airflow::Service::V1::ListWorkloadsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-ListWorkloadsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_workloads(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Orchestration::Airflow::Service::V1::ListWorkloadsResponse::ComposerWorkload>

Pass arguments to `list_workloads` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The environment name to get workloads for, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}" 
  * **page_size** (::Integer) — Optional. The maximum number of environments to return. 
  * **page_token** (::String) — Optional. The next_page_token value returned from a previous List request, if any. 
  * **filter** (::String) — Optional. The list filter. Currently only supports equality on the type field. The value of a field specified in the filter expression must be one ComposerWorkloadType enum option. It's possible to get multiple types using "OR" operator, e.g.: "type=SCHEDULER OR type=CELERY_WORKER". If not specified, all items are returned. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Orchestration::Airflow::Service::V1::ListWorkloadsResponse::ComposerWorkload](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-ListWorkloadsResponse-ComposerWorkload)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Orchestration::Airflow::Service::V1::ListWorkloadsResponse::ComposerWorkload](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-ListWorkloadsResponse-ComposerWorkload)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/orchestration/airflow/service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Orchestration::Airflow::Service::V1::Environments::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Orchestration::Airflow::Service::V1::ListWorkloadsRequest.new
    
    # Call the list_workloads method.
    result = client.list_workloads request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Orchestration::Airflow::Service::V1::ListWorkloadsResponse::ComposerWorkload.
      p item
    end

### #load_snapshot
    
    
    def load_snapshot(request, options = nil) -> ::Gapic::Operation
    def load_snapshot(environment: nil, snapshot_path: nil, skip_pypi_packages_installation: nil, skip_environment_variables_setting: nil, skip_airflow_overrides_setting: nil, skip_gcs_data_copying: nil) -> ::Gapic::Operation

Loads a snapshot of a Cloud Composer environment.

As a result of this operation, a snapshot of environment's specified in LoadSnapshotRequest is loaded into the environment.

**Overloads**
    
    
    def load_snapshot(request, options = nil) -> ::Gapic::Operation

Pass arguments to `load_snapshot` via a request object, either of type [LoadSnapshotRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-LoadSnapshotRequest "Google::Cloud::Orchestration::Airflow::Service::V1::LoadSnapshotRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Orchestration::Airflow::Service::V1::LoadSnapshotRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-LoadSnapshotRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def load_snapshot(environment: nil, snapshot_path: nil, skip_pypi_packages_installation: nil, skip_environment_variables_setting: nil, skip_airflow_overrides_setting: nil, skip_gcs_data_copying: nil) -> ::Gapic::Operation

Pass arguments to `load_snapshot` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **environment** (::String) — The resource name of the target environment in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}" 
  * **snapshot_path** (::String) — A Cloud Storage path to a snapshot to load, e.g.: "gs://my-bucket/snapshots/project_location_environment_timestamp". 
  * **skip_pypi_packages_installation** (::Boolean) — Whether or not to skip installing Pypi packages when loading the environment's state. 
  * **skip_environment_variables_setting** (::Boolean) — Whether or not to skip setting environment variables when loading the environment's state. 
  * **skip_airflow_overrides_setting** (::Boolean) — Whether or not to skip setting Airflow overrides when loading the environment's state. 
  * **skip_gcs_data_copying** (::Boolean) — Whether or not to skip copying Cloud Storage data when loading the environment's state. 



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
    
    
    require "google/cloud/orchestration/airflow/service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Orchestration::Airflow::Service::V1::Environments::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Orchestration::Airflow::Service::V1::LoadSnapshotRequest.new
    
    # Call the load_snapshot method.
    result = client.load_snapshot request
    
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
    
    
    def operations_client() -> ::Google::Cloud::Orchestration::Airflow::Service::V1::Environments::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::Orchestration::Airflow::Service::V1::Environments::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-Environments-Operations)) 



### #poll_airflow_command
    
    
    def poll_airflow_command(request, options = nil) -> ::Google::Cloud::Orchestration::Airflow::Service::V1::PollAirflowCommandResponse
    def poll_airflow_command(environment: nil, execution_id: nil, pod: nil, pod_namespace: nil, next_line_number: nil) -> ::Google::Cloud::Orchestration::Airflow::Service::V1::PollAirflowCommandResponse

Polls Airflow CLI command execution and fetches logs.

**Overloads**
    
    
    def poll_airflow_command(request, options = nil) -> ::Google::Cloud::Orchestration::Airflow::Service::V1::PollAirflowCommandResponse

Pass arguments to `poll_airflow_command` via a request object, either of type [PollAirflowCommandRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-PollAirflowCommandRequest "Google::Cloud::Orchestration::Airflow::Service::V1::PollAirflowCommandRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Orchestration::Airflow::Service::V1::PollAirflowCommandRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-PollAirflowCommandRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def poll_airflow_command(environment: nil, execution_id: nil, pod: nil, pod_namespace: nil, next_line_number: nil) -> ::Google::Cloud::Orchestration::Airflow::Service::V1::PollAirflowCommandResponse

Pass arguments to `poll_airflow_command` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **environment** (::String) — The resource name of the environment in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}" 
  * **execution_id** (::String) — The unique ID of the command execution. 
  * **pod** (::String) — The name of the pod where the command is executed. 
  * **pod_namespace** (::String) — The namespace of the pod where the command is executed. 
  * **next_line_number** (::Integer) — Line number from which new logs should be fetched. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Orchestration::Airflow::Service::V1::PollAirflowCommandResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-PollAirflowCommandResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Orchestration::Airflow::Service::V1::PollAirflowCommandResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-PollAirflowCommandResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/orchestration/airflow/service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Orchestration::Airflow::Service::V1::Environments::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Orchestration::Airflow::Service::V1::PollAirflowCommandRequest.new
    
    # Call the poll_airflow_command method.
    result = client.poll_airflow_command request
    
    # The returned object is of type Google::Cloud::Orchestration::Airflow::Service::V1::PollAirflowCommandResponse.
    p result

### #save_snapshot
    
    
    def save_snapshot(request, options = nil) -> ::Gapic::Operation
    def save_snapshot(environment: nil, snapshot_location: nil) -> ::Gapic::Operation

Creates a snapshots of a Cloud Composer environment.

As a result of this operation, snapshot of environment's state is stored in a location specified in the SaveSnapshotRequest.

**Overloads**
    
    
    def save_snapshot(request, options = nil) -> ::Gapic::Operation

Pass arguments to `save_snapshot` via a request object, either of type [SaveSnapshotRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-SaveSnapshotRequest "Google::Cloud::Orchestration::Airflow::Service::V1::SaveSnapshotRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Orchestration::Airflow::Service::V1::SaveSnapshotRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-SaveSnapshotRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def save_snapshot(environment: nil, snapshot_location: nil) -> ::Gapic::Operation

Pass arguments to `save_snapshot` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **environment** (::String) — The resource name of the source environment in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}" 
  * **snapshot_location** (::String) — Location in a Cloud Storage where the snapshot is going to be stored, e.g.: "gs://my-bucket/snapshots". 



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
    
    
    require "google/cloud/orchestration/airflow/service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Orchestration::Airflow::Service::V1::Environments::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Orchestration::Airflow::Service::V1::SaveSnapshotRequest.new
    
    # Call the save_snapshot method.
    result = client.save_snapshot request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #stop_airflow_command
    
    
    def stop_airflow_command(request, options = nil) -> ::Google::Cloud::Orchestration::Airflow::Service::V1::StopAirflowCommandResponse
    def stop_airflow_command(environment: nil, execution_id: nil, pod: nil, pod_namespace: nil, force: nil) -> ::Google::Cloud::Orchestration::Airflow::Service::V1::StopAirflowCommandResponse

Stops Airflow CLI command execution.

**Overloads**
    
    
    def stop_airflow_command(request, options = nil) -> ::Google::Cloud::Orchestration::Airflow::Service::V1::StopAirflowCommandResponse

Pass arguments to `stop_airflow_command` via a request object, either of type [StopAirflowCommandRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-StopAirflowCommandRequest "Google::Cloud::Orchestration::Airflow::Service::V1::StopAirflowCommandRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Orchestration::Airflow::Service::V1::StopAirflowCommandRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-StopAirflowCommandRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def stop_airflow_command(environment: nil, execution_id: nil, pod: nil, pod_namespace: nil, force: nil) -> ::Google::Cloud::Orchestration::Airflow::Service::V1::StopAirflowCommandResponse

Pass arguments to `stop_airflow_command` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **environment** (::String) — The resource name of the environment in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}". 
  * **execution_id** (::String) — The unique ID of the command execution. 
  * **pod** (::String) — The name of the pod where the command is executed. 
  * **pod_namespace** (::String) — The namespace of the pod where the command is executed. 
  * **force** (::Boolean) — If true, the execution is terminated forcefully (SIGKILL). If false, the execution is stopped gracefully, giving it time for cleanup. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Orchestration::Airflow::Service::V1::StopAirflowCommandResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-StopAirflowCommandResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Orchestration::Airflow::Service::V1::StopAirflowCommandResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-StopAirflowCommandResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/orchestration/airflow/service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Orchestration::Airflow::Service::V1::Environments::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Orchestration::Airflow::Service::V1::StopAirflowCommandRequest.new
    
    # Call the stop_airflow_command method.
    result = client.stop_airflow_command request
    
    # The returned object is of type Google::Cloud::Orchestration::Airflow::Service::V1::StopAirflowCommandResponse.
    p result

### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_environment
    
    
    def update_environment(request, options = nil) -> ::Gapic::Operation
    def update_environment(name: nil, environment: nil, update_mask: nil) -> ::Gapic::Operation

Update an environment.

**Overloads**
    
    
    def update_environment(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_environment` via a request object, either of type [UpdateEnvironmentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-UpdateEnvironmentRequest "Google::Cloud::Orchestration::Airflow::Service::V1::UpdateEnvironmentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Orchestration::Airflow::Service::V1::UpdateEnvironmentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-UpdateEnvironmentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_environment(name: nil, environment: nil, update_mask: nil) -> ::Gapic::Operation

Pass arguments to `update_environment` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — The relative resource name of the environment to update, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}" 
  * **environment** ([::Google::Cloud::Orchestration::Airflow::Service::V1::Environment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-Environment), ::Hash) — A patch environment. Fields specified by the `updateMask` will be copied from the patch environment into the environment under update. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Protobuf-FieldMask), ::Hash) — 

Required. A comma-separated list of paths, relative to `Environment`, of fields to update. For example, to set the version of scikit-learn to install in the environment to 0.19.0 and to remove an existing installation of numpy, the `updateMask` parameter would include the following two `paths` values: "config.softwareConfig.pypiPackages.scikit-learn" and "config.softwareConfig.pypiPackages.numpy". The included patch environment would specify the scikit-learn version as follows:
        
        {
          "config":{
            "softwareConfig":{
              "pypiPackages":{
                "scikit-learn":"==0.19.0"
              }
            }
          }
        }
        

Note that in the above example, any existing PyPI packages other than scikit-learn and numpy will be unaffected.

Only one update type may be included in a single request's `updateMask`. For example, one cannot update both the PyPI packages and labels in the same request. However, it is possible to update multiple members of a map field simultaneously in the same request. For example, to set the labels "label1" and "label2" while clearing "label3" (assuming it already exists), one can provide the paths "labels.label1", "labels.label2", and "labels.label3" and populate the patch environment as follows:
        
        {
          "labels":{
            "label1":"new-label1-value"
            "label2":"new-label2-value"
          }
        }
        

Note that in the above example, any existing labels that are not included in the `updateMask` will be unaffected.

It is also possible to replace an entire map field by providing the map field's path in the `updateMask`. The new value of the field will be that which is provided in the patch environment. For example, to delete all pre-existing user-specified PyPI packages and install botocore at version 1.7.14, the `updateMask` would contain the path "config.softwareConfig.pypiPackages", and the patch environment would be the following:
        
        {
          "config":{
            "softwareConfig":{
              "pypiPackages":{
                "botocore":"==1.7.14"
              }
            }
          }
        }
        

**Note:** Only the following fields can be updated:

    * `config.softwareConfig.pypiPackages`
      * Replace all custom custom PyPI packages. If a replacement package map is not included in `environment`, all custom PyPI packages are cleared. It is an error to provide both this mask and a mask specifying an individual package.
    * `config.softwareConfig.pypiPackages.`packagename 
      * Update the custom PyPI package _packagename_ , preserving other packages. To delete the package, include it in `updateMask`, and omit the mapping for it in `environment.config.softwareConfig.pypiPackages`. It is an error to provide both a mask of this form and the `config.softwareConfig.pypiPackages` mask.
    * `labels`
      * Replace all environment labels. If a replacement labels map is not included in `environment`, all labels are cleared. It is an error to provide both this mask and a mask specifying one or more individual labels.
    * `labels.`labelName 
      * Set the label named _labelName_ , while preserving other labels. To delete the label, include it in `updateMask` and omit its mapping in `environment.labels`. It is an error to provide both a mask of this form and the `labels` mask.
    * `config.nodeCount`
      * Horizontally scale the number of nodes in the environment. An integer greater than or equal to 3 must be provided in the `config.nodeCount` field. Supported for Cloud Composer environments in versions composer-1._._ -airflow-_._.*.
    * `config.webServerNetworkAccessControl`
      * Replace the environment's current `WebServerNetworkAccessControl`.
    * `config.softwareConfig.airflowConfigOverrides`
      * Replace all Apache Airflow config overrides. If a replacement config overrides map is not included in `environment`, all config overrides are cleared. It is an error to provide both this mask and a mask specifying one or more individual config overrides.
    * `config.softwareConfig.airflowConfigOverrides.`section-name 
      * Override the Apache Airflow config property _name_ in the section named _section_ , preserving other properties. To delete the property override, include it in `updateMask` and omit its mapping in `environment.config.softwareConfig.airflowConfigOverrides`. It is an error to provide both a mask of this form and the `config.softwareConfig.airflowConfigOverrides` mask.
    * `config.softwareConfig.envVariables`
      * Replace all environment variables. If a replacement environment variable map is not included in `environment`, all custom environment variables are cleared.
    * `config.softwareConfig.schedulerCount`
      * Horizontally scale the number of schedulers in Airflow. A positive integer not greater than the number of nodes must be provided in the `config.softwareConfig.schedulerCount` field. Supported for Cloud Composer environments in versions composer-1._._ -airflow-2._._.
    * `config.databaseConfig.machineType`
      * Cloud SQL machine type used by Airflow database. It has to be one of: db-n1-standard-2, db-n1-standard-4, db-n1-standard-8 or db-n1-standard-16. Supported for Cloud Composer environments in versions composer-1._._ -airflow-_._.*.
    * `config.webServerConfig.machineType`
      * Machine type on which Airflow web server is running. It has to be one of: composer-n1-webserver-2, composer-n1-webserver-4 or composer-n1-webserver-8. Supported for Cloud Composer environments in versions composer-1._._ -airflow-_._.*.



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
    
    
    require "google/cloud/orchestration/airflow/service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Orchestration::Airflow::Service::V1::Environments::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Orchestration::Airflow::Service::V1::UpdateEnvironmentRequest.new
    
    # Call the update_environment method.
    result = client.update_environment request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #update_user_workloads_config_map
    
    
    def update_user_workloads_config_map(request, options = nil) -> ::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsConfigMap
    def update_user_workloads_config_map(user_workloads_config_map: nil) -> ::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsConfigMap

Updates a user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Overloads**
    
    
    def update_user_workloads_config_map(request, options = nil) -> ::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsConfigMap

Pass arguments to `update_user_workloads_config_map` via a request object, either of type [UpdateUserWorkloadsConfigMapRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-UpdateUserWorkloadsConfigMapRequest "Google::Cloud::Orchestration::Airflow::Service::V1::UpdateUserWorkloadsConfigMapRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Orchestration::Airflow::Service::V1::UpdateUserWorkloadsConfigMapRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-UpdateUserWorkloadsConfigMapRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_user_workloads_config_map(user_workloads_config_map: nil) -> ::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsConfigMap

Pass arguments to `update_user_workloads_config_map` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **user_workloads_config_map** ([::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsConfigMap](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-UserWorkloadsConfigMap), ::Hash) — Optional. User workloads ConfigMap to override. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsConfigMap](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-UserWorkloadsConfigMap)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsConfigMap](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-UserWorkloadsConfigMap)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/orchestration/airflow/service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Orchestration::Airflow::Service::V1::Environments::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Orchestration::Airflow::Service::V1::UpdateUserWorkloadsConfigMapRequest.new
    
    # Call the update_user_workloads_config_map method.
    result = client.update_user_workloads_config_map request
    
    # The returned object is of type Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsConfigMap.
    p result

### #update_user_workloads_secret
    
    
    def update_user_workloads_secret(request, options = nil) -> ::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsSecret
    def update_user_workloads_secret(user_workloads_secret: nil) -> ::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsSecret

Updates a user workloads Secret.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Overloads**
    
    
    def update_user_workloads_secret(request, options = nil) -> ::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsSecret

Pass arguments to `update_user_workloads_secret` via a request object, either of type [UpdateUserWorkloadsSecretRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-UpdateUserWorkloadsSecretRequest "Google::Cloud::Orchestration::Airflow::Service::V1::UpdateUserWorkloadsSecretRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Orchestration::Airflow::Service::V1::UpdateUserWorkloadsSecretRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-UpdateUserWorkloadsSecretRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_user_workloads_secret(user_workloads_secret: nil) -> ::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsSecret

Pass arguments to `update_user_workloads_secret` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **user_workloads_secret** ([::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsSecret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-UserWorkloadsSecret), ::Hash) — Optional. User workloads Secret to override. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsSecret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-UserWorkloadsSecret)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsSecret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-orchestration-airflow-service-v1/latest/Google-Cloud-Orchestration-Airflow-Service-V1-UserWorkloadsSecret)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/orchestration/airflow/service/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Orchestration::Airflow::Service::V1::Environments::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Orchestration::Airflow::Service::V1::UpdateUserWorkloadsSecretRequest.new
    
    # Call the update_user_workloads_secret method.
    result = client.update_user_workloads_secret request
    
    # The returned object is of type Google::Cloud::Orchestration::Airflow::Service::V1::UserWorkloadsSecret.
    p result

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
