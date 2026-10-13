---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceClient
title: Class HubServiceClient (1.98.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:42:07.384990+00:00
---

# Class HubServiceClient (1.98.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class HubServiceClient (1.98.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.98.0 (latest)  1.94.0  1.93.0  1.92.0  1.90.0  1.87.0  1.86.0  1.84.0  1.82.0  1.81.0  1.79.0  1.77.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.0  1.69.0  1.67.0  1.66.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.9  1.1.1  1.0.0  0.5.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-networkconnectivity/google-cloud-networkconnectivity/src/main/java/com/google/cloud/networkconnectivity/v1/HubServiceClient.java)| [Product Reference](https://cloud.google.com/network-connectivity/docs)  
---|---  
  
Service Description: Network Connectivity Center is a hub-and-spoke abstraction for network connectivity management in Google Cloud. It reduces operational complexity through a simple, centralized connectivity management model.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       HubName name = HubName.of("[PROJECT]", "[HUB]");
       Hub response = hubServiceClient.getHub(name);
     }
     

Note: close() needs to be called on the HubServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListHubs |  Lists the Network Connectivity Center hubs associated with a given project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listHubs(ListHubsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listHubs(LocationName parent) 
  * listHubs(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listHubsPagedCallable() 
  * listHubsCallable() 

  
GetHub |  Gets details about a Network Connectivity Center hub. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getHub(GetHubRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getHub(HubName name) 
  * getHub(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getHubCallable() 

  
CreateHub |  Creates a new Network Connectivity Center hub in the specified project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createHubAsync(CreateHubRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createHubAsync(LocationName parent, Hub hub, String hubId) 
  * createHubAsync(String parent, Hub hub, String hubId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createHubOperationCallable() 
  * createHubCallable() 

  
UpdateHub |  Updates the description and/or labels of a Network Connectivity Center hub. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateHubAsync(UpdateHubRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateHubAsync(Hub hub, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateHubOperationCallable() 
  * updateHubCallable() 

  
DeleteHub |  Deletes a Network Connectivity Center hub. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteHubAsync(DeleteHubRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteHubAsync(HubName name) 
  * deleteHubAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteHubOperationCallable() 
  * deleteHubCallable() 

  
ListHubSpokes |  Lists the Network Connectivity Center spokes associated with a specified hub and location. The list includes both spokes that are attached to the hub and spokes that have been proposed but not yet accepted. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listHubSpokes(ListHubSpokesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listHubSpokes(HubName name) 
  * listHubSpokes(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listHubSpokesPagedCallable() 
  * listHubSpokesCallable() 

  
QueryHubStatus |  Query the Private Service Connect propagation status of a Network Connectivity Center hub. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * queryHubStatus(QueryHubStatusRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * queryHubStatus(HubName name) 
  * queryHubStatus(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * queryHubStatusPagedCallable() 
  * queryHubStatusCallable() 

  
ListSpokes |  Lists the Network Connectivity Center spokes in a specified project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listSpokes(ListSpokesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listSpokes(LocationName parent) 
  * listSpokes(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listSpokesPagedCallable() 
  * listSpokesCallable() 

  
GetSpoke |  Gets details about a Network Connectivity Center spoke. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getSpoke(GetSpokeRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getSpoke(SpokeName name) 
  * getSpoke(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getSpokeCallable() 

  
CreateSpoke |  Creates a Network Connectivity Center spoke. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createSpokeAsync(CreateSpokeRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createSpokeAsync(LocationName parent, Spoke spoke, String spokeId) 
  * createSpokeAsync(String parent, Spoke spoke, String spokeId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createSpokeOperationCallable() 
  * createSpokeCallable() 

  
UpdateSpoke |  Updates the parameters of a Network Connectivity Center spoke. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateSpokeAsync(UpdateSpokeRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateSpokeAsync(Spoke spoke, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateSpokeOperationCallable() 
  * updateSpokeCallable() 

  
RejectHubSpoke |  Rejects a Network Connectivity Center spoke from being attached to a hub. If the spoke was previously in the `ACTIVE` state, it transitions to the `INACTIVE` state and is no longer able to connect to other spokes that are attached to the hub. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * rejectHubSpokeAsync(RejectHubSpokeRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * rejectHubSpokeAsync(HubName name, SpokeName spokeUri) 
  * rejectHubSpokeAsync(HubName name, String spokeUri) 
  * rejectHubSpokeAsync(String name, SpokeName spokeUri) 
  * rejectHubSpokeAsync(String name, String spokeUri) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * rejectHubSpokeOperationCallable() 
  * rejectHubSpokeCallable() 

  
AcceptHubSpoke |  Accepts a proposal to attach a Network Connectivity Center spoke to a hub. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * acceptHubSpokeAsync(AcceptHubSpokeRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * acceptHubSpokeAsync(HubName name, SpokeName spokeUri) 
  * acceptHubSpokeAsync(HubName name, String spokeUri) 
  * acceptHubSpokeAsync(String name, SpokeName spokeUri) 
  * acceptHubSpokeAsync(String name, String spokeUri) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * acceptHubSpokeOperationCallable() 
  * acceptHubSpokeCallable() 

  
AcceptSpokeUpdate |  Accepts a proposal to update a Network Connectivity Center spoke in a hub. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * acceptSpokeUpdateAsync(AcceptSpokeUpdateRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * acceptSpokeUpdateAsync(HubName name, SpokeName spokeUri, String spokeEtag) 
  * acceptSpokeUpdateAsync(HubName name, String spokeUri, String spokeEtag) 
  * acceptSpokeUpdateAsync(String name, SpokeName spokeUri, String spokeEtag) 
  * acceptSpokeUpdateAsync(String name, String spokeUri, String spokeEtag) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * acceptSpokeUpdateOperationCallable() 
  * acceptSpokeUpdateCallable() 

  
RejectSpokeUpdate |  Rejects a proposal to update a Network Connectivity Center spoke in a hub. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * rejectSpokeUpdateAsync(RejectSpokeUpdateRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * rejectSpokeUpdateAsync(HubName name, SpokeName spokeUri, String spokeEtag) 
  * rejectSpokeUpdateAsync(HubName name, String spokeUri, String spokeEtag) 
  * rejectSpokeUpdateAsync(String name, SpokeName spokeUri, String spokeEtag) 
  * rejectSpokeUpdateAsync(String name, String spokeUri, String spokeEtag) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * rejectSpokeUpdateOperationCallable() 
  * rejectSpokeUpdateCallable() 

  
DeleteSpoke |  Deletes a Network Connectivity Center spoke. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteSpokeAsync(DeleteSpokeRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteSpokeAsync(SpokeName name) 
  * deleteSpokeAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteSpokeOperationCallable() 
  * deleteSpokeCallable() 

  
GetRouteTable |  Gets details about a Network Connectivity Center route table. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getRouteTable(GetRouteTableRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getRouteTable(RouteTableName name) 
  * getRouteTable(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getRouteTableCallable() 

  
GetRoute |  Gets details about the specified route. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getRoute(GetRouteRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getRoute(HubRouteName name) 
  * getRoute(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getRouteCallable() 

  
ListRoutes |  Lists routes in a given route table. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listRoutes(ListRoutesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listRoutes(RouteTableName parent) 
  * listRoutes(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listRoutesPagedCallable() 
  * listRoutesCallable() 

  
ListRouteTables |  Lists route tables in a given hub. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listRouteTables(ListRouteTablesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listRouteTables(HubName parent) 
  * listRouteTables(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listRouteTablesPagedCallable() 
  * listRouteTablesCallable() 

  
GetGroup |  Gets details about a Network Connectivity Center group. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getGroup(GetGroupRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getGroup(GroupName name) 
  * getGroup(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getGroupCallable() 

  
ListGroups |  Lists groups in a given hub. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listGroups(ListGroupsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listGroups(HubName parent) 
  * listGroups(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listGroupsPagedCallable() 
  * listGroupsCallable() 

  
UpdateGroup |  Updates the parameters of a Network Connectivity Center group. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateGroupAsync(UpdateGroupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateGroupAsync(Group group, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateGroupOperationCallable() 
  * updateGroupCallable() 

  
ListLocations |  Lists information about the supported locations for this service. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listLocations(ListLocationsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listLocationsPagedCallable() 
  * listLocationsCallable() 

  
GetLocation |  Gets information about a location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getLocation(GetLocationRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getLocationCallable() 

  
SetIamPolicy |  Sets the access control policy on the specified resource. Replacesany existing policy.  Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED`errors. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setIamPolicy(SetIamPolicyRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setIamPolicyCallable() 

  
GetIamPolicy |  Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getIamPolicy(GetIamPolicyRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getIamPolicyCallable() 

  
TestIamPermissions |  Returns permissions that a caller has on the specified resource. If theresource does not exist, this will return an empty set ofpermissions, not a `NOT_FOUND` error.  Note: This operation is designed to be used for buildingpermission-aware UIs and command-line tools, not for authorizationchecking. This operation may "fail open" without warning. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of HubServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     HubServiceSettings hubServiceSettings =
         HubServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     HubServiceClient hubServiceClient = HubServiceClient.create(hubServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     HubServiceSettings hubServiceSettings =
         HubServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     HubServiceClient hubServiceClient = HubServiceClient.create(hubServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > HubServiceClient

## Static Methods 

### create()
    
    
    public static final HubServiceClient create()

Constructs an instance of HubServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[HubServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(HubServiceSettings settings)
    
    
    public static final HubServiceClient create(HubServiceSettings settings)

Constructs an instance of HubServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[HubServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HubServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(HubServiceStub stub)
    
    
    public static final HubServiceClient create(HubServiceStub stub)

Constructs an instance of HubServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(HubServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[HubServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.stub.HubServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HubServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceClient)` |   
  
## Constructors 

### HubServiceClient(HubServiceSettings settings)
    
    
    protected HubServiceClient(HubServiceSettings settings)

Constructs an instance of HubServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[HubServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceSettings)`  
  
  
### HubServiceClient(HubServiceStub stub)
    
    
    protected HubServiceClient(HubServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[HubServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.stub.HubServiceStub)`  
  
  
## Methods 

### acceptHubSpokeAsync(@Nullable HubName name, @Nullable SpokeName spokeUri)
    
    
    public final OperationFuture<AcceptHubSpokeResponse,OperationMetadata> acceptHubSpokeAsync(@Nullable HubName name, @Nullable SpokeName spokeUri)

Accepts a proposal to attach a Network Connectivity Center spoke to a hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       HubName name = HubName.of("[PROJECT]", "[HUB]");
       SpokeName spokeUri = SpokeName.of("[PROJECT]", "[LOCATION]", "[SPOKE]");
       AcceptHubSpokeResponse response = hubServiceClient.acceptHubSpokeAsync(name, spokeUri).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.HubName`  
Required. The name of the hub into which to accept the spoke.  
`spokeUri` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.SpokeName`  
Required. The URI of the spoke to accept into the hub.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AcceptHubSpokeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.AcceptHubSpokeResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### acceptHubSpokeAsync(@Nullable HubName name, String spokeUri)
    
    
    public final OperationFuture<AcceptHubSpokeResponse,OperationMetadata> acceptHubSpokeAsync(@Nullable HubName name, String spokeUri)

Accepts a proposal to attach a Network Connectivity Center spoke to a hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       HubName name = HubName.of("[PROJECT]", "[HUB]");
       String spokeUri = SpokeName.of("[PROJECT]", "[LOCATION]", "[SPOKE]").toString();
       AcceptHubSpokeResponse response = hubServiceClient.acceptHubSpokeAsync(name, spokeUri).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.HubName`  
Required. The name of the hub into which to accept the spoke.  
`spokeUri` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The URI of the spoke to accept into the hub.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AcceptHubSpokeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.AcceptHubSpokeResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### acceptHubSpokeAsync(AcceptHubSpokeRequest request)
    
    
    public final OperationFuture<AcceptHubSpokeResponse,OperationMetadata> acceptHubSpokeAsync(AcceptHubSpokeRequest request)

Accepts a proposal to attach a Network Connectivity Center spoke to a hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       AcceptHubSpokeRequest request =
           AcceptHubSpokeRequest.newBuilder()
               .setName(HubName.of("[PROJECT]", "[HUB]").toString())
               .setSpokeUri(SpokeName.of("[PROJECT]", "[LOCATION]", "[SPOKE]").toString())
               .setRequestId("requestId693933066")
               .build();
       AcceptHubSpokeResponse response = hubServiceClient.acceptHubSpokeAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AcceptHubSpokeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.AcceptHubSpokeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AcceptHubSpokeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.AcceptHubSpokeResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### acceptHubSpokeAsync(String name, @Nullable SpokeName spokeUri)
    
    
    public final OperationFuture<AcceptHubSpokeResponse,OperationMetadata> acceptHubSpokeAsync(String name, @Nullable SpokeName spokeUri)

Accepts a proposal to attach a Network Connectivity Center spoke to a hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       String name = HubName.of("[PROJECT]", "[HUB]").toString();
       SpokeName spokeUri = SpokeName.of("[PROJECT]", "[LOCATION]", "[SPOKE]");
       AcceptHubSpokeResponse response = hubServiceClient.acceptHubSpokeAsync(name, spokeUri).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the hub into which to accept the spoke.  
`spokeUri` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.SpokeName`  
Required. The URI of the spoke to accept into the hub.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AcceptHubSpokeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.AcceptHubSpokeResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### acceptHubSpokeAsync(String name, String spokeUri)
    
    
    public final OperationFuture<AcceptHubSpokeResponse,OperationMetadata> acceptHubSpokeAsync(String name, String spokeUri)

Accepts a proposal to attach a Network Connectivity Center spoke to a hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       String name = HubName.of("[PROJECT]", "[HUB]").toString();
       String spokeUri = SpokeName.of("[PROJECT]", "[LOCATION]", "[SPOKE]").toString();
       AcceptHubSpokeResponse response = hubServiceClient.acceptHubSpokeAsync(name, spokeUri).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the hub into which to accept the spoke.  
`spokeUri` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The URI of the spoke to accept into the hub.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AcceptHubSpokeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.AcceptHubSpokeResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### acceptHubSpokeCallable()
    
    
    public final UnaryCallable<AcceptHubSpokeRequest,Operation> acceptHubSpokeCallable()

Accepts a proposal to attach a Network Connectivity Center spoke to a hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       AcceptHubSpokeRequest request =
           AcceptHubSpokeRequest.newBuilder()
               .setName(HubName.of("[PROJECT]", "[HUB]").toString())
               .setSpokeUri(SpokeName.of("[PROJECT]", "[LOCATION]", "[SPOKE]").toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = hubServiceClient.acceptHubSpokeCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AcceptHubSpokeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.AcceptHubSpokeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### acceptHubSpokeOperationCallable()
    
    
    public final OperationCallable<AcceptHubSpokeRequest,AcceptHubSpokeResponse,OperationMetadata> acceptHubSpokeOperationCallable()

Accepts a proposal to attach a Network Connectivity Center spoke to a hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       AcceptHubSpokeRequest request =
           AcceptHubSpokeRequest.newBuilder()
               .setName(HubName.of("[PROJECT]", "[HUB]").toString())
               .setSpokeUri(SpokeName.of("[PROJECT]", "[LOCATION]", "[SPOKE]").toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<AcceptHubSpokeResponse, OperationMetadata> future =
           hubServiceClient.acceptHubSpokeOperationCallable().futureCall(request);
       // Do something.
       AcceptHubSpokeResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[AcceptHubSpokeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.AcceptHubSpokeRequest),[AcceptHubSpokeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.AcceptHubSpokeResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### acceptSpokeUpdateAsync(@Nullable HubName name, @Nullable SpokeName spokeUri, String spokeEtag)
    
    
    public final OperationFuture<AcceptSpokeUpdateResponse,OperationMetadata> acceptSpokeUpdateAsync(@Nullable HubName name, @Nullable SpokeName spokeUri, String spokeEtag)

Accepts a proposal to update a Network Connectivity Center spoke in a hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       HubName name = HubName.of("[PROJECT]", "[HUB]");
       SpokeName spokeUri = SpokeName.of("[PROJECT]", "[LOCATION]", "[SPOKE]");
       String spokeEtag = "spokeEtag-1185145407";
       AcceptSpokeUpdateResponse response =
           hubServiceClient.acceptSpokeUpdateAsync(name, spokeUri, spokeEtag).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.HubName`  
Required. The name of the hub to accept spoke update.  
`spokeUri` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.SpokeName`  
Required. The URI of the spoke to accept update.  
`spokeEtag` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The etag of the spoke to accept update.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AcceptSpokeUpdateResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.AcceptSpokeUpdateResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### acceptSpokeUpdateAsync(@Nullable HubName name, String spokeUri, String spokeEtag)
    
    
    public final OperationFuture<AcceptSpokeUpdateResponse,OperationMetadata> acceptSpokeUpdateAsync(@Nullable HubName name, String spokeUri, String spokeEtag)

Accepts a proposal to update a Network Connectivity Center spoke in a hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       HubName name = HubName.of("[PROJECT]", "[HUB]");
       String spokeUri = SpokeName.of("[PROJECT]", "[LOCATION]", "[SPOKE]").toString();
       String spokeEtag = "spokeEtag-1185145407";
       AcceptSpokeUpdateResponse response =
           hubServiceClient.acceptSpokeUpdateAsync(name, spokeUri, spokeEtag).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.HubName`  
Required. The name of the hub to accept spoke update.  
`spokeUri` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The URI of the spoke to accept update.  
`spokeEtag` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The etag of the spoke to accept update.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AcceptSpokeUpdateResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.AcceptSpokeUpdateResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### acceptSpokeUpdateAsync(AcceptSpokeUpdateRequest request)
    
    
    public final OperationFuture<AcceptSpokeUpdateResponse,OperationMetadata> acceptSpokeUpdateAsync(AcceptSpokeUpdateRequest request)

Accepts a proposal to update a Network Connectivity Center spoke in a hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       AcceptSpokeUpdateRequest request =
           AcceptSpokeUpdateRequest.newBuilder()
               .setName(HubName.of("[PROJECT]", "[HUB]").toString())
               .setSpokeUri(SpokeName.of("[PROJECT]", "[LOCATION]", "[SPOKE]").toString())
               .setSpokeEtag("spokeEtag-1185145407")
               .setRequestId("requestId693933066")
               .build();
       AcceptSpokeUpdateResponse response = hubServiceClient.acceptSpokeUpdateAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AcceptSpokeUpdateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.AcceptSpokeUpdateRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AcceptSpokeUpdateResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.AcceptSpokeUpdateResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### acceptSpokeUpdateAsync(String name, @Nullable SpokeName spokeUri, String spokeEtag)
    
    
    public final OperationFuture<AcceptSpokeUpdateResponse,OperationMetadata> acceptSpokeUpdateAsync(String name, @Nullable SpokeName spokeUri, String spokeEtag)

Accepts a proposal to update a Network Connectivity Center spoke in a hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       String name = HubName.of("[PROJECT]", "[HUB]").toString();
       SpokeName spokeUri = SpokeName.of("[PROJECT]", "[LOCATION]", "[SPOKE]");
       String spokeEtag = "spokeEtag-1185145407";
       AcceptSpokeUpdateResponse response =
           hubServiceClient.acceptSpokeUpdateAsync(name, spokeUri, spokeEtag).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the hub to accept spoke update.  
`spokeUri` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.SpokeName`  
Required. The URI of the spoke to accept update.  
`spokeEtag` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The etag of the spoke to accept update.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AcceptSpokeUpdateResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.AcceptSpokeUpdateResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### acceptSpokeUpdateAsync(String name, String spokeUri, String spokeEtag)
    
    
    public final OperationFuture<AcceptSpokeUpdateResponse,OperationMetadata> acceptSpokeUpdateAsync(String name, String spokeUri, String spokeEtag)

Accepts a proposal to update a Network Connectivity Center spoke in a hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       String name = HubName.of("[PROJECT]", "[HUB]").toString();
       String spokeUri = SpokeName.of("[PROJECT]", "[LOCATION]", "[SPOKE]").toString();
       String spokeEtag = "spokeEtag-1185145407";
       AcceptSpokeUpdateResponse response =
           hubServiceClient.acceptSpokeUpdateAsync(name, spokeUri, spokeEtag).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the hub to accept spoke update.  
`spokeUri` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The URI of the spoke to accept update.  
`spokeEtag` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The etag of the spoke to accept update.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AcceptSpokeUpdateResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.AcceptSpokeUpdateResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### acceptSpokeUpdateCallable()
    
    
    public final UnaryCallable<AcceptSpokeUpdateRequest,Operation> acceptSpokeUpdateCallable()

Accepts a proposal to update a Network Connectivity Center spoke in a hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       AcceptSpokeUpdateRequest request =
           AcceptSpokeUpdateRequest.newBuilder()
               .setName(HubName.of("[PROJECT]", "[HUB]").toString())
               .setSpokeUri(SpokeName.of("[PROJECT]", "[LOCATION]", "[SPOKE]").toString())
               .setSpokeEtag("spokeEtag-1185145407")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           hubServiceClient.acceptSpokeUpdateCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AcceptSpokeUpdateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.AcceptSpokeUpdateRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### acceptSpokeUpdateOperationCallable()
    
    
    public final OperationCallable<AcceptSpokeUpdateRequest,AcceptSpokeUpdateResponse,OperationMetadata> acceptSpokeUpdateOperationCallable()

Accepts a proposal to update a Network Connectivity Center spoke in a hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       AcceptSpokeUpdateRequest request =
           AcceptSpokeUpdateRequest.newBuilder()
               .setName(HubName.of("[PROJECT]", "[HUB]").toString())
               .setSpokeUri(SpokeName.of("[PROJECT]", "[LOCATION]", "[SPOKE]").toString())
               .setSpokeEtag("spokeEtag-1185145407")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<AcceptSpokeUpdateResponse, OperationMetadata> future =
           hubServiceClient.acceptSpokeUpdateOperationCallable().futureCall(request);
       // Do something.
       AcceptSpokeUpdateResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[AcceptSpokeUpdateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.AcceptSpokeUpdateRequest),[AcceptSpokeUpdateResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.AcceptSpokeUpdateResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### awaitTermination(long duration, TimeUnit unit)
    
    
    public boolean awaitTermination(long duration, TimeUnit unit)

**Parameters**  
---  
**Name** | **Description**  
`duration` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`unit` | `[TimeUnit](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/TimeUnit.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InterruptedException](https://docs.oracle.com/javase/8/docs/api/java/lang/InterruptedException.html)` |   
  
### close()
    
    
    public final void close()

### createHubAsync(@Nullable LocationName parent, Hub hub, String hubId)
    
    
    public final OperationFuture<Hub,OperationMetadata> createHubAsync(@Nullable LocationName parent, Hub hub, String hubId)

Creates a new Network Connectivity Center hub in the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Hub hub = Hub.newBuilder().build();
       String hubId = "hubId99628272";
       Hub response = hubServiceClient.createHubAsync(parent, hub, hubId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.LocationName`  
Required. The parent resource.  
`hub` | `[Hub](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Hub)`  
Required. The initial values for a new hub.  
`hubId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A unique identifier for the hub.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Hub](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Hub),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### createHubAsync(CreateHubRequest request)
    
    
    public final OperationFuture<Hub,OperationMetadata> createHubAsync(CreateHubRequest request)

Creates a new Network Connectivity Center hub in the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       CreateHubRequest request =
           CreateHubRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setHubId("hubId99628272")
               .setHub(Hub.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Hub response = hubServiceClient.createHubAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateHubRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CreateHubRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Hub](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Hub),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### createHubAsync(String parent, Hub hub, String hubId)
    
    
    public final OperationFuture<Hub,OperationMetadata> createHubAsync(String parent, Hub hub, String hubId)

Creates a new Network Connectivity Center hub in the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Hub hub = Hub.newBuilder().build();
       String hubId = "hubId99628272";
       Hub response = hubServiceClient.createHubAsync(parent, hub, hubId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource.  
`hub` | `[Hub](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Hub)`  
Required. The initial values for a new hub.  
`hubId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A unique identifier for the hub.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Hub](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Hub),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### createHubCallable()
    
    
    public final UnaryCallable<CreateHubRequest,Operation> createHubCallable()

Creates a new Network Connectivity Center hub in the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       CreateHubRequest request =
           CreateHubRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setHubId("hubId99628272")
               .setHub(Hub.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = hubServiceClient.createHubCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateHubRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CreateHubRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createHubOperationCallable()
    
    
    public final OperationCallable<CreateHubRequest,Hub,OperationMetadata> createHubOperationCallable()

Creates a new Network Connectivity Center hub in the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       CreateHubRequest request =
           CreateHubRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setHubId("hubId99628272")
               .setHub(Hub.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Hub, OperationMetadata> future =
           hubServiceClient.createHubOperationCallable().futureCall(request);
       // Do something.
       Hub response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateHubRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CreateHubRequest),[Hub](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Hub),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### createSpokeAsync(@Nullable LocationName parent, Spoke spoke, String spokeId)
    
    
    public final OperationFuture<Spoke,OperationMetadata> createSpokeAsync(@Nullable LocationName parent, Spoke spoke, String spokeId)

Creates a Network Connectivity Center spoke.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Spoke spoke = Spoke.newBuilder().build();
       String spokeId = "spokeId-1998996281";
       Spoke response = hubServiceClient.createSpokeAsync(parent, spoke, spokeId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.LocationName`  
Required. The parent resource.  
`spoke` | `[Spoke](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Spoke)`  
Required. The initial values for a new spoke.  
`spokeId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Unique id for the spoke to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Spoke](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Spoke),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### createSpokeAsync(CreateSpokeRequest request)
    
    
    public final OperationFuture<Spoke,OperationMetadata> createSpokeAsync(CreateSpokeRequest request)

Creates a Network Connectivity Center spoke.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       CreateSpokeRequest request =
           CreateSpokeRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setSpokeId("spokeId-1998996281")
               .setSpoke(Spoke.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Spoke response = hubServiceClient.createSpokeAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateSpokeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CreateSpokeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Spoke](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Spoke),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### createSpokeAsync(String parent, Spoke spoke, String spokeId)
    
    
    public final OperationFuture<Spoke,OperationMetadata> createSpokeAsync(String parent, Spoke spoke, String spokeId)

Creates a Network Connectivity Center spoke.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Spoke spoke = Spoke.newBuilder().build();
       String spokeId = "spokeId-1998996281";
       Spoke response = hubServiceClient.createSpokeAsync(parent, spoke, spokeId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource.  
`spoke` | `[Spoke](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Spoke)`  
Required. The initial values for a new spoke.  
`spokeId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Unique id for the spoke to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Spoke](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Spoke),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### createSpokeCallable()
    
    
    public final UnaryCallable<CreateSpokeRequest,Operation> createSpokeCallable()

Creates a Network Connectivity Center spoke.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       CreateSpokeRequest request =
           CreateSpokeRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setSpokeId("spokeId-1998996281")
               .setSpoke(Spoke.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = hubServiceClient.createSpokeCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateSpokeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CreateSpokeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createSpokeOperationCallable()
    
    
    public final OperationCallable<CreateSpokeRequest,Spoke,OperationMetadata> createSpokeOperationCallable()

Creates a Network Connectivity Center spoke.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       CreateSpokeRequest request =
           CreateSpokeRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setSpokeId("spokeId-1998996281")
               .setSpoke(Spoke.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Spoke, OperationMetadata> future =
           hubServiceClient.createSpokeOperationCallable().futureCall(request);
       // Do something.
       Spoke response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateSpokeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CreateSpokeRequest),[Spoke](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Spoke),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### deleteHubAsync(@Nullable HubName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteHubAsync(@Nullable HubName name)

Deletes a Network Connectivity Center hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       HubName name = HubName.of("[PROJECT]", "[HUB]");
       hubServiceClient.deleteHubAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.HubName`  
Required. The name of the hub to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### deleteHubAsync(DeleteHubRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteHubAsync(DeleteHubRequest request)

Deletes a Network Connectivity Center hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       DeleteHubRequest request =
           DeleteHubRequest.newBuilder()
               .setName(HubName.of("[PROJECT]", "[HUB]").toString())
               .setRequestId("requestId693933066")
               .build();
       hubServiceClient.deleteHubAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteHubRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DeleteHubRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### deleteHubAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteHubAsync(String name)

Deletes a Network Connectivity Center hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       String name = HubName.of("[PROJECT]", "[HUB]").toString();
       hubServiceClient.deleteHubAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the hub to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### deleteHubCallable()
    
    
    public final UnaryCallable<DeleteHubRequest,Operation> deleteHubCallable()

Deletes a Network Connectivity Center hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       DeleteHubRequest request =
           DeleteHubRequest.newBuilder()
               .setName(HubName.of("[PROJECT]", "[HUB]").toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = hubServiceClient.deleteHubCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteHubRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DeleteHubRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteHubOperationCallable()
    
    
    public final OperationCallable<DeleteHubRequest,Empty,OperationMetadata> deleteHubOperationCallable()

Deletes a Network Connectivity Center hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       DeleteHubRequest request =
           DeleteHubRequest.newBuilder()
               .setName(HubName.of("[PROJECT]", "[HUB]").toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           hubServiceClient.deleteHubOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteHubRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DeleteHubRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### deleteSpokeAsync(@Nullable SpokeName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteSpokeAsync(@Nullable SpokeName name)

Deletes a Network Connectivity Center spoke.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       SpokeName name = SpokeName.of("[PROJECT]", "[LOCATION]", "[SPOKE]");
       hubServiceClient.deleteSpokeAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.SpokeName`  
Required. The name of the spoke to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### deleteSpokeAsync(DeleteSpokeRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteSpokeAsync(DeleteSpokeRequest request)

Deletes a Network Connectivity Center spoke.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       DeleteSpokeRequest request =
           DeleteSpokeRequest.newBuilder()
               .setName(SpokeName.of("[PROJECT]", "[LOCATION]", "[SPOKE]").toString())
               .setRequestId("requestId693933066")
               .build();
       hubServiceClient.deleteSpokeAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteSpokeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DeleteSpokeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### deleteSpokeAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteSpokeAsync(String name)

Deletes a Network Connectivity Center spoke.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       String name = SpokeName.of("[PROJECT]", "[LOCATION]", "[SPOKE]").toString();
       hubServiceClient.deleteSpokeAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the spoke to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### deleteSpokeCallable()
    
    
    public final UnaryCallable<DeleteSpokeRequest,Operation> deleteSpokeCallable()

Deletes a Network Connectivity Center spoke.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       DeleteSpokeRequest request =
           DeleteSpokeRequest.newBuilder()
               .setName(SpokeName.of("[PROJECT]", "[LOCATION]", "[SPOKE]").toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = hubServiceClient.deleteSpokeCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteSpokeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DeleteSpokeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteSpokeOperationCallable()
    
    
    public final OperationCallable<DeleteSpokeRequest,Empty,OperationMetadata> deleteSpokeOperationCallable()

Deletes a Network Connectivity Center spoke.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       DeleteSpokeRequest request =
           DeleteSpokeRequest.newBuilder()
               .setName(SpokeName.of("[PROJECT]", "[LOCATION]", "[SPOKE]").toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           hubServiceClient.deleteSpokeOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteSpokeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DeleteSpokeRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### getGroup(@Nullable GroupName name)
    
    
    public final Group getGroup(@Nullable GroupName name)

Gets details about a Network Connectivity Center group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       GroupName name = GroupName.of("[PROJECT]", "[HUB]", "[GROUP]");
       Group response = hubServiceClient.getGroup(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.GroupName`  
Required. The name of the route table resource.  
**Returns**  
---  
**Type** | **Description**  
`[Group](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Group)` |   
  
### getGroup(GetGroupRequest request)
    
    
    public final Group getGroup(GetGroupRequest request)

Gets details about a Network Connectivity Center group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       GetGroupRequest request =
           GetGroupRequest.newBuilder()
               .setName(GroupName.of("[PROJECT]", "[HUB]", "[GROUP]").toString())
               .build();
       Group response = hubServiceClient.getGroup(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.GetGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Group](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Group)` |   
  
### getGroup(String name)
    
    
    public final Group getGroup(String name)

Gets details about a Network Connectivity Center group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       String name = GroupName.of("[PROJECT]", "[HUB]", "[GROUP]").toString();
       Group response = hubServiceClient.getGroup(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the route table resource.  
**Returns**  
---  
**Type** | **Description**  
`[Group](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Group)` |   
  
### getGroupCallable()
    
    
    public final UnaryCallable<GetGroupRequest,Group> getGroupCallable()

Gets details about a Network Connectivity Center group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       GetGroupRequest request =
           GetGroupRequest.newBuilder()
               .setName(GroupName.of("[PROJECT]", "[HUB]", "[GROUP]").toString())
               .build();
       ApiFuture<Group> future = hubServiceClient.getGroupCallable().futureCall(request);
       // Do something.
       Group response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.GetGroupRequest),[Group](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Group)>` |   
  
### getHub(@Nullable HubName name)
    
    
    public final Hub getHub(@Nullable HubName name)

Gets details about a Network Connectivity Center hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       HubName name = HubName.of("[PROJECT]", "[HUB]");
       Hub response = hubServiceClient.getHub(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.HubName`  
Required. The name of the hub resource to get.  
**Returns**  
---  
**Type** | **Description**  
`[Hub](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Hub)` |   
  
### getHub(GetHubRequest request)
    
    
    public final Hub getHub(GetHubRequest request)

Gets details about a Network Connectivity Center hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       GetHubRequest request =
           GetHubRequest.newBuilder().setName(HubName.of("[PROJECT]", "[HUB]").toString()).build();
       Hub response = hubServiceClient.getHub(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetHubRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.GetHubRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Hub](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Hub)` |   
  
### getHub(String name)
    
    
    public final Hub getHub(String name)

Gets details about a Network Connectivity Center hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       String name = HubName.of("[PROJECT]", "[HUB]").toString();
       Hub response = hubServiceClient.getHub(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the hub resource to get.  
**Returns**  
---  
**Type** | **Description**  
`[Hub](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Hub)` |   
  
### getHubCallable()
    
    
    public final UnaryCallable<GetHubRequest,Hub> getHubCallable()

Gets details about a Network Connectivity Center hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       GetHubRequest request =
           GetHubRequest.newBuilder().setName(HubName.of("[PROJECT]", "[HUB]").toString()).build();
       ApiFuture<Hub> future = hubServiceClient.getHubCallable().futureCall(request);
       // Do something.
       Hub response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetHubRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.GetHubRequest),[Hub](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Hub)>` |   
  
### getIamPolicy(GetIamPolicyRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRequest request)

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(GroupName.of("[PROJECT]", "[HUB]", "[GROUP]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = hubServiceClient.getIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.GetIamPolicyRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.Policy` |   
  
### getIamPolicyCallable()
    
    
    public final UnaryCallable<GetIamPolicyRequest,Policy> getIamPolicyCallable()

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(GroupName.of("[PROJECT]", "[HUB]", "[GROUP]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future = hubServiceClient.getIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.GetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = hubServiceClient.getLocation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.cloud.location.GetLocationRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.cloud.location.Location` |   
  
### getLocationCallable()
    
    
    public final UnaryCallable<GetLocationRequest,Location> getLocationCallable()

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = hubServiceClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getRoute(@Nullable HubRouteName name)
    
    
    public final Route getRoute(@Nullable HubRouteName name)

Gets details about the specified route.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       HubRouteName name = HubRouteName.of("[PROJECT]", "[HUB]", "[ROUTE_TABLE]", "[ROUTE]");
       Route response = hubServiceClient.getRoute(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.HubRouteName`  
Required. The name of the route resource.  
**Returns**  
---  
**Type** | **Description**  
`[Route](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Route)` |   
  
### getRoute(GetRouteRequest request)
    
    
    public final Route getRoute(GetRouteRequest request)

Gets details about the specified route.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       GetRouteRequest request =
           GetRouteRequest.newBuilder()
               .setName(HubRouteName.of("[PROJECT]", "[HUB]", "[ROUTE_TABLE]", "[ROUTE]").toString())
               .build();
       Route response = hubServiceClient.getRoute(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.GetRouteRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Route](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Route)` |   
  
### getRoute(String name)
    
    
    public final Route getRoute(String name)

Gets details about the specified route.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       String name = HubRouteName.of("[PROJECT]", "[HUB]", "[ROUTE_TABLE]", "[ROUTE]").toString();
       Route response = hubServiceClient.getRoute(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the route resource.  
**Returns**  
---  
**Type** | **Description**  
`[Route](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Route)` |   
  
### getRouteCallable()
    
    
    public final UnaryCallable<GetRouteRequest,Route> getRouteCallable()

Gets details about the specified route.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       GetRouteRequest request =
           GetRouteRequest.newBuilder()
               .setName(HubRouteName.of("[PROJECT]", "[HUB]", "[ROUTE_TABLE]", "[ROUTE]").toString())
               .build();
       ApiFuture<Route> future = hubServiceClient.getRouteCallable().futureCall(request);
       // Do something.
       Route response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.GetRouteRequest),[Route](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Route)>` |   
  
### getRouteTable(@Nullable RouteTableName name)
    
    
    public final RouteTable getRouteTable(@Nullable RouteTableName name)

Gets details about a Network Connectivity Center route table.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       RouteTableName name = RouteTableName.of("[PROJECT]", "[HUB]", "[ROUTE_TABLE]");
       RouteTable response = hubServiceClient.getRouteTable(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.RouteTableName`  
Required. The name of the route table resource.  
**Returns**  
---  
**Type** | **Description**  
`[RouteTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.RouteTable)` |   
  
### getRouteTable(GetRouteTableRequest request)
    
    
    public final RouteTable getRouteTable(GetRouteTableRequest request)

Gets details about a Network Connectivity Center route table.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       GetRouteTableRequest request =
           GetRouteTableRequest.newBuilder()
               .setName(RouteTableName.of("[PROJECT]", "[HUB]", "[ROUTE_TABLE]").toString())
               .build();
       RouteTable response = hubServiceClient.getRouteTable(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRouteTableRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.GetRouteTableRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RouteTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.RouteTable)` |   
  
### getRouteTable(String name)
    
    
    public final RouteTable getRouteTable(String name)

Gets details about a Network Connectivity Center route table.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       String name = RouteTableName.of("[PROJECT]", "[HUB]", "[ROUTE_TABLE]").toString();
       RouteTable response = hubServiceClient.getRouteTable(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the route table resource.  
**Returns**  
---  
**Type** | **Description**  
`[RouteTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.RouteTable)` |   
  
### getRouteTableCallable()
    
    
    public final UnaryCallable<GetRouteTableRequest,RouteTable> getRouteTableCallable()

Gets details about a Network Connectivity Center route table.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       GetRouteTableRequest request =
           GetRouteTableRequest.newBuilder()
               .setName(RouteTableName.of("[PROJECT]", "[HUB]", "[ROUTE_TABLE]").toString())
               .build();
       ApiFuture<RouteTable> future = hubServiceClient.getRouteTableCallable().futureCall(request);
       // Do something.
       RouteTable response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetRouteTableRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.GetRouteTableRequest),[RouteTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.RouteTable)>` |   
  
### getSettings()
    
    
    public final @Nullable HubServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.HubServiceSettings` |   
  
### getSpoke(@Nullable SpokeName name)
    
    
    public final Spoke getSpoke(@Nullable SpokeName name)

Gets details about a Network Connectivity Center spoke.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       SpokeName name = SpokeName.of("[PROJECT]", "[LOCATION]", "[SPOKE]");
       Spoke response = hubServiceClient.getSpoke(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.SpokeName`  
Required. The name of the spoke resource.  
**Returns**  
---  
**Type** | **Description**  
`[Spoke](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Spoke)` |   
  
### getSpoke(GetSpokeRequest request)
    
    
    public final Spoke getSpoke(GetSpokeRequest request)

Gets details about a Network Connectivity Center spoke.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       GetSpokeRequest request =
           GetSpokeRequest.newBuilder()
               .setName(SpokeName.of("[PROJECT]", "[LOCATION]", "[SPOKE]").toString())
               .build();
       Spoke response = hubServiceClient.getSpoke(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSpokeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.GetSpokeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Spoke](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Spoke)` |   
  
### getSpoke(String name)
    
    
    public final Spoke getSpoke(String name)

Gets details about a Network Connectivity Center spoke.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       String name = SpokeName.of("[PROJECT]", "[LOCATION]", "[SPOKE]").toString();
       Spoke response = hubServiceClient.getSpoke(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the spoke resource.  
**Returns**  
---  
**Type** | **Description**  
`[Spoke](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Spoke)` |   
  
### getSpokeCallable()
    
    
    public final UnaryCallable<GetSpokeRequest,Spoke> getSpokeCallable()

Gets details about a Network Connectivity Center spoke.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       GetSpokeRequest request =
           GetSpokeRequest.newBuilder()
               .setName(SpokeName.of("[PROJECT]", "[LOCATION]", "[SPOKE]").toString())
               .build();
       ApiFuture<Spoke> future = hubServiceClient.getSpokeCallable().futureCall(request);
       // Do something.
       Spoke response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetSpokeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.GetSpokeRequest),[Spoke](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Spoke)>` |   
  
### getStub()
    
    
    public HubServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[HubServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.stub.HubServiceStub)` |   
  
### isShutdown()
    
    
    public boolean isShutdown()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### isTerminated()
    
    
    public boolean isTerminated()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### listGroups(@Nullable HubName parent)
    
    
    public final HubServiceClient.ListGroupsPagedResponse listGroups(@Nullable HubName parent)

Lists groups in a given hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       HubName parent = HubName.of("[PROJECT]", "[HUB]");
       for (Group element : hubServiceClient.listGroups(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.HubName`  
Required. The parent resource's name.  
**Returns**  
---  
**Type** | **Description**  
`[HubServiceClient.ListGroupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceClient.ListGroupsPagedResponse)` |   
  
### listGroups(ListGroupsRequest request)
    
    
    public final HubServiceClient.ListGroupsPagedResponse listGroups(ListGroupsRequest request)

Lists groups in a given hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       ListGroupsRequest request =
           ListGroupsRequest.newBuilder()
               .setParent(HubName.of("[PROJECT]", "[HUB]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Group element : hubServiceClient.listGroups(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListGroupsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[HubServiceClient.ListGroupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceClient.ListGroupsPagedResponse)` |   
  
### listGroups(String parent)
    
    
    public final HubServiceClient.ListGroupsPagedResponse listGroups(String parent)

Lists groups in a given hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       String parent = HubName.of("[PROJECT]", "[HUB]").toString();
       for (Group element : hubServiceClient.listGroups(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource's name.  
**Returns**  
---  
**Type** | **Description**  
`[HubServiceClient.ListGroupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceClient.ListGroupsPagedResponse)` |   
  
### listGroupsCallable()
    
    
    public final UnaryCallable<ListGroupsRequest,ListGroupsResponse> listGroupsCallable()

Lists groups in a given hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       ListGroupsRequest request =
           ListGroupsRequest.newBuilder()
               .setParent(HubName.of("[PROJECT]", "[HUB]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListGroupsResponse response = hubServiceClient.listGroupsCallable().call(request);
         for (Group element : response.getGroupsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListGroupsRequest),[ListGroupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListGroupsResponse)>` |   
  
### listGroupsPagedCallable()
    
    
    public final UnaryCallable<ListGroupsRequest,HubServiceClient.ListGroupsPagedResponse> listGroupsPagedCallable()

Lists groups in a given hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       ListGroupsRequest request =
           ListGroupsRequest.newBuilder()
               .setParent(HubName.of("[PROJECT]", "[HUB]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Group> future = hubServiceClient.listGroupsPagedCallable().futureCall(request);
       // Do something.
       for (Group element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListGroupsRequest),[ListGroupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceClient.ListGroupsPagedResponse)>` |   
  
### listHubSpokes(@Nullable HubName name)
    
    
    public final HubServiceClient.ListHubSpokesPagedResponse listHubSpokes(@Nullable HubName name)

Lists the Network Connectivity Center spokes associated with a specified hub and location. The list includes both spokes that are attached to the hub and spokes that have been proposed but not yet accepted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       HubName name = HubName.of("[PROJECT]", "[HUB]");
       for (Spoke element : hubServiceClient.listHubSpokes(name).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.HubName`  
Required. The name of the hub.  
**Returns**  
---  
**Type** | **Description**  
`[HubServiceClient.ListHubSpokesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceClient.ListHubSpokesPagedResponse)` |   
  
### listHubSpokes(ListHubSpokesRequest request)
    
    
    public final HubServiceClient.ListHubSpokesPagedResponse listHubSpokes(ListHubSpokesRequest request)

Lists the Network Connectivity Center spokes associated with a specified hub and location. The list includes both spokes that are attached to the hub and spokes that have been proposed but not yet accepted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       ListHubSpokesRequest request =
           ListHubSpokesRequest.newBuilder()
               .setName(HubName.of("[PROJECT]", "[HUB]").toString())
               .addAllSpokeLocations(new ArrayList<String>())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Spoke element : hubServiceClient.listHubSpokes(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListHubSpokesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListHubSpokesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[HubServiceClient.ListHubSpokesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceClient.ListHubSpokesPagedResponse)` |   
  
### listHubSpokes(String name)
    
    
    public final HubServiceClient.ListHubSpokesPagedResponse listHubSpokes(String name)

Lists the Network Connectivity Center spokes associated with a specified hub and location. The list includes both spokes that are attached to the hub and spokes that have been proposed but not yet accepted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       String name = HubName.of("[PROJECT]", "[HUB]").toString();
       for (Spoke element : hubServiceClient.listHubSpokes(name).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the hub.  
**Returns**  
---  
**Type** | **Description**  
`[HubServiceClient.ListHubSpokesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceClient.ListHubSpokesPagedResponse)` |   
  
### listHubSpokesCallable()
    
    
    public final UnaryCallable<ListHubSpokesRequest,ListHubSpokesResponse> listHubSpokesCallable()

Lists the Network Connectivity Center spokes associated with a specified hub and location. The list includes both spokes that are attached to the hub and spokes that have been proposed but not yet accepted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       ListHubSpokesRequest request =
           ListHubSpokesRequest.newBuilder()
               .setName(HubName.of("[PROJECT]", "[HUB]").toString())
               .addAllSpokeLocations(new ArrayList<String>())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListHubSpokesResponse response = hubServiceClient.listHubSpokesCallable().call(request);
         for (Spoke element : response.getSpokesList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListHubSpokesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListHubSpokesRequest),[ListHubSpokesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListHubSpokesResponse)>` |   
  
### listHubSpokesPagedCallable()
    
    
    public final UnaryCallable<ListHubSpokesRequest,HubServiceClient.ListHubSpokesPagedResponse> listHubSpokesPagedCallable()

Lists the Network Connectivity Center spokes associated with a specified hub and location. The list includes both spokes that are attached to the hub and spokes that have been proposed but not yet accepted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       ListHubSpokesRequest request =
           ListHubSpokesRequest.newBuilder()
               .setName(HubName.of("[PROJECT]", "[HUB]").toString())
               .addAllSpokeLocations(new ArrayList<String>())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Spoke> future = hubServiceClient.listHubSpokesPagedCallable().futureCall(request);
       // Do something.
       for (Spoke element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListHubSpokesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListHubSpokesRequest),[ListHubSpokesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceClient.ListHubSpokesPagedResponse)>` |   
  
### listHubs(@Nullable LocationName parent)
    
    
    public final HubServiceClient.ListHubsPagedResponse listHubs(@Nullable LocationName parent)

Lists the Network Connectivity Center hubs associated with a given project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Hub element : hubServiceClient.listHubs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.LocationName`  
Required. The parent resource's name.  
**Returns**  
---  
**Type** | **Description**  
`[HubServiceClient.ListHubsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceClient.ListHubsPagedResponse)` |   
  
### listHubs(ListHubsRequest request)
    
    
    public final HubServiceClient.ListHubsPagedResponse listHubs(ListHubsRequest request)

Lists the Network Connectivity Center hubs associated with a given project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       ListHubsRequest request =
           ListHubsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Hub element : hubServiceClient.listHubs(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListHubsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListHubsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[HubServiceClient.ListHubsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceClient.ListHubsPagedResponse)` |   
  
### listHubs(String parent)
    
    
    public final HubServiceClient.ListHubsPagedResponse listHubs(String parent)

Lists the Network Connectivity Center hubs associated with a given project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Hub element : hubServiceClient.listHubs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource's name.  
**Returns**  
---  
**Type** | **Description**  
`[HubServiceClient.ListHubsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceClient.ListHubsPagedResponse)` |   
  
### listHubsCallable()
    
    
    public final UnaryCallable<ListHubsRequest,ListHubsResponse> listHubsCallable()

Lists the Network Connectivity Center hubs associated with a given project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       ListHubsRequest request =
           ListHubsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListHubsResponse response = hubServiceClient.listHubsCallable().call(request);
         for (Hub element : response.getHubsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListHubsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListHubsRequest),[ListHubsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListHubsResponse)>` |   
  
### listHubsPagedCallable()
    
    
    public final UnaryCallable<ListHubsRequest,HubServiceClient.ListHubsPagedResponse> listHubsPagedCallable()

Lists the Network Connectivity Center hubs associated with a given project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       ListHubsRequest request =
           ListHubsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Hub> future = hubServiceClient.listHubsPagedCallable().futureCall(request);
       // Do something.
       for (Hub element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListHubsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListHubsRequest),[ListHubsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceClient.ListHubsPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final HubServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : hubServiceClient.listLocations(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.cloud.location.ListLocationsRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[HubServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response = hubServiceClient.listLocationsCallable().call(request);
         for (Location element : response.getLocationsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse>` |   
  
### listLocationsPagedCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,HubServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           hubServiceClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceClient.ListLocationsPagedResponse)>` |   
  
### listRouteTables(@Nullable HubName parent)
    
    
    public final HubServiceClient.ListRouteTablesPagedResponse listRouteTables(@Nullable HubName parent)

Lists route tables in a given hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       HubName parent = HubName.of("[PROJECT]", "[HUB]");
       for (RouteTable element : hubServiceClient.listRouteTables(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.HubName`  
Required. The parent resource's name.  
**Returns**  
---  
**Type** | **Description**  
`[HubServiceClient.ListRouteTablesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceClient.ListRouteTablesPagedResponse)` |   
  
### listRouteTables(ListRouteTablesRequest request)
    
    
    public final HubServiceClient.ListRouteTablesPagedResponse listRouteTables(ListRouteTablesRequest request)

Lists route tables in a given hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       ListRouteTablesRequest request =
           ListRouteTablesRequest.newBuilder()
               .setParent(HubName.of("[PROJECT]", "[HUB]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (RouteTable element : hubServiceClient.listRouteTables(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListRouteTablesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListRouteTablesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[HubServiceClient.ListRouteTablesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceClient.ListRouteTablesPagedResponse)` |   
  
### listRouteTables(String parent)
    
    
    public final HubServiceClient.ListRouteTablesPagedResponse listRouteTables(String parent)

Lists route tables in a given hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       String parent = HubName.of("[PROJECT]", "[HUB]").toString();
       for (RouteTable element : hubServiceClient.listRouteTables(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource's name.  
**Returns**  
---  
**Type** | **Description**  
`[HubServiceClient.ListRouteTablesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceClient.ListRouteTablesPagedResponse)` |   
  
### listRouteTablesCallable()
    
    
    public final UnaryCallable<ListRouteTablesRequest,ListRouteTablesResponse> listRouteTablesCallable()

Lists route tables in a given hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       ListRouteTablesRequest request =
           ListRouteTablesRequest.newBuilder()
               .setParent(HubName.of("[PROJECT]", "[HUB]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListRouteTablesResponse response = hubServiceClient.listRouteTablesCallable().call(request);
         for (RouteTable element : response.getRouteTablesList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRouteTablesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListRouteTablesRequest),[ListRouteTablesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListRouteTablesResponse)>` |   
  
### listRouteTablesPagedCallable()
    
    
    public final UnaryCallable<ListRouteTablesRequest,HubServiceClient.ListRouteTablesPagedResponse> listRouteTablesPagedCallable()

Lists route tables in a given hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       ListRouteTablesRequest request =
           ListRouteTablesRequest.newBuilder()
               .setParent(HubName.of("[PROJECT]", "[HUB]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<RouteTable> future =
           hubServiceClient.listRouteTablesPagedCallable().futureCall(request);
       // Do something.
       for (RouteTable element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRouteTablesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListRouteTablesRequest),[ListRouteTablesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceClient.ListRouteTablesPagedResponse)>` |   
  
### listRoutes(@Nullable RouteTableName parent)
    
    
    public final HubServiceClient.ListRoutesPagedResponse listRoutes(@Nullable RouteTableName parent)

Lists routes in a given route table.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       RouteTableName parent = RouteTableName.of("[PROJECT]", "[HUB]", "[ROUTE_TABLE]");
       for (Route element : hubServiceClient.listRoutes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.RouteTableName`  
Required. The parent resource's name.  
**Returns**  
---  
**Type** | **Description**  
`[HubServiceClient.ListRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceClient.ListRoutesPagedResponse)` |   
  
### listRoutes(ListRoutesRequest request)
    
    
    public final HubServiceClient.ListRoutesPagedResponse listRoutes(ListRoutesRequest request)

Lists routes in a given route table.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       ListRoutesRequest request =
           ListRoutesRequest.newBuilder()
               .setParent(RouteTableName.of("[PROJECT]", "[HUB]", "[ROUTE_TABLE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Route element : hubServiceClient.listRoutes(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListRoutesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[HubServiceClient.ListRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceClient.ListRoutesPagedResponse)` |   
  
### listRoutes(String parent)
    
    
    public final HubServiceClient.ListRoutesPagedResponse listRoutes(String parent)

Lists routes in a given route table.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       String parent = RouteTableName.of("[PROJECT]", "[HUB]", "[ROUTE_TABLE]").toString();
       for (Route element : hubServiceClient.listRoutes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource's name.  
**Returns**  
---  
**Type** | **Description**  
`[HubServiceClient.ListRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceClient.ListRoutesPagedResponse)` |   
  
### listRoutesCallable()
    
    
    public final UnaryCallable<ListRoutesRequest,ListRoutesResponse> listRoutesCallable()

Lists routes in a given route table.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       ListRoutesRequest request =
           ListRoutesRequest.newBuilder()
               .setParent(RouteTableName.of("[PROJECT]", "[HUB]", "[ROUTE_TABLE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListRoutesResponse response = hubServiceClient.listRoutesCallable().call(request);
         for (Route element : response.getRoutesList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListRoutesRequest),[ListRoutesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListRoutesResponse)>` |   
  
### listRoutesPagedCallable()
    
    
    public final UnaryCallable<ListRoutesRequest,HubServiceClient.ListRoutesPagedResponse> listRoutesPagedCallable()

Lists routes in a given route table.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       ListRoutesRequest request =
           ListRoutesRequest.newBuilder()
               .setParent(RouteTableName.of("[PROJECT]", "[HUB]", "[ROUTE_TABLE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Route> future = hubServiceClient.listRoutesPagedCallable().futureCall(request);
       // Do something.
       for (Route element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListRoutesRequest),[ListRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceClient.ListRoutesPagedResponse)>` |   
  
### listSpokes(@Nullable LocationName parent)
    
    
    public final HubServiceClient.ListSpokesPagedResponse listSpokes(@Nullable LocationName parent)

Lists the Network Connectivity Center spokes in a specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Spoke element : hubServiceClient.listSpokes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.LocationName`  
Required. The parent resource.  
**Returns**  
---  
**Type** | **Description**  
`[HubServiceClient.ListSpokesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceClient.ListSpokesPagedResponse)` |   
  
### listSpokes(ListSpokesRequest request)
    
    
    public final HubServiceClient.ListSpokesPagedResponse listSpokes(ListSpokesRequest request)

Lists the Network Connectivity Center spokes in a specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       ListSpokesRequest request =
           ListSpokesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Spoke element : hubServiceClient.listSpokes(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListSpokesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListSpokesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[HubServiceClient.ListSpokesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceClient.ListSpokesPagedResponse)` |   
  
### listSpokes(String parent)
    
    
    public final HubServiceClient.ListSpokesPagedResponse listSpokes(String parent)

Lists the Network Connectivity Center spokes in a specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Spoke element : hubServiceClient.listSpokes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource.  
**Returns**  
---  
**Type** | **Description**  
`[HubServiceClient.ListSpokesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceClient.ListSpokesPagedResponse)` |   
  
### listSpokesCallable()
    
    
    public final UnaryCallable<ListSpokesRequest,ListSpokesResponse> listSpokesCallable()

Lists the Network Connectivity Center spokes in a specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       ListSpokesRequest request =
           ListSpokesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListSpokesResponse response = hubServiceClient.listSpokesCallable().call(request);
         for (Spoke element : response.getSpokesList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSpokesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListSpokesRequest),[ListSpokesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListSpokesResponse)>` |   
  
### listSpokesPagedCallable()
    
    
    public final UnaryCallable<ListSpokesRequest,HubServiceClient.ListSpokesPagedResponse> listSpokesPagedCallable()

Lists the Network Connectivity Center spokes in a specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       ListSpokesRequest request =
           ListSpokesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Spoke> future = hubServiceClient.listSpokesPagedCallable().futureCall(request);
       // Do something.
       for (Spoke element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSpokesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListSpokesRequest),[ListSpokesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceClient.ListSpokesPagedResponse)>` |   
  
### queryHubStatus(@Nullable HubName name)
    
    
    public final HubServiceClient.QueryHubStatusPagedResponse queryHubStatus(@Nullable HubName name)

Query the Private Service Connect propagation status of a Network Connectivity Center hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       HubName name = HubName.of("[PROJECT]", "[HUB]");
       for (HubStatusEntry element : hubServiceClient.queryHubStatus(name).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.HubName`  
Required. The name of the hub.  
**Returns**  
---  
**Type** | **Description**  
`[HubServiceClient.QueryHubStatusPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceClient.QueryHubStatusPagedResponse)` |   
  
### queryHubStatus(QueryHubStatusRequest request)
    
    
    public final HubServiceClient.QueryHubStatusPagedResponse queryHubStatus(QueryHubStatusRequest request)

Query the Private Service Connect propagation status of a Network Connectivity Center hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       QueryHubStatusRequest request =
           QueryHubStatusRequest.newBuilder()
               .setName(HubName.of("[PROJECT]", "[HUB]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setGroupBy("groupBy293428022")
               .build();
       for (HubStatusEntry element : hubServiceClient.queryHubStatus(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[QueryHubStatusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.QueryHubStatusRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[HubServiceClient.QueryHubStatusPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceClient.QueryHubStatusPagedResponse)` |   
  
### queryHubStatus(String name)
    
    
    public final HubServiceClient.QueryHubStatusPagedResponse queryHubStatus(String name)

Query the Private Service Connect propagation status of a Network Connectivity Center hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       String name = HubName.of("[PROJECT]", "[HUB]").toString();
       for (HubStatusEntry element : hubServiceClient.queryHubStatus(name).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the hub.  
**Returns**  
---  
**Type** | **Description**  
`[HubServiceClient.QueryHubStatusPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceClient.QueryHubStatusPagedResponse)` |   
  
### queryHubStatusCallable()
    
    
    public final UnaryCallable<QueryHubStatusRequest,QueryHubStatusResponse> queryHubStatusCallable()

Query the Private Service Connect propagation status of a Network Connectivity Center hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       QueryHubStatusRequest request =
           QueryHubStatusRequest.newBuilder()
               .setName(HubName.of("[PROJECT]", "[HUB]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setGroupBy("groupBy293428022")
               .build();
       while (true) {
         QueryHubStatusResponse response = hubServiceClient.queryHubStatusCallable().call(request);
         for (HubStatusEntry element : response.getHubStatusEntriesList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[QueryHubStatusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.QueryHubStatusRequest),[QueryHubStatusResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.QueryHubStatusResponse)>` |   
  
### queryHubStatusPagedCallable()
    
    
    public final UnaryCallable<QueryHubStatusRequest,HubServiceClient.QueryHubStatusPagedResponse> queryHubStatusPagedCallable()

Query the Private Service Connect propagation status of a Network Connectivity Center hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       QueryHubStatusRequest request =
           QueryHubStatusRequest.newBuilder()
               .setName(HubName.of("[PROJECT]", "[HUB]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setGroupBy("groupBy293428022")
               .build();
       ApiFuture<HubStatusEntry> future =
           hubServiceClient.queryHubStatusPagedCallable().futureCall(request);
       // Do something.
       for (HubStatusEntry element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[QueryHubStatusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.QueryHubStatusRequest),[QueryHubStatusPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceClient.QueryHubStatusPagedResponse)>` |   
  
### rejectHubSpokeAsync(@Nullable HubName name, @Nullable SpokeName spokeUri)
    
    
    public final OperationFuture<RejectHubSpokeResponse,OperationMetadata> rejectHubSpokeAsync(@Nullable HubName name, @Nullable SpokeName spokeUri)

Rejects a Network Connectivity Center spoke from being attached to a hub. If the spoke was previously in the `ACTIVE` state, it transitions to the `INACTIVE` state and is no longer able to connect to other spokes that are attached to the hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       HubName name = HubName.of("[PROJECT]", "[HUB]");
       SpokeName spokeUri = SpokeName.of("[PROJECT]", "[LOCATION]", "[SPOKE]");
       RejectHubSpokeResponse response = hubServiceClient.rejectHubSpokeAsync(name, spokeUri).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.HubName`  
Required. The name of the hub from which to reject the spoke.  
`spokeUri` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.SpokeName`  
Required. The URI of the spoke to reject from the hub.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[RejectHubSpokeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.RejectHubSpokeResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### rejectHubSpokeAsync(@Nullable HubName name, String spokeUri)
    
    
    public final OperationFuture<RejectHubSpokeResponse,OperationMetadata> rejectHubSpokeAsync(@Nullable HubName name, String spokeUri)

Rejects a Network Connectivity Center spoke from being attached to a hub. If the spoke was previously in the `ACTIVE` state, it transitions to the `INACTIVE` state and is no longer able to connect to other spokes that are attached to the hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       HubName name = HubName.of("[PROJECT]", "[HUB]");
       String spokeUri = SpokeName.of("[PROJECT]", "[LOCATION]", "[SPOKE]").toString();
       RejectHubSpokeResponse response = hubServiceClient.rejectHubSpokeAsync(name, spokeUri).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.HubName`  
Required. The name of the hub from which to reject the spoke.  
`spokeUri` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The URI of the spoke to reject from the hub.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[RejectHubSpokeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.RejectHubSpokeResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### rejectHubSpokeAsync(RejectHubSpokeRequest request)
    
    
    public final OperationFuture<RejectHubSpokeResponse,OperationMetadata> rejectHubSpokeAsync(RejectHubSpokeRequest request)

Rejects a Network Connectivity Center spoke from being attached to a hub. If the spoke was previously in the `ACTIVE` state, it transitions to the `INACTIVE` state and is no longer able to connect to other spokes that are attached to the hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       RejectHubSpokeRequest request =
           RejectHubSpokeRequest.newBuilder()
               .setName(HubName.of("[PROJECT]", "[HUB]").toString())
               .setSpokeUri(SpokeName.of("[PROJECT]", "[LOCATION]", "[SPOKE]").toString())
               .setRequestId("requestId693933066")
               .setDetails("details1557721666")
               .build();
       RejectHubSpokeResponse response = hubServiceClient.rejectHubSpokeAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RejectHubSpokeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.RejectHubSpokeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[RejectHubSpokeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.RejectHubSpokeResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### rejectHubSpokeAsync(String name, @Nullable SpokeName spokeUri)
    
    
    public final OperationFuture<RejectHubSpokeResponse,OperationMetadata> rejectHubSpokeAsync(String name, @Nullable SpokeName spokeUri)

Rejects a Network Connectivity Center spoke from being attached to a hub. If the spoke was previously in the `ACTIVE` state, it transitions to the `INACTIVE` state and is no longer able to connect to other spokes that are attached to the hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       String name = HubName.of("[PROJECT]", "[HUB]").toString();
       SpokeName spokeUri = SpokeName.of("[PROJECT]", "[LOCATION]", "[SPOKE]");
       RejectHubSpokeResponse response = hubServiceClient.rejectHubSpokeAsync(name, spokeUri).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the hub from which to reject the spoke.  
`spokeUri` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.SpokeName`  
Required. The URI of the spoke to reject from the hub.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[RejectHubSpokeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.RejectHubSpokeResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### rejectHubSpokeAsync(String name, String spokeUri)
    
    
    public final OperationFuture<RejectHubSpokeResponse,OperationMetadata> rejectHubSpokeAsync(String name, String spokeUri)

Rejects a Network Connectivity Center spoke from being attached to a hub. If the spoke was previously in the `ACTIVE` state, it transitions to the `INACTIVE` state and is no longer able to connect to other spokes that are attached to the hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       String name = HubName.of("[PROJECT]", "[HUB]").toString();
       String spokeUri = SpokeName.of("[PROJECT]", "[LOCATION]", "[SPOKE]").toString();
       RejectHubSpokeResponse response = hubServiceClient.rejectHubSpokeAsync(name, spokeUri).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the hub from which to reject the spoke.  
`spokeUri` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The URI of the spoke to reject from the hub.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[RejectHubSpokeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.RejectHubSpokeResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### rejectHubSpokeCallable()
    
    
    public final UnaryCallable<RejectHubSpokeRequest,Operation> rejectHubSpokeCallable()

Rejects a Network Connectivity Center spoke from being attached to a hub. If the spoke was previously in the `ACTIVE` state, it transitions to the `INACTIVE` state and is no longer able to connect to other spokes that are attached to the hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       RejectHubSpokeRequest request =
           RejectHubSpokeRequest.newBuilder()
               .setName(HubName.of("[PROJECT]", "[HUB]").toString())
               .setSpokeUri(SpokeName.of("[PROJECT]", "[LOCATION]", "[SPOKE]").toString())
               .setRequestId("requestId693933066")
               .setDetails("details1557721666")
               .build();
       ApiFuture<Operation> future = hubServiceClient.rejectHubSpokeCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RejectHubSpokeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.RejectHubSpokeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### rejectHubSpokeOperationCallable()
    
    
    public final OperationCallable<RejectHubSpokeRequest,RejectHubSpokeResponse,OperationMetadata> rejectHubSpokeOperationCallable()

Rejects a Network Connectivity Center spoke from being attached to a hub. If the spoke was previously in the `ACTIVE` state, it transitions to the `INACTIVE` state and is no longer able to connect to other spokes that are attached to the hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       RejectHubSpokeRequest request =
           RejectHubSpokeRequest.newBuilder()
               .setName(HubName.of("[PROJECT]", "[HUB]").toString())
               .setSpokeUri(SpokeName.of("[PROJECT]", "[LOCATION]", "[SPOKE]").toString())
               .setRequestId("requestId693933066")
               .setDetails("details1557721666")
               .build();
       OperationFuture<RejectHubSpokeResponse, OperationMetadata> future =
           hubServiceClient.rejectHubSpokeOperationCallable().futureCall(request);
       // Do something.
       RejectHubSpokeResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RejectHubSpokeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.RejectHubSpokeRequest),[RejectHubSpokeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.RejectHubSpokeResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### rejectSpokeUpdateAsync(@Nullable HubName name, @Nullable SpokeName spokeUri, String spokeEtag)
    
    
    public final OperationFuture<RejectSpokeUpdateResponse,OperationMetadata> rejectSpokeUpdateAsync(@Nullable HubName name, @Nullable SpokeName spokeUri, String spokeEtag)

Rejects a proposal to update a Network Connectivity Center spoke in a hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       HubName name = HubName.of("[PROJECT]", "[HUB]");
       SpokeName spokeUri = SpokeName.of("[PROJECT]", "[LOCATION]", "[SPOKE]");
       String spokeEtag = "spokeEtag-1185145407";
       RejectSpokeUpdateResponse response =
           hubServiceClient.rejectSpokeUpdateAsync(name, spokeUri, spokeEtag).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.HubName`  
Required. The name of the hub to reject spoke update.  
`spokeUri` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.SpokeName`  
Required. The URI of the spoke to reject update.  
`spokeEtag` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The etag of the spoke to reject update.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[RejectSpokeUpdateResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.RejectSpokeUpdateResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### rejectSpokeUpdateAsync(@Nullable HubName name, String spokeUri, String spokeEtag)
    
    
    public final OperationFuture<RejectSpokeUpdateResponse,OperationMetadata> rejectSpokeUpdateAsync(@Nullable HubName name, String spokeUri, String spokeEtag)

Rejects a proposal to update a Network Connectivity Center spoke in a hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       HubName name = HubName.of("[PROJECT]", "[HUB]");
       String spokeUri = SpokeName.of("[PROJECT]", "[LOCATION]", "[SPOKE]").toString();
       String spokeEtag = "spokeEtag-1185145407";
       RejectSpokeUpdateResponse response =
           hubServiceClient.rejectSpokeUpdateAsync(name, spokeUri, spokeEtag).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.HubName`  
Required. The name of the hub to reject spoke update.  
`spokeUri` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The URI of the spoke to reject update.  
`spokeEtag` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The etag of the spoke to reject update.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[RejectSpokeUpdateResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.RejectSpokeUpdateResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### rejectSpokeUpdateAsync(RejectSpokeUpdateRequest request)
    
    
    public final OperationFuture<RejectSpokeUpdateResponse,OperationMetadata> rejectSpokeUpdateAsync(RejectSpokeUpdateRequest request)

Rejects a proposal to update a Network Connectivity Center spoke in a hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       RejectSpokeUpdateRequest request =
           RejectSpokeUpdateRequest.newBuilder()
               .setName(HubName.of("[PROJECT]", "[HUB]").toString())
               .setSpokeUri(SpokeName.of("[PROJECT]", "[LOCATION]", "[SPOKE]").toString())
               .setSpokeEtag("spokeEtag-1185145407")
               .setDetails("details1557721666")
               .setRequestId("requestId693933066")
               .build();
       RejectSpokeUpdateResponse response = hubServiceClient.rejectSpokeUpdateAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RejectSpokeUpdateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.RejectSpokeUpdateRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[RejectSpokeUpdateResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.RejectSpokeUpdateResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### rejectSpokeUpdateAsync(String name, @Nullable SpokeName spokeUri, String spokeEtag)
    
    
    public final OperationFuture<RejectSpokeUpdateResponse,OperationMetadata> rejectSpokeUpdateAsync(String name, @Nullable SpokeName spokeUri, String spokeEtag)

Rejects a proposal to update a Network Connectivity Center spoke in a hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       String name = HubName.of("[PROJECT]", "[HUB]").toString();
       SpokeName spokeUri = SpokeName.of("[PROJECT]", "[LOCATION]", "[SPOKE]");
       String spokeEtag = "spokeEtag-1185145407";
       RejectSpokeUpdateResponse response =
           hubServiceClient.rejectSpokeUpdateAsync(name, spokeUri, spokeEtag).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the hub to reject spoke update.  
`spokeUri` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.SpokeName`  
Required. The URI of the spoke to reject update.  
`spokeEtag` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The etag of the spoke to reject update.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[RejectSpokeUpdateResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.RejectSpokeUpdateResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### rejectSpokeUpdateAsync(String name, String spokeUri, String spokeEtag)
    
    
    public final OperationFuture<RejectSpokeUpdateResponse,OperationMetadata> rejectSpokeUpdateAsync(String name, String spokeUri, String spokeEtag)

Rejects a proposal to update a Network Connectivity Center spoke in a hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       String name = HubName.of("[PROJECT]", "[HUB]").toString();
       String spokeUri = SpokeName.of("[PROJECT]", "[LOCATION]", "[SPOKE]").toString();
       String spokeEtag = "spokeEtag-1185145407";
       RejectSpokeUpdateResponse response =
           hubServiceClient.rejectSpokeUpdateAsync(name, spokeUri, spokeEtag).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the hub to reject spoke update.  
`spokeUri` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The URI of the spoke to reject update.  
`spokeEtag` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The etag of the spoke to reject update.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[RejectSpokeUpdateResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.RejectSpokeUpdateResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### rejectSpokeUpdateCallable()
    
    
    public final UnaryCallable<RejectSpokeUpdateRequest,Operation> rejectSpokeUpdateCallable()

Rejects a proposal to update a Network Connectivity Center spoke in a hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       RejectSpokeUpdateRequest request =
           RejectSpokeUpdateRequest.newBuilder()
               .setName(HubName.of("[PROJECT]", "[HUB]").toString())
               .setSpokeUri(SpokeName.of("[PROJECT]", "[LOCATION]", "[SPOKE]").toString())
               .setSpokeEtag("spokeEtag-1185145407")
               .setDetails("details1557721666")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           hubServiceClient.rejectSpokeUpdateCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RejectSpokeUpdateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.RejectSpokeUpdateRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### rejectSpokeUpdateOperationCallable()
    
    
    public final OperationCallable<RejectSpokeUpdateRequest,RejectSpokeUpdateResponse,OperationMetadata> rejectSpokeUpdateOperationCallable()

Rejects a proposal to update a Network Connectivity Center spoke in a hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       RejectSpokeUpdateRequest request =
           RejectSpokeUpdateRequest.newBuilder()
               .setName(HubName.of("[PROJECT]", "[HUB]").toString())
               .setSpokeUri(SpokeName.of("[PROJECT]", "[LOCATION]", "[SPOKE]").toString())
               .setSpokeEtag("spokeEtag-1185145407")
               .setDetails("details1557721666")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<RejectSpokeUpdateResponse, OperationMetadata> future =
           hubServiceClient.rejectSpokeUpdateOperationCallable().futureCall(request);
       // Do something.
       RejectSpokeUpdateResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RejectSpokeUpdateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.RejectSpokeUpdateRequest),[RejectSpokeUpdateResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.RejectSpokeUpdateResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### setIamPolicy(SetIamPolicyRequest request)
    
    
    public final Policy setIamPolicy(SetIamPolicyRequest request)

Sets the access control policy on the specified resource. Replacesany existing policy.

Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED`errors.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(GroupName.of("[PROJECT]", "[HUB]", "[GROUP]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = hubServiceClient.setIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.SetIamPolicyRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.Policy` |   
  
### setIamPolicyCallable()
    
    
    public final UnaryCallable<SetIamPolicyRequest,Policy> setIamPolicyCallable()

Sets the access control policy on the specified resource. Replacesany existing policy.

Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED`errors.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(GroupName.of("[PROJECT]", "[HUB]", "[GROUP]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Policy> future = hubServiceClient.setIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.SetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### testIamPermissions(TestIamPermissionsRequest request)
    
    
    public final TestIamPermissionsResponse testIamPermissions(TestIamPermissionsRequest request)

Returns permissions that a caller has on the specified resource. If theresource does not exist, this will return an empty set ofpermissions, not a `NOT_FOUND` error.

Note: This operation is designed to be used for buildingpermission-aware UIs and command-line tools, not for authorizationchecking. This operation may "fail open" without warning.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(GroupName.of("[PROJECT]", "[HUB]", "[GROUP]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response = hubServiceClient.testIamPermissions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.TestIamPermissionsRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.TestIamPermissionsResponse` |   
  
### testIamPermissionsCallable()
    
    
    public final UnaryCallable<TestIamPermissionsRequest,TestIamPermissionsResponse> testIamPermissionsCallable()

Returns permissions that a caller has on the specified resource. If theresource does not exist, this will return an empty set ofpermissions, not a `NOT_FOUND` error.

Note: This operation is designed to be used for buildingpermission-aware UIs and command-line tools, not for authorizationchecking. This operation may "fail open" without warning.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(GroupName.of("[PROJECT]", "[HUB]", "[GROUP]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           hubServiceClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### updateGroupAsync(Group group, FieldMask updateMask)
    
    
    public final OperationFuture<Group,OperationMetadata> updateGroupAsync(Group group, FieldMask updateMask)

Updates the parameters of a Network Connectivity Center group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       Group group = Group.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Group response = hubServiceClient.updateGroupAsync(group, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`group` | `[Group](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Group)`  
Required. The state that the group should be in after the update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. In the case of an update to an existing group, field mask is used to specify the fields to be overwritten. The fields specified in the update_mask are relative to the resource, not the full request. A field is overwritten if it is in the mask. If the user does not provide a mask, then all fields are overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Group](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Group),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### updateGroupAsync(UpdateGroupRequest request)
    
    
    public final OperationFuture<Group,OperationMetadata> updateGroupAsync(UpdateGroupRequest request)

Updates the parameters of a Network Connectivity Center group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       UpdateGroupRequest request =
           UpdateGroupRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setGroup(Group.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Group response = hubServiceClient.updateGroupAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.UpdateGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Group](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Group),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### updateGroupCallable()
    
    
    public final UnaryCallable<UpdateGroupRequest,Operation> updateGroupCallable()

Updates the parameters of a Network Connectivity Center group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       UpdateGroupRequest request =
           UpdateGroupRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setGroup(Group.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = hubServiceClient.updateGroupCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.UpdateGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateGroupOperationCallable()
    
    
    public final OperationCallable<UpdateGroupRequest,Group,OperationMetadata> updateGroupOperationCallable()

Updates the parameters of a Network Connectivity Center group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       UpdateGroupRequest request =
           UpdateGroupRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setGroup(Group.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Group, OperationMetadata> future =
           hubServiceClient.updateGroupOperationCallable().futureCall(request);
       // Do something.
       Group response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.UpdateGroupRequest),[Group](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Group),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### updateHubAsync(Hub hub, FieldMask updateMask)
    
    
    public final OperationFuture<Hub,OperationMetadata> updateHubAsync(Hub hub, FieldMask updateMask)

Updates the description and/or labels of a Network Connectivity Center hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       Hub hub = Hub.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Hub response = hubServiceClient.updateHubAsync(hub, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`hub` | `[Hub](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Hub)`  
Required. The state that the hub should be in after the update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. In the case of an update to an existing hub, field mask is used to specify the fields to be overwritten. The fields specified in the update_mask are relative to the resource, not the full request. A field is overwritten if it is in the mask. If the user does not provide a mask, then all fields are overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Hub](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Hub),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### updateHubAsync(UpdateHubRequest request)
    
    
    public final OperationFuture<Hub,OperationMetadata> updateHubAsync(UpdateHubRequest request)

Updates the description and/or labels of a Network Connectivity Center hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       UpdateHubRequest request =
           UpdateHubRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setHub(Hub.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Hub response = hubServiceClient.updateHubAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateHubRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.UpdateHubRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Hub](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Hub),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### updateHubCallable()
    
    
    public final UnaryCallable<UpdateHubRequest,Operation> updateHubCallable()

Updates the description and/or labels of a Network Connectivity Center hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       UpdateHubRequest request =
           UpdateHubRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setHub(Hub.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = hubServiceClient.updateHubCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateHubRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.UpdateHubRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateHubOperationCallable()
    
    
    public final OperationCallable<UpdateHubRequest,Hub,OperationMetadata> updateHubOperationCallable()

Updates the description and/or labels of a Network Connectivity Center hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       UpdateHubRequest request =
           UpdateHubRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setHub(Hub.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Hub, OperationMetadata> future =
           hubServiceClient.updateHubOperationCallable().futureCall(request);
       // Do something.
       Hub response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateHubRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.UpdateHubRequest),[Hub](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Hub),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### updateSpokeAsync(Spoke spoke, FieldMask updateMask)
    
    
    public final OperationFuture<Spoke,OperationMetadata> updateSpokeAsync(Spoke spoke, FieldMask updateMask)

Updates the parameters of a Network Connectivity Center spoke.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       Spoke spoke = Spoke.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Spoke response = hubServiceClient.updateSpokeAsync(spoke, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`spoke` | `[Spoke](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Spoke)`  
Required. The state that the spoke should be in after the update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. In the case of an update to an existing spoke, field mask is used to specify the fields to be overwritten. The fields specified in the update_mask are relative to the resource, not the full request. A field is overwritten if it is in the mask. If the user does not provide a mask, then all fields are overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Spoke](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Spoke),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### updateSpokeAsync(UpdateSpokeRequest request)
    
    
    public final OperationFuture<Spoke,OperationMetadata> updateSpokeAsync(UpdateSpokeRequest request)

Updates the parameters of a Network Connectivity Center spoke.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       UpdateSpokeRequest request =
           UpdateSpokeRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setSpoke(Spoke.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Spoke response = hubServiceClient.updateSpokeAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateSpokeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.UpdateSpokeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Spoke](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Spoke),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### updateSpokeCallable()
    
    
    public final UnaryCallable<UpdateSpokeRequest,Operation> updateSpokeCallable()

Updates the parameters of a Network Connectivity Center spoke.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       UpdateSpokeRequest request =
           UpdateSpokeRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setSpoke(Spoke.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = hubServiceClient.updateSpokeCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateSpokeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.UpdateSpokeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateSpokeOperationCallable()
    
    
    public final OperationCallable<UpdateSpokeRequest,Spoke,OperationMetadata> updateSpokeOperationCallable()

Updates the parameters of a Network Connectivity Center spoke.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HubServiceClient hubServiceClient = HubServiceClient.create()) {
       UpdateSpokeRequest request =
           UpdateSpokeRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setSpoke(Spoke.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Spoke, OperationMetadata> future =
           hubServiceClient.updateSpokeOperationCallable().futureCall(request);
       // Do something.
       Spoke response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateSpokeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.UpdateSpokeRequest),[Spoke](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Spoke),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
