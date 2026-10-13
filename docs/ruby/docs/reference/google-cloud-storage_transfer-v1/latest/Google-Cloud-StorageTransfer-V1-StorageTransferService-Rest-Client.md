---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-StorageTransferService-Rest-Client/
title: Storage Transfer Service V1 API - Class Google::Cloud::StorageTransfer::V1::StorageTransferService::Rest::Client (v1.11.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:55:22.680270+00:00
---

# Storage Transfer Service V1 API - Class Google::Cloud::StorageTransfer::V1::StorageTransferService::Rest::Client (v1.11.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-StorageTransferService-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Storage Transfer Service V1 API - Class Google::Cloud::StorageTransfer::V1::StorageTransferService::Rest::Client (v1.11.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.11.1 (latest)  1.11.0  1.10.0  1.9.0  1.8.1  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.1  1.0.0  0.10.0  0.9.2  0.8.0  0.7.0  0.6.1  0.5.0  0.4.0  0.3.0  0.2.0  0.1.2 

Reference documentation and code samples for the Storage Transfer Service V1 API class Google::Cloud::StorageTransfer::V1::StorageTransferService::Rest::Client.

REST client for the StorageTransferService service.

Storage Transfer Service and its protos. Transfers data between between Google Cloud Storage buckets or from a data source external to Google to a Cloud Storage bucket.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::StorageTransfer::V1::StorageTransferService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-StorageTransferService-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the StorageTransferService Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-StorageTransferService-Rest-Client-Configuration "Google::Cloud::StorageTransfer::V1::StorageTransferService::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-StorageTransferService-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-StorageTransferService-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all StorageTransferService clients
    ::Google::Cloud::StorageTransfer::V1::StorageTransferService::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the StorageTransferService Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-StorageTransferService-Rest-Client#Google__Cloud__StorageTransfer__V1__StorageTransferService__Rest__Client_configure_class_ "Google::Cloud::StorageTransfer::V1::StorageTransferService::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-StorageTransferService-Rest-Client-Configuration "Google::Cloud::StorageTransfer::V1::StorageTransferService::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-StorageTransferService-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-StorageTransferService-Rest-Client-Configuration)) 



### #create_agent_pool
    
    
    def create_agent_pool(request, options = nil) -> ::Google::Cloud::StorageTransfer::V1::AgentPool
    def create_agent_pool(project_id: nil, agent_pool: nil, agent_pool_id: nil) -> ::Google::Cloud::StorageTransfer::V1::AgentPool

Creates an agent pool resource.

**Overloads**
    
    
    def create_agent_pool(request, options = nil) -> ::Google::Cloud::StorageTransfer::V1::AgentPool

Pass arguments to `create_agent_pool` via a request object, either of type [CreateAgentPoolRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-CreateAgentPoolRequest "Google::Cloud::StorageTransfer::V1::CreateAgentPoolRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::StorageTransfer::V1::CreateAgentPoolRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-CreateAgentPoolRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_agent_pool(project_id: nil, agent_pool: nil, agent_pool_id: nil) -> ::Google::Cloud::StorageTransfer::V1::AgentPool

Pass arguments to `create_agent_pool` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **project_id** (::String) — Required. The ID of the Google Cloud project that owns the agent pool. 
  * **agent_pool** ([::Google::Cloud::StorageTransfer::V1::AgentPool](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-AgentPool), ::Hash) — Required. The agent pool to create. 
  * **agent_pool_id** (::String) — Required. The ID of the agent pool to create.

The `agent_pool_id` must meet the following requirements:

    * Length of 128 characters or less.
    * Not start with the string `goog`.
    * Start with a lowercase ASCII character, followed by: 
      * Zero or more: lowercase Latin alphabet characters, numerals, hyphens (`-`), periods (`.`), underscores (`_`), or tildes (`~`).
      * One or more numerals or lowercase ASCII characters.

As expressed by the regular expression: `^(?!goog)[a-z]([a-z0-9-._~]*[a-z0-9])?$`. 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::StorageTransfer::V1::AgentPool](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-AgentPool)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::StorageTransfer::V1::AgentPool](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-AgentPool)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/storage_transfer/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::StorageTransfer::V1::StorageTransferService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::StorageTransfer::V1::CreateAgentPoolRequest.new
    
    # Call the create_agent_pool method.
    result = client.create_agent_pool request
    
    # The returned object is of type Google::Cloud::StorageTransfer::V1::AgentPool.
    p result

