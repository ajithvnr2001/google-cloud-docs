---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BigQueryWriteClient
title: Class BigQueryWriteClient (3.35.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:59:20.380882+00:00
---

# Class BigQueryWriteClient (3.35.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BigQueryWriteClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class BigQueryWriteClient (3.35.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.35.0 (latest)  3.31.0  3.30.0  3.29.0  3.27.0  3.24.0  3.23.0  3.21.0  3.20.0  3.19.1  3.18.0  3.17.3  3.16.3  3.15.3  3.14.1  3.12.0  3.11.4  3.10.3  3.9.3  3.8.0  3.6.1  3.5.2  3.4.0  3.3.1  3.2.0  3.1.0  3.0.1  2.47.0  2.45.0  2.44.1  2.43.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-bigquerystorage/google-cloud-bigquerystorage/src/main/java/com/google/cloud/bigquery/storage/v1/BigQueryWriteClient.java)| [Product Reference](https://cloud.google.com/bigquery/docs/reference/storage/)  
---|---  
  
Service Description: BigQuery Write API.

The Write API can be used to write data to BigQuery.

For supplementary information about the Write API, see: <https://cloud.google.com/bigquery/docs/write-api>

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BigQueryWriteClient bigQueryWriteClient = BigQueryWriteClient.create()) {
       TableName parent = TableName.of("[PROJECT]", "[DATASET]", "[TABLE]");
       WriteStream writeStream = WriteStream.newBuilder().build();
       WriteStream response = bigQueryWriteClient.createWriteStream(parent, writeStream);
     }
     

Note: close() needs to be called on the BigQueryWriteClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateWriteStream |  Creates a write stream to the given table. Additionally, every table has a special stream named '_default' to which data can be written. This stream doesn't need to be created using CreateWriteStream. It is a stream that can be used simultaneously by any number of clients. Data written to this stream is considered committed as soon as an acknowledgement is received. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createWriteStream(CreateWriteStreamRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createWriteStream(TableName parent, WriteStream writeStream) 
  * createWriteStream(String parent, WriteStream writeStream) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createWriteStreamCallable() 

  
AppendRows |  Appends data to the given stream.  If `offset` is specified, the `offset` is checked against the end of stream. The server returns `OUT_OF_RANGE` in `AppendRowsResponse` if an attempt is made to append to an offset beyond the current end of the stream or `ALREADY_EXISTS` if user provides an `offset` that has already been written to. User can retry with adjusted offset within the same RPC connection. If `offset` is not specified, append happens at the end of the stream.  The response contains an optional offset at which the append happened. No offset information will be returned for appends to a default stream.  Responses are received in the same order in which requests are sent. There will be one response for each successful inserted request. Responses may optionally embed error information if the originating AppendRequest was not successfully processed.  The specifics of when successfully appended data is made visible to the table are governed by the type of stream: 

  * For COMMITTED streams (which includes the default stream), data is visible immediately upon successful append. 


  * For BUFFERED streams, data is made visible via a subsequent `FlushRows` rpc which advances a cursor to a newer offset in the stream. 


  * For PENDING streams, data is not made visible until the stream itself is finalized (via the `FinalizeWriteStream` rpc), and the stream is explicitly committed via the `BatchCommitWriteStreams` rpc. 

