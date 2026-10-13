---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-dashboard-v1/latest/Google-Cloud-Monitoring-Dashboard-V1-DashboardsService-Rest-Client/
title: Cloud Monitoring Dashboards V1 API - Class Google::Cloud::Monitoring::Dashboard::V1::DashboardsService::Rest::Client (v1.8.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:17:42.586032+00:00
---

# Cloud Monitoring Dashboards V1 API - Class Google::Cloud::Monitoring::Dashboard::V1::DashboardsService::Rest::Client (v1.8.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-dashboard-v1/latest/Google-Cloud-Monitoring-Dashboard-V1-DashboardsService-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Monitoring Dashboards V1 API - Class Google::Cloud::Monitoring::Dashboard::V1::DashboardsService::Rest::Client (v1.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.0 (latest)  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.1  1.1.0  1.0.1  0.16.0  0.15.0  0.14.2  0.13.0  0.12.1  0.11.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.6 

Reference documentation and code samples for the Cloud Monitoring Dashboards V1 API class Google::Cloud::Monitoring::Dashboard::V1::DashboardsService::Rest::Client.

REST client for the DashboardsService service.

Manages Stackdriver dashboards. A dashboard is an arrangement of data display widgets in a specific layout.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::Monitoring::Dashboard::V1::DashboardsService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-dashboard-v1/latest/Google-Cloud-Monitoring-Dashboard-V1-DashboardsService-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the DashboardsService Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-dashboard-v1/latest/Google-Cloud-Monitoring-Dashboard-V1-DashboardsService-Rest-Client-Configuration "Google::Cloud::Monitoring::Dashboard::V1::DashboardsService::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-dashboard-v1/latest/Google-Cloud-Monitoring-Dashboard-V1-DashboardsService-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-dashboard-v1/latest/Google-Cloud-Monitoring-Dashboard-V1-DashboardsService-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all DashboardsService clients
    ::Google::Cloud::Monitoring::Dashboard::V1::DashboardsService::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the DashboardsService Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-dashboard-v1/latest/Google-Cloud-Monitoring-Dashboard-V1-DashboardsService-Rest-Client#Google__Cloud__Monitoring__Dashboard__V1__DashboardsService__Rest__Client_configure_class_ "Google::Cloud::Monitoring::Dashboard::V1::DashboardsService::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-dashboard-v1/latest/Google-Cloud-Monitoring-Dashboard-V1-DashboardsService-Rest-Client-Configuration "Google::Cloud::Monitoring::Dashboard::V1::DashboardsService::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-dashboard-v1/latest/Google-Cloud-Monitoring-Dashboard-V1-DashboardsService-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-dashboard-v1/latest/Google-Cloud-Monitoring-Dashboard-V1-DashboardsService-Rest-Client-Configuration)) 



### #create_dashboard
    
    
    def create_dashboard(request, options = nil) -> ::Google::Cloud::Monitoring::Dashboard::V1::Dashboard
    def create_dashboard(parent: nil, dashboard: nil, validate_only: nil) -> ::Google::Cloud::Monitoring::Dashboard::V1::Dashboard

Creates a new custom dashboard. For examples on how you can use this API to create dashboards, see [Managing dashboards by API](https://cloud.google.com/monitoring/dashboards/api-dashboard). This method requires the `monitoring.dashboards.create` permission on the specified project. For more information about permissions, see [Cloud Identity and Access Management](https://cloud.google.com/iam).

**Overloads**
    
    
    def create_dashboard(request, options = nil) -> ::Google::Cloud::Monitoring::Dashboard::V1::Dashboard

Pass arguments to `create_dashboard` via a request object, either of type [CreateDashboardRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-dashboard-v1/latest/Google-Cloud-Monitoring-Dashboard-V1-CreateDashboardRequest "Google::Cloud::Monitoring::Dashboard::V1::CreateDashboardRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Monitoring::Dashboard::V1::CreateDashboardRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-dashboard-v1/latest/Google-Cloud-Monitoring-Dashboard-V1-CreateDashboardRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_dashboard(parent: nil, dashboard: nil, validate_only: nil) -> ::Google::Cloud::Monitoring::Dashboard::V1::Dashboard

Pass arguments to `create_dashboard` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The project on which to execute the request. The format is:
        
        projects/[PROJECT_ID_OR_NUMBER]
        

The `[PROJECT_ID_OR_NUMBER]` must match the dashboard resource name. 

  * **dashboard** ([::Google::Cloud::Monitoring::Dashboard::V1::Dashboard](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-dashboard-v1/latest/Google-Cloud-Monitoring-Dashboard-V1-Dashboard), ::Hash) — Required. The initial dashboard specification. 
  * **validate_only** (::Boolean) — If set, validate the request and preview the review, but do not actually save it. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Monitoring::Dashboard::V1::Dashboard](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-dashboard-v1/latest/Google-Cloud-Monitoring-Dashboard-V1-Dashboard)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Monitoring::Dashboard::V1::Dashboard](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-dashboard-v1/latest/Google-Cloud-Monitoring-Dashboard-V1-Dashboard)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/monitoring/dashboard/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Monitoring::Dashboard::V1::DashboardsService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Monitoring::Dashboard::V1::CreateDashboardRequest.new
    
    # Call the create_dashboard method.
    result = client.create_dashboard request
    
    # The returned object is of type Google::Cloud::Monitoring::Dashboard::V1::Dashboard.
    p result

### #delete_dashboard
    
    
    def delete_dashboard(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_dashboard(name: nil) -> ::Google::Protobuf::Empty

Deletes an existing custom dashboard.

This method requires the `monitoring.dashboards.delete` permission on the specified dashboard. For more information, see [Cloud Identity and Access Management](https://cloud.google.com/iam).

**Overloads**
    
    
    def delete_dashboard(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_dashboard` via a request object, either of type [Google::Cloud::Monitoring::Dashboard::V1::DeleteDashboardRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-dashboard-v1/latest/Google-Cloud-Monitoring-Dashboard-V1-DeleteDashboardRequest "Google::Cloud::Monitoring::Dashboard::V1::DeleteDashboardRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Monitoring::Dashboard::V1::DeleteDashboardRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-dashboard-v1/latest/Google-Cloud-Monitoring-Dashboard-V1-DeleteDashboardRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_dashboard(name: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_dashboard` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — 

Required. The resource name of the Dashboard. The format is:
        
        projects/[PROJECT_ID_OR_NUMBER]/dashboards/[DASHBOARD_ID]
        




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-dashboard-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-dashboard-v1/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/monitoring/dashboard/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Monitoring::Dashboard::V1::DashboardsService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Monitoring::Dashboard::V1::DeleteDashboardRequest.new
    
    # Call the delete_dashboard method.
    result = client.delete_dashboard request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #get_dashboard
    
    
    def get_dashboard(request, options = nil) -> ::Google::Cloud::Monitoring::Dashboard::V1::Dashboard
    def get_dashboard(name: nil) -> ::Google::Cloud::Monitoring::Dashboard::V1::Dashboard

Fetches a specific dashboard.

This method requires the `monitoring.dashboards.get` permission on the specified dashboard. For more information, see [Cloud Identity and Access Management](https://cloud.google.com/iam).

**Overloads**
    
    
    def get_dashboard(request, options = nil) -> ::Google::Cloud::Monitoring::Dashboard::V1::Dashboard

Pass arguments to `get_dashboard` via a request object, either of type [GetDashboardRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-dashboard-v1/latest/Google-Cloud-Monitoring-Dashboard-V1-GetDashboardRequest "Google::Cloud::Monitoring::Dashboard::V1::GetDashboardRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Monitoring::Dashboard::V1::GetDashboardRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-dashboard-v1/latest/Google-Cloud-Monitoring-Dashboard-V1-GetDashboardRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_dashboard(name: nil) -> ::Google::Cloud::Monitoring::Dashboard::V1::Dashboard

Pass arguments to `get_dashboard` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — 

Required. The resource name of the Dashboard. The format is one of:

    * `dashboards/[DASHBOARD_ID]` (for system dashboards)
    * `projects/[PROJECT_ID_OR_NUMBER]/dashboards/[DASHBOARD_ID]` (for custom dashboards).



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Monitoring::Dashboard::V1::Dashboard](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-dashboard-v1/latest/Google-Cloud-Monitoring-Dashboard-V1-Dashboard)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Monitoring::Dashboard::V1::Dashboard](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-dashboard-v1/latest/Google-Cloud-Monitoring-Dashboard-V1-Dashboard)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/monitoring/dashboard/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Monitoring::Dashboard::V1::DashboardsService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Monitoring::Dashboard::V1::GetDashboardRequest.new
    
    # Call the get_dashboard method.
    result = client.get_dashboard request
    
    # The returned object is of type Google::Cloud::Monitoring::Dashboard::V1::Dashboard.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new DashboardsService REST client object.

**Yields**

  * (config) — Configure the DashboardsService client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-dashboard-v1/latest/Google-Cloud-Monitoring-Dashboard-V1-DashboardsService-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-dashboard-v1/latest/Google-Cloud-Monitoring-Dashboard-V1-DashboardsService-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Monitoring::Dashboard::V1::DashboardsService::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Monitoring::Dashboard::V1::DashboardsService::Rest::Client.new do |config|
      config.timeout = 10.0
    end

### #list_dashboards
    
    
    def list_dashboards(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Monitoring::Dashboard::V1::Dashboard>
    def list_dashboards(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Monitoring::Dashboard::V1::Dashboard>

Lists the existing dashboards.

This method requires the `monitoring.dashboards.list` permission on the specified project. For more information, see [Cloud Identity and Access Management](https://cloud.google.com/iam).

**Overloads**
    
    
    def list_dashboards(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Monitoring::Dashboard::V1::Dashboard>

Pass arguments to `list_dashboards` via a request object, either of type [ListDashboardsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-dashboard-v1/latest/Google-Cloud-Monitoring-Dashboard-V1-ListDashboardsRequest "Google::Cloud::Monitoring::Dashboard::V1::ListDashboardsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Monitoring::Dashboard::V1::ListDashboardsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-dashboard-v1/latest/Google-Cloud-Monitoring-Dashboard-V1-ListDashboardsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_dashboards(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Monitoring::Dashboard::V1::Dashboard>

Pass arguments to `list_dashboards` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — 

Required. The scope of the dashboards to list. The format is:
        
        projects/[PROJECT_ID_OR_NUMBER]
        

  * **page_size** (::Integer) — A positive number that is the maximum number of results to return. If unspecified, a default of 1000 is used. 
  * **page_token** (::String) — Optional. If this field is not empty then it must contain the `nextPageToken` value returned by a previous call to this method. Using this field causes the method to return additional results from the previous method call. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Monitoring::Dashboard::V1::Dashboard](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-dashboard-v1/latest/Google-Cloud-Monitoring-Dashboard-V1-Dashboard)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Monitoring::Dashboard::V1::Dashboard](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-dashboard-v1/latest/Google-Cloud-Monitoring-Dashboard-V1-Dashboard)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/monitoring/dashboard/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Monitoring::Dashboard::V1::DashboardsService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Monitoring::Dashboard::V1::ListDashboardsRequest.new
    
    # Call the list_dashboards method.
    result = client.list_dashboards request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Monitoring::Dashboard::V1::Dashboard.
      p item
    end

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



### #update_dashboard
    
    
    def update_dashboard(request, options = nil) -> ::Google::Cloud::Monitoring::Dashboard::V1::Dashboard
    def update_dashboard(dashboard: nil, validate_only: nil) -> ::Google::Cloud::Monitoring::Dashboard::V1::Dashboard

Replaces an existing custom dashboard with a new definition.

This method requires the `monitoring.dashboards.update` permission on the specified dashboard. For more information, see [Cloud Identity and Access Management](https://cloud.google.com/iam).

**Overloads**
    
    
    def update_dashboard(request, options = nil) -> ::Google::Cloud::Monitoring::Dashboard::V1::Dashboard

Pass arguments to `update_dashboard` via a request object, either of type [UpdateDashboardRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-dashboard-v1/latest/Google-Cloud-Monitoring-Dashboard-V1-UpdateDashboardRequest "Google::Cloud::Monitoring::Dashboard::V1::UpdateDashboardRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Monitoring::Dashboard::V1::UpdateDashboardRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-dashboard-v1/latest/Google-Cloud-Monitoring-Dashboard-V1-UpdateDashboardRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_dashboard(dashboard: nil, validate_only: nil) -> ::Google::Cloud::Monitoring::Dashboard::V1::Dashboard

Pass arguments to `update_dashboard` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **dashboard** ([::Google::Cloud::Monitoring::Dashboard::V1::Dashboard](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-dashboard-v1/latest/Google-Cloud-Monitoring-Dashboard-V1-Dashboard), ::Hash) — Required. The dashboard that will replace the existing dashboard. 
  * **validate_only** (::Boolean) — If set, validate the request and preview the review, but do not actually save it. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Monitoring::Dashboard::V1::Dashboard](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-dashboard-v1/latest/Google-Cloud-Monitoring-Dashboard-V1-Dashboard)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Monitoring::Dashboard::V1::Dashboard](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-dashboard-v1/latest/Google-Cloud-Monitoring-Dashboard-V1-Dashboard)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/monitoring/dashboard/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Monitoring::Dashboard::V1::DashboardsService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Monitoring::Dashboard::V1::UpdateDashboardRequest.new
    
    # Call the update_dashboard method.
    result = client.update_dashboard request
    
    # The returned object is of type Google::Cloud::Monitoring::Dashboard::V1::Dashboard.
    p result

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
