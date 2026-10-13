---
url: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1beta.ProductInputsServiceGrpc
title: Class ProductInputsServiceGrpc (1.27.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:41:49.266566+00:00
---

# Class ProductInputsServiceGrpc (1.27.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1beta.ProductInputsServiceGrpc

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ProductInputsServiceGrpc (1.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.27.0 (latest)  1.23.0  1.22.0  1.21.0  1.19.0  1.16.0  1.15.0  1.13.0  1.11.0  1.10.0  1.8.0  1.6.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.26.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public final class ProductInputsServiceGrpc

Service to use ProductInput resource. This service works for products with online channel only.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ProductInputsServiceGrpc

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

### bindService(ProductInputsServiceGrpc.AsyncService service)
    
    
    public static final ServerServiceDefinition bindService(ProductInputsServiceGrpc.AsyncService service)

**Parameter**  
---  
**Name** | **Description**  
`service` | `[ProductInputsServiceGrpc.AsyncService](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1beta.ProductInputsServiceGrpc.AsyncService)`  
  
**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServerServiceDefinition` |   
  
### getDeleteProductInputMethod()
    
    
    public static MethodDescriptor<DeleteProductInputRequest,Empty> getDeleteProductInputMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteProductInputRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1beta.DeleteProductInputRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getInsertProductInputMethod()
    
    
    public static MethodDescriptor<InsertProductInputRequest,ProductInput> getInsertProductInputMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[InsertProductInputRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1beta.InsertProductInputRequest),[ProductInput](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1beta.ProductInput)>` |   
  
### getServiceDescriptor()
    
    
    public static ServiceDescriptor getServiceDescriptor()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServiceDescriptor` |   
  
### getUpdateProductInputMethod()
    
    
    public static MethodDescriptor<UpdateProductInputRequest,ProductInput> getUpdateProductInputMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateProductInputRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1beta.UpdateProductInputRequest),[ProductInput](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1beta.ProductInput)>` |   
  
### newBlockingStub(Channel channel)
    
    
    public static ProductInputsServiceGrpc.ProductInputsServiceBlockingStub newBlockingStub(Channel channel)

Creates a new blocking-style stub that supports unary and streaming output calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductInputsServiceGrpc.ProductInputsServiceBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1beta.ProductInputsServiceGrpc.ProductInputsServiceBlockingStub)` |   
  
### newBlockingV2Stub(Channel channel)
    
    
    public static ProductInputsServiceGrpc.ProductInputsServiceBlockingV2Stub newBlockingV2Stub(Channel channel)

Creates a new blocking-style stub that supports all types of calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductInputsServiceGrpc.ProductInputsServiceBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1beta.ProductInputsServiceGrpc.ProductInputsServiceBlockingV2Stub)` |   
  
### newFutureStub(Channel channel)
    
    
    public static ProductInputsServiceGrpc.ProductInputsServiceFutureStub newFutureStub(Channel channel)

Creates a new ListenableFuture-style stub that supports unary calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductInputsServiceGrpc.ProductInputsServiceFutureStub](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1beta.ProductInputsServiceGrpc.ProductInputsServiceFutureStub)` |   
  
### newStub(Channel channel)
    
    
    public static ProductInputsServiceGrpc.ProductInputsServiceStub newStub(Channel channel)

Creates a new async stub that supports all call types for the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductInputsServiceGrpc.ProductInputsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1beta.ProductInputsServiceGrpc.ProductInputsServiceStub)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
