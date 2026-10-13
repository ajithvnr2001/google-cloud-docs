---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_registry-v1beta/latest/Google-Cloud-ApiRegistry-V1beta-CloudApiRegistry-Client/
title: Cloud API Registry V1BETA API - Class Google::Cloud::ApiRegistry::V1beta::CloudApiRegistry::Client (v0.4.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:31:23.191845+00:00
---

# Cloud API Registry V1BETA API - Class Google::Cloud::ApiRegistry::V1beta::CloudApiRegistry::Client (v0.4.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_registry-v1beta/latest/Google-Cloud-ApiRegistry-V1beta-CloudApiRegistry-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud API Registry V1BETA API - Class Google::Cloud::ApiRegistry::V1beta::CloudApiRegistry::Client (v0.4.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.4.2 (latest)  0.4.1  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Cloud API Registry V1BETA API class Google::Cloud::ApiRegistry::V1beta::CloudApiRegistry::Client.

Client for the CloudApiRegistry service.

The Cloud API Registry service provides a central registry for managing API Data.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::ApiRegistry::V1beta::CloudApiRegistry::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_registry-v1beta/latest/Google-Cloud-ApiRegistry-V1beta-CloudApiRegistry-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the CloudApiRegistry Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_registry-v1beta/latest/Google-Cloud-ApiRegistry-V1beta-CloudApiRegistry-Client-Configuration "Google::Cloud::ApiRegistry::V1beta::CloudApiRegistry::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_registry-v1beta/latest/Google-Cloud-ApiRegistry-V1beta-CloudApiRegistry-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_registry-v1beta/latest/Google-Cloud-ApiRegistry-V1beta-CloudApiRegistry-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all CloudApiRegistry clients
    ::Google::Cloud::ApiRegistry::V1beta::CloudApiRegistry::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the CloudApiRegistry Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_registry-v1beta/latest/Google-Cloud-ApiRegistry-V1beta-CloudApiRegistry-Client#Google__Cloud__ApiRegistry__V1beta__CloudApiRegistry__Client_configure_class_ "Google::Cloud::ApiRegistry::V1beta::CloudApiRegistry::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_registry-v1beta/latest/Google-Cloud-ApiRegistry-V1beta-CloudApiRegistry-Client-Configuration "Google::Cloud::ApiRegistry::V1beta::CloudApiRegistry::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_registry-v1beta/latest/Google-Cloud-ApiRegistry-V1beta-CloudApiRegistry-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_registry-v1beta/latest/Google-Cloud-ApiRegistry-V1beta-CloudApiRegistry-Client-Configuration)) 



### #get_mcp_server
    
    
    def get_mcp_server(request, options = nil) -> ::Google::Cloud::ApiRegistry::V1beta::McpServer
    def get_mcp_server(name: nil) -> ::Google::Cloud::ApiRegistry::V1beta::McpServer

Gets a single McpServer.

**Overloads**
    
    
    def get_mcp_server(request, options = nil) -> ::Google::Cloud::ApiRegistry::V1beta::McpServer

Pass arguments to `get_mcp_server` via a request object, either of type [GetMcpServerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_registry-v1beta/latest/Google-Cloud-ApiRegistry-V1beta-GetMcpServerRequest "Google::Cloud::ApiRegistry::V1beta::GetMcpServerRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApiRegistry::V1beta::GetMcpServerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_registry-v1beta/latest/Google-Cloud-ApiRegistry-V1beta-GetMcpServerRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_mcp_server(name: nil) -> ::Google::Cloud::ApiRegistry::V1beta::McpServer

Pass arguments to `get_mcp_server` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Name of the resource 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::ApiRegistry::V1beta::McpServer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_registry-v1beta/latest/Google-Cloud-ApiRegistry-V1beta-McpServer)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::ApiRegistry::V1beta::McpServer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_registry-v1beta/latest/Google-Cloud-ApiRegistry-V1beta-McpServer)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/api_registry/v1beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApiRegistry::V1beta::CloudApiRegistry::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApiRegistry::V1beta::GetMcpServerRequest.new
    
    # Call the get_mcp_server method.
    result = client.get_mcp_server request
    
    # The returned object is of type Google::Cloud::ApiRegistry::V1beta::McpServer.
    p result

### #get_mcp_tool
    
    
    def get_mcp_tool(request, options = nil) -> ::Google::Cloud::ApiRegistry::V1beta::McpTool
    def get_mcp_tool(name: nil) -> ::Google::Cloud::ApiRegistry::V1beta::McpTool

Gets a single McpTool.

**Overloads**
    
    
    def get_mcp_tool(request, options = nil) -> ::Google::Cloud::ApiRegistry::V1beta::McpTool

