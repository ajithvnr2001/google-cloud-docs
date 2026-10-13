---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementGrpc.GDCHardwareManagementStub
title: Class GDCHardwareManagementGrpc.GDCHardwareManagementStub (0.54.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:26:36.220340+00:00
---

# Class GDCHardwareManagementGrpc.GDCHardwareManagementStub (0.54.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementGrpc.GDCHardwareManagementStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class GDCHardwareManagementGrpc.GDCHardwareManagementStub (0.54.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.54.0 (latest)  0.50.0  0.49.0  0.48.0  0.46.0  0.43.0  0.42.0  0.40.0  0.38.0  0.37.0  0.36.0  0.35.0  0.33.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.25.0  0.23.0  0.22.0  0.19.0  0.18.0  0.17.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static final class GDCHardwareManagementGrpc.GDCHardwareManagementStub extends AbstractAsyncStub<GDCHardwareManagementGrpc.GDCHardwareManagementStub>

A stub to allow clients to do asynchronous rpc calls to service GDCHardwareManagement.

The GDC Hardware Management service.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractAsyncStub > GDCHardwareManagementGrpc.GDCHardwareManagementStub

## Inherited Members

io.grpc.stub.AbstractAsyncStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractAsyncStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.<T>withOption(io.grpc.CallOptions.Key<T>,T)

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.getCallOptions()

io.grpc.stub.AbstractStub.getChannel()

io.grpc.stub.AbstractStub.withCallCredentials(io.grpc.CallCredentials)

io.grpc.stub.AbstractStub.withChannel(io.grpc.Channel)

io.grpc.stub.AbstractStub.withCompression(java.lang.String)

io.grpc.stub.AbstractStub.withDeadline(io.grpc.Deadline)

io.grpc.stub.AbstractStub.withDeadlineAfter(java.time.Duration)

io.grpc.stub.AbstractStub.withDeadlineAfter(long,java.util.concurrent.TimeUnit)

io.grpc.stub.AbstractStub.withExecutor(java.util.concurrent.Executor)

io.grpc.stub.AbstractStub.withInterceptors(io.grpc.ClientInterceptor...)

io.grpc.stub.AbstractStub.withMaxInboundMessageSize(int)

io.grpc.stub.AbstractStub.withMaxOutboundMessageSize(int)

io.grpc.stub.AbstractStub.withOnReadyThreshold(int)

io.grpc.stub.AbstractStub.withWaitForReady()

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

## Methods 

### build(Channel channel, CallOptions callOptions)
    
    
    protected GDCHardwareManagementGrpc.GDCHardwareManagementStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[GDCHardwareManagementGrpc.GDCHardwareManagementStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementGrpc.GDCHardwareManagementStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### cancelOrder(CancelOrderRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void cancelOrder(CancelOrderRequest request, StreamObserver<Operation> responseObserver)

Cancels an order.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CancelOrderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CancelOrderRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createComment(CreateCommentRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createComment(CreateCommentRequest request, StreamObserver<Operation> responseObserver)

Creates a new comment on an order.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateCommentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CreateCommentRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createHardware(CreateHardwareRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createHardware(CreateHardwareRequest request, StreamObserver<Operation> responseObserver)

Creates new hardware in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateHardwareRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CreateHardwareRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createHardwareGroup(CreateHardwareGroupRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createHardwareGroup(CreateHardwareGroupRequest request, StreamObserver<Operation> responseObserver)

Creates a new hardware group in a given order.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateHardwareGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CreateHardwareGroupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createOrder(CreateOrderRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createOrder(CreateOrderRequest request, StreamObserver<Operation> responseObserver)

Creates a new order in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateOrderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CreateOrderRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createSite(CreateSiteRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createSite(CreateSiteRequest request, StreamObserver<Operation> responseObserver)

Creates a new site in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateSiteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CreateSiteRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createZone(CreateZoneRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createZone(CreateZoneRequest request, StreamObserver<Operation> responseObserver)

Creates a new zone in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateZoneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CreateZoneRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteHardware(DeleteHardwareRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteHardware(DeleteHardwareRequest request, StreamObserver<Operation> responseObserver)

Deletes hardware.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteHardwareRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.DeleteHardwareRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteHardwareGroup(DeleteHardwareGroupRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteHardwareGroup(DeleteHardwareGroupRequest request, StreamObserver<Operation> responseObserver)

Deletes a hardware group.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteHardwareGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.DeleteHardwareGroupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteOrder(DeleteOrderRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteOrder(DeleteOrderRequest request, StreamObserver<Operation> responseObserver)

Deletes an order.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteOrderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.DeleteOrderRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteSite(DeleteSiteRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteSite(DeleteSiteRequest request, StreamObserver<Operation> responseObserver)

Deletes a site.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteSiteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.DeleteSiteRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteZone(DeleteZoneRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteZone(DeleteZoneRequest request, StreamObserver<Operation> responseObserver)

Deletes a zone.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteZoneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.DeleteZoneRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### getChangeLogEntry(GetChangeLogEntryRequest request, StreamObserver<ChangeLogEntry> responseObserver)
    
    
    public void getChangeLogEntry(GetChangeLogEntryRequest request, StreamObserver<ChangeLogEntry> responseObserver)

Gets details of a change to an order.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetChangeLogEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GetChangeLogEntryRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ChangeLogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ChangeLogEntry)>`  
  
  
### getComment(GetCommentRequest request, StreamObserver<Comment> responseObserver)
    
    
    public void getComment(GetCommentRequest request, StreamObserver<Comment> responseObserver)

Gets the content of a comment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCommentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GetCommentRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Comment](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Comment)>`  
  
  
### getHardware(GetHardwareRequest request, StreamObserver<Hardware> responseObserver)
    
    
    public void getHardware(GetHardwareRequest request, StreamObserver<Hardware> responseObserver)

Gets hardware details.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetHardwareRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GetHardwareRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Hardware](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Hardware)>`  
  
  
### getHardwareGroup(GetHardwareGroupRequest request, StreamObserver<HardwareGroup> responseObserver)
    
    
    public void getHardwareGroup(GetHardwareGroupRequest request, StreamObserver<HardwareGroup> responseObserver)

Gets details of a hardware group.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetHardwareGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GetHardwareGroupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[HardwareGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.HardwareGroup)>`  
  
  
### getOrder(GetOrderRequest request, StreamObserver<Order> responseObserver)
    
    
    public void getOrder(GetOrderRequest request, StreamObserver<Order> responseObserver)

Gets details of an order.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetOrderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GetOrderRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Order](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Order)>`  
  
  
### getSite(GetSiteRequest request, StreamObserver<Site> responseObserver)
    
    
    public void getSite(GetSiteRequest request, StreamObserver<Site> responseObserver)

Gets details of a site.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSiteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GetSiteRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Site](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Site)>`  
  
  
### getSku(GetSkuRequest request, StreamObserver<Sku> responseObserver)
    
    
    public void getSku(GetSkuRequest request, StreamObserver<Sku> responseObserver)

Gets details of an SKU.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSkuRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GetSkuRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Sku](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Sku)>`  
  
  
### getZone(GetZoneRequest request, StreamObserver<Zone> responseObserver)
    
    
    public void getZone(GetZoneRequest request, StreamObserver<Zone> responseObserver)

Gets details of a zone.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetZoneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GetZoneRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Zone](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Zone)>`  
  
  
### listChangeLogEntries(ListChangeLogEntriesRequest request, StreamObserver<ListChangeLogEntriesResponse> responseObserver)
    
    
    public void listChangeLogEntries(ListChangeLogEntriesRequest request, StreamObserver<ListChangeLogEntriesResponse> responseObserver)

Lists the changes made to an order.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListChangeLogEntriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListChangeLogEntriesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListChangeLogEntriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListChangeLogEntriesResponse)>`  
  
  
### listComments(ListCommentsRequest request, StreamObserver<ListCommentsResponse> responseObserver)
    
    
    public void listComments(ListCommentsRequest request, StreamObserver<ListCommentsResponse> responseObserver)

Lists the comments on an order.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListCommentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListCommentsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListCommentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListCommentsResponse)>`  
  
  
### listHardware(ListHardwareRequest request, StreamObserver<ListHardwareResponse> responseObserver)
    
    
    public void listHardware(ListHardwareRequest request, StreamObserver<ListHardwareResponse> responseObserver)

Lists hardware in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListHardwareRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListHardwareRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListHardwareResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListHardwareResponse)>`  
  
  
### listHardwareGroups(ListHardwareGroupsRequest request, StreamObserver<ListHardwareGroupsResponse> responseObserver)
    
    
    public void listHardwareGroups(ListHardwareGroupsRequest request, StreamObserver<ListHardwareGroupsResponse> responseObserver)

Lists hardware groups in a given order.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListHardwareGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListHardwareGroupsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListHardwareGroupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListHardwareGroupsResponse)>`  
  
  
### listOrders(ListOrdersRequest request, StreamObserver<ListOrdersResponse> responseObserver)
    
    
    public void listOrders(ListOrdersRequest request, StreamObserver<ListOrdersResponse> responseObserver)

Lists orders in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListOrdersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListOrdersRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListOrdersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListOrdersResponse)>`  
  
  
### listSites(ListSitesRequest request, StreamObserver<ListSitesResponse> responseObserver)
    
    
    public void listSites(ListSitesRequest request, StreamObserver<ListSitesResponse> responseObserver)

Lists sites in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSitesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListSitesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListSitesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListSitesResponse)>`  
  
  
### listSkus(ListSkusRequest request, StreamObserver<ListSkusResponse> responseObserver)
    
    
    public void listSkus(ListSkusRequest request, StreamObserver<ListSkusResponse> responseObserver)

Lists SKUs for a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSkusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListSkusRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListSkusResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListSkusResponse)>`  
  
  
### listZones(ListZonesRequest request, StreamObserver<ListZonesResponse> responseObserver)
    
    
    public void listZones(ListZonesRequest request, StreamObserver<ListZonesResponse> responseObserver)

Lists zones in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListZonesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListZonesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListZonesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListZonesResponse)>`  
  
  
### recordActionOnComment(RecordActionOnCommentRequest request, StreamObserver<Comment> responseObserver)
    
    
    public void recordActionOnComment(RecordActionOnCommentRequest request, StreamObserver<Comment> responseObserver)

Record Action on a Comment. If the Action specified in the request is READ, the viewed time in the comment is set to the time the request was received. If the comment is already marked as read, subsequent calls will be ignored. If the Action is UNREAD, the viewed time is cleared from the comment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RecordActionOnCommentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.RecordActionOnCommentRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Comment](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Comment)>`  
  
  
### requestOrderDateChange(RequestOrderDateChangeRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void requestOrderDateChange(RequestOrderDateChangeRequest request, StreamObserver<Operation> responseObserver)

Updates the requested date change of a single Order.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RequestOrderDateChangeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.RequestOrderDateChangeRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### signalZoneState(SignalZoneStateRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void signalZoneState(SignalZoneStateRequest request, StreamObserver<Operation> responseObserver)

Signals the state of a zone.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SignalZoneStateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.SignalZoneStateRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### submitOrder(SubmitOrderRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void submitOrder(SubmitOrderRequest request, StreamObserver<Operation> responseObserver)

Submits an order.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SubmitOrderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.SubmitOrderRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateHardware(UpdateHardwareRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateHardware(UpdateHardwareRequest request, StreamObserver<Operation> responseObserver)

Updates hardware parameters.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateHardwareRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.UpdateHardwareRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateHardwareGroup(UpdateHardwareGroupRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateHardwareGroup(UpdateHardwareGroupRequest request, StreamObserver<Operation> responseObserver)

Updates the parameters of a hardware group.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateHardwareGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.UpdateHardwareGroupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateOrder(UpdateOrderRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateOrder(UpdateOrderRequest request, StreamObserver<Operation> responseObserver)

Updates the parameters of an order.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateOrderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.UpdateOrderRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateSite(UpdateSiteRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateSite(UpdateSiteRequest request, StreamObserver<Operation> responseObserver)

Updates the parameters of a site.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSiteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.UpdateSiteRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateZone(UpdateZoneRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateZone(UpdateZoneRequest request, StreamObserver<Operation> responseObserver)

Updates the parameters of a zone.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateZoneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.UpdateZoneRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
