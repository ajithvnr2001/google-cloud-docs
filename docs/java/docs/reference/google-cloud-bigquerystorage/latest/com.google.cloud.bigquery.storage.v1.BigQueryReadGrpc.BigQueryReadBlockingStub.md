---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BigQueryReadGrpc.BigQueryReadBlockingStub
title: Class BigQueryReadGrpc.BigQueryReadBlockingStub (3.35.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:00:08.226449+00:00
---

# Class BigQueryReadGrpc.BigQueryReadBlockingStub (3.35.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BigQueryReadGrpc.BigQueryReadBlockingStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class BigQueryReadGrpc.BigQueryReadBlockingStub (3.35.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.35.0 (latest)  3.31.0  3.30.0  3.29.0  3.27.0  3.24.0  3.23.0  3.21.0  3.20.0  3.19.1  3.18.0  3.17.3  3.16.3  3.15.3  3.14.1  3.12.0  3.11.4  3.10.3  3.9.3  3.8.0  3.6.1  3.5.2  3.4.0  3.3.1  3.2.0  3.1.0  3.0.1  2.47.0  2.45.0  2.44.1  2.43.0 
    
    
    public static final class BigQueryReadGrpc.BigQueryReadBlockingStub extends AbstractBlockingStub<BigQueryReadGrpc.BigQueryReadBlockingStub>

A stub to allow clients to do limited synchronous rpc calls to service BigQueryRead.

BigQuery Read API. The Read API can be used to read data from BigQuery.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > BigQueryReadGrpc.BigQueryReadBlockingStub

## Inherited Members

io.grpc.stub.AbstractBlockingStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractBlockingStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

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

### build(Channel channel, CallOptions callOptions)
    
    
    protected BigQueryReadGrpc.BigQueryReadBlockingStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[BigQueryReadGrpc.BigQueryReadBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BigQueryReadGrpc.BigQueryReadBlockingStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createReadSession(CreateReadSessionRequest request)
    
    
    public ReadSession createReadSession(CreateReadSessionRequest request)

Creates a new read session. A read session divides the contents of a BigQuery table into one or more streams, which can then be used to read data from the table. The read session also specifies properties of the data to be read, such as a list of columns or a push-down filter describing the rows to be returned. A particular row can be read by at most one stream. When the caller has reached the end of each stream in the session, then all the data in the table has been read. Data is assigned to each stream such that roughly the same number of rows can be read from each stream. Because the server-side unit for assigning data is collections of rows, the API does not guarantee that each stream will return the same number or rows. Additionally, the limits are enforced based on the number of pre-filtered rows, so some filters can lead to lopsided assignments. Read sessions automatically expire 6 hours after they are created and do not require manual clean-up by the caller.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateReadSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.CreateReadSessionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession)` |   
  
### readRows(ReadRowsRequest request)
    
    
    public Iterator<ReadRowsResponse> readRows(ReadRowsRequest request)

Reads rows from the stream in the format prescribed by the ReadSession. Each response contains one or more table rows, up to a maximum of 128 MB per response; read requests which attempt to read individual rows larger than 128 MB will fail. Each request also returns a set of stream statistics reflecting the current state of the stream.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ReadRowsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Iterator](https://docs.oracle.com/javase/8/docs/api/java/util/Iterator.html)<[ReadRowsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse)>` |   
  
### splitReadStream(SplitReadStreamRequest request)
    
    
    public SplitReadStreamResponse splitReadStream(SplitReadStreamRequest request)

Splits a given `ReadStream` into two `ReadStream` objects. These `ReadStream` objects are referred to as the primary and the residual streams of the split. The original `ReadStream` can still be read from in the same manner as before. Both of the returned `ReadStream` objects can also be read from, and the rows returned by both child streams will be the same as the rows read from the original stream. Moreover, the two child streams will be allocated back-to-back in the original `ReadStream`. Concretely, it is guaranteed that for streams original, primary, and residual, that original[0-j] = primary[0-j] and original[j-n] = residual[0-m] once the streams have been read to completion.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SplitReadStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.SplitReadStreamRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SplitReadStreamResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.SplitReadStreamResponse)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
