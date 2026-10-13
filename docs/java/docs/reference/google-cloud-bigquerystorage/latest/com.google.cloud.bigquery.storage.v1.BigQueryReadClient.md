---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BigQueryReadClient
title: Class BigQueryReadClient (3.35.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:59:20.625362+00:00
---

# Class BigQueryReadClient (3.35.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BigQueryReadClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class BigQueryReadClient (3.35.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.35.0 (latest)  3.31.0  3.30.0  3.29.0  3.27.0  3.24.0  3.23.0  3.21.0  3.20.0  3.19.1  3.18.0  3.17.3  3.16.3  3.15.3  3.14.1  3.12.0  3.11.4  3.10.3  3.9.3  3.8.0  3.6.1  3.5.2  3.4.0  3.3.1  3.2.0  3.1.0  3.0.1  2.47.0  2.45.0  2.44.1  2.43.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-bigquerystorage/google-cloud-bigquerystorage/src/main/java/com/google/cloud/bigquery/storage/v1/BigQueryReadClient.java)| [Product Reference](https://cloud.google.com/bigquery/docs/reference/storage/)  
---|---  
  
Service Description: BigQuery Read API.

The Read API can be used to read data from BigQuery.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     
     try (BigQueryReadClient BigQueryReadClient = BigQueryReadClient.create()) {
       String parent = "";
       ReadSession readSession = ReadSession.newBuilder().build();
       int maxStreamCount = 0;
       ReadSession response = BigQueryReadClient.createReadSession(parent, readSession, maxStreamCount);
     }
     
     

Note: close() needs to be called on the BigQueryReadClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

The surface of this class includes several types of Java methods for each of the API's methods:

  1. A "flattened" method. With this type of method, the fields of the request type have been converted into function parameters. It may be the case that not all fields are available as parameters, and not every API method will have a flattened method entry point. 
  2. A "request object" method. This type of method only takes one parameter, a request object, which must be constructed before the call. Not every API method will have a request object method. 
  3. A "callable" method. This type of method takes no parameters and returns an immutable API callable object, which can be used to initiate calls to the service. 



See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of BigQueryReadSettings to create(). For example:

To customize credentials:
    
    
     
     BigQueryReadSettings BigQueryReadSettings =
         BigQueryReadSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     BigQueryReadClient BigQueryReadClient =
         BigQueryReadClient.create(BigQueryReadSettings);
     
     

To customize the endpoint:
    
    
     
     BigQueryReadSettings BigQueryReadSettings =
         BigQueryReadSettings.newBuilder().setEndpoint(myEndpoint).build();
     BigQueryReadClient BigQueryReadClient =
         BigQueryReadClient.create(BigQueryReadSettings);
     
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > BigQueryReadClient

## Static Methods 

### create()
    
    
    public static final BigQueryReadClient create()

Constructs an instance of BigQueryReadClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[BigQueryReadClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BigQueryReadClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(BigQueryReadSettings settings)
    
    
    public static final BigQueryReadClient create(BigQueryReadSettings settings)

Constructs an instance of BigQueryReadClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[BigQueryReadSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BigQueryReadSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BigQueryReadClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BigQueryReadClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(EnhancedBigQueryReadStub stub)
    
    
    public static final BigQueryReadClient create(EnhancedBigQueryReadStub stub)

**Beta**

_A restructuring of stub classes is planned, so this may break in the future_

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Constructs an instance of BigQueryReadClient, using the given stub for making calls. This is for advanced usage - prefer to use BigQueryReadSettings}.

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[EnhancedBigQueryReadStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.stub.EnhancedBigQueryReadStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BigQueryReadClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BigQueryReadClient)` |   
  
## Constructors 

### BigQueryReadClient(BigQueryReadSettings settings)
    
    
    protected BigQueryReadClient(BigQueryReadSettings settings)

Constructs an instance of BigQueryReadClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[BigQueryReadSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BigQueryReadSettings)`  
  
  
### BigQueryReadClient(EnhancedBigQueryReadStub stub)
    
    
    protected BigQueryReadClient(EnhancedBigQueryReadStub stub)

**Beta**

_A restructuring of stub classes is planned, so this may break in the future_

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[EnhancedBigQueryReadStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.stub.EnhancedBigQueryReadStub)`  
  
  
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

### createReadSession(CreateReadSessionRequest request)
    
    
    public final ReadSession createReadSession(CreateReadSessionRequest request)

Creates a new read session. A read session divides the contents of a BigQuery table into one or more streams, which can then be used to read data from the table. The read session also specifies properties of the data to be read, such as a list of columns or a push-down filter describing the rows to be returned.

A particular row can be read by at most one stream. When the caller has reached the end of each stream in the session, then all the data in the table has been read.

Data is assigned to each stream such that roughly the same number of rows can be read from each stream. Because the server-side unit for assigning data is collections of rows, the API does not guarantee that each stream will return the same number or rows. Additionally, the limits are enforced based on the number of pre-filtered rows, so some filters can lead to lopsided assignments.

Read sessions automatically expire 24 hours after they are created and do not require manual clean-up by the caller.

Sample code:
    
    
     try (BigQueryReadClient BigQueryReadClient = BigQueryReadClient.create()) {
       CreateReadSessionRequest request = CreateReadSessionRequest.newBuilder().build();
       ReadSession response = BigQueryReadClient.createReadSession(request);
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

Read sessions automatically expire 24 hours after they are created and do not require manual clean-up by the caller.

Sample code:
    
    
     try (BigQueryReadClient BigQueryReadClient = BigQueryReadClient.create()) {
       String parent = "";
       ReadSession readSession = ReadSession.newBuilder().build();
       int maxStreamCount = 0;
       ReadSession response = BigQueryReadClient.createReadSession(parent, readSession, maxStreamCount);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The request project that owns the session, in the form of `projects/{project_id}`.  
`readSession` | `[ReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession)`  
Required. Session to be created.  
`maxStreamCount` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
Max initial number of streams. If unset or zero, the server will provide a value of streams so as to produce reasonable throughput. Must be non-negative. The number of streams may be lower than the requested number, depending on the amount parallelism that is reasonable for the table. Error will be returned if the max count is greater than the current system max limit of 1,000. Streams must be read starting from offset 0.  
**Returns**  
---  
**Type** | **Description**  
`[ReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession)` |   
  
### createReadSessionCallable()
    
    
    public final UnaryCallable<CreateReadSessionRequest,ReadSession> createReadSessionCallable()

Creates a new read session. A read session divides the contents of a BigQuery table into one or more streams, which can then be used to read data from the table. The read session also specifies properties of the data to be read, such as a list of columns or a push-down filter describing the rows to be returned.

A particular row can be read by at most one stream. When the caller has reached the end of each stream in the session, then all the data in the table has been read.

Data is assigned to each stream such that roughly the same number of rows can be read from each stream. Because the server-side unit for assigning data is collections of rows, the API does not guarantee that each stream will return the same number or rows. Additionally, the limits are enforced based on the number of pre-filtered rows, so some filters can lead to lopsided assignments.

Read sessions automatically expire 24 hours after they are created and do not require manual clean-up by the caller.

Sample code:
    
    
     try (BigQueryReadClient bigQueryReadClient = BigQueryReadClient.create()) {
       CreateReadSessionRequest request = CreateReadSessionRequest.newBuilder().build();
       ApiFuture<ReadSession> future = BigQueryReadClient.createReadSessionCallable().futureCall(request);
       // Do something
       ReadSession response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateReadSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.CreateReadSessionRequest),[ReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession)>` |   
  
### disableOpenTelemetryTracing()
    
    
    public void disableOpenTelemetryTracing()

### enableDefaultOpenTelemetryTracing()
    
    
    public void enableDefaultOpenTelemetryTracing()

### enableOpenTelemetryTracing(TracerProvider tracerProvider)
    
    
    public void enableOpenTelemetryTracing(TracerProvider tracerProvider)

**Parameter**  
---  
**Name** | **Description**  
`tracerProvider` | `io.opentelemetry.api.trace.TracerProvider`  
  
  
### getSettings()
    
    
    public final BigQueryReadSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`[BigQueryReadSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BigQueryReadSettings)` |   
  
### getStub()
    
    
    public EnhancedBigQueryReadStub getStub()

**Beta**

_A restructuring of stub classes is planned, so this may break in the future_

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

**Returns**  
---  
**Type** | **Description**  
`[EnhancedBigQueryReadStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.stub.EnhancedBigQueryReadStub)` |   
  
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

Reads rows from the stream in the format prescribed by the ReadSession. Each response contains one or more table rows, up to a maximum of 100 MiB per response; read requests which attempt to read individual rows larger than 100 MiB will fail.

Each request also returns a set of stream statistics reflecting the current state of the stream.

Sample code:
    
    
     try (BigQueryReadClient bigQueryReadClient = BigQueryReadClient.create()) {
       ReadRowsRequest request = ReadRowsRequest.newBuilder().build();
    
       ServerStream<ReadRowsResponse> stream = bigQueryReadClient.readRowsCallable().call(request);
       for (ReadRowsResponse response : stream) {
         // Do something when receive a response
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
    
    
     try (BigQueryReadClient bigQueryReadClient = BigQueryReadClient.create()) {
       SplitReadStreamRequest request = SplitReadStreamRequest.newBuilder().build();
       SplitReadStreamResponse response = bigQueryReadClient.splitReadStream(request);
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
    
    
     try (BigQueryReadClient bigQueryReadClient = BigQueryReadClient.create()) {
       SplitReadStreamRequest request = SplitReadStreamRequest.newBuilder().build();
       ApiFuture<SplitReadStreamResponse> future = bigQueryReadClient.splitReadStreamCallable().futureCall(request);
       // Do something
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
