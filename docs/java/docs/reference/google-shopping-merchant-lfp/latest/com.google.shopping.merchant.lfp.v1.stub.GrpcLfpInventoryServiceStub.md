---
url: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-lfp/latest/com.google.shopping.merchant.lfp.v1.stub.GrpcLfpInventoryServiceStub
title: Class GrpcLfpInventoryServiceStub (1.27.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:39:29.268658+00:00
---

# Class GrpcLfpInventoryServiceStub (1.27.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-lfp/latest/com.google.shopping.merchant.lfp.v1.stub.GrpcLfpInventoryServiceStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class GrpcLfpInventoryServiceStub (1.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.27.0 (latest)  1.23.0  1.22.0  1.21.0  1.19.0  1.16.0  1.15.0  1.13.0  1.11.0  1.10.0  1.8.0  1.6.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public class GrpcLfpInventoryServiceStub extends LfpInventoryServiceStub

gRPC stub implementation for the LfpInventoryService service API.

This class is for advanced usage and reflects the underlying API directly.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [LfpInventoryServiceStub](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-lfp/latest/com.google.shopping.merchant.lfp.v1.stub.LfpInventoryServiceStub) > GrpcLfpInventoryServiceStub

## Inherited Members

[LfpInventoryServiceStub.close()](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-lfp/latest/com.google.shopping.merchant.lfp.v1.stub.LfpInventoryServiceStub#com_google_shopping_merchant_lfp_v1_stub_LfpInventoryServiceStub_close__)

[LfpInventoryServiceStub.insertLfpInventoryCallable()](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-lfp/latest/com.google.shopping.merchant.lfp.v1.stub.LfpInventoryServiceStub#com_google_shopping_merchant_lfp_v1_stub_LfpInventoryServiceStub_insertLfpInventoryCallable__)

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
    
    
    public static final GrpcLfpInventoryServiceStub create(ClientContext clientContext)

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GrpcLfpInventoryServiceStub](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-lfp/latest/com.google.shopping.merchant.lfp.v1.stub.GrpcLfpInventoryServiceStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ClientContext clientContext, GrpcStubCallableFactory callableFactory)
    
    
    public static final GrpcLfpInventoryServiceStub create(ClientContext clientContext, GrpcStubCallableFactory callableFactory)

**Parameters**  
---  
**Name** | **Description**  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.html)`  
  
`callableFactory` | `[GrpcStubCallableFactory](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.GrpcStubCallableFactory.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GrpcLfpInventoryServiceStub](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-lfp/latest/com.google.shopping.merchant.lfp.v1.stub.GrpcLfpInventoryServiceStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(LfpInventoryServiceStubSettings settings)
    
    
    public static final GrpcLfpInventoryServiceStub create(LfpInventoryServiceStubSettings settings)

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[LfpInventoryServiceStubSettings](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-lfp/latest/com.google.shopping.merchant.lfp.v1.stub.LfpInventoryServiceStubSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GrpcLfpInventoryServiceStub](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-lfp/latest/com.google.shopping.merchant.lfp.v1.stub.GrpcLfpInventoryServiceStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
## Constructors 

### GrpcLfpInventoryServiceStub(LfpInventoryServiceStubSettings settings, ClientContext clientContext)
    
    
    protected GrpcLfpInventoryServiceStub(LfpInventoryServiceStubSettings settings, ClientContext clientContext)

Constructs an instance of GrpcLfpInventoryServiceStub, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameters**  
---  
**Name** | **Description**  
`settings` | `[LfpInventoryServiceStubSettings](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-lfp/latest/com.google.shopping.merchant.lfp.v1.stub.LfpInventoryServiceStubSettings)`  
  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.html)`  
  
  
### GrpcLfpInventoryServiceStub(LfpInventoryServiceStubSettings settings, ClientContext clientContext, GrpcStubCallableFactory callableFactory)
    
    
    protected GrpcLfpInventoryServiceStub(LfpInventoryServiceStubSettings settings, ClientContext clientContext, GrpcStubCallableFactory callableFactory)

Constructs an instance of GrpcLfpInventoryServiceStub, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameters**  
---  
**Name** | **Description**  
`settings` | `[LfpInventoryServiceStubSettings](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-lfp/latest/com.google.shopping.merchant.lfp.v1.stub.LfpInventoryServiceStubSettings)`  
  
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

[LfpInventoryServiceStub.close()](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-lfp/latest/com.google.shopping.merchant.lfp.v1.stub.LfpInventoryServiceStub#com_google_shopping_merchant_lfp_v1_stub_LfpInventoryServiceStub_close__)

### getOperationsStub()
    
    
    public GrpcOperationsStub getOperationsStub()

**Returns**  
---  
**Type** | **Description**  
`[GrpcOperationsStub](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.stub.GrpcOperationsStub.html)` |   
  
### insertLfpInventoryCallable()
    
    
    public UnaryCallable<InsertLfpInventoryRequest,LfpInventory> insertLfpInventoryCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertLfpInventoryRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-lfp/latest/com.google.shopping.merchant.lfp.v1.InsertLfpInventoryRequest),[LfpInventory](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-lfp/latest/com.google.shopping.merchant.lfp.v1.LfpInventory)>` |   
**Overrides**

[LfpInventoryServiceStub.insertLfpInventoryCallable()](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-lfp/latest/com.google.shopping.merchant.lfp.v1.stub.LfpInventoryServiceStub#com_google_shopping_merchant_lfp_v1_stub_LfpInventoryServiceStub_insertLfpInventoryCallable__)

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