Pass arguments to `get_mcp_tool` via a request object, either of type [GetMcpToolRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_registry-v1beta/latest/Google-Cloud-ApiRegistry-V1beta-GetMcpToolRequest "Google::Cloud::ApiRegistry::V1beta::GetMcpToolRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApiRegistry::V1beta::GetMcpToolRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_registry-v1beta/latest/Google-Cloud-ApiRegistry-V1beta-GetMcpToolRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_mcp_tool(name: nil) -> ::Google::Cloud::ApiRegistry::V1beta::McpTool

Pass arguments to `get_mcp_tool` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Name of the resource 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::ApiRegistry::V1beta::McpTool](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_registry-v1beta/latest/Google-Cloud-ApiRegistry-V1beta-McpTool)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::ApiRegistry::V1beta::McpTool](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_registry-v1beta/latest/Google-Cloud-ApiRegistry-V1beta-McpTool)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/api_registry/v1beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApiRegistry::V1beta::CloudApiRegistry::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApiRegistry::V1beta::GetMcpToolRequest.new
    
    # Call the get_mcp_tool method.
    result = client.get_mcp_tool request
    
    # The returned object is of type Google::Cloud::ApiRegistry::V1beta::McpTool.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new CloudApiRegistry client object.

**Yields**

  * (config) — Configure the CloudApiRegistry client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_registry-v1beta/latest/Google-Cloud-ApiRegistry-V1beta-CloudApiRegistry-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_registry-v1beta/latest/Google-Cloud-ApiRegistry-V1beta-CloudApiRegistry-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::ApiRegistry::V1beta::CloudApiRegistry::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::ApiRegistry::V1beta::CloudApiRegistry::Client.new do |config|
      config.timeout = 10.0
    end

### #list_mcp_servers
    
    
    def list_mcp_servers(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ApiRegistry::V1beta::McpServer>
    def list_mcp_servers(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ApiRegistry::V1beta::McpServer>

Lists McpServers in a given Project.

**Overloads**
    
    
    def list_mcp_servers(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ApiRegistry::V1beta::McpServer>

Pass arguments to `list_mcp_servers` via a request object, either of type [ListMcpServersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_registry-v1beta/latest/Google-Cloud-ApiRegistry-V1beta-ListMcpServersRequest "Google::Cloud::ApiRegistry::V1beta::ListMcpServersRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApiRegistry::V1beta::ListMcpServersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_registry-v1beta/latest/Google-Cloud-ApiRegistry-V1beta-ListMcpServersRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_mcp_servers(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ApiRegistry::V1beta::McpServer>

Pass arguments to `list_mcp_servers` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Parent value for ListMcpServersRequest 
  * **page_size** (::Integer) — Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default. 
  * **page_token** (::String) — Optional. A token identifying a page of results the server should return. 
  * **filter** (::String) — Optional. Filtering results 
  * **order_by** (::String) — Optional. Hint for how to order the results 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::ApiRegistry::V1beta::McpServer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_registry-v1beta/latest/Google-Cloud-ApiRegistry-V1beta-McpServer)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::ApiRegistry::V1beta::McpServer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_registry-v1beta/latest/Google-Cloud-ApiRegistry-V1beta-McpServer)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/api_registry/v1beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApiRegistry::V1beta::CloudApiRegistry::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApiRegistry::V1beta::ListMcpServersRequest.new
    
    # Call the list_mcp_servers method.
    result = client.list_mcp_servers request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::ApiRegistry::V1beta::McpServer.
      p item
    end

### #list_mcp_tools
    
    
    def list_mcp_tools(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ApiRegistry::V1beta::McpTool>
    def list_mcp_tools(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ApiRegistry::V1beta::McpTool>

Lists McpTools in a given McpServer.

**Overloads**
    
    
    def list_mcp_tools(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ApiRegistry::V1beta::McpTool>

Pass arguments to `list_mcp_tools` via a request object, either of type [ListMcpToolsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_registry-v1beta/latest/Google-Cloud-ApiRegistry-V1beta-ListMcpToolsRequest "Google::Cloud::ApiRegistry::V1beta::ListMcpToolsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApiRegistry::V1beta::ListMcpToolsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_registry-v1beta/latest/Google-Cloud-ApiRegistry-V1beta-ListMcpToolsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_mcp_tools(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ApiRegistry::V1beta::McpTool>

Pass arguments to `list_mcp_tools` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Parent value for ListMcpToolsRequest 
  * **page_size** (::Integer) — Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default. 
  * **page_token** (::String) — Optional. A token identifying a page of results the server should return. 
  * **filter** (::String) — Optional. Filtering results 
  * **order_by** (::String) — Optional. Hint for how to order the results 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::ApiRegistry::V1beta::McpTool](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_registry-v1beta/latest/Google-Cloud-ApiRegistry-V1beta-McpTool)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::ApiRegistry::V1beta::McpTool](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_registry-v1beta/latest/Google-Cloud-ApiRegistry-V1beta-McpTool)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/api_registry/v1beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApiRegistry::V1beta::CloudApiRegistry::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApiRegistry::V1beta::ListMcpToolsRequest.new
    
    # Call the list_mcp_tools method.
    result = client.list_mcp_tools request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::ApiRegistry::V1beta::McpTool.
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



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
