---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementGrpc.GDCHardwareManagementBlockingStub
title: Class GDCHardwareManagementGrpc.GDCHardwareManagementBlockingStub (0.54.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:20:23.246081+00:00
---

# Class GDCHardwareManagementGrpc.GDCHardwareManagementBlockingStub (0.54.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementGrpc.GDCHardwareManagementBlockingStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class GDCHardwareManagementGrpc.GDCHardwareManagementBlockingStub (0.54.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.54.0 (latest)  0.50.0  0.49.0  0.48.0  0.46.0  0.43.0  0.42.0  0.40.0  0.38.0  0.37.0  0.36.0  0.35.0  0.33.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.25.0  0.23.0  0.22.0  0.19.0  0.18.0  0.17.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static final class GDCHardwareManagementGrpc.GDCHardwareManagementBlockingStub extends AbstractBlockingStub<GDCHardwareManagementGrpc.GDCHardwareManagementBlockingStub>

A stub to allow clients to do limited synchronous rpc calls to service GDCHardwareManagement.

The GDC Hardware Management service.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > GDCHardwareManagementGrpc.GDCHardwareManagementBlockingStub

## Inherited Members

io.grpc.stub.AbstractBlockingStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractBlockingStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

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
    
    
    protected GDCHardwareManagementGrpc.GDCHardwareManagementBlockingStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[GDCHardwareManagementGrpc.GDCHardwareManagementBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementGrpc.GDCHardwareManagementBlockingStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### cancelOrder(CancelOrderRequest request)
    
    
    public Operation cancelOrder(CancelOrderRequest request)

Cancels an order.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CancelOrderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CancelOrderRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### createComment(CreateCommentRequest request)
    
    
    public Operation createComment(CreateCommentRequest request)

Creates a new comment on an order.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateCommentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CreateCommentRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### createHardware(CreateHardwareRequest request)
    
    
    public Operation createHardware(CreateHardwareRequest request)

Creates new hardware in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateHardwareRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CreateHardwareRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### createHardwareGroup(CreateHardwareGroupRequest request)
    
    
    public Operation createHardwareGroup(CreateHardwareGroupRequest request)

Creates a new hardware group in a given order.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateHardwareGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CreateHardwareGroupRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### createOrder(CreateOrderRequest request)
    
    
    public Operation createOrder(CreateOrderRequest request)

Creates a new order in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateOrderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CreateOrderRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### createSite(CreateSiteRequest request)
    
    
    public Operation createSite(CreateSiteRequest request)

Creates a new site in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateSiteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CreateSiteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### createZone(CreateZoneRequest request)
    
    
    public Operation createZone(CreateZoneRequest request)

Creates a new zone in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateZoneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CreateZoneRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### deleteHardware(DeleteHardwareRequest request)
    
    
    public Operation deleteHardware(DeleteHardwareRequest request)

Deletes hardware.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteHardwareRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.DeleteHardwareRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### deleteHardwareGroup(DeleteHardwareGroupRequest request)
    
    
    public Operation deleteHardwareGroup(DeleteHardwareGroupRequest request)

Deletes a hardware group.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteHardwareGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.DeleteHardwareGroupRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### deleteOrder(DeleteOrderRequest request)
    
    
    public Operation deleteOrder(DeleteOrderRequest request)

Deletes an order.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteOrderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.DeleteOrderRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### deleteSite(DeleteSiteRequest request)
    
    
    public Operation deleteSite(DeleteSiteRequest request)

Deletes a site.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteSiteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.DeleteSiteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### deleteZone(DeleteZoneRequest request)
    
    
    public Operation deleteZone(DeleteZoneRequest request)

Deletes a zone.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteZoneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.DeleteZoneRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### getChangeLogEntry(GetChangeLogEntryRequest request)
    
    
    public ChangeLogEntry getChangeLogEntry(GetChangeLogEntryRequest request)

Gets details of a change to an order.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetChangeLogEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GetChangeLogEntryRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ChangeLogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ChangeLogEntry)` |   
  
### getComment(GetCommentRequest request)
    
    
    public Comment getComment(GetCommentRequest request)

Gets the content of a comment.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetCommentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GetCommentRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Comment](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Comment)` |   
  
### getHardware(GetHardwareRequest request)
    
    
    public Hardware getHardware(GetHardwareRequest request)

Gets hardware details.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetHardwareRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GetHardwareRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Hardware](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Hardware)` |   
  
### getHardwareGroup(GetHardwareGroupRequest request)
    
    
    public HardwareGroup getHardwareGroup(GetHardwareGroupRequest request)

Gets details of a hardware group.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetHardwareGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GetHardwareGroupRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HardwareGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.HardwareGroup)` |   
  
### getOrder(GetOrderRequest request)
    
    
    public Order getOrder(GetOrderRequest request)

