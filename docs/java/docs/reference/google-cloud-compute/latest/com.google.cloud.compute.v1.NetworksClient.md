---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworksClient
title: Class NetworksClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:03:09.495235+00:00
---

# Class NetworksClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworksClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class NetworksClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/NetworksClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The Networks API.

This client uses Networks version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworksClient networksClient = NetworksClient.create()) {
       String project = "project-309310695";
       String network = "network1843485230";
       Network response = networksClient.get(project, network);
     }
     

Note: close() needs to be called on the NetworksClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
AddPeering |  Adds a peering to the specified network. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * addPeeringAsync(AddPeeringNetworkRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * addPeeringAsync(String project, String network, NetworksAddPeeringRequest networksAddPeeringRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * addPeeringOperationCallable() 
  * addPeeringCallable() 

  
CancelRequestRemovePeering |  Cancel requests to remove a peering from the specified network. Applicable only for PeeringConnection with update_strategy=CONSENSUS. Cancels a request to remove a peering from the specified network. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * cancelRequestRemovePeeringAsync(CancelRequestRemovePeeringNetworkRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * cancelRequestRemovePeeringAsync(String project, String network, NetworksCancelRequestRemovePeeringRequest networksCancelRequestRemovePeeringRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * cancelRequestRemovePeeringOperationCallable() 
  * cancelRequestRemovePeeringCallable() 

  
Delete |  Deletes the specified network. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteNetworkRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String network) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
Get |  Returns the specified network. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetNetworkRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String network) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
GetEffectiveFirewalls |  Returns the effective firewalls on a given network. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getEffectiveFirewalls(GetEffectiveFirewallsNetworkRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getEffectiveFirewalls(String project, String network) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getEffectiveFirewallsCallable() 

  
Insert |  Creates a network in the specified project using the data included in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertNetworkRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, Network networkResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Retrieves the list of networks available to the specified project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListNetworksRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
ListPeeringRoutes |  Lists the peering routes exchanged over peering connection. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listPeeringRoutes(ListPeeringRoutesNetworksRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listPeeringRoutes(String project, String network) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPeeringRoutesPagedCallable() 
  * listPeeringRoutesCallable() 

  
Patch |  Patches the specified network with the data included in the request. Only routingConfig can be modified. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * patchAsync(PatchNetworkRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * patchAsync(String project, String network, Network networkResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * patchOperationCallable() 
  * patchCallable() 

  
RemovePeering |  Removes a peering from the specified network. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * removePeeringAsync(RemovePeeringNetworkRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * removePeeringAsync(String project, String network, NetworksRemovePeeringRequest networksRemovePeeringRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * removePeeringOperationCallable() 
  * removePeeringCallable() 

  
RequestRemovePeering |  Requests to remove a peering from the specified network. Applicable only for PeeringConnection with update_strategy=CONSENSUS. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * requestRemovePeeringAsync(String project, String network, NetworksRequestRemovePeeringRequest networksRequestRemovePeeringRequestResource) 
  * requestRemovePeeringAsync(RequestRemovePeeringNetworkRequest request) 
  * requestRemovePeeringOperationCallable() 
  * requestRemovePeeringCallable() 

  
SwitchToCustomMode |  Switches the network mode from auto subnet mode to custom subnet mode. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * switchToCustomModeAsync(SwitchToCustomModeNetworkRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * switchToCustomModeAsync(String project, String network) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * switchToCustomModeOperationCallable() 
  * switchToCustomModeCallable() 

  
UpdatePeering |  Updates the specified network peering with the data included in the request. You can only modify the NetworkPeering.export_custom_routes field and the NetworkPeering.import_custom_routes field. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updatePeeringAsync(UpdatePeeringNetworkRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updatePeeringAsync(String project, String network, NetworksUpdatePeeringRequest networksUpdatePeeringRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updatePeeringOperationCallable() 
  * updatePeeringCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of NetworksSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     NetworksSettings networksSettings =
         NetworksSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     NetworksClient networksClient = NetworksClient.create(networksSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     NetworksSettings networksSettings =
         NetworksSettings.newBuilder().setEndpoint(myEndpoint).build();
     NetworksClient networksClient = NetworksClient.create(networksSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > NetworksClient

## Static Methods 

### create()
    
    
    public static final NetworksClient create()

Constructs an instance of NetworksClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[NetworksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworksClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(NetworksSettings settings)
    
    
    public static final NetworksClient create(NetworksSettings settings)

Constructs an instance of NetworksClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[NetworksSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworksSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NetworksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworksClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(NetworksStub stub)
    
    
    public static final NetworksClient create(NetworksStub stub)

Constructs an instance of NetworksClient, using the given stub for making calls. This is for advanced usage - prefer using create(NetworksSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[NetworksStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.NetworksStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NetworksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworksClient)` |   
  
## Constructors 

### NetworksClient(NetworksSettings settings)
    
    
    protected NetworksClient(NetworksSettings settings)

Constructs an instance of NetworksClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[NetworksSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworksSettings)`  
  
  
### NetworksClient(NetworksStub stub)
    
    
    protected NetworksClient(NetworksStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[NetworksStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.NetworksStub)`  
  
  
## Methods 

### addPeeringAsync(AddPeeringNetworkRequest request)
    
    
    public final OperationFuture<Operation,Operation> addPeeringAsync(AddPeeringNetworkRequest request)

Adds a peering to the specified network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworksClient networksClient = NetworksClient.create()) {
       AddPeeringNetworkRequest request =
           AddPeeringNetworkRequest.newBuilder()
               .setNetwork("network1843485230")
               .setNetworksAddPeeringRequestResource(NetworksAddPeeringRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response = networksClient.addPeeringAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AddPeeringNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddPeeringNetworkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addPeeringAsync(String project, String network, NetworksAddPeeringRequest networksAddPeeringRequestResource)
    
    
    public final OperationFuture<Operation,Operation> addPeeringAsync(String project, String network, NetworksAddPeeringRequest networksAddPeeringRequestResource)

Adds a peering to the specified network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworksClient networksClient = NetworksClient.create()) {
       String project = "project-309310695";
       String network = "network1843485230";
       NetworksAddPeeringRequest networksAddPeeringRequestResource =
           NetworksAddPeeringRequest.newBuilder().build();
       Operation response =
           networksClient.addPeeringAsync(project, network, networksAddPeeringRequestResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`network` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the network resource to add peering to.  
`networksAddPeeringRequestResource` | `[NetworksAddPeeringRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworksAddPeeringRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addPeeringCallable()
    
    
    public final UnaryCallable<AddPeeringNetworkRequest,Operation> addPeeringCallable()

Adds a peering to the specified network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworksClient networksClient = NetworksClient.create()) {
       AddPeeringNetworkRequest request =
           AddPeeringNetworkRequest.newBuilder()
               .setNetwork("network1843485230")
               .setNetworksAddPeeringRequestResource(NetworksAddPeeringRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = networksClient.addPeeringCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AddPeeringNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddPeeringNetworkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addPeeringOperationCallable()
    
    
    public final OperationCallable<AddPeeringNetworkRequest,Operation,Operation> addPeeringOperationCallable()

Adds a peering to the specified network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworksClient networksClient = NetworksClient.create()) {
       AddPeeringNetworkRequest request =
           AddPeeringNetworkRequest.newBuilder()
               .setNetwork("network1843485230")
               .setNetworksAddPeeringRequestResource(NetworksAddPeeringRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           networksClient.addPeeringOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[AddPeeringNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddPeeringNetworkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### cancelRequestRemovePeeringAsync(CancelRequestRemovePeeringNetworkRequest request)
    
    
    public final OperationFuture<Operation,Operation> cancelRequestRemovePeeringAsync(CancelRequestRemovePeeringNetworkRequest request)

Cancel requests to remove a peering from the specified network. Applicable only for PeeringConnection with update_strategy=CONSENSUS. Cancels a request to remove a peering from the specified network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworksClient networksClient = NetworksClient.create()) {
       CancelRequestRemovePeeringNetworkRequest request =
           CancelRequestRemovePeeringNetworkRequest.newBuilder()
               .setNetwork("network1843485230")
               .setNetworksCancelRequestRemovePeeringRequestResource(
                   NetworksCancelRequestRemovePeeringRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response = networksClient.cancelRequestRemovePeeringAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CancelRequestRemovePeeringNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CancelRequestRemovePeeringNetworkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### cancelRequestRemovePeeringAsync(String project, String network, NetworksCancelRequestRemovePeeringRequest networksCancelRequestRemovePeeringRequestResource)
    
    
    public final OperationFuture<Operation,Operation> cancelRequestRemovePeeringAsync(String project, String network, NetworksCancelRequestRemovePeeringRequest networksCancelRequestRemovePeeringRequestResource)

Cancel requests to remove a peering from the specified network. Applicable only for PeeringConnection with update_strategy=CONSENSUS. Cancels a request to remove a peering from the specified network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworksClient networksClient = NetworksClient.create()) {
       String project = "project-309310695";
       String network = "network1843485230";
       NetworksCancelRequestRemovePeeringRequest networksCancelRequestRemovePeeringRequestResource =
           NetworksCancelRequestRemovePeeringRequest.newBuilder().build();
       Operation response =
           networksClient
               .cancelRequestRemovePeeringAsync(
                   project, network, networksCancelRequestRemovePeeringRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`network` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the network resource to remove peering from.  
`networksCancelRequestRemovePeeringRequestResource` | `[NetworksCancelRequestRemovePeeringRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworksCancelRequestRemovePeeringRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### cancelRequestRemovePeeringCallable()
    
    
    public final UnaryCallable<CancelRequestRemovePeeringNetworkRequest,Operation> cancelRequestRemovePeeringCallable()

Cancel requests to remove a peering from the specified network. Applicable only for PeeringConnection with update_strategy=CONSENSUS. Cancels a request to remove a peering from the specified network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworksClient networksClient = NetworksClient.create()) {
       CancelRequestRemovePeeringNetworkRequest request =
           CancelRequestRemovePeeringNetworkRequest.newBuilder()
               .setNetwork("network1843485230")
               .setNetworksCancelRequestRemovePeeringRequestResource(
                   NetworksCancelRequestRemovePeeringRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           networksClient.cancelRequestRemovePeeringCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CancelRequestRemovePeeringNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CancelRequestRemovePeeringNetworkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### cancelRequestRemovePeeringOperationCallable()
    
    
    public final OperationCallable<CancelRequestRemovePeeringNetworkRequest,Operation,Operation> cancelRequestRemovePeeringOperationCallable()

Cancel requests to remove a peering from the specified network. Applicable only for PeeringConnection with update_strategy=CONSENSUS. Cancels a request to remove a peering from the specified network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworksClient networksClient = NetworksClient.create()) {
       CancelRequestRemovePeeringNetworkRequest request =
           CancelRequestRemovePeeringNetworkRequest.newBuilder()
               .setNetwork("network1843485230")
               .setNetworksCancelRequestRemovePeeringRequestResource(
                   NetworksCancelRequestRemovePeeringRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           networksClient.cancelRequestRemovePeeringOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CancelRequestRemovePeeringNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CancelRequestRemovePeeringNetworkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### close()
    
    
    public final void close()

### deleteAsync(DeleteNetworkRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteNetworkRequest request)

Deletes the specified network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworksClient networksClient = NetworksClient.create()) {
       DeleteNetworkRequest request =
           DeleteNetworkRequest.newBuilder()
               .setNetwork("network1843485230")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response = networksClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteNetworkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String network)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String network)

Deletes the specified network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworksClient networksClient = NetworksClient.create()) {
       String project = "project-309310695";
       String network = "network1843485230";
       Operation response = networksClient.deleteAsync(project, network).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`network` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the network to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteNetworkRequest,Operation> deleteCallable()

Deletes the specified network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworksClient networksClient = NetworksClient.create()) {
       DeleteNetworkRequest request =
           DeleteNetworkRequest.newBuilder()
               .setNetwork("network1843485230")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = networksClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteNetworkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteNetworkRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworksClient networksClient = NetworksClient.create()) {
       DeleteNetworkRequest request =
           DeleteNetworkRequest.newBuilder()
               .setNetwork("network1843485230")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           networksClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteNetworkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetNetworkRequest request)
    
    
    public final Network get(GetNetworkRequest request)

Returns the specified network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworksClient networksClient = NetworksClient.create()) {
       GetNetworkRequest request =
           GetNetworkRequest.newBuilder()
               .setNetwork("network1843485230")
               .setProject("project-309310695")
               .build();
       Network response = networksClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetNetworkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Network](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Network)` |   
  
### get(String project, String network)
    
    
    public final Network get(String project, String network)

Returns the specified network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworksClient networksClient = NetworksClient.create()) {
       String project = "project-309310695";
       String network = "network1843485230";
       Network response = networksClient.get(project, network);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`network` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the network to return.  
**Returns**  
---  
**Type** | **Description**  
`[Network](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Network)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetNetworkRequest,Network> getCallable()

Returns the specified network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworksClient networksClient = NetworksClient.create()) {
       GetNetworkRequest request =
           GetNetworkRequest.newBuilder()
               .setNetwork("network1843485230")
               .setProject("project-309310695")
               .build();
       ApiFuture<Network> future = networksClient.getCallable().futureCall(request);
       // Do something.
       Network response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetNetworkRequest),[Network](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Network)>` |   
  
### getEffectiveFirewalls(GetEffectiveFirewallsNetworkRequest request)
    
    
    public final NetworksGetEffectiveFirewallsResponse getEffectiveFirewalls(GetEffectiveFirewallsNetworkRequest request)

Returns the effective firewalls on a given network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworksClient networksClient = NetworksClient.create()) {
       GetEffectiveFirewallsNetworkRequest request =
           GetEffectiveFirewallsNetworkRequest.newBuilder()
               .setNetwork("network1843485230")
               .setProject("project-309310695")
               .build();
       NetworksGetEffectiveFirewallsResponse response =
           networksClient.getEffectiveFirewalls(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetEffectiveFirewallsNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetEffectiveFirewallsNetworkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NetworksGetEffectiveFirewallsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworksGetEffectiveFirewallsResponse)` |   
  
### getEffectiveFirewalls(String project, String network)
    
    
    public final NetworksGetEffectiveFirewallsResponse getEffectiveFirewalls(String project, String network)

Returns the effective firewalls on a given network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworksClient networksClient = NetworksClient.create()) {
       String project = "project-309310695";
       String network = "network1843485230";
       NetworksGetEffectiveFirewallsResponse response =
           networksClient.getEffectiveFirewalls(project, network);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`network` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the network for this request.  
**Returns**  
---  
**Type** | **Description**  
`[NetworksGetEffectiveFirewallsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworksGetEffectiveFirewallsResponse)` |   
  
### getEffectiveFirewallsCallable()
    
    
    public final UnaryCallable<GetEffectiveFirewallsNetworkRequest,NetworksGetEffectiveFirewallsResponse> getEffectiveFirewallsCallable()

Returns the effective firewalls on a given network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworksClient networksClient = NetworksClient.create()) {
       GetEffectiveFirewallsNetworkRequest request =
           GetEffectiveFirewallsNetworkRequest.newBuilder()
               .setNetwork("network1843485230")
               .setProject("project-309310695")
               .build();
       ApiFuture<NetworksGetEffectiveFirewallsResponse> future =
           networksClient.getEffectiveFirewallsCallable().futureCall(request);
       // Do something.
       NetworksGetEffectiveFirewallsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetEffectiveFirewallsNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetEffectiveFirewallsNetworkRequest),[NetworksGetEffectiveFirewallsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworksGetEffectiveFirewallsResponse)>` |   
  
### getSettings()
    
    
    public final @Nullable NetworksSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.NetworksSettings` |   
  
### getStub()
    
    
    public NetworksStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[NetworksStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.NetworksStub)` |   
  
### insertAsync(InsertNetworkRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertNetworkRequest request)

Creates a network in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworksClient networksClient = NetworksClient.create()) {
       InsertNetworkRequest request =
           InsertNetworkRequest.newBuilder()
               .setNetworkResource(Network.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response = networksClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertNetworkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, Network networkResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, Network networkResource)

Creates a network in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworksClient networksClient = NetworksClient.create()) {
       String project = "project-309310695";
       Network networkResource = Network.newBuilder().build();
       Operation response = networksClient.insertAsync(project, networkResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`networkResource` | `[Network](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Network)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertNetworkRequest,Operation> insertCallable()

Creates a network in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworksClient networksClient = NetworksClient.create()) {
       InsertNetworkRequest request =
           InsertNetworkRequest.newBuilder()
               .setNetworkResource(Network.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = networksClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertNetworkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertNetworkRequest,Operation,Operation> insertOperationCallable()

Creates a network in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworksClient networksClient = NetworksClient.create()) {
       InsertNetworkRequest request =
           InsertNetworkRequest.newBuilder()
               .setNetworkResource(Network.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           networksClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertNetworkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListNetworksRequest request)
    
    
    public final NetworksClient.ListPagedResponse list(ListNetworksRequest request)

Retrieves the list of networks available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworksClient networksClient = NetworksClient.create()) {
       ListNetworksRequest request =
           ListNetworksRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       for (Network element : networksClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListNetworksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListNetworksRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NetworksClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworksClient.ListPagedResponse)` |   
  
### list(String project)
    
    
    public final NetworksClient.ListPagedResponse list(String project)

Retrieves the list of networks available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworksClient networksClient = NetworksClient.create()) {
       String project = "project-309310695";
       for (Network element : networksClient.list(project).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
**Returns**  
---  
**Type** | **Description**  
`[NetworksClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworksClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListNetworksRequest,NetworkList> listCallable()

Retrieves the list of networks available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworksClient networksClient = NetworksClient.create()) {
       ListNetworksRequest request =
           ListNetworksRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       while (true) {
         NetworkList response = networksClient.listCallable().call(request);
         for (Network element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListNetworksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListNetworksRequest),[NetworkList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkList)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListNetworksRequest,NetworksClient.ListPagedResponse> listPagedCallable()

Retrieves the list of networks available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworksClient networksClient = NetworksClient.create()) {
       ListNetworksRequest request =
           ListNetworksRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       ApiFuture<Network> future = networksClient.listPagedCallable().futureCall(request);
       // Do something.
       for (Network element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListNetworksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListNetworksRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworksClient.ListPagedResponse)>` |   
  
### listPeeringRoutes(ListPeeringRoutesNetworksRequest request)
    
    
    public final NetworksClient.ListPeeringRoutesPagedResponse listPeeringRoutes(ListPeeringRoutesNetworksRequest request)

Lists the peering routes exchanged over peering connection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworksClient networksClient = NetworksClient.create()) {
       ListPeeringRoutesNetworksRequest request =
           ListPeeringRoutesNetworksRequest.newBuilder()
               .setDirection("direction-962590849")
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setNetwork("network1843485230")
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setPeeringName("peeringName-1170120213")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       for (ExchangedPeeringRoute element : networksClient.listPeeringRoutes(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListPeeringRoutesNetworksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListPeeringRoutesNetworksRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NetworksClient.ListPeeringRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworksClient.ListPeeringRoutesPagedResponse)` |   
  
### listPeeringRoutes(String project, String network)
    
    
    public final NetworksClient.ListPeeringRoutesPagedResponse listPeeringRoutes(String project, String network)

Lists the peering routes exchanged over peering connection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworksClient networksClient = NetworksClient.create()) {
       String project = "project-309310695";
       String network = "network1843485230";
       for (ExchangedPeeringRoute element :
           networksClient.listPeeringRoutes(project, network).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`network` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the network for this request.  
**Returns**  
---  
**Type** | **Description**  
`[NetworksClient.ListPeeringRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworksClient.ListPeeringRoutesPagedResponse)` |   
  
### listPeeringRoutesCallable()
    
    
    public final UnaryCallable<ListPeeringRoutesNetworksRequest,ExchangedPeeringRoutesList> listPeeringRoutesCallable()

Lists the peering routes exchanged over peering connection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworksClient networksClient = NetworksClient.create()) {
       ListPeeringRoutesNetworksRequest request =
           ListPeeringRoutesNetworksRequest.newBuilder()
               .setDirection("direction-962590849")
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setNetwork("network1843485230")
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setPeeringName("peeringName-1170120213")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       while (true) {
         ExchangedPeeringRoutesList response =
             networksClient.listPeeringRoutesCallable().call(request);
         for (ExchangedPeeringRoute element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPeeringRoutesNetworksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListPeeringRoutesNetworksRequest),[ExchangedPeeringRoutesList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ExchangedPeeringRoutesList)>` |   
  
### listPeeringRoutesPagedCallable()
    
    
    public final UnaryCallable<ListPeeringRoutesNetworksRequest,NetworksClient.ListPeeringRoutesPagedResponse> listPeeringRoutesPagedCallable()

Lists the peering routes exchanged over peering connection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworksClient networksClient = NetworksClient.create()) {
       ListPeeringRoutesNetworksRequest request =
           ListPeeringRoutesNetworksRequest.newBuilder()
               .setDirection("direction-962590849")
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setNetwork("network1843485230")
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setPeeringName("peeringName-1170120213")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       ApiFuture<ExchangedPeeringRoute> future =
           networksClient.listPeeringRoutesPagedCallable().futureCall(request);
       // Do something.
       for (ExchangedPeeringRoute element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPeeringRoutesNetworksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListPeeringRoutesNetworksRequest),[ListPeeringRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworksClient.ListPeeringRoutesPagedResponse)>` |   
  
### patchAsync(PatchNetworkRequest request)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(PatchNetworkRequest request)

Patches the specified network with the data included in the request. Only routingConfig can be modified.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworksClient networksClient = NetworksClient.create()) {
       PatchNetworkRequest request =
           PatchNetworkRequest.newBuilder()
               .setNetwork("network1843485230")
               .setNetworkResource(Network.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response = networksClient.patchAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchNetworkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchAsync(String project, String network, Network networkResource)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(String project, String network, Network networkResource)

Patches the specified network with the data included in the request. Only routingConfig can be modified.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworksClient networksClient = NetworksClient.create()) {
       String project = "project-309310695";
       String network = "network1843485230";
       Network networkResource = Network.newBuilder().build();
       Operation response = networksClient.patchAsync(project, network, networkResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`network` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the network to update.  
`networkResource` | `[Network](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Network)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchCallable()
    
    
    public final UnaryCallable<PatchNetworkRequest,Operation> patchCallable()

Patches the specified network with the data included in the request. Only routingConfig can be modified.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworksClient networksClient = NetworksClient.create()) {
       PatchNetworkRequest request =
           PatchNetworkRequest.newBuilder()
               .setNetwork("network1843485230")
               .setNetworkResource(Network.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = networksClient.patchCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PatchNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchNetworkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchOperationCallable()
    
    
    public final OperationCallable<PatchNetworkRequest,Operation,Operation> patchOperationCallable()

Patches the specified network with the data included in the request. Only routingConfig can be modified.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworksClient networksClient = NetworksClient.create()) {
       PatchNetworkRequest request =
           PatchNetworkRequest.newBuilder()
               .setNetwork("network1843485230")
               .setNetworkResource(Network.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           networksClient.patchOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PatchNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchNetworkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removePeeringAsync(RemovePeeringNetworkRequest request)
    
    
    public final OperationFuture<Operation,Operation> removePeeringAsync(RemovePeeringNetworkRequest request)

Removes a peering from the specified network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworksClient networksClient = NetworksClient.create()) {
       RemovePeeringNetworkRequest request =
           RemovePeeringNetworkRequest.newBuilder()
               .setNetwork("network1843485230")
               .setNetworksRemovePeeringRequestResource(
                   NetworksRemovePeeringRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response = networksClient.removePeeringAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RemovePeeringNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RemovePeeringNetworkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removePeeringAsync(String project, String network, NetworksRemovePeeringRequest networksRemovePeeringRequestResource)
    
    
    public final OperationFuture<Operation,Operation> removePeeringAsync(String project, String network, NetworksRemovePeeringRequest networksRemovePeeringRequestResource)

Removes a peering from the specified network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworksClient networksClient = NetworksClient.create()) {
       String project = "project-309310695";
       String network = "network1843485230";
       NetworksRemovePeeringRequest networksRemovePeeringRequestResource =
           NetworksRemovePeeringRequest.newBuilder().build();
       Operation response =
           networksClient
               .removePeeringAsync(project, network, networksRemovePeeringRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`network` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the network resource to remove peering from.  
`networksRemovePeeringRequestResource` | `[NetworksRemovePeeringRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworksRemovePeeringRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removePeeringCallable()
    
    
    public final UnaryCallable<RemovePeeringNetworkRequest,Operation> removePeeringCallable()

Removes a peering from the specified network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworksClient networksClient = NetworksClient.create()) {
       RemovePeeringNetworkRequest request =
           RemovePeeringNetworkRequest.newBuilder()
               .setNetwork("network1843485230")
               .setNetworksRemovePeeringRequestResource(
                   NetworksRemovePeeringRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = networksClient.removePeeringCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RemovePeeringNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RemovePeeringNetworkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removePeeringOperationCallable()
    
    
    public final OperationCallable<RemovePeeringNetworkRequest,Operation,Operation> removePeeringOperationCallable()

Removes a peering from the specified network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworksClient networksClient = NetworksClient.create()) {
       RemovePeeringNetworkRequest request =
           RemovePeeringNetworkRequest.newBuilder()
               .setNetwork("network1843485230")
               .setNetworksRemovePeeringRequestResource(
                   NetworksRemovePeeringRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           networksClient.removePeeringOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RemovePeeringNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RemovePeeringNetworkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### requestRemovePeeringAsync(RequestRemovePeeringNetworkRequest request)
    
    
    public final OperationFuture<Operation,Operation> requestRemovePeeringAsync(RequestRemovePeeringNetworkRequest request)

Requests to remove a peering from the specified network. Applicable only for PeeringConnection with update_strategy=CONSENSUS.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworksClient networksClient = NetworksClient.create()) {
       RequestRemovePeeringNetworkRequest request =
           RequestRemovePeeringNetworkRequest.newBuilder()
               .setNetwork("network1843485230")
               .setNetworksRequestRemovePeeringRequestResource(
                   NetworksRequestRemovePeeringRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response = networksClient.requestRemovePeeringAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RequestRemovePeeringNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RequestRemovePeeringNetworkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### requestRemovePeeringAsync(String project, String network, NetworksRequestRemovePeeringRequest networksRequestRemovePeeringRequestResource)
    
    
    public final OperationFuture<Operation,Operation> requestRemovePeeringAsync(String project, String network, NetworksRequestRemovePeeringRequest networksRequestRemovePeeringRequestResource)

Requests to remove a peering from the specified network. Applicable only for PeeringConnection with update_strategy=CONSENSUS.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworksClient networksClient = NetworksClient.create()) {
       String project = "project-309310695";
       String network = "network1843485230";
       NetworksRequestRemovePeeringRequest networksRequestRemovePeeringRequestResource =
           NetworksRequestRemovePeeringRequest.newBuilder().build();
       Operation response =
           networksClient
               .requestRemovePeeringAsync(
                   project, network, networksRequestRemovePeeringRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`network` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the network resource to remove peering from.  
`networksRequestRemovePeeringRequestResource` | `[NetworksRequestRemovePeeringRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworksRequestRemovePeeringRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### requestRemovePeeringCallable()
    
    
    public final UnaryCallable<RequestRemovePeeringNetworkRequest,Operation> requestRemovePeeringCallable()

Requests to remove a peering from the specified network. Applicable only for PeeringConnection with update_strategy=CONSENSUS.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworksClient networksClient = NetworksClient.create()) {
       RequestRemovePeeringNetworkRequest request =
           RequestRemovePeeringNetworkRequest.newBuilder()
               .setNetwork("network1843485230")
               .setNetworksRequestRemovePeeringRequestResource(
                   NetworksRequestRemovePeeringRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           networksClient.requestRemovePeeringCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RequestRemovePeeringNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RequestRemovePeeringNetworkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### requestRemovePeeringOperationCallable()
    
    
    public final OperationCallable<RequestRemovePeeringNetworkRequest,Operation,Operation> requestRemovePeeringOperationCallable()

Requests to remove a peering from the specified network. Applicable only for PeeringConnection with update_strategy=CONSENSUS.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworksClient networksClient = NetworksClient.create()) {
       RequestRemovePeeringNetworkRequest request =
           RequestRemovePeeringNetworkRequest.newBuilder()
               .setNetwork("network1843485230")
               .setNetworksRequestRemovePeeringRequestResource(
                   NetworksRequestRemovePeeringRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           networksClient.requestRemovePeeringOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RequestRemovePeeringNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RequestRemovePeeringNetworkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### switchToCustomModeAsync(SwitchToCustomModeNetworkRequest request)
    
    
    public final OperationFuture<Operation,Operation> switchToCustomModeAsync(SwitchToCustomModeNetworkRequest request)

Switches the network mode from auto subnet mode to custom subnet mode.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworksClient networksClient = NetworksClient.create()) {
       SwitchToCustomModeNetworkRequest request =
           SwitchToCustomModeNetworkRequest.newBuilder()
               .setNetwork("network1843485230")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response = networksClient.switchToCustomModeAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SwitchToCustomModeNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SwitchToCustomModeNetworkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### switchToCustomModeAsync(String project, String network)
    
    
    public final OperationFuture<Operation,Operation> switchToCustomModeAsync(String project, String network)

Switches the network mode from auto subnet mode to custom subnet mode.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworksClient networksClient = NetworksClient.create()) {
       String project = "project-309310695";
       String network = "network1843485230";
       Operation response = networksClient.switchToCustomModeAsync(project, network).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`network` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the network to be updated.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### switchToCustomModeCallable()
    
    
    public final UnaryCallable<SwitchToCustomModeNetworkRequest,Operation> switchToCustomModeCallable()

Switches the network mode from auto subnet mode to custom subnet mode.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworksClient networksClient = NetworksClient.create()) {
       SwitchToCustomModeNetworkRequest request =
           SwitchToCustomModeNetworkRequest.newBuilder()
               .setNetwork("network1843485230")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = networksClient.switchToCustomModeCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SwitchToCustomModeNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SwitchToCustomModeNetworkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### switchToCustomModeOperationCallable()
    
    
    public final OperationCallable<SwitchToCustomModeNetworkRequest,Operation,Operation> switchToCustomModeOperationCallable()

Switches the network mode from auto subnet mode to custom subnet mode.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworksClient networksClient = NetworksClient.create()) {
       SwitchToCustomModeNetworkRequest request =
           SwitchToCustomModeNetworkRequest.newBuilder()
               .setNetwork("network1843485230")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           networksClient.switchToCustomModeOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SwitchToCustomModeNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SwitchToCustomModeNetworkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updatePeeringAsync(UpdatePeeringNetworkRequest request)
    
    
    public final OperationFuture<Operation,Operation> updatePeeringAsync(UpdatePeeringNetworkRequest request)

Updates the specified network peering with the data included in the request. You can only modify the NetworkPeering.export_custom_routes field and the NetworkPeering.import_custom_routes field.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworksClient networksClient = NetworksClient.create()) {
       UpdatePeeringNetworkRequest request =
           UpdatePeeringNetworkRequest.newBuilder()
               .setNetwork("network1843485230")
               .setNetworksUpdatePeeringRequestResource(
                   NetworksUpdatePeeringRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response = networksClient.updatePeeringAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdatePeeringNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdatePeeringNetworkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updatePeeringAsync(String project, String network, NetworksUpdatePeeringRequest networksUpdatePeeringRequestResource)
    
    
    public final OperationFuture<Operation,Operation> updatePeeringAsync(String project, String network, NetworksUpdatePeeringRequest networksUpdatePeeringRequestResource)

Updates the specified network peering with the data included in the request. You can only modify the NetworkPeering.export_custom_routes field and the NetworkPeering.import_custom_routes field.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworksClient networksClient = NetworksClient.create()) {
       String project = "project-309310695";
       String network = "network1843485230";
       NetworksUpdatePeeringRequest networksUpdatePeeringRequestResource =
           NetworksUpdatePeeringRequest.newBuilder().build();
       Operation response =
           networksClient
               .updatePeeringAsync(project, network, networksUpdatePeeringRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`network` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the network resource which the updated peering is belonging to.  
`networksUpdatePeeringRequestResource` | `[NetworksUpdatePeeringRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworksUpdatePeeringRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updatePeeringCallable()
    
    
    public final UnaryCallable<UpdatePeeringNetworkRequest,Operation> updatePeeringCallable()

Updates the specified network peering with the data included in the request. You can only modify the NetworkPeering.export_custom_routes field and the NetworkPeering.import_custom_routes field.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworksClient networksClient = NetworksClient.create()) {
       UpdatePeeringNetworkRequest request =
           UpdatePeeringNetworkRequest.newBuilder()
               .setNetwork("network1843485230")
               .setNetworksUpdatePeeringRequestResource(
                   NetworksUpdatePeeringRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = networksClient.updatePeeringCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdatePeeringNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdatePeeringNetworkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updatePeeringOperationCallable()
    
    
    public final OperationCallable<UpdatePeeringNetworkRequest,Operation,Operation> updatePeeringOperationCallable()

Updates the specified network peering with the data included in the request. You can only modify the NetworkPeering.export_custom_routes field and the NetworkPeering.import_custom_routes field.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworksClient networksClient = NetworksClient.create()) {
       UpdatePeeringNetworkRequest request =
           UpdatePeeringNetworkRequest.newBuilder()
               .setNetwork("network1843485230")
               .setNetworksUpdatePeeringRequestResource(
                   NetworksUpdatePeeringRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           networksClient.updatePeeringOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdatePeeringNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdatePeeringNetworkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
