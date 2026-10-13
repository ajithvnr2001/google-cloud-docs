---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigqueryconnection.v1.ConnectionServiceClient
title: Class ConnectionServiceClient (2.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:14:30.792723+00:00
---

# Class ConnectionServiceClient (2.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigqueryconnection.v1.ConnectionServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ConnectionServiceClient (2.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.101.0 (latest)  2.97.0  2.96.0  2.95.0  2.93.0  2.90.0  2.89.0  2.87.0  2.85.0  2.84.0  2.83.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.74.0  2.72.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.6  2.4.0  2.2.4  2.1.11 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-bigqueryconnection/google-cloud-bigqueryconnection/src/main/java/com/google/cloud/bigqueryconnection/v1/ConnectionServiceClient.java)| [Product Reference](https://cloud.google.com/bigquery/docs/reference/bigqueryconnection/rest)  
---|---  
  
Service Description: Manages external data source connections and credentials.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Connection connection = Connection.newBuilder().build();
       String connectionId = "connectionId1923106969";
       Connection response =
           connectionServiceClient.createConnection(parent, connection, connectionId);
     }
     

Note: close() needs to be called on the ConnectionServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateConnection |  Creates a new connection. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createConnection(CreateConnectionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createConnection(LocationName parent, Connection connection, String connectionId) 
  * createConnection(String parent, Connection connection, String connectionId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createConnectionCallable() 

  
GetConnection |  Returns specified connection. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getConnection(GetConnectionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getConnection(ConnectionName name) 
  * getConnection(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getConnectionCallable() 

  
ListConnections |  Returns a list of connections in the given project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listConnections(ListConnectionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listConnections(LocationName parent) 
  * listConnections(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listConnectionsPagedCallable() 
  * listConnectionsCallable() 

  
UpdateConnection |  Updates the specified connection. For security reasons, also resets credential if connection properties are in the update field mask. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateConnection(UpdateConnectionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateConnection(ConnectionName name, Connection connection, FieldMask updateMask) 
  * updateConnection(String name, Connection connection, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateConnectionCallable() 

  
DeleteConnection |  Deletes connection and associated credential. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteConnection(DeleteConnectionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteConnection(ConnectionName name) 
  * deleteConnection(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteConnectionCallable() 

  
GetIamPolicy |  Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getIamPolicy(GetIamPolicyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getIamPolicy(ResourceName resource, GetPolicyOptions options) 
  * getIamPolicy(String resource, GetPolicyOptions options) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getIamPolicyCallable() 

  
SetIamPolicy |  Sets the access control policy on the specified resource. Replaces any existing policy.  Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setIamPolicy(SetIamPolicyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * setIamPolicy(ResourceName resource, Policy policy) 
  * setIamPolicy(String resource, Policy policy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setIamPolicyCallable() 

  
TestIamPermissions |  Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error.  Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * testIamPermissions(ResourceName resource, List<String> permissions) 
  * testIamPermissions(String resource, List<String> permissions) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of ConnectionServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ConnectionServiceSettings connectionServiceSettings =
         ConnectionServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     ConnectionServiceClient connectionServiceClient =
         ConnectionServiceClient.create(connectionServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ConnectionServiceSettings connectionServiceSettings =
         ConnectionServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     ConnectionServiceClient connectionServiceClient =
         ConnectionServiceClient.create(connectionServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ConnectionServiceSettings connectionServiceSettings =
         ConnectionServiceSettings.newHttpJsonBuilder().build();
     ConnectionServiceClient connectionServiceClient =
         ConnectionServiceClient.create(connectionServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ConnectionServiceClient

## Static Methods 

### create()
    
    
    public static final ConnectionServiceClient create()

Constructs an instance of ConnectionServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[ConnectionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigqueryconnection.v1.ConnectionServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ConnectionServiceSettings settings)
    
    
    public static final ConnectionServiceClient create(ConnectionServiceSettings settings)

Constructs an instance of ConnectionServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ConnectionServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigqueryconnection.v1.ConnectionServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigqueryconnection.v1.ConnectionServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ConnectionServiceStub stub)
    
    
    public static final ConnectionServiceClient create(ConnectionServiceStub stub)

Constructs an instance of ConnectionServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(ConnectionServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ConnectionServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigqueryconnection.v1.stub.ConnectionServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigqueryconnection.v1.ConnectionServiceClient)` |   
  
## Constructors 

### ConnectionServiceClient(ConnectionServiceSettings settings)
    
    
    protected ConnectionServiceClient(ConnectionServiceSettings settings)

Constructs an instance of ConnectionServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ConnectionServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigqueryconnection.v1.ConnectionServiceSettings)`  
  
  
### ConnectionServiceClient(ConnectionServiceStub stub)
    
    
    protected ConnectionServiceClient(ConnectionServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ConnectionServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigqueryconnection.v1.stub.ConnectionServiceStub)`  
  
  
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

### createConnection(@Nullable LocationName parent, Connection connection, String connectionId)
    
    
    public final Connection createConnection(@Nullable LocationName parent, Connection connection, String connectionId)

Creates a new connection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Connection connection = Connection.newBuilder().build();
       String connectionId = "connectionId1923106969";
       Connection response =
           connectionServiceClient.createConnection(parent, connection, connectionId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.bigquery.connection.v1.LocationName`  
Required. Parent resource name. Must be in the format `projects/{project_id}/locations/{location_id}`  
`connection` | `[Connection](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.Connection)`  
Required. Connection to create.  
`connectionId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. Connection id that should be assigned to the created connection.  
**Returns**  
---  
**Type** | **Description**  
`[Connection](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.Connection)` |   
  
### createConnection(CreateConnectionRequest request)
    
    
    public final Connection createConnection(CreateConnectionRequest request)

Creates a new connection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       CreateConnectionRequest request =
           CreateConnectionRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setConnectionId("connectionId1923106969")
               .setConnection(Connection.newBuilder().build())
               .build();
       Connection response = connectionServiceClient.createConnection(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.CreateConnectionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Connection](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.Connection)` |   
  
### createConnection(String parent, Connection connection, String connectionId)
    
    
    public final Connection createConnection(String parent, Connection connection, String connectionId)

Creates a new connection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Connection connection = Connection.newBuilder().build();
       String connectionId = "connectionId1923106969";
       Connection response =
           connectionServiceClient.createConnection(parent, connection, connectionId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Parent resource name. Must be in the format `projects/{project_id}/locations/{location_id}`  
`connection` | `[Connection](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.Connection)`  
Required. Connection to create.  
`connectionId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. Connection id that should be assigned to the created connection.  
**Returns**  
---  
**Type** | **Description**  
`[Connection](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.Connection)` |   
  
### createConnectionCallable()
    
    
    public final UnaryCallable<CreateConnectionRequest,Connection> createConnectionCallable()

Creates a new connection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       CreateConnectionRequest request =
           CreateConnectionRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setConnectionId("connectionId1923106969")
               .setConnection(Connection.newBuilder().build())
               .build();
       ApiFuture<Connection> future =
           connectionServiceClient.createConnectionCallable().futureCall(request);
       // Do something.
       Connection response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.CreateConnectionRequest),[Connection](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.Connection)>` |   
  
### deleteConnection(@Nullable ConnectionName name)
    
    
    public final void deleteConnection(@Nullable ConnectionName name)

Deletes connection and associated credential.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       ConnectionName name = ConnectionName.of("[PROJECT]", "[LOCATION]", "[CONNECTION]");
       connectionServiceClient.deleteConnection(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.bigquery.connection.v1.ConnectionName`  
Required. Name of the deleted connection, for example: `projects/{project_id}/locations/{location_id}/connections/{connection_id}`  
  
### deleteConnection(DeleteConnectionRequest request)
    
    
    public final void deleteConnection(DeleteConnectionRequest request)

Deletes connection and associated credential.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       DeleteConnectionRequest request =
           DeleteConnectionRequest.newBuilder()
               .setName(ConnectionName.of("[PROJECT]", "[LOCATION]", "[CONNECTION]").toString())
               .build();
       connectionServiceClient.deleteConnection(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.DeleteConnectionRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteConnection(String name)
    
    
    public final void deleteConnection(String name)

Deletes connection and associated credential.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       String name = ConnectionName.of("[PROJECT]", "[LOCATION]", "[CONNECTION]").toString();
       connectionServiceClient.deleteConnection(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the deleted connection, for example: `projects/{project_id}/locations/{location_id}/connections/{connection_id}`  
  
### deleteConnectionCallable()
    
    
    public final UnaryCallable<DeleteConnectionRequest,Empty> deleteConnectionCallable()

Deletes connection and associated credential.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       DeleteConnectionRequest request =
           DeleteConnectionRequest.newBuilder()
               .setName(ConnectionName.of("[PROJECT]", "[LOCATION]", "[CONNECTION]").toString())
               .build();
       ApiFuture<Empty> future =
           connectionServiceClient.deleteConnectionCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.DeleteConnectionRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getConnection(@Nullable ConnectionName name)
    
    
    public final Connection getConnection(@Nullable ConnectionName name)

Returns specified connection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       ConnectionName name = ConnectionName.of("[PROJECT]", "[LOCATION]", "[CONNECTION]");
       Connection response = connectionServiceClient.getConnection(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.bigquery.connection.v1.ConnectionName`  
Required. Name of the requested connection, for example: `projects/{project_id}/locations/{location_id}/connections/{connection_id}`  
**Returns**  
---  
**Type** | **Description**  
`[Connection](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.Connection)` |   
  
### getConnection(GetConnectionRequest request)
    
    
    public final Connection getConnection(GetConnectionRequest request)

Returns specified connection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       GetConnectionRequest request =
           GetConnectionRequest.newBuilder()
               .setName(ConnectionName.of("[PROJECT]", "[LOCATION]", "[CONNECTION]").toString())
               .build();
       Connection response = connectionServiceClient.getConnection(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.GetConnectionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Connection](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.Connection)` |   
  
### getConnection(String name)
    
    
    public final Connection getConnection(String name)

Returns specified connection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       String name = ConnectionName.of("[PROJECT]", "[LOCATION]", "[CONNECTION]").toString();
       Connection response = connectionServiceClient.getConnection(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the requested connection, for example: `projects/{project_id}/locations/{location_id}/connections/{connection_id}`  
**Returns**  
---  
**Type** | **Description**  
`[Connection](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.Connection)` |   
  
### getConnectionCallable()
    
    
    public final UnaryCallable<GetConnectionRequest,Connection> getConnectionCallable()

Returns specified connection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       GetConnectionRequest request =
           GetConnectionRequest.newBuilder()
               .setName(ConnectionName.of("[PROJECT]", "[LOCATION]", "[CONNECTION]").toString())
               .build();
       ApiFuture<Connection> future =
           connectionServiceClient.getConnectionCallable().futureCall(request);
       // Do something.
       Connection response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.GetConnectionRequest),[Connection](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.Connection)>` |   
  
### getIamPolicy(@Nullable ResourceName resource, GetPolicyOptions options)
    
    
    public final Policy getIamPolicy(@Nullable ResourceName resource, GetPolicyOptions options)

Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       ResourceName resource = ConnectionName.of("[PROJECT]", "[LOCATION]", "[CONNECTION]");
       GetPolicyOptions options = GetPolicyOptions.newBuilder().build();
       Policy response = connectionServiceClient.getIamPolicy(resource, options);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`resource` | `@org.jspecify.annotations.Nullable com.google.api.resourcenames.ResourceName`  
REQUIRED: The resource for which the policy is being requested. See the operation documentation for the appropriate value for this field.  
`options` | `com.google.iam.v1.GetPolicyOptions`  
OPTIONAL: A `GetPolicyOptions` object for specifying options to `GetIamPolicy`.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.Policy` |   
  
### getIamPolicy(GetIamPolicyRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRequest request)

Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(ConnectionName.of("[PROJECT]", "[LOCATION]", "[CONNECTION]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = connectionServiceClient.getIamPolicy(request);
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
  
### getIamPolicy(String resource, GetPolicyOptions options)
    
    
    public final Policy getIamPolicy(String resource, GetPolicyOptions options)

Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       String resource = ConnectionName.of("[PROJECT]", "[LOCATION]", "[CONNECTION]").toString();
       GetPolicyOptions options = GetPolicyOptions.newBuilder().build();
       Policy response = connectionServiceClient.getIamPolicy(resource, options);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
REQUIRED: The resource for which the policy is being requested. See the operation documentation for the appropriate value for this field.  
`options` | `com.google.iam.v1.GetPolicyOptions`  
OPTIONAL: A `GetPolicyOptions` object for specifying options to `GetIamPolicy`.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.Policy` |   
  
### getIamPolicyCallable()
    
    
    public final UnaryCallable<GetIamPolicyRequest,Policy> getIamPolicyCallable()

Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(ConnectionName.of("[PROJECT]", "[LOCATION]", "[CONNECTION]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future = connectionServiceClient.getIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.GetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### getSettings()
    
    
    public final @Nullable ConnectionServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.bigqueryconnection.v1.ConnectionServiceSettings` |   
  
### getStub()
    
    
    public ConnectionServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[ConnectionServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigqueryconnection.v1.stub.ConnectionServiceStub)` |   
  
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
  
### listConnections(@Nullable LocationName parent)
    
    
    public final ConnectionServiceClient.ListConnectionsPagedResponse listConnections(@Nullable LocationName parent)

Returns a list of connections in the given project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Connection element : connectionServiceClient.listConnections(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.bigquery.connection.v1.LocationName`  
Required. Parent resource name. Must be in the form: `projects/{project_id}/locations/{location_id}`  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionServiceClient.ListConnectionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigqueryconnection.v1.ConnectionServiceClient.ListConnectionsPagedResponse)` |   
  
### listConnections(ListConnectionsRequest request)
    
    
    public final ConnectionServiceClient.ListConnectionsPagedResponse listConnections(ListConnectionsRequest request)

Returns a list of connections in the given project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       ListConnectionsRequest request =
           ListConnectionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Connection element : connectionServiceClient.listConnections(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListConnectionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.ListConnectionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionServiceClient.ListConnectionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigqueryconnection.v1.ConnectionServiceClient.ListConnectionsPagedResponse)` |   
  
### listConnections(String parent)
    
    
    public final ConnectionServiceClient.ListConnectionsPagedResponse listConnections(String parent)

Returns a list of connections in the given project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Connection element : connectionServiceClient.listConnections(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Parent resource name. Must be in the form: `projects/{project_id}/locations/{location_id}`  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionServiceClient.ListConnectionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigqueryconnection.v1.ConnectionServiceClient.ListConnectionsPagedResponse)` |   
  
### listConnectionsCallable()
    
    
    public final UnaryCallable<ListConnectionsRequest,ListConnectionsResponse> listConnectionsCallable()

Returns a list of connections in the given project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       ListConnectionsRequest request =
           ListConnectionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListConnectionsResponse response =
             connectionServiceClient.listConnectionsCallable().call(request);
         for (Connection element : response.getConnectionsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListConnectionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.ListConnectionsRequest),[ListConnectionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.ListConnectionsResponse)>` |   
  
### listConnectionsPagedCallable()
    
    
    public final UnaryCallable<ListConnectionsRequest,ConnectionServiceClient.ListConnectionsPagedResponse> listConnectionsPagedCallable()

Returns a list of connections in the given project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       ListConnectionsRequest request =
           ListConnectionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Connection> future =
           connectionServiceClient.listConnectionsPagedCallable().futureCall(request);
       // Do something.
       for (Connection element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListConnectionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.ListConnectionsRequest),[ListConnectionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigqueryconnection.v1.ConnectionServiceClient.ListConnectionsPagedResponse)>` |   
  
### setIamPolicy(@Nullable ResourceName resource, Policy policy)
    
    
    public final Policy setIamPolicy(@Nullable ResourceName resource, Policy policy)

Sets the access control policy on the specified resource. Replaces any existing policy.

Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       ResourceName resource = ConnectionName.of("[PROJECT]", "[LOCATION]", "[CONNECTION]");
       Policy policy = Policy.newBuilder().build();
       Policy response = connectionServiceClient.setIamPolicy(resource, policy);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`resource` | `@org.jspecify.annotations.Nullable com.google.api.resourcenames.ResourceName`  
REQUIRED: The resource for which the policy is being specified. See the operation documentation for the appropriate value for this field.  
`policy` | `com.google.iam.v1.Policy`  
REQUIRED: The complete policy to be applied to the `resource`. The size of the policy is limited to a few 10s of KB. An empty policy is a valid policy but certain Cloud Platform services (such as Projects) might reject them.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.Policy` |   
  
### setIamPolicy(SetIamPolicyRequest request)
    
    
    public final Policy setIamPolicy(SetIamPolicyRequest request)

Sets the access control policy on the specified resource. Replaces any existing policy.

Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(ConnectionName.of("[PROJECT]", "[LOCATION]", "[CONNECTION]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = connectionServiceClient.setIamPolicy(request);
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
  
### setIamPolicy(String resource, Policy policy)
    
    
    public final Policy setIamPolicy(String resource, Policy policy)

Sets the access control policy on the specified resource. Replaces any existing policy.

Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       String resource = ConnectionName.of("[PROJECT]", "[LOCATION]", "[CONNECTION]").toString();
       Policy policy = Policy.newBuilder().build();
       Policy response = connectionServiceClient.setIamPolicy(resource, policy);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
REQUIRED: The resource for which the policy is being specified. See the operation documentation for the appropriate value for this field.  
`policy` | `com.google.iam.v1.Policy`  
REQUIRED: The complete policy to be applied to the `resource`. The size of the policy is limited to a few 10s of KB. An empty policy is a valid policy but certain Cloud Platform services (such as Projects) might reject them.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.Policy` |   
  
### setIamPolicyCallable()
    
    
    public final UnaryCallable<SetIamPolicyRequest,Policy> setIamPolicyCallable()

Sets the access control policy on the specified resource. Replaces any existing policy.

Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(ConnectionName.of("[PROJECT]", "[LOCATION]", "[CONNECTION]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Policy> future = connectionServiceClient.setIamPolicyCallable().futureCall(request);
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

### testIamPermissions(@Nullable ResourceName resource, List<String> permissions)
    
    
    public final TestIamPermissionsResponse testIamPermissions(@Nullable ResourceName resource, List<String> permissions)

Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error.

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       ResourceName resource = ConnectionName.of("[PROJECT]", "[LOCATION]", "[CONNECTION]");
       List<String> permissions = new ArrayList<>();
       TestIamPermissionsResponse response =
           connectionServiceClient.testIamPermissions(resource, permissions);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`resource` | `@org.jspecify.annotations.Nullable com.google.api.resourcenames.ResourceName`  
REQUIRED: The resource for which the policy detail is being requested. See the operation documentation for the appropriate value for this field.  
`permissions` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
The set of permissions to check for the `resource`. Permissions with wildcards (such as '*' or 'storage.*') are not allowed. For more information see [IAM Overview](https://cloud.google.com/iam/docs/overview#permissions).  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.TestIamPermissionsResponse` |   
  
### testIamPermissions(TestIamPermissionsRequest request)
    
    
    public final TestIamPermissionsResponse testIamPermissions(TestIamPermissionsRequest request)

Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error.

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(ConnectionName.of("[PROJECT]", "[LOCATION]", "[CONNECTION]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response = connectionServiceClient.testIamPermissions(request);
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
  
### testIamPermissions(String resource, List<String> permissions)
    
    
    public final TestIamPermissionsResponse testIamPermissions(String resource, List<String> permissions)

Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error.

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       String resource = ConnectionName.of("[PROJECT]", "[LOCATION]", "[CONNECTION]").toString();
       List<String> permissions = new ArrayList<>();
       TestIamPermissionsResponse response =
           connectionServiceClient.testIamPermissions(resource, permissions);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
REQUIRED: The resource for which the policy detail is being requested. See the operation documentation for the appropriate value for this field.  
`permissions` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
The set of permissions to check for the `resource`. Permissions with wildcards (such as '*' or 'storage.*') are not allowed. For more information see [IAM Overview](https://cloud.google.com/iam/docs/overview#permissions).  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.TestIamPermissionsResponse` |   
  
### testIamPermissionsCallable()
    
    
    public final UnaryCallable<TestIamPermissionsRequest,TestIamPermissionsResponse> testIamPermissionsCallable()

Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error.

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(ConnectionName.of("[PROJECT]", "[LOCATION]", "[CONNECTION]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           connectionServiceClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### updateConnection(@Nullable ConnectionName name, Connection connection, FieldMask updateMask)
    
    
    public final Connection updateConnection(@Nullable ConnectionName name, Connection connection, FieldMask updateMask)

Updates the specified connection. For security reasons, also resets credential if connection properties are in the update field mask.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       ConnectionName name = ConnectionName.of("[PROJECT]", "[LOCATION]", "[CONNECTION]");
       Connection connection = Connection.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Connection response = connectionServiceClient.updateConnection(name, connection, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.bigquery.connection.v1.ConnectionName`  
Required. Name of the connection to update, for example: `projects/{project_id}/locations/{location_id}/connections/{connection_id}`  
`connection` | `[Connection](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.Connection)`  
Required. Connection containing the updated fields.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Update mask for the connection fields to be updated.  
**Returns**  
---  
**Type** | **Description**  
`[Connection](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.Connection)` |   
  
### updateConnection(UpdateConnectionRequest request)
    
    
    public final Connection updateConnection(UpdateConnectionRequest request)

Updates the specified connection. For security reasons, also resets credential if connection properties are in the update field mask.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       UpdateConnectionRequest request =
           UpdateConnectionRequest.newBuilder()
               .setName(ConnectionName.of("[PROJECT]", "[LOCATION]", "[CONNECTION]").toString())
               .setConnection(Connection.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Connection response = connectionServiceClient.updateConnection(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.UpdateConnectionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Connection](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.Connection)` |   
  
### updateConnection(String name, Connection connection, FieldMask updateMask)
    
    
    public final Connection updateConnection(String name, Connection connection, FieldMask updateMask)

Updates the specified connection. For security reasons, also resets credential if connection properties are in the update field mask.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       String name = ConnectionName.of("[PROJECT]", "[LOCATION]", "[CONNECTION]").toString();
       Connection connection = Connection.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Connection response = connectionServiceClient.updateConnection(name, connection, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the connection to update, for example: `projects/{project_id}/locations/{location_id}/connections/{connection_id}`  
`connection` | `[Connection](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.Connection)`  
Required. Connection containing the updated fields.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Update mask for the connection fields to be updated.  
**Returns**  
---  
**Type** | **Description**  
`[Connection](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.Connection)` |   
  
### updateConnectionCallable()
    
    
    public final UnaryCallable<UpdateConnectionRequest,Connection> updateConnectionCallable()

Updates the specified connection. For security reasons, also resets credential if connection properties are in the update field mask.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       UpdateConnectionRequest request =
           UpdateConnectionRequest.newBuilder()
               .setName(ConnectionName.of("[PROJECT]", "[LOCATION]", "[CONNECTION]").toString())
               .setConnection(Connection.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Connection> future =
           connectionServiceClient.updateConnectionCallable().futureCall(request);
       // Do something.
       Connection response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.UpdateConnectionRequest),[Connection](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.Connection)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
