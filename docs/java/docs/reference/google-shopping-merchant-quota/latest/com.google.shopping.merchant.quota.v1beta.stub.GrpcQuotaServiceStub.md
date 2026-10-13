---
url: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-quota/latest/com.google.shopping.merchant.quota.v1beta.stub.GrpcQuotaServiceStub
title: Class GrpcQuotaServiceStub (1.27.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:45:19.001449+00:00
---

# Class GrpcQuotaServiceStub (1.27.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-quota/latest/com.google.shopping.merchant.quota.v1beta.stub.GrpcQuotaServiceStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class GrpcQuotaServiceStub (1.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.27.0 (latest)  1.23.0  1.22.0  1.21.0  1.19.0  1.16.0  1.15.0  1.13.0  1.11.0  1.10.0  1.8.0  1.6.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.33.0  0.31.0  0.30.0  0.27.0  0.26.0  0.25.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 
    
    
    public class GrpcQuotaServiceStub extends QuotaServiceStub

gRPC stub implementation for the QuotaService service API.

This class is for advanced usage and reflects the underlying API directly.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [QuotaServiceStub](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-quota/latest/com.google.shopping.merchant.quota.v1beta.stub.QuotaServiceStub) > GrpcQuotaServiceStub

## Inherited Members

[QuotaServiceStub.close()](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-quota/latest/com.google.shopping.merchant.quota.v1beta.stub.QuotaServiceStub#com_google_shopping_merchant_quota_v1beta_stub_QuotaServiceStub_close__)

[QuotaServiceStub.listQuotaGroupsCallable()](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-quota/latest/com.google.shopping.merchant.quota.v1beta.stub.QuotaServiceStub#com_google_shopping_merchant_quota_v1beta_stub_QuotaServiceStub_listQuotaGroupsCallable__)

[QuotaServiceStub.listQuotaGroupsPagedCallable()](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-quota/latest/com.google.shopping.merchant.quota.v1beta.stub.QuotaServiceStub#com_google_shopping_merchant_quota_v1beta_stub_QuotaServiceStub_listQuotaGroupsPagedCallable__)

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
    
    
    public static final GrpcQuotaServiceStub create(ClientContext clientContext)

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GrpcQuotaServiceStub](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-quota/latest/com.google.shopping.merchant.quota.v1beta.stub.GrpcQuotaServiceStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ClientContext clientContext, GrpcStubCallableFactory callableFactory)
    
    
    public static final GrpcQuotaServiceStub create(ClientContext clientContext, GrpcStubCallableFactory callableFactory)

**Parameters**  
---  
**Name** | **Description**  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.html)`  
  
`callableFactory` | `[GrpcStubCallableFactory](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.GrpcStubCallableFactory.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GrpcQuotaServiceStub](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-quota/latest/com.google.shopping.merchant.quota.v1beta.stub.GrpcQuotaServiceStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(QuotaServiceStubSettings settings)
    
    
    public static final GrpcQuotaServiceStub create(QuotaServiceStubSettings settings)

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[QuotaServiceStubSettings](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-quota/latest/com.google.shopping.merchant.quota.v1beta.stub.QuotaServiceStubSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GrpcQuotaServiceStub](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-quota/latest/com.google.shopping.merchant.quota.v1beta.stub.GrpcQuotaServiceStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
## Constructors 

### GrpcQuotaServiceStub(QuotaServiceStubSettings settings, ClientContext clientContext)
    
    
    protected GrpcQuotaServiceStub(QuotaServiceStubSettings settings, ClientContext clientContext)

Constructs an instance of GrpcQuotaServiceStub, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameters**  
---  
**Name** | **Description**  
`settings` | `[QuotaServiceStubSettings](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-quota/latest/com.google.shopping.merchant.quota.v1beta.stub.QuotaServiceStubSettings)`  
  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.html)`  
  
  
### GrpcQuotaServiceStub(QuotaServiceStubSettings settings, ClientContext clientContext, GrpcStubCallableFactory callableFactory)
    
    
    protected GrpcQuotaServiceStub(QuotaServiceStubSettings settings, ClientContext clientContext, GrpcStubCallableFactory callableFactory)

Constructs an instance of GrpcQuotaServiceStub, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameters**  
---  
**Name** | **Description**  
`settings` | `[QuotaServiceStubSettings](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-quota/latest/com.google.shopping.merchant.quota.v1beta.stub.QuotaServiceStubSettings)`  
  
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

[QuotaServiceStub.close()](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-quota/latest/com.google.shopping.merchant.quota.v1beta.stub.QuotaServiceStub#com_google_shopping_merchant_quota_v1beta_stub_QuotaServiceStub_close__)

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
  
### listQuotaGroupsCallable()
    
    
    public UnaryCallable<ListQuotaGroupsRequest,ListQuotaGroupsResponse> listQuotaGroupsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListQuotaGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-quota/latest/com.google.shopping.merchant.quota.v1beta.ListQuotaGroupsRequest),[ListQuotaGroupsResponse](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-quota/latest/com.google.shopping.merchant.quota.v1beta.ListQuotaGroupsResponse)>` |   
**Overrides**

[QuotaServiceStub.listQuotaGroupsCallable()](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-quota/latest/com.google.shopping.merchant.quota.v1beta.stub.QuotaServiceStub#com_google_shopping_merchant_quota_v1beta_stub_QuotaServiceStub_listQuotaGroupsCallable__)

### listQuotaGroupsPagedCallable()
    
    
    public UnaryCallable<ListQuotaGroupsRequest,QuotaServiceClient.ListQuotaGroupsPagedResponse> listQuotaGroupsPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListQuotaGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-quota/latest/com.google.shopping.merchant.quota.v1beta.ListQuotaGroupsRequest),[ListQuotaGroupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-quota/latest/com.google.shopping.merchant.quota.v1beta.QuotaServiceClient.ListQuotaGroupsPagedResponse)>` |   
**Overrides**

[QuotaServiceStub.listQuotaGroupsPagedCallable()](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-quota/latest/com.google.shopping.merchant.quota.v1beta.stub.QuotaServiceStub#com_google_shopping_merchant_quota_v1beta_stub_QuotaServiceStub_listQuotaGroupsPagedCallable__)

### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
