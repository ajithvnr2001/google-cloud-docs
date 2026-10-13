---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.EnvironmentsClient
title: Class EnvironmentsClient (0.110.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:34:00.818384+00:00
---

# Class EnvironmentsClient (0.110.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.EnvironmentsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class EnvironmentsClient (0.110.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.110.0 (latest)  0.106.0  0.105.0  0.104.0  0.102.0  0.99.0  0.98.0  0.96.0  0.94.0  0.93.0  0.92.0  0.91.0  0.89.0  0.87.0  0.86.0  0.85.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.75.0  0.74.0  0.73.0  0.71.0  0.70.0  0.69.0  0.68.0  0.67.0  0.66.0  0.65.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.7  0.13.1  0.12.1  0.11.5 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-dialogflow-cx/google-cloud-dialogflow-cx/src/main/java/com/google/cloud/dialogflow/cx/v3/EnvironmentsClient.java)| [Product Reference](https://cloud.google.com/dialogflow/cx/docs)| [REST Documentation](https://cloud.google.com/dialogflow/cx/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/dialogflow/cx/docs/reference/rpc)  
---|---|---|---  
  
Service Description: Service for managing Environments.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       EnvironmentName name =
           EnvironmentName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENVIRONMENT]");
       Environment response = environmentsClient.getEnvironment(name);
     }
     