### #create_transfer_job
    
    
    def create_transfer_job(request, options = nil) -> ::Google::Cloud::StorageTransfer::V1::TransferJob
    def create_transfer_job(transfer_job: nil) -> ::Google::Cloud::StorageTransfer::V1::TransferJob

Creates a transfer job that runs periodically.

**Overloads**
    
    
    def create_transfer_job(request, options = nil) -> ::Google::Cloud::StorageTransfer::V1::TransferJob

Pass arguments to `create_transfer_job` via a request object, either of type [CreateTransferJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-CreateTransferJobRequest "Google::Cloud::StorageTransfer::V1::CreateTransferJobRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::StorageTransfer::V1::CreateTransferJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-CreateTransferJobRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_transfer_job(transfer_job: nil) -> ::Google::Cloud::StorageTransfer::V1::TransferJob

Pass arguments to `create_transfer_job` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **transfer_job** ([::Google::Cloud::StorageTransfer::V1::TransferJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob), ::Hash) — Required. The job to create. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::StorageTransfer::V1::TransferJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::StorageTransfer::V1::TransferJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/storage_transfer/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::StorageTransfer::V1::StorageTransferService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::StorageTransfer::V1::CreateTransferJobRequest.new
    
    # Call the create_transfer_job method.
    result = client.create_transfer_job request
    
    # The returned object is of type Google::Cloud::StorageTransfer::V1::TransferJob.
    p result

### #delete_agent_pool
    
    
    def delete_agent_pool(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_agent_pool(name: nil) -> ::Google::Protobuf::Empty

Deletes an agent pool.

**Overloads**
    
    
    def delete_agent_pool(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_agent_pool` via a request object, either of type [DeleteAgentPoolRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-DeleteAgentPoolRequest "Google::Cloud::StorageTransfer::V1::DeleteAgentPoolRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::StorageTransfer::V1::DeleteAgentPoolRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-DeleteAgentPoolRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_agent_pool(name: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_agent_pool` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the agent pool to delete. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/storage_transfer/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::StorageTransfer::V1::StorageTransferService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::StorageTransfer::V1::DeleteAgentPoolRequest.new
    
    # Call the delete_agent_pool method.
    result = client.delete_agent_pool request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #delete_transfer_job
    
    
    def delete_transfer_job(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_transfer_job(job_name: nil, project_id: nil) -> ::Google::Protobuf::Empty

Deletes a transfer job. Deleting a transfer job sets its status to [DELETED](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob-Status#Google__Cloud__StorageTransfer__V1__TransferJob__Status__DELETED "Google::Cloud::StorageTransfer::V1::TransferJob::Status::DELETED \(constant\)").

**Overloads**
    
    
    def delete_transfer_job(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_transfer_job` via a request object, either of type [DeleteTransferJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-DeleteTransferJobRequest "Google::Cloud::StorageTransfer::V1::DeleteTransferJobRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::StorageTransfer::V1::DeleteTransferJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-DeleteTransferJobRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_transfer_job(job_name: nil, project_id: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_transfer_job` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **job_name** (::String) — Required. The job to delete. 
  * **project_id** (::String) — Required. The ID of the Google Cloud project that owns the job. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/storage_transfer/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::StorageTransfer::V1::StorageTransferService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::StorageTransfer::V1::DeleteTransferJobRequest.new
    
    # Call the delete_transfer_job method.
    result = client.delete_transfer_job request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #get_agent_pool
    
    
    def get_agent_pool(request, options = nil) -> ::Google::Cloud::StorageTransfer::V1::AgentPool
    def get_agent_pool(name: nil) -> ::Google::Cloud::StorageTransfer::V1::AgentPool

Gets an agent pool.

**Overloads**
    
    
    def get_agent_pool(request, options = nil) -> ::Google::Cloud::StorageTransfer::V1::AgentPool

Pass arguments to `get_agent_pool` via a request object, either of type [GetAgentPoolRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-GetAgentPoolRequest "Google::Cloud::StorageTransfer::V1::GetAgentPoolRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::StorageTransfer::V1::GetAgentPoolRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-GetAgentPoolRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_agent_pool(name: nil) -> ::Google::Cloud::StorageTransfer::V1::AgentPool

Pass arguments to `get_agent_pool` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the agent pool to get. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::StorageTransfer::V1::AgentPool](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-AgentPool)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::StorageTransfer::V1::AgentPool](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-AgentPool)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/storage_transfer/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::StorageTransfer::V1::StorageTransferService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::StorageTransfer::V1::GetAgentPoolRequest.new
    
    # Call the get_agent_pool method.
    result = client.get_agent_pool request
    
    # The returned object is of type Google::Cloud::StorageTransfer::V1::AgentPool.
    p result

### #get_google_service_account
    
    
    def get_google_service_account(request, options = nil) -> ::Google::Cloud::StorageTransfer::V1::GoogleServiceAccount
    def get_google_service_account(project_id: nil) -> ::Google::Cloud::StorageTransfer::V1::GoogleServiceAccount

Returns the Google service account that is used by Storage Transfer Service to access buckets in the project where transfers run or in other projects. Each Google service account is associated with one Google Cloud project. Users should add this service account to the Google Cloud Storage bucket ACLs to grant access to Storage Transfer Service. This service account is created and owned by Storage Transfer Service and can only be used by Storage Transfer Service.

**Overloads**
    
    
    def get_google_service_account(request, options = nil) -> ::Google::Cloud::StorageTransfer::V1::GoogleServiceAccount

Pass arguments to `get_google_service_account` via a request object, either of type [GetGoogleServiceAccountRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-GetGoogleServiceAccountRequest "Google::Cloud::StorageTransfer::V1::GetGoogleServiceAccountRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::StorageTransfer::V1::GetGoogleServiceAccountRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-GetGoogleServiceAccountRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_google_service_account(project_id: nil) -> ::Google::Cloud::StorageTransfer::V1::GoogleServiceAccount

Pass arguments to `get_google_service_account` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **project_id** (::String) — Required. The ID of the Google Cloud project that the Google service account is associated with. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::StorageTransfer::V1::GoogleServiceAccount](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-GoogleServiceAccount)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::StorageTransfer::V1::GoogleServiceAccount](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-GoogleServiceAccount)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/storage_transfer/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::StorageTransfer::V1::StorageTransferService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::StorageTransfer::V1::GetGoogleServiceAccountRequest.new
    
    # Call the get_google_service_account method.
    result = client.get_google_service_account request
    
    # The returned object is of type Google::Cloud::StorageTransfer::V1::GoogleServiceAccount.
    p result

### #get_transfer_job
    
    
    def get_transfer_job(request, options = nil) -> ::Google::Cloud::StorageTransfer::V1::TransferJob
    def get_transfer_job(job_name: nil, project_id: nil) -> ::Google::Cloud::StorageTransfer::V1::TransferJob

Gets a transfer job.

**Overloads**
    
    
    def get_transfer_job(request, options = nil) -> ::Google::Cloud::StorageTransfer::V1::TransferJob

Pass arguments to `get_transfer_job` via a request object, either of type [GetTransferJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-GetTransferJobRequest "Google::Cloud::StorageTransfer::V1::GetTransferJobRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::StorageTransfer::V1::GetTransferJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-GetTransferJobRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_transfer_job(job_name: nil, project_id: nil) -> ::Google::Cloud::StorageTransfer::V1::TransferJob

Pass arguments to `get_transfer_job` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **job_name** (::String) — Required. The job to get. 
  * **project_id** (::String) — Required. The ID of the Google Cloud project that owns the job. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::StorageTransfer::V1::TransferJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::StorageTransfer::V1::TransferJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/storage_transfer/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::StorageTransfer::V1::StorageTransferService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::StorageTransfer::V1::GetTransferJobRequest.new
    
    # Call the get_transfer_job method.
    result = client.get_transfer_job request
    
    # The returned object is of type Google::Cloud::StorageTransfer::V1::TransferJob.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new StorageTransferService REST client object.

**Yields**

  * (config) — Configure the StorageTransferService client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-StorageTransferService-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-StorageTransferService-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::StorageTransfer::V1::StorageTransferService::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::StorageTransfer::V1::StorageTransferService::Rest::Client.new do |config|
      config.timeout = 10.0
    end

### #list_agent_pools
    
    
    def list_agent_pools(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::StorageTransfer::V1::AgentPool>
    def list_agent_pools(project_id: nil, filter: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::StorageTransfer::V1::AgentPool>

Lists agent pools.

**Overloads**
    
    
    def list_agent_pools(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::StorageTransfer::V1::AgentPool>

Pass arguments to `list_agent_pools` via a request object, either of type [ListAgentPoolsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-ListAgentPoolsRequest "Google::Cloud::StorageTransfer::V1::ListAgentPoolsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::StorageTransfer::V1::ListAgentPoolsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-ListAgentPoolsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_agent_pools(project_id: nil, filter: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::StorageTransfer::V1::AgentPool>

Pass arguments to `list_agent_pools` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **project_id** (::String) — Required. The ID of the Google Cloud project that owns the job. 
  * **filter** (::String) — An optional list of query parameters specified as JSON text in the form of:

`{"agentPoolNames":["agentpool1","agentpool2",...]}`

Since `agentPoolNames` support multiple values, its values must be specified with array notation. When the filter is either empty or not provided, the list returns all agent pools for the project. 

  * **page_size** (::Integer) — The list page size. The max allowed value is `256`. 
  * **page_token** (::String) — The list page token. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::StorageTransfer::V1::AgentPool](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-AgentPool)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::StorageTransfer::V1::AgentPool](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-AgentPool)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/storage_transfer/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::StorageTransfer::V1::StorageTransferService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::StorageTransfer::V1::ListAgentPoolsRequest.new
    
    # Call the list_agent_pools method.
    result = client.list_agent_pools request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::StorageTransfer::V1::AgentPool.
      p item
    end

### #list_transfer_jobs
    
    
    def list_transfer_jobs(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::StorageTransfer::V1::TransferJob>
    def list_transfer_jobs(filter: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::StorageTransfer::V1::TransferJob>

Lists transfer jobs.

**Overloads**
    
    
    def list_transfer_jobs(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::StorageTransfer::V1::TransferJob>

Pass arguments to `list_transfer_jobs` via a request object, either of type [ListTransferJobsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-ListTransferJobsRequest "Google::Cloud::StorageTransfer::V1::ListTransferJobsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::StorageTransfer::V1::ListTransferJobsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-ListTransferJobsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_transfer_jobs(filter: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::StorageTransfer::V1::TransferJob>

Pass arguments to `list_transfer_jobs` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **filter** (::String) — 

Required. A list of query parameters specified as JSON text in the form of:

` { "projectId":"my_project_id", "jobNames":["jobid1","jobid2",...], "jobStatuses":["status1","status2",...], "dataBackend":"QUERY_REPLICATION_CONFIGS", "sourceBucket":"source-bucket-name", "sinkBucket":"sink-bucket-name", } `

The JSON formatting in the example is for display only; provide the query parameters without spaces or line breaks.

    * `projectId` is required.
    * Since `jobNames` and `jobStatuses` support multiple values, their values must be specified with array notation. `jobNames` and `jobStatuses` are optional. Valid values are case-insensitive: 
      * [ENABLED](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob-Status#Google__Cloud__StorageTransfer__V1__TransferJob__Status__ENABLED "Google::Cloud::StorageTransfer::V1::TransferJob::Status::ENABLED \(constant\)")
      * [DISABLED](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob-Status#Google__Cloud__StorageTransfer__V1__TransferJob__Status__DISABLED "Google::Cloud::StorageTransfer::V1::TransferJob::Status::DISABLED \(constant\)")
      * [DELETED](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob-Status#Google__Cloud__StorageTransfer__V1__TransferJob__Status__DELETED "Google::Cloud::StorageTransfer::V1::TransferJob::Status::DELETED \(constant\)")
    * Specify `"dataBackend":"QUERY_REPLICATION_CONFIGS"` to return a list of cross-bucket replication jobs.
    * Limit the results to jobs from a particular bucket with `sourceBucket` and/or to a particular bucket with `sinkBucket`.
  * **page_size** (::Integer) — The list page size. The max allowed value is 256. 
  * **page_token** (::String) — The list page token. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::StorageTransfer::V1::TransferJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::StorageTransfer::V1::TransferJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/storage_transfer/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::StorageTransfer::V1::StorageTransferService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::StorageTransfer::V1::ListTransferJobsRequest.new
    
    # Call the list_transfer_jobs method.
    result = client.list_transfer_jobs request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::StorageTransfer::V1::TransferJob.
      p item
    end

### #logger
    
    
    def logger() -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #operations_client
    
    
    def operations_client() -> ::Google::Cloud::StorageTransfer::V1::StorageTransferService::Rest::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::StorageTransfer::V1::StorageTransferService::Rest::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-StorageTransferService-Rest-Operations)) 



### #pause_transfer_operation
    
    
    def pause_transfer_operation(request, options = nil) -> ::Google::Protobuf::Empty
    def pause_transfer_operation(name: nil) -> ::Google::Protobuf::Empty

Pauses a transfer operation.

**Overloads**
    
    
    def pause_transfer_operation(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `pause_transfer_operation` via a request object, either of type [PauseTransferOperationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-PauseTransferOperationRequest "Google::Cloud::StorageTransfer::V1::PauseTransferOperationRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::StorageTransfer::V1::PauseTransferOperationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-PauseTransferOperationRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def pause_transfer_operation(name: nil) -> ::Google::Protobuf::Empty

Pass arguments to `pause_transfer_operation` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the transfer operation. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/storage_transfer/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::StorageTransfer::V1::StorageTransferService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::StorageTransfer::V1::PauseTransferOperationRequest.new
    
    # Call the pause_transfer_operation method.
    result = client.pause_transfer_operation request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #resume_transfer_operation
    
    
    def resume_transfer_operation(request, options = nil) -> ::Google::Protobuf::Empty
    def resume_transfer_operation(name: nil) -> ::Google::Protobuf::Empty

Resumes a transfer operation that is paused.

**Overloads**
    
    
    def resume_transfer_operation(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `resume_transfer_operation` via a request object, either of type [ResumeTransferOperationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-ResumeTransferOperationRequest "Google::Cloud::StorageTransfer::V1::ResumeTransferOperationRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::StorageTransfer::V1::ResumeTransferOperationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-ResumeTransferOperationRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def resume_transfer_operation(name: nil) -> ::Google::Protobuf::Empty

Pass arguments to `resume_transfer_operation` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the transfer operation. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/storage_transfer/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::StorageTransfer::V1::StorageTransferService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::StorageTransfer::V1::ResumeTransferOperationRequest.new
    
    # Call the resume_transfer_operation method.
    result = client.resume_transfer_operation request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #run_transfer_job
    
    
    def run_transfer_job(request, options = nil) -> ::Gapic::Operation
    def run_transfer_job(job_name: nil, project_id: nil) -> ::Gapic::Operation

Starts a new operation for the specified transfer job. A `TransferJob` has a maximum of one active `TransferOperation`. If this method is called while a `TransferOperation` is active, an error is returned.

**Overloads**
    
    
    def run_transfer_job(request, options = nil) -> ::Gapic::Operation

Pass arguments to `run_transfer_job` via a request object, either of type [RunTransferJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-RunTransferJobRequest "Google::Cloud::StorageTransfer::V1::RunTransferJobRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::StorageTransfer::V1::RunTransferJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-RunTransferJobRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def run_transfer_job(job_name: nil, project_id: nil) -> ::Gapic::Operation

Pass arguments to `run_transfer_job` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **job_name** (::String) — Required. The name of the transfer job. 
  * **project_id** (::String) — Required. The ID of the Google Cloud project that owns the transfer job. 



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
    
    
    require "google/cloud/storage_transfer/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::StorageTransfer::V1::StorageTransferService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::StorageTransfer::V1::RunTransferJobRequest.new
    
    # Call the run_transfer_job method.
    result = client.run_transfer_job request
    
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



### #update_agent_pool
    
    
    def update_agent_pool(request, options = nil) -> ::Google::Cloud::StorageTransfer::V1::AgentPool
    def update_agent_pool(agent_pool: nil, update_mask: nil) -> ::Google::Cloud::StorageTransfer::V1::AgentPool

Updates an existing agent pool resource.

**Overloads**
    
    
    def update_agent_pool(request, options = nil) -> ::Google::Cloud::StorageTransfer::V1::AgentPool

Pass arguments to `update_agent_pool` via a request object, either of type [UpdateAgentPoolRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-UpdateAgentPoolRequest "Google::Cloud::StorageTransfer::V1::UpdateAgentPoolRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::StorageTransfer::V1::UpdateAgentPoolRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-UpdateAgentPoolRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_agent_pool(agent_pool: nil, update_mask: nil) -> ::Google::Cloud::StorageTransfer::V1::AgentPool

Pass arguments to `update_agent_pool` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **agent_pool** ([::Google::Cloud::StorageTransfer::V1::AgentPool](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-AgentPool), ::Hash) — 

Required. The agent pool to update. `agent_pool` is expected to specify following fields:

    * [name](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-AgentPool#Google__Cloud__StorageTransfer__V1__AgentPool_name_instance_ "Google::Cloud::StorageTransfer::V1::AgentPool#name \(method\)")

    * [display_name](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-AgentPool#Google__Cloud__StorageTransfer__V1__AgentPool_display_name_instance_ "Google::Cloud::StorageTransfer::V1::AgentPool#display_name \(method\)")

    * [bandwidth_limit](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-AgentPool#Google__Cloud__StorageTransfer__V1__AgentPool_bandwidth_limit_instance_ "Google::Cloud::StorageTransfer::V1::AgentPool#bandwidth_limit \(method\)") An `UpdateAgentPoolRequest` with any other fields is rejected with the error [INVALID_ARGUMENT](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Rpc-Code#Google__Rpc__Code__INVALID_ARGUMENT "Google::Rpc::Code::INVALID_ARGUMENT \(constant\)").

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Protobuf-FieldMask), ::Hash) — 

The [field mask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf) of the fields in `agentPool` to update in this request. The following `agentPool` fields can be updated:

    * [display_name](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-AgentPool#Google__Cloud__StorageTransfer__V1__AgentPool_display_name_instance_ "Google::Cloud::StorageTransfer::V1::AgentPool#display_name \(method\)")

    * [bandwidth_limit](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-AgentPool#Google__Cloud__StorageTransfer__V1__AgentPool_bandwidth_limit_instance_ "Google::Cloud::StorageTransfer::V1::AgentPool#bandwidth_limit \(method\)")




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::StorageTransfer::V1::AgentPool](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-AgentPool)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::StorageTransfer::V1::AgentPool](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-AgentPool)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/storage_transfer/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::StorageTransfer::V1::StorageTransferService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::StorageTransfer::V1::UpdateAgentPoolRequest.new
    
    # Call the update_agent_pool method.
    result = client.update_agent_pool request
    
    # The returned object is of type Google::Cloud::StorageTransfer::V1::AgentPool.
    p result

### #update_transfer_job
    
    
    def update_transfer_job(request, options = nil) -> ::Google::Cloud::StorageTransfer::V1::TransferJob
    def update_transfer_job(job_name: nil, project_id: nil, transfer_job: nil, update_transfer_job_field_mask: nil) -> ::Google::Cloud::StorageTransfer::V1::TransferJob

Updates a transfer job. Updating a job's transfer spec does not affect transfer operations that are running already.

**Note:** The job's [status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob#Google__Cloud__StorageTransfer__V1__TransferJob_status_instance_ "Google::Cloud::StorageTransfer::V1::TransferJob#status \(method\)") field can be modified using this RPC (for example, to set a job's status to [DELETED](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob-Status#Google__Cloud__StorageTransfer__V1__TransferJob__Status__DELETED "Google::Cloud::StorageTransfer::V1::TransferJob::Status::DELETED \(constant\)"), [DISABLED](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob-Status#Google__Cloud__StorageTransfer__V1__TransferJob__Status__DISABLED "Google::Cloud::StorageTransfer::V1::TransferJob::Status::DISABLED \(constant\)"), or [ENABLED](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob-Status#Google__Cloud__StorageTransfer__V1__TransferJob__Status__ENABLED "Google::Cloud::StorageTransfer::V1::TransferJob::Status::ENABLED \(constant\)")).

**Overloads**
    
    
    def update_transfer_job(request, options = nil) -> ::Google::Cloud::StorageTransfer::V1::TransferJob

Pass arguments to `update_transfer_job` via a request object, either of type [UpdateTransferJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-UpdateTransferJobRequest "Google::Cloud::StorageTransfer::V1::UpdateTransferJobRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::StorageTransfer::V1::UpdateTransferJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-UpdateTransferJobRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_transfer_job(job_name: nil, project_id: nil, transfer_job: nil, update_transfer_job_field_mask: nil) -> ::Google::Cloud::StorageTransfer::V1::TransferJob

Pass arguments to `update_transfer_job` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **job_name** (::String) — Required. The name of job to update. 
  * **project_id** (::String) — Required. The ID of the Google Cloud project that owns the job. 
  * **transfer_job** ([::Google::Cloud::StorageTransfer::V1::TransferJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob), ::Hash) — Required. The job to update. `transferJob` is expected to specify one or more of five fields: [description](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob#Google__Cloud__StorageTransfer__V1__TransferJob_description_instance_ "Google::Cloud::StorageTransfer::V1::TransferJob#description \(method\)"), [transfer_spec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob#Google__Cloud__StorageTransfer__V1__TransferJob_transfer_spec_instance_ "Google::Cloud::StorageTransfer::V1::TransferJob#transfer_spec \(method\)"), [notification_config](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob#Google__Cloud__StorageTransfer__V1__TransferJob_notification_config_instance_ "Google::Cloud::StorageTransfer::V1::TransferJob#notification_config \(method\)"), [logging_config](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob#Google__Cloud__StorageTransfer__V1__TransferJob_logging_config_instance_ "Google::Cloud::StorageTransfer::V1::TransferJob#logging_config \(method\)"), and [status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob#Google__Cloud__StorageTransfer__V1__TransferJob_status_instance_ "Google::Cloud::StorageTransfer::V1::TransferJob#status \(method\)"). An `UpdateTransferJobRequest` that specifies other fields are rejected with the error [INVALID_ARGUMENT](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Rpc-Code#Google__Rpc__Code__INVALID_ARGUMENT "Google::Rpc::Code::INVALID_ARGUMENT \(constant\)"). Updating a job status to [DELETED](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob-Status#Google__Cloud__StorageTransfer__V1__TransferJob__Status__DELETED "Google::Cloud::StorageTransfer::V1::TransferJob::Status::DELETED \(constant\)") requires `storagetransfer.jobs.delete` permission. 
  * **update_transfer_job_field_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Protobuf-FieldMask), ::Hash) — The field mask of the fields in `transferJob` that are to be updated in this request. Fields in `transferJob` that can be updated are: [description](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob#Google__Cloud__StorageTransfer__V1__TransferJob_description_instance_ "Google::Cloud::StorageTransfer::V1::TransferJob#description \(method\)"), [transfer_spec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob#Google__Cloud__StorageTransfer__V1__TransferJob_transfer_spec_instance_ "Google::Cloud::StorageTransfer::V1::TransferJob#transfer_spec \(method\)"), [notification_config](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob#Google__Cloud__StorageTransfer__V1__TransferJob_notification_config_instance_ "Google::Cloud::StorageTransfer::V1::TransferJob#notification_config \(method\)"), [logging_config](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob#Google__Cloud__StorageTransfer__V1__TransferJob_logging_config_instance_ "Google::Cloud::StorageTransfer::V1::TransferJob#logging_config \(method\)"), and [status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob#Google__Cloud__StorageTransfer__V1__TransferJob_status_instance_ "Google::Cloud::StorageTransfer::V1::TransferJob#status \(method\)"). To update the `transfer_spec` of the job, a complete transfer specification must be provided. An incomplete specification missing any required fields is rejected with the error [INVALID_ARGUMENT](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Rpc-Code#Google__Rpc__Code__INVALID_ARGUMENT "Google::Rpc::Code::INVALID_ARGUMENT \(constant\)"). 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::StorageTransfer::V1::TransferJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::StorageTransfer::V1::TransferJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/storage_transfer/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::StorageTransfer::V1::StorageTransferService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::StorageTransfer::V1::UpdateTransferJobRequest.new
    
    # Call the update_transfer_job method.
    result = client.update_transfer_job request
    
    # The returned object is of type Google::Cloud::StorageTransfer::V1::TransferJob.
    p result

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
