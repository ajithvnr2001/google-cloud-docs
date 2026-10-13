---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-maintenance-api-v1/latest/Google-Cloud-Maintenance-Api-V1-Maintenance-Client/
title: Maintenance V1 API - Class Google::Cloud::Maintenance::Api::V1::Maintenance::Client (v1.0.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:21:23.717732+00:00
---

# Maintenance V1 API - Class Google::Cloud::Maintenance::Api::V1::Maintenance::Client (v1.0.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-maintenance-api-v1/latest/Google-Cloud-Maintenance-Api-V1-Maintenance-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Maintenance V1 API - Class Google::Cloud::Maintenance::Api::V1::Maintenance::Client (v1.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.1 (latest)  1.0.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Maintenance V1 API class Google::Cloud::Maintenance::Api::V1::Maintenance::Client.

Client for the Maintenance service.

Unified Maintenance service

## Inherits

  * Object 



## Includes

  * [Google::Cloud::Maintenance::Api::V1::Maintenance::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-maintenance-api-v1/latest/Google-Cloud-Maintenance-Api-V1-Maintenance-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the Maintenance Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-maintenance-api-v1/latest/Google-Cloud-Maintenance-Api-V1-Maintenance-Client-Configuration "Google::Cloud::Maintenance::Api::V1::Maintenance::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-maintenance-api-v1/latest/Google-Cloud-Maintenance-Api-V1-Maintenance-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-maintenance-api-v1/latest/Google-Cloud-Maintenance-Api-V1-Maintenance-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all Maintenance clients
    ::Google::Cloud::Maintenance::Api::V1::Maintenance::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the Maintenance Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-maintenance-api-v1/latest/Google-Cloud-Maintenance-Api-V1-Maintenance-Client#Google__Cloud__Maintenance__Api__V1__Maintenance__Client_configure_class_ "Google::Cloud::Maintenance::Api::V1::Maintenance::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-maintenance-api-v1/latest/Google-Cloud-Maintenance-Api-V1-Maintenance-Client-Configuration "Google::Cloud::Maintenance::Api::V1::Maintenance::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-maintenance-api-v1/latest/Google-Cloud-Maintenance-Api-V1-Maintenance-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-maintenance-api-v1/latest/Google-Cloud-Maintenance-Api-V1-Maintenance-Client-Configuration)) 



### #get_resource_maintenance
    
    
    def get_resource_maintenance(request, options = nil) -> ::Google::Cloud::Maintenance::Api::V1::ResourceMaintenance
    def get_resource_maintenance(name: nil) -> ::Google::Cloud::Maintenance::Api::V1::ResourceMaintenance

Retrieve a single resource maintenance.

**Overloads**
    
    
    def get_resource_maintenance(request, options = nil) -> ::Google::Cloud::Maintenance::Api::V1::ResourceMaintenance

Pass arguments to `get_resource_maintenance` via a request object, either of type [GetResourceMaintenanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-maintenance-api-v1/latest/Google-Cloud-Maintenance-Api-V1-GetResourceMaintenanceRequest "Google::Cloud::Maintenance::Api::V1::GetResourceMaintenanceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Maintenance::Api::V1::GetResourceMaintenanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-maintenance-api-v1/latest/Google-Cloud-Maintenance-Api-V1-GetResourceMaintenanceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_resource_maintenance(name: nil) -> ::Google::Cloud::Maintenance::Api::V1::ResourceMaintenance

Pass arguments to `get_resource_maintenance` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The resource name of the resource within a service. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Maintenance::Api::V1::ResourceMaintenance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-maintenance-api-v1/latest/Google-Cloud-Maintenance-Api-V1-ResourceMaintenance)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Maintenance::Api::V1::ResourceMaintenance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-maintenance-api-v1/latest/Google-Cloud-Maintenance-Api-V1-ResourceMaintenance)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/maintenance/api/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Maintenance::Api::V1::Maintenance::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Maintenance::Api::V1::GetResourceMaintenanceRequest.new
    
    # Call the get_resource_maintenance method.
    result = client.get_resource_maintenance request
    
    # The returned object is of type Google::Cloud::Maintenance::Api::V1::ResourceMaintenance.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new Maintenance client object.

**Yields**

  * (config) — Configure the Maintenance client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-maintenance-api-v1/latest/Google-Cloud-Maintenance-Api-V1-Maintenance-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-maintenance-api-v1/latest/Google-Cloud-Maintenance-Api-V1-Maintenance-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Maintenance::Api::V1::Maintenance::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Maintenance::Api::V1::Maintenance::Client.new do |config|
      config.timeout = 10.0
    end

### #list_resource_maintenances
    
    
    def list_resource_maintenances(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Maintenance::Api::V1::ResourceMaintenance>
    def list_resource_maintenances(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Maintenance::Api::V1::ResourceMaintenance>

Retrieve a collection of resource maintenances.

**Overloads**
    
    
    def list_resource_maintenances(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Maintenance::Api::V1::ResourceMaintenance>

Pass arguments to `list_resource_maintenances` via a request object, either of type [ListResourceMaintenancesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-maintenance-api-v1/latest/Google-Cloud-Maintenance-Api-V1-ListResourceMaintenancesRequest "Google::Cloud::Maintenance::Api::V1::ListResourceMaintenancesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Maintenance::Api::V1::ListResourceMaintenancesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-maintenance-api-v1/latest/Google-Cloud-Maintenance-Api-V1-ListResourceMaintenancesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_resource_maintenances(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Maintenance::Api::V1::ResourceMaintenance>

Pass arguments to `list_resource_maintenances` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent of the resource maintenance. 
  * **page_size** (::Integer) — The maximum number of resource maintenances to send per page. 
  * **page_token** (::String) — The page token: If the next_page_token from a previous response is provided, this request will send the subsequent page. 
  * **filter** (::String) — Filter the list as specified in https://google.aip.dev/160. 
  * **order_by** (::String) — Order results as specified in https://google.aip.dev/132. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Maintenance::Api::V1::ResourceMaintenance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-maintenance-api-v1/latest/Google-Cloud-Maintenance-Api-V1-ResourceMaintenance)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Maintenance::Api::V1::ResourceMaintenance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-maintenance-api-v1/latest/Google-Cloud-Maintenance-Api-V1-ResourceMaintenance)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/maintenance/api/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Maintenance::Api::V1::Maintenance::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Maintenance::Api::V1::ListResourceMaintenancesRequest.new
    
    # Call the list_resource_maintenances method.
    result = client.list_resource_maintenances request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Maintenance::Api::V1::ResourceMaintenance.
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



### #summarize_maintenances
    
    
    def summarize_maintenances(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Maintenance::Api::V1::MaintenanceSummary>
    def summarize_maintenances(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Maintenance::Api::V1::MaintenanceSummary>

Retrieves the statistics of a specific maintenance.

**Overloads**
    
    
    def summarize_maintenances(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Maintenance::Api::V1::MaintenanceSummary>

Pass arguments to `summarize_maintenances` via a request object, either of type [SummarizeMaintenancesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-maintenance-api-v1/latest/Google-Cloud-Maintenance-Api-V1-SummarizeMaintenancesRequest "Google::Cloud::Maintenance::Api::V1::SummarizeMaintenancesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Maintenance::Api::V1::SummarizeMaintenancesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-maintenance-api-v1/latest/Google-Cloud-Maintenance-Api-V1-SummarizeMaintenancesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def summarize_maintenances(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Maintenance::Api::V1::MaintenanceSummary>

Pass arguments to `summarize_maintenances` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent of the resource maintenance. eg. `projects/123/locations/*`
  * **page_size** (::Integer) — The maximum number of resource maintenances to send per page. The default page size is 20 and the maximum is 1000. 
  * **page_token** (::String) — The page token: If the next_page_token from a previous response is provided, this request will send the subsequent page. 
  * **filter** (::String) — 

Filter the list as specified in https://google.aip.dev/160. Supported fields include:

    * `maintenance.maintenanceName` Examples:
    * `maintenance.maintenanceName="eb3b709c-9ca1-5472-9fb6-800a3849eda1"`
  * **order_by** (::String) — Order results as specified in https://google.aip.dev/132. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Maintenance::Api::V1::MaintenanceSummary](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-maintenance-api-v1/latest/Google-Cloud-Maintenance-Api-V1-MaintenanceSummary)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Maintenance::Api::V1::MaintenanceSummary](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-maintenance-api-v1/latest/Google-Cloud-Maintenance-Api-V1-MaintenanceSummary)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/maintenance/api/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Maintenance::Api::V1::Maintenance::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Maintenance::Api::V1::SummarizeMaintenancesRequest.new
    
    # Call the summarize_maintenances method.
    result = client.summarize_maintenances request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Maintenance::Api::V1::MaintenanceSummary.
      p item
    end

### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