Note: close() needs to be called on the EnvironmentsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListEnvironments |  Returns the list of all environments in the specified Agent. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listEnvironments(ListEnvironmentsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listEnvironments(AgentName parent) 
  * listEnvironments(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listEnvironmentsPagedCallable() 
  * listEnvironmentsCallable() 

  
GetEnvironment |  Retrieves the specified Environment. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getEnvironment(GetEnvironmentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getEnvironment(EnvironmentName name) 
  * getEnvironment(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getEnvironmentCallable() 

  
CreateEnvironment |  Creates an Environment in the specified Agent.  This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:  \- `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct) \- `response`: Environment |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createEnvironmentAsync(CreateEnvironmentRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createEnvironmentAsync(AgentName parent, Environment environment) 
  * createEnvironmentAsync(String parent, Environment environment) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createEnvironmentOperationCallable() 
  * createEnvironmentCallable() 

  
UpdateEnvironment |  Updates the specified Environment.  This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:  \- `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct) \- `response`: Environment |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateEnvironmentAsync(UpdateEnvironmentRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateEnvironmentAsync(Environment environment, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateEnvironmentOperationCallable() 
  * updateEnvironmentCallable() 

  
DeleteEnvironment |  Deletes the specified Environment. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteEnvironment(DeleteEnvironmentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteEnvironment(EnvironmentName name) 
  * deleteEnvironment(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteEnvironmentCallable() 

  
LookupEnvironmentHistory |  Looks up the history of the specified Environment. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * lookupEnvironmentHistory(LookupEnvironmentHistoryRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * lookupEnvironmentHistory(EnvironmentName name) 
  * lookupEnvironmentHistory(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * lookupEnvironmentHistoryPagedCallable() 
  * lookupEnvironmentHistoryCallable() 

  
RunContinuousTest |  Kicks off a continuous test under the specified Environment.  This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:  \- `metadata`: RunContinuousTestMetadata \- `response`: RunContinuousTestResponse |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * runContinuousTestAsync(RunContinuousTestRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * runContinuousTestOperationCallable() 
  * runContinuousTestCallable() 

  
ListContinuousTestResults |  Fetches a list of continuous test results for a given environment. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listContinuousTestResults(ListContinuousTestResultsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listContinuousTestResults(EnvironmentName parent) 
  * listContinuousTestResults(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listContinuousTestResultsPagedCallable() 
  * listContinuousTestResultsCallable() 

  
DeployFlow |  Deploys a flow to the specified Environment.  This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:  \- `metadata`: DeployFlowMetadata \- `response`: DeployFlowResponse |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deployFlowAsync(DeployFlowRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deployFlowOperationCallable() 
  * deployFlowCallable() 

  
ListLocations |  Lists information about the supported locations for this service.  This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.  For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

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

This class can be customized by passing in a custom instance of EnvironmentsSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     EnvironmentsSettings environmentsSettings =
         EnvironmentsSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     EnvironmentsClient environmentsClient = EnvironmentsClient.create(environmentsSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     EnvironmentsSettings environmentsSettings =
         EnvironmentsSettings.newBuilder().setEndpoint(myEndpoint).build();
     EnvironmentsClient environmentsClient = EnvironmentsClient.create(environmentsSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     EnvironmentsSettings environmentsSettings = EnvironmentsSettings.newHttpJsonBuilder().build();
     EnvironmentsClient environmentsClient = EnvironmentsClient.create(environmentsSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > EnvironmentsClient

## Static Methods 

### create()
    
    
    public static final EnvironmentsClient create()

Constructs an instance of EnvironmentsClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[EnvironmentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.EnvironmentsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(EnvironmentsSettings settings)
    
    
    public static final EnvironmentsClient create(EnvironmentsSettings settings)

Constructs an instance of EnvironmentsClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[EnvironmentsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.EnvironmentsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[EnvironmentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.EnvironmentsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(EnvironmentsStub stub)
    
    
    public static final EnvironmentsClient create(EnvironmentsStub stub)

Constructs an instance of EnvironmentsClient, using the given stub for making calls. This is for advanced usage - prefer using create(EnvironmentsSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[EnvironmentsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.stub.EnvironmentsStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[EnvironmentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.EnvironmentsClient)` |   
  
## Constructors 

### EnvironmentsClient(EnvironmentsSettings settings)
    
    
    protected EnvironmentsClient(EnvironmentsSettings settings)

Constructs an instance of EnvironmentsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[EnvironmentsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.EnvironmentsSettings)`  
  
  
### EnvironmentsClient(EnvironmentsStub stub)
    
    
    protected EnvironmentsClient(EnvironmentsStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[EnvironmentsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.stub.EnvironmentsStub)`  
  
  
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

### createEnvironmentAsync(@Nullable AgentName parent, Environment environment)
    
    
    public final OperationFuture<Environment,Struct> createEnvironmentAsync(@Nullable AgentName parent, Environment environment)

Creates an Environment in the specified Agent.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)

  * `response`: Environment

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
        AgentName parent = AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]");
        Environment environment = Environment.newBuilder().build();
        Environment response = environmentsClient.createEnvironmentAsync(parent, environment).get();
        }
        




**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.AgentName`  
Required. The Agent to create an Environment for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
`environment` | `[Environment](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Environment)`  
Required. The environment to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Environment](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Environment),[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)>` |   
  
### createEnvironmentAsync(CreateEnvironmentRequest request)
    
    
    public final OperationFuture<Environment,Struct> createEnvironmentAsync(CreateEnvironmentRequest request)

Creates an Environment in the specified Agent.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)

  * `response`: Environment

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
        CreateEnvironmentRequest request =
            CreateEnvironmentRequest.newBuilder()
                .setParent(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
                .setEnvironment(Environment.newBuilder().build())
                .build();
        Environment response = environmentsClient.createEnvironmentAsync(request).get();
        }
        




**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateEnvironmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.CreateEnvironmentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Environment](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Environment),[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)>` |   
  
### createEnvironmentAsync(String parent, Environment environment)
    
    
    public final OperationFuture<Environment,Struct> createEnvironmentAsync(String parent, Environment environment)

Creates an Environment in the specified Agent.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)

  * `response`: Environment

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
        String parent = AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString();
        Environment environment = Environment.newBuilder().build();
        Environment response = environmentsClient.createEnvironmentAsync(parent, environment).get();
        }
        




**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The Agent to create an Environment for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
`environment` | `[Environment](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Environment)`  
Required. The environment to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Environment](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Environment),[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)>` |   
  
### createEnvironmentCallable()
    
    
    public final UnaryCallable<CreateEnvironmentRequest,Operation> createEnvironmentCallable()

Creates an Environment in the specified Agent.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)

  * `response`: Environment

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
        CreateEnvironmentRequest request =
            CreateEnvironmentRequest.newBuilder()
                .setParent(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
                .setEnvironment(Environment.newBuilder().build())
                .build();
        ApiFuture<Operation> future =
            environmentsClient.createEnvironmentCallable().futureCall(request);
        // Do something.
        Operation response = future.get();
        }
        




**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateEnvironmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.CreateEnvironmentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createEnvironmentOperationCallable()
    
    
    public final OperationCallable<CreateEnvironmentRequest,Environment,Struct> createEnvironmentOperationCallable()

Creates an Environment in the specified Agent.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)

  * `response`: Environment

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
        CreateEnvironmentRequest request =
            CreateEnvironmentRequest.newBuilder()
                .setParent(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
                .setEnvironment(Environment.newBuilder().build())
                .build();
        OperationFuture<Environment, Struct> future =
            environmentsClient.createEnvironmentOperationCallable().futureCall(request);
        // Do something.
        Environment response = future.get();
        }
        




**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateEnvironmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.CreateEnvironmentRequest),[Environment](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Environment),[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)>` |   
  
### deleteEnvironment(@Nullable EnvironmentName name)
    
    
    public final void deleteEnvironment(@Nullable EnvironmentName name)

Deletes the specified Environment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       EnvironmentName name =
           EnvironmentName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENVIRONMENT]");
       environmentsClient.deleteEnvironment(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.EnvironmentName`  
Required. The name of the Environment to delete. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>`.  
  
### deleteEnvironment(DeleteEnvironmentRequest request)
    
    
    public final void deleteEnvironment(DeleteEnvironmentRequest request)

Deletes the specified Environment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       DeleteEnvironmentRequest request =
           DeleteEnvironmentRequest.newBuilder()
               .setName(
                   EnvironmentName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENVIRONMENT]")
                       .toString())
               .build();
       environmentsClient.deleteEnvironment(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteEnvironmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DeleteEnvironmentRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteEnvironment(String name)
    
    
    public final void deleteEnvironment(String name)

Deletes the specified Environment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       String name =
           EnvironmentName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENVIRONMENT]").toString();
       environmentsClient.deleteEnvironment(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Environment to delete. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>`.  
  
### deleteEnvironmentCallable()
    
    
    public final UnaryCallable<DeleteEnvironmentRequest,Empty> deleteEnvironmentCallable()

Deletes the specified Environment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       DeleteEnvironmentRequest request =
           DeleteEnvironmentRequest.newBuilder()
               .setName(
                   EnvironmentName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENVIRONMENT]")
                       .toString())
               .build();
       ApiFuture<Empty> future = environmentsClient.deleteEnvironmentCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteEnvironmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DeleteEnvironmentRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deployFlowAsync(DeployFlowRequest request)
    
    
    public final OperationFuture<DeployFlowResponse,DeployFlowMetadata> deployFlowAsync(DeployFlowRequest request)

Deploys a flow to the specified Environment.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: DeployFlowMetadata \- `response`: DeployFlowResponse

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       DeployFlowRequest request =
           DeployFlowRequest.newBuilder()
               .setEnvironment(
                   EnvironmentName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENVIRONMENT]")
                       .toString())
               .setFlowVersion(
                   VersionName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[FLOW]", "[VERSION]")
                       .toString())
               .build();
       DeployFlowResponse response = environmentsClient.deployFlowAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeployFlowRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DeployFlowRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DeployFlowResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DeployFlowResponse),[DeployFlowMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DeployFlowMetadata)>` |   
  
### deployFlowCallable()
    
    
    public final UnaryCallable<DeployFlowRequest,Operation> deployFlowCallable()

Deploys a flow to the specified Environment.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: DeployFlowMetadata \- `response`: DeployFlowResponse

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       DeployFlowRequest request =
           DeployFlowRequest.newBuilder()
               .setEnvironment(
                   EnvironmentName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENVIRONMENT]")
                       .toString())
               .setFlowVersion(
                   VersionName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[FLOW]", "[VERSION]")
                       .toString())
               .build();
       ApiFuture<Operation> future = environmentsClient.deployFlowCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeployFlowRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DeployFlowRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deployFlowOperationCallable()
    
    
    public final OperationCallable<DeployFlowRequest,DeployFlowResponse,DeployFlowMetadata> deployFlowOperationCallable()

Deploys a flow to the specified Environment.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: DeployFlowMetadata \- `response`: DeployFlowResponse

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       DeployFlowRequest request =
           DeployFlowRequest.newBuilder()
               .setEnvironment(
                   EnvironmentName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENVIRONMENT]")
                       .toString())
               .setFlowVersion(
                   VersionName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[FLOW]", "[VERSION]")
                       .toString())
               .build();
       OperationFuture<DeployFlowResponse, DeployFlowMetadata> future =
           environmentsClient.deployFlowOperationCallable().futureCall(request);
       // Do something.
       DeployFlowResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeployFlowRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DeployFlowRequest),[DeployFlowResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DeployFlowResponse),[DeployFlowMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DeployFlowMetadata)>` |   
  
### getEnvironment(@Nullable EnvironmentName name)
    
    
    public final Environment getEnvironment(@Nullable EnvironmentName name)

Retrieves the specified Environment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       EnvironmentName name =
           EnvironmentName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENVIRONMENT]");
       Environment response = environmentsClient.getEnvironment(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.EnvironmentName`  
Required. The name of the Environment. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>`.  
**Returns**  
---  
**Type** | **Description**  
`[Environment](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Environment)` |   
  
### getEnvironment(GetEnvironmentRequest request)
    
    
    public final Environment getEnvironment(GetEnvironmentRequest request)

Retrieves the specified Environment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       GetEnvironmentRequest request =
           GetEnvironmentRequest.newBuilder()
               .setName(
                   EnvironmentName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENVIRONMENT]")
                       .toString())
               .build();
       Environment response = environmentsClient.getEnvironment(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetEnvironmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.GetEnvironmentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Environment](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Environment)` |   
  
### getEnvironment(String name)
    
    
    public final Environment getEnvironment(String name)

Retrieves the specified Environment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       String name =
           EnvironmentName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENVIRONMENT]").toString();
       Environment response = environmentsClient.getEnvironment(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Environment. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>`.  
**Returns**  
---  
**Type** | **Description**  
`[Environment](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Environment)` |   
  
### getEnvironmentCallable()
    
    
    public final UnaryCallable<GetEnvironmentRequest,Environment> getEnvironmentCallable()

Retrieves the specified Environment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       GetEnvironmentRequest request =
           GetEnvironmentRequest.newBuilder()
               .setName(
                   EnvironmentName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENVIRONMENT]")
                       .toString())
               .build();
       ApiFuture<Environment> future =
           environmentsClient.getEnvironmentCallable().futureCall(request);
       // Do something.
       Environment response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetEnvironmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.GetEnvironmentRequest),[Environment](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Environment)>` |   
  
### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = environmentsClient.getLocation(request);
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
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = environmentsClient.getLocationCallable().futureCall(request);
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
    
    
    public final @Nullable EnvironmentsSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.EnvironmentsSettings` |   
  
### getStub()
    
    
    public EnvironmentsStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[EnvironmentsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.stub.EnvironmentsStub)` |   
  
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
  
### listContinuousTestResults(@Nullable EnvironmentName parent)
    
    
    public final EnvironmentsClient.ListContinuousTestResultsPagedResponse listContinuousTestResults(@Nullable EnvironmentName parent)

Fetches a list of continuous test results for a given environment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       EnvironmentName parent =
           EnvironmentName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENVIRONMENT]");
       for (ContinuousTestResult element :
           environmentsClient.listContinuousTestResults(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.EnvironmentName`  
Required. The environment to list results for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>`.  
**Returns**  
---  
**Type** | **Description**  
`[EnvironmentsClient.ListContinuousTestResultsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.EnvironmentsClient.ListContinuousTestResultsPagedResponse)` |   
  
### listContinuousTestResults(ListContinuousTestResultsRequest request)
    
    
    public final EnvironmentsClient.ListContinuousTestResultsPagedResponse listContinuousTestResults(ListContinuousTestResultsRequest request)

Fetches a list of continuous test results for a given environment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       ListContinuousTestResultsRequest request =
           ListContinuousTestResultsRequest.newBuilder()
               .setParent(
                   EnvironmentName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENVIRONMENT]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (ContinuousTestResult element :
           environmentsClient.listContinuousTestResults(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListContinuousTestResultsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListContinuousTestResultsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[EnvironmentsClient.ListContinuousTestResultsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.EnvironmentsClient.ListContinuousTestResultsPagedResponse)` |   
  
### listContinuousTestResults(String parent)
    
    
    public final EnvironmentsClient.ListContinuousTestResultsPagedResponse listContinuousTestResults(String parent)

Fetches a list of continuous test results for a given environment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       String parent =
           EnvironmentName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENVIRONMENT]").toString();
       for (ContinuousTestResult element :
           environmentsClient.listContinuousTestResults(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The environment to list results for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>`.  
**Returns**  
---  
**Type** | **Description**  
`[EnvironmentsClient.ListContinuousTestResultsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.EnvironmentsClient.ListContinuousTestResultsPagedResponse)` |   
  
### listContinuousTestResultsCallable()
    
    
    public final UnaryCallable<ListContinuousTestResultsRequest,ListContinuousTestResultsResponse> listContinuousTestResultsCallable()

Fetches a list of continuous test results for a given environment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       ListContinuousTestResultsRequest request =
           ListContinuousTestResultsRequest.newBuilder()
               .setParent(
                   EnvironmentName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENVIRONMENT]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListContinuousTestResultsResponse response =
             environmentsClient.listContinuousTestResultsCallable().call(request);
         for (ContinuousTestResult element : response.getContinuousTestResultsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListContinuousTestResultsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListContinuousTestResultsRequest),[ListContinuousTestResultsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListContinuousTestResultsResponse)>` |   
  
### listContinuousTestResultsPagedCallable()
    
    
    public final UnaryCallable<ListContinuousTestResultsRequest,EnvironmentsClient.ListContinuousTestResultsPagedResponse> listContinuousTestResultsPagedCallable()

Fetches a list of continuous test results for a given environment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       ListContinuousTestResultsRequest request =
           ListContinuousTestResultsRequest.newBuilder()
               .setParent(
                   EnvironmentName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENVIRONMENT]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<ContinuousTestResult> future =
           environmentsClient.listContinuousTestResultsPagedCallable().futureCall(request);
       // Do something.
       for (ContinuousTestResult element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListContinuousTestResultsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListContinuousTestResultsRequest),[ListContinuousTestResultsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.EnvironmentsClient.ListContinuousTestResultsPagedResponse)>` |   
  
### listEnvironments(@Nullable AgentName parent)
    
    
    public final EnvironmentsClient.ListEnvironmentsPagedResponse listEnvironments(@Nullable AgentName parent)

Returns the list of all environments in the specified Agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       AgentName parent = AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]");
       for (Environment element : environmentsClient.listEnvironments(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.AgentName`  
Required. The Agent to list all environments for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
**Returns**  
---  
**Type** | **Description**  
`[EnvironmentsClient.ListEnvironmentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.EnvironmentsClient.ListEnvironmentsPagedResponse)` |   
  
### listEnvironments(ListEnvironmentsRequest request)
    
    
    public final EnvironmentsClient.ListEnvironmentsPagedResponse listEnvironments(ListEnvironmentsRequest request)

Returns the list of all environments in the specified Agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       ListEnvironmentsRequest request =
           ListEnvironmentsRequest.newBuilder()
               .setParent(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Environment element : environmentsClient.listEnvironments(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListEnvironmentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListEnvironmentsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[EnvironmentsClient.ListEnvironmentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.EnvironmentsClient.ListEnvironmentsPagedResponse)` |   
  
### listEnvironments(String parent)
    
    
    public final EnvironmentsClient.ListEnvironmentsPagedResponse listEnvironments(String parent)

Returns the list of all environments in the specified Agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       String parent = AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString();
       for (Environment element : environmentsClient.listEnvironments(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The Agent to list all environments for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
**Returns**  
---  
**Type** | **Description**  
`[EnvironmentsClient.ListEnvironmentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.EnvironmentsClient.ListEnvironmentsPagedResponse)` |   
  
### listEnvironmentsCallable()
    
    
    public final UnaryCallable<ListEnvironmentsRequest,ListEnvironmentsResponse> listEnvironmentsCallable()

Returns the list of all environments in the specified Agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       ListEnvironmentsRequest request =
           ListEnvironmentsRequest.newBuilder()
               .setParent(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListEnvironmentsResponse response =
             environmentsClient.listEnvironmentsCallable().call(request);
         for (Environment element : response.getEnvironmentsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListEnvironmentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListEnvironmentsRequest),[ListEnvironmentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListEnvironmentsResponse)>` |   
  
### listEnvironmentsPagedCallable()
    
    
    public final UnaryCallable<ListEnvironmentsRequest,EnvironmentsClient.ListEnvironmentsPagedResponse> listEnvironmentsPagedCallable()

Returns the list of all environments in the specified Agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       ListEnvironmentsRequest request =
           ListEnvironmentsRequest.newBuilder()
               .setParent(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Environment> future =
           environmentsClient.listEnvironmentsPagedCallable().futureCall(request);
       // Do something.
       for (Environment element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListEnvironmentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListEnvironmentsRequest),[ListEnvironmentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.EnvironmentsClient.ListEnvironmentsPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final EnvironmentsClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : environmentsClient.listLocations(request).iterateAll()) {
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
`[EnvironmentsClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.EnvironmentsClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response = environmentsClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,EnvironmentsClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           environmentsClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.EnvironmentsClient.ListLocationsPagedResponse)>` |   
  
### lookupEnvironmentHistory(@Nullable EnvironmentName name)
    
    
    public final EnvironmentsClient.LookupEnvironmentHistoryPagedResponse lookupEnvironmentHistory(@Nullable EnvironmentName name)

Looks up the history of the specified Environment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       EnvironmentName name =
           EnvironmentName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENVIRONMENT]");
       for (Environment element : environmentsClient.lookupEnvironmentHistory(name).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.EnvironmentName`  
Required. Resource name of the environment to look up the history for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>`.  
**Returns**  
---  
**Type** | **Description**  
`[EnvironmentsClient.LookupEnvironmentHistoryPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.EnvironmentsClient.LookupEnvironmentHistoryPagedResponse)` |   
  
### lookupEnvironmentHistory(LookupEnvironmentHistoryRequest request)
    
    
    public final EnvironmentsClient.LookupEnvironmentHistoryPagedResponse lookupEnvironmentHistory(LookupEnvironmentHistoryRequest request)

Looks up the history of the specified Environment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       LookupEnvironmentHistoryRequest request =
           LookupEnvironmentHistoryRequest.newBuilder()
               .setName(
                   EnvironmentName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENVIRONMENT]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Environment element :
           environmentsClient.lookupEnvironmentHistory(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[LookupEnvironmentHistoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.LookupEnvironmentHistoryRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[EnvironmentsClient.LookupEnvironmentHistoryPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.EnvironmentsClient.LookupEnvironmentHistoryPagedResponse)` |   
  
### lookupEnvironmentHistory(String name)
    
    
    public final EnvironmentsClient.LookupEnvironmentHistoryPagedResponse lookupEnvironmentHistory(String name)

Looks up the history of the specified Environment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       String name =
           EnvironmentName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENVIRONMENT]").toString();
       for (Environment element : environmentsClient.lookupEnvironmentHistory(name).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of the environment to look up the history for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>`.  
**Returns**  
---  
**Type** | **Description**  
`[EnvironmentsClient.LookupEnvironmentHistoryPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.EnvironmentsClient.LookupEnvironmentHistoryPagedResponse)` |   
  
### lookupEnvironmentHistoryCallable()
    
    
    public final UnaryCallable<LookupEnvironmentHistoryRequest,LookupEnvironmentHistoryResponse> lookupEnvironmentHistoryCallable()

Looks up the history of the specified Environment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       LookupEnvironmentHistoryRequest request =
           LookupEnvironmentHistoryRequest.newBuilder()
               .setName(
                   EnvironmentName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENVIRONMENT]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         LookupEnvironmentHistoryResponse response =
             environmentsClient.lookupEnvironmentHistoryCallable().call(request);
         for (Environment element : response.getEnvironmentsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[LookupEnvironmentHistoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.LookupEnvironmentHistoryRequest),[LookupEnvironmentHistoryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.LookupEnvironmentHistoryResponse)>` |   
  
### lookupEnvironmentHistoryPagedCallable()
    
    
    public final UnaryCallable<LookupEnvironmentHistoryRequest,EnvironmentsClient.LookupEnvironmentHistoryPagedResponse> lookupEnvironmentHistoryPagedCallable()

Looks up the history of the specified Environment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       LookupEnvironmentHistoryRequest request =
           LookupEnvironmentHistoryRequest.newBuilder()
               .setName(
                   EnvironmentName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENVIRONMENT]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Environment> future =
           environmentsClient.lookupEnvironmentHistoryPagedCallable().futureCall(request);
       // Do something.
       for (Environment element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[LookupEnvironmentHistoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.LookupEnvironmentHistoryRequest),[LookupEnvironmentHistoryPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.EnvironmentsClient.LookupEnvironmentHistoryPagedResponse)>` |   
  
### runContinuousTestAsync(RunContinuousTestRequest request)
    
    
    public final OperationFuture<RunContinuousTestResponse,RunContinuousTestMetadata> runContinuousTestAsync(RunContinuousTestRequest request)

Kicks off a continuous test under the specified Environment.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: RunContinuousTestMetadata \- `response`: RunContinuousTestResponse

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       RunContinuousTestRequest request =
           RunContinuousTestRequest.newBuilder()
               .setEnvironment(
                   EnvironmentName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENVIRONMENT]")
                       .toString())
               .build();
       RunContinuousTestResponse response = environmentsClient.runContinuousTestAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RunContinuousTestRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.RunContinuousTestRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[RunContinuousTestResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.RunContinuousTestResponse),[RunContinuousTestMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.RunContinuousTestMetadata)>` |   
  
### runContinuousTestCallable()
    
    
    public final UnaryCallable<RunContinuousTestRequest,Operation> runContinuousTestCallable()

Kicks off a continuous test under the specified Environment.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: RunContinuousTestMetadata \- `response`: RunContinuousTestResponse

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       RunContinuousTestRequest request =
           RunContinuousTestRequest.newBuilder()
               .setEnvironment(
                   EnvironmentName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENVIRONMENT]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           environmentsClient.runContinuousTestCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RunContinuousTestRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.RunContinuousTestRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### runContinuousTestOperationCallable()
    
    
    public final OperationCallable<RunContinuousTestRequest,RunContinuousTestResponse,RunContinuousTestMetadata> runContinuousTestOperationCallable()

Kicks off a continuous test under the specified Environment.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: RunContinuousTestMetadata \- `response`: RunContinuousTestResponse

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       RunContinuousTestRequest request =
           RunContinuousTestRequest.newBuilder()
               .setEnvironment(
                   EnvironmentName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENVIRONMENT]")
                       .toString())
               .build();
       OperationFuture<RunContinuousTestResponse, RunContinuousTestMetadata> future =
           environmentsClient.runContinuousTestOperationCallable().futureCall(request);
       // Do something.
       RunContinuousTestResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RunContinuousTestRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.RunContinuousTestRequest),[RunContinuousTestResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.RunContinuousTestResponse),[RunContinuousTestMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.RunContinuousTestMetadata)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateEnvironmentAsync(Environment environment, FieldMask updateMask)
    
    
    public final OperationFuture<Environment,Struct> updateEnvironmentAsync(Environment environment, FieldMask updateMask)

Updates the specified Environment.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)

  * `response`: Environment

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
        Environment environment = Environment.newBuilder().build();
        FieldMask updateMask = FieldMask.newBuilder().build();
        Environment response =
            environmentsClient.updateEnvironmentAsync(environment, updateMask).get();
        }
        




**Parameters**  
---  
**Name** | **Description**  
`environment` | `[Environment](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Environment)`  
Required. The environment to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. The mask to control which fields get updated.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Environment](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Environment),[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)>` |   
  
### updateEnvironmentAsync(UpdateEnvironmentRequest request)
    
    
    public final OperationFuture<Environment,Struct> updateEnvironmentAsync(UpdateEnvironmentRequest request)

Updates the specified Environment.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)

  * `response`: Environment

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
        UpdateEnvironmentRequest request =
            UpdateEnvironmentRequest.newBuilder()
                .setEnvironment(Environment.newBuilder().build())
                .setUpdateMask(FieldMask.newBuilder().build())
                .build();
        Environment response = environmentsClient.updateEnvironmentAsync(request).get();
        }
        




**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateEnvironmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.UpdateEnvironmentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Environment](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Environment),[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)>` |   
  
### updateEnvironmentCallable()
    
    
    public final UnaryCallable<UpdateEnvironmentRequest,Operation> updateEnvironmentCallable()

Updates the specified Environment.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)

  * `response`: Environment

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
        UpdateEnvironmentRequest request =
            UpdateEnvironmentRequest.newBuilder()
                .setEnvironment(Environment.newBuilder().build())
                .setUpdateMask(FieldMask.newBuilder().build())
                .build();
        ApiFuture<Operation> future =
            environmentsClient.updateEnvironmentCallable().futureCall(request);
        // Do something.
        Operation response = future.get();
        }
        




**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateEnvironmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.UpdateEnvironmentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateEnvironmentOperationCallable()
    
    
    public final OperationCallable<UpdateEnvironmentRequest,Environment,Struct> updateEnvironmentOperationCallable()

Updates the specified Environment.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)

  * `response`: Environment

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
        UpdateEnvironmentRequest request =
            UpdateEnvironmentRequest.newBuilder()
                .setEnvironment(Environment.newBuilder().build())
                .setUpdateMask(FieldMask.newBuilder().build())
                .build();
        OperationFuture<Environment, Struct> future =
            environmentsClient.updateEnvironmentOperationCallable().futureCall(request);
        // Do something.
        Environment response = future.get();
        }
        




**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateEnvironmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.UpdateEnvironmentRequest),[Environment](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Environment),[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
