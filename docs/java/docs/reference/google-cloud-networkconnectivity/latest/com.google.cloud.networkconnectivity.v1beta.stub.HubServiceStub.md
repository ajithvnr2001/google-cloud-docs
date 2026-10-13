---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.stub.HubServiceStub
title: Class HubServiceStub (1.98.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:07:44.030739+00:00
---

# Class HubServiceStub (1.98.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.stub.HubServiceStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class HubServiceStub (1.98.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.98.0 (latest)  1.94.0  1.93.0  1.92.0  1.90.0  1.87.0  1.86.0  1.84.0  1.82.0  1.81.0  1.79.0  1.77.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.0  1.69.0  1.67.0  1.66.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.9  1.1.1  1.0.0  0.5.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 
    
    
    public abstract class HubServiceStub implements BackgroundResource

Base stub class for the HubService service API.

This class is for advanced usage and reflects the underlying API directly.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > HubServiceStub

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

### HubServiceStub()
    
    
    public HubServiceStub()

## Methods 

### acceptHubSpokeCallable()
    
    
    public UnaryCallable<AcceptHubSpokeRequest,Operation> acceptHubSpokeCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AcceptHubSpokeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.AcceptHubSpokeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### acceptHubSpokeOperationCallable()
    
    
    public OperationCallable<AcceptHubSpokeRequest,AcceptHubSpokeResponse,OperationMetadata> acceptHubSpokeOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[AcceptHubSpokeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.AcceptHubSpokeRequest),[AcceptHubSpokeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.AcceptHubSpokeResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.OperationMetadata)>` |   
  
### acceptSpokeUpdateCallable()
    
    
    public UnaryCallable<AcceptSpokeUpdateRequest,Operation> acceptSpokeUpdateCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AcceptSpokeUpdateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.AcceptSpokeUpdateRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### acceptSpokeUpdateOperationCallable()
    
    
    public OperationCallable<AcceptSpokeUpdateRequest,AcceptSpokeUpdateResponse,OperationMetadata> acceptSpokeUpdateOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[AcceptSpokeUpdateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.AcceptSpokeUpdateRequest),[AcceptSpokeUpdateResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.AcceptSpokeUpdateResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.OperationMetadata)>` |   
  
### close()
    
    
    public abstract void close()

### createGatewayAdvertisedRouteCallable()
    
    
    public UnaryCallable<CreateGatewayAdvertisedRouteRequest,Operation> createGatewayAdvertisedRouteCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateGatewayAdvertisedRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.CreateGatewayAdvertisedRouteRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createGatewayAdvertisedRouteOperationCallable()
    
    
    public OperationCallable<CreateGatewayAdvertisedRouteRequest,GatewayAdvertisedRoute,OperationMetadata> createGatewayAdvertisedRouteOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateGatewayAdvertisedRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.CreateGatewayAdvertisedRouteRequest),[GatewayAdvertisedRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.GatewayAdvertisedRoute),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.OperationMetadata)>` |   
  
### createHubCallable()
    
    
    public UnaryCallable<CreateHubRequest,Operation> createHubCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateHubRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.CreateHubRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createHubOperationCallable()
    
    
    public OperationCallable<CreateHubRequest,Hub,OperationMetadata> createHubOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateHubRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.CreateHubRequest),[Hub](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.Hub),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.OperationMetadata)>` |   
  
### createSpokeCallable()
    
    
    public UnaryCallable<CreateSpokeRequest,Operation> createSpokeCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateSpokeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.CreateSpokeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createSpokeOperationCallable()
    
    
    public OperationCallable<CreateSpokeRequest,Spoke,OperationMetadata> createSpokeOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateSpokeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.CreateSpokeRequest),[Spoke](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.Spoke),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.OperationMetadata)>` |   
  
### deleteGatewayAdvertisedRouteCallable()
    
    
    public UnaryCallable<DeleteGatewayAdvertisedRouteRequest,Operation> deleteGatewayAdvertisedRouteCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteGatewayAdvertisedRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.DeleteGatewayAdvertisedRouteRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteGatewayAdvertisedRouteOperationCallable()
    
    
    public OperationCallable<DeleteGatewayAdvertisedRouteRequest,Empty,OperationMetadata> deleteGatewayAdvertisedRouteOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteGatewayAdvertisedRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.DeleteGatewayAdvertisedRouteRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.OperationMetadata)>` |   
  
### deleteHubCallable()
    
    
    public UnaryCallable<DeleteHubRequest,Operation> deleteHubCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteHubRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.DeleteHubRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteHubOperationCallable()
    
    
    public OperationCallable<DeleteHubRequest,Empty,OperationMetadata> deleteHubOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteHubRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.DeleteHubRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.OperationMetadata)>` |   
  
### deleteSpokeCallable()
    
    
    public UnaryCallable<DeleteSpokeRequest,Operation> deleteSpokeCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteSpokeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.DeleteSpokeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteSpokeOperationCallable()
    
    
    public OperationCallable<DeleteSpokeRequest,Empty,OperationMetadata> deleteSpokeOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteSpokeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.DeleteSpokeRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.OperationMetadata)>` |   
  
