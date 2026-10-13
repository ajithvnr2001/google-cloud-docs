---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BaseBigQueryReadClient
title: Class BaseBigQueryReadClient (3.35.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:59:19.952386+00:00
---

# Class BaseBigQueryReadClient (3.35.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BaseBigQueryReadClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class BaseBigQueryReadClient (3.35.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.35.0 (latest)  3.31.0  3.30.0  3.29.0  3.27.0  3.24.0  3.23.0  3.21.0  3.20.0  3.19.1  3.18.0  3.17.3  3.16.3  3.15.3  3.14.1  3.12.0  3.11.4  3.10.3  3.9.3  3.8.0  3.6.1  3.5.2  3.4.0  3.3.1  3.2.0  3.1.0  3.0.1  2.47.0  2.45.0  2.44.1  2.43.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-bigquerystorage/google-cloud-bigquerystorage/src/main/java/com/google/cloud/bigquery/storage/v1/BaseBigQueryReadClient.java)| [Product Reference](https://cloud.google.com/bigquery/docs/reference/storage/)  
---|---  
  
Service Description: BigQuery Read API.

The Read API can be used to read data from BigQuery.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BaseBigQueryReadClient baseBigQueryReadClient = BaseBigQueryReadClient.create()) {
       ProjectName parent = ProjectName.of("[PROJECT]");
       ReadSession readSession = ReadSession.newBuilder().build();
       int maxStreamCount = 940837515;
       ReadSession response =
           baseBigQueryReadClient.createReadSession(parent, readSession, maxStreamCount);
     }
     

