---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-clientgateways/latest/com.google.cloud.beyondcorp.clientgateways.v1.ClientGatewaysServiceClient
title: Class ClientGatewaysServiceClient (0.97.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:43:58.576032+00:00
---

# Class ClientGatewaysServiceClient (0.97.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-clientgateways/latest/com.google.cloud.beyondcorp.clientgateways.v1.ClientGatewaysServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ClientGatewaysServiceClient (0.97.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.97.0 (latest)  0.93.0  0.92.0  0.91.0  0.89.0  0.86.0  0.85.0  0.83.0  0.81.0  0.80.0  0.79.0  0.78.0  0.76.0  0.74.0  0.73.0  0.72.0  0.71.0  0.70.0  0.68.0  0.66.0  0.65.0  0.62.0  0.61.0  0.60.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-beyondcorp-clientgateways/google-cloud-beyondcorp-clientgateways/src/main/java/com/google/cloud/beyondcorp/clientgateways/v1/ClientGatewaysServiceClient.java)| [Product Reference](https://cloud.google.com/beyondcorp-enterprise/)  
---|---  
  
Service Description: API Overview:

The `beyondcorp.googleapis.com` service implements the Google Cloud BeyondCorp API.

Data Model:

The ClientGatewaysService exposes the following resources:

  * Client Gateways, named as follows: `projects/{project_id}/locations/{location_id}/clientGateways/{client_gateway_id}`. 



This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClientGatewaysServiceClient clientGatewaysServiceClient =
         ClientGatewaysServiceClient.create()) {
       ClientGatewayName name = ClientGatewayName.of("[PROJECT]", "[LOCATION]", "[CLIENT_GATEWAY]");
       ClientGateway response = clientGatewaysServiceClient.getClientGateway(name);
     }
     