### getGatewayAdvertisedRouteCallable()
    
    
    public UnaryCallable<GetGatewayAdvertisedRouteRequest,GatewayAdvertisedRoute> getGatewayAdvertisedRouteCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetGatewayAdvertisedRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.GetGatewayAdvertisedRouteRequest),[GatewayAdvertisedRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.GatewayAdvertisedRoute)>` |   
  
### getGroupCallable()
    
    
    public UnaryCallable<GetGroupRequest,Group> getGroupCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.GetGroupRequest),[Group](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.Group)>` |   
  
### getHubCallable()
    
    
    public UnaryCallable<GetHubRequest,Hub> getHubCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetHubRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.GetHubRequest),[Hub](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.Hub)>` |   
  
### getIamPolicyCallable()
    
    
    public UnaryCallable<GetIamPolicyRequest,Policy> getIamPolicyCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.GetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### getLocationCallable()
    
    
    public UnaryCallable<GetLocationRequest,Location> getLocationCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getOperationsStub()
    
    
    public @Nullable OperationsStub getOperationsStub()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.longrunning.stub.OperationsStub` |   
  
### getRouteCallable()
    
    
    public UnaryCallable<GetRouteRequest,Route> getRouteCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.GetRouteRequest),[Route](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.Route)>` |   
  
### getRouteTableCallable()
    
    
    public UnaryCallable<GetRouteTableRequest,RouteTable> getRouteTableCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetRouteTableRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.GetRouteTableRequest),[RouteTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.RouteTable)>` |   
  
### getSpokeCallable()
    
    
    public UnaryCallable<GetSpokeRequest,Spoke> getSpokeCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetSpokeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.GetSpokeRequest),[Spoke](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.Spoke)>` |   
  
### listGatewayAdvertisedRoutesCallable()
    
    
    public UnaryCallable<ListGatewayAdvertisedRoutesRequest,ListGatewayAdvertisedRoutesResponse> listGatewayAdvertisedRoutesCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGatewayAdvertisedRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.ListGatewayAdvertisedRoutesRequest),[ListGatewayAdvertisedRoutesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.ListGatewayAdvertisedRoutesResponse)>` |   
  
### listGatewayAdvertisedRoutesPagedCallable()
    
    
    public UnaryCallable<ListGatewayAdvertisedRoutesRequest,HubServiceClient.ListGatewayAdvertisedRoutesPagedResponse> listGatewayAdvertisedRoutesPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGatewayAdvertisedRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.ListGatewayAdvertisedRoutesRequest),[ListGatewayAdvertisedRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.HubServiceClient.ListGatewayAdvertisedRoutesPagedResponse)>` |   
  
### listGroupsCallable()
    
    
    public UnaryCallable<ListGroupsRequest,ListGroupsResponse> listGroupsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.ListGroupsRequest),[ListGroupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.ListGroupsResponse)>` |   
  
### listGroupsPagedCallable()
    
    
    public UnaryCallable<ListGroupsRequest,HubServiceClient.ListGroupsPagedResponse> listGroupsPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.ListGroupsRequest),[ListGroupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.HubServiceClient.ListGroupsPagedResponse)>` |   
  
### listHubSpokesCallable()
    
    
    public UnaryCallable<ListHubSpokesRequest,ListHubSpokesResponse> listHubSpokesCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListHubSpokesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.ListHubSpokesRequest),[ListHubSpokesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.ListHubSpokesResponse)>` |   
  
### listHubSpokesPagedCallable()
    
    
    public UnaryCallable<ListHubSpokesRequest,HubServiceClient.ListHubSpokesPagedResponse> listHubSpokesPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListHubSpokesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.ListHubSpokesRequest),[ListHubSpokesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.HubServiceClient.ListHubSpokesPagedResponse)>` |   
  
### listHubsCallable()
    
    
    public UnaryCallable<ListHubsRequest,ListHubsResponse> listHubsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListHubsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.ListHubsRequest),[ListHubsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.ListHubsResponse)>` |   
  
### listHubsPagedCallable()
    
    
    public UnaryCallable<ListHubsRequest,HubServiceClient.ListHubsPagedResponse> listHubsPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListHubsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.ListHubsRequest),[ListHubsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.HubServiceClient.ListHubsPagedResponse)>` |   
  
### listLocationsCallable()
    
    
    public UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse>` |   
  
### listLocationsPagedCallable()
    
    
    public UnaryCallable<ListLocationsRequest,HubServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.HubServiceClient.ListLocationsPagedResponse)>` |   
  
### listRouteTablesCallable()
    
    
    public UnaryCallable<ListRouteTablesRequest,ListRouteTablesResponse> listRouteTablesCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRouteTablesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.ListRouteTablesRequest),[ListRouteTablesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.ListRouteTablesResponse)>` |   
  
