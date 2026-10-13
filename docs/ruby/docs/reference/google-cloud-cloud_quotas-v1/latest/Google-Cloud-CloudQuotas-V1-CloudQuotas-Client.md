---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-CloudQuotas-Client/
title: Cloud Quotas V1 API - Class Google::Cloud::CloudQuotas::V1::CloudQuotas::Client (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:42:43.038492+00:00
---

# Cloud Quotas V1 API - Class Google::Cloud::CloudQuotas::V1::CloudQuotas::Client (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-CloudQuotas-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Quotas V1 API - Class Google::Cloud::CloudQuotas::V1::CloudQuotas::Client (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.0  2.3.0  2.2.2  2.1.0  2.0.1  1.3.0  1.2.0  1.1.0  1.0.1  0.3.3  0.2.2  0.1.0 

Reference documentation and code samples for the Cloud Quotas V1 API class Google::Cloud::CloudQuotas::V1::CloudQuotas::Client.

Client for the CloudQuotas service.

The Cloud Quotas API is an infrastructure service for Google Cloud that lets service consumers list and manage their resource usage limits.

  * List/Get the metadata and current status of the quotas for a service.
  * Create/Update quota preferencess that declare the preferred quota values.
  * Check the status of a quota preference request.
  * List/Get pending and historical quota preference.



## Inherits

  * Object 



## Includes

  * [Google::Cloud::CloudQuotas::V1::CloudQuotas::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-CloudQuotas-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the CloudQuotas Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-CloudQuotas-Client-Configuration "Google::Cloud::CloudQuotas::V1::CloudQuotas::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-CloudQuotas-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-CloudQuotas-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all CloudQuotas clients
    ::Google::Cloud::CloudQuotas::V1::CloudQuotas::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the CloudQuotas Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-CloudQuotas-Client#Google__Cloud__CloudQuotas__V1__CloudQuotas__Client_configure_class_ "Google::Cloud::CloudQuotas::V1::CloudQuotas::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-CloudQuotas-Client-Configuration "Google::Cloud::CloudQuotas::V1::CloudQuotas::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-CloudQuotas-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-CloudQuotas-Client-Configuration)) 



### #create_quota_preference
    
    
    def create_quota_preference(request, options = nil) -> ::Google::Cloud::CloudQuotas::V1::QuotaPreference
    def create_quota_preference(parent: nil, quota_preference_id: nil, quota_preference: nil, ignore_safety_checks: nil) -> ::Google::Cloud::CloudQuotas::V1::QuotaPreference

Creates a new QuotaPreference that declares the desired value for a quota.

**Overloads**
    
    
    def create_quota_preference(request, options = nil) -> ::Google::Cloud::CloudQuotas::V1::QuotaPreference

Pass arguments to `create_quota_preference` via a request object, either of type [Google::Cloud::CloudQuotas::V1::CreateQuotaPreferenceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-CreateQuotaPreferenceRequest "Google::Cloud::CloudQuotas::V1::CreateQuotaPreferenceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudQuotas::V1::CreateQuotaPreferenceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-CreateQuotaPreferenceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_quota_preference(parent: nil, quota_preference_id: nil, quota_preference: nil, ignore_safety_checks: nil) -> ::Google::Cloud::CloudQuotas::V1::QuotaPreference

Pass arguments to `create_quota_preference` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Identifier. Value for parent.

Example: `projects/123/locations/global`

  * **quota_preference_id** (::String) — Optional. Id of the requesting object, must be unique under its parent. If client does not set this field, the service will generate one. 
  * **quota_preference** ([::Google::Cloud::CloudQuotas::V1::QuotaPreference](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-QuotaPreference), ::Hash) — Required. The resource being created 
  * **ignore_safety_checks** (::Array<[::Google::Cloud::CloudQuotas::V1::QuotaSafetyCheck](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-QuotaSafetyCheck)>) — The list of quota safety checks to be ignored. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::CloudQuotas::V1::QuotaPreference](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-QuotaPreference)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::CloudQuotas::V1::QuotaPreference](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-QuotaPreference)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_quotas/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudQuotas::V1::CloudQuotas::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudQuotas::V1::CreateQuotaPreferenceRequest.new
    
    # Call the create_quota_preference method.
    result = client.create_quota_preference request
    
    # The returned object is of type Google::Cloud::CloudQuotas::V1::QuotaPreference.
    p result

### #get_quota_info
    
    
    def get_quota_info(request, options = nil) -> ::Google::Cloud::CloudQuotas::V1::QuotaInfo
    def get_quota_info(name: nil) -> ::Google::Cloud::CloudQuotas::V1::QuotaInfo

Retrieve the QuotaInfo of a quota for a project, folder or organization.

**Overloads**
    
    
    def get_quota_info(request, options = nil) -> ::Google::Cloud::CloudQuotas::V1::QuotaInfo

Pass arguments to `get_quota_info` via a request object, either of type [GetQuotaInfoRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-GetQuotaInfoRequest "Google::Cloud::CloudQuotas::V1::GetQuotaInfoRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudQuotas::V1::GetQuotaInfoRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-GetQuotaInfoRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_quota_info(name: nil) -> ::Google::Cloud::CloudQuotas::V1::QuotaInfo

Pass arguments to `get_quota_info` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Identifier. The resource name of the quota info.

An example name: `projects/123/locations/global/services/compute.googleapis.com/quotaInfos/CpusPerProjectPerRegion`




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::CloudQuotas::V1::QuotaInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-QuotaInfo)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::CloudQuotas::V1::QuotaInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-QuotaInfo)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_quotas/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudQuotas::V1::CloudQuotas::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudQuotas::V1::GetQuotaInfoRequest.new
    
    # Call the get_quota_info method.
    result = client.get_quota_info request
    
    # The returned object is of type Google::Cloud::CloudQuotas::V1::QuotaInfo.
    p result

