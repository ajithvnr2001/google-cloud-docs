---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-trace/latest/com.google.cloud.trace.v2.stub.GrpcTraceServiceStub
title: Class GrpcTraceServiceStub (2.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:52:57.953133+00:00
---

# Class GrpcTraceServiceStub (2.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-trace/latest/com.google.cloud.trace.v2.stub.GrpcTraceServiceStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class GrpcTraceServiceStub (2.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.99.0 (latest)  2.95.0  2.94.0  2.93.0  2.91.0  2.88.0  2.87.0  2.85.0  2.83.0  2.82.0  2.80.0  2.78.0  2.76.0  2.75.0  2.74.0  2.73.0  2.72.0  2.70.0  2.68.0  2.67.0  2.64.0  2.63.0  2.62.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.7  2.2.0  2.1.13 
    
    
    public class GrpcTraceServiceStub extends TraceServiceStub

gRPC stub implementation for the TraceService service API.

This class is for advanced usage and reflects the underlying API directly.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [TraceServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-trace/latest/com.google.cloud.trace.v2.stub.TraceServiceStub) > GrpcTraceServiceStub

## Inherited Members

[TraceServiceStub.batchWriteSpansCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-trace/latest/com.google.cloud.trace.v2.stub.TraceServiceStub#com_google_cloud_trace_v2_stub_TraceServiceStub_batchWriteSpansCallable__)

[TraceServiceStub.close()](https://docs.cloud.google.com/java/docs/reference/google-cloud-trace/latest/com.google.cloud.trace.v2.stub.TraceServiceStub#com_google_cloud_trace_v2_stub_TraceServiceStub_close__)

[TraceServiceStub.createSpanCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-trace/latest/com.google.cloud.trace.v2.stub.TraceServiceStub#com_google_cloud_trace_v2_stub_TraceServiceStub_createSpanCallable__)

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

## Static Methods 

### create(ClientContext clientContext)
    
    
    public static final GrpcTraceServiceStub create(ClientContext clientContext)

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GrpcTraceServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-trace/latest/com.google.cloud.trace.v2.stub.GrpcTraceServiceStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ClientContext clientContext, GrpcStubCallableFactory callableFactory)
    
    
    public static final GrpcTraceServiceStub create(ClientContext clientContext, GrpcStubCallableFactory callableFactory)

**Parameters**  
---  
**Name** | **Description**  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.html)`  
  
`callableFactory` | `[GrpcStubCallableFactory](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.GrpcStubCallableFactory.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GrpcTraceServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-trace/latest/com.google.cloud.trace.v2.stub.GrpcTraceServiceStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(TraceServiceStubSettings settings)
    
    
    public static final GrpcTraceServiceStub create(TraceServiceStubSettings settings)

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[TraceServiceStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-trace/latest/com.google.cloud.trace.v2.stub.TraceServiceStubSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GrpcTraceServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-trace/latest/com.google.cloud.trace.v2.stub.GrpcTraceServiceStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
## Constructors 

### GrpcTraceServiceStub(TraceServiceStubSettings settings, ClientContext clientContext)
    
    
    protected GrpcTraceServiceStub(TraceServiceStubSettings settings, ClientContext clientContext)

Constructs an instance of GrpcTraceServiceStub, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameters**  
---  
**Name** | **Description**  
`settings` | `[TraceServiceStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-trace/latest/com.google.cloud.trace.v2.stub.TraceServiceStubSettings)`  
  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.html)`  
  
  
### GrpcTraceServiceStub(TraceServiceStubSettings settings, ClientContext clientContext, GrpcStubCallableFactory callableFactory)
    
    
    protected GrpcTraceServiceStub(TraceServiceStubSettings settings, ClientContext clientContext, GrpcStubCallableFactory callableFactory)

Constructs an instance of GrpcTraceServiceStub, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameters**  
---  
**Name** | **Description**  
`settings` | `[TraceServiceStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-trace/latest/com.google.cloud.trace.v2.stub.TraceServiceStubSettings)`  
  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.html)`  
  
`callableFactory` | `[GrpcStubCallableFactory](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.GrpcStubCallableFactory.html)`  
  
  
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
  
### batchWriteSpansCallable()
    
    
    public UnaryCallable<BatchWriteSpansRequest,Empty> batchWriteSpansCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchWriteSpansRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-trace/latest/com.google.devtools.cloudtrace.v2.BatchWriteSpansRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
**Overrides**

[TraceServiceStub.batchWriteSpansCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-trace/latest/com.google.cloud.trace.v2.stub.TraceServiceStub#com_google_cloud_trace_v2_stub_TraceServiceStub_batchWriteSpansCallable__)

### close()
    
    
    public final void close()

**Overrides**

[TraceServiceStub.close()](https://docs.cloud.google.com/java/docs/reference/google-cloud-trace/latest/com.google.cloud.trace.v2.stub.TraceServiceStub#com_google_cloud_trace_v2_stub_TraceServiceStub_close__)

### createSpanCallable()
    
    
    public UnaryCallable<Span,Span> createSpanCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[Span](https://docs.cloud.google.com/java/docs/reference/google-cloud-trace/latest/com.google.devtools.cloudtrace.v2.Span),[Span](https://docs.cloud.google.com/java/docs/reference/google-cloud-trace/latest/com.google.devtools.cloudtrace.v2.Span)>` |   
**Overrides**

[TraceServiceStub.createSpanCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-trace/latest/com.google.cloud.trace.v2.stub.TraceServiceStub#com_google_cloud_trace_v2_stub_TraceServiceStub_createSpanCallable__)

### getOperationsStub()
    
    
    public GrpcOperationsStub getOperationsStub()

**Returns**  
---  
**Type** | **Description**  
`[GrpcOperationsStub](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.stub.GrpcOperationsStub.html)` |   
  
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

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
