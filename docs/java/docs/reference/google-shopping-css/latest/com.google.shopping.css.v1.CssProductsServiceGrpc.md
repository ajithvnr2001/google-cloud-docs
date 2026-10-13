---
url: https://docs.cloud.google.com/java/docs/reference/google-shopping-css/latest/com.google.shopping.css.v1.CssProductsServiceGrpc
title: Class CssProductsServiceGrpc (0.67.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:22:11.257993+00:00
---

# Class CssProductsServiceGrpc (0.67.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-shopping-css/latest/com.google.shopping.css.v1.CssProductsServiceGrpc

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CssProductsServiceGrpc (0.67.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.67.0 (latest)  0.63.0  0.62.0  0.61.0  0.59.0  0.56.0  0.55.0  0.53.0  0.51.0  0.50.0  0.48.0  0.46.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.38.0  0.36.0  0.35.0  0.32.0  0.31.0  0.30.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public final class CssProductsServiceGrpc

Service for doing get and list on Css Products(a.k.a Aggregate Offers internally).

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > CssProductsServiceGrpc

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

## Static Fields 

### SERVICE_NAME
    
    
    public static final String SERVICE_NAME

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
## Static Methods 

### bindService(CssProductsServiceGrpc.AsyncService service)
    
    
    public static final ServerServiceDefinition bindService(CssProductsServiceGrpc.AsyncService service)

**Parameter**  
---  
**Name** | **Description**  
`service` | `[CssProductsServiceGrpc.AsyncService](https://docs.cloud.google.com/java/docs/reference/google-shopping-css/latest/com.google.shopping.css.v1.CssProductsServiceGrpc.AsyncService)`  
  
**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServerServiceDefinition` |   
  
### getGetCssProductMethod()
    
    
    public static MethodDescriptor<GetCssProductRequest,CssProduct> getGetCssProductMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetCssProductRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-css/latest/com.google.shopping.css.v1.GetCssProductRequest),[CssProduct](https://docs.cloud.google.com/java/docs/reference/google-shopping-css/latest/com.google.shopping.css.v1.CssProduct)>` |   
  
### getListCssProductsMethod()
    
    
    public static MethodDescriptor<ListCssProductsRequest,ListCssProductsResponse> getListCssProductsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListCssProductsRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-css/latest/com.google.shopping.css.v1.ListCssProductsRequest),[ListCssProductsResponse](https://docs.cloud.google.com/java/docs/reference/google-shopping-css/latest/com.google.shopping.css.v1.ListCssProductsResponse)>` |   
  
### getServiceDescriptor()
    
    
    public static ServiceDescriptor getServiceDescriptor()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServiceDescriptor` |   
  
### newBlockingStub(Channel channel)
    
    
    public static CssProductsServiceGrpc.CssProductsServiceBlockingStub newBlockingStub(Channel channel)

Creates a new blocking-style stub that supports unary and streaming output calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[CssProductsServiceGrpc.CssProductsServiceBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-shopping-css/latest/com.google.shopping.css.v1.CssProductsServiceGrpc.CssProductsServiceBlockingStub)` |   
  
### newBlockingV2Stub(Channel channel)
    
    
    public static CssProductsServiceGrpc.CssProductsServiceBlockingV2Stub newBlockingV2Stub(Channel channel)

Creates a new blocking-style stub that supports all types of calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[CssProductsServiceGrpc.CssProductsServiceBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-shopping-css/latest/com.google.shopping.css.v1.CssProductsServiceGrpc.CssProductsServiceBlockingV2Stub)` |   
  
### newFutureStub(Channel channel)
    
    
    public static CssProductsServiceGrpc.CssProductsServiceFutureStub newFutureStub(Channel channel)

Creates a new ListenableFuture-style stub that supports unary calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[CssProductsServiceGrpc.CssProductsServiceFutureStub](https://docs.cloud.google.com/java/docs/reference/google-shopping-css/latest/com.google.shopping.css.v1.CssProductsServiceGrpc.CssProductsServiceFutureStub)` |   
  
### newStub(Channel channel)
    
    
    public static CssProductsServiceGrpc.CssProductsServiceStub newStub(Channel channel)

Creates a new async stub that supports all call types for the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[CssProductsServiceGrpc.CssProductsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-shopping-css/latest/com.google.shopping.css.v1.CssProductsServiceGrpc.CssProductsServiceStub)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
