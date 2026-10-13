---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-AlloyDBAdmin-Rest-Client/
title: AlloyDB V1ALPHA API - Class Google::Cloud::AlloyDB::V1alpha::AlloyDBAdmin::Rest::Client (v0.24.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:44:04.610888+00:00
---

# AlloyDB V1ALPHA API - Class Google::Cloud::AlloyDB::V1alpha::AlloyDBAdmin::Rest::Client (v0.24.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-AlloyDBAdmin-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  AlloyDB V1ALPHA API - Class Google::Cloud::AlloyDB::V1alpha::AlloyDBAdmin::Rest::Client (v0.24.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.24.0 (latest)  0.23.1  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.0  0.15.0  0.14.1  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.0  0.7.2  0.6.0  0.5.2  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the AlloyDB V1ALPHA API class Google::Cloud::AlloyDB::V1alpha::AlloyDBAdmin::Rest::Client.

REST client for the AlloyDBAdmin service.

Service describing handlers for resources

## Inherits

  * Object 



## Includes

  * [Google::Cloud::AlloyDB::V1alpha::AlloyDBAdmin::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-AlloyDBAdmin-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the AlloyDBAdmin Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-AlloyDBAdmin-Rest-Client-Configuration "Google::Cloud::AlloyDB::V1alpha::AlloyDBAdmin::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-AlloyDBAdmin-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-AlloyDBAdmin-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all AlloyDBAdmin clients
    ::Google::Cloud::AlloyDB::V1alpha::AlloyDBAdmin::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #batch_create_instances
    
    
    def batch_create_instances(request, options = nil) -> ::Gapic::Operation
    def batch_create_instances(parent: nil, requests: nil, request_id: nil) -> ::Gapic::Operation

Creates new instances under the given project, location and cluster. There can be only one primary instance in a cluster. If the primary instance exists in the cluster as well as this request, then API will throw an error. The primary instance should exist before any read pool instance is created. If the primary instance is a part of the request payload, then the API will take care of creating instances in the correct order. This method is here to support Google-internal use cases, and is not meant for external customers to consume. Please do not start relying on it; its behavior is subject to change without notice.

**Overloads**
    
    
    def batch_create_instances(request, options = nil) -> ::Gapic::Operation

Pass arguments to `batch_create_instances` via a request object, either of type [BatchCreateInstancesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-BatchCreateInstancesRequest "Google::Cloud::AlloyDB::V1alpha::BatchCreateInstancesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AlloyDB::V1alpha::BatchCreateInstancesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-BatchCreateInstancesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def batch_create_instances(parent: nil, requests: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `batch_create_instances` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The name of the parent resource. 
  * **requests** ([::Google::Cloud::AlloyDB::V1alpha::CreateInstanceRequests](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-CreateInstanceRequests), ::Hash) — Required. Resources being created. 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server ignores the request if it has already been completed. The server guarantees that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, ignores the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Operation) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/alloy_db/v1alpha"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AlloyDB::V1alpha::AlloyDBAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AlloyDB::V1alpha::BatchCreateInstancesRequest.new
    
    # Call the batch_create_instances method.
    result = client.batch_create_instances request
    
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

Configure the AlloyDBAdmin Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-AlloyDBAdmin-Rest-Client#Google__Cloud__AlloyDB__V1alpha__AlloyDBAdmin__Rest__Client_configure_class_ "Google::Cloud::AlloyDB::V1alpha::AlloyDBAdmin::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-AlloyDBAdmin-Rest-Client-Configuration "Google::Cloud::AlloyDB::V1alpha::AlloyDBAdmin::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-AlloyDBAdmin-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-AlloyDBAdmin-Rest-Client-Configuration)) 



### #create_backup
    
    
    def create_backup(request, options = nil) -> ::Gapic::Operation
    def create_backup(parent: nil, backup_id: nil, backup: nil, request_id: nil, validate_only: nil) -> ::Gapic::Operation

Creates a new Backup in a given project and location.

**Overloads**
    
    
    def create_backup(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_backup` via a request object, either of type [CreateBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-CreateBackupRequest "Google::Cloud::AlloyDB::V1alpha::CreateBackupRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AlloyDB::V1alpha::CreateBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-CreateBackupRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_backup(parent: nil, backup_id: nil, backup: nil, request_id: nil, validate_only: nil) -> ::Gapic::Operation

Pass arguments to `create_backup` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Value for parent. 
  * **backup_id** (::String) — Required. ID of the requesting object. 
  * **backup** ([::Google::Cloud::AlloyDB::V1alpha::Backup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-Backup), ::Hash) — Required. The resource being created 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server ignores the request if it has already been completed. The server guarantees that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, ignores the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

  * **validate_only** (::Boolean) — Optional. If set, the backend validates the request, but doesn't actually execute it. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Operation) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/alloy_db/v1alpha"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AlloyDB::V1alpha::AlloyDBAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AlloyDB::V1alpha::CreateBackupRequest.new
    
    # Call the create_backup method.
    result = client.create_backup request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #create_cluster
    
    
    def create_cluster(request, options = nil) -> ::Gapic::Operation
    def create_cluster(parent: nil, cluster_id: nil, cluster: nil, request_id: nil, validate_only: nil) -> ::Gapic::Operation

Creates a new Cluster in a given project and location.

**Overloads**
    
    
    def create_cluster(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_cluster` via a request object, either of type [CreateClusterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-CreateClusterRequest "Google::Cloud::AlloyDB::V1alpha::CreateClusterRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AlloyDB::V1alpha::CreateClusterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-CreateClusterRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_cluster(parent: nil, cluster_id: nil, cluster: nil, request_id: nil, validate_only: nil) -> ::Gapic::Operation

Pass arguments to `create_cluster` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The location of the new cluster. For the required format, see the comment on the Cluster.name field. 
  * **cluster_id** (::String) — Required. ID of the requesting object. 
  * **cluster** ([::Google::Cloud::AlloyDB::V1alpha::Cluster](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-Cluster), ::Hash) — Required. The resource being created 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server ignores the request if it has already been completed. The server guarantees that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, ignores the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

  * **validate_only** (::Boolean) — Optional. If set, performs request validation, for example, permission checks and any other type of validation, but does not actually execute the create request. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Operation) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/alloy_db/v1alpha"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AlloyDB::V1alpha::AlloyDBAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AlloyDB::V1alpha::CreateClusterRequest.new
    
    # Call the create_cluster method.
    result = client.create_cluster request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #create_database
    
    
    def create_database(request, options = nil) -> ::Google::Cloud::AlloyDB::V1alpha::Database
    def create_database(parent: nil, database_id: nil, database: nil) -> ::Google::Cloud::AlloyDB::V1alpha::Database

Creates a new Database in a given project, location, and cluster.

**Overloads**
    
    
    def create_database(request, options = nil) -> ::Google::Cloud::AlloyDB::V1alpha::Database

Pass arguments to `create_database` via a request object, either of type [CreateDatabaseRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-CreateDatabaseRequest "Google::Cloud::AlloyDB::V1alpha::CreateDatabaseRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AlloyDB::V1alpha::CreateDatabaseRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-CreateDatabaseRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_database(parent: nil, database_id: nil, database: nil) -> ::Google::Cloud::AlloyDB::V1alpha::Database

Pass arguments to `create_database` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Value for parent. 
  * **database_id** (::String) — Required. ID of the requesting object. 
  * **database** ([::Google::Cloud::AlloyDB::V1alpha::Database](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-Database), ::Hash) — Required. The resource being created. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AlloyDB::V1alpha::Database](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-Database)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AlloyDB::V1alpha::Database](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-Database)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/alloy_db/v1alpha"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AlloyDB::V1alpha::AlloyDBAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AlloyDB::V1alpha::CreateDatabaseRequest.new
    
    # Call the create_database method.
    result = client.create_database request
    
    # The returned object is of type Google::Cloud::AlloyDB::V1alpha::Database.
    p result

### #create_instance
    
    
    def create_instance(request, options = nil) -> ::Gapic::Operation
    def create_instance(parent: nil, instance_id: nil, instance: nil, request_id: nil, validate_only: nil) -> ::Gapic::Operation

Creates a new Instance in a given project and location.

**Overloads**
    
    
    def create_instance(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_instance` via a request object, either of type [CreateInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-CreateInstanceRequest "Google::Cloud::AlloyDB::V1alpha::CreateInstanceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AlloyDB::V1alpha::CreateInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-CreateInstanceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_instance(parent: nil, instance_id: nil, instance: nil, request_id: nil, validate_only: nil) -> ::Gapic::Operation

Pass arguments to `create_instance` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The name of the parent resource. For the required format, see the comment on the Instance.name field. 
  * **instance_id** (::String) — Required. ID of the requesting object. 
  * **instance** ([::Google::Cloud::AlloyDB::V1alpha::Instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-Instance), ::Hash) — Required. The resource being created 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server ignores the request if it has already been completed. The server guarantees that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, ignores the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

  * **validate_only** (::Boolean) — Optional. If set, performs request validation, for example, permission checks and any other type of validation, but does not actually execute the create request. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Operation) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/alloy_db/v1alpha"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AlloyDB::V1alpha::AlloyDBAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AlloyDB::V1alpha::CreateInstanceRequest.new
    
    # Call the create_instance method.
    result = client.create_instance request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #create_secondary_cluster
    
    
    def create_secondary_cluster(request, options = nil) -> ::Gapic::Operation
    def create_secondary_cluster(parent: nil, cluster_id: nil, cluster: nil, request_id: nil, validate_only: nil) -> ::Gapic::Operation

Creates a cluster of type SECONDARY in the given location using the primary cluster as the source.

**Overloads**
    
    
    def create_secondary_cluster(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_secondary_cluster` via a request object, either of type [CreateSecondaryClusterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-CreateSecondaryClusterRequest "Google::Cloud::AlloyDB::V1alpha::CreateSecondaryClusterRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AlloyDB::V1alpha::CreateSecondaryClusterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-CreateSecondaryClusterRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_secondary_cluster(parent: nil, cluster_id: nil, cluster: nil, request_id: nil, validate_only: nil) -> ::Gapic::Operation

Pass arguments to `create_secondary_cluster` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The location of the new cluster. For the required format, see the comment on the Cluster.name field. 
  * **cluster_id** (::String) — Required. ID of the requesting object (the secondary cluster). 
  * **cluster** ([::Google::Cloud::AlloyDB::V1alpha::Cluster](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-Cluster), ::Hash) — Required. Configuration of the requesting object (the secondary cluster). 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server ignores the request if it has already been completed. The server guarantees that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, ignores the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

  * **validate_only** (::Boolean) — Optional. If set, performs request validation, for example, permission checks and any other type of validation, but does not actually execute the create request. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Operation) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/alloy_db/v1alpha"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AlloyDB::V1alpha::AlloyDBAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AlloyDB::V1alpha::CreateSecondaryClusterRequest.new
    
    # Call the create_secondary_cluster method.
    result = client.create_secondary_cluster request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #create_secondary_instance
    
    
    def create_secondary_instance(request, options = nil) -> ::Gapic::Operation
    def create_secondary_instance(parent: nil, instance_id: nil, instance: nil, request_id: nil, validate_only: nil) -> ::Gapic::Operation

Creates a new SECONDARY Instance in a given project and location.

**Overloads**
    
    
    def create_secondary_instance(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_secondary_instance` via a request object, either of type [CreateSecondaryInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-CreateSecondaryInstanceRequest "Google::Cloud::AlloyDB::V1alpha::CreateSecondaryInstanceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AlloyDB::V1alpha::CreateSecondaryInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-CreateSecondaryInstanceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_secondary_instance(parent: nil, instance_id: nil, instance: nil, request_id: nil, validate_only: nil) -> ::Gapic::Operation

Pass arguments to `create_secondary_instance` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The name of the parent resource. For the required format, see the comment on the Instance.name field. 
  * **instance_id** (::String) — Required. ID of the requesting object. 
  * **instance** ([::Google::Cloud::AlloyDB::V1alpha::Instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-Instance), ::Hash) — Required. The resource being created 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server ignores the request if it has already been completed. The server guarantees that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, ignores the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

  * **validate_only** (::Boolean) — Optional. If set, performs request validation, for example, permission checks and any other type of validation, but does not actually execute the create request. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Operation) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/alloy_db/v1alpha"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AlloyDB::V1alpha::AlloyDBAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AlloyDB::V1alpha::CreateSecondaryInstanceRequest.new
    
    # Call the create_secondary_instance method.
    result = client.create_secondary_instance request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #create_user
    
    
    def create_user(request, options = nil) -> ::Google::Cloud::AlloyDB::V1alpha::User
    def create_user(parent: nil, user_id: nil, user: nil, request_id: nil, validate_only: nil) -> ::Google::Cloud::AlloyDB::V1alpha::User

Creates a new User in a given project, location, and cluster.

**Overloads**
    
    
    def create_user(request, options = nil) -> ::Google::Cloud::AlloyDB::V1alpha::User

Pass arguments to `create_user` via a request object, either of type [CreateUserRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-CreateUserRequest "Google::Cloud::AlloyDB::V1alpha::CreateUserRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AlloyDB::V1alpha::CreateUserRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-CreateUserRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_user(parent: nil, user_id: nil, user: nil, request_id: nil, validate_only: nil) -> ::Google::Cloud::AlloyDB::V1alpha::User

Pass arguments to `create_user` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Value for parent. 
  * **user_id** (::String) — Required. ID of the requesting object. 
  * **user** ([::Google::Cloud::AlloyDB::V1alpha::User](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-User), ::Hash) — Required. The resource being created 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server ignores the request if it has already been completed. The server guarantees that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, ignores the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

  * **validate_only** (::Boolean) — Optional. If set, the backend validates the request, but doesn't actually execute it. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AlloyDB::V1alpha::User](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-User)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AlloyDB::V1alpha::User](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-User)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/alloy_db/v1alpha"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AlloyDB::V1alpha::AlloyDBAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AlloyDB::V1alpha::CreateUserRequest.new
    
    # Call the create_user method.
    result = client.create_user request
    
    # The returned object is of type Google::Cloud::AlloyDB::V1alpha::User.
    p result

### #delete_backup
    
    
    def delete_backup(request, options = nil) -> ::Gapic::Operation
    def delete_backup(name: nil, request_id: nil, validate_only: nil, etag: nil) -> ::Gapic::Operation

Deletes a single Backup.

**Overloads**
    
    
    def delete_backup(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_backup` via a request object, either of type [DeleteBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-DeleteBackupRequest "Google::Cloud::AlloyDB::V1alpha::DeleteBackupRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AlloyDB::V1alpha::DeleteBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-DeleteBackupRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_backup(name: nil, request_id: nil, validate_only: nil, etag: nil) -> ::Gapic::Operation

Pass arguments to `delete_backup` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Name of the resource. For the required format, see the comment on the Backup.name field. 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server ignores the request if it has already been completed. The server guarantees that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, ignores the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

  * **validate_only** (::Boolean) — Optional. If set, the backend validates the request, but doesn't actually execute it. 
  * **etag** (::String) — Optional. The current etag of the Backup. If an etag is provided and does not match the current etag of the Backup, deletion will be blocked and an ABORTED error will be returned. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Operation) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/alloy_db/v1alpha"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AlloyDB::V1alpha::AlloyDBAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AlloyDB::V1alpha::DeleteBackupRequest.new
    
    # Call the delete_backup method.
    result = client.delete_backup request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_cluster
    
    
    def delete_cluster(request, options = nil) -> ::Gapic::Operation
    def delete_cluster(name: nil, request_id: nil, etag: nil, validate_only: nil, force: nil) -> ::Gapic::Operation

Deletes a single Cluster.

**Overloads**
    
    
    def delete_cluster(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_cluster` via a request object, either of type [DeleteClusterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-DeleteClusterRequest "Google::Cloud::AlloyDB::V1alpha::DeleteClusterRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AlloyDB::V1alpha::DeleteClusterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-DeleteClusterRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_cluster(name: nil, request_id: nil, etag: nil, validate_only: nil, force: nil) -> ::Gapic::Operation

Pass arguments to `delete_cluster` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the resource. For the required format, see the comment on the Cluster.name field. 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server ignores the request if it has already been completed. The server guarantees that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, ignores the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

  * **etag** (::String) — Optional. The current etag of the Cluster. If an etag is provided and does not match the current etag of the Cluster, deletion will be blocked and an ABORTED error will be returned. 
  * **validate_only** (::Boolean) — Optional. If set, performs request validation, for example, permission checks and any other type of validation, but does not actually execute the create request. 
  * **force** (::Boolean) — Optional. Whether to cascade delete child instances for given cluster. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Operation) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/alloy_db/v1alpha"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AlloyDB::V1alpha::AlloyDBAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AlloyDB::V1alpha::DeleteClusterRequest.new
    
    # Call the delete_cluster method.
    result = client.delete_cluster request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_instance
    
    
    def delete_instance(request, options = nil) -> ::Gapic::Operation
    def delete_instance(name: nil, request_id: nil, etag: nil, validate_only: nil) -> ::Gapic::Operation

Deletes a single Instance.

**Overloads**
    
    
    def delete_instance(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_instance` via a request object, either of type [DeleteInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-DeleteInstanceRequest "Google::Cloud::AlloyDB::V1alpha::DeleteInstanceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AlloyDB::V1alpha::DeleteInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-DeleteInstanceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_instance(name: nil, request_id: nil, etag: nil, validate_only: nil) -> ::Gapic::Operation

Pass arguments to `delete_instance` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the resource. For the required format, see the comment on the Instance.name field. 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server ignores the request if it has already been completed. The server guarantees that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, ignores the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

  * **etag** (::String) — Optional. The current etag of the Instance. If an etag is provided and does not match the current etag of the Instance, deletion will be blocked and an ABORTED error will be returned. 
  * **validate_only** (::Boolean) — Optional. If set, performs request validation, for example, permission checks and any other type of validation, but does not actually execute the create request. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Operation) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/alloy_db/v1alpha"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AlloyDB::V1alpha::AlloyDBAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AlloyDB::V1alpha::DeleteInstanceRequest.new
    
    # Call the delete_instance method.
    result = client.delete_instance request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_user
    
    
    def delete_user(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_user(name: nil, request_id: nil, validate_only: nil) -> ::Google::Protobuf::Empty

Deletes a single User.

**Overloads**
    
    
    def delete_user(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_user` via a request object, either of type [DeleteUserRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-DeleteUserRequest "Google::Cloud::AlloyDB::V1alpha::DeleteUserRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AlloyDB::V1alpha::DeleteUserRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-DeleteUserRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_user(name: nil, request_id: nil, validate_only: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_user` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the resource. For the required format, see the comment on the User.name field. 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server ignores the request if it has already been completed. The server guarantees that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, ignores the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

  * **validate_only** (::Boolean) — Optional. If set, the backend validates the request, but doesn't actually execute it. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/alloy_db/v1alpha"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AlloyDB::V1alpha::AlloyDBAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AlloyDB::V1alpha::DeleteUserRequest.new
    
    # Call the delete_user method.
    result = client.delete_user request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #execute_sql
    
    
    def execute_sql(request, options = nil) -> ::Google::Cloud::AlloyDB::V1alpha::ExecuteSqlResponse
    def execute_sql(password: nil, instance: nil, database: nil, user: nil, sql_statement: nil, validate_only: nil) -> ::Google::Cloud::AlloyDB::V1alpha::ExecuteSqlResponse

Executes a SQL statement in a database inside an AlloyDB instance.

**Overloads**
    
    
    def execute_sql(request, options = nil) -> ::Google::Cloud::AlloyDB::V1alpha::ExecuteSqlResponse

Pass arguments to `execute_sql` via a request object, either of type [ExecuteSqlRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-ExecuteSqlRequest "Google::Cloud::AlloyDB::V1alpha::ExecuteSqlRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AlloyDB::V1alpha::ExecuteSqlRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-ExecuteSqlRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def execute_sql(password: nil, instance: nil, database: nil, user: nil, sql_statement: nil, validate_only: nil) -> ::Google::Cloud::AlloyDB::V1alpha::ExecuteSqlResponse

Pass arguments to `execute_sql` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **password** (::String) — Optional. The database native user’s password. 
  * **instance** (::String) — Required. The instance where the SQL will be executed. For the required format, see the comment on the Instance.name field. 
  * **database** (::String) — Required. Name of the database where the query will be executed. Note - Value provided should be the same as expected from `SELECT current_database();` and NOT as a resource reference. 
  * **user** (::String) — Required. Database user to be used for executing the SQL. Note - Value provided should be the same as expected from `SELECT current_user;` and NOT as a resource reference. 
  * **sql_statement** (::String) — Required. SQL statement to execute on database. Any valid statement is permitted, including DDL, DML, DQL statements. 
  * **validate_only** (::Boolean) — Optional. If set, validates the sql statement by performing syntax and semantic validation and doesn't execute the query. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AlloyDB::V1alpha::ExecuteSqlResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-ExecuteSqlResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AlloyDB::V1alpha::ExecuteSqlResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-ExecuteSqlResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/alloy_db/v1alpha"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AlloyDB::V1alpha::AlloyDBAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AlloyDB::V1alpha::ExecuteSqlRequest.new
    
    # Call the execute_sql method.
    result = client.execute_sql request
    
    # The returned object is of type Google::Cloud::AlloyDB::V1alpha::ExecuteSqlResponse.
    p result

### #export_cluster
    
    
    def export_cluster(request, options = nil) -> ::Gapic::Operation
    def export_cluster(gcs_destination: nil, csv_export_options: nil, sql_export_options: nil, name: nil, database: nil) -> ::Gapic::Operation

Exports data from the cluster. Imperative only.

**Overloads**
    
    
    def export_cluster(request, options = nil) -> ::Gapic::Operation

Pass arguments to `export_cluster` via a request object, either of type [ExportClusterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-ExportClusterRequest "Google::Cloud::AlloyDB::V1alpha::ExportClusterRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AlloyDB::V1alpha::ExportClusterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-ExportClusterRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def export_cluster(gcs_destination: nil, csv_export_options: nil, sql_export_options: nil, name: nil, database: nil) -> ::Gapic::Operation

Pass arguments to `export_cluster` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **gcs_destination** ([::Google::Cloud::AlloyDB::V1alpha::GcsDestination](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-GcsDestination), ::Hash) — Required. Option to export data to cloud storage. 
  * **csv_export_options** ([::Google::Cloud::AlloyDB::V1alpha::ExportClusterRequest::CsvExportOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-ExportClusterRequest-CsvExportOptions), ::Hash) — Options for exporting data in CSV format. Required field to be set for CSV file type.

Note: The following parameters are mutually exclusive: `csv_export_options`, `sql_export_options`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **sql_export_options** ([::Google::Cloud::AlloyDB::V1alpha::ExportClusterRequest::SqlExportOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-ExportClusterRequest-SqlExportOptions), ::Hash) — Options for exporting data in SQL format. Required field to be set for SQL file type.

Note: The following parameters are mutually exclusive: `sql_export_options`, `csv_export_options`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **name** (::String) — Required. The resource name of the cluster. 
  * **database** (::String) — Required. Name of the database where the export command will be executed. Note - Value provided should be the same as expected from `SELECT current_database();` and NOT as a resource reference. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Operation) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/alloy_db/v1alpha"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AlloyDB::V1alpha::AlloyDBAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AlloyDB::V1alpha::ExportClusterRequest.new
    
    # Call the export_cluster method.
    result = client.export_cluster request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #failover_instance
    
    
    def failover_instance(request, options = nil) -> ::Gapic::Operation
    def failover_instance(name: nil, request_id: nil, validate_only: nil) -> ::Gapic::Operation

Forces a Failover for a highly available instance. Failover promotes the HA standby instance as the new primary. Imperative only.

**Overloads**
    
    
    def failover_instance(request, options = nil) -> ::Gapic::Operation

Pass arguments to `failover_instance` via a request object, either of type [FailoverInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-FailoverInstanceRequest "Google::Cloud::AlloyDB::V1alpha::FailoverInstanceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AlloyDB::V1alpha::FailoverInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-FailoverInstanceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def failover_instance(name: nil, request_id: nil, validate_only: nil) -> ::Gapic::Operation

Pass arguments to `failover_instance` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the resource. For the required format, see the comment on the Instance.name field. 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server ignores the request if it has already been completed. The server guarantees that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, ignores the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

  * **validate_only** (::Boolean) — Optional. If set, performs request validation, for example, permission checks and any other type of validation, but does not actually execute the create request. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Operation) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/alloy_db/v1alpha"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AlloyDB::V1alpha::AlloyDBAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AlloyDB::V1alpha::FailoverInstanceRequest.new
    
    # Call the failover_instance method.
    result = client.failover_instance request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #generate_client_certificate
    
    
    def generate_client_certificate(request, options = nil) -> ::Google::Cloud::AlloyDB::V1alpha::GenerateClientCertificateResponse
    def generate_client_certificate(parent: nil, request_id: nil, pem_csr: nil, cert_duration: nil, public_key: nil, use_metadata_exchange: nil) -> ::Google::Cloud::AlloyDB::V1alpha::GenerateClientCertificateResponse

Generate a client certificate signed by a Cluster CA. The sole purpose of this endpoint is to support AlloyDB connectors and the Auth Proxy client. The endpoint's behavior is subject to change without notice, so do not rely on its behavior remaining constant. Future changes will not break AlloyDB connectors or the Auth Proxy client.

**Overloads**
    
    
    def generate_client_certificate(request, options = nil) -> ::Google::Cloud::AlloyDB::V1alpha::GenerateClientCertificateResponse

Pass arguments to `generate_client_certificate` via a request object, either of type [GenerateClientCertificateRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-GenerateClientCertificateRequest "Google::Cloud::AlloyDB::V1alpha::GenerateClientCertificateRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AlloyDB::V1alpha::GenerateClientCertificateRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-GenerateClientCertificateRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def generate_client_certificate(parent: nil, request_id: nil, pem_csr: nil, cert_duration: nil, public_key: nil, use_metadata_exchange: nil) -> ::Google::Cloud::AlloyDB::V1alpha::GenerateClientCertificateResponse

Pass arguments to `generate_client_certificate` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — 

Required. The name of the parent resource. The required format is:

    * projects/{project}/locations/{location}/clusters/{cluster}
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server ignores the request if it has already been completed. The server guarantees that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, ignores the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

  * **pem_csr** (::String) — Optional. A pem-encoded X.509 certificate signing request (CSR). It is recommended to use public_key instead. 
  * **cert_duration** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Protobuf-Duration), ::Hash) — Optional. An optional hint to the endpoint to generate the client certificate with the requested duration. The duration can be from 1 hour to 24 hours. The endpoint may or may not honor the hint. If the hint is left unspecified or is not honored, then the endpoint will pick an appropriate default duration. 
  * **public_key** (::String) — Optional. The public key from the client. 
  * **use_metadata_exchange** (::Boolean) — Optional. An optional hint to the endpoint to generate a client certificate that can be used by AlloyDB connectors to exchange additional metadata with the server after TLS handshake. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AlloyDB::V1alpha::GenerateClientCertificateResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-GenerateClientCertificateResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AlloyDB::V1alpha::GenerateClientCertificateResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-GenerateClientCertificateResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/alloy_db/v1alpha"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AlloyDB::V1alpha::AlloyDBAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AlloyDB::V1alpha::GenerateClientCertificateRequest.new
    
    # Call the generate_client_certificate method.
    result = client.generate_client_certificate request
    
    # The returned object is of type Google::Cloud::AlloyDB::V1alpha::GenerateClientCertificateResponse.
    p result

### #get_backup
    
    
    def get_backup(request, options = nil) -> ::Google::Cloud::AlloyDB::V1alpha::Backup
    def get_backup(name: nil) -> ::Google::Cloud::AlloyDB::V1alpha::Backup

Gets details of a single Backup.

**Overloads**
    
    
    def get_backup(request, options = nil) -> ::Google::Cloud::AlloyDB::V1alpha::Backup

Pass arguments to `get_backup` via a request object, either of type [GetBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-GetBackupRequest "Google::Cloud::AlloyDB::V1alpha::GetBackupRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AlloyDB::V1alpha::GetBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-GetBackupRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_backup(name: nil) -> ::Google::Cloud::AlloyDB::V1alpha::Backup

Pass arguments to `get_backup` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Name of the resource 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AlloyDB::V1alpha::Backup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-Backup)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AlloyDB::V1alpha::Backup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-Backup)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/alloy_db/v1alpha"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AlloyDB::V1alpha::AlloyDBAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AlloyDB::V1alpha::GetBackupRequest.new
    
    # Call the get_backup method.
    result = client.get_backup request
    
    # The returned object is of type Google::Cloud::AlloyDB::V1alpha::Backup.
    p result

### #get_cluster
    
    
    def get_cluster(request, options = nil) -> ::Google::Cloud::AlloyDB::V1alpha::Cluster
    def get_cluster(name: nil, view: nil) -> ::Google::Cloud::AlloyDB::V1alpha::Cluster

Gets details of a single Cluster.

**Overloads**
    
    
    def get_cluster(request, options = nil) -> ::Google::Cloud::AlloyDB::V1alpha::Cluster

Pass arguments to `get_cluster` via a request object, either of type [GetClusterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-GetClusterRequest "Google::Cloud::AlloyDB::V1alpha::GetClusterRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AlloyDB::V1alpha::GetClusterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-GetClusterRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_cluster(name: nil, view: nil) -> ::Google::Cloud::AlloyDB::V1alpha::Cluster

Pass arguments to `get_cluster` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the resource. For the required format, see the comment on the Cluster.name field. 
  * **view** ([::Google::Cloud::AlloyDB::V1alpha::ClusterView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-ClusterView)) — Optional. The view of the cluster to return. Returns all default fields if not set. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AlloyDB::V1alpha::Cluster](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-Cluster)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AlloyDB::V1alpha::Cluster](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-Cluster)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/alloy_db/v1alpha"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AlloyDB::V1alpha::AlloyDBAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AlloyDB::V1alpha::GetClusterRequest.new
    
    # Call the get_cluster method.
    result = client.get_cluster request
    
    # The returned object is of type Google::Cloud::AlloyDB::V1alpha::Cluster.
    p result

### #get_connection_info
    
    
    def get_connection_info(request, options = nil) -> ::Google::Cloud::AlloyDB::V1alpha::ConnectionInfo
    def get_connection_info(parent: nil, request_id: nil) -> ::Google::Cloud::AlloyDB::V1alpha::ConnectionInfo

Get instance metadata used for a connection.

**Overloads**
    
    
    def get_connection_info(request, options = nil) -> ::Google::Cloud::AlloyDB::V1alpha::ConnectionInfo

Pass arguments to `get_connection_info` via a request object, either of type [GetConnectionInfoRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-GetConnectionInfoRequest "Google::Cloud::AlloyDB::V1alpha::GetConnectionInfoRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AlloyDB::V1alpha::GetConnectionInfoRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-GetConnectionInfoRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_connection_info(parent: nil, request_id: nil) -> ::Google::Cloud::AlloyDB::V1alpha::ConnectionInfo

Pass arguments to `get_connection_info` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The name of the parent resource. The required format is: projects/{project}/locations/{location}/clusters/{cluster}/instances/{instance} 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server ignores the request if it has already been completed. The server guarantees that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, ignores the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AlloyDB::V1alpha::ConnectionInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-ConnectionInfo)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AlloyDB::V1alpha::ConnectionInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-ConnectionInfo)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/alloy_db/v1alpha"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AlloyDB::V1alpha::AlloyDBAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AlloyDB::V1alpha::GetConnectionInfoRequest.new
    
    # Call the get_connection_info method.
    result = client.get_connection_info request
    
    # The returned object is of type Google::Cloud::AlloyDB::V1alpha::ConnectionInfo.
    p result

### #get_instance
    
    
    def get_instance(request, options = nil) -> ::Google::Cloud::AlloyDB::V1alpha::Instance
    def get_instance(name: nil, view: nil) -> ::Google::Cloud::AlloyDB::V1alpha::Instance

Gets details of a single Instance.

**Overloads**
    
    
    def get_instance(request, options = nil) -> ::Google::Cloud::AlloyDB::V1alpha::Instance

Pass arguments to `get_instance` via a request object, either of type [GetInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-GetInstanceRequest "Google::Cloud::AlloyDB::V1alpha::GetInstanceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AlloyDB::V1alpha::GetInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-GetInstanceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_instance(name: nil, view: nil) -> ::Google::Cloud::AlloyDB::V1alpha::Instance

Pass arguments to `get_instance` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the resource. For the required format, see the comment on the Instance.name field. 
  * **view** ([::Google::Cloud::AlloyDB::V1alpha::InstanceView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-InstanceView)) — The view of the instance to return. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AlloyDB::V1alpha::Instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-Instance)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AlloyDB::V1alpha::Instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-Instance)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/alloy_db/v1alpha"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AlloyDB::V1alpha::AlloyDBAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AlloyDB::V1alpha::GetInstanceRequest.new
    
    # Call the get_instance method.
    result = client.get_instance request
    
    # The returned object is of type Google::Cloud::AlloyDB::V1alpha::Instance.
    p result

### #get_user
    
    
    def get_user(request, options = nil) -> ::Google::Cloud::AlloyDB::V1alpha::User
    def get_user(name: nil) -> ::Google::Cloud::AlloyDB::V1alpha::User

Gets details of a single User.

**Overloads**
    
    
    def get_user(request, options = nil) -> ::Google::Cloud::AlloyDB::V1alpha::User

Pass arguments to `get_user` via a request object, either of type [GetUserRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-GetUserRequest "Google::Cloud::AlloyDB::V1alpha::GetUserRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AlloyDB::V1alpha::GetUserRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-GetUserRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_user(name: nil) -> ::Google::Cloud::AlloyDB::V1alpha::User

Pass arguments to `get_user` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the resource. For the required format, see the comment on the User.name field. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AlloyDB::V1alpha::User](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-User)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AlloyDB::V1alpha::User](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-User)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/alloy_db/v1alpha"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AlloyDB::V1alpha::AlloyDBAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AlloyDB::V1alpha::GetUserRequest.new
    
    # Call the get_user method.
    result = client.get_user request
    
    # The returned object is of type Google::Cloud::AlloyDB::V1alpha::User.
    p result

### #iam_policy_client
    
    
    def iam_policy_client() -> Google::Iam::V1::IAMPolicy::Rest::Client

Get the associated client for mix-in of the IAMPolicy.

**Returns**

  * (Google::Iam::V1::IAMPolicy::Rest::Client) 



### #import_cluster
    
    
    def import_cluster(request, options = nil) -> ::Gapic::Operation
    def import_cluster(sql_import_options: nil, csv_import_options: nil, name: nil, gcs_uri: nil, database: nil, user: nil) -> ::Gapic::Operation

Imports data to the cluster. Imperative only.

**Overloads**
    
    
    def import_cluster(request, options = nil) -> ::Gapic::Operation

Pass arguments to `import_cluster` via a request object, either of type [ImportClusterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-ImportClusterRequest "Google::Cloud::AlloyDB::V1alpha::ImportClusterRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AlloyDB::V1alpha::ImportClusterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-ImportClusterRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def import_cluster(sql_import_options: nil, csv_import_options: nil, name: nil, gcs_uri: nil, database: nil, user: nil) -> ::Gapic::Operation

Pass arguments to `import_cluster` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **sql_import_options** ([::Google::Cloud::AlloyDB::V1alpha::ImportClusterRequest::SqlImportOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-ImportClusterRequest-SqlImportOptions), ::Hash) — Options for importing data in SQL format.

Note: The following parameters are mutually exclusive: `sql_import_options`, `csv_import_options`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **csv_import_options** ([::Google::Cloud::AlloyDB::V1alpha::ImportClusterRequest::CsvImportOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-ImportClusterRequest-CsvImportOptions), ::Hash) — Options for importing data in CSV format.

Note: The following parameters are mutually exclusive: `csv_import_options`, `sql_import_options`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **name** (::String) — Required. The resource name of the cluster. 
  * **gcs_uri** (::String) — Required. The path to the file in Google Cloud Storage where the source file for import will be stored. The URI is in the form `gs://bucketName/fileName`. 
  * **database** (::String) — Optional. Name of the database to which the import will be done. For import from SQL file, this is required only if the file does not specify a database. Note - Value provided should be the same as expected from `SELECT current_database();` and NOT as a resource reference. 
  * **user** (::String) — Optional. Database user to be used for importing the data. Note - Value provided should be the same as expected from `SELECT current_user;` and NOT as a resource reference. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Operation) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/alloy_db/v1alpha"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AlloyDB::V1alpha::AlloyDBAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AlloyDB::V1alpha::ImportClusterRequest.new
    
    # Call the import_cluster method.
    result = client.import_cluster request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new AlloyDBAdmin REST client object.

**Yields**

  * (config) — Configure the AlloyDBAdmin client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-AlloyDBAdmin-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-AlloyDBAdmin-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::AlloyDB::V1alpha::AlloyDBAdmin::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::AlloyDB::V1alpha::AlloyDBAdmin::Rest::Client.new do |config|
      config.timeout = 10.0
    end

### #inject_fault
    
    
    def inject_fault(request, options = nil) -> ::Gapic::Operation
    def inject_fault(fault_type: nil, name: nil, request_id: nil, validate_only: nil) -> ::Gapic::Operation

Injects fault in an instance. Imperative only.

**Overloads**
    
    
    def inject_fault(request, options = nil) -> ::Gapic::Operation

Pass arguments to `inject_fault` via a request object, either of type [InjectFaultRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-InjectFaultRequest "Google::Cloud::AlloyDB::V1alpha::InjectFaultRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AlloyDB::V1alpha::InjectFaultRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-InjectFaultRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def inject_fault(fault_type: nil, name: nil, request_id: nil, validate_only: nil) -> ::Gapic::Operation

Pass arguments to `inject_fault` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **fault_type** ([::Google::Cloud::AlloyDB::V1alpha::InjectFaultRequest::FaultType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-InjectFaultRequest-FaultType)) — Required. The type of fault to be injected in an instance. 
  * **name** (::String) — Required. The name of the resource. For the required format, see the comment on the Instance.name field. 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server ignores the request if it has already been completed. The server guarantees that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, ignores the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

  * **validate_only** (::Boolean) — Optional. If set, performs request validation, for example, permission checks and any other type of validation, but does not actually execute the create request. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Operation) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/alloy_db/v1alpha"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AlloyDB::V1alpha::AlloyDBAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AlloyDB::V1alpha::InjectFaultRequest.new
    
    # Call the inject_fault method.
    result = client.inject_fault request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #list_backups
    
    
    def list_backups(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AlloyDB::V1alpha::Backup>
    def list_backups(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AlloyDB::V1alpha::Backup>

Lists Backups in a given project and location.

**Overloads**
    
    
    def list_backups(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AlloyDB::V1alpha::Backup>

Pass arguments to `list_backups` via a request object, either of type [ListBackupsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-ListBackupsRequest "Google::Cloud::AlloyDB::V1alpha::ListBackupsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AlloyDB::V1alpha::ListBackupsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-ListBackupsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_backups(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AlloyDB::V1alpha::Backup>

Pass arguments to `list_backups` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Parent value for ListBackupsRequest 
  * **page_size** (::Integer) — Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default. 
  * **page_token** (::String) — A token identifying a page of results the server should return. 
  * **filter** (::String) — Filtering results 
  * **order_by** (::String) — Hint for how to order the results 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::AlloyDB::V1alpha::Backup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-Backup)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::AlloyDB::V1alpha::Backup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-Backup)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/alloy_db/v1alpha"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AlloyDB::V1alpha::AlloyDBAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AlloyDB::V1alpha::ListBackupsRequest.new
    
    # Call the list_backups method.
    result = client.list_backups request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::AlloyDB::V1alpha::Backup.
      p item
    end

### #list_clusters
    
    
    def list_clusters(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AlloyDB::V1alpha::Cluster>
    def list_clusters(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AlloyDB::V1alpha::Cluster>

Lists Clusters in a given project and location.

**Overloads**
    
    
    def list_clusters(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AlloyDB::V1alpha::Cluster>

Pass arguments to `list_clusters` via a request object, either of type [ListClustersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-ListClustersRequest "Google::Cloud::AlloyDB::V1alpha::ListClustersRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AlloyDB::V1alpha::ListClustersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-ListClustersRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_clusters(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AlloyDB::V1alpha::Cluster>

Pass arguments to `list_clusters` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — 

Required. The name of the parent resource. For the required format, see the comment on the Cluster.name field. Additionally, you can perform an aggregated list operation by specifying a value with the following format:

    * projects/{project}/locations/-
  * **page_size** (::Integer) — Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default. 
  * **page_token** (::String) — A token identifying a page of results the server should return. 
  * **filter** (::String) — Optional. Filtering results 
  * **order_by** (::String) — Optional. Hint for how to order the results 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::AlloyDB::V1alpha::Cluster](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-Cluster)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::AlloyDB::V1alpha::Cluster](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-Cluster)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/alloy_db/v1alpha"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AlloyDB::V1alpha::AlloyDBAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AlloyDB::V1alpha::ListClustersRequest.new
    
    # Call the list_clusters method.
    result = client.list_clusters request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::AlloyDB::V1alpha::Cluster.
      p item
    end

### #list_databases
    
    
    def list_databases(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AlloyDB::V1alpha::Database>
    def list_databases(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AlloyDB::V1alpha::Database>

Lists Databases in a given project and location.

**Overloads**
    
    
    def list_databases(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AlloyDB::V1alpha::Database>

Pass arguments to `list_databases` via a request object, either of type [ListDatabasesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-ListDatabasesRequest "Google::Cloud::AlloyDB::V1alpha::ListDatabasesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AlloyDB::V1alpha::ListDatabasesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-ListDatabasesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_databases(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AlloyDB::V1alpha::Database>

Pass arguments to `list_databases` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Parent value for ListDatabasesRequest. 
  * **page_size** (::Integer) — Optional. The maximum number of databases to return. The service may return fewer than this value. If unspecified, 2000 is the default page_size. The max value of page_size will be 4000, values above max will be coerced to max. 
  * **page_token** (::String) — Optional. A page token, received from a previous `ListDatabases` call. This should be provided to retrieve the subsequent page. This field is currently not supported, its value will be ignored if passed. 
  * **filter** (::String) — Optional. Filtering results. This field is currently not supported, its value will be ignored if passed. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::AlloyDB::V1alpha::Database](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-Database)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::AlloyDB::V1alpha::Database](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-Database)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/alloy_db/v1alpha"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AlloyDB::V1alpha::AlloyDBAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AlloyDB::V1alpha::ListDatabasesRequest.new
    
    # Call the list_databases method.
    result = client.list_databases request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::AlloyDB::V1alpha::Database.
      p item
    end

### #list_instances
    
    
    def list_instances(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AlloyDB::V1alpha::Instance>
    def list_instances(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AlloyDB::V1alpha::Instance>

Lists Instances in a given project and location.

**Overloads**
    
    
    def list_instances(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AlloyDB::V1alpha::Instance>

Pass arguments to `list_instances` via a request object, either of type [ListInstancesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-ListInstancesRequest "Google::Cloud::AlloyDB::V1alpha::ListInstancesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AlloyDB::V1alpha::ListInstancesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-ListInstancesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_instances(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AlloyDB::V1alpha::Instance>

Pass arguments to `list_instances` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — 

Required. The name of the parent resource. For the required format, see the comment on the Instance.name field. Additionally, you can perform an aggregated list operation by specifying a value with one of the following formats:

    * projects/{project}/locations/-/clusters/-
    * projects/{project}/locations/{region}/clusters/-
  * **page_size** (::Integer) — Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default. 
  * **page_token** (::String) — A token identifying a page of results the server should return. 
  * **filter** (::String) — Optional. Filtering results 
  * **order_by** (::String) — Optional. Hint for how to order the results 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::AlloyDB::V1alpha::Instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-Instance)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::AlloyDB::V1alpha::Instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-Instance)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/alloy_db/v1alpha"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AlloyDB::V1alpha::AlloyDBAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AlloyDB::V1alpha::ListInstancesRequest.new
    
    # Call the list_instances method.
    result = client.list_instances request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::AlloyDB::V1alpha::Instance.
      p item
    end

### #list_supported_database_flags
    
    
    def list_supported_database_flags(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AlloyDB::V1alpha::SupportedDatabaseFlag>
    def list_supported_database_flags(parent: nil, page_size: nil, page_token: nil, scope: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AlloyDB::V1alpha::SupportedDatabaseFlag>

Lists SupportedDatabaseFlags for a given project and location.

**Overloads**
    
    
    def list_supported_database_flags(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AlloyDB::V1alpha::SupportedDatabaseFlag>

Pass arguments to `list_supported_database_flags` via a request object, either of type [ListSupportedDatabaseFlagsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-ListSupportedDatabaseFlagsRequest "Google::Cloud::AlloyDB::V1alpha::ListSupportedDatabaseFlagsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AlloyDB::V1alpha::ListSupportedDatabaseFlagsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-ListSupportedDatabaseFlagsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_supported_database_flags(parent: nil, page_size: nil, page_token: nil, scope: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AlloyDB::V1alpha::SupportedDatabaseFlag>

Pass arguments to `list_supported_database_flags` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The name of the parent resource. The required format is:

    * projects/{project}/locations/{location}

Regardless of the parent specified here, as long it is contains a valid project and location, the service will return a static list of supported flags resources. Note that we do not yet support region-specific flags. 

  * **page_size** (::Integer) — Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default. 
  * **page_token** (::String) — A token identifying a page of results the server should return. 
  * **scope** ([::Google::Cloud::AlloyDB::V1alpha::SupportedDatabaseFlag::Scope](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-SupportedDatabaseFlag-Scope)) — Optional. The scope for which supported flags are requested. If not specified, default is DATABASE. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::AlloyDB::V1alpha::SupportedDatabaseFlag](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-SupportedDatabaseFlag)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::AlloyDB::V1alpha::SupportedDatabaseFlag](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-SupportedDatabaseFlag)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/alloy_db/v1alpha"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AlloyDB::V1alpha::AlloyDBAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AlloyDB::V1alpha::ListSupportedDatabaseFlagsRequest.new
    
    # Call the list_supported_database_flags method.
    result = client.list_supported_database_flags request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::AlloyDB::V1alpha::SupportedDatabaseFlag.
      p item
    end

### #list_users
    
    
    def list_users(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AlloyDB::V1alpha::User>
    def list_users(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AlloyDB::V1alpha::User>

Lists Users in a given project and location.

**Overloads**
    
    
    def list_users(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AlloyDB::V1alpha::User>

Pass arguments to `list_users` via a request object, either of type [ListUsersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-ListUsersRequest "Google::Cloud::AlloyDB::V1alpha::ListUsersRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AlloyDB::V1alpha::ListUsersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-ListUsersRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_users(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AlloyDB::V1alpha::User>

Pass arguments to `list_users` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Parent value for ListUsersRequest 
  * **page_size** (::Integer) — Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default. 
  * **page_token** (::String) — Optional. A token identifying a page of results the server should return. 
  * **filter** (::String) — Optional. Filtering results 
  * **order_by** (::String) — Optional. Hint for how to order the results 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::AlloyDB::V1alpha::User](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-User)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::AlloyDB::V1alpha::User](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-User)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/alloy_db/v1alpha"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AlloyDB::V1alpha::AlloyDBAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AlloyDB::V1alpha::ListUsersRequest.new
    
    # Call the list_users method.
    result = client.list_users request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::AlloyDB::V1alpha::User.
      p item
    end

### #location_client
    
    
    def location_client() -> Google::Cloud::Location::Locations::Rest::Client

Get the associated client for mix-in of the Locations.

**Returns**

  * (Google::Cloud::Location::Locations::Rest::Client) 



### #logger
    
    
    def logger() -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #operations_client
    
    
    def operations_client() -> ::Google::Cloud::AlloyDB::V1alpha::AlloyDBAdmin::Rest::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::AlloyDB::V1alpha::AlloyDBAdmin::Rest::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-AlloyDBAdmin-Rest-Operations)) 



### #promote_cluster
    
    
    def promote_cluster(request, options = nil) -> ::Gapic::Operation
    def promote_cluster(name: nil, request_id: nil, etag: nil, validate_only: nil) -> ::Gapic::Operation

Promotes a SECONDARY cluster. This turns down replication from the PRIMARY cluster and promotes a secondary cluster into its own standalone cluster. Imperative only.

**Overloads**
    
    
    def promote_cluster(request, options = nil) -> ::Gapic::Operation

Pass arguments to `promote_cluster` via a request object, either of type [PromoteClusterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-PromoteClusterRequest "Google::Cloud::AlloyDB::V1alpha::PromoteClusterRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AlloyDB::V1alpha::PromoteClusterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-PromoteClusterRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def promote_cluster(name: nil, request_id: nil, etag: nil, validate_only: nil) -> ::Gapic::Operation

Pass arguments to `promote_cluster` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the resource. For the required format, see the comment on the Cluster.name field 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server ignores the request if it has already been completed. The server guarantees that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

  * **etag** (::String) — Optional. The current etag of the Cluster. If an etag is provided and does not match the current etag of the Cluster, deletion will be blocked and an ABORTED error will be returned. 
  * **validate_only** (::Boolean) — Optional. If set, performs request validation, for example, permission checks and any other type of validation, but does not actually execute the create request. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Operation) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/alloy_db/v1alpha"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AlloyDB::V1alpha::AlloyDBAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AlloyDB::V1alpha::PromoteClusterRequest.new
    
    # Call the promote_cluster method.
    result = client.promote_cluster request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #restart_instance
    
    
    def restart_instance(request, options = nil) -> ::Gapic::Operation
    def restart_instance(name: nil, request_id: nil, validate_only: nil, node_ids: nil) -> ::Gapic::Operation

Restart an Instance in a cluster. Imperative only.

**Overloads**
    
    
    def restart_instance(request, options = nil) -> ::Gapic::Operation

Pass arguments to `restart_instance` via a request object, either of type [RestartInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-RestartInstanceRequest "Google::Cloud::AlloyDB::V1alpha::RestartInstanceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AlloyDB::V1alpha::RestartInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-RestartInstanceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def restart_instance(name: nil, request_id: nil, validate_only: nil, node_ids: nil) -> ::Gapic::Operation

Pass arguments to `restart_instance` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the resource. For the required format, see the comment on the Instance.name field. 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server ignores the request if it has already been completed. The server guarantees that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, ignores the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

  * **validate_only** (::Boolean) — Optional. If set, performs request validation, for example, permission checks and any other type of validation, but does not actually execute the create request. 
  * **node_ids** (::Array<::String>) — Optional. Full name of the nodes as obtained from INSTANCE_VIEW_FULL to restart upon. Applicable only to read instances. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Operation) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/alloy_db/v1alpha"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AlloyDB::V1alpha::AlloyDBAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AlloyDB::V1alpha::RestartInstanceRequest.new
    
    # Call the restart_instance method.
    result = client.restart_instance request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #restore_cluster
    
    
    def restore_cluster(request, options = nil) -> ::Gapic::Operation
    def restore_cluster(backup_source: nil, continuous_backup_source: nil, parent: nil, cluster_id: nil, cluster: nil, request_id: nil, validate_only: nil) -> ::Gapic::Operation

Creates a new Cluster in a given project and location, with a volume restored from the provided source, either a backup ID or a point-in-time and a source cluster.

**Overloads**
    
    
    def restore_cluster(request, options = nil) -> ::Gapic::Operation

Pass arguments to `restore_cluster` via a request object, either of type [RestoreClusterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-RestoreClusterRequest "Google::Cloud::AlloyDB::V1alpha::RestoreClusterRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AlloyDB::V1alpha::RestoreClusterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-RestoreClusterRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def restore_cluster(backup_source: nil, continuous_backup_source: nil, parent: nil, cluster_id: nil, cluster: nil, request_id: nil, validate_only: nil) -> ::Gapic::Operation

Pass arguments to `restore_cluster` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **backup_source** ([::Google::Cloud::AlloyDB::V1alpha::BackupSource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-BackupSource), ::Hash) — Backup source.

Note: The following parameters are mutually exclusive: `backup_source`, `continuous_backup_source`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **continuous_backup_source** ([::Google::Cloud::AlloyDB::V1alpha::ContinuousBackupSource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-ContinuousBackupSource), ::Hash) — ContinuousBackup source. Continuous backup needs to be enabled in the source cluster for this operation to succeed.

Note: The following parameters are mutually exclusive: `continuous_backup_source`, `backup_source`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **parent** (::String) — Required. The name of the parent resource. For the required format, see the comment on the Cluster.name field. 
  * **cluster_id** (::String) — Required. ID of the requesting object. 
  * **cluster** ([::Google::Cloud::AlloyDB::V1alpha::Cluster](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-Cluster), ::Hash) — Required. The resource being created 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server ignores the request if it has already been completed. The server guarantees that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, ignores the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

  * **validate_only** (::Boolean) — Optional. If set, performs request validation, for example, permission checks and any other type of validation, but does not actually execute the create request. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Operation) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/alloy_db/v1alpha"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AlloyDB::V1alpha::AlloyDBAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AlloyDB::V1alpha::RestoreClusterRequest.new
    
    # Call the restore_cluster method.
    result = client.restore_cluster request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #switchover_cluster
    
    
    def switchover_cluster(request, options = nil) -> ::Gapic::Operation
    def switchover_cluster(name: nil, request_id: nil, validate_only: nil) -> ::Gapic::Operation

Switches the roles of PRIMARY and SECONDARY clusters without any data loss. This promotes the SECONDARY cluster to PRIMARY and sets up the original PRIMARY cluster to replicate from this newly promoted cluster.

**Overloads**
    
    
    def switchover_cluster(request, options = nil) -> ::Gapic::Operation

Pass arguments to `switchover_cluster` via a request object, either of type [SwitchoverClusterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-SwitchoverClusterRequest "Google::Cloud::AlloyDB::V1alpha::SwitchoverClusterRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AlloyDB::V1alpha::SwitchoverClusterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-SwitchoverClusterRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def switchover_cluster(name: nil, request_id: nil, validate_only: nil) -> ::Gapic::Operation

Pass arguments to `switchover_cluster` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the resource. For the required format, see the comment on the Cluster.name field 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server ignores the request if it has already been completed. The server guarantees that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, ignores the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

  * **validate_only** (::Boolean) — Optional. If set, performs request validation, for example, permission checks and any other type of validation, but does not actually execute the create request. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Operation) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/alloy_db/v1alpha"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AlloyDB::V1alpha::AlloyDBAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AlloyDB::V1alpha::SwitchoverClusterRequest.new
    
    # Call the switchover_cluster method.
    result = client.switchover_cluster request
    
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



### #update_backup
    
    
    def update_backup(request, options = nil) -> ::Gapic::Operation
    def update_backup(update_mask: nil, backup: nil, request_id: nil, validate_only: nil, allow_missing: nil) -> ::Gapic::Operation

Updates the parameters of a single Backup.

**Overloads**
    
    
    def update_backup(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_backup` via a request object, either of type [UpdateBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-UpdateBackupRequest "Google::Cloud::AlloyDB::V1alpha::UpdateBackupRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AlloyDB::V1alpha::UpdateBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-UpdateBackupRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_backup(update_mask: nil, backup: nil, request_id: nil, validate_only: nil, allow_missing: nil) -> ::Gapic::Operation

Pass arguments to `update_backup` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. Field mask is used to specify the fields to be overwritten in the Backup resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. 
  * **backup** ([::Google::Cloud::AlloyDB::V1alpha::Backup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-Backup), ::Hash) — Required. The resource being updated 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server ignores the request if it has already been completed. The server guarantees that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, ignores the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

  * **validate_only** (::Boolean) — Optional. If set, the backend validates the request, but doesn't actually execute it. 
  * **allow_missing** (::Boolean) — Optional. If set to true, update succeeds even if instance is not found. In that case, a new backup is created and `update_mask` is ignored. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Operation) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/alloy_db/v1alpha"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AlloyDB::V1alpha::AlloyDBAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AlloyDB::V1alpha::UpdateBackupRequest.new
    
    # Call the update_backup method.
    result = client.update_backup request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #update_cluster
    
    
    def update_cluster(request, options = nil) -> ::Gapic::Operation
    def update_cluster(update_mask: nil, cluster: nil, request_id: nil, validate_only: nil, allow_missing: nil) -> ::Gapic::Operation

Updates the parameters of a single Cluster.

**Overloads**
    
    
    def update_cluster(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_cluster` via a request object, either of type [UpdateClusterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-UpdateClusterRequest "Google::Cloud::AlloyDB::V1alpha::UpdateClusterRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AlloyDB::V1alpha::UpdateClusterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-UpdateClusterRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_cluster(update_mask: nil, cluster: nil, request_id: nil, validate_only: nil, allow_missing: nil) -> ::Gapic::Operation

Pass arguments to `update_cluster` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. Field mask is used to specify the fields to be overwritten in the Cluster resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. 
  * **cluster** ([::Google::Cloud::AlloyDB::V1alpha::Cluster](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-Cluster), ::Hash) — Required. The resource being updated 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server ignores the request if it has already been completed. The server guarantees that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, ignores the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

  * **validate_only** (::Boolean) — Optional. If set, performs request validation, for example, permission checks and any other type of validation, but does not actually execute the create request. 
  * **allow_missing** (::Boolean) — Optional. If set to true, update succeeds even if cluster is not found. In that case, a new cluster is created and `update_mask` is ignored. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Operation) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/alloy_db/v1alpha"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AlloyDB::V1alpha::AlloyDBAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AlloyDB::V1alpha::UpdateClusterRequest.new
    
    # Call the update_cluster method.
    result = client.update_cluster request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #update_instance
    
    
    def update_instance(request, options = nil) -> ::Gapic::Operation
    def update_instance(update_mask: nil, instance: nil, request_id: nil, validate_only: nil, allow_missing: nil) -> ::Gapic::Operation

Updates the parameters of a single Instance.

**Overloads**
    
    
    def update_instance(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_instance` via a request object, either of type [UpdateInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-UpdateInstanceRequest "Google::Cloud::AlloyDB::V1alpha::UpdateInstanceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AlloyDB::V1alpha::UpdateInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-UpdateInstanceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_instance(update_mask: nil, instance: nil, request_id: nil, validate_only: nil, allow_missing: nil) -> ::Gapic::Operation

Pass arguments to `update_instance` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. Field mask is used to specify the fields to be overwritten in the Instance resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. 
  * **instance** ([::Google::Cloud::AlloyDB::V1alpha::Instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-Instance), ::Hash) — Required. The resource being updated 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server ignores the request if it has already been completed. The server guarantees that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, ignores the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

  * **validate_only** (::Boolean) — Optional. If set, performs request validation, for example, permission checks and any other type of validation, but does not actually execute the create request. 
  * **allow_missing** (::Boolean) — Optional. If set to true, update succeeds even if instance is not found. In that case, a new instance is created and `update_mask` is ignored. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Operation) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/alloy_db/v1alpha"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AlloyDB::V1alpha::AlloyDBAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AlloyDB::V1alpha::UpdateInstanceRequest.new
    
    # Call the update_instance method.
    result = client.update_instance request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #update_user
    
    
    def update_user(request, options = nil) -> ::Google::Cloud::AlloyDB::V1alpha::User
    def update_user(update_mask: nil, user: nil, request_id: nil, validate_only: nil, allow_missing: nil) -> ::Google::Cloud::AlloyDB::V1alpha::User

Updates the parameters of a single User.

**Overloads**
    
    
    def update_user(request, options = nil) -> ::Google::Cloud::AlloyDB::V1alpha::User

Pass arguments to `update_user` via a request object, either of type [UpdateUserRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-UpdateUserRequest "Google::Cloud::AlloyDB::V1alpha::UpdateUserRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AlloyDB::V1alpha::UpdateUserRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-UpdateUserRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_user(update_mask: nil, user: nil, request_id: nil, validate_only: nil, allow_missing: nil) -> ::Google::Cloud::AlloyDB::V1alpha::User

Pass arguments to `update_user` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. Field mask is used to specify the fields to be overwritten in the User resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. 
  * **user** ([::Google::Cloud::AlloyDB::V1alpha::User](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-User), ::Hash) — Required. The resource being updated 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server ignores the request if it has already been completed. The server guarantees that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, ignores the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

  * **validate_only** (::Boolean) — Optional. If set, the backend validates the request, but doesn't actually execute it. 
  * **allow_missing** (::Boolean) — Optional. Allow missing fields in the update mask. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AlloyDB::V1alpha::User](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-User)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AlloyDB::V1alpha::User](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-User)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/alloy_db/v1alpha"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AlloyDB::V1alpha::AlloyDBAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AlloyDB::V1alpha::UpdateUserRequest.new
    
    # Call the update_user method.
    result = client.update_user request
    
    # The returned object is of type Google::Cloud::AlloyDB::V1alpha::User.
    p result

### #upgrade_cluster
    
    
    def upgrade_cluster(request, options = nil) -> ::Gapic::Operation
    def upgrade_cluster(name: nil, version: nil, request_id: nil, validate_only: nil, etag: nil) -> ::Gapic::Operation

Upgrades a single Cluster. Imperative only.

**Overloads**
    
    
    def upgrade_cluster(request, options = nil) -> ::Gapic::Operation

Pass arguments to `upgrade_cluster` via a request object, either of type [UpgradeClusterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-UpgradeClusterRequest "Google::Cloud::AlloyDB::V1alpha::UpgradeClusterRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AlloyDB::V1alpha::UpgradeClusterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-UpgradeClusterRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def upgrade_cluster(name: nil, version: nil, request_id: nil, validate_only: nil, etag: nil) -> ::Gapic::Operation

Pass arguments to `upgrade_cluster` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The resource name of the cluster. 
  * **version** ([::Google::Cloud::AlloyDB::V1alpha::DatabaseVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-DatabaseVersion)) — Required. The version the cluster is going to be upgraded to. 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server ignores the request if it has already been completed. The server guarantees that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, ignores the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

  * **validate_only** (::Boolean) — Optional. If set, performs request validation, for example, permission checks and any other type of validation, but does not actually execute the create request. 
  * **etag** (::String) — Optional. The current etag of the Cluster. If an etag is provided and does not match the current etag of the Cluster, upgrade will be blocked and an ABORTED error will be returned. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Operation) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/alloy_db/v1alpha"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AlloyDB::V1alpha::AlloyDBAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AlloyDB::V1alpha::UpgradeClusterRequest.new
    
    # Call the upgrade_cluster method.
    result = client.upgrade_cluster request
    
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
