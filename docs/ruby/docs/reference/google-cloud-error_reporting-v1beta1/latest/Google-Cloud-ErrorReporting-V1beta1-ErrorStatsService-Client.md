---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-error_reporting-v1beta1/latest/Google-Cloud-ErrorReporting-V1beta1-ErrorStatsService-Client/
title: Error Reporting V1beta1 API - Class Google::Cloud::ErrorReporting::V1beta1::ErrorStatsService::Client (v0.17.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:07:05.976116+00:00
---

# Error Reporting V1beta1 API - Class Google::Cloud::ErrorReporting::V1beta1::ErrorStatsService::Client (v0.17.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-error_reporting-v1beta1/latest/Google-Cloud-ErrorReporting-V1beta1-ErrorStatsService-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Error Reporting V1beta1 API - Class Google::Cloud::ErrorReporting::V1beta1::ErrorStatsService::Client (v0.17.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.17.1 (latest)  0.17.0  0.16.0  0.15.1  0.14.0  0.13.1  0.12.0  0.11.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.0  0.5.1  0.4.5 

Reference documentation and code samples for the Error Reporting V1beta1 API class Google::Cloud::ErrorReporting::V1beta1::ErrorStatsService::Client.

Client for the ErrorStatsService service.

An API for retrieving and managing error statistics as well as data for individual events.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::ErrorReporting::V1beta1::ErrorStatsService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-error_reporting-v1beta1/latest/Google-Cloud-ErrorReporting-V1beta1-ErrorStatsService-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the ErrorStatsService Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-error_reporting-v1beta1/latest/Google-Cloud-ErrorReporting-V1beta1-ErrorStatsService-Client-Configuration "Google::Cloud::ErrorReporting::V1beta1::ErrorStatsService::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-error_reporting-v1beta1/latest/Google-Cloud-ErrorReporting-V1beta1-ErrorStatsService-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-error_reporting-v1beta1/latest/Google-Cloud-ErrorReporting-V1beta1-ErrorStatsService-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all ErrorStatsService clients
    ::Google::Cloud::ErrorReporting::V1beta1::ErrorStatsService::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the ErrorStatsService Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-error_reporting-v1beta1/latest/Google-Cloud-ErrorReporting-V1beta1-ErrorStatsService-Client#Google__Cloud__ErrorReporting__V1beta1__ErrorStatsService__Client_configure_class_ "Google::Cloud::ErrorReporting::V1beta1::ErrorStatsService::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-error_reporting-v1beta1/latest/Google-Cloud-ErrorReporting-V1beta1-ErrorStatsService-Client-Configuration "Google::Cloud::ErrorReporting::V1beta1::ErrorStatsService::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-error_reporting-v1beta1/latest/Google-Cloud-ErrorReporting-V1beta1-ErrorStatsService-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-error_reporting-v1beta1/latest/Google-Cloud-ErrorReporting-V1beta1-ErrorStatsService-Client-Configuration)) 



### #delete_events
    
    
    def delete_events(request, options = nil) -> ::Google::Cloud::ErrorReporting::V1beta1::DeleteEventsResponse
    def delete_events(project_name: nil) -> ::Google::Cloud::ErrorReporting::V1beta1::DeleteEventsResponse

Deletes all error events of a given project.

**Overloads**
    
    
    def delete_events(request, options = nil) -> ::Google::Cloud::ErrorReporting::V1beta1::DeleteEventsResponse

Pass arguments to `delete_events` via a request object, either of type [DeleteEventsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-error_reporting-v1beta1/latest/Google-Cloud-ErrorReporting-V1beta1-DeleteEventsRequest "Google::Cloud::ErrorReporting::V1beta1::DeleteEventsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ErrorReporting::V1beta1::DeleteEventsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-error_reporting-v1beta1/latest/Google-Cloud-ErrorReporting-V1beta1-DeleteEventsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_events(project_name: nil) -> ::Google::Cloud::ErrorReporting::V1beta1::DeleteEventsResponse

Pass arguments to `delete_events` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **project_name** (::String) — Required. The resource name of the Google Cloud Platform project. Written as `projects/{projectID}` or `projects/{projectID}/locations/{location}`, where `{projectID}` is the [Google Cloud Platform project ID](https://support.google.com/cloud/answer/6158840) and `{location}` is a Cloud region.

Examples: `projects/my-project-123`, `projects/my-project-123/locations/global`.

For a list of supported locations, see [Supported Regions](https://cloud.google.com/logging/docs/region-support). `global` is the default when unspecified. 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::ErrorReporting::V1beta1::DeleteEventsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-error_reporting-v1beta1/latest/Google-Cloud-ErrorReporting-V1beta1-DeleteEventsResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::ErrorReporting::V1beta1::DeleteEventsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-error_reporting-v1beta1/latest/Google-Cloud-ErrorReporting-V1beta1-DeleteEventsResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/error_reporting/v1beta1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ErrorReporting::V1beta1::ErrorStatsService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ErrorReporting::V1beta1::DeleteEventsRequest.new
    
    # Call the delete_events method.
    result = client.delete_events request
    
    # The returned object is of type Google::Cloud::ErrorReporting::V1beta1::DeleteEventsResponse.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new ErrorStatsService client object.

**Yields**

  * (config) — Configure the ErrorStatsService client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-error_reporting-v1beta1/latest/Google-Cloud-ErrorReporting-V1beta1-ErrorStatsService-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-error_reporting-v1beta1/latest/Google-Cloud-ErrorReporting-V1beta1-ErrorStatsService-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::ErrorReporting::V1beta1::ErrorStatsService::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::ErrorReporting::V1beta1::ErrorStatsService::Client.new do |config|
      config.timeout = 10.0
    end

### #list_events
    
    
    def list_events(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ErrorReporting::V1beta1::ErrorEvent>
    def list_events(project_name: nil, group_id: nil, service_filter: nil, time_range: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ErrorReporting::V1beta1::ErrorEvent>

Lists the specified events.

**Overloads**
    
    
    def list_events(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ErrorReporting::V1beta1::ErrorEvent>

Pass arguments to `list_events` via a request object, either of type [ListEventsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-error_reporting-v1beta1/latest/Google-Cloud-ErrorReporting-V1beta1-ListEventsRequest "Google::Cloud::ErrorReporting::V1beta1::ListEventsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ErrorReporting::V1beta1::ListEventsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-error_reporting-v1beta1/latest/Google-Cloud-ErrorReporting-V1beta1-ListEventsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_events(project_name: nil, group_id: nil, service_filter: nil, time_range: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ErrorReporting::V1beta1::ErrorEvent>

Pass arguments to `list_events` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **project_name** (::String) — Required. The resource name of the Google Cloud Platform project. Written as `projects/{projectID}` or `projects/{projectID}/locations/{location}`, where `{projectID}` is the [Google Cloud Platform project ID](https://support.google.com/cloud/answer/6158840) and `{location}` is a Cloud region.

Examples: `projects/my-project-123`, `projects/my-project-123/locations/global`.

For a list of supported locations, see [Supported Regions](https://cloud.google.com/logging/docs/region-support). `global` is the default when unspecified. 

  * **group_id** (::String) — Required. The group for which events shall be returned. The `group_id` is a unique identifier for a particular error group. The identifier is derived from key parts of the error-log content and is treated as Service Data. For information about how Service Data is handled, see [Google Cloud Privacy Notice](https://cloud.google.com/terms/cloud-privacy-notice). 
  * **service_filter** ([::Google::Cloud::ErrorReporting::V1beta1::ServiceContextFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-error_reporting-v1beta1/latest/Google-Cloud-ErrorReporting-V1beta1-ServiceContextFilter), ::Hash) — Optional. List only ErrorGroups which belong to a service context that matches the filter. Data for all service contexts is returned if this field is not specified. 
  * **time_range** ([::Google::Cloud::ErrorReporting::V1beta1::QueryTimeRange](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-error_reporting-v1beta1/latest/Google-Cloud-ErrorReporting-V1beta1-QueryTimeRange), ::Hash) — Optional. List only data for the given time range. If not set a default time range is used. The field time_range_begin in the response will specify the beginning of this time range. 
  * **page_size** (::Integer) — Optional. The maximum number of results to return per response. 
  * **page_token** (::String) — Optional. A `next_page_token` provided by a previous response. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::ErrorReporting::V1beta1::ErrorEvent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-error_reporting-v1beta1/latest/Google-Cloud-ErrorReporting-V1beta1-ErrorEvent)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::ErrorReporting::V1beta1::ErrorEvent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-error_reporting-v1beta1/latest/Google-Cloud-ErrorReporting-V1beta1-ErrorEvent)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/error_reporting/v1beta1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ErrorReporting::V1beta1::ErrorStatsService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ErrorReporting::V1beta1::ListEventsRequest.new
    
    # Call the list_events method.
    result = client.list_events request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::ErrorReporting::V1beta1::ErrorEvent.
      p item
    end

### #list_group_stats
    
    
    def list_group_stats(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ErrorReporting::V1beta1::ErrorGroupStats>
    def list_group_stats(project_name: nil, group_id: nil, service_filter: nil, time_range: nil, timed_count_duration: nil, alignment: nil, alignment_time: nil, order: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ErrorReporting::V1beta1::ErrorGroupStats>

Lists the specified groups.

**Overloads**
    
    
    def list_group_stats(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ErrorReporting::V1beta1::ErrorGroupStats>

Pass arguments to `list_group_stats` via a request object, either of type [ListGroupStatsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-error_reporting-v1beta1/latest/Google-Cloud-ErrorReporting-V1beta1-ListGroupStatsRequest "Google::Cloud::ErrorReporting::V1beta1::ListGroupStatsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ErrorReporting::V1beta1::ListGroupStatsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-error_reporting-v1beta1/latest/Google-Cloud-ErrorReporting-V1beta1-ListGroupStatsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_group_stats(project_name: nil, group_id: nil, service_filter: nil, time_range: nil, timed_count_duration: nil, alignment: nil, alignment_time: nil, order: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ErrorReporting::V1beta1::ErrorGroupStats>

Pass arguments to `list_group_stats` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **project_name** (::String) — Required. The resource name of the Google Cloud Platform project. Written as `projects/{projectID}` or `projects/{projectNumber}`, where `{projectID}` and `{projectNumber}` can be found in the [Google Cloud console](https://support.google.com/cloud/answer/6158840). It may also include a location, such as `projects/{projectID}/locations/{location}` where `{location}` is a cloud region.

Examples: `projects/my-project-123`, `projects/5551234`, `projects/my-project-123/locations/us-central1`, `projects/5551234/locations/us-central1`.

For a list of supported locations, see [Supported Regions](https://cloud.google.com/logging/docs/region-support). `global` is the default when unspecified. Use `-` as a wildcard to request group stats from all regions. 

  * **group_id** (::Array<::String>) — Optional. List all [ErrorGroupStats] [google.devtools.clouderrorreporting.v1beta1.ErrorGroupStats] with these IDs. The `group_id` is a unique identifier for a particular error group. The identifier is derived from key parts of the error-log content and is treated as Service Data. For information about how Service Data is handled, see [Google Cloud Privacy Notice](https://cloud.google.com/terms/cloud-privacy-notice). 
  * **service_filter** ([::Google::Cloud::ErrorReporting::V1beta1::ServiceContextFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-error_reporting-v1beta1/latest/Google-Cloud-ErrorReporting-V1beta1-ServiceContextFilter), ::Hash) — Optional. List only [ErrorGroupStats] [google.devtools.clouderrorreporting.v1beta1.ErrorGroupStats] which belong to a service context that matches the filter. Data for all service contexts is returned if this field is not specified. 
  * **time_range** ([::Google::Cloud::ErrorReporting::V1beta1::QueryTimeRange](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-error_reporting-v1beta1/latest/Google-Cloud-ErrorReporting-V1beta1-QueryTimeRange), ::Hash) — Optional. List data for the given time range. If not set, a default time range is used. The field [time_range_begin] [google.devtools.clouderrorreporting.v1beta1.ListGroupStatsResponse.time_range_begin] in the response will specify the beginning of this time range. Only [ErrorGroupStats] [google.devtools.clouderrorreporting.v1beta1.ErrorGroupStats] with a non-zero count in the given time range are returned, unless the request contains an explicit [group_id] [google.devtools.clouderrorreporting.v1beta1.ListGroupStatsRequest.group_id] list. If a [group_id] [google.devtools.clouderrorreporting.v1beta1.ListGroupStatsRequest.group_id] list is given, also [ErrorGroupStats] [google.devtools.clouderrorreporting.v1beta1.ErrorGroupStats] with zero occurrences are returned. 
  * **timed_count_duration** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-error_reporting-v1beta1/latest/Google-Protobuf-Duration), ::Hash) — Optional. The preferred duration for a single returned [TimedCount] [google.devtools.clouderrorreporting.v1beta1.TimedCount]. If not set, no timed counts are returned. 
  * **alignment** ([::Google::Cloud::ErrorReporting::V1beta1::TimedCountAlignment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-error_reporting-v1beta1/latest/Google-Cloud-ErrorReporting-V1beta1-TimedCountAlignment)) — Optional. The alignment of the timed counts to be returned. Default is `ALIGNMENT_EQUAL_AT_END`. 
  * **alignment_time** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-error_reporting-v1beta1/latest/Google-Protobuf-Timestamp), ::Hash) — Optional. Time where the timed counts shall be aligned if rounded alignment is chosen. Default is 00:00 UTC. 
  * **order** ([::Google::Cloud::ErrorReporting::V1beta1::ErrorGroupOrder](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-error_reporting-v1beta1/latest/Google-Cloud-ErrorReporting-V1beta1-ErrorGroupOrder)) — Optional. The sort order in which the results are returned. Default is `COUNT_DESC`. 
  * **page_size** (::Integer) — Optional. The maximum number of results to return per response. Default is 20. 
  * **page_token** (::String) — Optional. A [next_page_token] [google.devtools.clouderrorreporting.v1beta1.ListGroupStatsResponse.next_page_token] provided by a previous response. To view additional results, pass this token along with the identical query parameters as the first request. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::ErrorReporting::V1beta1::ErrorGroupStats](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-error_reporting-v1beta1/latest/Google-Cloud-ErrorReporting-V1beta1-ErrorGroupStats)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::ErrorReporting::V1beta1::ErrorGroupStats](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-error_reporting-v1beta1/latest/Google-Cloud-ErrorReporting-V1beta1-ErrorGroupStats)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/error_reporting/v1beta1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ErrorReporting::V1beta1::ErrorStatsService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ErrorReporting::V1beta1::ListGroupStatsRequest.new
    
    # Call the list_group_stats method.
    result = client.list_group_stats request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::ErrorReporting::V1beta1::ErrorGroupStats.
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



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