### #get_quota_preference
    
    
    def get_quota_preference(request, options = nil) -> ::Google::Cloud::CloudQuotas::V1::QuotaPreference
    def get_quota_preference(name: nil) -> ::Google::Cloud::CloudQuotas::V1::QuotaPreference

Gets details of a single QuotaPreference.

**Overloads**
    
    
    def get_quota_preference(request, options = nil) -> ::Google::Cloud::CloudQuotas::V1::QuotaPreference

Pass arguments to `get_quota_preference` via a request object, either of type [GetQuotaPreferenceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-GetQuotaPreferenceRequest "Google::Cloud::CloudQuotas::V1::GetQuotaPreferenceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudQuotas::V1::GetQuotaPreferenceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-GetQuotaPreferenceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_quota_preference(name: nil) -> ::Google::Cloud::CloudQuotas::V1::QuotaPreference

Pass arguments to `get_quota_preference` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Identifier. Name of the resource

Example name: `projects/123/locations/global/quota_preferences/my-config-for-us-east1`




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::CloudQuotas::V1::QuotaPreference](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-QuotaPreference)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::CloudQuotas::V1::QuotaPreference](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-QuotaPreference)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_quotas/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudQuotas::V1::CloudQuotas::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudQuotas::V1::GetQuotaPreferenceRequest.new
    
    # Call the get_quota_preference method.
    result = client.get_quota_preference request
    
    # The returned object is of type Google::Cloud::CloudQuotas::V1::QuotaPreference.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new CloudQuotas client object.

**Yields**

  * (config) — Configure the CloudQuotas client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-CloudQuotas-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-CloudQuotas-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::CloudQuotas::V1::CloudQuotas::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::CloudQuotas::V1::CloudQuotas::Client.new do |config|
      config.timeout = 10.0
    end

