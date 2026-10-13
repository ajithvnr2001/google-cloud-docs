---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.RegistrationServiceClient
title: Class RegistrationServiceClient (2.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:43:11.863842+00:00
---

# Class RegistrationServiceClient (2.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.RegistrationServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class RegistrationServiceClient (2.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.100.0 (latest)  2.96.0  2.95.0  2.94.0  2.92.0  2.89.0  2.88.0  2.86.0  2.84.0  2.83.0  2.81.0  2.79.0  2.77.0  2.76.0  2.75.0  2.74.0  2.73.0  2.71.0  2.69.0  2.68.0  2.65.0  2.64.0  2.63.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.5  2.2.7 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-servicedirectory/google-cloud-servicedirectory/src/main/java/com/google/cloud/servicedirectory/v1/RegistrationServiceClient.java)| [Product Reference](https://cloud.google.com/service-directory/)| [REST Documentation](https://cloud.google.com/service-directory/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/service-directory/docs/reference/rpc)  
---|---|---|---  
  
Service Description: Service Directory API for registering services. It defines the following resource model:

\- The API has a collection of Namespace resources, named `projects/*/locations/*/namespaces/*`.

\- Each Namespace has a collection of Service resources, named `projects/*/locations/*/namespaces/*/services/*`.

\- Each Service has a collection of Endpoint resources, named `projects/*/locations/*/namespaces/*/services/*/endpoints/*`.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Namespace namespace = Namespace.newBuilder().build();
       String namespaceId = "namespaceId790852566";
       Namespace response =
           registrationServiceClient.createNamespace(parent, namespace, namespaceId);
     }
     

