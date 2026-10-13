---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2beta.CatalogServiceGrpc
title: Class CatalogServiceGrpc (2.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:32:29.582030+00:00
---

# Class CatalogServiceGrpc (2.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2beta.CatalogServiceGrpc

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CatalogServiceGrpc (2.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.101.0 (latest)  2.97.0  2.96.0  2.95.0  2.93.0  2.90.0  2.89.0  2.87.0  2.85.0  2.84.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.74.0  2.72.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.1  2.4.0  2.3.0  2.2.3  2.1.0  2.0.19 
    
    
    public final class CatalogServiceGrpc

Service for managing catalog configuration.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > CatalogServiceGrpc

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

### bindService(CatalogServiceGrpc.AsyncService service)
    
    
    public static final ServerServiceDefinition bindService(CatalogServiceGrpc.AsyncService service)

**Parameter**  
---  
**Name** | **Description**  
`service` | `[CatalogServiceGrpc.AsyncService](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2beta.CatalogServiceGrpc.AsyncService)`  
  
**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServerServiceDefinition` |   
  
### getAddCatalogAttributeMethod()
    
    
    public static MethodDescriptor<AddCatalogAttributeRequest,AttributesConfig> getAddCatalogAttributeMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[AddCatalogAttributeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2beta.AddCatalogAttributeRequest),[AttributesConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2beta.AttributesConfig)>` |   
  
### getBatchRemoveCatalogAttributesMethod()
    
    
    public static MethodDescriptor<BatchRemoveCatalogAttributesRequest,BatchRemoveCatalogAttributesResponse> getBatchRemoveCatalogAttributesMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[BatchRemoveCatalogAttributesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2beta.BatchRemoveCatalogAttributesRequest),[BatchRemoveCatalogAttributesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2beta.BatchRemoveCatalogAttributesResponse)>` |   
  
### getGetAttributesConfigMethod()
    
    
    public static MethodDescriptor<GetAttributesConfigRequest,AttributesConfig> getGetAttributesConfigMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetAttributesConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2beta.GetAttributesConfigRequest),[AttributesConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2beta.AttributesConfig)>` |   
  
### getGetCompletionConfigMethod()
    
    
    public static MethodDescriptor<GetCompletionConfigRequest,CompletionConfig> getGetCompletionConfigMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetCompletionConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2beta.GetCompletionConfigRequest),[CompletionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2beta.CompletionConfig)>` |   
  
### getGetDefaultBranchMethod()
    
    
    public static MethodDescriptor<GetDefaultBranchRequest,GetDefaultBranchResponse> getGetDefaultBranchMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetDefaultBranchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2beta.GetDefaultBranchRequest),[GetDefaultBranchResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2beta.GetDefaultBranchResponse)>` |   
  
### getListCatalogsMethod()
    
    
    public static MethodDescriptor<ListCatalogsRequest,ListCatalogsResponse> getListCatalogsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListCatalogsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2beta.ListCatalogsRequest),[ListCatalogsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2beta.ListCatalogsResponse)>` |   
  
### getRemoveCatalogAttributeMethod()
    
    
    public static MethodDescriptor<RemoveCatalogAttributeRequest,AttributesConfig> getRemoveCatalogAttributeMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[RemoveCatalogAttributeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2beta.RemoveCatalogAttributeRequest),[AttributesConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2beta.AttributesConfig)>` |   
  
### getReplaceCatalogAttributeMethod()
    
    
    public static MethodDescriptor<ReplaceCatalogAttributeRequest,AttributesConfig> getReplaceCatalogAttributeMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ReplaceCatalogAttributeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2beta.ReplaceCatalogAttributeRequest),[AttributesConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2beta.AttributesConfig)>` |   
  
### getServiceDescriptor()
    
    
    public static ServiceDescriptor getServiceDescriptor()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServiceDescriptor` |   
  
### getSetDefaultBranchMethod()
    
    
    public static MethodDescriptor<SetDefaultBranchRequest,Empty> getSetDefaultBranchMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[SetDefaultBranchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2beta.SetDefaultBranchRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getUpdateAttributesConfigMethod()
    
    
    public static MethodDescriptor<UpdateAttributesConfigRequest,AttributesConfig> getUpdateAttributesConfigMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateAttributesConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2beta.UpdateAttributesConfigRequest),[AttributesConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2beta.AttributesConfig)>` |   
  
### getUpdateCatalogMethod()
    
    
    public static MethodDescriptor<UpdateCatalogRequest,Catalog> getUpdateCatalogMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateCatalogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2beta.UpdateCatalogRequest),[Catalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2beta.Catalog)>` |   
  
### getUpdateCompletionConfigMethod()
    
    
    public static MethodDescriptor<UpdateCompletionConfigRequest,CompletionConfig> getUpdateCompletionConfigMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateCompletionConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2beta.UpdateCompletionConfigRequest),[CompletionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2beta.CompletionConfig)>` |   
  
### newBlockingStub(Channel channel)
    
    
    public static CatalogServiceGrpc.CatalogServiceBlockingStub newBlockingStub(Channel channel)

Creates a new blocking-style stub that supports unary and streaming output calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[CatalogServiceGrpc.CatalogServiceBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2beta.CatalogServiceGrpc.CatalogServiceBlockingStub)` |   
  
### newBlockingV2Stub(Channel channel)
    
    
    public static CatalogServiceGrpc.CatalogServiceBlockingV2Stub newBlockingV2Stub(Channel channel)

Creates a new blocking-style stub that supports all types of calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[CatalogServiceGrpc.CatalogServiceBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2beta.CatalogServiceGrpc.CatalogServiceBlockingV2Stub)` |   
  
### newFutureStub(Channel channel)
    
    
    public static CatalogServiceGrpc.CatalogServiceFutureStub newFutureStub(Channel channel)

Creates a new ListenableFuture-style stub that supports unary calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[CatalogServiceGrpc.CatalogServiceFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2beta.CatalogServiceGrpc.CatalogServiceFutureStub)` |   
  
### newStub(Channel channel)
    
    
    public static CatalogServiceGrpc.CatalogServiceStub newStub(Channel channel)

Creates a new async stub that supports all call types for the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[CatalogServiceGrpc.CatalogServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2beta.CatalogServiceGrpc.CatalogServiceStub)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
