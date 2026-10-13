---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkClient
title: Class EdgeNetworkClient (0.67.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:00:49.348052+00:00
---

# Class EdgeNetworkClient (0.67.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class EdgeNetworkClient (0.67.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.67.0 (latest)  0.63.0  0.62.0  0.61.0  0.59.0  0.56.0  0.55.0  0.53.0  0.51.0  0.50.0  0.49.0  0.48.0  0.46.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.38.0  0.36.0  0.35.0  0.32.0  0.31.0  0.30.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-edgenetwork/google-cloud-edgenetwork/src/main/java/com/google/cloud/edgenetwork/v1/EdgeNetworkClient.java)| [Product Reference](https://cloud.google.com/distributed-cloud/edge/latest/docs/overview)  
---|---  
  
Service Description: EdgeNetwork API provides managed, highly available cloud dynamic network configuration service to the GEC customer to enable edge application and network function solutions. This allows the customers to easily define and configure the network setup and property to meet the workload requirement.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       ZoneName name = ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]");
       InitializeZoneResponse response = edgeNetworkClient.initializeZone(name);
     }
     

Note: close() needs to be called on the EdgeNetworkClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
InitializeZone |  InitializeZone will initialize resources for a zone in a project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * initializeZone(InitializeZoneRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * initializeZone(ZoneName name) 
  * initializeZone(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * initializeZoneCallable() 

  
ListZones |  Deprecated: not implemented. Lists Zones in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listZones(ListZonesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listZones(LocationName parent) 
  * listZones(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listZonesPagedCallable() 
  * listZonesCallable() 

  
GetZone |  Deprecated: not implemented. Gets details of a single Zone. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getZone(GetZoneRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getZone(ZoneName name) 
  * getZone(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getZoneCallable() 

  
ListNetworks |  Lists Networks in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listNetworks(ListNetworksRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listNetworks(ZoneName parent) 
  * listNetworks(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listNetworksPagedCallable() 
  * listNetworksCallable() 

  
GetNetwork |  Gets details of a single Network. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getNetwork(GetNetworkRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getNetwork(NetworkName name) 
  * getNetwork(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getNetworkCallable() 

  
DiagnoseNetwork |  Get the diagnostics of a single network resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * diagnoseNetwork(DiagnoseNetworkRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * diagnoseNetwork(NetworkName name) 
  * diagnoseNetwork(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * diagnoseNetworkCallable() 

  
CreateNetwork |  Creates a new Network in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createNetworkAsync(CreateNetworkRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createNetworkAsync(ZoneName parent, Network network, String networkId) 
  * createNetworkAsync(String parent, Network network, String networkId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createNetworkOperationCallable() 
  * createNetworkCallable() 

  
DeleteNetwork |  Deletes a single Network. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteNetworkAsync(DeleteNetworkRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteNetworkAsync(NetworkName name) 
  * deleteNetworkAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteNetworkOperationCallable() 
  * deleteNetworkCallable() 

  
ListSubnets |  Lists Subnets in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listSubnets(ListSubnetsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listSubnets(ZoneName parent) 
  * listSubnets(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listSubnetsPagedCallable() 
  * listSubnetsCallable() 

  
GetSubnet |  Gets details of a single Subnet. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getSubnet(GetSubnetRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getSubnet(SubnetName name) 
  * getSubnet(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getSubnetCallable() 

  
CreateSubnet |  Creates a new Subnet in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createSubnetAsync(CreateSubnetRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createSubnetAsync(ZoneName parent, Subnet subnet, String subnetId) 
  * createSubnetAsync(String parent, Subnet subnet, String subnetId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createSubnetOperationCallable() 
  * createSubnetCallable() 

  
UpdateSubnet |  Updates the parameters of a single Subnet. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateSubnetAsync(UpdateSubnetRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateSubnetAsync(Subnet subnet, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateSubnetOperationCallable() 
  * updateSubnetCallable() 

  
DeleteSubnet |  Deletes a single Subnet. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteSubnetAsync(DeleteSubnetRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteSubnetAsync(SubnetName name) 
  * deleteSubnetAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteSubnetOperationCallable() 
  * deleteSubnetCallable() 

  
ListInterconnects |  Lists Interconnects in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listInterconnects(ListInterconnectsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listInterconnects(ZoneName parent) 
  * listInterconnects(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listInterconnectsPagedCallable() 
  * listInterconnectsCallable() 

  
GetInterconnect |  Gets details of a single Interconnect. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getInterconnect(GetInterconnectRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getInterconnect(InterconnectName name) 
  * getInterconnect(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getInterconnectCallable() 

  
DiagnoseInterconnect |  Get the diagnostics of a single interconnect resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * diagnoseInterconnect(DiagnoseInterconnectRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * diagnoseInterconnect(InterconnectName name) 
  * diagnoseInterconnect(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * diagnoseInterconnectCallable() 

  
ListInterconnectAttachments |  Lists InterconnectAttachments in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listInterconnectAttachments(ListInterconnectAttachmentsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listInterconnectAttachments(ZoneName parent) 
  * listInterconnectAttachments(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listInterconnectAttachmentsPagedCallable() 
  * listInterconnectAttachmentsCallable() 

  
GetInterconnectAttachment |  Gets details of a single InterconnectAttachment. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getInterconnectAttachment(GetInterconnectAttachmentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getInterconnectAttachment(InterconnectAttachmentName name) 
  * getInterconnectAttachment(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getInterconnectAttachmentCallable() 

  
CreateInterconnectAttachment |  Creates a new InterconnectAttachment in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createInterconnectAttachmentAsync(CreateInterconnectAttachmentRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createInterconnectAttachmentAsync(ZoneName parent, InterconnectAttachment interconnectAttachment, String interconnectAttachmentId) 
  * createInterconnectAttachmentAsync(String parent, InterconnectAttachment interconnectAttachment, String interconnectAttachmentId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createInterconnectAttachmentOperationCallable() 
  * createInterconnectAttachmentCallable() 

  
DeleteInterconnectAttachment |  Deletes a single InterconnectAttachment. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteInterconnectAttachmentAsync(DeleteInterconnectAttachmentRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteInterconnectAttachmentAsync(InterconnectAttachmentName name) 
  * deleteInterconnectAttachmentAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteInterconnectAttachmentOperationCallable() 
  * deleteInterconnectAttachmentCallable() 

  
ListRouters |  Lists Routers in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listRouters(ListRoutersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listRouters(ZoneName parent) 
  * listRouters(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listRoutersPagedCallable() 
  * listRoutersCallable() 

  
GetRouter |  Gets details of a single Router. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getRouter(GetRouterRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getRouter(RouterName name) 
  * getRouter(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getRouterCallable() 

  
DiagnoseRouter |  Get the diagnostics of a single router resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * diagnoseRouter(DiagnoseRouterRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * diagnoseRouter(RouterName name) 
  * diagnoseRouter(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * diagnoseRouterCallable() 

  
CreateRouter |  Creates a new Router in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createRouterAsync(CreateRouterRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createRouterAsync(ZoneName parent, Router router, String routerId) 
  * createRouterAsync(String parent, Router router, String routerId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createRouterOperationCallable() 
  * createRouterCallable() 

  
UpdateRouter |  Updates the parameters of a single Router. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateRouterAsync(UpdateRouterRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateRouterAsync(Router router, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateRouterOperationCallable() 
  * updateRouterCallable() 

  
DeleteRouter |  Deletes a single Router. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteRouterAsync(DeleteRouterRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteRouterAsync(RouterName name) 
  * deleteRouterAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteRouterOperationCallable() 
  * deleteRouterCallable() 

  
ListLocations |  Lists information about the supported locations for this service. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listLocations(ListLocationsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listLocationsPagedCallable() 
  * listLocationsCallable() 

  
GetLocation |  Gets information about a location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getLocation(GetLocationRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getLocationCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of EdgeNetworkSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     EdgeNetworkSettings edgeNetworkSettings =
         EdgeNetworkSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create(edgeNetworkSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     EdgeNetworkSettings edgeNetworkSettings =
         EdgeNetworkSettings.newBuilder().setEndpoint(myEndpoint).build();
     EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create(edgeNetworkSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     EdgeNetworkSettings edgeNetworkSettings = EdgeNetworkSettings.newHttpJsonBuilder().build();
     EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create(edgeNetworkSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > EdgeNetworkClient

## Static Methods 

### create()
    
    
    public static final EdgeNetworkClient create()

Constructs an instance of EdgeNetworkClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[EdgeNetworkClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(EdgeNetworkSettings settings)
    
    
    public static final EdgeNetworkClient create(EdgeNetworkSettings settings)

Constructs an instance of EdgeNetworkClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[EdgeNetworkSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[EdgeNetworkClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(EdgeNetworkStub stub)
    
    
    public static final EdgeNetworkClient create(EdgeNetworkStub stub)

Constructs an instance of EdgeNetworkClient, using the given stub for making calls. This is for advanced usage - prefer using create(EdgeNetworkSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[EdgeNetworkStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.stub.EdgeNetworkStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[EdgeNetworkClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkClient)` |   
  
## Constructors 

### EdgeNetworkClient(EdgeNetworkSettings settings)
    
    
    protected EdgeNetworkClient(EdgeNetworkSettings settings)

Constructs an instance of EdgeNetworkClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[EdgeNetworkSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkSettings)`  
  
  
### EdgeNetworkClient(EdgeNetworkStub stub)
    
    
    protected EdgeNetworkClient(EdgeNetworkStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[EdgeNetworkStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.stub.EdgeNetworkStub)`  
  
  
## Methods 

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

### createInterconnectAttachmentAsync(@Nullable ZoneName parent, InterconnectAttachment interconnectAttachment, String interconnectAttachmentId)
    
    
    public final OperationFuture<InterconnectAttachment,OperationMetadata> createInterconnectAttachmentAsync(@Nullable ZoneName parent, InterconnectAttachment interconnectAttachment, String interconnectAttachmentId)

Creates a new InterconnectAttachment in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       ZoneName parent = ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]");
       InterconnectAttachment interconnectAttachment = InterconnectAttachment.newBuilder().build();
       String interconnectAttachmentId = "interconnectAttachmentId1053538636";
       InterconnectAttachment response =
           edgeNetworkClient
               .createInterconnectAttachmentAsync(
                   parent, interconnectAttachment, interconnectAttachmentId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.edgenetwork.v1.ZoneName`  
Required. Value for parent.  
`interconnectAttachment` | `[InterconnectAttachment](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.InterconnectAttachment)`  
Required. The resource being created  
`interconnectAttachmentId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Id of the requesting object If auto-generating Id server-side, remove this field and interconnect_attachment_id from the method_signature of Create RPC  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[InterconnectAttachment](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.InterconnectAttachment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.OperationMetadata)>` |   
  
### createInterconnectAttachmentAsync(CreateInterconnectAttachmentRequest request)
    
    
    public final OperationFuture<InterconnectAttachment,OperationMetadata> createInterconnectAttachmentAsync(CreateInterconnectAttachmentRequest request)

Creates a new InterconnectAttachment in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       CreateInterconnectAttachmentRequest request =
           CreateInterconnectAttachmentRequest.newBuilder()
               .setParent(ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString())
               .setInterconnectAttachmentId("interconnectAttachmentId1053538636")
               .setInterconnectAttachment(InterconnectAttachment.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       InterconnectAttachment response =
           edgeNetworkClient.createInterconnectAttachmentAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateInterconnectAttachmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.CreateInterconnectAttachmentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[InterconnectAttachment](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.InterconnectAttachment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.OperationMetadata)>` |   
  
### createInterconnectAttachmentAsync(String parent, InterconnectAttachment interconnectAttachment, String interconnectAttachmentId)
    
    
    public final OperationFuture<InterconnectAttachment,OperationMetadata> createInterconnectAttachmentAsync(String parent, InterconnectAttachment interconnectAttachment, String interconnectAttachmentId)

Creates a new InterconnectAttachment in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       String parent = ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString();
       InterconnectAttachment interconnectAttachment = InterconnectAttachment.newBuilder().build();
       String interconnectAttachmentId = "interconnectAttachmentId1053538636";
       InterconnectAttachment response =
           edgeNetworkClient
               .createInterconnectAttachmentAsync(
                   parent, interconnectAttachment, interconnectAttachmentId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Value for parent.  
`interconnectAttachment` | `[InterconnectAttachment](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.InterconnectAttachment)`  
Required. The resource being created  
`interconnectAttachmentId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Id of the requesting object If auto-generating Id server-side, remove this field and interconnect_attachment_id from the method_signature of Create RPC  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[InterconnectAttachment](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.InterconnectAttachment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.OperationMetadata)>` |   
  
### createInterconnectAttachmentCallable()
    
    
    public final UnaryCallable<CreateInterconnectAttachmentRequest,Operation> createInterconnectAttachmentCallable()

Creates a new InterconnectAttachment in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       CreateInterconnectAttachmentRequest request =
           CreateInterconnectAttachmentRequest.newBuilder()
               .setParent(ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString())
               .setInterconnectAttachmentId("interconnectAttachmentId1053538636")
               .setInterconnectAttachment(InterconnectAttachment.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           edgeNetworkClient.createInterconnectAttachmentCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateInterconnectAttachmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.CreateInterconnectAttachmentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createInterconnectAttachmentOperationCallable()
    
    
    public final OperationCallable<CreateInterconnectAttachmentRequest,InterconnectAttachment,OperationMetadata> createInterconnectAttachmentOperationCallable()

Creates a new InterconnectAttachment in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       CreateInterconnectAttachmentRequest request =
           CreateInterconnectAttachmentRequest.newBuilder()
               .setParent(ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString())
               .setInterconnectAttachmentId("interconnectAttachmentId1053538636")
               .setInterconnectAttachment(InterconnectAttachment.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<InterconnectAttachment, OperationMetadata> future =
           edgeNetworkClient.createInterconnectAttachmentOperationCallable().futureCall(request);
       // Do something.
       InterconnectAttachment response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateInterconnectAttachmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.CreateInterconnectAttachmentRequest),[InterconnectAttachment](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.InterconnectAttachment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.OperationMetadata)>` |   
  
### createNetworkAsync(@Nullable ZoneName parent, Network network, String networkId)
    
    
    public final OperationFuture<Network,OperationMetadata> createNetworkAsync(@Nullable ZoneName parent, Network network, String networkId)

Creates a new Network in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       ZoneName parent = ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]");
       Network network = Network.newBuilder().build();
       String networkId = "networkId2062782441";
       Network response = edgeNetworkClient.createNetworkAsync(parent, network, networkId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.edgenetwork.v1.ZoneName`  
Required. Value for parent.  
`network` | `[Network](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Network)`  
Required. The resource being created  
`networkId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Id of the requesting object If auto-generating Id server-side, remove this field and network_id from the method_signature of Create RPC  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Network](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Network),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.OperationMetadata)>` |   
  
### createNetworkAsync(CreateNetworkRequest request)
    
    
    public final OperationFuture<Network,OperationMetadata> createNetworkAsync(CreateNetworkRequest request)

Creates a new Network in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       CreateNetworkRequest request =
           CreateNetworkRequest.newBuilder()
               .setParent(ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString())
               .setNetworkId("networkId2062782441")
               .setNetwork(Network.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Network response = edgeNetworkClient.createNetworkAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.CreateNetworkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Network](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Network),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.OperationMetadata)>` |   
  
### createNetworkAsync(String parent, Network network, String networkId)
    
    
    public final OperationFuture<Network,OperationMetadata> createNetworkAsync(String parent, Network network, String networkId)

Creates a new Network in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       String parent = ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString();
       Network network = Network.newBuilder().build();
       String networkId = "networkId2062782441";
       Network response = edgeNetworkClient.createNetworkAsync(parent, network, networkId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Value for parent.  
`network` | `[Network](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Network)`  
Required. The resource being created  
`networkId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Id of the requesting object If auto-generating Id server-side, remove this field and network_id from the method_signature of Create RPC  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Network](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Network),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.OperationMetadata)>` |   
  
### createNetworkCallable()
    
    
    public final UnaryCallable<CreateNetworkRequest,Operation> createNetworkCallable()

Creates a new Network in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       CreateNetworkRequest request =
           CreateNetworkRequest.newBuilder()
               .setParent(ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString())
               .setNetworkId("networkId2062782441")
               .setNetwork(Network.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = edgeNetworkClient.createNetworkCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.CreateNetworkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createNetworkOperationCallable()
    
    
    public final OperationCallable<CreateNetworkRequest,Network,OperationMetadata> createNetworkOperationCallable()

Creates a new Network in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       CreateNetworkRequest request =
           CreateNetworkRequest.newBuilder()
               .setParent(ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString())
               .setNetworkId("networkId2062782441")
               .setNetwork(Network.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Network, OperationMetadata> future =
           edgeNetworkClient.createNetworkOperationCallable().futureCall(request);
       // Do something.
       Network response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.CreateNetworkRequest),[Network](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Network),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.OperationMetadata)>` |   
  
### createRouterAsync(@Nullable ZoneName parent, Router router, String routerId)
    
    
    public final OperationFuture<Router,OperationMetadata> createRouterAsync(@Nullable ZoneName parent, Router router, String routerId)

Creates a new Router in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       ZoneName parent = ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]");
       Router router = Router.newBuilder().build();
       String routerId = "routerId5435972";
       Router response = edgeNetworkClient.createRouterAsync(parent, router, routerId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.edgenetwork.v1.ZoneName`  
Required. Value for parent.  
`router` | `[Router](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Router)`  
Required. The resource being created  
`routerId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Id of the requesting object If auto-generating Id server-side, remove this field and router_id from the method_signature of Create RPC  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Router](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Router),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.OperationMetadata)>` |   
  
### createRouterAsync(CreateRouterRequest request)
    
    
    public final OperationFuture<Router,OperationMetadata> createRouterAsync(CreateRouterRequest request)

Creates a new Router in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       CreateRouterRequest request =
           CreateRouterRequest.newBuilder()
               .setParent(ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString())
               .setRouterId("routerId5435972")
               .setRouter(Router.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Router response = edgeNetworkClient.createRouterAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.CreateRouterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Router](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Router),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.OperationMetadata)>` |   
  
### createRouterAsync(String parent, Router router, String routerId)
    
    
    public final OperationFuture<Router,OperationMetadata> createRouterAsync(String parent, Router router, String routerId)

Creates a new Router in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       String parent = ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString();
       Router router = Router.newBuilder().build();
       String routerId = "routerId5435972";
       Router response = edgeNetworkClient.createRouterAsync(parent, router, routerId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Value for parent.  
`router` | `[Router](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Router)`  
Required. The resource being created  
`routerId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Id of the requesting object If auto-generating Id server-side, remove this field and router_id from the method_signature of Create RPC  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Router](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Router),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.OperationMetadata)>` |   
  
### createRouterCallable()
    
    
    public final UnaryCallable<CreateRouterRequest,Operation> createRouterCallable()

Creates a new Router in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       CreateRouterRequest request =
           CreateRouterRequest.newBuilder()
               .setParent(ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString())
               .setRouterId("routerId5435972")
               .setRouter(Router.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = edgeNetworkClient.createRouterCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.CreateRouterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createRouterOperationCallable()
    
    
    public final OperationCallable<CreateRouterRequest,Router,OperationMetadata> createRouterOperationCallable()

Creates a new Router in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       CreateRouterRequest request =
           CreateRouterRequest.newBuilder()
               .setParent(ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString())
               .setRouterId("routerId5435972")
               .setRouter(Router.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Router, OperationMetadata> future =
           edgeNetworkClient.createRouterOperationCallable().futureCall(request);
       // Do something.
       Router response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.CreateRouterRequest),[Router](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Router),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.OperationMetadata)>` |   
  
### createSubnetAsync(@Nullable ZoneName parent, Subnet subnet, String subnetId)
    
    
    public final OperationFuture<Subnet,OperationMetadata> createSubnetAsync(@Nullable ZoneName parent, Subnet subnet, String subnetId)

Creates a new Subnet in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       ZoneName parent = ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]");
       Subnet subnet = Subnet.newBuilder().build();
       String subnetId = "subnetId-2066159272";
       Subnet response = edgeNetworkClient.createSubnetAsync(parent, subnet, subnetId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.edgenetwork.v1.ZoneName`  
Required. Value for parent.  
`subnet` | `[Subnet](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Subnet)`  
Required. The resource being created  
`subnetId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Id of the requesting object If auto-generating Id server-side, remove this field and subnet_id from the method_signature of Create RPC  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Subnet](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Subnet),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.OperationMetadata)>` |   
  
### createSubnetAsync(CreateSubnetRequest request)
    
    
    public final OperationFuture<Subnet,OperationMetadata> createSubnetAsync(CreateSubnetRequest request)

Creates a new Subnet in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       CreateSubnetRequest request =
           CreateSubnetRequest.newBuilder()
               .setParent(ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString())
               .setSubnetId("subnetId-2066159272")
               .setSubnet(Subnet.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Subnet response = edgeNetworkClient.createSubnetAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateSubnetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.CreateSubnetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Subnet](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Subnet),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.OperationMetadata)>` |   
  
### createSubnetAsync(String parent, Subnet subnet, String subnetId)
    
    
    public final OperationFuture<Subnet,OperationMetadata> createSubnetAsync(String parent, Subnet subnet, String subnetId)

Creates a new Subnet in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       String parent = ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString();
       Subnet subnet = Subnet.newBuilder().build();
       String subnetId = "subnetId-2066159272";
       Subnet response = edgeNetworkClient.createSubnetAsync(parent, subnet, subnetId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Value for parent.  
`subnet` | `[Subnet](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Subnet)`  
Required. The resource being created  
`subnetId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Id of the requesting object If auto-generating Id server-side, remove this field and subnet_id from the method_signature of Create RPC  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Subnet](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Subnet),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.OperationMetadata)>` |   
  
### createSubnetCallable()
    
    
    public final UnaryCallable<CreateSubnetRequest,Operation> createSubnetCallable()

Creates a new Subnet in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       CreateSubnetRequest request =
           CreateSubnetRequest.newBuilder()
               .setParent(ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString())
               .setSubnetId("subnetId-2066159272")
               .setSubnet(Subnet.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = edgeNetworkClient.createSubnetCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateSubnetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.CreateSubnetRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createSubnetOperationCallable()
    
    
    public final OperationCallable<CreateSubnetRequest,Subnet,OperationMetadata> createSubnetOperationCallable()

Creates a new Subnet in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       CreateSubnetRequest request =
           CreateSubnetRequest.newBuilder()
               .setParent(ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString())
               .setSubnetId("subnetId-2066159272")
               .setSubnet(Subnet.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Subnet, OperationMetadata> future =
           edgeNetworkClient.createSubnetOperationCallable().futureCall(request);
       // Do something.
       Subnet response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateSubnetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.CreateSubnetRequest),[Subnet](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Subnet),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.OperationMetadata)>` |   
  
### deleteInterconnectAttachmentAsync(@Nullable InterconnectAttachmentName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteInterconnectAttachmentAsync(@Nullable InterconnectAttachmentName name)

Deletes a single InterconnectAttachment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       InterconnectAttachmentName name =
           InterconnectAttachmentName.of(
               "[PROJECT]", "[LOCATION]", "[ZONE]", "[INTERCONNECT_ATTACHMENT]");
       edgeNetworkClient.deleteInterconnectAttachmentAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.edgenetwork.v1.InterconnectAttachmentName`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.OperationMetadata)>` |   
  
### deleteInterconnectAttachmentAsync(DeleteInterconnectAttachmentRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteInterconnectAttachmentAsync(DeleteInterconnectAttachmentRequest request)

Deletes a single InterconnectAttachment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       DeleteInterconnectAttachmentRequest request =
           DeleteInterconnectAttachmentRequest.newBuilder()
               .setName(
                   InterconnectAttachmentName.of(
                           "[PROJECT]", "[LOCATION]", "[ZONE]", "[INTERCONNECT_ATTACHMENT]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       edgeNetworkClient.deleteInterconnectAttachmentAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteInterconnectAttachmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DeleteInterconnectAttachmentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.OperationMetadata)>` |   
  
### deleteInterconnectAttachmentAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteInterconnectAttachmentAsync(String name)

Deletes a single InterconnectAttachment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       String name =
           InterconnectAttachmentName.of(
                   "[PROJECT]", "[LOCATION]", "[ZONE]", "[INTERCONNECT_ATTACHMENT]")
               .toString();
       edgeNetworkClient.deleteInterconnectAttachmentAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.OperationMetadata)>` |   
  
### deleteInterconnectAttachmentCallable()
    
    
    public final UnaryCallable<DeleteInterconnectAttachmentRequest,Operation> deleteInterconnectAttachmentCallable()

Deletes a single InterconnectAttachment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       DeleteInterconnectAttachmentRequest request =
           DeleteInterconnectAttachmentRequest.newBuilder()
               .setName(
                   InterconnectAttachmentName.of(
                           "[PROJECT]", "[LOCATION]", "[ZONE]", "[INTERCONNECT_ATTACHMENT]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           edgeNetworkClient.deleteInterconnectAttachmentCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteInterconnectAttachmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DeleteInterconnectAttachmentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteInterconnectAttachmentOperationCallable()
    
    
    public final OperationCallable<DeleteInterconnectAttachmentRequest,Empty,OperationMetadata> deleteInterconnectAttachmentOperationCallable()

Deletes a single InterconnectAttachment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       DeleteInterconnectAttachmentRequest request =
           DeleteInterconnectAttachmentRequest.newBuilder()
               .setName(
                   InterconnectAttachmentName.of(
                           "[PROJECT]", "[LOCATION]", "[ZONE]", "[INTERCONNECT_ATTACHMENT]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           edgeNetworkClient.deleteInterconnectAttachmentOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteInterconnectAttachmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DeleteInterconnectAttachmentRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.OperationMetadata)>` |   
  
### deleteNetworkAsync(@Nullable NetworkName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteNetworkAsync(@Nullable NetworkName name)

Deletes a single Network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       NetworkName name = NetworkName.of("[PROJECT]", "[LOCATION]", "[ZONE]", "[NETWORK]");
       edgeNetworkClient.deleteNetworkAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.edgenetwork.v1.NetworkName`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.OperationMetadata)>` |   
  
### deleteNetworkAsync(DeleteNetworkRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteNetworkAsync(DeleteNetworkRequest request)

Deletes a single Network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       DeleteNetworkRequest request =
           DeleteNetworkRequest.newBuilder()
               .setName(NetworkName.of("[PROJECT]", "[LOCATION]", "[ZONE]", "[NETWORK]").toString())
               .setRequestId("requestId693933066")
               .build();
       edgeNetworkClient.deleteNetworkAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DeleteNetworkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.OperationMetadata)>` |   
  
### deleteNetworkAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteNetworkAsync(String name)

Deletes a single Network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       String name = NetworkName.of("[PROJECT]", "[LOCATION]", "[ZONE]", "[NETWORK]").toString();
       edgeNetworkClient.deleteNetworkAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.OperationMetadata)>` |   
  
### deleteNetworkCallable()
    
    
    public final UnaryCallable<DeleteNetworkRequest,Operation> deleteNetworkCallable()

Deletes a single Network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       DeleteNetworkRequest request =
           DeleteNetworkRequest.newBuilder()
               .setName(NetworkName.of("[PROJECT]", "[LOCATION]", "[ZONE]", "[NETWORK]").toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = edgeNetworkClient.deleteNetworkCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DeleteNetworkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteNetworkOperationCallable()
    
    
    public final OperationCallable<DeleteNetworkRequest,Empty,OperationMetadata> deleteNetworkOperationCallable()

Deletes a single Network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       DeleteNetworkRequest request =
           DeleteNetworkRequest.newBuilder()
               .setName(NetworkName.of("[PROJECT]", "[LOCATION]", "[ZONE]", "[NETWORK]").toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           edgeNetworkClient.deleteNetworkOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DeleteNetworkRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.OperationMetadata)>` |   
  
### deleteRouterAsync(@Nullable RouterName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteRouterAsync(@Nullable RouterName name)

Deletes a single Router.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       RouterName name = RouterName.of("[PROJECT]", "[LOCATION]", "[ZONE]", "[ROUTER]");
       edgeNetworkClient.deleteRouterAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.edgenetwork.v1.RouterName`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.OperationMetadata)>` |   
  
### deleteRouterAsync(DeleteRouterRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteRouterAsync(DeleteRouterRequest request)

Deletes a single Router.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       DeleteRouterRequest request =
           DeleteRouterRequest.newBuilder()
               .setName(RouterName.of("[PROJECT]", "[LOCATION]", "[ZONE]", "[ROUTER]").toString())
               .setRequestId("requestId693933066")
               .build();
       edgeNetworkClient.deleteRouterAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DeleteRouterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.OperationMetadata)>` |   
  
### deleteRouterAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteRouterAsync(String name)

Deletes a single Router.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       String name = RouterName.of("[PROJECT]", "[LOCATION]", "[ZONE]", "[ROUTER]").toString();
       edgeNetworkClient.deleteRouterAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.OperationMetadata)>` |   
  
### deleteRouterCallable()
    
    
    public final UnaryCallable<DeleteRouterRequest,Operation> deleteRouterCallable()

Deletes a single Router.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       DeleteRouterRequest request =
           DeleteRouterRequest.newBuilder()
               .setName(RouterName.of("[PROJECT]", "[LOCATION]", "[ZONE]", "[ROUTER]").toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = edgeNetworkClient.deleteRouterCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DeleteRouterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteRouterOperationCallable()
    
    
    public final OperationCallable<DeleteRouterRequest,Empty,OperationMetadata> deleteRouterOperationCallable()

Deletes a single Router.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       DeleteRouterRequest request =
           DeleteRouterRequest.newBuilder()
               .setName(RouterName.of("[PROJECT]", "[LOCATION]", "[ZONE]", "[ROUTER]").toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           edgeNetworkClient.deleteRouterOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DeleteRouterRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.OperationMetadata)>` |   
  
### deleteSubnetAsync(@Nullable SubnetName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteSubnetAsync(@Nullable SubnetName name)

Deletes a single Subnet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       SubnetName name = SubnetName.of("[PROJECT]", "[LOCATION]", "[ZONE]", "[SUBNET]");
       edgeNetworkClient.deleteSubnetAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.edgenetwork.v1.SubnetName`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.OperationMetadata)>` |   
  
### deleteSubnetAsync(DeleteSubnetRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteSubnetAsync(DeleteSubnetRequest request)

Deletes a single Subnet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       DeleteSubnetRequest request =
           DeleteSubnetRequest.newBuilder()
               .setName(SubnetName.of("[PROJECT]", "[LOCATION]", "[ZONE]", "[SUBNET]").toString())
               .setRequestId("requestId693933066")
               .build();
       edgeNetworkClient.deleteSubnetAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteSubnetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DeleteSubnetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.OperationMetadata)>` |   
  
### deleteSubnetAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteSubnetAsync(String name)

Deletes a single Subnet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       String name = SubnetName.of("[PROJECT]", "[LOCATION]", "[ZONE]", "[SUBNET]").toString();
       edgeNetworkClient.deleteSubnetAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.OperationMetadata)>` |   
  
### deleteSubnetCallable()
    
    
    public final UnaryCallable<DeleteSubnetRequest,Operation> deleteSubnetCallable()

Deletes a single Subnet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       DeleteSubnetRequest request =
           DeleteSubnetRequest.newBuilder()
               .setName(SubnetName.of("[PROJECT]", "[LOCATION]", "[ZONE]", "[SUBNET]").toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = edgeNetworkClient.deleteSubnetCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteSubnetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DeleteSubnetRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteSubnetOperationCallable()
    
    
    public final OperationCallable<DeleteSubnetRequest,Empty,OperationMetadata> deleteSubnetOperationCallable()

Deletes a single Subnet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       DeleteSubnetRequest request =
           DeleteSubnetRequest.newBuilder()
               .setName(SubnetName.of("[PROJECT]", "[LOCATION]", "[ZONE]", "[SUBNET]").toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           edgeNetworkClient.deleteSubnetOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteSubnetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DeleteSubnetRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.OperationMetadata)>` |   
  
### diagnoseInterconnect(@Nullable InterconnectName name)
    
    
    public final DiagnoseInterconnectResponse diagnoseInterconnect(@Nullable InterconnectName name)

Get the diagnostics of a single interconnect resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       InterconnectName name =
           InterconnectName.of("[PROJECT]", "[LOCATION]", "[ZONE]", "[INTERCONNECT]");
       DiagnoseInterconnectResponse response = edgeNetworkClient.diagnoseInterconnect(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.edgenetwork.v1.InterconnectName`  
Required. The name of the interconnect resource.  
**Returns**  
---  
**Type** | **Description**  
`[DiagnoseInterconnectResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DiagnoseInterconnectResponse)` |   
  
### diagnoseInterconnect(DiagnoseInterconnectRequest request)
    
    
    public final DiagnoseInterconnectResponse diagnoseInterconnect(DiagnoseInterconnectRequest request)

Get the diagnostics of a single interconnect resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       DiagnoseInterconnectRequest request =
           DiagnoseInterconnectRequest.newBuilder()
               .setName(
                   InterconnectName.of("[PROJECT]", "[LOCATION]", "[ZONE]", "[INTERCONNECT]")
                       .toString())
               .build();
       DiagnoseInterconnectResponse response = edgeNetworkClient.diagnoseInterconnect(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DiagnoseInterconnectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DiagnoseInterconnectRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DiagnoseInterconnectResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DiagnoseInterconnectResponse)` |   
  
### diagnoseInterconnect(String name)
    
    
    public final DiagnoseInterconnectResponse diagnoseInterconnect(String name)

Get the diagnostics of a single interconnect resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       String name =
           InterconnectName.of("[PROJECT]", "[LOCATION]", "[ZONE]", "[INTERCONNECT]").toString();
       DiagnoseInterconnectResponse response = edgeNetworkClient.diagnoseInterconnect(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the interconnect resource.  
**Returns**  
---  
**Type** | **Description**  
`[DiagnoseInterconnectResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DiagnoseInterconnectResponse)` |   
  
### diagnoseInterconnectCallable()
    
    
    public final UnaryCallable<DiagnoseInterconnectRequest,DiagnoseInterconnectResponse> diagnoseInterconnectCallable()

Get the diagnostics of a single interconnect resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       DiagnoseInterconnectRequest request =
           DiagnoseInterconnectRequest.newBuilder()
               .setName(
                   InterconnectName.of("[PROJECT]", "[LOCATION]", "[ZONE]", "[INTERCONNECT]")
                       .toString())
               .build();
       ApiFuture<DiagnoseInterconnectResponse> future =
           edgeNetworkClient.diagnoseInterconnectCallable().futureCall(request);
       // Do something.
       DiagnoseInterconnectResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DiagnoseInterconnectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DiagnoseInterconnectRequest),[DiagnoseInterconnectResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DiagnoseInterconnectResponse)>` |   
  
### diagnoseNetwork(@Nullable NetworkName name)
    
    
    public final DiagnoseNetworkResponse diagnoseNetwork(@Nullable NetworkName name)

Get the diagnostics of a single network resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       NetworkName name = NetworkName.of("[PROJECT]", "[LOCATION]", "[ZONE]", "[NETWORK]");
       DiagnoseNetworkResponse response = edgeNetworkClient.diagnoseNetwork(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.edgenetwork.v1.NetworkName`  
Required. The name of the network resource.  
**Returns**  
---  
**Type** | **Description**  
`[DiagnoseNetworkResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DiagnoseNetworkResponse)` |   
  
### diagnoseNetwork(DiagnoseNetworkRequest request)
    
    
    public final DiagnoseNetworkResponse diagnoseNetwork(DiagnoseNetworkRequest request)

Get the diagnostics of a single network resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       DiagnoseNetworkRequest request =
           DiagnoseNetworkRequest.newBuilder()
               .setName(NetworkName.of("[PROJECT]", "[LOCATION]", "[ZONE]", "[NETWORK]").toString())
               .build();
       DiagnoseNetworkResponse response = edgeNetworkClient.diagnoseNetwork(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DiagnoseNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DiagnoseNetworkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DiagnoseNetworkResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DiagnoseNetworkResponse)` |   
  
### diagnoseNetwork(String name)
    
    
    public final DiagnoseNetworkResponse diagnoseNetwork(String name)

Get the diagnostics of a single network resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       String name = NetworkName.of("[PROJECT]", "[LOCATION]", "[ZONE]", "[NETWORK]").toString();
       DiagnoseNetworkResponse response = edgeNetworkClient.diagnoseNetwork(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the network resource.  
**Returns**  
---  
**Type** | **Description**  
`[DiagnoseNetworkResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DiagnoseNetworkResponse)` |   
  
### diagnoseNetworkCallable()
    
    
    public final UnaryCallable<DiagnoseNetworkRequest,DiagnoseNetworkResponse> diagnoseNetworkCallable()

Get the diagnostics of a single network resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       DiagnoseNetworkRequest request =
           DiagnoseNetworkRequest.newBuilder()
               .setName(NetworkName.of("[PROJECT]", "[LOCATION]", "[ZONE]", "[NETWORK]").toString())
               .build();
       ApiFuture<DiagnoseNetworkResponse> future =
           edgeNetworkClient.diagnoseNetworkCallable().futureCall(request);
       // Do something.
       DiagnoseNetworkResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DiagnoseNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DiagnoseNetworkRequest),[DiagnoseNetworkResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DiagnoseNetworkResponse)>` |   
  
### diagnoseRouter(@Nullable RouterName name)
    
    
    public final DiagnoseRouterResponse diagnoseRouter(@Nullable RouterName name)

Get the diagnostics of a single router resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       RouterName name = RouterName.of("[PROJECT]", "[LOCATION]", "[ZONE]", "[ROUTER]");
       DiagnoseRouterResponse response = edgeNetworkClient.diagnoseRouter(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.edgenetwork.v1.RouterName`  
Required. The name of the router resource.  
**Returns**  
---  
**Type** | **Description**  
`[DiagnoseRouterResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DiagnoseRouterResponse)` |   
  
### diagnoseRouter(DiagnoseRouterRequest request)
    
    
    public final DiagnoseRouterResponse diagnoseRouter(DiagnoseRouterRequest request)

Get the diagnostics of a single router resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       DiagnoseRouterRequest request =
           DiagnoseRouterRequest.newBuilder()
               .setName(RouterName.of("[PROJECT]", "[LOCATION]", "[ZONE]", "[ROUTER]").toString())
               .build();
       DiagnoseRouterResponse response = edgeNetworkClient.diagnoseRouter(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DiagnoseRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DiagnoseRouterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DiagnoseRouterResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DiagnoseRouterResponse)` |   
  
### diagnoseRouter(String name)
    
    
    public final DiagnoseRouterResponse diagnoseRouter(String name)

Get the diagnostics of a single router resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       String name = RouterName.of("[PROJECT]", "[LOCATION]", "[ZONE]", "[ROUTER]").toString();
       DiagnoseRouterResponse response = edgeNetworkClient.diagnoseRouter(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the router resource.  
**Returns**  
---  
**Type** | **Description**  
`[DiagnoseRouterResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DiagnoseRouterResponse)` |   
  
### diagnoseRouterCallable()
    
    
    public final UnaryCallable<DiagnoseRouterRequest,DiagnoseRouterResponse> diagnoseRouterCallable()

Get the diagnostics of a single router resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       DiagnoseRouterRequest request =
           DiagnoseRouterRequest.newBuilder()
               .setName(RouterName.of("[PROJECT]", "[LOCATION]", "[ZONE]", "[ROUTER]").toString())
               .build();
       ApiFuture<DiagnoseRouterResponse> future =
           edgeNetworkClient.diagnoseRouterCallable().futureCall(request);
       // Do something.
       DiagnoseRouterResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DiagnoseRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DiagnoseRouterRequest),[DiagnoseRouterResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DiagnoseRouterResponse)>` |   
  
### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getInterconnect(@Nullable InterconnectName name)
    
    
    public final Interconnect getInterconnect(@Nullable InterconnectName name)

Gets details of a single Interconnect.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       InterconnectName name =
           InterconnectName.of("[PROJECT]", "[LOCATION]", "[ZONE]", "[INTERCONNECT]");
       Interconnect response = edgeNetworkClient.getInterconnect(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.edgenetwork.v1.InterconnectName`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[Interconnect](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Interconnect)` |   
  
### getInterconnect(GetInterconnectRequest request)
    
    
    public final Interconnect getInterconnect(GetInterconnectRequest request)

Gets details of a single Interconnect.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       GetInterconnectRequest request =
           GetInterconnectRequest.newBuilder()
               .setName(
                   InterconnectName.of("[PROJECT]", "[LOCATION]", "[ZONE]", "[INTERCONNECT]")
                       .toString())
               .build();
       Interconnect response = edgeNetworkClient.getInterconnect(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetInterconnectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.GetInterconnectRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Interconnect](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Interconnect)` |   
  
### getInterconnect(String name)
    
    
    public final Interconnect getInterconnect(String name)

Gets details of a single Interconnect.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       String name =
           InterconnectName.of("[PROJECT]", "[LOCATION]", "[ZONE]", "[INTERCONNECT]").toString();
       Interconnect response = edgeNetworkClient.getInterconnect(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[Interconnect](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Interconnect)` |   
  
### getInterconnectAttachment(@Nullable InterconnectAttachmentName name)
    
    
    public final InterconnectAttachment getInterconnectAttachment(@Nullable InterconnectAttachmentName name)

Gets details of a single InterconnectAttachment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       InterconnectAttachmentName name =
           InterconnectAttachmentName.of(
               "[PROJECT]", "[LOCATION]", "[ZONE]", "[INTERCONNECT_ATTACHMENT]");
       InterconnectAttachment response = edgeNetworkClient.getInterconnectAttachment(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.edgenetwork.v1.InterconnectAttachmentName`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[InterconnectAttachment](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.InterconnectAttachment)` |   
  
### getInterconnectAttachment(GetInterconnectAttachmentRequest request)
    
    
    public final InterconnectAttachment getInterconnectAttachment(GetInterconnectAttachmentRequest request)

Gets details of a single InterconnectAttachment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       GetInterconnectAttachmentRequest request =
           GetInterconnectAttachmentRequest.newBuilder()
               .setName(
                   InterconnectAttachmentName.of(
                           "[PROJECT]", "[LOCATION]", "[ZONE]", "[INTERCONNECT_ATTACHMENT]")
                       .toString())
               .build();
       InterconnectAttachment response = edgeNetworkClient.getInterconnectAttachment(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetInterconnectAttachmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.GetInterconnectAttachmentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[InterconnectAttachment](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.InterconnectAttachment)` |   
  
### getInterconnectAttachment(String name)
    
    
    public final InterconnectAttachment getInterconnectAttachment(String name)

Gets details of a single InterconnectAttachment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       String name =
           InterconnectAttachmentName.of(
                   "[PROJECT]", "[LOCATION]", "[ZONE]", "[INTERCONNECT_ATTACHMENT]")
               .toString();
       InterconnectAttachment response = edgeNetworkClient.getInterconnectAttachment(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[InterconnectAttachment](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.InterconnectAttachment)` |   
  
### getInterconnectAttachmentCallable()
    
    
    public final UnaryCallable<GetInterconnectAttachmentRequest,InterconnectAttachment> getInterconnectAttachmentCallable()

Gets details of a single InterconnectAttachment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       GetInterconnectAttachmentRequest request =
           GetInterconnectAttachmentRequest.newBuilder()
               .setName(
                   InterconnectAttachmentName.of(
                           "[PROJECT]", "[LOCATION]", "[ZONE]", "[INTERCONNECT_ATTACHMENT]")
                       .toString())
               .build();
       ApiFuture<InterconnectAttachment> future =
           edgeNetworkClient.getInterconnectAttachmentCallable().futureCall(request);
       // Do something.
       InterconnectAttachment response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetInterconnectAttachmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.GetInterconnectAttachmentRequest),[InterconnectAttachment](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.InterconnectAttachment)>` |   
  
### getInterconnectCallable()
    
    
    public final UnaryCallable<GetInterconnectRequest,Interconnect> getInterconnectCallable()

Gets details of a single Interconnect.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       GetInterconnectRequest request =
           GetInterconnectRequest.newBuilder()
               .setName(
                   InterconnectName.of("[PROJECT]", "[LOCATION]", "[ZONE]", "[INTERCONNECT]")
                       .toString())
               .build();
       ApiFuture<Interconnect> future =
           edgeNetworkClient.getInterconnectCallable().futureCall(request);
       // Do something.
       Interconnect response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetInterconnectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.GetInterconnectRequest),[Interconnect](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Interconnect)>` |   
  
### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = edgeNetworkClient.getLocation(request);
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
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = edgeNetworkClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getNetwork(@Nullable NetworkName name)
    
    
    public final Network getNetwork(@Nullable NetworkName name)

Gets details of a single Network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       NetworkName name = NetworkName.of("[PROJECT]", "[LOCATION]", "[ZONE]", "[NETWORK]");
       Network response = edgeNetworkClient.getNetwork(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.edgenetwork.v1.NetworkName`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[Network](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Network)` |   
  
### getNetwork(GetNetworkRequest request)
    
    
    public final Network getNetwork(GetNetworkRequest request)

Gets details of a single Network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       GetNetworkRequest request =
           GetNetworkRequest.newBuilder()
               .setName(NetworkName.of("[PROJECT]", "[LOCATION]", "[ZONE]", "[NETWORK]").toString())
               .build();
       Network response = edgeNetworkClient.getNetwork(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.GetNetworkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Network](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Network)` |   
  
### getNetwork(String name)
    
    
    public final Network getNetwork(String name)

Gets details of a single Network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       String name = NetworkName.of("[PROJECT]", "[LOCATION]", "[ZONE]", "[NETWORK]").toString();
       Network response = edgeNetworkClient.getNetwork(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[Network](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Network)` |   
  
### getNetworkCallable()
    
    
    public final UnaryCallable<GetNetworkRequest,Network> getNetworkCallable()

Gets details of a single Network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       GetNetworkRequest request =
           GetNetworkRequest.newBuilder()
               .setName(NetworkName.of("[PROJECT]", "[LOCATION]", "[ZONE]", "[NETWORK]").toString())
               .build();
       ApiFuture<Network> future = edgeNetworkClient.getNetworkCallable().futureCall(request);
       // Do something.
       Network response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.GetNetworkRequest),[Network](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Network)>` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getRouter(@Nullable RouterName name)
    
    
    public final Router getRouter(@Nullable RouterName name)

Gets details of a single Router.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       RouterName name = RouterName.of("[PROJECT]", "[LOCATION]", "[ZONE]", "[ROUTER]");
       Router response = edgeNetworkClient.getRouter(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.edgenetwork.v1.RouterName`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[Router](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Router)` |   
  
### getRouter(GetRouterRequest request)
    
    
    public final Router getRouter(GetRouterRequest request)

Gets details of a single Router.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       GetRouterRequest request =
           GetRouterRequest.newBuilder()
               .setName(RouterName.of("[PROJECT]", "[LOCATION]", "[ZONE]", "[ROUTER]").toString())
               .build();
       Router response = edgeNetworkClient.getRouter(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.GetRouterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Router](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Router)` |   
  
### getRouter(String name)
    
    
    public final Router getRouter(String name)

Gets details of a single Router.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       String name = RouterName.of("[PROJECT]", "[LOCATION]", "[ZONE]", "[ROUTER]").toString();
       Router response = edgeNetworkClient.getRouter(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[Router](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Router)` |   
  
### getRouterCallable()
    
    
    public final UnaryCallable<GetRouterRequest,Router> getRouterCallable()

Gets details of a single Router.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       GetRouterRequest request =
           GetRouterRequest.newBuilder()
               .setName(RouterName.of("[PROJECT]", "[LOCATION]", "[ZONE]", "[ROUTER]").toString())
               .build();
       ApiFuture<Router> future = edgeNetworkClient.getRouterCallable().futureCall(request);
       // Do something.
       Router response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.GetRouterRequest),[Router](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Router)>` |   
  
### getSettings()
    
    
    public final @Nullable EdgeNetworkSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.edgenetwork.v1.EdgeNetworkSettings` |   
  
### getStub()
    
    
    public EdgeNetworkStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[EdgeNetworkStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.stub.EdgeNetworkStub)` |   
  
### getSubnet(@Nullable SubnetName name)
    
    
    public final Subnet getSubnet(@Nullable SubnetName name)

Gets details of a single Subnet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       SubnetName name = SubnetName.of("[PROJECT]", "[LOCATION]", "[ZONE]", "[SUBNET]");
       Subnet response = edgeNetworkClient.getSubnet(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.edgenetwork.v1.SubnetName`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[Subnet](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Subnet)` |   
  
### getSubnet(GetSubnetRequest request)
    
    
    public final Subnet getSubnet(GetSubnetRequest request)

Gets details of a single Subnet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       GetSubnetRequest request =
           GetSubnetRequest.newBuilder()
               .setName(SubnetName.of("[PROJECT]", "[LOCATION]", "[ZONE]", "[SUBNET]").toString())
               .build();
       Subnet response = edgeNetworkClient.getSubnet(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSubnetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.GetSubnetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Subnet](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Subnet)` |   
  
### getSubnet(String name)
    
    
    public final Subnet getSubnet(String name)

Gets details of a single Subnet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       String name = SubnetName.of("[PROJECT]", "[LOCATION]", "[ZONE]", "[SUBNET]").toString();
       Subnet response = edgeNetworkClient.getSubnet(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[Subnet](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Subnet)` |   
  
### getSubnetCallable()
    
    
    public final UnaryCallable<GetSubnetRequest,Subnet> getSubnetCallable()

Gets details of a single Subnet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       GetSubnetRequest request =
           GetSubnetRequest.newBuilder()
               .setName(SubnetName.of("[PROJECT]", "[LOCATION]", "[ZONE]", "[SUBNET]").toString())
               .build();
       ApiFuture<Subnet> future = edgeNetworkClient.getSubnetCallable().futureCall(request);
       // Do something.
       Subnet response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetSubnetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.GetSubnetRequest),[Subnet](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Subnet)>` |   
  
### getZone(@Nullable ZoneName name) (deprecated)
    
    
    public final Zone getZone(@Nullable ZoneName name)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Deprecated: not implemented. Gets details of a single Zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       ZoneName name = ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]");
       Zone response = edgeNetworkClient.getZone(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.edgenetwork.v1.ZoneName`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[Zone](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Zone)` |   
  
### getZone(GetZoneRequest request) (deprecated)
    
    
    public final Zone getZone(GetZoneRequest request)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Deprecated: not implemented. Gets details of a single Zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       GetZoneRequest request =
           GetZoneRequest.newBuilder()
               .setName(ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString())
               .build();
       Zone response = edgeNetworkClient.getZone(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetZoneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.GetZoneRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Zone](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Zone)` |   
  
### getZone(String name) (deprecated)
    
    
    public final Zone getZone(String name)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Deprecated: not implemented. Gets details of a single Zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       String name = ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString();
       Zone response = edgeNetworkClient.getZone(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[Zone](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Zone)` |   
  
### getZoneCallable() (deprecated)
    
    
    public final UnaryCallable<GetZoneRequest,Zone> getZoneCallable()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Deprecated: not implemented. Gets details of a single Zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       GetZoneRequest request =
           GetZoneRequest.newBuilder()
               .setName(ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString())
               .build();
       ApiFuture<Zone> future = edgeNetworkClient.getZoneCallable().futureCall(request);
       // Do something.
       Zone response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetZoneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.GetZoneRequest),[Zone](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Zone)>` |   
  
### initializeZone(@Nullable ZoneName name)
    
    
    public final InitializeZoneResponse initializeZone(@Nullable ZoneName name)

InitializeZone will initialize resources for a zone in a project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       ZoneName name = ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]");
       InitializeZoneResponse response = edgeNetworkClient.initializeZone(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.edgenetwork.v1.ZoneName`  
Required. The name of the zone resource.  
**Returns**  
---  
**Type** | **Description**  
`[InitializeZoneResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.InitializeZoneResponse)` |   
  
### initializeZone(InitializeZoneRequest request)
    
    
    public final InitializeZoneResponse initializeZone(InitializeZoneRequest request)

InitializeZone will initialize resources for a zone in a project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       InitializeZoneRequest request =
           InitializeZoneRequest.newBuilder()
               .setName(ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString())
               .build();
       InitializeZoneResponse response = edgeNetworkClient.initializeZone(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InitializeZoneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.InitializeZoneRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[InitializeZoneResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.InitializeZoneResponse)` |   
  
### initializeZone(String name)
    
    
    public final InitializeZoneResponse initializeZone(String name)

InitializeZone will initialize resources for a zone in a project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       String name = ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString();
       InitializeZoneResponse response = edgeNetworkClient.initializeZone(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the zone resource.  
**Returns**  
---  
**Type** | **Description**  
`[InitializeZoneResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.InitializeZoneResponse)` |   
  
### initializeZoneCallable()
    
    
    public final UnaryCallable<InitializeZoneRequest,InitializeZoneResponse> initializeZoneCallable()

InitializeZone will initialize resources for a zone in a project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       InitializeZoneRequest request =
           InitializeZoneRequest.newBuilder()
               .setName(ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString())
               .build();
       ApiFuture<InitializeZoneResponse> future =
           edgeNetworkClient.initializeZoneCallable().futureCall(request);
       // Do something.
       InitializeZoneResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InitializeZoneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.InitializeZoneRequest),[InitializeZoneResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.InitializeZoneResponse)>` |   
  
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
  
### listInterconnectAttachments(@Nullable ZoneName parent)
    
    
    public final EdgeNetworkClient.ListInterconnectAttachmentsPagedResponse listInterconnectAttachments(@Nullable ZoneName parent)

Lists InterconnectAttachments in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       ZoneName parent = ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]");
       for (InterconnectAttachment element :
           edgeNetworkClient.listInterconnectAttachments(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.edgenetwork.v1.ZoneName`  
Required. Parent value for ListInterconnectAttachmentsRequest  
**Returns**  
---  
**Type** | **Description**  
`[EdgeNetworkClient.ListInterconnectAttachmentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkClient.ListInterconnectAttachmentsPagedResponse)` |   
  
### listInterconnectAttachments(ListInterconnectAttachmentsRequest request)
    
    
    public final EdgeNetworkClient.ListInterconnectAttachmentsPagedResponse listInterconnectAttachments(ListInterconnectAttachmentsRequest request)

Lists InterconnectAttachments in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       ListInterconnectAttachmentsRequest request =
           ListInterconnectAttachmentsRequest.newBuilder()
               .setParent(ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (InterconnectAttachment element :
           edgeNetworkClient.listInterconnectAttachments(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListInterconnectAttachmentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListInterconnectAttachmentsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[EdgeNetworkClient.ListInterconnectAttachmentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkClient.ListInterconnectAttachmentsPagedResponse)` |   
  
### listInterconnectAttachments(String parent)
    
    
    public final EdgeNetworkClient.ListInterconnectAttachmentsPagedResponse listInterconnectAttachments(String parent)

Lists InterconnectAttachments in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       String parent = ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString();
       for (InterconnectAttachment element :
           edgeNetworkClient.listInterconnectAttachments(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Parent value for ListInterconnectAttachmentsRequest  
**Returns**  
---  
**Type** | **Description**  
`[EdgeNetworkClient.ListInterconnectAttachmentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkClient.ListInterconnectAttachmentsPagedResponse)` |   
  
### listInterconnectAttachmentsCallable()
    
    
    public final UnaryCallable<ListInterconnectAttachmentsRequest,ListInterconnectAttachmentsResponse> listInterconnectAttachmentsCallable()

Lists InterconnectAttachments in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       ListInterconnectAttachmentsRequest request =
           ListInterconnectAttachmentsRequest.newBuilder()
               .setParent(ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListInterconnectAttachmentsResponse response =
             edgeNetworkClient.listInterconnectAttachmentsCallable().call(request);
         for (InterconnectAttachment element : response.getInterconnectAttachmentsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListInterconnectAttachmentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListInterconnectAttachmentsRequest),[ListInterconnectAttachmentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListInterconnectAttachmentsResponse)>` |   
  
### listInterconnectAttachmentsPagedCallable()
    
    
    public final UnaryCallable<ListInterconnectAttachmentsRequest,EdgeNetworkClient.ListInterconnectAttachmentsPagedResponse> listInterconnectAttachmentsPagedCallable()

Lists InterconnectAttachments in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       ListInterconnectAttachmentsRequest request =
           ListInterconnectAttachmentsRequest.newBuilder()
               .setParent(ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<InterconnectAttachment> future =
           edgeNetworkClient.listInterconnectAttachmentsPagedCallable().futureCall(request);
       // Do something.
       for (InterconnectAttachment element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListInterconnectAttachmentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListInterconnectAttachmentsRequest),[ListInterconnectAttachmentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkClient.ListInterconnectAttachmentsPagedResponse)>` |   
  
### listInterconnects(@Nullable ZoneName parent)
    
    
    public final EdgeNetworkClient.ListInterconnectsPagedResponse listInterconnects(@Nullable ZoneName parent)

Lists Interconnects in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       ZoneName parent = ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]");
       for (Interconnect element : edgeNetworkClient.listInterconnects(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.edgenetwork.v1.ZoneName`  
Required. Parent value for ListInterconnectsRequest  
**Returns**  
---  
**Type** | **Description**  
`[EdgeNetworkClient.ListInterconnectsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkClient.ListInterconnectsPagedResponse)` |   
  
### listInterconnects(ListInterconnectsRequest request)
    
    
    public final EdgeNetworkClient.ListInterconnectsPagedResponse listInterconnects(ListInterconnectsRequest request)

Lists Interconnects in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       ListInterconnectsRequest request =
           ListInterconnectsRequest.newBuilder()
               .setParent(ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Interconnect element : edgeNetworkClient.listInterconnects(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListInterconnectsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListInterconnectsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[EdgeNetworkClient.ListInterconnectsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkClient.ListInterconnectsPagedResponse)` |   
  
### listInterconnects(String parent)
    
    
    public final EdgeNetworkClient.ListInterconnectsPagedResponse listInterconnects(String parent)

Lists Interconnects in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       String parent = ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString();
       for (Interconnect element : edgeNetworkClient.listInterconnects(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Parent value for ListInterconnectsRequest  
**Returns**  
---  
**Type** | **Description**  
`[EdgeNetworkClient.ListInterconnectsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkClient.ListInterconnectsPagedResponse)` |   
  
### listInterconnectsCallable()
    
    
    public final UnaryCallable<ListInterconnectsRequest,ListInterconnectsResponse> listInterconnectsCallable()

Lists Interconnects in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       ListInterconnectsRequest request =
           ListInterconnectsRequest.newBuilder()
               .setParent(ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListInterconnectsResponse response =
             edgeNetworkClient.listInterconnectsCallable().call(request);
         for (Interconnect element : response.getInterconnectsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListInterconnectsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListInterconnectsRequest),[ListInterconnectsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListInterconnectsResponse)>` |   
  
### listInterconnectsPagedCallable()
    
    
    public final UnaryCallable<ListInterconnectsRequest,EdgeNetworkClient.ListInterconnectsPagedResponse> listInterconnectsPagedCallable()

Lists Interconnects in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       ListInterconnectsRequest request =
           ListInterconnectsRequest.newBuilder()
               .setParent(ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Interconnect> future =
           edgeNetworkClient.listInterconnectsPagedCallable().futureCall(request);
       // Do something.
       for (Interconnect element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListInterconnectsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListInterconnectsRequest),[ListInterconnectsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkClient.ListInterconnectsPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final EdgeNetworkClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : edgeNetworkClient.listLocations(request).iterateAll()) {
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
`[EdgeNetworkClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response = edgeNetworkClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,EdgeNetworkClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           edgeNetworkClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkClient.ListLocationsPagedResponse)>` |   
  
### listNetworks(@Nullable ZoneName parent)
    
    
    public final EdgeNetworkClient.ListNetworksPagedResponse listNetworks(@Nullable ZoneName parent)

Lists Networks in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       ZoneName parent = ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]");
       for (Network element : edgeNetworkClient.listNetworks(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.edgenetwork.v1.ZoneName`  
Required. Parent value for ListNetworksRequest  
**Returns**  
---  
**Type** | **Description**  
`[EdgeNetworkClient.ListNetworksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkClient.ListNetworksPagedResponse)` |   
  
### listNetworks(ListNetworksRequest request)
    
    
    public final EdgeNetworkClient.ListNetworksPagedResponse listNetworks(ListNetworksRequest request)

Lists Networks in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       ListNetworksRequest request =
           ListNetworksRequest.newBuilder()
               .setParent(ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Network element : edgeNetworkClient.listNetworks(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListNetworksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListNetworksRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[EdgeNetworkClient.ListNetworksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkClient.ListNetworksPagedResponse)` |   
  
### listNetworks(String parent)
    
    
    public final EdgeNetworkClient.ListNetworksPagedResponse listNetworks(String parent)

Lists Networks in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       String parent = ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString();
       for (Network element : edgeNetworkClient.listNetworks(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Parent value for ListNetworksRequest  
**Returns**  
---  
**Type** | **Description**  
`[EdgeNetworkClient.ListNetworksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkClient.ListNetworksPagedResponse)` |   
  
### listNetworksCallable()
    
    
    public final UnaryCallable<ListNetworksRequest,ListNetworksResponse> listNetworksCallable()

Lists Networks in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       ListNetworksRequest request =
           ListNetworksRequest.newBuilder()
               .setParent(ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListNetworksResponse response = edgeNetworkClient.listNetworksCallable().call(request);
         for (Network element : response.getNetworksList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListNetworksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListNetworksRequest),[ListNetworksResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListNetworksResponse)>` |   
  
### listNetworksPagedCallable()
    
    
    public final UnaryCallable<ListNetworksRequest,EdgeNetworkClient.ListNetworksPagedResponse> listNetworksPagedCallable()

Lists Networks in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       ListNetworksRequest request =
           ListNetworksRequest.newBuilder()
               .setParent(ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Network> future = edgeNetworkClient.listNetworksPagedCallable().futureCall(request);
       // Do something.
       for (Network element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListNetworksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListNetworksRequest),[ListNetworksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkClient.ListNetworksPagedResponse)>` |   
  
### listRouters(@Nullable ZoneName parent)
    
    
    public final EdgeNetworkClient.ListRoutersPagedResponse listRouters(@Nullable ZoneName parent)

Lists Routers in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       ZoneName parent = ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]");
       for (Router element : edgeNetworkClient.listRouters(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.edgenetwork.v1.ZoneName`  
Required. Parent value for ListRoutersRequest  
**Returns**  
---  
**Type** | **Description**  
`[EdgeNetworkClient.ListRoutersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkClient.ListRoutersPagedResponse)` |   
  
### listRouters(ListRoutersRequest request)
    
    
    public final EdgeNetworkClient.ListRoutersPagedResponse listRouters(ListRoutersRequest request)

Lists Routers in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       ListRoutersRequest request =
           ListRoutersRequest.newBuilder()
               .setParent(ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Router element : edgeNetworkClient.listRouters(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListRoutersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListRoutersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[EdgeNetworkClient.ListRoutersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkClient.ListRoutersPagedResponse)` |   
  
### listRouters(String parent)
    
    
    public final EdgeNetworkClient.ListRoutersPagedResponse listRouters(String parent)

Lists Routers in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       String parent = ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString();
       for (Router element : edgeNetworkClient.listRouters(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Parent value for ListRoutersRequest  
**Returns**  
---  
**Type** | **Description**  
`[EdgeNetworkClient.ListRoutersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkClient.ListRoutersPagedResponse)` |   
  
### listRoutersCallable()
    
    
    public final UnaryCallable<ListRoutersRequest,ListRoutersResponse> listRoutersCallable()

Lists Routers in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       ListRoutersRequest request =
           ListRoutersRequest.newBuilder()
               .setParent(ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListRoutersResponse response = edgeNetworkClient.listRoutersCallable().call(request);
         for (Router element : response.getRoutersList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRoutersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListRoutersRequest),[ListRoutersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListRoutersResponse)>` |   
  
### listRoutersPagedCallable()
    
    
    public final UnaryCallable<ListRoutersRequest,EdgeNetworkClient.ListRoutersPagedResponse> listRoutersPagedCallable()

Lists Routers in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       ListRoutersRequest request =
           ListRoutersRequest.newBuilder()
               .setParent(ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Router> future = edgeNetworkClient.listRoutersPagedCallable().futureCall(request);
       // Do something.
       for (Router element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRoutersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListRoutersRequest),[ListRoutersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkClient.ListRoutersPagedResponse)>` |   
  
### listSubnets(@Nullable ZoneName parent)
    
    
    public final EdgeNetworkClient.ListSubnetsPagedResponse listSubnets(@Nullable ZoneName parent)

Lists Subnets in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       ZoneName parent = ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]");
       for (Subnet element : edgeNetworkClient.listSubnets(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.edgenetwork.v1.ZoneName`  
Required. Parent value for ListSubnetsRequest  
**Returns**  
---  
**Type** | **Description**  
`[EdgeNetworkClient.ListSubnetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkClient.ListSubnetsPagedResponse)` |   
  
### listSubnets(ListSubnetsRequest request)
    
    
    public final EdgeNetworkClient.ListSubnetsPagedResponse listSubnets(ListSubnetsRequest request)

Lists Subnets in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       ListSubnetsRequest request =
           ListSubnetsRequest.newBuilder()
               .setParent(ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Subnet element : edgeNetworkClient.listSubnets(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListSubnetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListSubnetsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[EdgeNetworkClient.ListSubnetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkClient.ListSubnetsPagedResponse)` |   
  
### listSubnets(String parent)
    
    
    public final EdgeNetworkClient.ListSubnetsPagedResponse listSubnets(String parent)

Lists Subnets in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       String parent = ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString();
       for (Subnet element : edgeNetworkClient.listSubnets(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Parent value for ListSubnetsRequest  
**Returns**  
---  
**Type** | **Description**  
`[EdgeNetworkClient.ListSubnetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkClient.ListSubnetsPagedResponse)` |   
  
### listSubnetsCallable()
    
    
    public final UnaryCallable<ListSubnetsRequest,ListSubnetsResponse> listSubnetsCallable()

Lists Subnets in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       ListSubnetsRequest request =
           ListSubnetsRequest.newBuilder()
               .setParent(ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListSubnetsResponse response = edgeNetworkClient.listSubnetsCallable().call(request);
         for (Subnet element : response.getSubnetsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSubnetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListSubnetsRequest),[ListSubnetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListSubnetsResponse)>` |   
  
### listSubnetsPagedCallable()
    
    
    public final UnaryCallable<ListSubnetsRequest,EdgeNetworkClient.ListSubnetsPagedResponse> listSubnetsPagedCallable()

Lists Subnets in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       ListSubnetsRequest request =
           ListSubnetsRequest.newBuilder()
               .setParent(ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Subnet> future = edgeNetworkClient.listSubnetsPagedCallable().futureCall(request);
       // Do something.
       for (Subnet element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSubnetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListSubnetsRequest),[ListSubnetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkClient.ListSubnetsPagedResponse)>` |   
  
### listZones(@Nullable LocationName parent) (deprecated)
    
    
    public final EdgeNetworkClient.ListZonesPagedResponse listZones(@Nullable LocationName parent)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Deprecated: not implemented. Lists Zones in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Zone element : edgeNetworkClient.listZones(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.edgenetwork.v1.LocationName`  
Required. Parent value for ListZonesRequest  
**Returns**  
---  
**Type** | **Description**  
`[EdgeNetworkClient.ListZonesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkClient.ListZonesPagedResponse)` |   
  
### listZones(ListZonesRequest request) (deprecated)
    
    
    public final EdgeNetworkClient.ListZonesPagedResponse listZones(ListZonesRequest request)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Deprecated: not implemented. Lists Zones in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       ListZonesRequest request =
           ListZonesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Zone element : edgeNetworkClient.listZones(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListZonesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListZonesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[EdgeNetworkClient.ListZonesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkClient.ListZonesPagedResponse)` |   
  
### listZones(String parent) (deprecated)
    
    
    public final EdgeNetworkClient.ListZonesPagedResponse listZones(String parent)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Deprecated: not implemented. Lists Zones in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Zone element : edgeNetworkClient.listZones(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Parent value for ListZonesRequest  
**Returns**  
---  
**Type** | **Description**  
`[EdgeNetworkClient.ListZonesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkClient.ListZonesPagedResponse)` |   
  
### listZonesCallable() (deprecated)
    
    
    public final UnaryCallable<ListZonesRequest,ListZonesResponse> listZonesCallable()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Deprecated: not implemented. Lists Zones in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       ListZonesRequest request =
           ListZonesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListZonesResponse response = edgeNetworkClient.listZonesCallable().call(request);
         for (Zone element : response.getZonesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListZonesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListZonesRequest),[ListZonesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListZonesResponse)>` |   
  
### listZonesPagedCallable() (deprecated)
    
    
    public final UnaryCallable<ListZonesRequest,EdgeNetworkClient.ListZonesPagedResponse> listZonesPagedCallable()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Deprecated: not implemented. Lists Zones in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       ListZonesRequest request =
           ListZonesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Zone> future = edgeNetworkClient.listZonesPagedCallable().futureCall(request);
       // Do something.
       for (Zone element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListZonesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListZonesRequest),[ListZonesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkClient.ListZonesPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateRouterAsync(Router router, FieldMask updateMask)
    
    
    public final OperationFuture<Router,OperationMetadata> updateRouterAsync(Router router, FieldMask updateMask)

Updates the parameters of a single Router.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       Router router = Router.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Router response = edgeNetworkClient.updateRouterAsync(router, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`router` | `[Router](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Router)`  
Required. The resource being updated  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the Router resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Router](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Router),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.OperationMetadata)>` |   
  
### updateRouterAsync(UpdateRouterRequest request)
    
    
    public final OperationFuture<Router,OperationMetadata> updateRouterAsync(UpdateRouterRequest request)

Updates the parameters of a single Router.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       UpdateRouterRequest request =
           UpdateRouterRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setRouter(Router.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Router response = edgeNetworkClient.updateRouterAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.UpdateRouterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Router](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Router),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.OperationMetadata)>` |   
  
### updateRouterCallable()
    
    
    public final UnaryCallable<UpdateRouterRequest,Operation> updateRouterCallable()

Updates the parameters of a single Router.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       UpdateRouterRequest request =
           UpdateRouterRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setRouter(Router.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = edgeNetworkClient.updateRouterCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.UpdateRouterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateRouterOperationCallable()
    
    
    public final OperationCallable<UpdateRouterRequest,Router,OperationMetadata> updateRouterOperationCallable()

Updates the parameters of a single Router.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       UpdateRouterRequest request =
           UpdateRouterRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setRouter(Router.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Router, OperationMetadata> future =
           edgeNetworkClient.updateRouterOperationCallable().futureCall(request);
       // Do something.
       Router response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.UpdateRouterRequest),[Router](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Router),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.OperationMetadata)>` |   
  
### updateSubnetAsync(Subnet subnet, FieldMask updateMask)
    
    
    public final OperationFuture<Subnet,OperationMetadata> updateSubnetAsync(Subnet subnet, FieldMask updateMask)

Updates the parameters of a single Subnet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       Subnet subnet = Subnet.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Subnet response = edgeNetworkClient.updateSubnetAsync(subnet, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`subnet` | `[Subnet](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Subnet)`  
Required. The resource being updated  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the Subnet resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Subnet](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Subnet),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.OperationMetadata)>` |   
  
### updateSubnetAsync(UpdateSubnetRequest request)
    
    
    public final OperationFuture<Subnet,OperationMetadata> updateSubnetAsync(UpdateSubnetRequest request)

Updates the parameters of a single Subnet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       UpdateSubnetRequest request =
           UpdateSubnetRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setSubnet(Subnet.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Subnet response = edgeNetworkClient.updateSubnetAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateSubnetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.UpdateSubnetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Subnet](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Subnet),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.OperationMetadata)>` |   
  
### updateSubnetCallable()
    
    
    public final UnaryCallable<UpdateSubnetRequest,Operation> updateSubnetCallable()

Updates the parameters of a single Subnet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       UpdateSubnetRequest request =
           UpdateSubnetRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setSubnet(Subnet.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = edgeNetworkClient.updateSubnetCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateSubnetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.UpdateSubnetRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateSubnetOperationCallable()
    
    
    public final OperationCallable<UpdateSubnetRequest,Subnet,OperationMetadata> updateSubnetOperationCallable()

Updates the parameters of a single Subnet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EdgeNetworkClient edgeNetworkClient = EdgeNetworkClient.create()) {
       UpdateSubnetRequest request =
           UpdateSubnetRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setSubnet(Subnet.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Subnet, OperationMetadata> future =
           edgeNetworkClient.updateSubnetOperationCallable().futureCall(request);
       // Do something.
       Subnet response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateSubnetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.UpdateSubnetRequest),[Subnet](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Subnet),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.OperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