Note: close() needs to be called on the BaseBigQueryReadClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateReadSession |  Creates a new read session. A read session divides the contents of a BigQuery table into one or more streams, which can then be used to read data from the table. The read session also specifies properties of the data to be read, such as a list of columns or a push-down filter describing the rows to be returned.  A particular row can be read by at most one stream. When the caller has reached the end of each stream in the session, then all the data in the table has been read.  Data is assigned to each stream such that roughly the same number of rows can be read from each stream. Because the server-side unit for assigning data is collections of rows, the API does not guarantee that each stream will return the same number or rows. Additionally, the limits are enforced based on the number of pre-filtered rows, so some filters can lead to lopsided assignments.  Read sessions automatically expire 6 hours after they are created and do not require manual clean-up by the caller. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createReadSession(CreateReadSessionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createReadSession(ProjectName parent, ReadSession readSession, int maxStreamCount) 
  * createReadSession(String parent, ReadSession readSession, int maxStreamCount) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createReadSessionCallable() 

  
ReadRows |  Reads rows from the stream in the format prescribed by the ReadSession. Each response contains one or more table rows, up to a maximum of 128 MB per response; read requests which attempt to read individual rows larger than 128 MB will fail.  Each request also returns a set of stream statistics reflecting the current state of the stream. |  Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * readRowsCallable() 

  
SplitReadStream |  Splits a given `ReadStream` into two `ReadStream` objects. These `ReadStream` objects are referred to as the primary and the residual streams of the split. The original `ReadStream` can still be read from in the same manner as before. Both of the returned `ReadStream` objects can also be read from, and the rows returned by both child streams will be the same as the rows read from the original stream.  Moreover, the two child streams will be allocated back-to-back in the original `ReadStream`. Concretely, it is guaranteed that for streams original, primary, and residual, that original[0-j] = primary[0-j] and original[j-n] = residual[0-m] once the streams have been read to completion. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * splitReadStream(SplitReadStreamRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * splitReadStreamCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of BaseBigQueryReadSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     BaseBigQueryReadSettings baseBigQueryReadSettings =
         BaseBigQueryReadSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     BaseBigQueryReadClient baseBigQueryReadClient =
         BaseBigQueryReadClient.create(baseBigQueryReadSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     BaseBigQueryReadSettings baseBigQueryReadSettings =
         BaseBigQueryReadSettings.newBuilder().setEndpoint(myEndpoint).build();
     BaseBigQueryReadClient baseBigQueryReadClient =
         BaseBigQueryReadClient.create(baseBigQueryReadSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > BaseBigQueryReadClient

## Static Methods 

### create()
    
    
    public static final BaseBigQueryReadClient create()

Constructs an instance of BaseBigQueryReadClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[BaseBigQueryReadClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BaseBigQueryReadClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(BaseBigQueryReadSettings settings)
    
    
    public static final BaseBigQueryReadClient create(BaseBigQueryReadSettings settings)

Constructs an instance of BaseBigQueryReadClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[BaseBigQueryReadSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BaseBigQueryReadSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BaseBigQueryReadClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BaseBigQueryReadClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(BigQueryReadStub stub)
    
    
    public static final BaseBigQueryReadClient create(BigQueryReadStub stub)

Constructs an instance of BaseBigQueryReadClient, using the given stub for making calls. This is for advanced usage - prefer using create(BaseBigQueryReadSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[BigQueryReadStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.stub.BigQueryReadStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BaseBigQueryReadClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BaseBigQueryReadClient)` |   
  
## Constructors 

### BaseBigQueryReadClient(BaseBigQueryReadSettings settings)
    
    
    protected BaseBigQueryReadClient(BaseBigQueryReadSettings settings)

Constructs an instance of BaseBigQueryReadClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[BaseBigQueryReadSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BaseBigQueryReadSettings)`  
  
  
### BaseBigQueryReadClient(BigQueryReadStub stub)
    
    
    protected BaseBigQueryReadClient(BigQueryReadStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[BigQueryReadStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.stub.BigQueryReadStub)`  
  
  
## Methods 

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
  
### close()
    
    
    public final void close()

### createReadSession(@Nullable ProjectName parent, ReadSession readSession, int maxStreamCount)
    
    
    public final ReadSession createReadSession(@Nullable ProjectName parent, ReadSession readSession, int maxStreamCount)

Creates a new read session. A read session divides the contents of a BigQuery table into one or more streams, which can then be used to read data from the table. The read session also specifies properties of the data to be read, such as a list of columns or a push-down filter describing the rows to be returned.

A particular row can be read by at most one stream. When the caller has reached the end of each stream in the session, then all the data in the table has been read.

Data is assigned to each stream such that roughly the same number of rows can be read from each stream. Because the server-side unit for assigning data is collections of rows, the API does not guarantee that each stream will return the same number or rows. Additionally, the limits are enforced based on the number of pre-filtered rows, so some filters can lead to lopsided assignments.

Read sessions automatically expire 6 hours after they are created and do not require manual clean-up by the caller.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BaseBigQueryReadClient baseBigQueryReadClient = BaseBigQueryReadClient.create()) {
       ProjectName parent = ProjectName.of("[PROJECT]");
       ReadSession readSession = ReadSession.newBuilder().build();
       int maxStreamCount = 940837515;
       ReadSession response =
           baseBigQueryReadClient.createReadSession(parent, readSession, maxStreamCount);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.bigquery.storage.v1.ProjectName`  
Required. The request project that owns the session, in the form of `projects/{project_id}`.  
`readSession` | `[ReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession)`  
Required. Session to be created.  
`maxStreamCount` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
Max initial number of streams. If unset or zero, the server will provide a value of streams so as to produce reasonable throughput. Must be non-negative. The number of streams may be lower than the requested number, depending on the amount parallelism that is reasonable for the table. There is a default system max limit of 1,000. This must be greater than or equal to preferred_min_stream_count. Typically, clients should either leave this unset to let the system to determine an upper bound OR set this a size for the maximum "units of work" it can gracefully handle.  
**Returns**  
---  
**Type** | **Description**  
`[ReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession)` |   
  
### createReadSession(CreateReadSessionRequest request)
    
    
    public final ReadSession createReadSession(CreateReadSessionRequest request)

Creates a new read session. A read session divides the contents of a BigQuery table into one or more streams, which can then be used to read data from the table. The read session also specifies properties of the data to be read, such as a list of columns or a push-down filter describing the rows to be returned.

A particular row can be read by at most one stream. When the caller has reached the end of each stream in the session, then all the data in the table has been read.

Data is assigned to each stream such that roughly the same number of rows can be read from each stream. Because the server-side unit for assigning data is collections of rows, the API does not guarantee that each stream will return the same number or rows. Additionally, the limits are enforced based on the number of pre-filtered rows, so some filters can lead to lopsided assignments.

Read sessions automatically expire 6 hours after they are created and do not require manual clean-up by the caller.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BaseBigQueryReadClient baseBigQueryReadClient = BaseBigQueryReadClient.create()) {
       CreateReadSessionRequest request =
           CreateReadSessionRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setReadSession(ReadSession.newBuilder().build())
               .setMaxStreamCount(940837515)
               .setPreferredMinStreamCount(-1905507237)
               .build();
       ReadSession response = baseBigQueryReadClient.createReadSession(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateReadSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.CreateReadSessionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession)` |   
  
### createReadSession(String parent, ReadSession readSession, int maxStreamCount)
    
    
    public final ReadSession createReadSession(String parent, ReadSession readSession, int maxStreamCount)

Creates a new read session. A read session divides the contents of a BigQuery table into one or more streams, which can then be used to read data from the table. The read session also specifies properties of the data to be read, such as a list of columns or a push-down filter describing the rows to be returned.

A particular row can be read by at most one stream. When the caller has reached the end of each stream in the session, then all the data in the table has been read.

Data is assigned to each stream such that roughly the same number of rows can be read from each stream. Because the server-side unit for assigning data is collections of rows, the API does not guarantee that each stream will return the same number or rows. Additionally, the limits are enforced based on the number of pre-filtered rows, so some filters can lead to lopsided assignments.

Read sessions automatically expire 6 hours after they are created and do not require manual clean-up by the caller.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BaseBigQueryReadClient baseBigQueryReadClient = BaseBigQueryReadClient.create()) {
       String parent = ProjectName.of("[PROJECT]").toString();
       ReadSession readSession = ReadSession.newBuilder().build();
       int maxStreamCount = 940837515;
       ReadSession response =
           baseBigQueryReadClient.createReadSession(parent, readSession, maxStreamCount);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The request project that owns the session, in the form of `projects/{project_id}`.  
`readSession` | `[ReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession)`  
Required. Session to be created.  
`maxStreamCount` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
Max initial number of streams. If unset or zero, the server will provide a value of streams so as to produce reasonable throughput. Must be non-negative. The number of streams may be lower than the requested number, depending on the amount parallelism that is reasonable for the table. There is a default system max limit of 1,000. This must be greater than or equal to preferred_min_stream_count. Typically, clients should either leave this unset to let the system to determine an upper bound OR set this a size for the maximum "units of work" it can gracefully handle.  
**Returns**  
---  
**Type** | **Description**  
`[ReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession)` |   
  
### createReadSessionCallable()
    
    
    public final UnaryCallable<CreateReadSessionRequest,ReadSession> createReadSessionCallable()

Creates a new read session. A read session divides the contents of a BigQuery table into one or more streams, which can then be used to read data from the table. The read session also specifies properties of the data to be read, such as a list of columns or a push-down filter describing the rows to be returned.

A particular row can be read by at most one stream. When the caller has reached the end of each stream in the session, then all the data in the table has been read.

Data is assigned to each stream such that roughly the same number of rows can be read from each stream. Because the server-side unit for assigning data is collections of rows, the API does not guarantee that each stream will return the same number or rows. Additionally, the limits are enforced based on the number of pre-filtered rows, so some filters can lead to lopsided assignments.

Read sessions automatically expire 6 hours after they are created and do not require manual clean-up by the caller.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BaseBigQueryReadClient baseBigQueryReadClient = BaseBigQueryReadClient.create()) {
       CreateReadSessionRequest request =
           CreateReadSessionRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setReadSession(ReadSession.newBuilder().build())
               .setMaxStreamCount(940837515)
               .setPreferredMinStreamCount(-1905507237)
               .build();
       ApiFuture<ReadSession> future =
           baseBigQueryReadClient.createReadSessionCallable().futureCall(request);
       // Do something.
       ReadSession response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateReadSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.CreateReadSessionRequest),[ReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession)>` |   
  
### getSettings()
    
    
    public final @Nullable BaseBigQueryReadSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.bigquery.storage.v1.BaseBigQueryReadSettings` |   
  
### getStub()
    
    
    public BigQueryReadStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[BigQueryReadStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.stub.BigQueryReadStub)` |   
  
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
  
### readRowsCallable()
    
    
    public final ServerStreamingCallable<ReadRowsRequest,ReadRowsResponse> readRowsCallable()

Reads rows from the stream in the format prescribed by the ReadSession. Each response contains one or more table rows, up to a maximum of 128 MB per response; read requests which attempt to read individual rows larger than 128 MB will fail.

Each request also returns a set of stream statistics reflecting the current state of the stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BaseBigQueryReadClient baseBigQueryReadClient = BaseBigQueryReadClient.create()) {
       ReadRowsRequest request =
           ReadRowsRequest.newBuilder()
               .setReadStream(
                   ReadStreamName.of("[PROJECT]", "[LOCATION]", "[SESSION]", "[STREAM]").toString())
               .setOffset(-1019779949)
               .build();
       ServerStream<ReadRowsResponse> stream =
           baseBigQueryReadClient.readRowsCallable().call(request);
       for (ReadRowsResponse response : stream) {
         // Do something when a response is received.
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[ServerStreamingCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ServerStreamingCallable.html)<[ReadRowsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsRequest),[ReadRowsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### splitReadStream(SplitReadStreamRequest request)
    
    
    public final SplitReadStreamResponse splitReadStream(SplitReadStreamRequest request)

Splits a given `ReadStream` into two `ReadStream` objects. These `ReadStream` objects are referred to as the primary and the residual streams of the split. The original `ReadStream` can still be read from in the same manner as before. Both of the returned `ReadStream` objects can also be read from, and the rows returned by both child streams will be the same as the rows read from the original stream.

Moreover, the two child streams will be allocated back-to-back in the original `ReadStream`. Concretely, it is guaranteed that for streams original, primary, and residual, that original[0-j] = primary[0-j] and original[j-n] = residual[0-m] once the streams have been read to completion.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BaseBigQueryReadClient baseBigQueryReadClient = BaseBigQueryReadClient.create()) {
       SplitReadStreamRequest request =
           SplitReadStreamRequest.newBuilder()
               .setName(
                   ReadStreamName.of("[PROJECT]", "[LOCATION]", "[SESSION]", "[STREAM]").toString())
               .setFraction(-1653751294)
               .build();
       SplitReadStreamResponse response = baseBigQueryReadClient.splitReadStream(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SplitReadStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.SplitReadStreamRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SplitReadStreamResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.SplitReadStreamResponse)` |   
  
### splitReadStreamCallable()
    
    
    public final UnaryCallable<SplitReadStreamRequest,SplitReadStreamResponse> splitReadStreamCallable()

Splits a given `ReadStream` into two `ReadStream` objects. These `ReadStream` objects are referred to as the primary and the residual streams of the split. The original `ReadStream` can still be read from in the same manner as before. Both of the returned `ReadStream` objects can also be read from, and the rows returned by both child streams will be the same as the rows read from the original stream.

Moreover, the two child streams will be allocated back-to-back in the original `ReadStream`. Concretely, it is guaranteed that for streams original, primary, and residual, that original[0-j] = primary[0-j] and original[j-n] = residual[0-m] once the streams have been read to completion.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BaseBigQueryReadClient baseBigQueryReadClient = BaseBigQueryReadClient.create()) {
       SplitReadStreamRequest request =
           SplitReadStreamRequest.newBuilder()
               .setName(
                   ReadStreamName.of("[PROJECT]", "[LOCATION]", "[SESSION]", "[STREAM]").toString())
               .setFraction(-1653751294)
               .build();
       ApiFuture<SplitReadStreamResponse> future =
           baseBigQueryReadClient.splitReadStreamCallable().futureCall(request);
       // Do something.
       SplitReadStreamResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SplitReadStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.SplitReadStreamRequest),[SplitReadStreamResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.SplitReadStreamResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
