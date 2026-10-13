---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.CommerceTransactionGrpc
title: Class CommerceTransactionGrpc (0.5.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:49:37.390556+00:00
---

# Class CommerceTransactionGrpc (0.5.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.CommerceTransactionGrpc

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CommerceTransactionGrpc (0.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.0 (latest)  0.1.0 
    
    
    public final class CommerceTransactionGrpc

APIs related to managing resources that model commercial transactions.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > CommerceTransactionGrpc

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

### bindService(CommerceTransactionGrpc.AsyncService service)
    
    
    public static final ServerServiceDefinition bindService(CommerceTransactionGrpc.AsyncService service)

**Parameter**  
---  
**Name** | **Description**  
`service` | `[CommerceTransactionGrpc.AsyncService](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.CommerceTransactionGrpc.AsyncService)`  
  
**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServerServiceDefinition` |   
  
### getCancelPrivateOfferMethod()
    
    
    public static MethodDescriptor<CancelPrivateOfferRequest,PrivateOffer> getCancelPrivateOfferMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CancelPrivateOfferRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.CancelPrivateOfferRequest),[PrivateOffer](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.PrivateOffer)>` |   
  
### getCreatePrivateOfferDocumentMethod()
    
    
    public static MethodDescriptor<CreatePrivateOfferDocumentRequest,PrivateOfferDocument> getCreatePrivateOfferDocumentMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreatePrivateOfferDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.CreatePrivateOfferDocumentRequest),[PrivateOfferDocument](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.PrivateOfferDocument)>` |   
  
### getCreatePrivateOfferMethod()
    
    
    public static MethodDescriptor<CreatePrivateOfferRequest,PrivateOffer> getCreatePrivateOfferMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreatePrivateOfferRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.CreatePrivateOfferRequest),[PrivateOffer](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.PrivateOffer)>` |   
  
### getDeletePrivateOfferDocumentMethod()
    
    
    public static MethodDescriptor<DeletePrivateOfferDocumentRequest,Empty> getDeletePrivateOfferDocumentMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeletePrivateOfferDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.DeletePrivateOfferDocumentRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getDeletePrivateOfferMethod()
    
    
    public static MethodDescriptor<DeletePrivateOfferRequest,Empty> getDeletePrivateOfferMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeletePrivateOfferRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.DeletePrivateOfferRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getGetPrivateOfferDocumentMethod()
    
    
    public static MethodDescriptor<GetPrivateOfferDocumentRequest,PrivateOfferDocument> getGetPrivateOfferDocumentMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetPrivateOfferDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.GetPrivateOfferDocumentRequest),[PrivateOfferDocument](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.PrivateOfferDocument)>` |   
  
### getGetPrivateOfferMethod()
    
    
    public static MethodDescriptor<GetPrivateOfferRequest,PrivateOffer> getGetPrivateOfferMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetPrivateOfferRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.GetPrivateOfferRequest),[PrivateOffer](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.PrivateOffer)>` |   
  
### getGetServiceMethod()
    
    
    public static MethodDescriptor<GetServiceRequest,Service> getGetServiceMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.GetServiceRequest),[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.Service)>` |   
  
### getGetSkuGroupMethod()
    
    
    public static MethodDescriptor<GetSkuGroupRequest,SkuGroup> getGetSkuGroupMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetSkuGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.GetSkuGroupRequest),[SkuGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.SkuGroup)>` |   
  
### getGetSkuMethod()
    
    
    public static MethodDescriptor<GetSkuRequest,Sku> getGetSkuMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetSkuRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.GetSkuRequest),[Sku](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.Sku)>` |   
  
### getGetStandardOfferMethod()
    
    
    public static MethodDescriptor<GetStandardOfferRequest,StandardOffer> getGetStandardOfferMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetStandardOfferRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.GetStandardOfferRequest),[StandardOffer](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.StandardOffer)>` |   
  
### getListPrivateOfferDocumentsMethod()
    
    
    public static MethodDescriptor<ListPrivateOfferDocumentsRequest,ListPrivateOfferDocumentsResponse> getListPrivateOfferDocumentsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListPrivateOfferDocumentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.ListPrivateOfferDocumentsRequest),[ListPrivateOfferDocumentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.ListPrivateOfferDocumentsResponse)>` |   
  
### getListPrivateOffersMethod()
    
    
    public static MethodDescriptor<ListPrivateOffersRequest,ListPrivateOffersResponse> getListPrivateOffersMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListPrivateOffersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.ListPrivateOffersRequest),[ListPrivateOffersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.ListPrivateOffersResponse)>` |   
  
