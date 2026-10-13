---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.HubServiceGrpc.AsyncService
title: Interface HubServiceGrpc.AsyncService (1.98.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:28:07.174360+00:00
---

# Interface HubServiceGrpc.AsyncService (1.98.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.HubServiceGrpc.AsyncService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface HubServiceGrpc.AsyncService (1.98.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.98.0 (latest)  1.94.0  1.93.0  1.92.0  1.90.0  1.87.0  1.86.0  1.84.0  1.82.0  1.81.0  1.79.0  1.77.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.0  1.69.0  1.67.0  1.66.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.9  1.1.1  1.0.0  0.5.0 
    
    
    public static interface HubServiceGrpc.AsyncService

Network Connectivity Center is a hub-and-spoke abstraction for network connectivity management in Google Cloud. It reduces operational complexity through a simple, centralized connectivity management model.

## Methods 

### acceptHubSpoke(AcceptHubSpokeRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void acceptHubSpoke(AcceptHubSpokeRequest request, StreamObserver<Operation> responseObserver)

Accepts a proposal to attach a Network Connectivity Center spoke to a hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AcceptHubSpokeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.AcceptHubSpokeRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### acceptSpokeUpdate(AcceptSpokeUpdateRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void acceptSpokeUpdate(AcceptSpokeUpdateRequest request, StreamObserver<Operation> responseObserver)

Accepts a proposal to update a Network Connectivity Center spoke in a hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AcceptSpokeUpdateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.AcceptSpokeUpdateRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createGatewayAdvertisedRoute(CreateGatewayAdvertisedRouteRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void createGatewayAdvertisedRoute(CreateGatewayAdvertisedRouteRequest request, StreamObserver<Operation> responseObserver)

Create a GatewayAdvertisedRoute

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateGatewayAdvertisedRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.CreateGatewayAdvertisedRouteRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createHub(CreateHubRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void createHub(CreateHubRequest request, StreamObserver<Operation> responseObserver)

Creates a new Network Connectivity Center hub in the specified project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateHubRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.CreateHubRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createSpoke(CreateSpokeRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void createSpoke(CreateSpokeRequest request, StreamObserver<Operation> responseObserver)

Creates a Network Connectivity Center spoke.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateSpokeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.CreateSpokeRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteGatewayAdvertisedRoute(DeleteGatewayAdvertisedRouteRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void deleteGatewayAdvertisedRoute(DeleteGatewayAdvertisedRouteRequest request, StreamObserver<Operation> responseObserver)

Delete a GatewayAdvertisedRoute

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteGatewayAdvertisedRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.DeleteGatewayAdvertisedRouteRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteHub(DeleteHubRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void deleteHub(DeleteHubRequest request, StreamObserver<Operation> responseObserver)

Deletes a Network Connectivity Center hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteHubRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.DeleteHubRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteSpoke(DeleteSpokeRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void deleteSpoke(DeleteSpokeRequest request, StreamObserver<Operation> responseObserver)

Deletes a Network Connectivity Center spoke.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteSpokeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.DeleteSpokeRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### getGatewayAdvertisedRoute(GetGatewayAdvertisedRouteRequest request, StreamObserver<GatewayAdvertisedRoute> responseObserver)
    
    
    public default void getGatewayAdvertisedRoute(GetGatewayAdvertisedRouteRequest request, StreamObserver<GatewayAdvertisedRoute> responseObserver)

Get a GatewayAdvertisedRoute

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGatewayAdvertisedRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.GetGatewayAdvertisedRouteRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[GatewayAdvertisedRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.GatewayAdvertisedRoute)>`  
  
  
### getGroup(GetGroupRequest request, StreamObserver<Group> responseObserver)
    
    
    public default void getGroup(GetGroupRequest request, StreamObserver<Group> responseObserver)

Gets details about a Network Connectivity Center group.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.GetGroupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Group](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.Group)>`  
  
  
### getHub(GetHubRequest request, StreamObserver<Hub> responseObserver)
    
    
    public default void getHub(GetHubRequest request, StreamObserver<Hub> responseObserver)

Gets details about a Network Connectivity Center hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetHubRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.GetHubRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Hub](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.Hub)>`  
  
  
### getRoute(GetRouteRequest request, StreamObserver<Route> responseObserver)
    
    
    public default void getRoute(GetRouteRequest request, StreamObserver<Route> responseObserver)

Gets details about the specified route.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.GetRouteRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Route](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.Route)>`  
  
  
### getRouteTable(GetRouteTableRequest request, StreamObserver<RouteTable> responseObserver)
    
    
    public default void getRouteTable(GetRouteTableRequest request, StreamObserver<RouteTable> responseObserver)

Gets details about a Network Connectivity Center route table.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRouteTableRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.GetRouteTableRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[RouteTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.RouteTable)>`  
  
  
### getSpoke(GetSpokeRequest request, StreamObserver<Spoke> responseObserver)
    
    
    public default void getSpoke(GetSpokeRequest request, StreamObserver<Spoke> responseObserver)

Gets details about a Network Connectivity Center spoke.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSpokeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.GetSpokeRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Spoke](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.Spoke)>`  
  
  
### listGatewayAdvertisedRoutes(ListGatewayAdvertisedRoutesRequest request, StreamObserver<ListGatewayAdvertisedRoutesResponse> responseObserver)
    
    
    public default void listGatewayAdvertisedRoutes(ListGatewayAdvertisedRoutesRequest request, StreamObserver<ListGatewayAdvertisedRoutesResponse> responseObserver)

List GatewayAdvertisedRoutes

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGatewayAdvertisedRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.ListGatewayAdvertisedRoutesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListGatewayAdvertisedRoutesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.ListGatewayAdvertisedRoutesResponse)>`  
  
  
### listGroups(ListGroupsRequest request, StreamObserver<ListGroupsResponse> responseObserver)
    
    
    public default void listGroups(ListGroupsRequest request, StreamObserver<ListGroupsResponse> responseObserver)

Lists groups in a given hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.ListGroupsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListGroupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.ListGroupsResponse)>`  
  
  
### listHubSpokes(ListHubSpokesRequest request, StreamObserver<ListHubSpokesResponse> responseObserver)
    
    
    public default void listHubSpokes(ListHubSpokesRequest request, StreamObserver<ListHubSpokesResponse> responseObserver)

Lists the Network Connectivity Center spokes associated with a specified hub and location. The list includes both spokes that are attached to the hub and spokes that have been proposed but not yet accepted.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListHubSpokesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.ListHubSpokesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListHubSpokesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.ListHubSpokesResponse)>`  
  
  
### listHubs(ListHubsRequest request, StreamObserver<ListHubsResponse> responseObserver)
    
    
    public default void listHubs(ListHubsRequest request, StreamObserver<ListHubsResponse> responseObserver)

Lists the Network Connectivity Center hubs associated with a given project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListHubsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.ListHubsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListHubsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.ListHubsResponse)>`  
  
  
### listRouteTables(ListRouteTablesRequest request, StreamObserver<ListRouteTablesResponse> responseObserver)
    
    
    public default void listRouteTables(ListRouteTablesRequest request, StreamObserver<ListRouteTablesResponse> responseObserver)

Lists route tables in a given hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRouteTablesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.ListRouteTablesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListRouteTablesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.ListRouteTablesResponse)>`  
  
  
### listRoutes(ListRoutesRequest request, StreamObserver<ListRoutesResponse> responseObserver)
    
    
    public default void listRoutes(ListRoutesRequest request, StreamObserver<ListRoutesResponse> responseObserver)

Lists routes in a given route table.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.ListRoutesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListRoutesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.ListRoutesResponse)>`  
  
  
### listSpokes(ListSpokesRequest request, StreamObserver<ListSpokesResponse> responseObserver)
    
    
    public default void listSpokes(ListSpokesRequest request, StreamObserver<ListSpokesResponse> responseObserver)

Lists the Network Connectivity Center spokes in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSpokesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.ListSpokesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListSpokesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.ListSpokesResponse)>`  
  
  
### queryHubStatus(QueryHubStatusRequest request, StreamObserver<QueryHubStatusResponse> responseObserver)
    
    
    public default void queryHubStatus(QueryHubStatusRequest request, StreamObserver<QueryHubStatusResponse> responseObserver)

Query the Private Service Connect propagation status of a Network Connectivity Center hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryHubStatusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.QueryHubStatusRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[QueryHubStatusResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.QueryHubStatusResponse)>`  
  
  
### rejectHubSpoke(RejectHubSpokeRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void rejectHubSpoke(RejectHubSpokeRequest request, StreamObserver<Operation> responseObserver)

Rejects a Network Connectivity Center spoke from being attached to a hub. If the spoke was previously in the `ACTIVE` state, it transitions to the `INACTIVE` state and is no longer able to connect to other spokes that are attached to the hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RejectHubSpokeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.RejectHubSpokeRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### rejectSpokeUpdate(RejectSpokeUpdateRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void rejectSpokeUpdate(RejectSpokeUpdateRequest request, StreamObserver<Operation> responseObserver)

Rejects a proposal to update a Network Connectivity Center spoke in a hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RejectSpokeUpdateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.RejectSpokeUpdateRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateGatewayAdvertisedRoute(UpdateGatewayAdvertisedRouteRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void updateGatewayAdvertisedRoute(UpdateGatewayAdvertisedRouteRequest request, StreamObserver<Operation> responseObserver)

Update a GatewayAdvertisedRoute

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateGatewayAdvertisedRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.UpdateGatewayAdvertisedRouteRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateGroup(UpdateGroupRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void updateGroup(UpdateGroupRequest request, StreamObserver<Operation> responseObserver)

Updates the parameters of a Network Connectivity Center group.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.UpdateGroupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateHub(UpdateHubRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void updateHub(UpdateHubRequest request, StreamObserver<Operation> responseObserver)

Updates the description and/or labels of a Network Connectivity Center hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateHubRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.UpdateHubRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateSpoke(UpdateSpokeRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void updateSpoke(UpdateSpokeRequest request, StreamObserver<Operation> responseObserver)

Updates the parameters of a Network Connectivity Center spoke.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSpokeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.UpdateSpokeRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
