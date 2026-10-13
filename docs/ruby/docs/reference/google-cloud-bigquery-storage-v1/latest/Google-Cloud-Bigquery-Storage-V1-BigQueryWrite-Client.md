---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage-v1/latest/Google-Cloud-Bigquery-Storage-V1-BigQueryWrite-Client/
title: BigQuery Storage V1 API - Class Google::Cloud::Bigquery::Storage::V1::BigQueryWrite::Client (v1.9.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:06:15.680903+00:00
---

# BigQuery Storage V1 API - Class Google::Cloud::Bigquery::Storage::V1::BigQueryWrite::Client (v1.9.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage-v1/latest/Google-Cloud-Bigquery-Storage-V1-BigQueryWrite-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  BigQuery Storage V1 API - Class Google::Cloud::Bigquery::Storage::V1::BigQueryWrite::Client (v1.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.9.0 (latest)  1.8.1  1.7.0  1.6.0  1.5.1  1.4.0  1.3.1  1.2.0  1.1.0  1.0.1  0.27.0  0.26.0  0.25.2  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.1  0.18.0  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.1  0.10.1  0.9.2 

Reference documentation and code samples for the BigQuery Storage V1 API class Google::Cloud::Bigquery::Storage::V1::BigQueryWrite::Client.

Client for the BigQueryWrite service.

BigQuery Write API.

The Write API can be used to write data to BigQuery.

For supplementary information about the Write API, see: <https://cloud.google.com/bigquery/docs/write-api>

## Inherits

  * Object 



## Includes

  * [Google::Cloud::Bigquery::Storage::V1::BigQueryWrite::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage-v1/latest/Google-Cloud-Bigquery-Storage-V1-BigQueryWrite-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the BigQueryWrite Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage-v1/latest/Google-Cloud-Bigquery-Storage-V1-BigQueryWrite-Client-Configuration "Google::Cloud::Bigquery::Storage::V1::BigQueryWrite::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage-v1/latest/Google-Cloud-Bigquery-Storage-V1-BigQueryWrite-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage-v1/latest/Google-Cloud-Bigquery-Storage-V1-BigQueryWrite-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all BigQueryWrite clients
    ::Google::Cloud::Bigquery::Storage::V1::BigQueryWrite::Client.configure do |config|
      config.timeout = 10.0
    end

### #append_rows
    
    
    def append_rows(request, options = nil) { |response, operation| ... } -> ::Enumerable<::Google::Cloud::Bigquery::Storage::V1::AppendRowsResponse>

Appends data to the given stream.

If `offset` is specified, the `offset` is checked against the end of stream. The server returns `OUT_OF_RANGE` in `AppendRowsResponse` if an attempt is made to append to an offset beyond the current end of the stream or `ALREADY_EXISTS` if user provides an `offset` that has already been written to. User can retry with adjusted offset within the same RPC connection. If `offset` is not specified, append happens at the end of the stream.

The response contains an optional offset at which the append happened. No offset information will be returned for appends to a default stream.

Responses are received in the same order in which requests are sent. There will be one response for each successful inserted request. Responses may optionally embed error information if the originating AppendRequest was not successfully processed.

The specifics of when successfully appended data is made visible to the table are governed by the type of stream:

  * For COMMITTED streams (which includes the default stream), data is visible immediately upon successful append.

  * For BUFFERED streams, data is made visible via a subsequent `FlushRows` rpc which advances a cursor to a newer offset in the stream.

  * For PENDING streams, data is not made visible until the stream itself is finalized (via the `FinalizeWriteStream` rpc), and the stream is explicitly committed via the `BatchCommitWriteStreams` rpc.




**Parameters**

  * **request** (::Gapic::StreamInput, ::Enumerable<[::Google::Cloud::Bigquery::Storage::V1::AppendRowsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage-v1/latest/Google-Cloud-Bigquery-Storage-V1-AppendRowsRequest), ::Hash>) — An enumerable of [AppendRowsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage-v1/latest/Google-Cloud-Bigquery-Storage-V1-AppendRowsRequest "Google::Cloud::Bigquery::Storage::V1::AppendRowsRequest \(class\)") instances. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Enumerable<[::Google::Cloud::Bigquery::Storage::V1::AppendRowsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage-v1/latest/Google-Cloud-Bigquery-Storage-V1-AppendRowsResponse)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Enumerable<[::Google::Cloud::Bigquery::Storage::V1::AppendRowsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage-v1/latest/Google-Cloud-Bigquery-Storage-V1-AppendRowsResponse)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/storage/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::Storage::V1::BigQueryWrite::Client.new
    
    # Create an input stream.
    input = Gapic::StreamInput.new
    
    # Call the append_rows method to start streaming.
    output = client.append_rows input
    
    # Send requests on the stream. For each request object, set fields by
    # passing keyword arguments. Be sure to close the stream when done.
    input << Google::Cloud::Bigquery::Storage::V1::AppendRowsRequest.new
    input << Google::Cloud::Bigquery::Storage::V1::AppendRowsRequest.new
    input.close
    
    # The returned object is a streamed enumerable yielding elements of type
    # ::Google::Cloud::Bigquery::Storage::V1::AppendRowsResponse
    output.each do |current_response|
      p current_response
    end

### #batch_commit_write_streams
    
    
    def batch_commit_write_streams(request, options = nil) -> ::Google::Cloud::Bigquery::Storage::V1::BatchCommitWriteStreamsResponse
    def batch_commit_write_streams(parent: nil, write_streams: nil) -> ::Google::Cloud::Bigquery::Storage::V1::BatchCommitWriteStreamsResponse

Atomically commits a group of `PENDING` streams that belong to the same `parent` table.

Streams must be finalized before commit and cannot be committed multiple times. Once a stream is committed, data in the stream becomes available for read operations.

**Overloads**
    
    
    def batch_commit_write_streams(request, options = nil) -> ::Google::Cloud::Bigquery::Storage::V1::BatchCommitWriteStreamsResponse

Pass arguments to `batch_commit_write_streams` via a request object, either of type [Google::Cloud::Bigquery::Storage::V1::BatchCommitWriteStreamsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage-v1/latest/Google-Cloud-Bigquery-Storage-V1-BatchCommitWriteStreamsRequest "Google::Cloud::Bigquery::Storage::V1::BatchCommitWriteStreamsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::Storage::V1::BatchCommitWriteStreamsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage-v1/latest/Google-Cloud-Bigquery-Storage-V1-BatchCommitWriteStreamsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def batch_commit_write_streams(parent: nil, write_streams: nil) -> ::Google::Cloud::Bigquery::Storage::V1::BatchCommitWriteStreamsResponse

Pass arguments to `batch_commit_write_streams` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Parent table that all the streams should belong to, in the form of `projects/{project}/datasets/{dataset}/tables/{table}`. 
  * **write_streams** (::Array<::String>) — Required. The group of streams that will be committed atomically. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Bigquery::Storage::V1::BatchCommitWriteStreamsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage-v1/latest/Google-Cloud-Bigquery-Storage-V1-BatchCommitWriteStreamsResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Bigquery::Storage::V1::BatchCommitWriteStreamsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage-v1/latest/Google-Cloud-Bigquery-Storage-V1-BatchCommitWriteStreamsResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/storage/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::Storage::V1::BigQueryWrite::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::Storage::V1::BatchCommitWriteStreamsRequest.new
    
    # Call the batch_commit_write_streams method.
    result = client.batch_commit_write_streams request
    
    # The returned object is of type Google::Cloud::Bigquery::Storage::V1::BatchCommitWriteStreamsResponse.
    p result

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the BigQueryWrite Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage-v1/latest/Google-Cloud-Bigquery-Storage-V1-BigQueryWrite-Client#Google__Cloud__Bigquery__Storage__V1__BigQueryWrite__Client_configure_class_ "Google::Cloud::Bigquery::Storage::V1::BigQueryWrite::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage-v1/latest/Google-Cloud-Bigquery-Storage-V1-BigQueryWrite-Client-Configuration "Google::Cloud::Bigquery::Storage::V1::BigQueryWrite::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage-v1/latest/Google-Cloud-Bigquery-Storage-V1-BigQueryWrite-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage-v1/latest/Google-Cloud-Bigquery-Storage-V1-BigQueryWrite-Client-Configuration)) 



### #create_write_stream
    
    
    def create_write_stream(request, options = nil) -> ::Google::Cloud::Bigquery::Storage::V1::WriteStream
    def create_write_stream(parent: nil, write_stream: nil) -> ::Google::Cloud::Bigquery::Storage::V1::WriteStream

Creates a write stream to the given table. Additionally, every table has a special stream named '_default' to which data can be written. This stream doesn't need to be created using CreateWriteStream. It is a stream that can be used simultaneously by any number of clients. Data written to this stream is considered committed as soon as an acknowledgement is received.

**Overloads**
    
    
    def create_write_stream(request, options = nil) -> ::Google::Cloud::Bigquery::Storage::V1::WriteStream

Pass arguments to `create_write_stream` via a request object, either of type [CreateWriteStreamRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage-v1/latest/Google-Cloud-Bigquery-Storage-V1-CreateWriteStreamRequest "Google::Cloud::Bigquery::Storage::V1::CreateWriteStreamRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::Storage::V1::CreateWriteStreamRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage-v1/latest/Google-Cloud-Bigquery-Storage-V1-CreateWriteStreamRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_write_stream(parent: nil, write_stream: nil) -> ::Google::Cloud::Bigquery::Storage::V1::WriteStream

Pass arguments to `create_write_stream` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Reference to the table to which the stream belongs, in the format of `projects/{project}/datasets/{dataset}/tables/{table}`. 
  * **write_stream** ([::Google::Cloud::Bigquery::Storage::V1::WriteStream](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage-v1/latest/Google-Cloud-Bigquery-Storage-V1-WriteStream), ::Hash) — Required. Stream to be created. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Bigquery::Storage::V1::WriteStream](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage-v1/latest/Google-Cloud-Bigquery-Storage-V1-WriteStream)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Bigquery::Storage::V1::WriteStream](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage-v1/latest/Google-Cloud-Bigquery-Storage-V1-WriteStream)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/storage/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::Storage::V1::BigQueryWrite::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::Storage::V1::CreateWriteStreamRequest.new
    
    # Call the create_write_stream method.
    result = client.create_write_stream request
    
    # The returned object is of type Google::Cloud::Bigquery::Storage::V1::WriteStream.
    p result

### #finalize_write_stream
    
    
    def finalize_write_stream(request, options = nil) -> ::Google::Cloud::Bigquery::Storage::V1::FinalizeWriteStreamResponse
    def finalize_write_stream(name: nil) -> ::Google::Cloud::Bigquery::Storage::V1::FinalizeWriteStreamResponse

Finalize a write stream so that no new data can be appended to the stream. Finalize is not supported on the '_default' stream.

**Overloads**
    
    
    def finalize_write_stream(request, options = nil) -> ::Google::Cloud::Bigquery::Storage::V1::FinalizeWriteStreamResponse

Pass arguments to `finalize_write_stream` via a request object, either of type [FinalizeWriteStreamRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage-v1/latest/Google-Cloud-Bigquery-Storage-V1-FinalizeWriteStreamRequest "Google::Cloud::Bigquery::Storage::V1::FinalizeWriteStreamRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::Storage::V1::FinalizeWriteStreamRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage-v1/latest/Google-Cloud-Bigquery-Storage-V1-FinalizeWriteStreamRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def finalize_write_stream(name: nil) -> ::Google::Cloud::Bigquery::Storage::V1::FinalizeWriteStreamResponse

Pass arguments to `finalize_write_stream` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Name of the stream to finalize, in the form of `projects/{project}/datasets/{dataset}/tables/{table}/streams/{stream}`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Bigquery::Storage::V1::FinalizeWriteStreamResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage-v1/latest/Google-Cloud-Bigquery-Storage-V1-FinalizeWriteStreamResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Bigquery::Storage::V1::FinalizeWriteStreamResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage-v1/latest/Google-Cloud-Bigquery-Storage-V1-FinalizeWriteStreamResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/storage/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::Storage::V1::BigQueryWrite::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::Storage::V1::FinalizeWriteStreamRequest.new
    
    # Call the finalize_write_stream method.
    result = client.finalize_write_stream request
    
    # The returned object is of type Google::Cloud::Bigquery::Storage::V1::FinalizeWriteStreamResponse.
    p result

### #flush_rows
    
    
    def flush_rows(request, options = nil) -> ::Google::Cloud::Bigquery::Storage::V1::FlushRowsResponse
    def flush_rows(write_stream: nil, offset: nil) -> ::Google::Cloud::Bigquery::Storage::V1::FlushRowsResponse

Flushes rows to a BUFFERED stream.

If users are appending rows to BUFFERED stream, flush operation is required in order for the rows to become available for reading. A Flush operation flushes up to any previously flushed offset in a BUFFERED stream, to the offset specified in the request.

Flush is not supported on the _default stream, since it is not BUFFERED.

**Overloads**
    
    
    def flush_rows(request, options = nil) -> ::Google::Cloud::Bigquery::Storage::V1::FlushRowsResponse

Pass arguments to `flush_rows` via a request object, either of type [FlushRowsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage-v1/latest/Google-Cloud-Bigquery-Storage-V1-FlushRowsRequest "Google::Cloud::Bigquery::Storage::V1::FlushRowsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::Storage::V1::FlushRowsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage-v1/latest/Google-Cloud-Bigquery-Storage-V1-FlushRowsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def flush_rows(write_stream: nil, offset: nil) -> ::Google::Cloud::Bigquery::Storage::V1::FlushRowsResponse

Pass arguments to `flush_rows` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **write_stream** (::String) — Required. The stream that is the target of the flush operation. 
  * **offset** ([::Google::Protobuf::Int64Value](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage-v1/latest/Google-Protobuf-Int64Value), ::Hash) — Ending offset of the flush operation. Rows before this offset(including this offset) will be flushed. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Bigquery::Storage::V1::FlushRowsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage-v1/latest/Google-Cloud-Bigquery-Storage-V1-FlushRowsResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Bigquery::Storage::V1::FlushRowsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage-v1/latest/Google-Cloud-Bigquery-Storage-V1-FlushRowsResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/storage/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::Storage::V1::BigQueryWrite::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::Storage::V1::FlushRowsRequest.new
    
    # Call the flush_rows method.
    result = client.flush_rows request
    
    # The returned object is of type Google::Cloud::Bigquery::Storage::V1::FlushRowsResponse.
    p result

### #get_write_stream
    
    
    def get_write_stream(request, options = nil) -> ::Google::Cloud::Bigquery::Storage::V1::WriteStream
    def get_write_stream(name: nil, view: nil) -> ::Google::Cloud::Bigquery::Storage::V1::WriteStream

Gets information about a write stream.

**Overloads**
    
    
    def get_write_stream(request, options = nil) -> ::Google::Cloud::Bigquery::Storage::V1::WriteStream

Pass arguments to `get_write_stream` via a request object, either of type [GetWriteStreamRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage-v1/latest/Google-Cloud-Bigquery-Storage-V1-GetWriteStreamRequest "Google::Cloud::Bigquery::Storage::V1::GetWriteStreamRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::Storage::V1::GetWriteStreamRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage-v1/latest/Google-Cloud-Bigquery-Storage-V1-GetWriteStreamRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_write_stream(name: nil, view: nil) -> ::Google::Cloud::Bigquery::Storage::V1::WriteStream

Pass arguments to `get_write_stream` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Name of the stream to get, in the form of `projects/{project}/datasets/{dataset}/tables/{table}/streams/{stream}`. 
  * **view** ([::Google::Cloud::Bigquery::Storage::V1::WriteStreamView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage-v1/latest/Google-Cloud-Bigquery-Storage-V1-WriteStreamView)) — Indicates whether to get full or partial view of the WriteStream. If not set, view returned will be basic. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Bigquery::Storage::V1::WriteStream](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage-v1/latest/Google-Cloud-Bigquery-Storage-V1-WriteStream)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Bigquery::Storage::V1::WriteStream](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage-v1/latest/Google-Cloud-Bigquery-Storage-V1-WriteStream)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/storage/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::Storage::V1::BigQueryWrite::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::Storage::V1::GetWriteStreamRequest.new
    
    # Call the get_write_stream method.
    result = client.get_write_stream request
    
    # The returned object is of type Google::Cloud::Bigquery::Storage::V1::WriteStream.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new BigQueryWrite client object.

**Yields**

  * (config) — Configure the BigQueryWrite client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage-v1/latest/Google-Cloud-Bigquery-Storage-V1-BigQueryWrite-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage-v1/latest/Google-Cloud-Bigquery-Storage-V1-BigQueryWrite-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Bigquery::Storage::V1::BigQueryWrite::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Bigquery::Storage::V1::BigQueryWrite::Client.new do |config|
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

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
