---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.StreamWriter.Builder
title: Class StreamWriter.Builder (3.35.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:59:39.091510+00:00
---

# Class StreamWriter.Builder (3.35.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.StreamWriter.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class StreamWriter.Builder (3.35.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.35.0 (latest)  3.31.0  3.30.0  3.29.0  3.27.0  3.24.0  3.23.0  3.21.0  3.20.0  3.19.1  3.18.0  3.17.3  3.16.3  3.15.3  3.14.1  3.12.0  3.11.4  3.10.3  3.9.3  3.8.0  3.6.1  3.5.2  3.4.0  3.3.1  3.2.0  3.1.0  3.0.1  2.47.0  2.45.0  2.44.1  2.43.0 
    
    
    public static final class StreamWriter.Builder

A builder of [StreamWriter](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.StreamWriter)s.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > StreamWriter.Builder

## Inherited Members

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

### build()
    
    
    public StreamWriter build()

Builds the `StreamWriterV2`.

**Returns**  
---  
**Type** | **Description**  
`[StreamWriter](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.StreamWriter)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### setChannelProvider(TransportChannelProvider channelProvider)
    
    
    public StreamWriter.Builder setChannelProvider(TransportChannelProvider channelProvider)

`ChannelProvider` to use to create Channels, which must point at Cloud BigQuery Storage API endpoint.

For performance, this client benefits from having multiple underlying connections. See com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder#setPoolSize(int).

**Parameter**  
---  
**Name** | **Description**  
`channelProvider` | `[TransportChannelProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.TransportChannelProvider.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamWriter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.StreamWriter.Builder)` |   
  
### setCompressorName(String compressorName)
    
    
    public StreamWriter.Builder setCompressorName(String compressorName)

**Parameter**  
---  
**Name** | **Description**  
`compressorName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamWriter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.StreamWriter.Builder)` |   
  
### setCredentialsProvider(CredentialsProvider credentialsProvider)
    
    
    public StreamWriter.Builder setCredentialsProvider(CredentialsProvider credentialsProvider)

`CredentialsProvider` to use to create Credentials to authenticate calls.

**Parameter**  
---  
**Name** | **Description**  
`credentialsProvider` | `[CredentialsProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.CredentialsProvider.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamWriter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.StreamWriter.Builder)` |   
  
### setDefaultMissingValueInterpretation(AppendRowsRequest.MissingValueInterpretation defaultMissingValueInterpretation)
    
    
    public StreamWriter.Builder setDefaultMissingValueInterpretation(AppendRowsRequest.MissingValueInterpretation defaultMissingValueInterpretation)

Sets the default missing value interpretation value if the column is not presented in the missing_value_interpretations map.

**Parameter**  
---  
**Name** | **Description**  
`defaultMissingValueInterpretation` | `[AppendRowsRequest.MissingValueInterpretation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretation)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamWriter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.StreamWriter.Builder)` |   
  
### setEnableConnectionPool(boolean enableConnectionPool)
    
    
    public StreamWriter.Builder setEnableConnectionPool(boolean enableConnectionPool)

Enables a static shared bidi-streaming connection pool that would dynamically scale up connections based on backlog within each individual connection. A single table's traffic might be splitted into multiple connections if needed. Different tables' traffic can also be multiplexed within the same connection.
    
    
     Each connection pool would have a upper limit (default to 20) and lower limit (default to
     2) for the number of active connections. This parameter can be tuned via a static method
     exposed on [ConnectionWorkerPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ConnectionWorkerPool).
    
     Example:
     ConnectionWorkerPool.setOptions(
         Settings.builder().setMinConnectionsPerRegion(4).setMaxConnectionsPerRegion(10).build());
    
     

**Parameter**  
---  
**Name** | **Description**  
`enableConnectionPool` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamWriter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.StreamWriter.Builder)` | Builder  
  
### setEnableLatencyProfiler(boolean enableLatencyProfiler)
    
    
    public StreamWriter.Builder setEnableLatencyProfiler(boolean enableLatencyProfiler)

Enable a latency profiler that would periodically generate a detailed latency report for the top latency requests. This is currently an experimental API.

**Parameter**  
---  
**Name** | **Description**  
`enableLatencyProfiler` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamWriter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.StreamWriter.Builder)` |   
  
### setEnableOpenTelemetry(boolean enableOpenTelemetry)
    
    
    public StreamWriter.Builder setEnableOpenTelemetry(boolean enableOpenTelemetry)

Enable generation of metrics for OpenTelemetry.

**Parameter**  
---  
**Name** | **Description**  
`enableOpenTelemetry` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamWriter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.StreamWriter.Builder)` |   
  
### setEndpoint(String endpoint)
    
    
    public StreamWriter.Builder setEndpoint(String endpoint)

Gives the ability to override the gRPC endpoint.

