---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkGrpc.EdgeNetworkBlockingV2Stub
title: Class EdgeNetworkGrpc.EdgeNetworkBlockingV2Stub (0.67.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:29:39.320069+00:00
---

# Class EdgeNetworkGrpc.EdgeNetworkBlockingV2Stub (0.67.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkGrpc.EdgeNetworkBlockingV2Stub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class EdgeNetworkGrpc.EdgeNetworkBlockingV2Stub (0.67.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.67.0 (latest)  0.63.0  0.62.0  0.61.0  0.59.0  0.56.0  0.55.0  0.53.0  0.51.0  0.50.0  0.49.0  0.48.0  0.46.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.38.0  0.36.0  0.35.0  0.32.0  0.31.0  0.30.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static final class EdgeNetworkGrpc.EdgeNetworkBlockingV2Stub extends AbstractBlockingStub<EdgeNetworkGrpc.EdgeNetworkBlockingV2Stub>

A stub to allow clients to do synchronous rpc calls to service EdgeNetwork.

EdgeNetwork API provides managed, highly available cloud dynamic network configuration service to the GEC customer to enable edge application and network function solutions. This allows the customers to easily define and configure the network setup and property to meet the workload requirement.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > EdgeNetworkGrpc.EdgeNetworkBlockingV2Stub

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
    
    
    protected EdgeNetworkGrpc.EdgeNetworkBlockingV2Stub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[EdgeNetworkGrpc.EdgeNetworkBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkGrpc.EdgeNetworkBlockingV2Stub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createInterconnectAttachment(CreateInterconnectAttachmentRequest request)
    
    
    public Operation createInterconnectAttachment(CreateInterconnectAttachmentRequest request)

Creates a new InterconnectAttachment in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateInterconnectAttachmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.CreateInterconnectAttachmentRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createNetwork(CreateNetworkRequest request)
    
    
    public Operation createNetwork(CreateNetworkRequest request)

Creates a new Network in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.CreateNetworkRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createRouter(CreateRouterRequest request)
    
    
    public Operation createRouter(CreateRouterRequest request)

Creates a new Router in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.CreateRouterRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createSubnet(CreateSubnetRequest request)
    
    
    public Operation createSubnet(CreateSubnetRequest request)

Creates a new Subnet in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateSubnetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.CreateSubnetRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteInterconnectAttachment(DeleteInterconnectAttachmentRequest request)
    
    
    public Operation deleteInterconnectAttachment(DeleteInterconnectAttachmentRequest request)

Deletes a single InterconnectAttachment.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteInterconnectAttachmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DeleteInterconnectAttachmentRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteNetwork(DeleteNetworkRequest request)
    
    
    public Operation deleteNetwork(DeleteNetworkRequest request)

Deletes a single Network.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DeleteNetworkRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteRouter(DeleteRouterRequest request)
    
    
    public Operation deleteRouter(DeleteRouterRequest request)

Deletes a single Router.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DeleteRouterRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteSubnet(DeleteSubnetRequest request)
    
    
    public Operation deleteSubnet(DeleteSubnetRequest request)

Deletes a single Subnet.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteSubnetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DeleteSubnetRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### diagnoseInterconnect(DiagnoseInterconnectRequest request)
    
    
    public DiagnoseInterconnectResponse diagnoseInterconnect(DiagnoseInterconnectRequest request)

Get the diagnostics of a single interconnect resource.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DiagnoseInterconnectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DiagnoseInterconnectRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiagnoseInterconnectResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DiagnoseInterconnectResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### diagnoseNetwork(DiagnoseNetworkRequest request)
    
    
    public DiagnoseNetworkResponse diagnoseNetwork(DiagnoseNetworkRequest request)

Get the diagnostics of a single network resource.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DiagnoseNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DiagnoseNetworkRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiagnoseNetworkResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DiagnoseNetworkResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### diagnoseRouter(DiagnoseRouterRequest request)
    
    
    public DiagnoseRouterResponse diagnoseRouter(DiagnoseRouterRequest request)

Get the diagnostics of a single router resource.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DiagnoseRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DiagnoseRouterRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiagnoseRouterResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DiagnoseRouterResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getInterconnect(GetInterconnectRequest request)
    
    
    public Interconnect getInterconnect(GetInterconnectRequest request)

Gets details of a single Interconnect.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetInterconnectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.GetInterconnectRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Interconnect](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Interconnect)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getInterconnectAttachment(GetInterconnectAttachmentRequest request)
    
    
    public InterconnectAttachment getInterconnectAttachment(GetInterconnectAttachmentRequest request)

Gets details of a single InterconnectAttachment.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetInterconnectAttachmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.GetInterconnectAttachmentRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InterconnectAttachment](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.InterconnectAttachment)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getNetwork(GetNetworkRequest request)
    
    
    public Network getNetwork(GetNetworkRequest request)

Gets details of a single Network.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.GetNetworkRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Network](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Network)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getRouter(GetRouterRequest request)
    
    
    public Router getRouter(GetRouterRequest request)

Gets details of a single Router.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.GetRouterRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Router](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Router)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getSubnet(GetSubnetRequest request)
    
    
    public Subnet getSubnet(GetSubnetRequest request)

Gets details of a single Subnet.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSubnetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.GetSubnetRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Subnet](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Subnet)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getZone(GetZoneRequest request) (deprecated)
    
    
    public Zone getZone(GetZoneRequest request)

Deprecated: not implemented. Gets details of a single Zone.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetZoneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.GetZoneRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Zone](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Zone)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### initializeZone(InitializeZoneRequest request)
    
    
    public InitializeZoneResponse initializeZone(InitializeZoneRequest request)

InitializeZone will initialize resources for a zone in a project.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InitializeZoneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.InitializeZoneRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InitializeZoneResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.InitializeZoneResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listInterconnectAttachments(ListInterconnectAttachmentsRequest request)
    
    
    public ListInterconnectAttachmentsResponse listInterconnectAttachments(ListInterconnectAttachmentsRequest request)

Lists InterconnectAttachments in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListInterconnectAttachmentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListInterconnectAttachmentsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListInterconnectAttachmentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListInterconnectAttachmentsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listInterconnects(ListInterconnectsRequest request)
    
    
    public ListInterconnectsResponse listInterconnects(ListInterconnectsRequest request)

Lists Interconnects in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListInterconnectsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListInterconnectsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListInterconnectsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListInterconnectsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listNetworks(ListNetworksRequest request)
    
    
    public ListNetworksResponse listNetworks(ListNetworksRequest request)

Lists Networks in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListNetworksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListNetworksRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListNetworksResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListNetworksResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listRouters(ListRoutersRequest request)
    
    
    public ListRoutersResponse listRouters(ListRoutersRequest request)

Lists Routers in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListRoutersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListRoutersRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListRoutersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListRoutersResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listSubnets(ListSubnetsRequest request)
    
    
    public ListSubnetsResponse listSubnets(ListSubnetsRequest request)

Lists Subnets in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListSubnetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListSubnetsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListSubnetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListSubnetsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listZones(ListZonesRequest request) (deprecated)
    
    
    public ListZonesResponse listZones(ListZonesRequest request)

Deprecated: not implemented. Lists Zones in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListZonesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListZonesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListZonesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListZonesResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateRouter(UpdateRouterRequest request)
    
    
    public Operation updateRouter(UpdateRouterRequest request)

Updates the parameters of a single Router.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.UpdateRouterRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateSubnet(UpdateSubnetRequest request)
    
    
    public Operation updateSubnet(UpdateSubnetRequest request)

Updates the parameters of a single Subnet.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateSubnetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.UpdateSubnetRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
