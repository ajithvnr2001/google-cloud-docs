---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-trace-v2/latest/Google-Cloud-Trace-V2-TraceService-Client/
title: Cloud Trace V2 API - Class Google::Cloud::Trace::V2::TraceService::Client (v1.5.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:49:59.618034+00:00
---

# Cloud Trace V2 API - Class Google::Cloud::Trace::V2::TraceService::Client (v1.5.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-trace-v2/latest/Google-Cloud-Trace-V2-TraceService-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Trace V2 API - Class Google::Cloud::Trace::V2::TraceService::Client (v1.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.5.1 (latest)  1.5.0  1.4.1  1.3.0  1.2.1  1.1.0  1.0.1  0.9.0  0.8.2  0.7.0  0.6.1  0.5.0  0.4.1  0.3.5 

Reference documentation and code samples for the Cloud Trace V2 API class Google::Cloud::Trace::V2::TraceService::Client.

Client for the TraceService service.

Service for collecting and viewing traces and spans within a trace.

A trace is a collection of spans corresponding to a single operation or a set of operations in an application.

A span is an individual timed event which forms a node of the trace tree. A single trace can contain spans from multiple services.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::Trace::V2::TraceService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-trace-v2/latest/Google-Cloud-Trace-V2-TraceService-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the TraceService Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-trace-v2/latest/Google-Cloud-Trace-V2-TraceService-Client-Configuration "Google::Cloud::Trace::V2::TraceService::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-trace-v2/latest/Google-Cloud-Trace-V2-TraceService-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-trace-v2/latest/Google-Cloud-Trace-V2-TraceService-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all TraceService clients
    ::Google::Cloud::Trace::V2::TraceService::Client.configure do |config|
      config.timeout = 10.0
    end

### #batch_write_spans
    
    
    def batch_write_spans(request, options = nil) -> ::Google::Protobuf::Empty
    def batch_write_spans(name: nil, spans: nil) -> ::Google::Protobuf::Empty

Batch writes new spans to new or existing traces. You cannot update existing spans.

**Overloads**
    
    
    def batch_write_spans(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `batch_write_spans` via a request object, either of type [BatchWriteSpansRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-trace-v2/latest/Google-Cloud-Trace-V2-BatchWriteSpansRequest "Google::Cloud::Trace::V2::BatchWriteSpansRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Trace::V2::BatchWriteSpansRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-trace-v2/latest/Google-Cloud-Trace-V2-BatchWriteSpansRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def batch_write_spans(name: nil, spans: nil) -> ::Google::Protobuf::Empty

Pass arguments to `batch_write_spans` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the project where the spans belong. The format is `projects/[PROJECT_ID]`. 
  * **spans** (::Array<[::Google::Cloud::Trace::V2::Span](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-trace-v2/latest/Google-Cloud-Trace-V2-Span), ::Hash>) — Required. A list of new spans. The span names must not match existing spans, otherwise the results are undefined. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-trace-v2/latest/Google-Protobuf-Empty)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-trace-v2/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/trace/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Trace::V2::TraceService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Trace::V2::BatchWriteSpansRequest.new
    
    # Call the batch_write_spans method.
    result = client.batch_write_spans request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the TraceService Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-trace-v2/latest/Google-Cloud-Trace-V2-TraceService-Client#Google__Cloud__Trace__V2__TraceService__Client_configure_class_ "Google::Cloud::Trace::V2::TraceService::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-trace-v2/latest/Google-Cloud-Trace-V2-TraceService-Client-Configuration "Google::Cloud::Trace::V2::TraceService::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-trace-v2/latest/Google-Cloud-Trace-V2-TraceService-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-trace-v2/latest/Google-Cloud-Trace-V2-TraceService-Client-Configuration)) 



### #create_span
    
    
    def create_span(request, options = nil) -> ::Google::Cloud::Trace::V2::Span
    def create_span(name: nil, span_id: nil, parent_span_id: nil, display_name: nil, start_time: nil, end_time: nil, attributes: nil, stack_trace: nil, time_events: nil, links: nil, status: nil, same_process_as_parent_span: nil, child_span_count: nil, span_kind: nil) -> ::Google::Cloud::Trace::V2::Span

Creates a new span.

**Overloads**
    
    
    def create_span(request, options = nil) -> ::Google::Cloud::Trace::V2::Span

Pass arguments to `create_span` via a request object, either of type [Span](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-trace-v2/latest/Google-Cloud-Trace-V2-Span "Google::Cloud::Trace::V2::Span \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Trace::V2::Span](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-trace-v2/latest/Google-Cloud-Trace-V2-Span), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_span(name: nil, span_id: nil, parent_span_id: nil, display_name: nil, start_time: nil, end_time: nil, attributes: nil, stack_trace: nil, time_events: nil, links: nil, status: nil, same_process_as_parent_span: nil, child_span_count: nil, span_kind: nil) -> ::Google::Cloud::Trace::V2::Span

Pass arguments to `create_span` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The resource name of the span in the following format:

    * `projects/[PROJECT_ID]/traces/[TRACE_ID]/spans/[SPAN_ID]`

`[TRACE_ID]` is a unique identifier for a trace within a project; it is a 32-character hexadecimal encoding of a 16-byte array. It should not be zero.

`[SPAN_ID]` is a unique identifier for a span within a trace; it is a 16-character hexadecimal encoding of an 8-byte array. It should not be zero. . 

  * **span_id** (::String) — Required. The `[SPAN_ID]` portion of the span's resource name. 
  * **parent_span_id** (::String) — The `[SPAN_ID]` of this span's parent span. If this is a root span, then this field must be empty. 
  * **display_name** ([::Google::Cloud::Trace::V2::TruncatableString](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-trace-v2/latest/Google-Cloud-Trace-V2-TruncatableString), ::Hash) — Required. A description of the span's operation (up to 128 bytes). Cloud Trace displays the description in the Cloud console. For example, the display name can be a qualified method name or a file name and a line number where the operation is called. A best practice is to use the same display name within an application and at the same call point. This makes it easier to correlate spans in different traces. 
  * **start_time** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-trace-v2/latest/Google-Protobuf-Timestamp), ::Hash) — Required. The start time of the span. On the client side, this is the time kept by the local machine where the span execution starts. On the server side, this is the time when the server's application handler starts running. 
  * **end_time** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-trace-v2/latest/Google-Protobuf-Timestamp), ::Hash) — Required. The end time of the span. On the client side, this is the time kept by the local machine where the span execution ends. On the server side, this is the time when the server application handler stops running. 
  * **attributes** ([::Google::Cloud::Trace::V2::Span::Attributes](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-trace-v2/latest/Google-Cloud-Trace-V2-Span-Attributes), ::Hash) — A set of attributes on the span. You can have up to 32 attributes per span. 
  * **stack_trace** ([::Google::Cloud::Trace::V2::StackTrace](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-trace-v2/latest/Google-Cloud-Trace-V2-StackTrace), ::Hash) — Stack trace captured at the start of the span. 
  * **time_events** ([::Google::Cloud::Trace::V2::Span::TimeEvents](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-trace-v2/latest/Google-Cloud-Trace-V2-Span-TimeEvents), ::Hash) — A set of time events. You can have up to 32 annotations and 128 message events per span. 
  * **links** ([::Google::Cloud::Trace::V2::Span::Links](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-trace-v2/latest/Google-Cloud-Trace-V2-Span-Links), ::Hash) — Links associated with the span. You can have up to 128 links per Span. 
  * **status** ([::Google::Rpc::Status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-trace-v2/latest/Google-Rpc-Status), ::Hash) — Optional. The final status for this span. 
  * **same_process_as_parent_span** ([::Google::Protobuf::BoolValue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-trace-v2/latest/Google-Protobuf-BoolValue), ::Hash) — Optional. Set this parameter to indicate whether this span is in the same process as its parent. If you do not set this parameter, Trace is unable to take advantage of this helpful information. 
  * **child_span_count** ([::Google::Protobuf::Int32Value](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-trace-v2/latest/Google-Protobuf-Int32Value), ::Hash) — Optional. The number of child spans that were generated while this span was active. If set, allows implementation to detect missing child spans. 
  * **span_kind** ([::Google::Cloud::Trace::V2::Span::SpanKind](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-trace-v2/latest/Google-Cloud-Trace-V2-Span-SpanKind)) — Optional. Distinguishes between spans generated in a particular context. For example, two spans with the same name may be distinguished using `CLIENT` (caller) and `SERVER` (callee) to identify an RPC call. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Trace::V2::Span](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-trace-v2/latest/Google-Cloud-Trace-V2-Span)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Trace::V2::Span](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-trace-v2/latest/Google-Cloud-Trace-V2-Span)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/trace/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Trace::V2::TraceService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Trace::V2::Span.new
    
    # Call the create_span method.
    result = client.create_span request
    
    # The returned object is of type Google::Cloud::Trace::V2::Span.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new TraceService client object.

**Yields**

  * (config) — Configure the TraceService client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-trace-v2/latest/Google-Cloud-Trace-V2-TraceService-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-trace-v2/latest/Google-Cloud-Trace-V2-TraceService-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Trace::V2::TraceService::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Trace::V2::TraceService::Client.new do |config|
      config.timeout = 10.0
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

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