**Parameter**  
---  
**Name** | **Description**  
`endpoint` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamWriter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.StreamWriter.Builder)` |   
  
### setExecutorProvider(ExecutorProvider executorProvider)
    
    
    public StreamWriter.Builder setExecutorProvider(ExecutorProvider executorProvider)

`ExecutorProvider` to use to create Executor to run background jobs.

**Parameter**  
---  
**Name** | **Description**  
`executorProvider` | `[ExecutorProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.ExecutorProvider.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamWriter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.StreamWriter.Builder)` |   
  
### setLimitExceededBehavior(FlowController.LimitExceededBehavior limitExceededBehavior)
    
    
    public StreamWriter.Builder setLimitExceededBehavior(FlowController.LimitExceededBehavior limitExceededBehavior)

Sets the limit exceeded behavior.

**Parameter**  
---  
**Name** | **Description**  
`limitExceededBehavior` | `[LimitExceededBehavior](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.batching.FlowController.LimitExceededBehavior.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamWriter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.StreamWriter.Builder)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusRuntimeException` |   
  
### setLocation(String location)
    
    
    public StreamWriter.Builder setLocation(String location)

Location of the table this stream writer is targeting.

**Parameter**  
---  
**Name** | **Description**  
`location` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamWriter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.StreamWriter.Builder)` |   
  
### setMaxInflightBytes(long value)
    
    
    public StreamWriter.Builder setMaxInflightBytes(long value)

**Parameter**  
---  
**Name** | **Description**  
`value` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamWriter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.StreamWriter.Builder)` |   
  
### setMaxInflightRequests(long value)
    
    
    public StreamWriter.Builder setMaxInflightRequests(long value)

**Parameter**  
---  
**Name** | **Description**  
`value` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamWriter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.StreamWriter.Builder)` |   
  
### setMaxRetryDuration(Duration maxRetryDuration)
    
    
    public StreamWriter.Builder setMaxRetryDuration(Duration maxRetryDuration)

**Parameter**  
---  
**Name** | **Description**  
`maxRetryDuration` | `[Duration](https://docs.oracle.com/javase/8/docs/api/java/time/Duration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamWriter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.StreamWriter.Builder)` |   
  
### setMissingValueInterpretationMap(Map<String,AppendRowsRequest.MissingValueInterpretation> missingValueInterpretationMap)
    
    
    public StreamWriter.Builder setMissingValueInterpretationMap(Map<String,AppendRowsRequest.MissingValueInterpretation> missingValueInterpretationMap)

Sets the missing value interpretation map for the stream writer. The input missingValueInterpretationMap is used for all write requests unless otherwise changed.

**Parameter**  
---  
**Name** | **Description**  
`missingValueInterpretationMap` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[MissingValueInterpretation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretation)>`  
the missing value interpretation map used by stream writer.  
**Returns**  
---  
**Type** | **Description**  
`[StreamWriter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.StreamWriter.Builder)` | Builder  
  
### setRetrySettings(RetrySettings retrySettings)
    
    
    public StreamWriter.Builder setRetrySettings(RetrySettings retrySettings)

Enable client lib automatic retries on request level errors.

Immeidate Retry code: ABORTED, UNAVAILABLE, CANCELLED, INTERNAL, DEADLINE_EXCEEDED Backoff Retry code: RESOURCE_EXHAUSTED

Example: RetrySettings retrySettings = RetrySettings.newBuilder() .setInitialRetryDelay(Duration.ofMillis(500)) // applies to backoff retry .setRetryDelayMultiplier(1.1) // applies to backoff retry .setMaxAttempts(5) // applies to both retries .setMaxRetryDelay(Duration.ofMinutes(1)) // applies to backoff retry .build();

**Parameter**  
---  
**Name** | **Description**  
`retrySettings` | `[RetrySettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamWriter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.StreamWriter.Builder)` |   
  
### setTraceId(String traceId)
    
    
    public StreamWriter.Builder setTraceId(String traceId)

Sets traceId for debuging purpose. TraceId must follow the format of CustomerDomain:DebugString, e.g. DATAFLOW:job_id_x.

**Parameter**  
---  
**Name** | **Description**  
`traceId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamWriter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.StreamWriter.Builder)` |   
  
### setWriterSchema(ArrowSchema arrowSchema)
    
    
    public StreamWriter.Builder setWriterSchema(ArrowSchema arrowSchema)

Sets the user provided serialized Arrow schema of the rows.

**Parameter**  
---  
**Name** | **Description**  
`arrowSchema` | `[ArrowSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ArrowSchema)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamWriter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.StreamWriter.Builder)` |   
  
### setWriterSchema(ProtoSchema protoSchema)
    
    
    public StreamWriter.Builder setWriterSchema(ProtoSchema protoSchema)

Sets the user provided proto schema of the rows.

**Parameter**  
---  
**Name** | **Description**  
`protoSchema` | `[ProtoSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ProtoSchema)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamWriter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.StreamWriter.Builder)` |   
  
### setWriterSchema(Schema arrowSchema)
    
    
    public StreamWriter.Builder setWriterSchema(Schema arrowSchema)

Sets the user provided unserialized Arrow schema of the rows.

**Parameter**  
---  
**Name** | **Description**  
`arrowSchema` | `org.apache.arrow.vector.types.pojo.Schema`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamWriter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.StreamWriter.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
