---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkGrpc.AsyncService
title: Interface EdgeNetworkGrpc.AsyncService (0.67.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:38:27.601712+00:00
---

# Interface EdgeNetworkGrpc.AsyncService (0.67.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkGrpc.AsyncService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface EdgeNetworkGrpc.AsyncService (0.67.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.67.0 (latest)  0.63.0  0.62.0  0.61.0  0.59.0  0.56.0  0.55.0  0.53.0  0.51.0  0.50.0  0.49.0  0.48.0  0.46.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.38.0  0.36.0  0.35.0  0.32.0  0.31.0  0.30.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static interface EdgeNetworkGrpc.AsyncService

EdgeNetwork API provides managed, highly available cloud dynamic network configuration service to the GEC customer to enable edge application and network function solutions. This allows the customers to easily define and configure the network setup and property to meet the workload requirement.

## Methods 

### createInterconnectAttachment(CreateInterconnectAttachmentRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void createInterconnectAttachment(CreateInterconnectAttachmentRequest request, StreamObserver<Operation> responseObserver)

Creates a new InterconnectAttachment in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateInterconnectAttachmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.CreateInterconnectAttachmentRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createNetwork(CreateNetworkRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void createNetwork(CreateNetworkRequest request, StreamObserver<Operation> responseObserver)

Creates a new Network in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.CreateNetworkRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createRouter(CreateRouterRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void createRouter(CreateRouterRequest request, StreamObserver<Operation> responseObserver)

Creates a new Router in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.CreateRouterRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createSubnet(CreateSubnetRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void createSubnet(CreateSubnetRequest request, StreamObserver<Operation> responseObserver)

Creates a new Subnet in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateSubnetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.CreateSubnetRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteInterconnectAttachment(DeleteInterconnectAttachmentRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void deleteInterconnectAttachment(DeleteInterconnectAttachmentRequest request, StreamObserver<Operation> responseObserver)

Deletes a single InterconnectAttachment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteInterconnectAttachmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DeleteInterconnectAttachmentRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteNetwork(DeleteNetworkRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void deleteNetwork(DeleteNetworkRequest request, StreamObserver<Operation> responseObserver)

Deletes a single Network.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DeleteNetworkRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteRouter(DeleteRouterRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void deleteRouter(DeleteRouterRequest request, StreamObserver<Operation> responseObserver)

Deletes a single Router.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DeleteRouterRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteSubnet(DeleteSubnetRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void deleteSubnet(DeleteSubnetRequest request, StreamObserver<Operation> responseObserver)

Deletes a single Subnet.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteSubnetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DeleteSubnetRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### diagnoseInterconnect(DiagnoseInterconnectRequest request, StreamObserver<DiagnoseInterconnectResponse> responseObserver)
    
    
    public default void diagnoseInterconnect(DiagnoseInterconnectRequest request, StreamObserver<DiagnoseInterconnectResponse> responseObserver)

Get the diagnostics of a single interconnect resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DiagnoseInterconnectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DiagnoseInterconnectRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[DiagnoseInterconnectResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DiagnoseInterconnectResponse)>`  
  
  
### diagnoseNetwork(DiagnoseNetworkRequest request, StreamObserver<DiagnoseNetworkResponse> responseObserver)
    
    
    public default void diagnoseNetwork(DiagnoseNetworkRequest request, StreamObserver<DiagnoseNetworkResponse> responseObserver)

Get the diagnostics of a single network resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DiagnoseNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DiagnoseNetworkRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[DiagnoseNetworkResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DiagnoseNetworkResponse)>`  
  
  
### diagnoseRouter(DiagnoseRouterRequest request, StreamObserver<DiagnoseRouterResponse> responseObserver)
    
    
    public default void diagnoseRouter(DiagnoseRouterRequest request, StreamObserver<DiagnoseRouterResponse> responseObserver)

Get the diagnostics of a single router resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DiagnoseRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DiagnoseRouterRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[DiagnoseRouterResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DiagnoseRouterResponse)>`  
  
  
### getInterconnect(GetInterconnectRequest request, StreamObserver<Interconnect> responseObserver)
    
    
    public default void getInterconnect(GetInterconnectRequest request, StreamObserver<Interconnect> responseObserver)

Gets details of a single Interconnect.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetInterconnectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.GetInterconnectRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Interconnect](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Interconnect)>`  
  
  
### getInterconnectAttachment(GetInterconnectAttachmentRequest request, StreamObserver<InterconnectAttachment> responseObserver)
    
    
    public default void getInterconnectAttachment(GetInterconnectAttachmentRequest request, StreamObserver<InterconnectAttachment> responseObserver)

Gets details of a single InterconnectAttachment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetInterconnectAttachmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.GetInterconnectAttachmentRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[InterconnectAttachment](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.InterconnectAttachment)>`  
  
  
### getNetwork(GetNetworkRequest request, StreamObserver<Network> responseObserver)
    
    
    public default void getNetwork(GetNetworkRequest request, StreamObserver<Network> responseObserver)

Gets details of a single Network.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.GetNetworkRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Network](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Network)>`  
  
  
### getRouter(GetRouterRequest request, StreamObserver<Router> responseObserver)
    
    
    public default void getRouter(GetRouterRequest request, StreamObserver<Router> responseObserver)

Gets details of a single Router.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.GetRouterRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Router](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Router)>`  
  
  
### getSubnet(GetSubnetRequest request, StreamObserver<Subnet> responseObserver)
    
    
    public default void getSubnet(GetSubnetRequest request, StreamObserver<Subnet> responseObserver)

Gets details of a single Subnet.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSubnetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.GetSubnetRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Subnet](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Subnet)>`  
  
  
### getZone(GetZoneRequest request, StreamObserver<Zone> responseObserver) (deprecated)
    
    
    public default void getZone(GetZoneRequest request, StreamObserver<Zone> responseObserver)

Deprecated: not implemented. Gets details of a single Zone.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetZoneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.GetZoneRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Zone](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Zone)>`  
  
  
### initializeZone(InitializeZoneRequest request, StreamObserver<InitializeZoneResponse> responseObserver)
    
    
    public default void initializeZone(InitializeZoneRequest request, StreamObserver<InitializeZoneResponse> responseObserver)

InitializeZone will initialize resources for a zone in a project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[InitializeZoneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.InitializeZoneRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[InitializeZoneResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.InitializeZoneResponse)>`  
  
  
### listInterconnectAttachments(ListInterconnectAttachmentsRequest request, StreamObserver<ListInterconnectAttachmentsResponse> responseObserver)
    
    
    public default void listInterconnectAttachments(ListInterconnectAttachmentsRequest request, StreamObserver<ListInterconnectAttachmentsResponse> responseObserver)

Lists InterconnectAttachments in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListInterconnectAttachmentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListInterconnectAttachmentsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListInterconnectAttachmentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListInterconnectAttachmentsResponse)>`  
  
  
### listInterconnects(ListInterconnectsRequest request, StreamObserver<ListInterconnectsResponse> responseObserver)
    
    
    public default void listInterconnects(ListInterconnectsRequest request, StreamObserver<ListInterconnectsResponse> responseObserver)

Lists Interconnects in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListInterconnectsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListInterconnectsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListInterconnectsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListInterconnectsResponse)>`  
  
  
### listNetworks(ListNetworksRequest request, StreamObserver<ListNetworksResponse> responseObserver)
    
    
    public default void listNetworks(ListNetworksRequest request, StreamObserver<ListNetworksResponse> responseObserver)

Lists Networks in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListNetworksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListNetworksRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListNetworksResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListNetworksResponse)>`  
  
  
### listRouters(ListRoutersRequest request, StreamObserver<ListRoutersResponse> responseObserver)
    
    
    public default void listRouters(ListRoutersRequest request, StreamObserver<ListRoutersResponse> responseObserver)

Lists Routers in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRoutersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListRoutersRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListRoutersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListRoutersResponse)>`  
  
  
### listSubnets(ListSubnetsRequest request, StreamObserver<ListSubnetsResponse> responseObserver)
    
    
    public default void listSubnets(ListSubnetsRequest request, StreamObserver<ListSubnetsResponse> responseObserver)

Lists Subnets in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSubnetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListSubnetsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListSubnetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListSubnetsResponse)>`  
  
  
### listZones(ListZonesRequest request, StreamObserver<ListZonesResponse> responseObserver) (deprecated)
    
    
    public default void listZones(ListZonesRequest request, StreamObserver<ListZonesResponse> responseObserver)

Deprecated: not implemented. Lists Zones in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListZonesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListZonesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListZonesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListZonesResponse)>`  
  
  
### updateRouter(UpdateRouterRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void updateRouter(UpdateRouterRequest request, StreamObserver<Operation> responseObserver)

Updates the parameters of a single Router.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.UpdateRouterRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateSubnet(UpdateSubnetRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void updateSubnet(UpdateSubnetRequest request, StreamObserver<Operation> responseObserver)

Updates the parameters of a single Subnet.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSubnetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.UpdateSubnetRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
