---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.SchemaAwareStreamWriter.Builder
title: Class SchemaAwareStreamWriter.Builder<T> (3.35.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:59:38.196095+00:00
---

# Class SchemaAwareStreamWriter.Builder<T> (3.35.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.SchemaAwareStreamWriter.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SchemaAwareStreamWriter.Builder<T> (3.35.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.35.0 (latest)  3.31.0  3.30.0  3.29.0  3.27.0  3.24.0  3.23.0  3.21.0  3.20.0  3.19.1  3.18.0  3.17.3  3.16.3  3.15.3  3.14.1  3.12.0  3.11.4  3.10.3  3.9.3  3.8.0  3.6.1  3.5.2  3.4.0  3.3.1  3.2.0  3.1.0  3.0.1  2.47.0  2.45.0  2.44.1  2.43.0 
    
    
    public static final class SchemaAwareStreamWriter.Builder<T>

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > SchemaAwareStreamWriter.Builder<T>

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

## Type Parameter  
  
---  
**Name** | **Description**  
`T` |   
  
## Methods 

### build()
    
    
    public SchemaAwareStreamWriter<T> build()

Builds SchemaAwareStreamWriter

**Returns**  
---  
**Type** | **Description**  
`[SchemaAwareStreamWriter](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.SchemaAwareStreamWriter)<T>` | SchemaAwareStreamWriter  
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
    
    
    public SchemaAwareStreamWriter.Builder<T> setChannelProvider(TransportChannelProvider channelProvider)

Setter for the underlying StreamWriter's TransportChannelProvider.

**Parameter**  
---  
**Name** | **Description**  
`channelProvider` | `[TransportChannelProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.TransportChannelProvider.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.SchemaAwareStreamWriter.Builder)<T>` | Builder  
  
### setCompressorName(String compressorName)
    
    
    public SchemaAwareStreamWriter.Builder<T> setCompressorName(String compressorName)

Sets the compression to use for the calls. The compressor must be of type gzip.

**Parameter**  
---  
**Name** | **Description**  
`compressorName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.SchemaAwareStreamWriter.Builder)<T>` | Builder  
  
### setCredentialsProvider(CredentialsProvider credentialsProvider)
    
    
    public SchemaAwareStreamWriter.Builder<T> setCredentialsProvider(CredentialsProvider credentialsProvider)

Setter for the underlying StreamWriter's CredentialsProvider.

**Parameter**  
---  
**Name** | **Description**  
`credentialsProvider` | `[CredentialsProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.CredentialsProvider.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.SchemaAwareStreamWriter.Builder)<T>` | Builder  
  
### setDefaultMissingValueInterpretation(AppendRowsRequest.MissingValueInterpretation defaultMissingValueInterpretation)
    
    
    public SchemaAwareStreamWriter.Builder setDefaultMissingValueInterpretation(AppendRowsRequest.MissingValueInterpretation defaultMissingValueInterpretation)

Sets the default missing value interpretation value if the column is not presented in the missing_value_interpretations map.

**Parameter**  
---  
**Name** | **Description**  
`defaultMissingValueInterpretation` | `[AppendRowsRequest.MissingValueInterpretation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretation)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SchemaAwareStreamWriter.Builder<T>](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.SchemaAwareStreamWriter.Builder)` |   
  
### setEnableConnectionPool(boolean enableConnectionPool)
    
    
    public SchemaAwareStreamWriter.Builder<T> setEnableConnectionPool(boolean enableConnectionPool)

Enable multiplexing for this writer. In multiplexing mode tables will share the same connection if possible until the connection is overwhelmed. This feature is still under development, please contact write api team before using.

**Parameter**  
---  
**Name** | **Description**  
`enableConnectionPool` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.SchemaAwareStreamWriter.Builder)<T>` | Builder  
  
### setEnableLatencyProfiler(boolean enableLatencyProfiler)
    
    
    public SchemaAwareStreamWriter.Builder setEnableLatencyProfiler(boolean enableLatencyProfiler)

Enable a latency profiler that would periodically generate a detailed latency report for the top latency requests. This is currently an experimental API.

**Parameter**  
---  
**Name** | **Description**  
`enableLatencyProfiler` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SchemaAwareStreamWriter.Builder<T>](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.SchemaAwareStreamWriter.Builder)` |   
  
