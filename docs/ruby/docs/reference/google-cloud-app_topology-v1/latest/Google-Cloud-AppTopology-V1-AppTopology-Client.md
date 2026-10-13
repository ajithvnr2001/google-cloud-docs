---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_topology-v1/latest/Google-Cloud-AppTopology-V1-AppTopology-Client/
title: App Topology V1 API - Class Google::Cloud::AppTopology::V1::AppTopology::Client (v0.1.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:42:34.517909+00:00
---

# App Topology V1 API - Class Google::Cloud::AppTopology::V1::AppTopology::Client (v0.1.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_topology-v1/latest/Google-Cloud-AppTopology-V1-AppTopology-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  App Topology V1 API - Class Google::Cloud::AppTopology::V1::AppTopology::Client (v0.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

Reference documentation and code samples for the App Topology V1 API class Google::Cloud::AppTopology::V1::AppTopology::Client.

Client for the AppTopology service.

Service describing handlers for resources

## Inherits

  * Object 



## Includes

  * [Google::Cloud::AppTopology::V1::AppTopology::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_topology-v1/latest/Google-Cloud-AppTopology-V1-AppTopology-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the AppTopology Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_topology-v1/latest/Google-Cloud-AppTopology-V1-AppTopology-Client-Configuration "Google::Cloud::AppTopology::V1::AppTopology::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_topology-v1/latest/Google-Cloud-AppTopology-V1-AppTopology-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_topology-v1/latest/Google-Cloud-AppTopology-V1-AppTopology-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all AppTopology clients
    ::Google::Cloud::AppTopology::V1::AppTopology::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the AppTopology Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_topology-v1/latest/Google-Cloud-AppTopology-V1-AppTopology-Client#Google__Cloud__AppTopology__V1__AppTopology__Client_configure_class_ "Google::Cloud::AppTopology::V1::AppTopology::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_topology-v1/latest/Google-Cloud-AppTopology-V1-AppTopology-Client-Configuration "Google::Cloud::AppTopology::V1::AppTopology::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_topology-v1/latest/Google-Cloud-AppTopology-V1-AppTopology-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_topology-v1/latest/Google-Cloud-AppTopology-V1-AppTopology-Client-Configuration)) 



### #generate_discovered_resources_topology
    
    
    def generate_discovered_resources_topology(request, options = nil) -> ::Google::Cloud::AppTopology::V1::GenerateDiscoveredResourcesTopologyResponse
    def generate_discovered_resources_topology(filter: nil, name: nil, topology_domains: nil) -> ::Google::Cloud::AppTopology::V1::GenerateDiscoveredResourcesTopologyResponse

Generate the topology for all resources in the given project. If the project represents an [app boundary](https://cloud.google.com/app-hub/docs/reference/rest/v1/Boundary), the topology is generated for all resources in the boundary.

**Overloads**
    
    
    def generate_discovered_resources_topology(request, options = nil) -> ::Google::Cloud::AppTopology::V1::GenerateDiscoveredResourcesTopologyResponse

Pass arguments to `generate_discovered_resources_topology` via a request object, either of type [GenerateDiscoveredResourcesTopologyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_topology-v1/latest/Google-Cloud-AppTopology-V1-GenerateDiscoveredResourcesTopologyRequest "Google::Cloud::AppTopology::V1::GenerateDiscoveredResourcesTopologyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AppTopology::V1::GenerateDiscoveredResourcesTopologyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_topology-v1/latest/Google-Cloud-AppTopology-V1-GenerateDiscoveredResourcesTopologyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def generate_discovered_resources_topology(filter: nil, name: nil, topology_domains: nil) -> ::Google::Cloud::AppTopology::V1::GenerateDiscoveredResourcesTopologyResponse

Pass arguments to `generate_discovered_resources_topology` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **filter** ([::Google::Cloud::AppTopology::V1::GraphPattern](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_topology-v1/latest/Google-Cloud-AppTopology-V1-GraphPattern), ::Hash) — Filters for the topology nodes and edges; Detail format see GraphPattern proto. A separate 'LookupSchema' method will be added that will return the necessary information to be able to construct these filters. 
  * **name** (::String) — Required. The project to query discoverable resources on. Expected format: `projects/{project}/locations/{location}/discoveredResourcesTopology`. Only `global` location is supported. 
  * **topology_domains** (::Array<::String>) — Required. The full resource name of the domain of the app topology. Format: `projects/{project}/locations/{location}/domains/{domain}` Caller must have apptopology.domains.get permission on each of the domains. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::AppTopology::V1::GenerateDiscoveredResourcesTopologyResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_topology-v1/latest/Google-Cloud-AppTopology-V1-GenerateDiscoveredResourcesTopologyResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::AppTopology::V1::GenerateDiscoveredResourcesTopologyResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_topology-v1/latest/Google-Cloud-AppTopology-V1-GenerateDiscoveredResourcesTopologyResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/app_topology/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AppTopology::V1::AppTopology::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AppTopology::V1::GenerateDiscoveredResourcesTopologyRequest.new
    
    # Call the generate_discovered_resources_topology method.
    result = client.generate_discovered_resources_topology request
    
    # The returned object is of type Google::Cloud::AppTopology::V1::GenerateDiscoveredResourcesTopologyResponse.
    p result

### #get_domain
    
    
    def get_domain(request, options = nil) -> ::Google::Cloud::AppTopology::V1::Domain
    def get_domain(name: nil) -> ::Google::Cloud::AppTopology::V1::Domain

Retrieves the specified topology domain.

**Overloads**
    
    
    def get_domain(request, options = nil) -> ::Google::Cloud::AppTopology::V1::Domain

Pass arguments to `get_domain` via a request object, either of type [GetDomainRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_topology-v1/latest/Google-Cloud-AppTopology-V1-GetDomainRequest "Google::Cloud::AppTopology::V1::GetDomainRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AppTopology::V1::GetDomainRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_topology-v1/latest/Google-Cloud-AppTopology-V1-GetDomainRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_domain(name: nil) -> ::Google::Cloud::AppTopology::V1::Domain

Pass arguments to `get_domain` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the domain to retrieve. Format: `projects/{project}/locations/{location}/domains/{domain}`



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::AppTopology::V1::Domain](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_topology-v1/latest/Google-Cloud-AppTopology-V1-Domain)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::AppTopology::V1::Domain](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_topology-v1/latest/Google-Cloud-AppTopology-V1-Domain)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/app_topology/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AppTopology::V1::AppTopology::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AppTopology::V1::GetDomainRequest.new
    
    # Call the get_domain method.
    result = client.get_domain request
    
    # The returned object is of type Google::Cloud::AppTopology::V1::Domain.
    p result

### #get_schema
    
    
    def get_schema(request, options = nil) -> ::Google::Cloud::AppTopology::V1::Schema
    def get_schema(name: nil) -> ::Google::Cloud::AppTopology::V1::Schema

Retrieves the schema for the specified topology domain. The schema defines the NodeTypes and EdgeTypes that are supported in GenerateDiscoveredResourcesTopology requests and responses for a given domain.

**Overloads**
    
    
    def get_schema(request, options = nil) -> ::Google::Cloud::AppTopology::V1::Schema

Pass arguments to `get_schema` via a request object, either of type [GetSchemaRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_topology-v1/latest/Google-Cloud-AppTopology-V1-GetSchemaRequest "Google::Cloud::AppTopology::V1::GetSchemaRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AppTopology::V1::GetSchemaRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_topology-v1/latest/Google-Cloud-AppTopology-V1-GetSchemaRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_schema(name: nil) -> ::Google::Cloud::AppTopology::V1::Schema

Pass arguments to `get_schema` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the singleton domain schema resource. Format: `projects/{project}/locations/{location}/domains/{domain}/schema`



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::AppTopology::V1::Schema](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_topology-v1/latest/Google-Cloud-AppTopology-V1-Schema)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::AppTopology::V1::Schema](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_topology-v1/latest/Google-Cloud-AppTopology-V1-Schema)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/app_topology/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AppTopology::V1::AppTopology::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AppTopology::V1::GetSchemaRequest.new
    
    # Call the get_schema method.
    result = client.get_schema request
    
    # The returned object is of type Google::Cloud::AppTopology::V1::Schema.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new AppTopology client object.

**Yields**

  * (config) — Configure the AppTopology client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_topology-v1/latest/Google-Cloud-AppTopology-V1-AppTopology-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_topology-v1/latest/Google-Cloud-AppTopology-V1-AppTopology-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::AppTopology::V1::AppTopology::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::AppTopology::V1::AppTopology::Client.new do |config|
      config.timeout = 10.0
    end

### #list_domains
    
    
    def list_domains(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::AppTopology::V1::Domain>
    def list_domains(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::AppTopology::V1::Domain>

Lists the topology domains available in a specific location. Only `global` location is supported.

**Overloads**
    
    
    def list_domains(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::AppTopology::V1::Domain>

Pass arguments to `list_domains` via a request object, either of type [ListDomainsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_topology-v1/latest/Google-Cloud-AppTopology-V1-ListDomainsRequest "Google::Cloud::AppTopology::V1::ListDomainsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AppTopology::V1::ListDomainsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_topology-v1/latest/Google-Cloud-AppTopology-V1-ListDomainsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_domains(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::AppTopology::V1::Domain>

Pass arguments to `list_domains` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent location to list domains for. Format: `projects/{project}/locations/{location}` Only `global` location is supported. 
  * **page_size** (::Integer) — Optional. The maximum number of domains to return. The service may return fewer than this value. If unspecified, at most 50 domains will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000. 
  * **page_token** (::String) — Optional. A page token, received from a previous `ListDomains` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `ListDomains` must match the call that provided the page token. 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::AppTopology::V1::Domain](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_topology-v1/latest/Google-Cloud-AppTopology-V1-Domain)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::AppTopology::V1::Domain](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_topology-v1/latest/Google-Cloud-AppTopology-V1-Domain)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/app_topology/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AppTopology::V1::AppTopology::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AppTopology::V1::ListDomainsRequest.new
    
    # Call the list_domains method.
    result = client.list_domains request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::AppTopology::V1::Domain.
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
