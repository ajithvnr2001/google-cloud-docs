---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.JsonStreamWriter.Builder
title: Class JsonStreamWriter.Builder (3.35.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:59:34.493671+00:00
---

# Class JsonStreamWriter.Builder (3.35.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.JsonStreamWriter.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class JsonStreamWriter.Builder (3.35.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.35.0 (latest)  3.31.0  3.30.0  3.29.0  3.27.0  3.24.0  3.23.0  3.21.0  3.20.0  3.19.1  3.18.0  3.17.3  3.16.3  3.15.3  3.14.1  3.12.0  3.11.4  3.10.3  3.9.3  3.8.0  3.6.1  3.5.2  3.4.0  3.3.1  3.2.0  3.1.0  3.0.1  2.47.0  2.45.0  2.44.1  2.43.0 
    
    
    public static final class JsonStreamWriter.Builder

## Inheritance

[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > JsonStreamWriter.Builder

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
    
    
    public JsonStreamWriter build()

Builds JsonStreamWriter

**Returns**  
---  
**Type** | **Description**  
`[JsonStreamWriter](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.JsonStreamWriter)` | JsonStreamWriter  
**Exceptions**  
---  
**Type** | **Description**  
`[DescriptorValidationException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.DescriptorValidationException.html)` |   
`[IllegalArgumentException](https://docs.oracle.com/javase/8/docs/api/java/lang/IllegalArgumentException.html)` |   
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
`[InterruptedException](https://docs.oracle.com/javase/8/docs/api/java/lang/InterruptedException.html)` |   
  
### getStreamName()
    
    
    public String getStreamName()

Stream name on the builder.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | Builder  
  
### setChannelProvider(TransportChannelProvider channelProvider)
    
    
    public JsonStreamWriter.Builder setChannelProvider(TransportChannelProvider channelProvider)

Setter for the underlying StreamWriter's TransportChannelProvider.

**Parameter**  
---  
**Name** | **Description**  
`channelProvider` | `[TransportChannelProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.TransportChannelProvider.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[JsonStreamWriter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.JsonStreamWriter.Builder)` | Builder  
  
### setCompressorName(String compressorName)
    
    
    public JsonStreamWriter.Builder setCompressorName(String compressorName)

Sets the compression to use for the calls. The compressor must be of type gzip.

**Parameter**  
---  
**Name** | **Description**  
`compressorName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[JsonStreamWriter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.JsonStreamWriter.Builder)` | Builder  
  
### setCredentialsProvider(CredentialsProvider credentialsProvider)
    
    
    public JsonStreamWriter.Builder setCredentialsProvider(CredentialsProvider credentialsProvider)

Setter for the underlying StreamWriter's CredentialsProvider.

**Parameter**  
---  
**Name** | **Description**  
`credentialsProvider` | `[CredentialsProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.CredentialsProvider.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[JsonStreamWriter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.JsonStreamWriter.Builder)` | Builder  
  
### setDefaultMissingValueInterpretation(AppendRowsRequest.MissingValueInterpretation defaultMissingValueInterpretation)
    
    
    public JsonStreamWriter.Builder setDefaultMissingValueInterpretation(AppendRowsRequest.MissingValueInterpretation defaultMissingValueInterpretation)

Sets the default missing value interpretation value if the column is not presented in the missing_value_interpretations map.

If this value is set to `DEFAULT_VALUE`, we will always populate default value if the field is missing from json and default value is defined in the column.

If this value is set to `NULL_VALUE`, we will always not populate default value.

**Parameter**  
---  
**Name** | **Description**  
`defaultMissingValueInterpretation` | `[AppendRowsRequest.MissingValueInterpretation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretation)`  
  
**Returns**  
---  
**Type** | **Description**  
`[JsonStreamWriter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.JsonStreamWriter.Builder)` |   
  
### setEnableConnectionPool(boolean enableConnectionPool)
    
    
    public JsonStreamWriter.Builder setEnableConnectionPool(boolean enableConnectionPool)

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
`[JsonStreamWriter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.JsonStreamWriter.Builder)` | Builder  
  
### setEnableLatencyProfiler(boolean enableLatencyProfiler)
    
    
    public JsonStreamWriter.Builder setEnableLatencyProfiler(boolean enableLatencyProfiler)

Enable a latency profiler that would periodically generate a detailed latency report for the top latency requests. This is currently an experimental API.

**Parameter**  
---  
**Name** | **Description**  
`enableLatencyProfiler` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[JsonStreamWriter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.JsonStreamWriter.Builder)` |   
  
### setEnableOpenTelemetry(boolean enableOpenTelemetry)
    
    
    public JsonStreamWriter.Builder setEnableOpenTelemetry(boolean enableOpenTelemetry)

Enable generation of metrics for OpenTelemetry.

**Parameter**  
---  
**Name** | **Description**  
`enableOpenTelemetry` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[JsonStreamWriter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.JsonStreamWriter.Builder)` |   
  
### setEndpoint(String endpoint)
    
    
    public JsonStreamWriter.Builder setEndpoint(String endpoint)

Setter for the underlying StreamWriter's Endpoint.

**Parameter**  
---  
**Name** | **Description**  
`endpoint` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[JsonStreamWriter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.JsonStreamWriter.Builder)` | Builder  
  
### setExecutorProvider(ExecutorProvider executorProvider)
    
    
    public JsonStreamWriter.Builder setExecutorProvider(ExecutorProvider executorProvider)

Setter for the underlying StreamWriter's ExecutorProvider.

**Parameter**  
---  
**Name** | **Description**  
`executorProvider` | `[ExecutorProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.ExecutorProvider.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[JsonStreamWriter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.JsonStreamWriter.Builder)` |   
  
### setFlowControlSettings(FlowControlSettings flowControlSettings)
    
    
    public JsonStreamWriter.Builder setFlowControlSettings(FlowControlSettings flowControlSettings)

Setter for the underlying StreamWriter's FlowControlSettings.

**Parameter**  
---  
**Name** | **Description**  
`flowControlSettings` | `[FlowControlSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.batching.FlowControlSettings.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[JsonStreamWriter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.JsonStreamWriter.Builder)` | Builder  
  
### setIgnoreUnknownFields(boolean ignoreUnknownFields)
    
    
    public JsonStreamWriter.Builder setIgnoreUnknownFields(boolean ignoreUnknownFields)

Setter for a ignoreUnkownFields, if true, unknown Json fields to BigQuery will be ignored instead of error out.

**Parameter**  
---  
**Name** | **Description**  
`ignoreUnknownFields` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[JsonStreamWriter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.JsonStreamWriter.Builder)` | Builder  
  
### setLocation(String location)
    
    
    public JsonStreamWriter.Builder setLocation(String location)

Location of the table this stream writer is targeting. Connection pools are shared by location.

**Parameter**  
---  
**Name** | **Description**  
`location` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[JsonStreamWriter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.JsonStreamWriter.Builder)` | Builder  
  
### setMissingValueInterpretationMap(Map<String,AppendRowsRequest.MissingValueInterpretation> missingValueInterpretationMap)
    
    
    public JsonStreamWriter.Builder setMissingValueInterpretationMap(Map<String,AppendRowsRequest.MissingValueInterpretation> missingValueInterpretationMap)

Sets the missing value interpretation map for the JsonStreamWriter. The input missingValueInterpretationMap is used for all append requests unless otherwise changed.

**Parameter**  
---  
**Name** | **Description**  
`missingValueInterpretationMap` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[MissingValueInterpretation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretation)>`  
the missing value interpretation map used by the JsonStreamWriter.  
**Returns**  
---  
**Type** | **Description**  
`[JsonStreamWriter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.JsonStreamWriter.Builder)` | Builder  
  
### setReconnectAfter10M(boolean reconnectAfter10M)
    
    
    public JsonStreamWriter.Builder setReconnectAfter10M(boolean reconnectAfter10M)

This parameter is not used. It will be removed soon.

**Parameter**  
---  
**Name** | **Description**  
`reconnectAfter10M` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[JsonStreamWriter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.JsonStreamWriter.Builder)` |   
  
### setRetrySettings(RetrySettings retrySettings)
    
    
    public JsonStreamWriter.Builder setRetrySettings(RetrySettings retrySettings)

Enable client lib automatic retries on request level errors.

Immediate Retry code: ABORTED, UNAVAILABLE, CANCELLED, INTERNAL, DEADLINE_EXCEEDED Backoff Retry code: RESOURCE_EXHAUSTED

Example: RetrySettings retrySettings = RetrySettings.newBuilder() .setInitialRetryDelay(Duration.ofMillis(500)) // applies to backoff retry .setRetryDelayMultiplier(1.1) // applies to backoff retry .setMaxAttempts(5) // applies to both retries .setMaxRetryDelay(Duration.ofMinutes(1)) // applies to backoff retry .build();

**Parameter**  
---  
**Name** | **Description**  
`retrySettings` | `[RetrySettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[JsonStreamWriter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.JsonStreamWriter.Builder)` |   
  
### setTraceId(String traceId)
    
    
    public JsonStreamWriter.Builder setTraceId(String traceId)

Setter for a traceId to help identify traffic origin.

**Parameter**  
---  
**Name** | **Description**  
`traceId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[JsonStreamWriter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.JsonStreamWriter.Builder)` | Builder  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
