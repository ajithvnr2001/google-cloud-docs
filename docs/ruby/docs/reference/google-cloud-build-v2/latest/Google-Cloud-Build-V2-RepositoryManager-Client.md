---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-RepositoryManager-Client/
title: Cloud Build V2 API - Class Google::Cloud::Build::V2::RepositoryManager::Client (v0.14.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:53:48.977496+00:00
---

# Cloud Build V2 API - Class Google::Cloud::Build::V2::RepositoryManager::Client (v0.14.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-RepositoryManager-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Build V2 API - Class Google::Cloud::Build::V2::RepositoryManager::Client (v0.14.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.14.2 (latest)  0.14.1  0.13.0  0.12.1  0.11.0  0.10.0  0.9.1  0.8.0  0.7.2  0.6.0  0.5.2  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Cloud Build V2 API class Google::Cloud::Build::V2::RepositoryManager::Client.

Client for the RepositoryManager service.

Manages connections to source code repositories.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::Build::V2::RepositoryManager::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-RepositoryManager-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the RepositoryManager Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-RepositoryManager-Client-Configuration "Google::Cloud::Build::V2::RepositoryManager::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-RepositoryManager-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-RepositoryManager-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all RepositoryManager clients
    ::Google::Cloud::Build::V2::RepositoryManager::Client.configure do |config|
      config.timeout = 10.0
    end

### #batch_create_repositories
    
    
    def batch_create_repositories(request, options = nil) -> ::Gapic::Operation
    def batch_create_repositories(parent: nil, requests: nil) -> ::Gapic::Operation

Creates multiple repositories inside a connection.

**Overloads**
    
    
    def batch_create_repositories(request, options = nil) -> ::Gapic::Operation

Pass arguments to `batch_create_repositories` via a request object, either of type [BatchCreateRepositoriesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-BatchCreateRepositoriesRequest "Google::Cloud::Build::V2::BatchCreateRepositoriesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Build::V2::BatchCreateRepositoriesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-BatchCreateRepositoriesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def batch_create_repositories(parent: nil, requests: nil) -> ::Gapic::Operation

Pass arguments to `batch_create_repositories` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The connection to contain all the repositories being created. Format: projects/_/locations/_ /connections/* The parent field in the CreateRepositoryRequest messages must either be empty or match this field. 
  * **requests** (::Array<[::Google::Cloud::Build::V2::CreateRepositoryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-CreateRepositoryRequest), ::Hash>) — Required. The request messages specifying the repositories to create. 



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
    
    
    require "google/cloud/build/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Build::V2::RepositoryManager::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Build::V2::BatchCreateRepositoriesRequest.new
    
    # Call the batch_create_repositories method.
    result = client.batch_create_repositories request
    
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

Configure the RepositoryManager Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-RepositoryManager-Client#Google__Cloud__Build__V2__RepositoryManager__Client_configure_class_ "Google::Cloud::Build::V2::RepositoryManager::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-RepositoryManager-Client-Configuration "Google::Cloud::Build::V2::RepositoryManager::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-RepositoryManager-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-RepositoryManager-Client-Configuration)) 



### #create_connection
    
    
    def create_connection(request, options = nil) -> ::Gapic::Operation
    def create_connection(parent: nil, connection: nil, connection_id: nil) -> ::Gapic::Operation

Creates a Connection.

**Overloads**
    
    
    def create_connection(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_connection` via a request object, either of type [CreateConnectionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-CreateConnectionRequest "Google::Cloud::Build::V2::CreateConnectionRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Build::V2::CreateConnectionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-CreateConnectionRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_connection(parent: nil, connection: nil, connection_id: nil) -> ::Gapic::Operation

Pass arguments to `create_connection` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Project and location where the connection will be created. Format: `projects/*/locations/*`. 
  * **connection** ([::Google::Cloud::Build::V2::Connection](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-Connection), ::Hash) — Required. The Connection to create. 
  * **connection_id** (::String) — Required. The ID to use for the Connection, which will become the final component of the Connection's resource name. Names must be unique per-project per-location. Allows alphanumeric characters and any of -._~%!$&'()*+,;=@. 



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
    
    
    require "google/cloud/build/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Build::V2::RepositoryManager::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Build::V2::CreateConnectionRequest.new
    
    # Call the create_connection method.
    result = client.create_connection request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #create_repository
    
    
    def create_repository(request, options = nil) -> ::Gapic::Operation
    def create_repository(parent: nil, repository: nil, repository_id: nil) -> ::Gapic::Operation

Creates a Repository.

**Overloads**
    
    
    def create_repository(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_repository` via a request object, either of type [CreateRepositoryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-CreateRepositoryRequest "Google::Cloud::Build::V2::CreateRepositoryRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Build::V2::CreateRepositoryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-CreateRepositoryRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_repository(parent: nil, repository: nil, repository_id: nil) -> ::Gapic::Operation

Pass arguments to `create_repository` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The connection to contain the repository. If the request is part of a BatchCreateRepositoriesRequest, this field should be empty or match the parent specified there. 
  * **repository** ([::Google::Cloud::Build::V2::Repository](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-Repository), ::Hash) — Required. The repository to create. 
  * **repository_id** (::String) — Required. The ID to use for the repository, which will become the final component of the repository's resource name. This ID should be unique in the connection. Allows alphanumeric characters and any of -._~%!$&'()*+,;=@. 



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
    
    
    require "google/cloud/build/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Build::V2::RepositoryManager::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Build::V2::CreateRepositoryRequest.new
    
    # Call the create_repository method.
    result = client.create_repository request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_connection
    
    
    def delete_connection(request, options = nil) -> ::Gapic::Operation
    def delete_connection(name: nil, etag: nil, validate_only: nil) -> ::Gapic::Operation

Deletes a single connection.

**Overloads**
    
    
    def delete_connection(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_connection` via a request object, either of type [DeleteConnectionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-DeleteConnectionRequest "Google::Cloud::Build::V2::DeleteConnectionRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Build::V2::DeleteConnectionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-DeleteConnectionRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_connection(name: nil, etag: nil, validate_only: nil) -> ::Gapic::Operation

Pass arguments to `delete_connection` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the Connection to delete. Format: `projects/*/locations/*/connections/*`. 
  * **etag** (::String) — The current etag of the connection. If an etag is provided and does not match the current etag of the connection, deletion will be blocked and an ABORTED error will be returned. 
  * **validate_only** (::Boolean) — If set, validate the request, but do not actually post it. 



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
    
    
    require "google/cloud/build/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Build::V2::RepositoryManager::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Build::V2::DeleteConnectionRequest.new
    
    # Call the delete_connection method.
    result = client.delete_connection request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_repository
    
    
    def delete_repository(request, options = nil) -> ::Gapic::Operation
    def delete_repository(name: nil, etag: nil, validate_only: nil) -> ::Gapic::Operation

Deletes a single repository.

**Overloads**
    
    
    def delete_repository(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_repository` via a request object, either of type [DeleteRepositoryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-DeleteRepositoryRequest "Google::Cloud::Build::V2::DeleteRepositoryRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Build::V2::DeleteRepositoryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-DeleteRepositoryRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_repository(name: nil, etag: nil, validate_only: nil) -> ::Gapic::Operation

Pass arguments to `delete_repository` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the Repository to delete. Format: `projects/*/locations/*/connections/*/repositories/*`. 
  * **etag** (::String) — The current etag of the repository. If an etag is provided and does not match the current etag of the repository, deletion will be blocked and an ABORTED error will be returned. 
  * **validate_only** (::Boolean) — If set, validate the request, but do not actually post it. 



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
    
    
    require "google/cloud/build/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Build::V2::RepositoryManager::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Build::V2::DeleteRepositoryRequest.new
    
    # Call the delete_repository method.
    result = client.delete_repository request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #fetch_git_refs
    
    
    def fetch_git_refs(request, options = nil) -> ::Google::Cloud::Build::V2::FetchGitRefsResponse
    def fetch_git_refs(repository: nil, ref_type: nil) -> ::Google::Cloud::Build::V2::FetchGitRefsResponse

Fetch the list of branches or tags for a given repository.

**Overloads**
    
    
    def fetch_git_refs(request, options = nil) -> ::Google::Cloud::Build::V2::FetchGitRefsResponse

Pass arguments to `fetch_git_refs` via a request object, either of type [FetchGitRefsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-FetchGitRefsRequest "Google::Cloud::Build::V2::FetchGitRefsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Build::V2::FetchGitRefsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-FetchGitRefsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def fetch_git_refs(repository: nil, ref_type: nil) -> ::Google::Cloud::Build::V2::FetchGitRefsResponse

Pass arguments to `fetch_git_refs` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **repository** (::String) — Required. The resource name of the repository in the format `projects/*/locations/*/connections/*/repositories/*`. 
  * **ref_type** ([::Google::Cloud::Build::V2::FetchGitRefsRequest::RefType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-FetchGitRefsRequest-RefType)) — Type of refs to fetch 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Build::V2::FetchGitRefsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-FetchGitRefsResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Build::V2::FetchGitRefsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-FetchGitRefsResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/build/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Build::V2::RepositoryManager::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Build::V2::FetchGitRefsRequest.new
    
    # Call the fetch_git_refs method.
    result = client.fetch_git_refs request
    
    # The returned object is of type Google::Cloud::Build::V2::FetchGitRefsResponse.
    p result

### #fetch_linkable_repositories
    
    
    def fetch_linkable_repositories(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Build::V2::Repository>
    def fetch_linkable_repositories(connection: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Build::V2::Repository>

FetchLinkableRepositories get repositories from SCM that are accessible and could be added to the connection.

**Overloads**
    
    
    def fetch_linkable_repositories(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Build::V2::Repository>

Pass arguments to `fetch_linkable_repositories` via a request object, either of type [FetchLinkableRepositoriesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-FetchLinkableRepositoriesRequest "Google::Cloud::Build::V2::FetchLinkableRepositoriesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Build::V2::FetchLinkableRepositoriesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-FetchLinkableRepositoriesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def fetch_linkable_repositories(connection: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Build::V2::Repository>

Pass arguments to `fetch_linkable_repositories` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **connection** (::String) — Required. The name of the Connection. Format: `projects/*/locations/*/connections/*`. 
  * **page_size** (::Integer) — Number of results to return in the list. Default to 20. 
  * **page_token** (::String) — Page start. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Build::V2::Repository](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-Repository)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Build::V2::Repository](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-Repository)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/build/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Build::V2::RepositoryManager::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Build::V2::FetchLinkableRepositoriesRequest.new
    
    # Call the fetch_linkable_repositories method.
    result = client.fetch_linkable_repositories request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Build::V2::Repository.
      p item
    end

### #fetch_read_token
    
    
    def fetch_read_token(request, options = nil) -> ::Google::Cloud::Build::V2::FetchReadTokenResponse
    def fetch_read_token(repository: nil) -> ::Google::Cloud::Build::V2::FetchReadTokenResponse

Fetches read token of a given repository.

**Overloads**
    
    
    def fetch_read_token(request, options = nil) -> ::Google::Cloud::Build::V2::FetchReadTokenResponse

Pass arguments to `fetch_read_token` via a request object, either of type [FetchReadTokenRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-FetchReadTokenRequest "Google::Cloud::Build::V2::FetchReadTokenRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Build::V2::FetchReadTokenRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-FetchReadTokenRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def fetch_read_token(repository: nil) -> ::Google::Cloud::Build::V2::FetchReadTokenResponse

Pass arguments to `fetch_read_token` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **repository** (::String) — Required. The resource name of the repository in the format `projects/*/locations/*/connections/*/repositories/*`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Build::V2::FetchReadTokenResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-FetchReadTokenResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Build::V2::FetchReadTokenResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-FetchReadTokenResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/build/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Build::V2::RepositoryManager::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Build::V2::FetchReadTokenRequest.new
    
    # Call the fetch_read_token method.
    result = client.fetch_read_token request
    
    # The returned object is of type Google::Cloud::Build::V2::FetchReadTokenResponse.
    p result

### #fetch_read_write_token
    
    
    def fetch_read_write_token(request, options = nil) -> ::Google::Cloud::Build::V2::FetchReadWriteTokenResponse
    def fetch_read_write_token(repository: nil) -> ::Google::Cloud::Build::V2::FetchReadWriteTokenResponse

Fetches read/write token of a given repository.

**Overloads**
    
    
    def fetch_read_write_token(request, options = nil) -> ::Google::Cloud::Build::V2::FetchReadWriteTokenResponse

Pass arguments to `fetch_read_write_token` via a request object, either of type [FetchReadWriteTokenRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-FetchReadWriteTokenRequest "Google::Cloud::Build::V2::FetchReadWriteTokenRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Build::V2::FetchReadWriteTokenRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-FetchReadWriteTokenRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def fetch_read_write_token(repository: nil) -> ::Google::Cloud::Build::V2::FetchReadWriteTokenResponse

Pass arguments to `fetch_read_write_token` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **repository** (::String) — Required. The resource name of the repository in the format `projects/*/locations/*/connections/*/repositories/*`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Build::V2::FetchReadWriteTokenResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-FetchReadWriteTokenResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Build::V2::FetchReadWriteTokenResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-FetchReadWriteTokenResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/build/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Build::V2::RepositoryManager::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Build::V2::FetchReadWriteTokenRequest.new
    
    # Call the fetch_read_write_token method.
    result = client.fetch_read_write_token request
    
    # The returned object is of type Google::Cloud::Build::V2::FetchReadWriteTokenResponse.
    p result

### #get_connection
    
    
    def get_connection(request, options = nil) -> ::Google::Cloud::Build::V2::Connection
    def get_connection(name: nil) -> ::Google::Cloud::Build::V2::Connection

Gets details of a single connection.

**Overloads**
    
    
    def get_connection(request, options = nil) -> ::Google::Cloud::Build::V2::Connection

Pass arguments to `get_connection` via a request object, either of type [GetConnectionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-GetConnectionRequest "Google::Cloud::Build::V2::GetConnectionRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Build::V2::GetConnectionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-GetConnectionRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_connection(name: nil) -> ::Google::Cloud::Build::V2::Connection

Pass arguments to `get_connection` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the Connection to retrieve. Format: `projects/*/locations/*/connections/*`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Build::V2::Connection](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-Connection)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Build::V2::Connection](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-Connection)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/build/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Build::V2::RepositoryManager::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Build::V2::GetConnectionRequest.new
    
    # Call the get_connection method.
    result = client.get_connection request
    
    # The returned object is of type Google::Cloud::Build::V2::Connection.
    p result

### #get_repository
    
    
    def get_repository(request, options = nil) -> ::Google::Cloud::Build::V2::Repository
    def get_repository(name: nil) -> ::Google::Cloud::Build::V2::Repository

Gets details of a single repository.

**Overloads**
    
    
    def get_repository(request, options = nil) -> ::Google::Cloud::Build::V2::Repository

Pass arguments to `get_repository` via a request object, either of type [GetRepositoryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-GetRepositoryRequest "Google::Cloud::Build::V2::GetRepositoryRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Build::V2::GetRepositoryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-GetRepositoryRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_repository(name: nil) -> ::Google::Cloud::Build::V2::Repository

Pass arguments to `get_repository` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the Repository to retrieve. Format: `projects/*/locations/*/connections/*/repositories/*`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Build::V2::Repository](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-Repository)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Build::V2::Repository](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-Repository)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/build/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Build::V2::RepositoryManager::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Build::V2::GetRepositoryRequest.new
    
    # Call the get_repository method.
    result = client.get_repository request
    
    # The returned object is of type Google::Cloud::Build::V2::Repository.
    p result

### #iam_policy_client
    
    
    def iam_policy_client() -> Google::Iam::V1::IAMPolicy::Client

Get the associated client for mix-in of the IAMPolicy.

**Returns**

  * (Google::Iam::V1::IAMPolicy::Client) 



### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new RepositoryManager client object.

**Yields**

  * (config) — Configure the RepositoryManager client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-RepositoryManager-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-RepositoryManager-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Build::V2::RepositoryManager::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Build::V2::RepositoryManager::Client.new do |config|
      config.timeout = 10.0
    end

### #list_connections
    
    
    def list_connections(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Build::V2::Connection>
    def list_connections(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Build::V2::Connection>

Lists Connections in a given project and location.

**Overloads**
    
    
    def list_connections(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Build::V2::Connection>

Pass arguments to `list_connections` via a request object, either of type [ListConnectionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-ListConnectionsRequest "Google::Cloud::Build::V2::ListConnectionsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Build::V2::ListConnectionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-ListConnectionsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_connections(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Build::V2::Connection>

Pass arguments to `list_connections` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent, which owns this collection of Connections. Format: `projects/*/locations/*`. 
  * **page_size** (::Integer) — Number of results to return in the list. 
  * **page_token** (::String) — Page start. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Build::V2::Connection](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-Connection)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Build::V2::Connection](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-Connection)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/build/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Build::V2::RepositoryManager::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Build::V2::ListConnectionsRequest.new
    
    # Call the list_connections method.
    result = client.list_connections request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Build::V2::Connection.
      p item
    end

### #list_repositories
    
    
    def list_repositories(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Build::V2::Repository>
    def list_repositories(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Build::V2::Repository>

Lists Repositories in a given connection.

**Overloads**
    
    
    def list_repositories(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Build::V2::Repository>

Pass arguments to `list_repositories` via a request object, either of type [ListRepositoriesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-ListRepositoriesRequest "Google::Cloud::Build::V2::ListRepositoriesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Build::V2::ListRepositoriesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-ListRepositoriesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_repositories(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Build::V2::Repository>

Pass arguments to `list_repositories` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent, which owns this collection of Repositories. Format: `projects/*/locations/*/connections/*`. 
  * **page_size** (::Integer) — Number of results to return in the list. 
  * **page_token** (::String) — Page start. 
  * **filter** (::String) — A filter expression that filters resources listed in the response. Expressions must follow API improvement proposal [AIP-160](https://google.aip.dev/160). e.g. `remote_uri:"https://github.com*"`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Build::V2::Repository](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-Repository)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Build::V2::Repository](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-Repository)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/build/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Build::V2::RepositoryManager::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Build::V2::ListRepositoriesRequest.new
    
    # Call the list_repositories method.
    result = client.list_repositories request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Build::V2::Repository.
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



### #operations_client
    
    
    def operations_client() -> ::Google::Cloud::Build::V2::RepositoryManager::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::Build::V2::RepositoryManager::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-RepositoryManager-Operations)) 



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_connection
    
    
    def update_connection(request, options = nil) -> ::Gapic::Operation
    def update_connection(connection: nil, update_mask: nil, allow_missing: nil, etag: nil) -> ::Gapic::Operation

Updates a single connection.

**Overloads**
    
    
    def update_connection(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_connection` via a request object, either of type [UpdateConnectionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-UpdateConnectionRequest "Google::Cloud::Build::V2::UpdateConnectionRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Build::V2::UpdateConnectionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-UpdateConnectionRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_connection(connection: nil, update_mask: nil, allow_missing: nil, etag: nil) -> ::Gapic::Operation

Pass arguments to `update_connection` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **connection** ([::Google::Cloud::Build::V2::Connection](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-Connection), ::Hash) — Required. The Connection to update. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Protobuf-FieldMask), ::Hash) — The list of fields to be updated. 
  * **allow_missing** (::Boolean) — If set to true, and the connection is not found a new connection will be created. In this situation `update_mask` is ignored. The creation will succeed only if the input connection has all the necessary information (e.g a github_config with both user_oauth_token and installation_id properties). 
  * **etag** (::String) — The current etag of the connection. If an etag is provided and does not match the current etag of the connection, update will be blocked and an ABORTED error will be returned. 



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
    
    
    require "google/cloud/build/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Build::V2::RepositoryManager::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Build::V2::UpdateConnectionRequest.new
    
    # Call the update_connection method.
    result = client.update_connection request
    
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