### #list_quota_infos
    
    
    def list_quota_infos(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::CloudQuotas::V1::QuotaInfo>
    def list_quota_infos(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::CloudQuotas::V1::QuotaInfo>

Lists QuotaInfos of all quotas for a given project, folder or organization.

**Overloads**
    
    
    def list_quota_infos(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::CloudQuotas::V1::QuotaInfo>

Pass arguments to `list_quota_infos` via a request object, either of type [ListQuotaInfosRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-ListQuotaInfosRequest "Google::Cloud::CloudQuotas::V1::ListQuotaInfosRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudQuotas::V1::ListQuotaInfosRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-ListQuotaInfosRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_quota_infos(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::CloudQuotas::V1::QuotaInfo>

Pass arguments to `list_quota_infos` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Identifier. Parent value of QuotaInfo resources. Listing across different resource containers (such as 'projects/-') is not allowed.

Example names: `projects/123/locations/global/services/compute.googleapis.com` `folders/234/locations/global/services/compute.googleapis.com` `organizations/345/locations/global/services/compute.googleapis.com`

  * **page_size** (::Integer) — Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default. 
  * **page_token** (::String) — Optional. A token identifying a page of results the server should return. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::CloudQuotas::V1::QuotaInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-QuotaInfo)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::CloudQuotas::V1::QuotaInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-QuotaInfo)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_quotas/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudQuotas::V1::CloudQuotas::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudQuotas::V1::ListQuotaInfosRequest.new
    
    # Call the list_quota_infos method.
    result = client.list_quota_infos request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::CloudQuotas::V1::QuotaInfo.
      p item
    end

### #list_quota_preferences
    
    
    def list_quota_preferences(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::CloudQuotas::V1::QuotaPreference>
    def list_quota_preferences(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::CloudQuotas::V1::QuotaPreference>

Lists QuotaPreferences in a given project, folder or organization.

**Overloads**
    
    
    def list_quota_preferences(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::CloudQuotas::V1::QuotaPreference>

Pass arguments to `list_quota_preferences` via a request object, either of type [ListQuotaPreferencesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-ListQuotaPreferencesRequest "Google::Cloud::CloudQuotas::V1::ListQuotaPreferencesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudQuotas::V1::ListQuotaPreferencesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-ListQuotaPreferencesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_quota_preferences(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::CloudQuotas::V1::QuotaPreference>

Pass arguments to `list_quota_preferences` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Identifier. Parent value of QuotaPreference resources. Listing across different resource containers (such as 'projects/-') is not allowed.

When the value starts with 'folders' or 'organizations', it lists the QuotaPreferences for org quotas in the container. It does not list the QuotaPreferences in the descendant projects of the container.

Example parents: `projects/123/locations/global`

  * **page_size** (::Integer) — Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default. 
  * **page_token** (::String) — Optional. A token identifying a page of results the server should return. 
  * **filter** (::String) — Optional. Filter result QuotaPreferences by their state, type, create/update time range.

Example filters: `reconciling=true AND request_type=CLOUD_CONSOLE`, `reconciling=true OR creation_time>2022-12-03T10:30:00`

  * **order_by** (::String) — Optional. How to order of the results. By default, the results are ordered by create time.

Example orders: `quota_id`, `service, create_time`




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::CloudQuotas::V1::QuotaPreference](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-QuotaPreference)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::CloudQuotas::V1::QuotaPreference](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-QuotaPreference)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_quotas/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudQuotas::V1::CloudQuotas::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudQuotas::V1::ListQuotaPreferencesRequest.new
    
    # Call the list_quota_preferences method.
    result = client.list_quota_preferences request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::CloudQuotas::V1::QuotaPreference.
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



### #update_quota_preference
    
    
    def update_quota_preference(request, options = nil) -> ::Google::Cloud::CloudQuotas::V1::QuotaPreference
    def update_quota_preference(update_mask: nil, quota_preference: nil, allow_missing: nil, validate_only: nil, ignore_safety_checks: nil) -> ::Google::Cloud::CloudQuotas::V1::QuotaPreference

Updates the parameters of a single QuotaPreference. It can updates the config in any states, not just the ones pending approval.

**Overloads**
    
    
    def update_quota_preference(request, options = nil) -> ::Google::Cloud::CloudQuotas::V1::QuotaPreference

Pass arguments to `update_quota_preference` via a request object, either of type [UpdateQuotaPreferenceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-UpdateQuotaPreferenceRequest "Google::Cloud::CloudQuotas::V1::UpdateQuotaPreferenceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudQuotas::V1::UpdateQuotaPreferenceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-UpdateQuotaPreferenceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_quota_preference(update_mask: nil, quota_preference: nil, allow_missing: nil, validate_only: nil, ignore_safety_checks: nil) -> ::Google::Cloud::CloudQuotas::V1::QuotaPreference

Pass arguments to `update_quota_preference` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. Field mask is used to specify the fields to be overwritten in the QuotaPreference resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. 
  * **quota_preference** ([::Google::Cloud::CloudQuotas::V1::QuotaPreference](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-QuotaPreference), ::Hash) — Required. The resource being updated 
  * **allow_missing** (::Boolean) — Optional. If set to true, and the quota preference is not found, a new one will be created. In this situation, `update_mask` is ignored. 
  * **validate_only** (::Boolean) — Optional. If set to true, validate the request, but do not actually update. Note that a request being valid does not mean that the request is guaranteed to be fulfilled. 
  * **ignore_safety_checks** (::Array<[::Google::Cloud::CloudQuotas::V1::QuotaSafetyCheck](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-QuotaSafetyCheck)>) — The list of quota safety checks to be ignored. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::CloudQuotas::V1::QuotaPreference](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-QuotaPreference)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::CloudQuotas::V1::QuotaPreference](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-QuotaPreference)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_quotas/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudQuotas::V1::CloudQuotas::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudQuotas::V1::UpdateQuotaPreferenceRequest.new
    
    # Call the update_quota_preference method.
    result = client.update_quota_preference request
    
    # The returned object is of type Google::Cloud::CloudQuotas::V1::QuotaPreference.
    p result

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
