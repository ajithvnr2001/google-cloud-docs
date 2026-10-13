---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.OrderServiceStub
title: Class OrderServiceStub (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:35:46.261974+00:00
---

# Class OrderServiceStub (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.OrderServiceStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class OrderServiceStub (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public abstract class OrderServiceStub implements BackgroundResource

Base stub class for the OrderService service API.

This class is for advanced usage and reflects the underlying API directly.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > OrderServiceStub

## Implements

[BackgroundResource](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.BackgroundResource.html)

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

## Constructors 

### OrderServiceStub()
    
    
    public OrderServiceStub()

## Methods 

### batchApproveAndOverbookOrdersCallable()
    
    
    public UnaryCallable<BatchApproveAndOverbookOrdersRequest,BatchApproveAndOverbookOrdersResponse> batchApproveAndOverbookOrdersCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchApproveAndOverbookOrdersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchApproveAndOverbookOrdersRequest),[BatchApproveAndOverbookOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchApproveAndOverbookOrdersResponse)>` |   
  
### batchApproveOrdersCallable()
    
    
    public UnaryCallable<BatchApproveOrdersRequest,BatchApproveOrdersResponse> batchApproveOrdersCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchApproveOrdersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchApproveOrdersRequest),[BatchApproveOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchApproveOrdersResponse)>` |   
  
### batchApproveOrdersWithoutReservationCallable()
    
    
    public UnaryCallable<BatchApproveOrdersWithoutReservationRequest,BatchApproveOrdersWithoutReservationResponse> batchApproveOrdersWithoutReservationCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchApproveOrdersWithoutReservationRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchApproveOrdersWithoutReservationRequest),[BatchApproveOrdersWithoutReservationResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchApproveOrdersWithoutReservationResponse)>` |   
  
### batchArchiveOrdersCallable()
    
    
    public UnaryCallable<BatchArchiveOrdersRequest,BatchArchiveOrdersResponse> batchArchiveOrdersCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchArchiveOrdersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchiveOrdersRequest),[BatchArchiveOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchiveOrdersResponse)>` |   
  
### batchCreateOrdersCallable()
    
    
    public UnaryCallable<BatchCreateOrdersRequest,BatchCreateOrdersResponse> batchCreateOrdersCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchCreateOrdersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateOrdersRequest),[BatchCreateOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateOrdersResponse)>` |   
  
### batchDeleteOrdersCallable()
    
    
    public UnaryCallable<BatchDeleteOrdersRequest,BatchDeleteOrdersResponse> batchDeleteOrdersCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchDeleteOrdersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeleteOrdersRequest),[BatchDeleteOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeleteOrdersResponse)>` |   
  
### batchDisapproveOrdersCallable()
    
    
    public UnaryCallable<BatchDisapproveOrdersRequest,BatchDisapproveOrdersResponse> batchDisapproveOrdersCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchDisapproveOrdersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDisapproveOrdersRequest),[BatchDisapproveOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDisapproveOrdersResponse)>` |   
  
### batchDisapproveOrdersWithoutReservationChangesCallable()
    
    
    public UnaryCallable<BatchDisapproveOrdersWithoutReservationChangesRequest,BatchDisapproveOrdersWithoutReservationChangesResponse> batchDisapproveOrdersWithoutReservationChangesCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchDisapproveOrdersWithoutReservationChangesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDisapproveOrdersWithoutReservationChangesRequest),[BatchDisapproveOrdersWithoutReservationChangesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDisapproveOrdersWithoutReservationChangesResponse)>` |   
  
### batchPauseOrdersCallable()
    
    
    public UnaryCallable<BatchPauseOrdersRequest,BatchPauseOrdersResponse> batchPauseOrdersCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchPauseOrdersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchPauseOrdersRequest),[BatchPauseOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchPauseOrdersResponse)>` |   
  
### batchResumeAndOverbookOrdersCallable()
    
    
    public UnaryCallable<BatchResumeAndOverbookOrdersRequest,BatchResumeAndOverbookOrdersResponse> batchResumeAndOverbookOrdersCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchResumeAndOverbookOrdersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchResumeAndOverbookOrdersRequest),[BatchResumeAndOverbookOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchResumeAndOverbookOrdersResponse)>` |   
  