Note: close() needs to be called on the RegistrationServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateNamespace |  Creates a namespace, and returns the new namespace. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createNamespace(CreateNamespaceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createNamespace(LocationName parent, Namespace namespace, String namespaceId) 
  * createNamespace(String parent, Namespace namespace, String namespaceId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createNamespaceCallable() 

  
ListNamespaces |  Lists all namespaces. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listNamespaces(ListNamespacesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listNamespaces(LocationName parent) 
  * listNamespaces(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listNamespacesPagedCallable() 
  * listNamespacesCallable() 

  
GetNamespace |  Gets a namespace. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getNamespace(GetNamespaceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getNamespace(NamespaceName name) 
  * getNamespace(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getNamespaceCallable() 

  
UpdateNamespace |  Updates a namespace. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateNamespace(UpdateNamespaceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateNamespace(Namespace namespace, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateNamespaceCallable() 

  
DeleteNamespace |  Deletes a namespace. This also deletes all services and endpoints in the namespace. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteNamespace(DeleteNamespaceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteNamespace(NamespaceName name) 
  * deleteNamespace(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteNamespaceCallable() 

  
CreateService |  Creates a service, and returns the new service. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createService(CreateServiceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createService(NamespaceName parent, Service service, String serviceId) 
  * createService(String parent, Service service, String serviceId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createServiceCallable() 

  
ListServices |  Lists all services belonging to a namespace. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listServices(ListServicesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listServices(NamespaceName parent) 
  * listServices(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listServicesPagedCallable() 
  * listServicesCallable() 

  
GetService |  Gets a service. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getService(GetServiceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getService(ServiceName name) 
  * getService(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getServiceCallable() 

  
UpdateService |  Updates a service. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateService(UpdateServiceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateService(Service service, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateServiceCallable() 

  
DeleteService |  Deletes a service. This also deletes all endpoints associated with the service. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteService(DeleteServiceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteService(ServiceName name) 
  * deleteService(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteServiceCallable() 

  
CreateEndpoint |  Creates an endpoint, and returns the new endpoint. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createEndpoint(CreateEndpointRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createEndpoint(ServiceName parent, Endpoint endpoint, String endpointId) 
  * createEndpoint(String parent, Endpoint endpoint, String endpointId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createEndpointCallable() 

  
ListEndpoints |  Lists all endpoints. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listEndpoints(ListEndpointsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listEndpoints(ServiceName parent) 
  * listEndpoints(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listEndpointsPagedCallable() 
  * listEndpointsCallable() 

  
GetEndpoint |  Gets an endpoint. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getEndpoint(GetEndpointRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getEndpoint(EndpointName name) 
  * getEndpoint(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getEndpointCallable() 

  
UpdateEndpoint |  Updates an endpoint. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateEndpoint(UpdateEndpointRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateEndpoint(Endpoint endpoint, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateEndpointCallable() 

  
DeleteEndpoint |  Deletes an endpoint. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteEndpoint(DeleteEndpointRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteEndpoint(EndpointName name) 
  * deleteEndpoint(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteEndpointCallable() 

  
GetIamPolicy |  Gets the IAM Policy for a resource (namespace or service only). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getIamPolicy(GetIamPolicyRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getIamPolicyCallable() 

  
SetIamPolicy |  Sets the IAM Policy for a resource (namespace or service only). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setIamPolicy(SetIamPolicyRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setIamPolicyCallable() 

  
TestIamPermissions |  Tests IAM permissions for a resource (namespace or service only). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
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

This class can be customized by passing in a custom instance of RegistrationServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RegistrationServiceSettings registrationServiceSettings =
         RegistrationServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     RegistrationServiceClient registrationServiceClient =
         RegistrationServiceClient.create(registrationServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RegistrationServiceSettings registrationServiceSettings =
         RegistrationServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     RegistrationServiceClient registrationServiceClient =
         RegistrationServiceClient.create(registrationServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RegistrationServiceSettings registrationServiceSettings =
         RegistrationServiceSettings.newHttpJsonBuilder().build();
     RegistrationServiceClient registrationServiceClient =
         RegistrationServiceClient.create(registrationServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > RegistrationServiceClient

## Static Methods 

### create()
    
    
    public static final RegistrationServiceClient create()

Constructs an instance of RegistrationServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[RegistrationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.RegistrationServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RegistrationServiceSettings settings)
    
    
    public static final RegistrationServiceClient create(RegistrationServiceSettings settings)

Constructs an instance of RegistrationServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RegistrationServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.RegistrationServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RegistrationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.RegistrationServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RegistrationServiceStub stub)
    
    
    public static final RegistrationServiceClient create(RegistrationServiceStub stub)

Constructs an instance of RegistrationServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(RegistrationServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RegistrationServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.stub.RegistrationServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RegistrationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.RegistrationServiceClient)` |   
  
## Constructors 

### RegistrationServiceClient(RegistrationServiceSettings settings)
    
    
    protected RegistrationServiceClient(RegistrationServiceSettings settings)

Constructs an instance of RegistrationServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RegistrationServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.RegistrationServiceSettings)`  
  
  
### RegistrationServiceClient(RegistrationServiceStub stub)
    
    
    protected RegistrationServiceClient(RegistrationServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RegistrationServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.stub.RegistrationServiceStub)`  
  
  
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

### createEndpoint(@Nullable ServiceName parent, Endpoint endpoint, String endpointId)
    
    
    public final Endpoint createEndpoint(@Nullable ServiceName parent, Endpoint endpoint, String endpointId)

Creates an endpoint, and returns the new endpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       ServiceName parent = ServiceName.of("[PROJECT]", "[LOCATION]", "[NAMESPACE]", "[SERVICE]");
       Endpoint endpoint = Endpoint.newBuilder().build();
       String endpointId = "endpointId-1837754992";
       Endpoint response = registrationServiceClient.createEndpoint(parent, endpoint, endpointId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.servicedirectory.v1.ServiceName`  
Required. The resource name of the service that this endpoint provides.  
`endpoint` | `[Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Endpoint)`  
Required. A endpoint with initial fields set.  
`endpointId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The Resource ID must be 1-63 characters long, and comply with <a href="<https://www.ietf.org/rfc/rfc1035.txt>" target="_blank">RFC1035</a>. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.RegistrationServiceClient?:\[-a-z0-9\]{0,61}\[a-z0-9\])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Endpoint)` |   
  
### createEndpoint(CreateEndpointRequest request)
    
    
    public final Endpoint createEndpoint(CreateEndpointRequest request)

Creates an endpoint, and returns the new endpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       CreateEndpointRequest request =
           CreateEndpointRequest.newBuilder()
               .setParent(
                   ServiceName.of("[PROJECT]", "[LOCATION]", "[NAMESPACE]", "[SERVICE]").toString())
               .setEndpointId("endpointId-1837754992")
               .setEndpoint(Endpoint.newBuilder().build())
               .build();
       Endpoint response = registrationServiceClient.createEndpoint(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateEndpointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.CreateEndpointRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Endpoint)` |   
  
### createEndpoint(String parent, Endpoint endpoint, String endpointId)
    
    
    public final Endpoint createEndpoint(String parent, Endpoint endpoint, String endpointId)

Creates an endpoint, and returns the new endpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       String parent =
           ServiceName.of("[PROJECT]", "[LOCATION]", "[NAMESPACE]", "[SERVICE]").toString();
       Endpoint endpoint = Endpoint.newBuilder().build();
       String endpointId = "endpointId-1837754992";
       Endpoint response = registrationServiceClient.createEndpoint(parent, endpoint, endpointId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the service that this endpoint provides.  
`endpoint` | `[Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Endpoint)`  
Required. A endpoint with initial fields set.  
`endpointId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The Resource ID must be 1-63 characters long, and comply with <a href="<https://www.ietf.org/rfc/rfc1035.txt>" target="_blank">RFC1035</a>. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.RegistrationServiceClient?:\[-a-z0-9\]{0,61}\[a-z0-9\])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Endpoint)` |   
  
### createEndpointCallable()
    
    
    public final UnaryCallable<CreateEndpointRequest,Endpoint> createEndpointCallable()

Creates an endpoint, and returns the new endpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       CreateEndpointRequest request =
           CreateEndpointRequest.newBuilder()
               .setParent(
                   ServiceName.of("[PROJECT]", "[LOCATION]", "[NAMESPACE]", "[SERVICE]").toString())
               .setEndpointId("endpointId-1837754992")
               .setEndpoint(Endpoint.newBuilder().build())
               .build();
       ApiFuture<Endpoint> future =
           registrationServiceClient.createEndpointCallable().futureCall(request);
       // Do something.
       Endpoint response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateEndpointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.CreateEndpointRequest),[Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Endpoint)>` |   
  
### createNamespace(@Nullable LocationName parent, Namespace namespace, String namespaceId)
    
    
    public final Namespace createNamespace(@Nullable LocationName parent, Namespace namespace, String namespaceId)

Creates a namespace, and returns the new namespace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Namespace namespace = Namespace.newBuilder().build();
       String namespaceId = "namespaceId790852566";
       Namespace response =
           registrationServiceClient.createNamespace(parent, namespace, namespaceId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.servicedirectory.v1.LocationName`  
Required. The resource name of the project and location the namespace will be created in.  
`namespace` | `[Namespace](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Namespace)`  
Required. A namespace with initial fields set.  
`namespaceId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The Resource ID must be 1-63 characters long, and comply with <a href="<https://www.ietf.org/rfc/rfc1035.txt>" target="_blank">RFC1035</a>. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.RegistrationServiceClient?:\[-a-z0-9\]{0,61}\[a-z0-9\])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
**Returns**  
---  
**Type** | **Description**  
`[Namespace](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Namespace)` |   
  
### createNamespace(CreateNamespaceRequest request)
    
    
    public final Namespace createNamespace(CreateNamespaceRequest request)

Creates a namespace, and returns the new namespace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       CreateNamespaceRequest request =
           CreateNamespaceRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setNamespaceId("namespaceId790852566")
               .setNamespace(Namespace.newBuilder().build())
               .build();
       Namespace response = registrationServiceClient.createNamespace(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateNamespaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.CreateNamespaceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Namespace](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Namespace)` |   
  
### createNamespace(String parent, Namespace namespace, String namespaceId)
    
    
    public final Namespace createNamespace(String parent, Namespace namespace, String namespaceId)

Creates a namespace, and returns the new namespace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Namespace namespace = Namespace.newBuilder().build();
       String namespaceId = "namespaceId790852566";
       Namespace response =
           registrationServiceClient.createNamespace(parent, namespace, namespaceId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the project and location the namespace will be created in.  
`namespace` | `[Namespace](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Namespace)`  
Required. A namespace with initial fields set.  
`namespaceId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The Resource ID must be 1-63 characters long, and comply with <a href="<https://www.ietf.org/rfc/rfc1035.txt>" target="_blank">RFC1035</a>. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.RegistrationServiceClient?:\[-a-z0-9\]{0,61}\[a-z0-9\])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
**Returns**  
---  
**Type** | **Description**  
`[Namespace](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Namespace)` |   
  
### createNamespaceCallable()
    
    
    public final UnaryCallable<CreateNamespaceRequest,Namespace> createNamespaceCallable()

Creates a namespace, and returns the new namespace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       CreateNamespaceRequest request =
           CreateNamespaceRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setNamespaceId("namespaceId790852566")
               .setNamespace(Namespace.newBuilder().build())
               .build();
       ApiFuture<Namespace> future =
           registrationServiceClient.createNamespaceCallable().futureCall(request);
       // Do something.
       Namespace response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateNamespaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.CreateNamespaceRequest),[Namespace](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Namespace)>` |   
  
### createService(@Nullable NamespaceName parent, Service service, String serviceId)
    
    
    public final Service createService(@Nullable NamespaceName parent, Service service, String serviceId)

Creates a service, and returns the new service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       NamespaceName parent = NamespaceName.of("[PROJECT]", "[LOCATION]", "[NAMESPACE]");
       Service service = Service.newBuilder().build();
       String serviceId = "serviceId-194185552";
       Service response = registrationServiceClient.createService(parent, service, serviceId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.servicedirectory.v1.NamespaceName`  
Required. The resource name of the namespace this service will belong to.  
`service` | `[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Service)`  
Required. A service with initial fields set.  
`serviceId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The Resource ID must be 1-63 characters long, and comply with <a href="<https://www.ietf.org/rfc/rfc1035.txt>" target="_blank">RFC1035</a>. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.RegistrationServiceClient?:\[-a-z0-9\]{0,61}\[a-z0-9\])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
**Returns**  
---  
**Type** | **Description**  
`[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Service)` |   
  
### createService(CreateServiceRequest request)
    
    
    public final Service createService(CreateServiceRequest request)

Creates a service, and returns the new service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       CreateServiceRequest request =
           CreateServiceRequest.newBuilder()
               .setParent(NamespaceName.of("[PROJECT]", "[LOCATION]", "[NAMESPACE]").toString())
               .setServiceId("serviceId-194185552")
               .setService(Service.newBuilder().build())
               .build();
       Service response = registrationServiceClient.createService(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.CreateServiceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Service)` |   
  
### createService(String parent, Service service, String serviceId)
    
    
    public final Service createService(String parent, Service service, String serviceId)

Creates a service, and returns the new service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       String parent = NamespaceName.of("[PROJECT]", "[LOCATION]", "[NAMESPACE]").toString();
       Service service = Service.newBuilder().build();
       String serviceId = "serviceId-194185552";
       Service response = registrationServiceClient.createService(parent, service, serviceId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the namespace this service will belong to.  
`service` | `[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Service)`  
Required. A service with initial fields set.  
`serviceId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The Resource ID must be 1-63 characters long, and comply with <a href="<https://www.ietf.org/rfc/rfc1035.txt>" target="_blank">RFC1035</a>. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.RegistrationServiceClient?:\[-a-z0-9\]{0,61}\[a-z0-9\])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
**Returns**  
---  
**Type** | **Description**  
`[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Service)` |   
  
### createServiceCallable()
    
    
    public final UnaryCallable<CreateServiceRequest,Service> createServiceCallable()

Creates a service, and returns the new service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       CreateServiceRequest request =
           CreateServiceRequest.newBuilder()
               .setParent(NamespaceName.of("[PROJECT]", "[LOCATION]", "[NAMESPACE]").toString())
               .setServiceId("serviceId-194185552")
               .setService(Service.newBuilder().build())
               .build();
       ApiFuture<Service> future =
           registrationServiceClient.createServiceCallable().futureCall(request);
       // Do something.
       Service response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.CreateServiceRequest),[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Service)>` |   
  
### deleteEndpoint(@Nullable EndpointName name)
    
    
    public final void deleteEndpoint(@Nullable EndpointName name)

Deletes an endpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       EndpointName name =
           EndpointName.of("[PROJECT]", "[LOCATION]", "[NAMESPACE]", "[SERVICE]", "[ENDPOINT]");
       registrationServiceClient.deleteEndpoint(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.servicedirectory.v1.EndpointName`  
Required. The name of the endpoint to delete.  
  
### deleteEndpoint(DeleteEndpointRequest request)
    
    
    public final void deleteEndpoint(DeleteEndpointRequest request)

Deletes an endpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       DeleteEndpointRequest request =
           DeleteEndpointRequest.newBuilder()
               .setName(
                   EndpointName.of(
                           "[PROJECT]", "[LOCATION]", "[NAMESPACE]", "[SERVICE]", "[ENDPOINT]")
                       .toString())
               .build();
       registrationServiceClient.deleteEndpoint(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteEndpointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.DeleteEndpointRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteEndpoint(String name)
    
    
    public final void deleteEndpoint(String name)

Deletes an endpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       String name =
           EndpointName.of("[PROJECT]", "[LOCATION]", "[NAMESPACE]", "[SERVICE]", "[ENDPOINT]")
               .toString();
       registrationServiceClient.deleteEndpoint(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the endpoint to delete.  
  
### deleteEndpointCallable()
    
    
    public final UnaryCallable<DeleteEndpointRequest,Empty> deleteEndpointCallable()

Deletes an endpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       DeleteEndpointRequest request =
           DeleteEndpointRequest.newBuilder()
               .setName(
                   EndpointName.of(
                           "[PROJECT]", "[LOCATION]", "[NAMESPACE]", "[SERVICE]", "[ENDPOINT]")
                       .toString())
               .build();
       ApiFuture<Empty> future =
           registrationServiceClient.deleteEndpointCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteEndpointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.DeleteEndpointRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteNamespace(@Nullable NamespaceName name)
    
    
    public final void deleteNamespace(@Nullable NamespaceName name)

Deletes a namespace. This also deletes all services and endpoints in the namespace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       NamespaceName name = NamespaceName.of("[PROJECT]", "[LOCATION]", "[NAMESPACE]");
       registrationServiceClient.deleteNamespace(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.servicedirectory.v1.NamespaceName`  
Required. The name of the namespace to delete.  
  
### deleteNamespace(DeleteNamespaceRequest request)
    
    
    public final void deleteNamespace(DeleteNamespaceRequest request)

Deletes a namespace. This also deletes all services and endpoints in the namespace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       DeleteNamespaceRequest request =
           DeleteNamespaceRequest.newBuilder()
               .setName(NamespaceName.of("[PROJECT]", "[LOCATION]", "[NAMESPACE]").toString())
               .build();
       registrationServiceClient.deleteNamespace(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteNamespaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.DeleteNamespaceRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteNamespace(String name)
    
    
    public final void deleteNamespace(String name)

Deletes a namespace. This also deletes all services and endpoints in the namespace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       String name = NamespaceName.of("[PROJECT]", "[LOCATION]", "[NAMESPACE]").toString();
       registrationServiceClient.deleteNamespace(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the namespace to delete.  
  
### deleteNamespaceCallable()
    
    
    public final UnaryCallable<DeleteNamespaceRequest,Empty> deleteNamespaceCallable()

Deletes a namespace. This also deletes all services and endpoints in the namespace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       DeleteNamespaceRequest request =
           DeleteNamespaceRequest.newBuilder()
               .setName(NamespaceName.of("[PROJECT]", "[LOCATION]", "[NAMESPACE]").toString())
               .build();
       ApiFuture<Empty> future =
           registrationServiceClient.deleteNamespaceCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteNamespaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.DeleteNamespaceRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteService(@Nullable ServiceName name)
    
    
    public final void deleteService(@Nullable ServiceName name)

Deletes a service. This also deletes all endpoints associated with the service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       ServiceName name = ServiceName.of("[PROJECT]", "[LOCATION]", "[NAMESPACE]", "[SERVICE]");
       registrationServiceClient.deleteService(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.servicedirectory.v1.ServiceName`  
Required. The name of the service to delete.  
  
### deleteService(DeleteServiceRequest request)
    
    
    public final void deleteService(DeleteServiceRequest request)

Deletes a service. This also deletes all endpoints associated with the service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       DeleteServiceRequest request =
           DeleteServiceRequest.newBuilder()
               .setName(
                   ServiceName.of("[PROJECT]", "[LOCATION]", "[NAMESPACE]", "[SERVICE]").toString())
               .build();
       registrationServiceClient.deleteService(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.DeleteServiceRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteService(String name)
    
    
    public final void deleteService(String name)

Deletes a service. This also deletes all endpoints associated with the service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       String name =
           ServiceName.of("[PROJECT]", "[LOCATION]", "[NAMESPACE]", "[SERVICE]").toString();
       registrationServiceClient.deleteService(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the service to delete.  
  
### deleteServiceCallable()
    
    
    public final UnaryCallable<DeleteServiceRequest,Empty> deleteServiceCallable()

Deletes a service. This also deletes all endpoints associated with the service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       DeleteServiceRequest request =
           DeleteServiceRequest.newBuilder()
               .setName(
                   ServiceName.of("[PROJECT]", "[LOCATION]", "[NAMESPACE]", "[SERVICE]").toString())
               .build();
       ApiFuture<Empty> future =
           registrationServiceClient.deleteServiceCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.DeleteServiceRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getEndpoint(@Nullable EndpointName name)
    
    
    public final Endpoint getEndpoint(@Nullable EndpointName name)

Gets an endpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       EndpointName name =
           EndpointName.of("[PROJECT]", "[LOCATION]", "[NAMESPACE]", "[SERVICE]", "[ENDPOINT]");
       Endpoint response = registrationServiceClient.getEndpoint(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.servicedirectory.v1.EndpointName`  
Required. The name of the endpoint to get.  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Endpoint)` |   
  
### getEndpoint(GetEndpointRequest request)
    
    
    public final Endpoint getEndpoint(GetEndpointRequest request)

Gets an endpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       GetEndpointRequest request =
           GetEndpointRequest.newBuilder()
               .setName(
                   EndpointName.of(
                           "[PROJECT]", "[LOCATION]", "[NAMESPACE]", "[SERVICE]", "[ENDPOINT]")
                       .toString())
               .build();
       Endpoint response = registrationServiceClient.getEndpoint(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetEndpointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.GetEndpointRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Endpoint)` |   
  
### getEndpoint(String name)
    
    
    public final Endpoint getEndpoint(String name)

Gets an endpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       String name =
           EndpointName.of("[PROJECT]", "[LOCATION]", "[NAMESPACE]", "[SERVICE]", "[ENDPOINT]")
               .toString();
       Endpoint response = registrationServiceClient.getEndpoint(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the endpoint to get.  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Endpoint)` |   
  
### getEndpointCallable()
    
    
    public final UnaryCallable<GetEndpointRequest,Endpoint> getEndpointCallable()

Gets an endpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       GetEndpointRequest request =
           GetEndpointRequest.newBuilder()
               .setName(
                   EndpointName.of(
                           "[PROJECT]", "[LOCATION]", "[NAMESPACE]", "[SERVICE]", "[ENDPOINT]")
                       .toString())
               .build();
       ApiFuture<Endpoint> future =
           registrationServiceClient.getEndpointCallable().futureCall(request);
       // Do something.
       Endpoint response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetEndpointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.GetEndpointRequest),[Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Endpoint)>` |   
  
### getIamPolicy(GetIamPolicyRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRequest request)

Gets the IAM Policy for a resource (namespace or service only).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(NamespaceName.of("[PROJECT]", "[LOCATION]", "[NAMESPACE]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = registrationServiceClient.getIamPolicy(request);
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

Gets the IAM Policy for a resource (namespace or service only).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(NamespaceName.of("[PROJECT]", "[LOCATION]", "[NAMESPACE]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future =
           registrationServiceClient.getIamPolicyCallable().futureCall(request);
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
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = registrationServiceClient.getLocation(request);
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
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future =
           registrationServiceClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getNamespace(@Nullable NamespaceName name)
    
    
    public final Namespace getNamespace(@Nullable NamespaceName name)

Gets a namespace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       NamespaceName name = NamespaceName.of("[PROJECT]", "[LOCATION]", "[NAMESPACE]");
       Namespace response = registrationServiceClient.getNamespace(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.servicedirectory.v1.NamespaceName`  
Required. The name of the namespace to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`[Namespace](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Namespace)` |   
  
### getNamespace(GetNamespaceRequest request)
    
    
    public final Namespace getNamespace(GetNamespaceRequest request)

Gets a namespace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       GetNamespaceRequest request =
           GetNamespaceRequest.newBuilder()
               .setName(NamespaceName.of("[PROJECT]", "[LOCATION]", "[NAMESPACE]").toString())
               .build();
       Namespace response = registrationServiceClient.getNamespace(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetNamespaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.GetNamespaceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Namespace](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Namespace)` |   
  
### getNamespace(String name)
    
    
    public final Namespace getNamespace(String name)

Gets a namespace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       String name = NamespaceName.of("[PROJECT]", "[LOCATION]", "[NAMESPACE]").toString();
       Namespace response = registrationServiceClient.getNamespace(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the namespace to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`[Namespace](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Namespace)` |   
  
### getNamespaceCallable()
    
    
    public final UnaryCallable<GetNamespaceRequest,Namespace> getNamespaceCallable()

Gets a namespace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       GetNamespaceRequest request =
           GetNamespaceRequest.newBuilder()
               .setName(NamespaceName.of("[PROJECT]", "[LOCATION]", "[NAMESPACE]").toString())
               .build();
       ApiFuture<Namespace> future =
           registrationServiceClient.getNamespaceCallable().futureCall(request);
       // Do something.
       Namespace response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetNamespaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.GetNamespaceRequest),[Namespace](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Namespace)>` |   
  
### getService(@Nullable ServiceName name)
    
    
    public final Service getService(@Nullable ServiceName name)

Gets a service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       ServiceName name = ServiceName.of("[PROJECT]", "[LOCATION]", "[NAMESPACE]", "[SERVICE]");
       Service response = registrationServiceClient.getService(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.servicedirectory.v1.ServiceName`  
Required. The name of the service to get.  
**Returns**  
---  
**Type** | **Description**  
`[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Service)` |   
  
### getService(GetServiceRequest request)
    
    
    public final Service getService(GetServiceRequest request)

Gets a service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       GetServiceRequest request =
           GetServiceRequest.newBuilder()
               .setName(
                   ServiceName.of("[PROJECT]", "[LOCATION]", "[NAMESPACE]", "[SERVICE]").toString())
               .build();
       Service response = registrationServiceClient.getService(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.GetServiceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Service)` |   
  
### getService(String name)
    
    
    public final Service getService(String name)

Gets a service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       String name =
           ServiceName.of("[PROJECT]", "[LOCATION]", "[NAMESPACE]", "[SERVICE]").toString();
       Service response = registrationServiceClient.getService(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the service to get.  
**Returns**  
---  
**Type** | **Description**  
`[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Service)` |   
  
### getServiceCallable()
    
    
    public final UnaryCallable<GetServiceRequest,Service> getServiceCallable()

Gets a service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       GetServiceRequest request =
           GetServiceRequest.newBuilder()
               .setName(
                   ServiceName.of("[PROJECT]", "[LOCATION]", "[NAMESPACE]", "[SERVICE]").toString())
               .build();
       ApiFuture<Service> future =
           registrationServiceClient.getServiceCallable().futureCall(request);
       // Do something.
       Service response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.GetServiceRequest),[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Service)>` |   
  
### getSettings()
    
    
    public final @Nullable RegistrationServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.servicedirectory.v1.RegistrationServiceSettings` |   
  
### getStub()
    
    
    public RegistrationServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[RegistrationServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.stub.RegistrationServiceStub)` |   
  
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
  
### listEndpoints(@Nullable ServiceName parent)
    
    
    public final RegistrationServiceClient.ListEndpointsPagedResponse listEndpoints(@Nullable ServiceName parent)

Lists all endpoints.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       ServiceName parent = ServiceName.of("[PROJECT]", "[LOCATION]", "[NAMESPACE]", "[SERVICE]");
       for (Endpoint element : registrationServiceClient.listEndpoints(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.servicedirectory.v1.ServiceName`  
Required. The resource name of the service whose endpoints you'd like to list.  
**Returns**  
---  
**Type** | **Description**  
`[RegistrationServiceClient.ListEndpointsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.RegistrationServiceClient.ListEndpointsPagedResponse)` |   
  
### listEndpoints(ListEndpointsRequest request)
    
    
    public final RegistrationServiceClient.ListEndpointsPagedResponse listEndpoints(ListEndpointsRequest request)

Lists all endpoints.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       ListEndpointsRequest request =
           ListEndpointsRequest.newBuilder()
               .setParent(
                   ServiceName.of("[PROJECT]", "[LOCATION]", "[NAMESPACE]", "[SERVICE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Endpoint element : registrationServiceClient.listEndpoints(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListEndpointsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.ListEndpointsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RegistrationServiceClient.ListEndpointsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.RegistrationServiceClient.ListEndpointsPagedResponse)` |   
  
### listEndpoints(String parent)
    
    
    public final RegistrationServiceClient.ListEndpointsPagedResponse listEndpoints(String parent)

Lists all endpoints.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       String parent =
           ServiceName.of("[PROJECT]", "[LOCATION]", "[NAMESPACE]", "[SERVICE]").toString();
       for (Endpoint element : registrationServiceClient.listEndpoints(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the service whose endpoints you'd like to list.  
**Returns**  
---  
**Type** | **Description**  
`[RegistrationServiceClient.ListEndpointsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.RegistrationServiceClient.ListEndpointsPagedResponse)` |   
  
### listEndpointsCallable()
    
    
    public final UnaryCallable<ListEndpointsRequest,ListEndpointsResponse> listEndpointsCallable()

Lists all endpoints.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       ListEndpointsRequest request =
           ListEndpointsRequest.newBuilder()
               .setParent(
                   ServiceName.of("[PROJECT]", "[LOCATION]", "[NAMESPACE]", "[SERVICE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListEndpointsResponse response =
             registrationServiceClient.listEndpointsCallable().call(request);
         for (Endpoint element : response.getEndpointsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListEndpointsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.ListEndpointsRequest),[ListEndpointsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.ListEndpointsResponse)>` |   
  
### listEndpointsPagedCallable()
    
    
    public final UnaryCallable<ListEndpointsRequest,RegistrationServiceClient.ListEndpointsPagedResponse> listEndpointsPagedCallable()

Lists all endpoints.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       ListEndpointsRequest request =
           ListEndpointsRequest.newBuilder()
               .setParent(
                   ServiceName.of("[PROJECT]", "[LOCATION]", "[NAMESPACE]", "[SERVICE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Endpoint> future =
           registrationServiceClient.listEndpointsPagedCallable().futureCall(request);
       // Do something.
       for (Endpoint element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListEndpointsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.ListEndpointsRequest),[ListEndpointsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.RegistrationServiceClient.ListEndpointsPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final RegistrationServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : registrationServiceClient.listLocations(request).iterateAll()) {
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
`[RegistrationServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.RegistrationServiceClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             registrationServiceClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,RegistrationServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           registrationServiceClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.RegistrationServiceClient.ListLocationsPagedResponse)>` |   
  
### listNamespaces(@Nullable LocationName parent)
    
    
    public final RegistrationServiceClient.ListNamespacesPagedResponse listNamespaces(@Nullable LocationName parent)

Lists all namespaces.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Namespace element : registrationServiceClient.listNamespaces(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.servicedirectory.v1.LocationName`  
Required. The resource name of the project and location whose namespaces you'd like to list.  
**Returns**  
---  
**Type** | **Description**  
`[RegistrationServiceClient.ListNamespacesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.RegistrationServiceClient.ListNamespacesPagedResponse)` |   
  
### listNamespaces(ListNamespacesRequest request)
    
    
    public final RegistrationServiceClient.ListNamespacesPagedResponse listNamespaces(ListNamespacesRequest request)

Lists all namespaces.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       ListNamespacesRequest request =
           ListNamespacesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Namespace element : registrationServiceClient.listNamespaces(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListNamespacesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.ListNamespacesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RegistrationServiceClient.ListNamespacesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.RegistrationServiceClient.ListNamespacesPagedResponse)` |   
  
### listNamespaces(String parent)
    
    
    public final RegistrationServiceClient.ListNamespacesPagedResponse listNamespaces(String parent)

Lists all namespaces.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Namespace element : registrationServiceClient.listNamespaces(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the project and location whose namespaces you'd like to list.  
**Returns**  
---  
**Type** | **Description**  
`[RegistrationServiceClient.ListNamespacesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.RegistrationServiceClient.ListNamespacesPagedResponse)` |   
  
### listNamespacesCallable()
    
    
    public final UnaryCallable<ListNamespacesRequest,ListNamespacesResponse> listNamespacesCallable()

Lists all namespaces.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       ListNamespacesRequest request =
           ListNamespacesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListNamespacesResponse response =
             registrationServiceClient.listNamespacesCallable().call(request);
         for (Namespace element : response.getNamespacesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListNamespacesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.ListNamespacesRequest),[ListNamespacesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.ListNamespacesResponse)>` |   
  
### listNamespacesPagedCallable()
    
    
    public final UnaryCallable<ListNamespacesRequest,RegistrationServiceClient.ListNamespacesPagedResponse> listNamespacesPagedCallable()

Lists all namespaces.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       ListNamespacesRequest request =
           ListNamespacesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Namespace> future =
           registrationServiceClient.listNamespacesPagedCallable().futureCall(request);
       // Do something.
       for (Namespace element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListNamespacesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.ListNamespacesRequest),[ListNamespacesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.RegistrationServiceClient.ListNamespacesPagedResponse)>` |   
  
### listServices(@Nullable NamespaceName parent)
    
    
    public final RegistrationServiceClient.ListServicesPagedResponse listServices(@Nullable NamespaceName parent)

Lists all services belonging to a namespace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       NamespaceName parent = NamespaceName.of("[PROJECT]", "[LOCATION]", "[NAMESPACE]");
       for (Service element : registrationServiceClient.listServices(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.servicedirectory.v1.NamespaceName`  
Required. The resource name of the namespace whose services you'd like to list.  
**Returns**  
---  
**Type** | **Description**  
`[RegistrationServiceClient.ListServicesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.RegistrationServiceClient.ListServicesPagedResponse)` |   
  
### listServices(ListServicesRequest request)
    
    
    public final RegistrationServiceClient.ListServicesPagedResponse listServices(ListServicesRequest request)

Lists all services belonging to a namespace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       ListServicesRequest request =
           ListServicesRequest.newBuilder()
               .setParent(NamespaceName.of("[PROJECT]", "[LOCATION]", "[NAMESPACE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Service element : registrationServiceClient.listServices(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListServicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.ListServicesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RegistrationServiceClient.ListServicesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.RegistrationServiceClient.ListServicesPagedResponse)` |   
  
### listServices(String parent)
    
    
    public final RegistrationServiceClient.ListServicesPagedResponse listServices(String parent)

Lists all services belonging to a namespace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       String parent = NamespaceName.of("[PROJECT]", "[LOCATION]", "[NAMESPACE]").toString();
       for (Service element : registrationServiceClient.listServices(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the namespace whose services you'd like to list.  
**Returns**  
---  
**Type** | **Description**  
`[RegistrationServiceClient.ListServicesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.RegistrationServiceClient.ListServicesPagedResponse)` |   
  
### listServicesCallable()
    
    
    public final UnaryCallable<ListServicesRequest,ListServicesResponse> listServicesCallable()

Lists all services belonging to a namespace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       ListServicesRequest request =
           ListServicesRequest.newBuilder()
               .setParent(NamespaceName.of("[PROJECT]", "[LOCATION]", "[NAMESPACE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListServicesResponse response =
             registrationServiceClient.listServicesCallable().call(request);
         for (Service element : response.getServicesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListServicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.ListServicesRequest),[ListServicesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.ListServicesResponse)>` |   
  
### listServicesPagedCallable()
    
    
    public final UnaryCallable<ListServicesRequest,RegistrationServiceClient.ListServicesPagedResponse> listServicesPagedCallable()

Lists all services belonging to a namespace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       ListServicesRequest request =
           ListServicesRequest.newBuilder()
               .setParent(NamespaceName.of("[PROJECT]", "[LOCATION]", "[NAMESPACE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Service> future =
           registrationServiceClient.listServicesPagedCallable().futureCall(request);
       // Do something.
       for (Service element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListServicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.ListServicesRequest),[ListServicesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.RegistrationServiceClient.ListServicesPagedResponse)>` |   
  
### setIamPolicy(SetIamPolicyRequest request)
    
    
    public final Policy setIamPolicy(SetIamPolicyRequest request)

Sets the IAM Policy for a resource (namespace or service only).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(NamespaceName.of("[PROJECT]", "[LOCATION]", "[NAMESPACE]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = registrationServiceClient.setIamPolicy(request);
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

Sets the IAM Policy for a resource (namespace or service only).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(NamespaceName.of("[PROJECT]", "[LOCATION]", "[NAMESPACE]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Policy> future =
           registrationServiceClient.setIamPolicyCallable().futureCall(request);
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

Tests IAM permissions for a resource (namespace or service only).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(NamespaceName.of("[PROJECT]", "[LOCATION]", "[NAMESPACE]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response = registrationServiceClient.testIamPermissions(request);
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

Tests IAM permissions for a resource (namespace or service only).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(NamespaceName.of("[PROJECT]", "[LOCATION]", "[NAMESPACE]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           registrationServiceClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### updateEndpoint(Endpoint endpoint, FieldMask updateMask)
    
    
    public final Endpoint updateEndpoint(Endpoint endpoint, FieldMask updateMask)

Updates an endpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       Endpoint endpoint = Endpoint.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Endpoint response = registrationServiceClient.updateEndpoint(endpoint, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`endpoint` | `[Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Endpoint)`  
Required. The updated endpoint.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. List of fields to be updated in this request.  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Endpoint)` |   
  
### updateEndpoint(UpdateEndpointRequest request)
    
    
    public final Endpoint updateEndpoint(UpdateEndpointRequest request)

Updates an endpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       UpdateEndpointRequest request =
           UpdateEndpointRequest.newBuilder()
               .setEndpoint(Endpoint.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Endpoint response = registrationServiceClient.updateEndpoint(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateEndpointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.UpdateEndpointRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Endpoint)` |   
  
### updateEndpointCallable()
    
    
    public final UnaryCallable<UpdateEndpointRequest,Endpoint> updateEndpointCallable()

Updates an endpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       UpdateEndpointRequest request =
           UpdateEndpointRequest.newBuilder()
               .setEndpoint(Endpoint.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Endpoint> future =
           registrationServiceClient.updateEndpointCallable().futureCall(request);
       // Do something.
       Endpoint response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateEndpointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.UpdateEndpointRequest),[Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Endpoint)>` |   
  
### updateNamespace(Namespace namespace, FieldMask updateMask)
    
    
    public final Namespace updateNamespace(Namespace namespace, FieldMask updateMask)

Updates a namespace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       Namespace namespace = Namespace.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Namespace response = registrationServiceClient.updateNamespace(namespace, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`namespace` | `[Namespace](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Namespace)`  
Required. The updated namespace.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. List of fields to be updated in this request.  
**Returns**  
---  
**Type** | **Description**  
`[Namespace](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Namespace)` |   
  
### updateNamespace(UpdateNamespaceRequest request)
    
    
    public final Namespace updateNamespace(UpdateNamespaceRequest request)

Updates a namespace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       UpdateNamespaceRequest request =
           UpdateNamespaceRequest.newBuilder()
               .setNamespace(Namespace.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Namespace response = registrationServiceClient.updateNamespace(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateNamespaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.UpdateNamespaceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Namespace](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Namespace)` |   
  
### updateNamespaceCallable()
    
    
    public final UnaryCallable<UpdateNamespaceRequest,Namespace> updateNamespaceCallable()

Updates a namespace.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       UpdateNamespaceRequest request =
           UpdateNamespaceRequest.newBuilder()
               .setNamespace(Namespace.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Namespace> future =
           registrationServiceClient.updateNamespaceCallable().futureCall(request);
       // Do something.
       Namespace response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateNamespaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.UpdateNamespaceRequest),[Namespace](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Namespace)>` |   
  
### updateService(Service service, FieldMask updateMask)
    
    
    public final Service updateService(Service service, FieldMask updateMask)

Updates a service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       Service service = Service.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Service response = registrationServiceClient.updateService(service, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`service` | `[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Service)`  
Required. The updated service.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. List of fields to be updated in this request.  
**Returns**  
---  
**Type** | **Description**  
`[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Service)` |   
  
### updateService(UpdateServiceRequest request)
    
    
    public final Service updateService(UpdateServiceRequest request)

Updates a service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       UpdateServiceRequest request =
           UpdateServiceRequest.newBuilder()
               .setService(Service.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Service response = registrationServiceClient.updateService(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.UpdateServiceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Service)` |   
  
### updateServiceCallable()
    
    
    public final UnaryCallable<UpdateServiceRequest,Service> updateServiceCallable()

Updates a service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegistrationServiceClient registrationServiceClient = RegistrationServiceClient.create()) {
       UpdateServiceRequest request =
           UpdateServiceRequest.newBuilder()
               .setService(Service.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Service> future =
           registrationServiceClient.updateServiceCallable().futureCall(request);
       // Do something.
       Service response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.UpdateServiceRequest),[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Service)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
