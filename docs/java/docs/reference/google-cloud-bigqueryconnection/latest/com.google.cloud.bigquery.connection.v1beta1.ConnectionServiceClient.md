---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1beta1.ConnectionServiceClient
title: Class ConnectionServiceClient (2.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:15:06.601396+00:00
---

# Class ConnectionServiceClient (2.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1beta1.ConnectionServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ConnectionServiceClient (2.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.101.0 (latest)  2.97.0  2.96.0  2.95.0  2.93.0  2.90.0  2.89.0  2.87.0  2.85.0  2.84.0  2.83.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.74.0  2.72.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.6  2.4.0  2.2.4  2.1.11 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-bigqueryconnection/google-cloud-bigqueryconnection/src/main/java/com/google/cloud/bigquery/connection/v1beta1/ConnectionServiceClient.java)| [Product Reference](https://cloud.google.com/bigquery/docs/reference/bigqueryconnection/rest)  
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
       ConnectionProto.Connection connection = ConnectionProto.Connection.newBuilder().build();
       String connectionId = "connectionId1923106969";
       ConnectionProto.Connection response =
           connectionServiceClient.createConnection(parent, connection, connectionId);
     }
     

Note: close() needs to be called on the ConnectionServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateConnection |  Creates a new connection. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createConnection(ConnectionProto.CreateConnectionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createConnection(LocationName parent, ConnectionProto.Connection connection, String connectionId) 
  * createConnection(String parent, ConnectionProto.Connection connection, String connectionId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createConnectionCallable() 

  
GetConnection |  Returns specified connection. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getConnection(ConnectionProto.GetConnectionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getConnection(ConnectionName name) 
  * getConnection(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getConnectionCallable() 

  
ListConnections |  Returns a list of connections in the given project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listConnections(ConnectionProto.ListConnectionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listConnections(LocationName parent, UInt32Value maxResults) 
  * listConnections(String parent, UInt32Value maxResults) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listConnectionsCallable() 

  
UpdateConnection |  Updates the specified connection. For security reasons, also resets credential if connection properties are in the update field mask. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateConnection(ConnectionProto.UpdateConnectionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateConnection(ConnectionName name, ConnectionProto.Connection connection, FieldMask updateMask) 
  * updateConnection(String name, ConnectionProto.Connection connection, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateConnectionCallable() 

  
UpdateConnectionCredential |  Sets the credential for the specified connection. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateConnectionCredential(ConnectionProto.UpdateConnectionCredentialRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateConnectionCredential(String name, ConnectionProto.ConnectionCredential credential) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateConnectionCredentialCallable() 

  
DeleteConnection |  Deletes connection and associated credential. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteConnection(ConnectionProto.DeleteConnectionRequest request) 

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
`[ConnectionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1beta1.ConnectionServiceClient)` |   
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
`settings` | `[ConnectionServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1beta1.ConnectionServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1beta1.ConnectionServiceClient)` |   
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
`stub` | `[ConnectionServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1beta1.stub.ConnectionServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1beta1.ConnectionServiceClient)` |   
  
## Constructors 

### ConnectionServiceClient(ConnectionServiceSettings settings)
    
    
    protected ConnectionServiceClient(ConnectionServiceSettings settings)

Constructs an instance of ConnectionServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ConnectionServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1beta1.ConnectionServiceSettings)`  
  
  
### ConnectionServiceClient(ConnectionServiceStub stub)
    
    
    protected ConnectionServiceClient(ConnectionServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ConnectionServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1beta1.stub.ConnectionServiceStub)`  
  
  
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

### createConnection(@Nullable LocationName parent, ConnectionProto.Connection connection, String connectionId)
    
    
    public final ConnectionProto.Connection createConnection(@Nullable LocationName parent, ConnectionProto.Connection connection, String connectionId)

Creates a new connection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       ConnectionProto.Connection connection = ConnectionProto.Connection.newBuilder().build();
       String connectionId = "connectionId1923106969";
       ConnectionProto.Connection response =
           connectionServiceClient.createConnection(parent, connection, connectionId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.bigquery.connection.v1beta1.LocationName`  
Required. Parent resource name. Must be in the format `projects/{project_id}/locations/{location_id}`  
`connection` | `[ConnectionProto.Connection](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1beta1.ConnectionProto.Connection)`  
Required. Connection to create.  
`connectionId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. Connection id that should be assigned to the created connection.  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionProto.Connection](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1beta1.ConnectionProto.Connection)` |   
  
### createConnection(ConnectionProto.CreateConnectionRequest request)
    
    
    public final ConnectionProto.Connection createConnection(ConnectionProto.CreateConnectionRequest request)

Creates a new connection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       ConnectionProto.CreateConnectionRequest request =
           ConnectionProto.CreateConnectionRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setConnectionId("connectionId1923106969")
               .setConnection(ConnectionProto.Connection.newBuilder().build())
               .build();
       ConnectionProto.Connection response = connectionServiceClient.createConnection(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ConnectionProto.CreateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1beta1.ConnectionProto.CreateConnectionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionProto.Connection](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1beta1.ConnectionProto.Connection)` |   
  
### createConnection(String parent, ConnectionProto.Connection connection, String connectionId)
    
    
    public final ConnectionProto.Connection createConnection(String parent, ConnectionProto.Connection connection, String connectionId)

Creates a new connection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       ConnectionProto.Connection connection = ConnectionProto.Connection.newBuilder().build();
       String connectionId = "connectionId1923106969";
       ConnectionProto.Connection response =
           connectionServiceClient.createConnection(parent, connection, connectionId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Parent resource name. Must be in the format `projects/{project_id}/locations/{location_id}`  
`connection` | `[ConnectionProto.Connection](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1beta1.ConnectionProto.Connection)`  
Required. Connection to create.  
`connectionId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. Connection id that should be assigned to the created connection.  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionProto.Connection](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1beta1.ConnectionProto.Connection)` |   
  
### createConnectionCallable()
    
    
    public final UnaryCallable<ConnectionProto.CreateConnectionRequest,ConnectionProto.Connection> createConnectionCallable()

Creates a new connection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       ConnectionProto.CreateConnectionRequest request =
           ConnectionProto.CreateConnectionRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setConnectionId("connectionId1923106969")
               .setConnection(ConnectionProto.Connection.newBuilder().build())
               .build();
       ApiFuture<ConnectionProto.Connection> future =
           connectionServiceClient.createConnectionCallable().futureCall(request);
       // Do something.
       ConnectionProto.Connection response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1beta1.ConnectionProto.CreateConnectionRequest),[Connection](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1beta1.ConnectionProto.Connection)>` |   
  
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
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.bigquery.connection.v1beta1.ConnectionName`  
Required. Name of the deleted connection, for example: `projects/{project_id}/locations/{location_id}/connections/{connection_id}`  
  
### deleteConnection(ConnectionProto.DeleteConnectionRequest request)
    
    
    public final void deleteConnection(ConnectionProto.DeleteConnectionRequest request)

Deletes connection and associated credential.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       ConnectionProto.DeleteConnectionRequest request =
           ConnectionProto.DeleteConnectionRequest.newBuilder()
               .setName(ConnectionName.of("[PROJECT]", "[LOCATION]", "[CONNECTION]").toString())
               .build();
       connectionServiceClient.deleteConnection(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ConnectionProto.DeleteConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1beta1.ConnectionProto.DeleteConnectionRequest)`  
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
    
    
    public final UnaryCallable<ConnectionProto.DeleteConnectionRequest,Empty> deleteConnectionCallable()

Deletes connection and associated credential.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       ConnectionProto.DeleteConnectionRequest request =
           ConnectionProto.DeleteConnectionRequest.newBuilder()
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1beta1.ConnectionProto.DeleteConnectionRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getConnection(@Nullable ConnectionName name)
    
    
    public final ConnectionProto.Connection getConnection(@Nullable ConnectionName name)

Returns specified connection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       ConnectionName name = ConnectionName.of("[PROJECT]", "[LOCATION]", "[CONNECTION]");
       ConnectionProto.Connection response = connectionServiceClient.getConnection(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.bigquery.connection.v1beta1.ConnectionName`  
Required. Name of the requested connection, for example: `projects/{project_id}/locations/{location_id}/connections/{connection_id}`  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionProto.Connection](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1beta1.ConnectionProto.Connection)` |   
  
### getConnection(ConnectionProto.GetConnectionRequest request)
    
    
    public final ConnectionProto.Connection getConnection(ConnectionProto.GetConnectionRequest request)

Returns specified connection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       ConnectionProto.GetConnectionRequest request =
           ConnectionProto.GetConnectionRequest.newBuilder()
               .setName(ConnectionName.of("[PROJECT]", "[LOCATION]", "[CONNECTION]").toString())
               .build();
       ConnectionProto.Connection response = connectionServiceClient.getConnection(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ConnectionProto.GetConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1beta1.ConnectionProto.GetConnectionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionProto.Connection](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1beta1.ConnectionProto.Connection)` |   
  
### getConnection(String name)
    
    
    public final ConnectionProto.Connection getConnection(String name)

Returns specified connection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       String name = ConnectionName.of("[PROJECT]", "[LOCATION]", "[CONNECTION]").toString();
       ConnectionProto.Connection response = connectionServiceClient.getConnection(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the requested connection, for example: `projects/{project_id}/locations/{location_id}/connections/{connection_id}`  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionProto.Connection](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1beta1.ConnectionProto.Connection)` |   
  
### getConnectionCallable()
    
    
    public final UnaryCallable<ConnectionProto.GetConnectionRequest,ConnectionProto.Connection> getConnectionCallable()

Returns specified connection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       ConnectionProto.GetConnectionRequest request =
           ConnectionProto.GetConnectionRequest.newBuilder()
               .setName(ConnectionName.of("[PROJECT]", "[LOCATION]", "[CONNECTION]").toString())
               .build();
       ApiFuture<ConnectionProto.Connection> future =
           connectionServiceClient.getConnectionCallable().futureCall(request);
       // Do something.
       ConnectionProto.Connection response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1beta1.ConnectionProto.GetConnectionRequest),[Connection](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1beta1.ConnectionProto.Connection)>` |   
  
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
`@org.jspecify.annotations.Nullable com.google.cloud.bigquery.connection.v1beta1.ConnectionServiceSettings` |   
  
### getStub()
    
    
    public ConnectionServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[ConnectionServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1beta1.stub.ConnectionServiceStub)` |   
  
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
  
### listConnections(@Nullable LocationName parent, UInt32Value maxResults)
    
    
    public final ConnectionProto.ListConnectionsResponse listConnections(@Nullable LocationName parent, UInt32Value maxResults)

Returns a list of connections in the given project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       UInt32Value maxResults = UInt32Value.newBuilder().build();
       ConnectionProto.ListConnectionsResponse response =
           connectionServiceClient.listConnections(parent, maxResults);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.bigquery.connection.v1beta1.LocationName`  
Required. Parent resource name. Must be in the form: `projects/{project_id}/locations/{location_id}`  
`maxResults` | `[UInt32Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.UInt32Value.html)`  
Required. Maximum number of results per page.  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionProto.ListConnectionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1beta1.ConnectionProto.ListConnectionsResponse)` |   
  
### listConnections(ConnectionProto.ListConnectionsRequest request)
    
    
    public final ConnectionProto.ListConnectionsResponse listConnections(ConnectionProto.ListConnectionsRequest request)

Returns a list of connections in the given project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       ConnectionProto.ListConnectionsRequest request =
           ConnectionProto.ListConnectionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setMaxResults(UInt32Value.newBuilder().build())
               .setPageToken("pageToken873572522")
               .build();
       ConnectionProto.ListConnectionsResponse response =
           connectionServiceClient.listConnections(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ConnectionProto.ListConnectionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1beta1.ConnectionProto.ListConnectionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionProto.ListConnectionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1beta1.ConnectionProto.ListConnectionsResponse)` |   
  
### listConnections(String parent, UInt32Value maxResults)
    
    
    public final ConnectionProto.ListConnectionsResponse listConnections(String parent, UInt32Value maxResults)

Returns a list of connections in the given project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       UInt32Value maxResults = UInt32Value.newBuilder().build();
       ConnectionProto.ListConnectionsResponse response =
           connectionServiceClient.listConnections(parent, maxResults);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Parent resource name. Must be in the form: `projects/{project_id}/locations/{location_id}`  
`maxResults` | `[UInt32Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.UInt32Value.html)`  
Required. Maximum number of results per page.  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionProto.ListConnectionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1beta1.ConnectionProto.ListConnectionsResponse)` |   
  
### listConnectionsCallable()
    
    
    public final UnaryCallable<ConnectionProto.ListConnectionsRequest,ConnectionProto.ListConnectionsResponse> listConnectionsCallable()

Returns a list of connections in the given project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       ConnectionProto.ListConnectionsRequest request =
           ConnectionProto.ListConnectionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setMaxResults(UInt32Value.newBuilder().build())
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<ConnectionProto.ListConnectionsResponse> future =
           connectionServiceClient.listConnectionsCallable().futureCall(request);
       // Do something.
       ConnectionProto.ListConnectionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListConnectionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1beta1.ConnectionProto.ListConnectionsRequest),[ListConnectionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1beta1.ConnectionProto.ListConnectionsResponse)>` |   
  
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
  
### updateConnection(@Nullable ConnectionName name, ConnectionProto.Connection connection, FieldMask updateMask)
    
    
    public final ConnectionProto.Connection updateConnection(@Nullable ConnectionName name, ConnectionProto.Connection connection, FieldMask updateMask)

Updates the specified connection. For security reasons, also resets credential if connection properties are in the update field mask.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       ConnectionName name = ConnectionName.of("[PROJECT]", "[LOCATION]", "[CONNECTION]");
       ConnectionProto.Connection connection = ConnectionProto.Connection.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       ConnectionProto.Connection response =
           connectionServiceClient.updateConnection(name, connection, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.bigquery.connection.v1beta1.ConnectionName`  
Required. Name of the connection to update, for example: `projects/{project_id}/locations/{location_id}/connections/{connection_id}`  
`connection` | `[ConnectionProto.Connection](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1beta1.ConnectionProto.Connection)`  
Required. Connection containing the updated fields.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Update mask for the connection fields to be updated.  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionProto.Connection](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1beta1.ConnectionProto.Connection)` |   
  
### updateConnection(ConnectionProto.UpdateConnectionRequest request)
    
    
    public final ConnectionProto.Connection updateConnection(ConnectionProto.UpdateConnectionRequest request)

Updates the specified connection. For security reasons, also resets credential if connection properties are in the update field mask.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       ConnectionProto.UpdateConnectionRequest request =
           ConnectionProto.UpdateConnectionRequest.newBuilder()
               .setName(ConnectionName.of("[PROJECT]", "[LOCATION]", "[CONNECTION]").toString())
               .setConnection(ConnectionProto.Connection.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ConnectionProto.Connection response = connectionServiceClient.updateConnection(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ConnectionProto.UpdateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1beta1.ConnectionProto.UpdateConnectionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionProto.Connection](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1beta1.ConnectionProto.Connection)` |   
  
### updateConnection(String name, ConnectionProto.Connection connection, FieldMask updateMask)
    
    
    public final ConnectionProto.Connection updateConnection(String name, ConnectionProto.Connection connection, FieldMask updateMask)

Updates the specified connection. For security reasons, also resets credential if connection properties are in the update field mask.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       String name = ConnectionName.of("[PROJECT]", "[LOCATION]", "[CONNECTION]").toString();
       ConnectionProto.Connection connection = ConnectionProto.Connection.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       ConnectionProto.Connection response =
           connectionServiceClient.updateConnection(name, connection, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the connection to update, for example: `projects/{project_id}/locations/{location_id}/connections/{connection_id}`  
`connection` | `[ConnectionProto.Connection](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1beta1.ConnectionProto.Connection)`  
Required. Connection containing the updated fields.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Update mask for the connection fields to be updated.  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionProto.Connection](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1beta1.ConnectionProto.Connection)` |   
  
### updateConnectionCallable()
    
    
    public final UnaryCallable<ConnectionProto.UpdateConnectionRequest,ConnectionProto.Connection> updateConnectionCallable()

Updates the specified connection. For security reasons, also resets credential if connection properties are in the update field mask.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       ConnectionProto.UpdateConnectionRequest request =
           ConnectionProto.UpdateConnectionRequest.newBuilder()
               .setName(ConnectionName.of("[PROJECT]", "[LOCATION]", "[CONNECTION]").toString())
               .setConnection(ConnectionProto.Connection.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<ConnectionProto.Connection> future =
           connectionServiceClient.updateConnectionCallable().futureCall(request);
       // Do something.
       ConnectionProto.Connection response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1beta1.ConnectionProto.UpdateConnectionRequest),[Connection](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1beta1.ConnectionProto.Connection)>` |   
  
### updateConnectionCredential(ConnectionProto.UpdateConnectionCredentialRequest request)
    
    
    public final void updateConnectionCredential(ConnectionProto.UpdateConnectionCredentialRequest request)

Sets the credential for the specified connection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       ConnectionProto.UpdateConnectionCredentialRequest request =
           ConnectionProto.UpdateConnectionCredentialRequest.newBuilder()
               .setName("name3373707")
               .setCredential(ConnectionProto.ConnectionCredential.newBuilder().build())
               .build();
       connectionServiceClient.updateConnectionCredential(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ConnectionProto.UpdateConnectionCredentialRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1beta1.ConnectionProto.UpdateConnectionCredentialRequest)`  
The request object containing all of the parameters for the API call.  
  
### updateConnectionCredential(String name, ConnectionProto.ConnectionCredential credential)
    
    
    public final void updateConnectionCredential(String name, ConnectionProto.ConnectionCredential credential)

Sets the credential for the specified connection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       String name = "name3373707";
       ConnectionProto.ConnectionCredential credential =
           ConnectionProto.ConnectionCredential.newBuilder().build();
       connectionServiceClient.updateConnectionCredential(name, credential);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the connection, for example: `projects/{project_id}/locations/{location_id}/connections/{connection_id}/credential`  
`credential` | `[ConnectionProto.ConnectionCredential](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1beta1.ConnectionProto.ConnectionCredential)`  
Required. Credential to use with the connection.  
  
### updateConnectionCredentialCallable()
    
    
    public final UnaryCallable<ConnectionProto.UpdateConnectionCredentialRequest,Empty> updateConnectionCredentialCallable()

Sets the credential for the specified connection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.create()) {
       ConnectionProto.UpdateConnectionCredentialRequest request =
           ConnectionProto.UpdateConnectionCredentialRequest.newBuilder()
               .setName("name3373707")
               .setCredential(ConnectionProto.ConnectionCredential.newBuilder().build())
               .build();
       ApiFuture<Empty> future =
           connectionServiceClient.updateConnectionCredentialCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateConnectionCredentialRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1beta1.ConnectionProto.UpdateConnectionCredentialRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
