---
url: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1.stub.HttpJsonLocalInventoryServiceStub
title: Class HttpJsonLocalInventoryServiceStub (1.27.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:11:11.531498+00:00
---

# Class HttpJsonLocalInventoryServiceStub (1.27.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1.stub.HttpJsonLocalInventoryServiceStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class HttpJsonLocalInventoryServiceStub (1.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.27.0 (latest)  1.23.0  1.22.0  1.21.0  1.19.0  1.16.0  1.15.0  1.13.0  1.11.0  1.10.0  1.8.0  1.6.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.46.0  0.44.0  0.43.0  0.40.0  0.39.0  0.38.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0 
    
    
    public class HttpJsonLocalInventoryServiceStub extends LocalInventoryServiceStub

REST stub implementation for the LocalInventoryService service API.

This class is for advanced usage and reflects the underlying API directly.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [LocalInventoryServiceStub](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1.stub.LocalInventoryServiceStub) > HttpJsonLocalInventoryServiceStub

## Inherited Members

[LocalInventoryServiceStub.close()](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1.stub.LocalInventoryServiceStub#com_google_shopping_merchant_inventories_v1_stub_LocalInventoryServiceStub_close__)

[LocalInventoryServiceStub.deleteLocalInventoryCallable()](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1.stub.LocalInventoryServiceStub#com_google_shopping_merchant_inventories_v1_stub_LocalInventoryServiceStub_deleteLocalInventoryCallable__)

[LocalInventoryServiceStub.insertLocalInventoryCallable()](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1.stub.LocalInventoryServiceStub#com_google_shopping_merchant_inventories_v1_stub_LocalInventoryServiceStub_insertLocalInventoryCallable__)

[LocalInventoryServiceStub.listLocalInventoriesCallable()](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1.stub.LocalInventoryServiceStub#com_google_shopping_merchant_inventories_v1_stub_LocalInventoryServiceStub_listLocalInventoriesCallable__)

[LocalInventoryServiceStub.listLocalInventoriesPagedCallable()](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1.stub.LocalInventoryServiceStub#com_google_shopping_merchant_inventories_v1_stub_LocalInventoryServiceStub_listLocalInventoriesPagedCallable__)

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
    
    
    public static final HttpJsonLocalInventoryServiceStub create(ClientContext clientContext)

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HttpJsonLocalInventoryServiceStub](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1.stub.HttpJsonLocalInventoryServiceStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ClientContext clientContext, HttpJsonStubCallableFactory callableFactory)
    
    
    public static final HttpJsonLocalInventoryServiceStub create(ClientContext clientContext, HttpJsonStubCallableFactory callableFactory)

**Parameters**  
---  
**Name** | **Description**  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.html)`  
  
`callableFactory` | `[HttpJsonStubCallableFactory](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.HttpJsonStubCallableFactory.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HttpJsonLocalInventoryServiceStub](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1.stub.HttpJsonLocalInventoryServiceStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(LocalInventoryServiceStubSettings settings)
    
    
    public static final HttpJsonLocalInventoryServiceStub create(LocalInventoryServiceStubSettings settings)

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[LocalInventoryServiceStubSettings](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1.stub.LocalInventoryServiceStubSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HttpJsonLocalInventoryServiceStub](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1.stub.HttpJsonLocalInventoryServiceStub)` |   
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

### HttpJsonLocalInventoryServiceStub(LocalInventoryServiceStubSettings settings, ClientContext clientContext)
    
    
    protected HttpJsonLocalInventoryServiceStub(LocalInventoryServiceStubSettings settings, ClientContext clientContext)

Constructs an instance of HttpJsonLocalInventoryServiceStub, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameters**  
---  
**Name** | **Description**  
`settings` | `[LocalInventoryServiceStubSettings](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1.stub.LocalInventoryServiceStubSettings)`  
  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.html)`  
  
  
### HttpJsonLocalInventoryServiceStub(LocalInventoryServiceStubSettings settings, ClientContext clientContext, HttpJsonStubCallableFactory callableFactory)
    
    
    protected HttpJsonLocalInventoryServiceStub(LocalInventoryServiceStubSettings settings, ClientContext clientContext, HttpJsonStubCallableFactory callableFactory)

Constructs an instance of HttpJsonLocalInventoryServiceStub, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameters**  
---  
**Name** | **Description**  
`settings` | `[LocalInventoryServiceStubSettings](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1.stub.LocalInventoryServiceStubSettings)`  
  
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

[LocalInventoryServiceStub.close()](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1.stub.LocalInventoryServiceStub#com_google_shopping_merchant_inventories_v1_stub_LocalInventoryServiceStub_close__)

### deleteLocalInventoryCallable()
    
    
    public UnaryCallable<DeleteLocalInventoryRequest,Empty> deleteLocalInventoryCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteLocalInventoryRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1.DeleteLocalInventoryRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
**Overrides**

[LocalInventoryServiceStub.deleteLocalInventoryCallable()](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1.stub.LocalInventoryServiceStub#com_google_shopping_merchant_inventories_v1_stub_LocalInventoryServiceStub_deleteLocalInventoryCallable__)

### insertLocalInventoryCallable()
    
    
    public UnaryCallable<InsertLocalInventoryRequest,LocalInventory> insertLocalInventoryCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertLocalInventoryRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1.InsertLocalInventoryRequest),[LocalInventory](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1.LocalInventory)>` |   
**Overrides**

[LocalInventoryServiceStub.insertLocalInventoryCallable()](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1.stub.LocalInventoryServiceStub#com_google_shopping_merchant_inventories_v1_stub_LocalInventoryServiceStub_insertLocalInventoryCallable__)

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
  
### listLocalInventoriesCallable()
    
    
    public UnaryCallable<ListLocalInventoriesRequest,ListLocalInventoriesResponse> listLocalInventoriesCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListLocalInventoriesRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1.ListLocalInventoriesRequest),[ListLocalInventoriesResponse](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1.ListLocalInventoriesResponse)>` |   
**Overrides**

[LocalInventoryServiceStub.listLocalInventoriesCallable()](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1.stub.LocalInventoryServiceStub#com_google_shopping_merchant_inventories_v1_stub_LocalInventoryServiceStub_listLocalInventoriesCallable__)

### listLocalInventoriesPagedCallable()
    
    
    public UnaryCallable<ListLocalInventoriesRequest,LocalInventoryServiceClient.ListLocalInventoriesPagedResponse> listLocalInventoriesPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListLocalInventoriesRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1.ListLocalInventoriesRequest),[ListLocalInventoriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1.LocalInventoryServiceClient.ListLocalInventoriesPagedResponse)>` |   
**Overrides**

[LocalInventoryServiceStub.listLocalInventoriesPagedCallable()](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1.stub.LocalInventoryServiceStub#com_google_shopping_merchant_inventories_v1_stub_LocalInventoryServiceStub_listLocalInventoriesPagedCallable__)

### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
