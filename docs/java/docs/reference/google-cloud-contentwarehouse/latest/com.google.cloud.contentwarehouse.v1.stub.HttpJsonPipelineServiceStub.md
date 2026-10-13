---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.stub.HttpJsonPipelineServiceStub
title: Class HttpJsonPipelineServiceStub (0.95.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:46:07.823557+00:00
---

# Class HttpJsonPipelineServiceStub (0.95.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.stub.HttpJsonPipelineServiceStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class HttpJsonPipelineServiceStub (0.95.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.95.0 (latest)  0.91.0  0.90.0  0.89.0  0.87.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.70.0  0.69.0  0.68.0  0.66.0  0.64.0  0.63.0  0.60.0  0.59.0  0.58.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public class HttpJsonPipelineServiceStub extends PipelineServiceStub

REST stub implementation for the PipelineService service API.

This class is for advanced usage and reflects the underlying API directly.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [PipelineServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.stub.PipelineServiceStub) > HttpJsonPipelineServiceStub

## Inherited Members

[PipelineServiceStub.close()](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.stub.PipelineServiceStub#com_google_cloud_contentwarehouse_v1_stub_PipelineServiceStub_close__)

[PipelineServiceStub.getHttpJsonOperationsStub()](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.stub.PipelineServiceStub#com_google_cloud_contentwarehouse_v1_stub_PipelineServiceStub_getHttpJsonOperationsStub__)

[PipelineServiceStub.getOperationsStub()](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.stub.PipelineServiceStub#com_google_cloud_contentwarehouse_v1_stub_PipelineServiceStub_getOperationsStub__)

[PipelineServiceStub.runPipelineCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.stub.PipelineServiceStub#com_google_cloud_contentwarehouse_v1_stub_PipelineServiceStub_runPipelineCallable__)

[PipelineServiceStub.runPipelineOperationCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.stub.PipelineServiceStub#com_google_cloud_contentwarehouse_v1_stub_PipelineServiceStub_runPipelineOperationCallable__)

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
    
    
    public static final HttpJsonPipelineServiceStub create(ClientContext clientContext)

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HttpJsonPipelineServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.stub.HttpJsonPipelineServiceStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ClientContext clientContext, HttpJsonStubCallableFactory callableFactory)
    
    
    public static final HttpJsonPipelineServiceStub create(ClientContext clientContext, HttpJsonStubCallableFactory callableFactory)

**Parameters**  
---  
**Name** | **Description**  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.html)`  
  
`callableFactory` | `[HttpJsonStubCallableFactory](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.HttpJsonStubCallableFactory.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HttpJsonPipelineServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.stub.HttpJsonPipelineServiceStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(PipelineServiceStubSettings settings)
    
    
    public static final HttpJsonPipelineServiceStub create(PipelineServiceStubSettings settings)

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[PipelineServiceStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.stub.PipelineServiceStubSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HttpJsonPipelineServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.stub.HttpJsonPipelineServiceStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### getMethodDescriptors()
    
    
    public static List<ApiMethodDescriptor> getMethodDescriptors()

**Internal Only** : This feature is not stable for application use.

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ApiMethodDescriptor](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.ApiMethodDescriptor.html)>` |   
  
## Constructors 

### HttpJsonPipelineServiceStub(PipelineServiceStubSettings settings, ClientContext clientContext)
    
    
    protected HttpJsonPipelineServiceStub(PipelineServiceStubSettings settings, ClientContext clientContext)

Constructs an instance of HttpJsonPipelineServiceStub, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameters**  
---  
**Name** | **Description**  
`settings` | `[PipelineServiceStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.stub.PipelineServiceStubSettings)`  
  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.html)`  
  
  
### HttpJsonPipelineServiceStub(PipelineServiceStubSettings settings, ClientContext clientContext, HttpJsonStubCallableFactory callableFactory)
    
    
    protected HttpJsonPipelineServiceStub(PipelineServiceStubSettings settings, ClientContext clientContext, HttpJsonStubCallableFactory callableFactory)

Constructs an instance of HttpJsonPipelineServiceStub, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameters**  
---  
**Name** | **Description**  
`settings` | `[PipelineServiceStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.stub.PipelineServiceStubSettings)`  
  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.html)`  
  
`callableFactory` | `[HttpJsonStubCallableFactory](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.HttpJsonStubCallableFactory.html)`  
  
  
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

**Overrides**

[PipelineServiceStub.close()](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.stub.PipelineServiceStub#com_google_cloud_contentwarehouse_v1_stub_PipelineServiceStub_close__)

### getHttpJsonOperationsStub()
    
    
    public HttpJsonOperationsStub getHttpJsonOperationsStub()

**Returns**  
---  
**Type** | **Description**  
`[HttpJsonOperationsStub](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.stub.HttpJsonOperationsStub.html)` |   
**Overrides**

[PipelineServiceStub.getHttpJsonOperationsStub()](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.stub.PipelineServiceStub#com_google_cloud_contentwarehouse_v1_stub_PipelineServiceStub_getHttpJsonOperationsStub__)

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
  
### runPipelineCallable()
    
    
    public UnaryCallable<RunPipelineRequest,Operation> runPipelineCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RunPipelineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RunPipelineRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
**Overrides**

[PipelineServiceStub.runPipelineCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.stub.PipelineServiceStub#com_google_cloud_contentwarehouse_v1_stub_PipelineServiceStub_runPipelineCallable__)

### runPipelineOperationCallable()
    
    
    public OperationCallable<RunPipelineRequest,RunPipelineResponse,RunPipelineMetadata> runPipelineOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RunPipelineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RunPipelineRequest),[RunPipelineResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RunPipelineResponse),[RunPipelineMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RunPipelineMetadata)>` |   
**Overrides**

[PipelineServiceStub.runPipelineOperationCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.stub.PipelineServiceStub#com_google_cloud_contentwarehouse_v1_stub_PipelineServiceStub_runPipelineOperationCallable__)

### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