Note: close() needs to be called on the ClientGatewaysServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListClientGateways |  Lists ClientGateways in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listClientGateways(ListClientGatewaysRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listClientGateways(LocationName parent) 
  * listClientGateways(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listClientGatewaysPagedCallable() 
  * listClientGatewaysCallable() 

  
GetClientGateway |  Gets details of a single ClientGateway. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getClientGateway(GetClientGatewayRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getClientGateway(ClientGatewayName name) 
  * getClientGateway(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getClientGatewayCallable() 

  
CreateClientGateway |  Creates a new ClientGateway in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createClientGatewayAsync(CreateClientGatewayRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createClientGatewayAsync(LocationName parent, ClientGateway clientGateway, String clientGatewayId) 
  * createClientGatewayAsync(String parent, ClientGateway clientGateway, String clientGatewayId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createClientGatewayOperationCallable() 
  * createClientGatewayCallable() 

  
DeleteClientGateway |  Deletes a single ClientGateway. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteClientGatewayAsync(DeleteClientGatewayRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteClientGatewayAsync(ClientGatewayName name) 
  * deleteClientGatewayAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteClientGatewayOperationCallable() 
  * deleteClientGatewayCallable() 

  
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

This class can be customized by passing in a custom instance of ClientGatewaysServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ClientGatewaysServiceSettings clientGatewaysServiceSettings =
         ClientGatewaysServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     ClientGatewaysServiceClient clientGatewaysServiceClient =
         ClientGatewaysServiceClient.create(clientGatewaysServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ClientGatewaysServiceSettings clientGatewaysServiceSettings =
         ClientGatewaysServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     ClientGatewaysServiceClient clientGatewaysServiceClient =
         ClientGatewaysServiceClient.create(clientGatewaysServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ClientGatewaysServiceClient

## Static Methods 

### create()
    
    
    public static final ClientGatewaysServiceClient create()

Constructs an instance of ClientGatewaysServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[ClientGatewaysServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-clientgateways/latest/com.google.cloud.beyondcorp.clientgateways.v1.ClientGatewaysServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ClientGatewaysServiceSettings settings)
    
    
    public static final ClientGatewaysServiceClient create(ClientGatewaysServiceSettings settings)

Constructs an instance of ClientGatewaysServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ClientGatewaysServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-clientgateways/latest/com.google.cloud.beyondcorp.clientgateways.v1.ClientGatewaysServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClientGatewaysServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-clientgateways/latest/com.google.cloud.beyondcorp.clientgateways.v1.ClientGatewaysServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ClientGatewaysServiceStub stub)
    
    
    public static final ClientGatewaysServiceClient create(ClientGatewaysServiceStub stub)

Constructs an instance of ClientGatewaysServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(ClientGatewaysServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ClientGatewaysServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-clientgateways/latest/com.google.cloud.beyondcorp.clientgateways.v1.stub.ClientGatewaysServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClientGatewaysServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-clientgateways/latest/com.google.cloud.beyondcorp.clientgateways.v1.ClientGatewaysServiceClient)` |   
  
## Constructors 

### ClientGatewaysServiceClient(ClientGatewaysServiceSettings settings)
    
    
    protected ClientGatewaysServiceClient(ClientGatewaysServiceSettings settings)

Constructs an instance of ClientGatewaysServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ClientGatewaysServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-clientgateways/latest/com.google.cloud.beyondcorp.clientgateways.v1.ClientGatewaysServiceSettings)`  
  
  
### ClientGatewaysServiceClient(ClientGatewaysServiceStub stub)
    
    
    protected ClientGatewaysServiceClient(ClientGatewaysServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ClientGatewaysServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-clientgateways/latest/com.google.cloud.beyondcorp.clientgateways.v1.stub.ClientGatewaysServiceStub)`  
  
  
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

### createClientGatewayAsync(@Nullable LocationName parent, ClientGateway clientGateway, String clientGatewayId)
    
    
    public final OperationFuture<ClientGateway,ClientGatewayOperationMetadata> createClientGatewayAsync(@Nullable LocationName parent, ClientGateway clientGateway, String clientGatewayId)

Creates a new ClientGateway in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClientGatewaysServiceClient clientGatewaysServiceClient =
         ClientGatewaysServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       ClientGateway clientGateway = ClientGateway.newBuilder().build();
       String clientGatewayId = "clientGatewayId-1199632652";
       ClientGateway response =
           clientGatewaysServiceClient
               .createClientGatewayAsync(parent, clientGateway, clientGatewayId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.beyondcorp.clientgateways.v1.LocationName`  
Required. Value for parent.  
`clientGateway` | `[ClientGateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-clientgateways/latest/com.google.cloud.beyondcorp.clientgateways.v1.ClientGateway)`  
Required. The resource being created.  
`clientGatewayId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. User-settable client gateway resource ID. * Must start with a letter. * Must contain between 4-63 characters from `/a-z-/`. * Must end with a number or a letter.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ClientGateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-clientgateways/latest/com.google.cloud.beyondcorp.clientgateways.v1.ClientGateway),[ClientGatewayOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-clientgateways/latest/com.google.cloud.beyondcorp.clientgateways.v1.ClientGatewayOperationMetadata)>` |   
  
### createClientGatewayAsync(CreateClientGatewayRequest request)
    
    
    public final OperationFuture<ClientGateway,ClientGatewayOperationMetadata> createClientGatewayAsync(CreateClientGatewayRequest request)

Creates a new ClientGateway in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClientGatewaysServiceClient clientGatewaysServiceClient =
         ClientGatewaysServiceClient.create()) {
       CreateClientGatewayRequest request =
           CreateClientGatewayRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setClientGatewayId("clientGatewayId-1199632652")
               .setClientGateway(ClientGateway.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       ClientGateway response = clientGatewaysServiceClient.createClientGatewayAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateClientGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-clientgateways/latest/com.google.cloud.beyondcorp.clientgateways.v1.CreateClientGatewayRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ClientGateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-clientgateways/latest/com.google.cloud.beyondcorp.clientgateways.v1.ClientGateway),[ClientGatewayOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-clientgateways/latest/com.google.cloud.beyondcorp.clientgateways.v1.ClientGatewayOperationMetadata)>` |   
  
### createClientGatewayAsync(String parent, ClientGateway clientGateway, String clientGatewayId)
    
    
    public final OperationFuture<ClientGateway,ClientGatewayOperationMetadata> createClientGatewayAsync(String parent, ClientGateway clientGateway, String clientGatewayId)

Creates a new ClientGateway in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClientGatewaysServiceClient clientGatewaysServiceClient =
         ClientGatewaysServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       ClientGateway clientGateway = ClientGateway.newBuilder().build();
       String clientGatewayId = "clientGatewayId-1199632652";
       ClientGateway response =
           clientGatewaysServiceClient
               .createClientGatewayAsync(parent, clientGateway, clientGatewayId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Value for parent.  
`clientGateway` | `[ClientGateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-clientgateways/latest/com.google.cloud.beyondcorp.clientgateways.v1.ClientGateway)`  
Required. The resource being created.  
`clientGatewayId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. User-settable client gateway resource ID. * Must start with a letter. * Must contain between 4-63 characters from `/a-z-/`. * Must end with a number or a letter.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ClientGateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-clientgateways/latest/com.google.cloud.beyondcorp.clientgateways.v1.ClientGateway),[ClientGatewayOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-clientgateways/latest/com.google.cloud.beyondcorp.clientgateways.v1.ClientGatewayOperationMetadata)>` |   
  
### createClientGatewayCallable()
    
    
    public final UnaryCallable<CreateClientGatewayRequest,Operation> createClientGatewayCallable()

Creates a new ClientGateway in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClientGatewaysServiceClient clientGatewaysServiceClient =
         ClientGatewaysServiceClient.create()) {
       CreateClientGatewayRequest request =
           CreateClientGatewayRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setClientGatewayId("clientGatewayId-1199632652")
               .setClientGateway(ClientGateway.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future =
           clientGatewaysServiceClient.createClientGatewayCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateClientGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-clientgateways/latest/com.google.cloud.beyondcorp.clientgateways.v1.CreateClientGatewayRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createClientGatewayOperationCallable()
    
    
    public final OperationCallable<CreateClientGatewayRequest,ClientGateway,ClientGatewayOperationMetadata> createClientGatewayOperationCallable()

Creates a new ClientGateway in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClientGatewaysServiceClient clientGatewaysServiceClient =
         ClientGatewaysServiceClient.create()) {
       CreateClientGatewayRequest request =
           CreateClientGatewayRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setClientGatewayId("clientGatewayId-1199632652")
               .setClientGateway(ClientGateway.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       OperationFuture<ClientGateway, ClientGatewayOperationMetadata> future =
           clientGatewaysServiceClient.createClientGatewayOperationCallable().futureCall(request);
       // Do something.
       ClientGateway response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateClientGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-clientgateways/latest/com.google.cloud.beyondcorp.clientgateways.v1.CreateClientGatewayRequest),[ClientGateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-clientgateways/latest/com.google.cloud.beyondcorp.clientgateways.v1.ClientGateway),[ClientGatewayOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-clientgateways/latest/com.google.cloud.beyondcorp.clientgateways.v1.ClientGatewayOperationMetadata)>` |   
  
### deleteClientGatewayAsync(@Nullable ClientGatewayName name)
    
    
    public final OperationFuture<Empty,ClientGatewayOperationMetadata> deleteClientGatewayAsync(@Nullable ClientGatewayName name)

Deletes a single ClientGateway.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClientGatewaysServiceClient clientGatewaysServiceClient =
         ClientGatewaysServiceClient.create()) {
       ClientGatewayName name = ClientGatewayName.of("[PROJECT]", "[LOCATION]", "[CLIENT_GATEWAY]");
       clientGatewaysServiceClient.deleteClientGatewayAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.beyondcorp.clientgateways.v1.ClientGatewayName`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[ClientGatewayOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-clientgateways/latest/com.google.cloud.beyondcorp.clientgateways.v1.ClientGatewayOperationMetadata)>` |   
  
### deleteClientGatewayAsync(DeleteClientGatewayRequest request)
    
    
    public final OperationFuture<Empty,ClientGatewayOperationMetadata> deleteClientGatewayAsync(DeleteClientGatewayRequest request)

Deletes a single ClientGateway.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClientGatewaysServiceClient clientGatewaysServiceClient =
         ClientGatewaysServiceClient.create()) {
       DeleteClientGatewayRequest request =
           DeleteClientGatewayRequest.newBuilder()
               .setName(
                   ClientGatewayName.of("[PROJECT]", "[LOCATION]", "[CLIENT_GATEWAY]").toString())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       clientGatewaysServiceClient.deleteClientGatewayAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteClientGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-clientgateways/latest/com.google.cloud.beyondcorp.clientgateways.v1.DeleteClientGatewayRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[ClientGatewayOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-clientgateways/latest/com.google.cloud.beyondcorp.clientgateways.v1.ClientGatewayOperationMetadata)>` |   
  
### deleteClientGatewayAsync(String name)
    
    
    public final OperationFuture<Empty,ClientGatewayOperationMetadata> deleteClientGatewayAsync(String name)

Deletes a single ClientGateway.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClientGatewaysServiceClient clientGatewaysServiceClient =
         ClientGatewaysServiceClient.create()) {
       String name = ClientGatewayName.of("[PROJECT]", "[LOCATION]", "[CLIENT_GATEWAY]").toString();
       clientGatewaysServiceClient.deleteClientGatewayAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[ClientGatewayOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-clientgateways/latest/com.google.cloud.beyondcorp.clientgateways.v1.ClientGatewayOperationMetadata)>` |   
  
### deleteClientGatewayCallable()
    
    
    public final UnaryCallable<DeleteClientGatewayRequest,Operation> deleteClientGatewayCallable()

Deletes a single ClientGateway.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClientGatewaysServiceClient clientGatewaysServiceClient =
         ClientGatewaysServiceClient.create()) {
       DeleteClientGatewayRequest request =
           DeleteClientGatewayRequest.newBuilder()
               .setName(
                   ClientGatewayName.of("[PROJECT]", "[LOCATION]", "[CLIENT_GATEWAY]").toString())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future =
           clientGatewaysServiceClient.deleteClientGatewayCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteClientGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-clientgateways/latest/com.google.cloud.beyondcorp.clientgateways.v1.DeleteClientGatewayRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteClientGatewayOperationCallable()
    
    
    public final OperationCallable<DeleteClientGatewayRequest,Empty,ClientGatewayOperationMetadata> deleteClientGatewayOperationCallable()

Deletes a single ClientGateway.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClientGatewaysServiceClient clientGatewaysServiceClient =
         ClientGatewaysServiceClient.create()) {
       DeleteClientGatewayRequest request =
           DeleteClientGatewayRequest.newBuilder()
               .setName(
                   ClientGatewayName.of("[PROJECT]", "[LOCATION]", "[CLIENT_GATEWAY]").toString())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       OperationFuture<Empty, ClientGatewayOperationMetadata> future =
           clientGatewaysServiceClient.deleteClientGatewayOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteClientGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-clientgateways/latest/com.google.cloud.beyondcorp.clientgateways.v1.DeleteClientGatewayRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[ClientGatewayOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-clientgateways/latest/com.google.cloud.beyondcorp.clientgateways.v1.ClientGatewayOperationMetadata)>` |   
  
### getClientGateway(@Nullable ClientGatewayName name)
    
    
    public final ClientGateway getClientGateway(@Nullable ClientGatewayName name)

Gets details of a single ClientGateway.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClientGatewaysServiceClient clientGatewaysServiceClient =
         ClientGatewaysServiceClient.create()) {
       ClientGatewayName name = ClientGatewayName.of("[PROJECT]", "[LOCATION]", "[CLIENT_GATEWAY]");
       ClientGateway response = clientGatewaysServiceClient.getClientGateway(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.beyondcorp.clientgateways.v1.ClientGatewayName`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[ClientGateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-clientgateways/latest/com.google.cloud.beyondcorp.clientgateways.v1.ClientGateway)` |   
  
### getClientGateway(GetClientGatewayRequest request)
    
    
    public final ClientGateway getClientGateway(GetClientGatewayRequest request)

Gets details of a single ClientGateway.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClientGatewaysServiceClient clientGatewaysServiceClient =
         ClientGatewaysServiceClient.create()) {
       GetClientGatewayRequest request =
           GetClientGatewayRequest.newBuilder()
               .setName(
                   ClientGatewayName.of("[PROJECT]", "[LOCATION]", "[CLIENT_GATEWAY]").toString())
               .build();
       ClientGateway response = clientGatewaysServiceClient.getClientGateway(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetClientGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-clientgateways/latest/com.google.cloud.beyondcorp.clientgateways.v1.GetClientGatewayRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ClientGateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-clientgateways/latest/com.google.cloud.beyondcorp.clientgateways.v1.ClientGateway)` |   
  
### getClientGateway(String name)
    
    
    public final ClientGateway getClientGateway(String name)

Gets details of a single ClientGateway.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClientGatewaysServiceClient clientGatewaysServiceClient =
         ClientGatewaysServiceClient.create()) {
       String name = ClientGatewayName.of("[PROJECT]", "[LOCATION]", "[CLIENT_GATEWAY]").toString();
       ClientGateway response = clientGatewaysServiceClient.getClientGateway(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[ClientGateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-clientgateways/latest/com.google.cloud.beyondcorp.clientgateways.v1.ClientGateway)` |   
  
### getClientGatewayCallable()
    
    
    public final UnaryCallable<GetClientGatewayRequest,ClientGateway> getClientGatewayCallable()

Gets details of a single ClientGateway.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClientGatewaysServiceClient clientGatewaysServiceClient =
         ClientGatewaysServiceClient.create()) {
       GetClientGatewayRequest request =
           GetClientGatewayRequest.newBuilder()
               .setName(
                   ClientGatewayName.of("[PROJECT]", "[LOCATION]", "[CLIENT_GATEWAY]").toString())
               .build();
       ApiFuture<ClientGateway> future =
           clientGatewaysServiceClient.getClientGatewayCallable().futureCall(request);
       // Do something.
       ClientGateway response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetClientGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-clientgateways/latest/com.google.cloud.beyondcorp.clientgateways.v1.GetClientGatewayRequest),[ClientGateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-clientgateways/latest/com.google.cloud.beyondcorp.clientgateways.v1.ClientGateway)>` |   
  
### getIamPolicy(GetIamPolicyRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRequest request)

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClientGatewaysServiceClient clientGatewaysServiceClient =
         ClientGatewaysServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   ClientGatewayName.of("[PROJECT]", "[LOCATION]", "[CLIENT_GATEWAY]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = clientGatewaysServiceClient.getIamPolicy(request);
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
     try (ClientGatewaysServiceClient clientGatewaysServiceClient =
         ClientGatewaysServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   ClientGatewayName.of("[PROJECT]", "[LOCATION]", "[CLIENT_GATEWAY]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future =
           clientGatewaysServiceClient.getIamPolicyCallable().futureCall(request);
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
     try (ClientGatewaysServiceClient clientGatewaysServiceClient =
         ClientGatewaysServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = clientGatewaysServiceClient.getLocation(request);
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
     try (ClientGatewaysServiceClient clientGatewaysServiceClient =
         ClientGatewaysServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future =
           clientGatewaysServiceClient.getLocationCallable().futureCall(request);
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
  
### getSettings()
    
    
    public final @Nullable ClientGatewaysServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.beyondcorp.clientgateways.v1.ClientGatewaysServiceSettings` |   
  
### getStub()
    
    
    public ClientGatewaysServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[ClientGatewaysServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-clientgateways/latest/com.google.cloud.beyondcorp.clientgateways.v1.stub.ClientGatewaysServiceStub)` |   
  
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
  
### listClientGateways(@Nullable LocationName parent)
    
    
    public final ClientGatewaysServiceClient.ListClientGatewaysPagedResponse listClientGateways(@Nullable LocationName parent)

Lists ClientGateways in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClientGatewaysServiceClient clientGatewaysServiceClient =
         ClientGatewaysServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (ClientGateway element :
           clientGatewaysServiceClient.listClientGateways(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.beyondcorp.clientgateways.v1.LocationName`  
Required. Parent value for ListClientGatewaysRequest.  
**Returns**  
---  
**Type** | **Description**  
`[ClientGatewaysServiceClient.ListClientGatewaysPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-clientgateways/latest/com.google.cloud.beyondcorp.clientgateways.v1.ClientGatewaysServiceClient.ListClientGatewaysPagedResponse)` |   
  
### listClientGateways(ListClientGatewaysRequest request)
    
    
    public final ClientGatewaysServiceClient.ListClientGatewaysPagedResponse listClientGateways(ListClientGatewaysRequest request)

Lists ClientGateways in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClientGatewaysServiceClient clientGatewaysServiceClient =
         ClientGatewaysServiceClient.create()) {
       ListClientGatewaysRequest request =
           ListClientGatewaysRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (ClientGateway element :
           clientGatewaysServiceClient.listClientGateways(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListClientGatewaysRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-clientgateways/latest/com.google.cloud.beyondcorp.clientgateways.v1.ListClientGatewaysRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ClientGatewaysServiceClient.ListClientGatewaysPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-clientgateways/latest/com.google.cloud.beyondcorp.clientgateways.v1.ClientGatewaysServiceClient.ListClientGatewaysPagedResponse)` |   
  
### listClientGateways(String parent)
    
    
    public final ClientGatewaysServiceClient.ListClientGatewaysPagedResponse listClientGateways(String parent)

Lists ClientGateways in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClientGatewaysServiceClient clientGatewaysServiceClient =
         ClientGatewaysServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (ClientGateway element :
           clientGatewaysServiceClient.listClientGateways(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Parent value for ListClientGatewaysRequest.  
**Returns**  
---  
**Type** | **Description**  
`[ClientGatewaysServiceClient.ListClientGatewaysPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-clientgateways/latest/com.google.cloud.beyondcorp.clientgateways.v1.ClientGatewaysServiceClient.ListClientGatewaysPagedResponse)` |   
  
### listClientGatewaysCallable()
    
    
    public final UnaryCallable<ListClientGatewaysRequest,ListClientGatewaysResponse> listClientGatewaysCallable()

Lists ClientGateways in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClientGatewaysServiceClient clientGatewaysServiceClient =
         ClientGatewaysServiceClient.create()) {
       ListClientGatewaysRequest request =
           ListClientGatewaysRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListClientGatewaysResponse response =
             clientGatewaysServiceClient.listClientGatewaysCallable().call(request);
         for (ClientGateway element : response.getClientGatewaysList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListClientGatewaysRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-clientgateways/latest/com.google.cloud.beyondcorp.clientgateways.v1.ListClientGatewaysRequest),[ListClientGatewaysResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-clientgateways/latest/com.google.cloud.beyondcorp.clientgateways.v1.ListClientGatewaysResponse)>` |   
  
### listClientGatewaysPagedCallable()
    
    
    public final UnaryCallable<ListClientGatewaysRequest,ClientGatewaysServiceClient.ListClientGatewaysPagedResponse> listClientGatewaysPagedCallable()

Lists ClientGateways in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClientGatewaysServiceClient clientGatewaysServiceClient =
         ClientGatewaysServiceClient.create()) {
       ListClientGatewaysRequest request =
           ListClientGatewaysRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<ClientGateway> future =
           clientGatewaysServiceClient.listClientGatewaysPagedCallable().futureCall(request);
       // Do something.
       for (ClientGateway element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListClientGatewaysRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-clientgateways/latest/com.google.cloud.beyondcorp.clientgateways.v1.ListClientGatewaysRequest),[ListClientGatewaysPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-clientgateways/latest/com.google.cloud.beyondcorp.clientgateways.v1.ClientGatewaysServiceClient.ListClientGatewaysPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final ClientGatewaysServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClientGatewaysServiceClient clientGatewaysServiceClient =
         ClientGatewaysServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : clientGatewaysServiceClient.listLocations(request).iterateAll()) {
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
`[ClientGatewaysServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-clientgateways/latest/com.google.cloud.beyondcorp.clientgateways.v1.ClientGatewaysServiceClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClientGatewaysServiceClient clientGatewaysServiceClient =
         ClientGatewaysServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             clientGatewaysServiceClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,ClientGatewaysServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClientGatewaysServiceClient clientGatewaysServiceClient =
         ClientGatewaysServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           clientGatewaysServiceClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-clientgateways/latest/com.google.cloud.beyondcorp.clientgateways.v1.ClientGatewaysServiceClient.ListLocationsPagedResponse)>` |   
  
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
     try (ClientGatewaysServiceClient clientGatewaysServiceClient =
         ClientGatewaysServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   ClientGatewayName.of("[PROJECT]", "[LOCATION]", "[CLIENT_GATEWAY]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = clientGatewaysServiceClient.setIamPolicy(request);
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
     try (ClientGatewaysServiceClient clientGatewaysServiceClient =
         ClientGatewaysServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   ClientGatewayName.of("[PROJECT]", "[LOCATION]", "[CLIENT_GATEWAY]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Policy> future =
           clientGatewaysServiceClient.setIamPolicyCallable().futureCall(request);
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
     try (ClientGatewaysServiceClient clientGatewaysServiceClient =
         ClientGatewaysServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   ClientGatewayName.of("[PROJECT]", "[LOCATION]", "[CLIENT_GATEWAY]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response = clientGatewaysServiceClient.testIamPermissions(request);
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
     try (ClientGatewaysServiceClient clientGatewaysServiceClient =
         ClientGatewaysServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   ClientGatewayName.of("[PROJECT]", "[LOCATION]", "[CLIENT_GATEWAY]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           clientGatewaysServiceClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
