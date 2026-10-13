---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.stub.GrpcConversationalSearchServiceStub
title: Class GrpcConversationalSearchServiceStub (2.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:24:40.434692+00:00
---

# Class GrpcConversationalSearchServiceStub (2.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.stub.GrpcConversationalSearchServiceStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class GrpcConversationalSearchServiceStub (2.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.101.0 (latest)  2.97.0  2.96.0  2.95.0  2.93.0  2.90.0  2.89.0  2.87.0  2.85.0  2.84.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.74.0  2.72.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.1  2.4.0  2.3.0  2.2.3  2.1.0  2.0.19 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 
    
    
    public class GrpcConversationalSearchServiceStub extends ConversationalSearchServiceStub

gRPC stub implementation for the ConversationalSearchService service API.

This class is for advanced usage and reflects the underlying API directly.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [ConversationalSearchServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.stub.ConversationalSearchServiceStub) > GrpcConversationalSearchServiceStub

## Inherited Members

[ConversationalSearchServiceStub.close()](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.stub.ConversationalSearchServiceStub#com_google_cloud_retail_v2alpha_stub_ConversationalSearchServiceStub_close__)

[ConversationalSearchServiceStub.conversationalSearchCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.stub.ConversationalSearchServiceStub#com_google_cloud_retail_v2alpha_stub_ConversationalSearchServiceStub_conversationalSearchCallable__)

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
    
    
    public static final GrpcConversationalSearchServiceStub create(ClientContext clientContext)

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GrpcConversationalSearchServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.stub.GrpcConversationalSearchServiceStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ClientContext clientContext, GrpcStubCallableFactory callableFactory)
    
    
    public static final GrpcConversationalSearchServiceStub create(ClientContext clientContext, GrpcStubCallableFactory callableFactory)

**Parameters**  
---  
**Name** | **Description**  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.html)`  
  
`callableFactory` | `[GrpcStubCallableFactory](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.GrpcStubCallableFactory.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GrpcConversationalSearchServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.stub.GrpcConversationalSearchServiceStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ConversationalSearchServiceStubSettings settings)
    
    
    public static final GrpcConversationalSearchServiceStub create(ConversationalSearchServiceStubSettings settings)

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ConversationalSearchServiceStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.stub.ConversationalSearchServiceStubSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GrpcConversationalSearchServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.stub.GrpcConversationalSearchServiceStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
## Constructors 

### GrpcConversationalSearchServiceStub(ConversationalSearchServiceStubSettings settings, ClientContext clientContext)
    
    
    protected GrpcConversationalSearchServiceStub(ConversationalSearchServiceStubSettings settings, ClientContext clientContext)

Constructs an instance of GrpcConversationalSearchServiceStub, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameters**  
---  
**Name** | **Description**  
`settings` | `[ConversationalSearchServiceStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.stub.ConversationalSearchServiceStubSettings)`  
  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.html)`  
  
  
### GrpcConversationalSearchServiceStub(ConversationalSearchServiceStubSettings settings, ClientContext clientContext, GrpcStubCallableFactory callableFactory)
    
    
    protected GrpcConversationalSearchServiceStub(ConversationalSearchServiceStubSettings settings, ClientContext clientContext, GrpcStubCallableFactory callableFactory)

Constructs an instance of GrpcConversationalSearchServiceStub, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameters**  
---  
**Name** | **Description**  
`settings` | `[ConversationalSearchServiceStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.stub.ConversationalSearchServiceStubSettings)`  
  
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
  
### close()
    
    
    public final void close()

**Overrides**

[ConversationalSearchServiceStub.close()](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.stub.ConversationalSearchServiceStub#com_google_cloud_retail_v2alpha_stub_ConversationalSearchServiceStub_close__)

### conversationalSearchCallable()
    
    
    public ServerStreamingCallable<ConversationalSearchRequest,ConversationalSearchResponse> conversationalSearchCallable()

**Returns**  
---  
**Type** | **Description**  
`[ServerStreamingCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ServerStreamingCallable.html)<[ConversationalSearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.ConversationalSearchRequest),[ConversationalSearchResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.ConversationalSearchResponse)>` |   
**Overrides**

[ConversationalSearchServiceStub.conversationalSearchCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.stub.ConversationalSearchServiceStub#com_google_cloud_retail_v2alpha_stub_ConversationalSearchServiceStub_conversationalSearchCallable__)

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

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