### batchResumeOrdersCallable()
    
    
    public UnaryCallable<BatchResumeOrdersRequest,BatchResumeOrdersResponse> batchResumeOrdersCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchResumeOrdersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchResumeOrdersRequest),[BatchResumeOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchResumeOrdersResponse)>` |   
  
### batchRetractOrdersCallable()
    
    
    public UnaryCallable<BatchRetractOrdersRequest,BatchRetractOrdersResponse> batchRetractOrdersCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchRetractOrdersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchRetractOrdersRequest),[BatchRetractOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchRetractOrdersResponse)>` |   
  
### batchRetractOrdersWithoutReservationChangesCallable()
    
    
    public UnaryCallable<BatchRetractOrdersWithoutReservationChangesRequest,BatchRetractOrdersWithoutReservationChangesResponse> batchRetractOrdersWithoutReservationChangesCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchRetractOrdersWithoutReservationChangesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchRetractOrdersWithoutReservationChangesRequest),[BatchRetractOrdersWithoutReservationChangesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchRetractOrdersWithoutReservationChangesResponse)>` |   
  
### batchSubmitOrdersForApprovalAndOverbookCallable()
    
    
    public UnaryCallable<BatchSubmitOrdersForApprovalAndOverbookRequest,BatchSubmitOrdersForApprovalAndOverbookResponse> batchSubmitOrdersForApprovalAndOverbookCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchSubmitOrdersForApprovalAndOverbookRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchSubmitOrdersForApprovalAndOverbookRequest),[BatchSubmitOrdersForApprovalAndOverbookResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchSubmitOrdersForApprovalAndOverbookResponse)>` |   
  
### batchSubmitOrdersForApprovalCallable()
    
    
    public UnaryCallable<BatchSubmitOrdersForApprovalRequest,BatchSubmitOrdersForApprovalResponse> batchSubmitOrdersForApprovalCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchSubmitOrdersForApprovalRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchSubmitOrdersForApprovalRequest),[BatchSubmitOrdersForApprovalResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchSubmitOrdersForApprovalResponse)>` |   
  
### batchSubmitOrdersForApprovalWithoutReservationChangesCallable()
    
    
    public UnaryCallable<BatchSubmitOrdersForApprovalWithoutReservationChangesRequest,BatchSubmitOrdersForApprovalWithoutReservationChangesResponse> batchSubmitOrdersForApprovalWithoutReservationChangesCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchSubmitOrdersForApprovalWithoutReservationChangesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchSubmitOrdersForApprovalWithoutReservationChangesRequest),[BatchSubmitOrdersForApprovalWithoutReservationChangesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchSubmitOrdersForApprovalWithoutReservationChangesResponse)>` |   
  
### batchUnarchiveOrdersCallable()
    
    
    public UnaryCallable<BatchUnarchiveOrdersRequest,BatchUnarchiveOrdersResponse> batchUnarchiveOrdersCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchUnarchiveOrdersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUnarchiveOrdersRequest),[BatchUnarchiveOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUnarchiveOrdersResponse)>` |   
  
### batchUpdateOrdersCallable()
    
    
    public UnaryCallable<BatchUpdateOrdersRequest,BatchUpdateOrdersResponse> batchUpdateOrdersCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchUpdateOrdersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateOrdersRequest),[BatchUpdateOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateOrdersResponse)>` |   
  
### close()
    
    
    public abstract void close()

### getOrderCallable()
    
    
    public UnaryCallable<GetOrderRequest,Order> getOrderCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetOrderRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetOrderRequest),[Order](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Order)>` |   
  
### listOrdersCallable()
    
    
    public UnaryCallable<ListOrdersRequest,ListOrdersResponse> listOrdersCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListOrdersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListOrdersRequest),[ListOrdersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListOrdersResponse)>` |   
  
### listOrdersPagedCallable()
    
    
    public UnaryCallable<ListOrdersRequest,OrderServiceClient.ListOrdersPagedResponse> listOrdersPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListOrdersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListOrdersRequest),[ListOrdersPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.OrderServiceClient.ListOrdersPagedResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