### listRouteTablesPagedCallable()
    
    
    public UnaryCallable<ListRouteTablesRequest,HubServiceClient.ListRouteTablesPagedResponse> listRouteTablesPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRouteTablesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.ListRouteTablesRequest),[ListRouteTablesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.HubServiceClient.ListRouteTablesPagedResponse)>` |   
  
### listRoutesCallable()
    
    
    public UnaryCallable<ListRoutesRequest,ListRoutesResponse> listRoutesCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.ListRoutesRequest),[ListRoutesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.ListRoutesResponse)>` |   
  
### listRoutesPagedCallable()
    
    
    public UnaryCallable<ListRoutesRequest,HubServiceClient.ListRoutesPagedResponse> listRoutesPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.ListRoutesRequest),[ListRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.HubServiceClient.ListRoutesPagedResponse)>` |   
  
### listSpokesCallable()
    
    
    public UnaryCallable<ListSpokesRequest,ListSpokesResponse> listSpokesCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSpokesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.ListSpokesRequest),[ListSpokesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.ListSpokesResponse)>` |   
  
### listSpokesPagedCallable()
    
    
    public UnaryCallable<ListSpokesRequest,HubServiceClient.ListSpokesPagedResponse> listSpokesPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSpokesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.ListSpokesRequest),[ListSpokesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.HubServiceClient.ListSpokesPagedResponse)>` |   
  
### queryHubStatusCallable()
    
    
    public UnaryCallable<QueryHubStatusRequest,QueryHubStatusResponse> queryHubStatusCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[QueryHubStatusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.QueryHubStatusRequest),[QueryHubStatusResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.QueryHubStatusResponse)>` |   
  
### queryHubStatusPagedCallable()
    
    
    public UnaryCallable<QueryHubStatusRequest,HubServiceClient.QueryHubStatusPagedResponse> queryHubStatusPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[QueryHubStatusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.QueryHubStatusRequest),[QueryHubStatusPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.HubServiceClient.QueryHubStatusPagedResponse)>` |   
  
### rejectHubSpokeCallable()
    
    
    public UnaryCallable<RejectHubSpokeRequest,Operation> rejectHubSpokeCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RejectHubSpokeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.RejectHubSpokeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### rejectHubSpokeOperationCallable()
    
    
    public OperationCallable<RejectHubSpokeRequest,RejectHubSpokeResponse,OperationMetadata> rejectHubSpokeOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RejectHubSpokeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.RejectHubSpokeRequest),[RejectHubSpokeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.RejectHubSpokeResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.OperationMetadata)>` |   
  
### rejectSpokeUpdateCallable()
    
    
    public UnaryCallable<RejectSpokeUpdateRequest,Operation> rejectSpokeUpdateCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RejectSpokeUpdateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.RejectSpokeUpdateRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### rejectSpokeUpdateOperationCallable()
    
    
    public OperationCallable<RejectSpokeUpdateRequest,RejectSpokeUpdateResponse,OperationMetadata> rejectSpokeUpdateOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RejectSpokeUpdateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.RejectSpokeUpdateRequest),[RejectSpokeUpdateResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.RejectSpokeUpdateResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.OperationMetadata)>` |   
  
### setIamPolicyCallable()
    
    
    public UnaryCallable<SetIamPolicyRequest,Policy> setIamPolicyCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.SetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### testIamPermissionsCallable()
    
    
    public UnaryCallable<TestIamPermissionsRequest,TestIamPermissionsResponse> testIamPermissionsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### updateGatewayAdvertisedRouteCallable()
    
    
    public UnaryCallable<UpdateGatewayAdvertisedRouteRequest,Operation> updateGatewayAdvertisedRouteCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateGatewayAdvertisedRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.UpdateGatewayAdvertisedRouteRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateGatewayAdvertisedRouteOperationCallable()
    
    
    public OperationCallable<UpdateGatewayAdvertisedRouteRequest,GatewayAdvertisedRoute,OperationMetadata> updateGatewayAdvertisedRouteOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateGatewayAdvertisedRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.UpdateGatewayAdvertisedRouteRequest),[GatewayAdvertisedRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.GatewayAdvertisedRoute),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.OperationMetadata)>` |   
  
### updateGroupCallable()
    
    
    public UnaryCallable<UpdateGroupRequest,Operation> updateGroupCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.UpdateGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateGroupOperationCallable()
    
    
    public OperationCallable<UpdateGroupRequest,Group,OperationMetadata> updateGroupOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.UpdateGroupRequest),[Group](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.Group),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.OperationMetadata)>` |   
  
### updateHubCallable()
    
    
    public UnaryCallable<UpdateHubRequest,Operation> updateHubCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateHubRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.UpdateHubRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateHubOperationCallable()
    
    
    public OperationCallable<UpdateHubRequest,Hub,OperationMetadata> updateHubOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateHubRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.UpdateHubRequest),[Hub](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.Hub),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.OperationMetadata)>` |   
  
### updateSpokeCallable()
    
    
    public UnaryCallable<UpdateSpokeRequest,Operation> updateSpokeCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateSpokeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.UpdateSpokeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateSpokeOperationCallable()
    
    
    public OperationCallable<UpdateSpokeRequest,Spoke,OperationMetadata> updateSpokeOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateSpokeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.UpdateSpokeRequest),[Spoke](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.Spoke),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.OperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