|  Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * appendRowsCallable() 

  
GetWriteStream |  Gets information about a write stream. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getWriteStream(GetWriteStreamRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getWriteStream(WriteStreamName name) 
  * getWriteStream(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getWriteStreamCallable() 

  
FinalizeWriteStream |  Finalize a write stream so that no new data can be appended to the stream. Finalize is not supported on the '_default' stream. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * finalizeWriteStream(FinalizeWriteStreamRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * finalizeWriteStream(WriteStreamName name) 
  * finalizeWriteStream(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * finalizeWriteStreamCallable() 

  
BatchCommitWriteStreams |  Atomically commits a group of `PENDING` streams that belong to the same `parent` table.  Streams must be finalized before commit and cannot be committed multiple times. Once a stream is committed, data in the stream becomes available for read operations. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchCommitWriteStreams(BatchCommitWriteStreamsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchCommitWriteStreams(TableName parent) 
  * batchCommitWriteStreams(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchCommitWriteStreamsCallable() 

  
FlushRows |  Flushes rows to a BUFFERED stream.  If users are appending rows to BUFFERED stream, flush operation is required in order for the rows to become available for reading. A Flush operation flushes up to any previously flushed offset in a BUFFERED stream, to the offset specified in the request.  Flush is not supported on the _default stream, since it is not BUFFERED. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * flushRows(FlushRowsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * flushRows(WriteStreamName writeStream) 
  * flushRows(String writeStream) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * flushRowsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of BigQueryWriteSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     BigQueryWriteSettings bigQueryWriteSettings =
         BigQueryWriteSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     BigQueryWriteClient bigQueryWriteClient = BigQueryWriteClient.create(bigQueryWriteSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     BigQueryWriteSettings bigQueryWriteSettings =
         BigQueryWriteSettings.newBuilder().setEndpoint(myEndpoint).build();
     BigQueryWriteClient bigQueryWriteClient = BigQueryWriteClient.create(bigQueryWriteSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > BigQueryWriteClient

## Static Methods 

### create()
    
    
    public static final BigQueryWriteClient create()

Constructs an instance of BigQueryWriteClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[BigQueryWriteClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BigQueryWriteClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(BigQueryWriteSettings settings)
    
    
    public static final BigQueryWriteClient create(BigQueryWriteSettings settings)

Constructs an instance of BigQueryWriteClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[BigQueryWriteSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BigQueryWriteSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BigQueryWriteClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BigQueryWriteClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(BigQueryWriteStub stub)
    
    
    public static final BigQueryWriteClient create(BigQueryWriteStub stub)

Constructs an instance of BigQueryWriteClient, using the given stub for making calls. This is for advanced usage - prefer using create(BigQueryWriteSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[BigQueryWriteStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.stub.BigQueryWriteStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BigQueryWriteClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BigQueryWriteClient)` |   
  
## Constructors 

### BigQueryWriteClient(BigQueryWriteSettings settings)
    
    
    protected BigQueryWriteClient(BigQueryWriteSettings settings)

Constructs an instance of BigQueryWriteClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[BigQueryWriteSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BigQueryWriteSettings)`  
  
  
### BigQueryWriteClient(BigQueryWriteStub stub)
    
    
    protected BigQueryWriteClient(BigQueryWriteStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[BigQueryWriteStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.stub.BigQueryWriteStub)`  
  
  
## Methods 

### appendRowsCallable()
    
    
    public final BidiStreamingCallable<AppendRowsRequest,AppendRowsResponse> appendRowsCallable()

Appends data to the given stream.

If `offset` is specified, the `offset` is checked against the end of stream. The server returns `OUT_OF_RANGE` in `AppendRowsResponse` if an attempt is made to append to an offset beyond the current end of the stream or `ALREADY_EXISTS` if user provides an `offset` that has already been written to. User can retry with adjusted offset within the same RPC connection. If `offset` is not specified, append happens at the end of the stream.

The response contains an optional offset at which the append happened. No offset information will be returned for appends to a default stream.

Responses are received in the same order in which requests are sent. There will be one response for each successful inserted request. Responses may optionally embed error information if the originating AppendRequest was not successfully processed.

The specifics of when successfully appended data is made visible to the table are governed by the type of stream:

  * For COMMITTED streams (which includes the default stream), data is visible immediately upon successful append. 


  * For BUFFERED streams, data is made visible via a subsequent `FlushRows` rpc which advances a cursor to a newer offset in the stream. 


  * For PENDING streams, data is not made visible until the stream itself is finalized (via the `FinalizeWriteStream` rpc), and the stream is explicitly committed via the `BatchCommitWriteStreams` rpc. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BigQueryWriteClient bigQueryWriteClient = BigQueryWriteClient.create()) {
       BidiStream<AppendRowsRequest, AppendRowsResponse> bidiStream =
           bigQueryWriteClient.appendRowsCallable().call();
       AppendRowsRequest request =
           AppendRowsRequest.newBuilder()
               .setWriteStream(
                   WriteStreamName.of("[PROJECT]", "[DATASET]", "[TABLE]", "[STREAM]").toString())
               .setOffset(Int64Value.newBuilder().build())
               .setTraceId("traceId-1067401920")
               .putAllMissingValueInterpretations(
                   new HashMap<String, AppendRowsRequest.MissingValueInterpretation>())
               .setClientStats(ClientStats.newBuilder().build())
               .build();
       bidiStream.send(request);
       for (AppendRowsResponse response : bidiStream) {
         // Do something when a response is received.
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[BidiStreamingCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.BidiStreamingCallable.html)<[AppendRowsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest),[AppendRowsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsResponse)>` |   
  
### awaitTermination(long duration, TimeUnit unit)
    
    
    public boolean awaitTermination(long duration, TimeUnit unit)

**Parameters**  
---  
**Name** | **Description**  
`duration` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`unit` | `[TimeUnit](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/TimeUnit.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InterruptedException](https://docs.oracle.com/javase/8/docs/api/java/lang/InterruptedException.html)` |   
  
### batchCommitWriteStreams(@Nullable TableName parent)
    
    
    public final BatchCommitWriteStreamsResponse batchCommitWriteStreams(@Nullable TableName parent)

Atomically commits a group of `PENDING` streams that belong to the same `parent` table.

Streams must be finalized before commit and cannot be committed multiple times. Once a stream is committed, data in the stream becomes available for read operations.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BigQueryWriteClient bigQueryWriteClient = BigQueryWriteClient.create()) {
       TableName parent = TableName.of("[PROJECT]", "[DATASET]", "[TABLE]");
       BatchCommitWriteStreamsResponse response =
           bigQueryWriteClient.batchCommitWriteStreams(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.bigquery.storage.v1.TableName`  
Required. Parent table that all the streams should belong to, in the form of `projects/{project}/datasets/{dataset}/tables/{table}`.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCommitWriteStreamsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BatchCommitWriteStreamsResponse)` |   
  
### batchCommitWriteStreams(BatchCommitWriteStreamsRequest request)
    
    
    public final BatchCommitWriteStreamsResponse batchCommitWriteStreams(BatchCommitWriteStreamsRequest request)

Atomically commits a group of `PENDING` streams that belong to the same `parent` table.

Streams must be finalized before commit and cannot be committed multiple times. Once a stream is committed, data in the stream becomes available for read operations.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BigQueryWriteClient bigQueryWriteClient = BigQueryWriteClient.create()) {
       BatchCommitWriteStreamsRequest request =
           BatchCommitWriteStreamsRequest.newBuilder()
               .setParent(TableName.of("[PROJECT]", "[DATASET]", "[TABLE]").toString())
               .addAllWriteStreams(new ArrayList<String>())
               .build();
       BatchCommitWriteStreamsResponse response =
           bigQueryWriteClient.batchCommitWriteStreams(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchCommitWriteStreamsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BatchCommitWriteStreamsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCommitWriteStreamsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BatchCommitWriteStreamsResponse)` |   
  
### batchCommitWriteStreams(String parent)
    
    
    public final BatchCommitWriteStreamsResponse batchCommitWriteStreams(String parent)

Atomically commits a group of `PENDING` streams that belong to the same `parent` table.

Streams must be finalized before commit and cannot be committed multiple times. Once a stream is committed, data in the stream becomes available for read operations.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BigQueryWriteClient bigQueryWriteClient = BigQueryWriteClient.create()) {
       String parent = TableName.of("[PROJECT]", "[DATASET]", "[TABLE]").toString();
       BatchCommitWriteStreamsResponse response =
           bigQueryWriteClient.batchCommitWriteStreams(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Parent table that all the streams should belong to, in the form of `projects/{project}/datasets/{dataset}/tables/{table}`.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCommitWriteStreamsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BatchCommitWriteStreamsResponse)` |   
  
### batchCommitWriteStreamsCallable()
    
    
    public final UnaryCallable<BatchCommitWriteStreamsRequest,BatchCommitWriteStreamsResponse> batchCommitWriteStreamsCallable()

Atomically commits a group of `PENDING` streams that belong to the same `parent` table.

Streams must be finalized before commit and cannot be committed multiple times. Once a stream is committed, data in the stream becomes available for read operations.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BigQueryWriteClient bigQueryWriteClient = BigQueryWriteClient.create()) {
       BatchCommitWriteStreamsRequest request =
           BatchCommitWriteStreamsRequest.newBuilder()
               .setParent(TableName.of("[PROJECT]", "[DATASET]", "[TABLE]").toString())
               .addAllWriteStreams(new ArrayList<String>())
               .build();
       ApiFuture<BatchCommitWriteStreamsResponse> future =
           bigQueryWriteClient.batchCommitWriteStreamsCallable().futureCall(request);
       // Do something.
       BatchCommitWriteStreamsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchCommitWriteStreamsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BatchCommitWriteStreamsRequest),[BatchCommitWriteStreamsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BatchCommitWriteStreamsResponse)>` |   
  
### close()
    
    
    public final void close()

### createWriteStream(@Nullable TableName parent, WriteStream writeStream)
    
    
    public final WriteStream createWriteStream(@Nullable TableName parent, WriteStream writeStream)

Creates a write stream to the given table. Additionally, every table has a special stream named '_default' to which data can be written. This stream doesn't need to be created using CreateWriteStream. It is a stream that can be used simultaneously by any number of clients. Data written to this stream is considered committed as soon as an acknowledgement is received.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BigQueryWriteClient bigQueryWriteClient = BigQueryWriteClient.create()) {
       TableName parent = TableName.of("[PROJECT]", "[DATASET]", "[TABLE]");
       WriteStream writeStream = WriteStream.newBuilder().build();
       WriteStream response = bigQueryWriteClient.createWriteStream(parent, writeStream);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.bigquery.storage.v1.TableName`  
Required. Reference to the table to which the stream belongs, in the format of `projects/{project}/datasets/{dataset}/tables/{table}`.  
`writeStream` | `[WriteStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.WriteStream)`  
Required. Stream to be created.  
**Returns**  
---  
**Type** | **Description**  
`[WriteStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.WriteStream)` |   
  
### createWriteStream(CreateWriteStreamRequest request)
    
    
    public final WriteStream createWriteStream(CreateWriteStreamRequest request)

Creates a write stream to the given table. Additionally, every table has a special stream named '_default' to which data can be written. This stream doesn't need to be created using CreateWriteStream. It is a stream that can be used simultaneously by any number of clients. Data written to this stream is considered committed as soon as an acknowledgement is received.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BigQueryWriteClient bigQueryWriteClient = BigQueryWriteClient.create()) {
       CreateWriteStreamRequest request =
           CreateWriteStreamRequest.newBuilder()
               .setParent(TableName.of("[PROJECT]", "[DATASET]", "[TABLE]").toString())
               .setWriteStream(WriteStream.newBuilder().build())
               .build();
       WriteStream response = bigQueryWriteClient.createWriteStream(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateWriteStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.CreateWriteStreamRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[WriteStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.WriteStream)` |   
  
### createWriteStream(String parent, WriteStream writeStream)
    
    
    public final WriteStream createWriteStream(String parent, WriteStream writeStream)

Creates a write stream to the given table. Additionally, every table has a special stream named '_default' to which data can be written. This stream doesn't need to be created using CreateWriteStream. It is a stream that can be used simultaneously by any number of clients. Data written to this stream is considered committed as soon as an acknowledgement is received.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BigQueryWriteClient bigQueryWriteClient = BigQueryWriteClient.create()) {
       String parent = TableName.of("[PROJECT]", "[DATASET]", "[TABLE]").toString();
       WriteStream writeStream = WriteStream.newBuilder().build();
       WriteStream response = bigQueryWriteClient.createWriteStream(parent, writeStream);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Reference to the table to which the stream belongs, in the format of `projects/{project}/datasets/{dataset}/tables/{table}`.  
`writeStream` | `[WriteStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.WriteStream)`  
Required. Stream to be created.  
**Returns**  
---  
**Type** | **Description**  
`[WriteStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.WriteStream)` |   
  
### createWriteStreamCallable()
    
    
    public final UnaryCallable<CreateWriteStreamRequest,WriteStream> createWriteStreamCallable()

Creates a write stream to the given table. Additionally, every table has a special stream named '_default' to which data can be written. This stream doesn't need to be created using CreateWriteStream. It is a stream that can be used simultaneously by any number of clients. Data written to this stream is considered committed as soon as an acknowledgement is received.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BigQueryWriteClient bigQueryWriteClient = BigQueryWriteClient.create()) {
       CreateWriteStreamRequest request =
           CreateWriteStreamRequest.newBuilder()
               .setParent(TableName.of("[PROJECT]", "[DATASET]", "[TABLE]").toString())
               .setWriteStream(WriteStream.newBuilder().build())
               .build();
       ApiFuture<WriteStream> future =
           bigQueryWriteClient.createWriteStreamCallable().futureCall(request);
       // Do something.
       WriteStream response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateWriteStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.CreateWriteStreamRequest),[WriteStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.WriteStream)>` |   
  
### finalizeWriteStream(@Nullable WriteStreamName name)
    
    
    public final FinalizeWriteStreamResponse finalizeWriteStream(@Nullable WriteStreamName name)

Finalize a write stream so that no new data can be appended to the stream. Finalize is not supported on the '_default' stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BigQueryWriteClient bigQueryWriteClient = BigQueryWriteClient.create()) {
       WriteStreamName name = WriteStreamName.of("[PROJECT]", "[DATASET]", "[TABLE]", "[STREAM]");
       FinalizeWriteStreamResponse response = bigQueryWriteClient.finalizeWriteStream(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.bigquery.storage.v1.WriteStreamName`  
Required. Name of the stream to finalize, in the form of `projects/{project}/datasets/{dataset}/tables/{table}/streams/{stream}`.  
**Returns**  
---  
**Type** | **Description**  
`[FinalizeWriteStreamResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.FinalizeWriteStreamResponse)` |   
  
### finalizeWriteStream(FinalizeWriteStreamRequest request)
    
    
    public final FinalizeWriteStreamResponse finalizeWriteStream(FinalizeWriteStreamRequest request)

Finalize a write stream so that no new data can be appended to the stream. Finalize is not supported on the '_default' stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BigQueryWriteClient bigQueryWriteClient = BigQueryWriteClient.create()) {
       FinalizeWriteStreamRequest request =
           FinalizeWriteStreamRequest.newBuilder()
               .setName(
                   WriteStreamName.of("[PROJECT]", "[DATASET]", "[TABLE]", "[STREAM]").toString())
               .build();
       FinalizeWriteStreamResponse response = bigQueryWriteClient.finalizeWriteStream(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FinalizeWriteStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.FinalizeWriteStreamRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FinalizeWriteStreamResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.FinalizeWriteStreamResponse)` |   
  
### finalizeWriteStream(String name)
    
    
    public final FinalizeWriteStreamResponse finalizeWriteStream(String name)

Finalize a write stream so that no new data can be appended to the stream. Finalize is not supported on the '_default' stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BigQueryWriteClient bigQueryWriteClient = BigQueryWriteClient.create()) {
       String name = WriteStreamName.of("[PROJECT]", "[DATASET]", "[TABLE]", "[STREAM]").toString();
       FinalizeWriteStreamResponse response = bigQueryWriteClient.finalizeWriteStream(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the stream to finalize, in the form of `projects/{project}/datasets/{dataset}/tables/{table}/streams/{stream}`.  
**Returns**  
---  
**Type** | **Description**  
`[FinalizeWriteStreamResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.FinalizeWriteStreamResponse)` |   
  
### finalizeWriteStreamCallable()
    
    
    public final UnaryCallable<FinalizeWriteStreamRequest,FinalizeWriteStreamResponse> finalizeWriteStreamCallable()

Finalize a write stream so that no new data can be appended to the stream. Finalize is not supported on the '_default' stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BigQueryWriteClient bigQueryWriteClient = BigQueryWriteClient.create()) {
       FinalizeWriteStreamRequest request =
           FinalizeWriteStreamRequest.newBuilder()
               .setName(
                   WriteStreamName.of("[PROJECT]", "[DATASET]", "[TABLE]", "[STREAM]").toString())
               .build();
       ApiFuture<FinalizeWriteStreamResponse> future =
           bigQueryWriteClient.finalizeWriteStreamCallable().futureCall(request);
       // Do something.
       FinalizeWriteStreamResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FinalizeWriteStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.FinalizeWriteStreamRequest),[FinalizeWriteStreamResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.FinalizeWriteStreamResponse)>` |   
  
### flushRows(@Nullable WriteStreamName writeStream)
    
    
    public final FlushRowsResponse flushRows(@Nullable WriteStreamName writeStream)

Flushes rows to a BUFFERED stream.

If users are appending rows to BUFFERED stream, flush operation is required in order for the rows to become available for reading. A Flush operation flushes up to any previously flushed offset in a BUFFERED stream, to the offset specified in the request.

Flush is not supported on the _default stream, since it is not BUFFERED.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BigQueryWriteClient bigQueryWriteClient = BigQueryWriteClient.create()) {
       WriteStreamName writeStream =
           WriteStreamName.of("[PROJECT]", "[DATASET]", "[TABLE]", "[STREAM]");
       FlushRowsResponse response = bigQueryWriteClient.flushRows(writeStream);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`writeStream` | `@org.jspecify.annotations.Nullable com.google.cloud.bigquery.storage.v1.WriteStreamName`  
Required. The stream that is the target of the flush operation.  
**Returns**  
---  
**Type** | **Description**  
`[FlushRowsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.FlushRowsResponse)` |   
  
### flushRows(FlushRowsRequest request)
    
    
    public final FlushRowsResponse flushRows(FlushRowsRequest request)

Flushes rows to a BUFFERED stream.

If users are appending rows to BUFFERED stream, flush operation is required in order for the rows to become available for reading. A Flush operation flushes up to any previously flushed offset in a BUFFERED stream, to the offset specified in the request.

Flush is not supported on the _default stream, since it is not BUFFERED.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BigQueryWriteClient bigQueryWriteClient = BigQueryWriteClient.create()) {
       FlushRowsRequest request =
           FlushRowsRequest.newBuilder()
               .setWriteStream(
                   WriteStreamName.of("[PROJECT]", "[DATASET]", "[TABLE]", "[STREAM]").toString())
               .setOffset(Int64Value.newBuilder().build())
               .build();
       FlushRowsResponse response = bigQueryWriteClient.flushRows(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FlushRowsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.FlushRowsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FlushRowsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.FlushRowsResponse)` |   
  
### flushRows(String writeStream)
    
    
    public final FlushRowsResponse flushRows(String writeStream)

Flushes rows to a BUFFERED stream.

If users are appending rows to BUFFERED stream, flush operation is required in order for the rows to become available for reading. A Flush operation flushes up to any previously flushed offset in a BUFFERED stream, to the offset specified in the request.

Flush is not supported on the _default stream, since it is not BUFFERED.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BigQueryWriteClient bigQueryWriteClient = BigQueryWriteClient.create()) {
       String writeStream =
           WriteStreamName.of("[PROJECT]", "[DATASET]", "[TABLE]", "[STREAM]").toString();
       FlushRowsResponse response = bigQueryWriteClient.flushRows(writeStream);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`writeStream` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The stream that is the target of the flush operation.  
**Returns**  
---  
**Type** | **Description**  
`[FlushRowsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.FlushRowsResponse)` |   
  
### flushRowsCallable()
    
    
    public final UnaryCallable<FlushRowsRequest,FlushRowsResponse> flushRowsCallable()

Flushes rows to a BUFFERED stream.

If users are appending rows to BUFFERED stream, flush operation is required in order for the rows to become available for reading. A Flush operation flushes up to any previously flushed offset in a BUFFERED stream, to the offset specified in the request.

Flush is not supported on the _default stream, since it is not BUFFERED.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BigQueryWriteClient bigQueryWriteClient = BigQueryWriteClient.create()) {
       FlushRowsRequest request =
           FlushRowsRequest.newBuilder()
               .setWriteStream(
                   WriteStreamName.of("[PROJECT]", "[DATASET]", "[TABLE]", "[STREAM]").toString())
               .setOffset(Int64Value.newBuilder().build())
               .build();
       ApiFuture<FlushRowsResponse> future =
           bigQueryWriteClient.flushRowsCallable().futureCall(request);
       // Do something.
       FlushRowsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FlushRowsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.FlushRowsRequest),[FlushRowsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.FlushRowsResponse)>` |   
  
### getSettings()
    
    
    public final @Nullable BigQueryWriteSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.bigquery.storage.v1.BigQueryWriteSettings` |   
  
### getStub()
    
    
    public BigQueryWriteStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[BigQueryWriteStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.stub.BigQueryWriteStub)` |   
  
### getWriteStream(@Nullable WriteStreamName name)
    
    
    public final WriteStream getWriteStream(@Nullable WriteStreamName name)

Gets information about a write stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BigQueryWriteClient bigQueryWriteClient = BigQueryWriteClient.create()) {
       WriteStreamName name = WriteStreamName.of("[PROJECT]", "[DATASET]", "[TABLE]", "[STREAM]");
       WriteStream response = bigQueryWriteClient.getWriteStream(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.bigquery.storage.v1.WriteStreamName`  
Required. Name of the stream to get, in the form of `projects/{project}/datasets/{dataset}/tables/{table}/streams/{stream}`.  
**Returns**  
---  
**Type** | **Description**  
`[WriteStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.WriteStream)` |   
  
### getWriteStream(GetWriteStreamRequest request)
    
    
    public final WriteStream getWriteStream(GetWriteStreamRequest request)

Gets information about a write stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BigQueryWriteClient bigQueryWriteClient = BigQueryWriteClient.create()) {
       GetWriteStreamRequest request =
           GetWriteStreamRequest.newBuilder()
               .setName(
                   WriteStreamName.of("[PROJECT]", "[DATASET]", "[TABLE]", "[STREAM]").toString())
               .setView(WriteStreamView.forNumber(0))
               .build();
       WriteStream response = bigQueryWriteClient.getWriteStream(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetWriteStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.GetWriteStreamRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[WriteStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.WriteStream)` |   
  
### getWriteStream(String name)
    
    
    public final WriteStream getWriteStream(String name)

Gets information about a write stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BigQueryWriteClient bigQueryWriteClient = BigQueryWriteClient.create()) {
       String name = WriteStreamName.of("[PROJECT]", "[DATASET]", "[TABLE]", "[STREAM]").toString();
       WriteStream response = bigQueryWriteClient.getWriteStream(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the stream to get, in the form of `projects/{project}/datasets/{dataset}/tables/{table}/streams/{stream}`.  
**Returns**  
---  
**Type** | **Description**  
`[WriteStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.WriteStream)` |   
  
### getWriteStreamCallable()
    
    
    public final UnaryCallable<GetWriteStreamRequest,WriteStream> getWriteStreamCallable()

Gets information about a write stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BigQueryWriteClient bigQueryWriteClient = BigQueryWriteClient.create()) {
       GetWriteStreamRequest request =
           GetWriteStreamRequest.newBuilder()
               .setName(
                   WriteStreamName.of("[PROJECT]", "[DATASET]", "[TABLE]", "[STREAM]").toString())
               .setView(WriteStreamView.forNumber(0))
               .build();
       ApiFuture<WriteStream> future =
           bigQueryWriteClient.getWriteStreamCallable().futureCall(request);
       // Do something.
       WriteStream response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetWriteStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.GetWriteStreamRequest),[WriteStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.WriteStream)>` |   
  
### isShutdown()
    
    
    public boolean isShutdown()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### isTerminated()
    
    
    public boolean isTerminated()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
