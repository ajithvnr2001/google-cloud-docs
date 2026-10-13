---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1beta1.BigQueryStorageGrpc.BigQueryStorageFutureStub
title: Class BigQueryStorageGrpc.BigQueryStorageFutureStub (3.35.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:49:34.297172+00:00
---

# Class BigQueryStorageGrpc.BigQueryStorageFutureStub (3.35.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1beta1.BigQueryStorageGrpc.BigQueryStorageFutureStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class BigQueryStorageGrpc.BigQueryStorageFutureStub (3.35.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.35.0 (latest)  3.31.0  3.30.0  3.29.0  3.27.0  3.24.0  3.23.0  3.21.0  3.20.0  3.19.1  3.18.0  3.17.3  3.16.3  3.15.3  3.14.1  3.12.0  3.11.4  3.10.3  3.9.3  3.8.0  3.6.1  3.5.2  3.4.0  3.3.1  3.2.0  3.1.0  3.0.1  2.47.0  2.45.0  2.44.1  2.43.0 
    
    
    public static final class BigQueryStorageGrpc.BigQueryStorageFutureStub extends AbstractFutureStub<BigQueryStorageGrpc.BigQueryStorageFutureStub>

A stub to allow clients to do ListenableFuture-style rpc calls to service BigQueryStorage.

BigQuery storage API. The BigQuery storage API can be used to read data stored in BigQuery. The v1beta1 API is not yet officially deprecated, and will go through a full deprecation cycle (<https://cloud.google.com/products#product-launch-stages>) before the service is turned down. However, new code should use the v1 API going forward.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractFutureStub > BigQueryStorageGrpc.BigQueryStorageFutureStub

## Inherited Members

io.grpc.stub.AbstractFutureStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractFutureStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.<T>withOption(io.grpc.CallOptions.Key<T>,T)

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.getCallOptions()

io.grpc.stub.AbstractStub.getChannel()

io.grpc.stub.AbstractStub.withCallCredentials(io.grpc.CallCredentials)

io.grpc.stub.AbstractStub.withChannel(io.grpc.Channel)

io.grpc.stub.AbstractStub.withCompression(java.lang.String)

io.grpc.stub.AbstractStub.withDeadline(io.grpc.Deadline)

io.grpc.stub.AbstractStub.withDeadlineAfter(java.time.Duration)

io.grpc.stub.AbstractStub.withDeadlineAfter(long,java.util.concurrent.TimeUnit)

io.grpc.stub.AbstractStub.withExecutor(java.util.concurrent.Executor)

io.grpc.stub.AbstractStub.withInterceptors(io.grpc.ClientInterceptor...)

io.grpc.stub.AbstractStub.withMaxInboundMessageSize(int)

io.grpc.stub.AbstractStub.withMaxOutboundMessageSize(int)

io.grpc.stub.AbstractStub.withOnReadyThreshold(int)

io.grpc.stub.AbstractStub.withWaitForReady()

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Methods 

### batchCreateReadSessionStreams(Storage.BatchCreateReadSessionStreamsRequest request)
    
    
    public ListenableFuture<Storage.BatchCreateReadSessionStreamsResponse> batchCreateReadSessionStreams(Storage.BatchCreateReadSessionStreamsRequest request)

Creates additional streams for a ReadSession. This API can be used to dynamically adjust the parallelism of a batch processing task upwards by adding additional workers.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[Storage.BatchCreateReadSessionStreamsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1beta1.Storage.BatchCreateReadSessionStreamsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[BatchCreateReadSessionStreamsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1beta1.Storage.BatchCreateReadSessionStreamsResponse)>` |   
  
### build(Channel channel, CallOptions callOptions)
    
    
    protected BigQueryStorageGrpc.BigQueryStorageFutureStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[BigQueryStorageGrpc.BigQueryStorageFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1beta1.BigQueryStorageGrpc.BigQueryStorageFutureStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createReadSession(Storage.CreateReadSessionRequest request)
    
    
    public ListenableFuture<Storage.ReadSession> createReadSession(Storage.CreateReadSessionRequest request)

Creates a new read session. A read session divides the contents of a BigQuery table into one or more streams, which can then be used to read data from the table. The read session also specifies properties of the data to be read, such as a list of columns or a push-down filter describing the rows to be returned. A particular row can be read by at most one stream. When the caller has reached the end of each stream in the session, then all the data in the table has been read. Read sessions automatically expire 6 hours after they are created and do not require manual clean-up by the caller.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[Storage.CreateReadSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1beta1.Storage.CreateReadSessionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1beta1.Storage.ReadSession)>` |   
  
### finalizeStream(Storage.FinalizeStreamRequest request)
    
    
    public ListenableFuture<Empty> finalizeStream(Storage.FinalizeStreamRequest request)

Causes a single stream in a ReadSession to gracefully stop. This API can be used to dynamically adjust the parallelism of a batch processing task downwards without losing data. This API does not delete the stream -- it remains visible in the ReadSession, and any data processed by the stream is not released to other streams. However, no additional data will be assigned to the stream once this call completes. Callers must continue reading data on the stream until the end of the stream is reached so that data which has already been assigned to the stream will be processed. This method will return an error if there are no other live streams in the Session, or if SplitReadStream() has been called on the given Stream.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[Storage.FinalizeStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1beta1.Storage.FinalizeStreamRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### splitReadStream(Storage.SplitReadStreamRequest request)
    
    
    public ListenableFuture<Storage.SplitReadStreamResponse> splitReadStream(Storage.SplitReadStreamRequest request)

Splits a given read stream into two Streams. These streams are referred to as the primary and the residual of the split. The original stream can still be read from in the same manner as before. Both of the returned streams can also be read from, and the total rows return by both child streams will be the same as the rows read from the original stream. Moreover, the two child streams will be allocated back to back in the original Stream. Concretely, it is guaranteed that for streams Original, Primary, and Residual, that Original[0-j] = Primary[0-j] and Original[j-n] = Residual[0-m] once the streams have been read to completion. This method is guaranteed to be idempotent.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[Storage.SplitReadStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1beta1.Storage.SplitReadStreamRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[SplitReadStreamResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1beta1.Storage.SplitReadStreamResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