### setEnableOpenTelemetry(boolean enableOpenTelemetry)
    
    
    public SchemaAwareStreamWriter.Builder setEnableOpenTelemetry(boolean enableOpenTelemetry)

Enable generation of metrics for OpenTelemetry.

**Parameter**  
---  
**Name** | **Description**  
`enableOpenTelemetry` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SchemaAwareStreamWriter.Builder<T>](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.SchemaAwareStreamWriter.Builder)` |   
  
### setEndpoint(String endpoint)
    
    
    public SchemaAwareStreamWriter.Builder<T> setEndpoint(String endpoint)

Setter for the underlying StreamWriter's Endpoint.

**Parameter**  
---  
**Name** | **Description**  
`endpoint` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.SchemaAwareStreamWriter.Builder)<T>` | Builder  
  
### setExecutorProvider(ExecutorProvider executorProvider)
    
    
    public SchemaAwareStreamWriter.Builder<T> setExecutorProvider(ExecutorProvider executorProvider)

Setter for the underlying StreamWriter's ExecutorProvider.

**Parameter**  
---  
**Name** | **Description**  
`executorProvider` | `[ExecutorProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.ExecutorProvider.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.SchemaAwareStreamWriter.Builder)<T>` |   
  
### setFlowControlSettings(FlowControlSettings flowControlSettings)
    
    
    public SchemaAwareStreamWriter.Builder<T> setFlowControlSettings(FlowControlSettings flowControlSettings)

Setter for the underlying StreamWriter's FlowControlSettings.

**Parameter**  
---  
**Name** | **Description**  
`flowControlSettings` | `[FlowControlSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.batching.FlowControlSettings.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.SchemaAwareStreamWriter.Builder)<T>` | Builder  
  
### setIgnoreUnknownFields(boolean ignoreUnknownFields)
    
    
    public SchemaAwareStreamWriter.Builder<T> setIgnoreUnknownFields(boolean ignoreUnknownFields)

Setter for a ignoreUnknownFields, if true, unknown fields to BigQuery will be ignored instead of error out. 1

**Parameter**  
---  
**Name** | **Description**  
`ignoreUnknownFields` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.SchemaAwareStreamWriter.Builder)<T>` | Builder  
  
### setLocation(String location)
    
    
    public SchemaAwareStreamWriter.Builder<T> setLocation(String location)

Location of the table this stream writer is targeting. Connection pools are shared by location.

**Parameter**  
---  
**Name** | **Description**  
`location` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.SchemaAwareStreamWriter.Builder)<T>` | Builder  
  
### setMissingValueInterpretationMap(Map<String,AppendRowsRequest.MissingValueInterpretation> missingValueInterpretationMap)
    
    
    public SchemaAwareStreamWriter.Builder setMissingValueInterpretationMap(Map<String,AppendRowsRequest.MissingValueInterpretation> missingValueInterpretationMap)

Sets the missing value interpretation map for the SchemaAwareStreamWriter. The input missingValueInterpretationMap is used for all append requests unless otherwise changed.

**Parameter**  
---  
**Name** | **Description**  
`missingValueInterpretationMap` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[MissingValueInterpretation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretation)>`  
the missing value interpretation map used by the SchemaAwareStreamWriter.  
**Returns**  
---  
**Type** | **Description**  
`[SchemaAwareStreamWriter.Builder<T>](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.SchemaAwareStreamWriter.Builder)` | Builder  
  
### setRetrySettings(RetrySettings retrySettings)
    
    
    public SchemaAwareStreamWriter.Builder setRetrySettings(RetrySettings retrySettings)

Sets the RetrySettings to use for in-stream error retry.

**Parameter**  
---  
**Name** | **Description**  
`retrySettings` | `[RetrySettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SchemaAwareStreamWriter.Builder<T>](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.SchemaAwareStreamWriter.Builder)` | Builder  
  
### setTraceId(String traceId)
    
    
    public SchemaAwareStreamWriter.Builder<T> setTraceId(String traceId)

Setter for a traceId to help identify traffic origin.

**Parameter**  
---  
**Name** | **Description**  
`traceId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.SchemaAwareStreamWriter.Builder)<T>` | Builder  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
