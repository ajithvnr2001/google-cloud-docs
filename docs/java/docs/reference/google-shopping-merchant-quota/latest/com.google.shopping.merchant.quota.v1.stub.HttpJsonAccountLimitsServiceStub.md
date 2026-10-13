---
url: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-quota/latest/com.google.shopping.merchant.quota.v1.stub.HttpJsonAccountLimitsServiceStub
title: Class HttpJsonAccountLimitsServiceStub (1.27.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:34:13.588006+00:00
---

# Class HttpJsonAccountLimitsServiceStub (1.27.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-quota/latest/com.google.shopping.merchant.quota.v1.stub.HttpJsonAccountLimitsServiceStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class HttpJsonAccountLimitsServiceStub (1.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.27.0 (latest)  1.23.0  1.22.0  1.21.0  1.19.0  1.16.0  1.15.0  1.13.0  1.11.0  1.10.0  1.8.0  1.6.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.33.0  0.31.0  0.30.0  0.27.0  0.26.0  0.25.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0 
    
    
    public class HttpJsonAccountLimitsServiceStub extends AccountLimitsServiceStub

REST stub implementation for the AccountLimitsService service API.

This class is for advanced usage and reflects the underlying API directly.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AccountLimitsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-quota/latest/com.google.shopping.merchant.quota.v1.stub.AccountLimitsServiceStub) > HttpJsonAccountLimitsServiceStub

## Inherited Members

[AccountLimitsServiceStub.close()](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-quota/latest/com.google.shopping.merchant.quota.v1.stub.AccountLimitsServiceStub#com_google_shopping_merchant_quota_v1_stub_AccountLimitsServiceStub_close__)

[AccountLimitsServiceStub.getAccountLimitCallable()](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-quota/latest/com.google.shopping.merchant.quota.v1.stub.AccountLimitsServiceStub#com_google_shopping_merchant_quota_v1_stub_AccountLimitsServiceStub_getAccountLimitCallable__)

[AccountLimitsServiceStub.listAccountLimitsCallable()](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-quota/latest/com.google.shopping.merchant.quota.v1.stub.AccountLimitsServiceStub#com_google_shopping_merchant_quota_v1_stub_AccountLimitsServiceStub_listAccountLimitsCallable__)

[AccountLimitsServiceStub.listAccountLimitsPagedCallable()](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-quota/latest/com.google.shopping.merchant.quota.v1.stub.AccountLimitsServiceStub#com_google_shopping_merchant_quota_v1_stub_AccountLimitsServiceStub_listAccountLimitsPagedCallable__)

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
    
    
    public static final HttpJsonAccountLimitsServiceStub create(ClientContext clientContext)

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HttpJsonAccountLimitsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-quota/latest/com.google.shopping.merchant.quota.v1.stub.HttpJsonAccountLimitsServiceStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ClientContext clientContext, HttpJsonStubCallableFactory callableFactory)
    
    
    public static final HttpJsonAccountLimitsServiceStub create(ClientContext clientContext, HttpJsonStubCallableFactory callableFactory)

**Parameters**  
---  
**Name** | **Description**  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.html)`  
  
`callableFactory` | `[HttpJsonStubCallableFactory](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.HttpJsonStubCallableFactory.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HttpJsonAccountLimitsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-quota/latest/com.google.shopping.merchant.quota.v1.stub.HttpJsonAccountLimitsServiceStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(AccountLimitsServiceStubSettings settings)
    
    
    public static final HttpJsonAccountLimitsServiceStub create(AccountLimitsServiceStubSettings settings)

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[AccountLimitsServiceStubSettings](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-quota/latest/com.google.shopping.merchant.quota.v1.stub.AccountLimitsServiceStubSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HttpJsonAccountLimitsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-quota/latest/com.google.shopping.merchant.quota.v1.stub.HttpJsonAccountLimitsServiceStub)` |   
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

### HttpJsonAccountLimitsServiceStub(AccountLimitsServiceStubSettings settings, ClientContext clientContext)
    
    
    protected HttpJsonAccountLimitsServiceStub(AccountLimitsServiceStubSettings settings, ClientContext clientContext)

Constructs an instance of HttpJsonAccountLimitsServiceStub, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameters**  
---  
**Name** | **Description**  
`settings` | `[AccountLimitsServiceStubSettings](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-quota/latest/com.google.shopping.merchant.quota.v1.stub.AccountLimitsServiceStubSettings)`  
  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.html)`  
  
  
### HttpJsonAccountLimitsServiceStub(AccountLimitsServiceStubSettings settings, ClientContext clientContext, HttpJsonStubCallableFactory callableFactory)
    
    
    protected HttpJsonAccountLimitsServiceStub(AccountLimitsServiceStubSettings settings, ClientContext clientContext, HttpJsonStubCallableFactory callableFactory)

Constructs an instance of HttpJsonAccountLimitsServiceStub, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameters**  
---  
**Name** | **Description**  
`settings` | `[AccountLimitsServiceStubSettings](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-quota/latest/com.google.shopping.merchant.quota.v1.stub.AccountLimitsServiceStubSettings)`  
  
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

[AccountLimitsServiceStub.close()](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-quota/latest/com.google.shopping.merchant.quota.v1.stub.AccountLimitsServiceStub#com_google_shopping_merchant_quota_v1_stub_AccountLimitsServiceStub_close__)

### getAccountLimitCallable()
    
    
    public UnaryCallable<GetAccountLimitRequest,AccountLimit> getAccountLimitCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetAccountLimitRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-quota/latest/com.google.shopping.merchant.quota.v1.GetAccountLimitRequest),[AccountLimit](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-quota/latest/com.google.shopping.merchant.quota.v1.AccountLimit)>` |   
**Overrides**

[AccountLimitsServiceStub.getAccountLimitCallable()](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-quota/latest/com.google.shopping.merchant.quota.v1.stub.AccountLimitsServiceStub#com_google_shopping_merchant_quota_v1_stub_AccountLimitsServiceStub_getAccountLimitCallable__)

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
  
### listAccountLimitsCallable()
    
    
    public UnaryCallable<ListAccountLimitsRequest,ListAccountLimitsResponse> listAccountLimitsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAccountLimitsRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-quota/latest/com.google.shopping.merchant.quota.v1.ListAccountLimitsRequest),[ListAccountLimitsResponse](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-quota/latest/com.google.shopping.merchant.quota.v1.ListAccountLimitsResponse)>` |   
**Overrides**

[AccountLimitsServiceStub.listAccountLimitsCallable()](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-quota/latest/com.google.shopping.merchant.quota.v1.stub.AccountLimitsServiceStub#com_google_shopping_merchant_quota_v1_stub_AccountLimitsServiceStub_listAccountLimitsCallable__)

### listAccountLimitsPagedCallable()
    
    
    public UnaryCallable<ListAccountLimitsRequest,AccountLimitsServiceClient.ListAccountLimitsPagedResponse> listAccountLimitsPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAccountLimitsRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-quota/latest/com.google.shopping.merchant.quota.v1.ListAccountLimitsRequest),[ListAccountLimitsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-quota/latest/com.google.shopping.merchant.quota.v1.AccountLimitsServiceClient.ListAccountLimitsPagedResponse)>` |   
**Overrides**

[AccountLimitsServiceStub.listAccountLimitsPagedCallable()](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-quota/latest/com.google.shopping.merchant.quota.v1.stub.AccountLimitsServiceStub#com_google_shopping_merchant_quota_v1_stub_AccountLimitsServiceStub_listAccountLimitsPagedCallable__)

### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