### getListServicesMethod()
    
    
    public static MethodDescriptor<ListServicesRequest,ListServicesResponse> getListServicesMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListServicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.ListServicesRequest),[ListServicesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.ListServicesResponse)>` |   
  
### getListSkuGroupsMethod()
    
    
    public static MethodDescriptor<ListSkuGroupsRequest,ListSkuGroupsResponse> getListSkuGroupsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListSkuGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.ListSkuGroupsRequest),[ListSkuGroupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.ListSkuGroupsResponse)>` |   
  
### getListSkusMethod()
    
    
    public static MethodDescriptor<ListSkusRequest,ListSkusResponse> getListSkusMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListSkusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.ListSkusRequest),[ListSkusResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.ListSkusResponse)>` |   
  
### getListStandardOffersMethod()
    
    
    public static MethodDescriptor<ListStandardOffersRequest,ListStandardOffersResponse> getListStandardOffersMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListStandardOffersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.ListStandardOffersRequest),[ListStandardOffersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.ListStandardOffersResponse)>` |   
  
### getPublishPrivateOfferMethod()
    
    
    public static MethodDescriptor<PublishPrivateOfferRequest,PrivateOffer> getPublishPrivateOfferMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[PublishPrivateOfferRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.PublishPrivateOfferRequest),[PrivateOffer](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.PrivateOffer)>` |   
  
### getResolveAmendmentTargetMethod()
    
    
    public static MethodDescriptor<ResolveAmendmentTargetRequest,ResolveAmendmentTargetResponse> getResolveAmendmentTargetMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ResolveAmendmentTargetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.ResolveAmendmentTargetRequest),[ResolveAmendmentTargetResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.ResolveAmendmentTargetResponse)>` |   
  
### getServiceDescriptor()
    
    
    public static ServiceDescriptor getServiceDescriptor()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServiceDescriptor` |   
  
### getUpdatePrivateOfferDocumentMethod()
    
    
    public static MethodDescriptor<UpdatePrivateOfferDocumentRequest,PrivateOfferDocument> getUpdatePrivateOfferDocumentMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdatePrivateOfferDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.UpdatePrivateOfferDocumentRequest),[PrivateOfferDocument](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.PrivateOfferDocument)>` |   
  
### getUpdatePrivateOfferMethod()
    
    
    public static MethodDescriptor<UpdatePrivateOfferRequest,PrivateOffer> getUpdatePrivateOfferMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdatePrivateOfferRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.UpdatePrivateOfferRequest),[PrivateOffer](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.PrivateOffer)>` |   
  
### newBlockingStub(Channel channel)
    
    
    public static CommerceTransactionGrpc.CommerceTransactionBlockingStub newBlockingStub(Channel channel)

Creates a new blocking-style stub that supports unary and streaming output calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[CommerceTransactionGrpc.CommerceTransactionBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.CommerceTransactionGrpc.CommerceTransactionBlockingStub)` |   
  
### newBlockingV2Stub(Channel channel)
    
    
    public static CommerceTransactionGrpc.CommerceTransactionBlockingV2Stub newBlockingV2Stub(Channel channel)

Creates a new blocking-style stub that supports all types of calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[CommerceTransactionGrpc.CommerceTransactionBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.CommerceTransactionGrpc.CommerceTransactionBlockingV2Stub)` |   
  
### newFutureStub(Channel channel)
    
    
    public static CommerceTransactionGrpc.CommerceTransactionFutureStub newFutureStub(Channel channel)

Creates a new ListenableFuture-style stub that supports unary calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[CommerceTransactionGrpc.CommerceTransactionFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.CommerceTransactionGrpc.CommerceTransactionFutureStub)` |   
  
### newStub(Channel channel)
    
    
    public static CommerceTransactionGrpc.CommerceTransactionStub newStub(Channel channel)

Creates a new async stub that supports all call types for the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[CommerceTransactionGrpc.CommerceTransactionStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.CommerceTransactionGrpc.CommerceTransactionStub)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