Gets details of an order.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetOrderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GetOrderRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Order](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Order)` |   
  
### getSite(GetSiteRequest request)
    
    
    public Site getSite(GetSiteRequest request)

Gets details of a site.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSiteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GetSiteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Site](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Site)` |   
  
### getSku(GetSkuRequest request)
    
    
    public Sku getSku(GetSkuRequest request)

Gets details of an SKU.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSkuRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GetSkuRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Sku](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Sku)` |   
  
### getZone(GetZoneRequest request)
    
    
    public Zone getZone(GetZoneRequest request)

Gets details of a zone.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetZoneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GetZoneRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Zone](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Zone)` |   
  
### listChangeLogEntries(ListChangeLogEntriesRequest request)
    
    
    public ListChangeLogEntriesResponse listChangeLogEntries(ListChangeLogEntriesRequest request)

Lists the changes made to an order.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListChangeLogEntriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListChangeLogEntriesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListChangeLogEntriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListChangeLogEntriesResponse)` |   
  
### listComments(ListCommentsRequest request)
    
    
    public ListCommentsResponse listComments(ListCommentsRequest request)

Lists the comments on an order.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListCommentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListCommentsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListCommentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListCommentsResponse)` |   
  
### listHardware(ListHardwareRequest request)
    
    
    public ListHardwareResponse listHardware(ListHardwareRequest request)

Lists hardware in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListHardwareRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListHardwareRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListHardwareResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListHardwareResponse)` |   
  
### listHardwareGroups(ListHardwareGroupsRequest request)
    
    
    public ListHardwareGroupsResponse listHardwareGroups(ListHardwareGroupsRequest request)

Lists hardware groups in a given order.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListHardwareGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListHardwareGroupsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListHardwareGroupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListHardwareGroupsResponse)` |   
  
### listOrders(ListOrdersRequest request)
    
    
    public ListOrdersResponse listOrders(ListOrdersRequest request)

Lists orders in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListOrdersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListOrdersRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListOrdersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListOrdersResponse)` |   
  
### listSites(ListSitesRequest request)
    
    
    public ListSitesResponse listSites(ListSitesRequest request)

Lists sites in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListSitesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListSitesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListSitesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListSitesResponse)` |   
  
### listSkus(ListSkusRequest request)
    
    
    public ListSkusResponse listSkus(ListSkusRequest request)

Lists SKUs for a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListSkusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListSkusRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListSkusResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListSkusResponse)` |   
  
### listZones(ListZonesRequest request)
    
    
    public ListZonesResponse listZones(ListZonesRequest request)

Lists zones in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListZonesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListZonesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListZonesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListZonesResponse)` |   
  
### recordActionOnComment(RecordActionOnCommentRequest request)
    
    
    public Comment recordActionOnComment(RecordActionOnCommentRequest request)

Record Action on a Comment. If the Action specified in the request is READ, the viewed time in the comment is set to the time the request was received. If the comment is already marked as read, subsequent calls will be ignored. If the Action is UNREAD, the viewed time is cleared from the comment.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RecordActionOnCommentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.RecordActionOnCommentRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Comment](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Comment)` |   
  
### requestOrderDateChange(RequestOrderDateChangeRequest request)
    
    
    public Operation requestOrderDateChange(RequestOrderDateChangeRequest request)

Updates the requested date change of a single Order.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RequestOrderDateChangeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.RequestOrderDateChangeRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### signalZoneState(SignalZoneStateRequest request)
    
    
    public Operation signalZoneState(SignalZoneStateRequest request)

Signals the state of a zone.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SignalZoneStateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.SignalZoneStateRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### submitOrder(SubmitOrderRequest request)
    
    
    public Operation submitOrder(SubmitOrderRequest request)

Submits an order.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SubmitOrderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.SubmitOrderRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### updateHardware(UpdateHardwareRequest request)
    
    
    public Operation updateHardware(UpdateHardwareRequest request)

Updates hardware parameters.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateHardwareRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.UpdateHardwareRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### updateHardwareGroup(UpdateHardwareGroupRequest request)
    
    
    public Operation updateHardwareGroup(UpdateHardwareGroupRequest request)

Updates the parameters of a hardware group.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateHardwareGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.UpdateHardwareGroupRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### updateOrder(UpdateOrderRequest request)
    
    
    public Operation updateOrder(UpdateOrderRequest request)

Updates the parameters of an order.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateOrderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.UpdateOrderRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### updateSite(UpdateSiteRequest request)
    
    
    public Operation updateSite(UpdateSiteRequest request)

Updates the parameters of a site.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateSiteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.UpdateSiteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### updateZone(UpdateZoneRequest request)
    
    
    public Operation updateZone(UpdateZoneRequest request)

Updates the parameters of a zone.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateZoneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.UpdateZoneRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
