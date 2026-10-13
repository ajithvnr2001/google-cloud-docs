---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.EnvironmentsClient
title: Class EnvironmentsClient (1.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:58.804994+00:00
---

# Class EnvironmentsClient (1.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.EnvironmentsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class EnvironmentsClient (1.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.99.0 (latest)  1.95.0  1.94.0  1.93.0  1.91.0  1.88.0  1.87.0  1.85.0  1.83.0  1.82.0  1.80.0  1.78.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.70.0  1.68.0  1.67.0  1.64.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-orchestration-airflow/google-cloud-orchestration-airflow/src/main/java/com/google/cloud/orchestration/airflow/service/v1/EnvironmentsClient.java)| [Product Reference](https://cloud.google.com/composer/docs)| [REST Documentation](https://cloud.google.com/composer/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/composer/docs/reference/rpc)  
---|---|---|---  
  
Service Description: Managed Apache Airflow Environments.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       String name = "name3373707";
       Environment response = environmentsClient.getEnvironment(name);
     }
     

Note: close() needs to be called on the EnvironmentsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateEnvironment |  Create a new environment. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createEnvironmentAsync(CreateEnvironmentRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createEnvironmentAsync(String parent, Environment environment) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createEnvironmentOperationCallable() 
  * createEnvironmentCallable() 

  
GetEnvironment |  Get an existing environment. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getEnvironment(GetEnvironmentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getEnvironment(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getEnvironmentCallable() 

  
ListEnvironments |  List environments. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listEnvironments(ListEnvironmentsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listEnvironments(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listEnvironmentsPagedCallable() 
  * listEnvironmentsCallable() 

  
UpdateEnvironment |  Update an environment. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateEnvironmentAsync(UpdateEnvironmentRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateEnvironmentAsync(String name, Environment environment, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateEnvironmentOperationCallable() 
  * updateEnvironmentCallable() 

  
DeleteEnvironment |  Delete an environment. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteEnvironmentAsync(DeleteEnvironmentRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteEnvironmentAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteEnvironmentOperationCallable() 
  * deleteEnvironmentCallable() 

  
ExecuteAirflowCommand |  Executes Airflow CLI command. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * executeAirflowCommand(ExecuteAirflowCommandRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * executeAirflowCommandCallable() 

  
StopAirflowCommand |  Stops Airflow CLI command execution. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * stopAirflowCommand(StopAirflowCommandRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * stopAirflowCommandCallable() 

  
PollAirflowCommand |  Polls Airflow CLI command execution and fetches logs. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * pollAirflowCommand(PollAirflowCommandRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * pollAirflowCommandCallable() 

  
ListWorkloads |  Lists workloads in a Cloud Composer environment. Workload is a unit that runs a single Composer component.  This method is supported for Cloud Composer environments in versions composer-2.*.*-airflow-*.*.* and newer. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listWorkloads(ListWorkloadsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listWorkloads(EnvironmentName parent) 
  * listWorkloads(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listWorkloadsPagedCallable() 
  * listWorkloadsCallable() 

  
CheckUpgrade |  Check if an upgrade operation on the environment will succeed.  In case of problems detailed info can be found in the returned Operation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * checkUpgradeAsync(CheckUpgradeRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * checkUpgradeOperationCallable() 
  * checkUpgradeCallable() 

  
CreateUserWorkloadsSecret |  Creates a user workloads Secret.  This method is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createUserWorkloadsSecret(CreateUserWorkloadsSecretRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createUserWorkloadsSecret(EnvironmentName parent, UserWorkloadsSecret userWorkloadsSecret) 
  * createUserWorkloadsSecret(String parent, UserWorkloadsSecret userWorkloadsSecret) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createUserWorkloadsSecretCallable() 

  
GetUserWorkloadsSecret |  Gets an existing user workloads Secret. Values of the "data" field in the response are cleared.  This method is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getUserWorkloadsSecret(GetUserWorkloadsSecretRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getUserWorkloadsSecret(UserWorkloadsSecretName name) 
  * getUserWorkloadsSecret(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getUserWorkloadsSecretCallable() 

  
ListUserWorkloadsSecrets |  Lists user workloads Secrets.  This method is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listUserWorkloadsSecrets(ListUserWorkloadsSecretsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listUserWorkloadsSecrets(EnvironmentName parent) 
  * listUserWorkloadsSecrets(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listUserWorkloadsSecretsPagedCallable() 
  * listUserWorkloadsSecretsCallable() 

  
UpdateUserWorkloadsSecret |  Updates a user workloads Secret.  This method is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateUserWorkloadsSecret(UpdateUserWorkloadsSecretRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateUserWorkloadsSecret(UserWorkloadsSecret userWorkloadsSecret) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateUserWorkloadsSecretCallable() 

  
DeleteUserWorkloadsSecret |  Deletes a user workloads Secret.  This method is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteUserWorkloadsSecret(DeleteUserWorkloadsSecretRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteUserWorkloadsSecret(UserWorkloadsSecretName name) 
  * deleteUserWorkloadsSecret(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteUserWorkloadsSecretCallable() 

  
CreateUserWorkloadsConfigMap |  Creates a user workloads ConfigMap.  This method is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createUserWorkloadsConfigMap(CreateUserWorkloadsConfigMapRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createUserWorkloadsConfigMap(EnvironmentName parent, UserWorkloadsConfigMap userWorkloadsConfigMap) 
  * createUserWorkloadsConfigMap(String parent, UserWorkloadsConfigMap userWorkloadsConfigMap) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createUserWorkloadsConfigMapCallable() 

  
GetUserWorkloadsConfigMap |  Gets an existing user workloads ConfigMap.  This method is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getUserWorkloadsConfigMap(GetUserWorkloadsConfigMapRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getUserWorkloadsConfigMap(UserWorkloadsConfigMapName name) 
  * getUserWorkloadsConfigMap(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getUserWorkloadsConfigMapCallable() 

  
ListUserWorkloadsConfigMaps |  Lists user workloads ConfigMaps.  This method is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listUserWorkloadsConfigMaps(ListUserWorkloadsConfigMapsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listUserWorkloadsConfigMaps(EnvironmentName parent) 
  * listUserWorkloadsConfigMaps(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listUserWorkloadsConfigMapsPagedCallable() 
  * listUserWorkloadsConfigMapsCallable() 

  
UpdateUserWorkloadsConfigMap |  Updates a user workloads ConfigMap.  This method is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateUserWorkloadsConfigMap(UpdateUserWorkloadsConfigMapRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateUserWorkloadsConfigMap(UserWorkloadsConfigMap userWorkloadsConfigMap) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateUserWorkloadsConfigMapCallable() 

  
DeleteUserWorkloadsConfigMap |  Deletes a user workloads ConfigMap.  This method is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteUserWorkloadsConfigMap(DeleteUserWorkloadsConfigMapRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteUserWorkloadsConfigMap(UserWorkloadsConfigMapName name) 
  * deleteUserWorkloadsConfigMap(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteUserWorkloadsConfigMapCallable() 

  
SaveSnapshot |  Creates a snapshots of a Cloud Composer environment.  As a result of this operation, snapshot of environment's state is stored in a location specified in the SaveSnapshotRequest. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * saveSnapshotAsync(SaveSnapshotRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * saveSnapshotOperationCallable() 
  * saveSnapshotCallable() 

  
LoadSnapshot |  Loads a snapshot of a Cloud Composer environment.  As a result of this operation, a snapshot of environment's specified in LoadSnapshotRequest is loaded into the environment. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * loadSnapshotAsync(LoadSnapshotRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * loadSnapshotOperationCallable() 
  * loadSnapshotCallable() 

  
DatabaseFailover |  Triggers database failover (only for highly resilient environments). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * databaseFailoverAsync(DatabaseFailoverRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * databaseFailoverOperationCallable() 
  * databaseFailoverCallable() 

  
FetchDatabaseProperties |  Fetches database properties. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * fetchDatabaseProperties(FetchDatabasePropertiesRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * fetchDatabasePropertiesCallable() 

  
  
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
`[EnvironmentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.EnvironmentsClient)` |   
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
`settings` | `[EnvironmentsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.EnvironmentsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[EnvironmentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.EnvironmentsClient)` |   
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
`stub` | `[EnvironmentsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.stub.EnvironmentsStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[EnvironmentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.EnvironmentsClient)` |   
  
## Constructors 

### EnvironmentsClient(EnvironmentsSettings settings)
    
    
    protected EnvironmentsClient(EnvironmentsSettings settings)

Constructs an instance of EnvironmentsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[EnvironmentsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.EnvironmentsSettings)`  
  
  
### EnvironmentsClient(EnvironmentsStub stub)
    
    
    protected EnvironmentsClient(EnvironmentsStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[EnvironmentsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.stub.EnvironmentsStub)`  
  
  
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
  
### checkUpgradeAsync(CheckUpgradeRequest request)
    
    
    public final OperationFuture<CheckUpgradeResponse,OperationMetadata> checkUpgradeAsync(CheckUpgradeRequest request)

Check if an upgrade operation on the environment will succeed.

In case of problems detailed info can be found in the returned Operation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       CheckUpgradeRequest request =
           CheckUpgradeRequest.newBuilder()
               .setEnvironment("environment-85904877")
               .setImageVersion("imageVersion949870333")
               .build();
       CheckUpgradeResponse response = environmentsClient.checkUpgradeAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CheckUpgradeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.CheckUpgradeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[CheckUpgradeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.CheckUpgradeResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.OperationMetadata)>` |   
  
### checkUpgradeCallable()
    
    
    public final UnaryCallable<CheckUpgradeRequest,Operation> checkUpgradeCallable()

Check if an upgrade operation on the environment will succeed.

In case of problems detailed info can be found in the returned Operation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       CheckUpgradeRequest request =
           CheckUpgradeRequest.newBuilder()
               .setEnvironment("environment-85904877")
               .setImageVersion("imageVersion949870333")
               .build();
       ApiFuture<Operation> future = environmentsClient.checkUpgradeCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CheckUpgradeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.CheckUpgradeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### checkUpgradeOperationCallable()
    
    
    public final OperationCallable<CheckUpgradeRequest,CheckUpgradeResponse,OperationMetadata> checkUpgradeOperationCallable()

Check if an upgrade operation on the environment will succeed.

In case of problems detailed info can be found in the returned Operation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       CheckUpgradeRequest request =
           CheckUpgradeRequest.newBuilder()
               .setEnvironment("environment-85904877")
               .setImageVersion("imageVersion949870333")
               .build();
       OperationFuture<CheckUpgradeResponse, OperationMetadata> future =
           environmentsClient.checkUpgradeOperationCallable().futureCall(request);
       // Do something.
       CheckUpgradeResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CheckUpgradeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.CheckUpgradeRequest),[CheckUpgradeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.CheckUpgradeResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.OperationMetadata)>` |   
  
### close()
    
    
    public final void close()

### createEnvironmentAsync(CreateEnvironmentRequest request)
    
    
    public final OperationFuture<Environment,OperationMetadata> createEnvironmentAsync(CreateEnvironmentRequest request)

Create a new environment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       CreateEnvironmentRequest request =
           CreateEnvironmentRequest.newBuilder()
               .setParent("parent-995424086")
               .setEnvironment(Environment.newBuilder().build())
               .build();
       Environment response = environmentsClient.createEnvironmentAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateEnvironmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.CreateEnvironmentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Environment](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.Environment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.OperationMetadata)>` |   
  
### createEnvironmentAsync(String parent, Environment environment)
    
    
    public final OperationFuture<Environment,OperationMetadata> createEnvironmentAsync(String parent, Environment environment)

Create a new environment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       String parent = "parent-995424086";
       Environment environment = Environment.newBuilder().build();
       Environment response = environmentsClient.createEnvironmentAsync(parent, environment).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The parent must be of the form "projects/{projectId}/locations/{locationId}".  
`environment` | `[Environment](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.Environment)`  
The environment to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Environment](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.Environment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.OperationMetadata)>` |   
  
### createEnvironmentCallable()
    
    
    public final UnaryCallable<CreateEnvironmentRequest,Operation> createEnvironmentCallable()

Create a new environment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       CreateEnvironmentRequest request =
           CreateEnvironmentRequest.newBuilder()
               .setParent("parent-995424086")
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateEnvironmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.CreateEnvironmentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createEnvironmentOperationCallable()
    
    
    public final OperationCallable<CreateEnvironmentRequest,Environment,OperationMetadata> createEnvironmentOperationCallable()

Create a new environment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       CreateEnvironmentRequest request =
           CreateEnvironmentRequest.newBuilder()
               .setParent("parent-995424086")
               .setEnvironment(Environment.newBuilder().build())
               .build();
       OperationFuture<Environment, OperationMetadata> future =
           environmentsClient.createEnvironmentOperationCallable().futureCall(request);
       // Do something.
       Environment response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateEnvironmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.CreateEnvironmentRequest),[Environment](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.Environment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.OperationMetadata)>` |   
  
### createUserWorkloadsConfigMap(@Nullable EnvironmentName parent, UserWorkloadsConfigMap userWorkloadsConfigMap)
    
    
    public final UserWorkloadsConfigMap createUserWorkloadsConfigMap(@Nullable EnvironmentName parent, UserWorkloadsConfigMap userWorkloadsConfigMap)

Creates a user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       EnvironmentName parent = EnvironmentName.of("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]");
       UserWorkloadsConfigMap userWorkloadsConfigMap = UserWorkloadsConfigMap.newBuilder().build();
       UserWorkloadsConfigMap response =
           environmentsClient.createUserWorkloadsConfigMap(parent, userWorkloadsConfigMap);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.orchestration.airflow.service.v1.EnvironmentName`  
Required. The environment name to create a ConfigMap for, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}"  
`userWorkloadsConfigMap` | `[UserWorkloadsConfigMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.UserWorkloadsConfigMap)`  
Required. User workloads ConfigMap to create.  
**Returns**  
---  
**Type** | **Description**  
`[UserWorkloadsConfigMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.UserWorkloadsConfigMap)` |   
  
### createUserWorkloadsConfigMap(CreateUserWorkloadsConfigMapRequest request)
    
    
    public final UserWorkloadsConfigMap createUserWorkloadsConfigMap(CreateUserWorkloadsConfigMapRequest request)

Creates a user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       CreateUserWorkloadsConfigMapRequest request =
           CreateUserWorkloadsConfigMapRequest.newBuilder()
               .setParent(EnvironmentName.of("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]").toString())
               .setUserWorkloadsConfigMap(UserWorkloadsConfigMap.newBuilder().build())
               .build();
       UserWorkloadsConfigMap response = environmentsClient.createUserWorkloadsConfigMap(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateUserWorkloadsConfigMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.CreateUserWorkloadsConfigMapRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[UserWorkloadsConfigMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.UserWorkloadsConfigMap)` |   
  
### createUserWorkloadsConfigMap(String parent, UserWorkloadsConfigMap userWorkloadsConfigMap)
    
    
    public final UserWorkloadsConfigMap createUserWorkloadsConfigMap(String parent, UserWorkloadsConfigMap userWorkloadsConfigMap)

Creates a user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       String parent = EnvironmentName.of("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]").toString();
       UserWorkloadsConfigMap userWorkloadsConfigMap = UserWorkloadsConfigMap.newBuilder().build();
       UserWorkloadsConfigMap response =
           environmentsClient.createUserWorkloadsConfigMap(parent, userWorkloadsConfigMap);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The environment name to create a ConfigMap for, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}"  
`userWorkloadsConfigMap` | `[UserWorkloadsConfigMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.UserWorkloadsConfigMap)`  
Required. User workloads ConfigMap to create.  
**Returns**  
---  
**Type** | **Description**  
`[UserWorkloadsConfigMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.UserWorkloadsConfigMap)` |   
  
### createUserWorkloadsConfigMapCallable()
    
    
    public final UnaryCallable<CreateUserWorkloadsConfigMapRequest,UserWorkloadsConfigMap> createUserWorkloadsConfigMapCallable()

Creates a user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       CreateUserWorkloadsConfigMapRequest request =
           CreateUserWorkloadsConfigMapRequest.newBuilder()
               .setParent(EnvironmentName.of("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]").toString())
               .setUserWorkloadsConfigMap(UserWorkloadsConfigMap.newBuilder().build())
               .build();
       ApiFuture<UserWorkloadsConfigMap> future =
           environmentsClient.createUserWorkloadsConfigMapCallable().futureCall(request);
       // Do something.
       UserWorkloadsConfigMap response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateUserWorkloadsConfigMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.CreateUserWorkloadsConfigMapRequest),[UserWorkloadsConfigMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.UserWorkloadsConfigMap)>` |   
  
### createUserWorkloadsSecret(@Nullable EnvironmentName parent, UserWorkloadsSecret userWorkloadsSecret)
    
    
    public final UserWorkloadsSecret createUserWorkloadsSecret(@Nullable EnvironmentName parent, UserWorkloadsSecret userWorkloadsSecret)

Creates a user workloads Secret.

This method is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       EnvironmentName parent = EnvironmentName.of("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]");
       UserWorkloadsSecret userWorkloadsSecret = UserWorkloadsSecret.newBuilder().build();
       UserWorkloadsSecret response =
           environmentsClient.createUserWorkloadsSecret(parent, userWorkloadsSecret);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.orchestration.airflow.service.v1.EnvironmentName`  
Required. The environment name to create a Secret for, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}"  
`userWorkloadsSecret` | `[UserWorkloadsSecret](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.UserWorkloadsSecret)`  
Required. User workloads Secret to create.  
**Returns**  
---  
**Type** | **Description**  
`[UserWorkloadsSecret](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.UserWorkloadsSecret)` |   
  
### createUserWorkloadsSecret(CreateUserWorkloadsSecretRequest request)
    
    
    public final UserWorkloadsSecret createUserWorkloadsSecret(CreateUserWorkloadsSecretRequest request)

Creates a user workloads Secret.

This method is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       CreateUserWorkloadsSecretRequest request =
           CreateUserWorkloadsSecretRequest.newBuilder()
               .setParent(EnvironmentName.of("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]").toString())
               .setUserWorkloadsSecret(UserWorkloadsSecret.newBuilder().build())
               .build();
       UserWorkloadsSecret response = environmentsClient.createUserWorkloadsSecret(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateUserWorkloadsSecretRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.CreateUserWorkloadsSecretRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[UserWorkloadsSecret](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.UserWorkloadsSecret)` |   
  
### createUserWorkloadsSecret(String parent, UserWorkloadsSecret userWorkloadsSecret)
    
    
    public final UserWorkloadsSecret createUserWorkloadsSecret(String parent, UserWorkloadsSecret userWorkloadsSecret)

Creates a user workloads Secret.

This method is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       String parent = EnvironmentName.of("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]").toString();
       UserWorkloadsSecret userWorkloadsSecret = UserWorkloadsSecret.newBuilder().build();
       UserWorkloadsSecret response =
           environmentsClient.createUserWorkloadsSecret(parent, userWorkloadsSecret);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The environment name to create a Secret for, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}"  
`userWorkloadsSecret` | `[UserWorkloadsSecret](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.UserWorkloadsSecret)`  
Required. User workloads Secret to create.  
**Returns**  
---  
**Type** | **Description**  
`[UserWorkloadsSecret](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.UserWorkloadsSecret)` |   
  
### createUserWorkloadsSecretCallable()
    
    
    public final UnaryCallable<CreateUserWorkloadsSecretRequest,UserWorkloadsSecret> createUserWorkloadsSecretCallable()

Creates a user workloads Secret.

This method is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       CreateUserWorkloadsSecretRequest request =
           CreateUserWorkloadsSecretRequest.newBuilder()
               .setParent(EnvironmentName.of("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]").toString())
               .setUserWorkloadsSecret(UserWorkloadsSecret.newBuilder().build())
               .build();
       ApiFuture<UserWorkloadsSecret> future =
           environmentsClient.createUserWorkloadsSecretCallable().futureCall(request);
       // Do something.
       UserWorkloadsSecret response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateUserWorkloadsSecretRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.CreateUserWorkloadsSecretRequest),[UserWorkloadsSecret](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.UserWorkloadsSecret)>` |   
  
### databaseFailoverAsync(DatabaseFailoverRequest request)
    
    
    public final OperationFuture<DatabaseFailoverResponse,OperationMetadata> databaseFailoverAsync(DatabaseFailoverRequest request)

Triggers database failover (only for highly resilient environments).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       DatabaseFailoverRequest request =
           DatabaseFailoverRequest.newBuilder().setEnvironment("environment-85904877").build();
       DatabaseFailoverResponse response = environmentsClient.databaseFailoverAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DatabaseFailoverRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.DatabaseFailoverRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DatabaseFailoverResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.DatabaseFailoverResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.OperationMetadata)>` |   
  
### databaseFailoverCallable()
    
    
    public final UnaryCallable<DatabaseFailoverRequest,Operation> databaseFailoverCallable()

Triggers database failover (only for highly resilient environments).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       DatabaseFailoverRequest request =
           DatabaseFailoverRequest.newBuilder().setEnvironment("environment-85904877").build();
       ApiFuture<Operation> future =
           environmentsClient.databaseFailoverCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DatabaseFailoverRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.DatabaseFailoverRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### databaseFailoverOperationCallable()
    
    
    public final OperationCallable<DatabaseFailoverRequest,DatabaseFailoverResponse,OperationMetadata> databaseFailoverOperationCallable()

Triggers database failover (only for highly resilient environments).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       DatabaseFailoverRequest request =
           DatabaseFailoverRequest.newBuilder().setEnvironment("environment-85904877").build();
       OperationFuture<DatabaseFailoverResponse, OperationMetadata> future =
           environmentsClient.databaseFailoverOperationCallable().futureCall(request);
       // Do something.
       DatabaseFailoverResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DatabaseFailoverRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.DatabaseFailoverRequest),[DatabaseFailoverResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.DatabaseFailoverResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.OperationMetadata)>` |   
  
### deleteEnvironmentAsync(DeleteEnvironmentRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteEnvironmentAsync(DeleteEnvironmentRequest request)

Delete an environment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       DeleteEnvironmentRequest request =
           DeleteEnvironmentRequest.newBuilder().setName("name3373707").build();
       environmentsClient.deleteEnvironmentAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteEnvironmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.DeleteEnvironmentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.OperationMetadata)>` |   
  
### deleteEnvironmentAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteEnvironmentAsync(String name)

Delete an environment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       String name = "name3373707";
       environmentsClient.deleteEnvironmentAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The environment to delete, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}"  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.OperationMetadata)>` |   
  
### deleteEnvironmentCallable()
    
    
    public final UnaryCallable<DeleteEnvironmentRequest,Operation> deleteEnvironmentCallable()

Delete an environment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       DeleteEnvironmentRequest request =
           DeleteEnvironmentRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Operation> future =
           environmentsClient.deleteEnvironmentCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteEnvironmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.DeleteEnvironmentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteEnvironmentOperationCallable()
    
    
    public final OperationCallable<DeleteEnvironmentRequest,Empty,OperationMetadata> deleteEnvironmentOperationCallable()

Delete an environment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       DeleteEnvironmentRequest request =
           DeleteEnvironmentRequest.newBuilder().setName("name3373707").build();
       OperationFuture<Empty, OperationMetadata> future =
           environmentsClient.deleteEnvironmentOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteEnvironmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.DeleteEnvironmentRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.OperationMetadata)>` |   
  
### deleteUserWorkloadsConfigMap(@Nullable UserWorkloadsConfigMapName name)
    
    
    public final void deleteUserWorkloadsConfigMap(@Nullable UserWorkloadsConfigMapName name)

Deletes a user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       UserWorkloadsConfigMapName name =
           UserWorkloadsConfigMapName.of(
               "[PROJECT]", "[LOCATION]", "[ENVIRONMENT]", "[USER_WORKLOADS_CONFIG_MAP]");
       environmentsClient.deleteUserWorkloadsConfigMap(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.orchestration.airflow.service.v1.UserWorkloadsConfigMapName`  
Required. The ConfigMap to delete, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}/userWorkloadsConfigMaps/{userWorkloadsConfigMapId}"  
  
### deleteUserWorkloadsConfigMap(DeleteUserWorkloadsConfigMapRequest request)
    
    
    public final void deleteUserWorkloadsConfigMap(DeleteUserWorkloadsConfigMapRequest request)

Deletes a user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       DeleteUserWorkloadsConfigMapRequest request =
           DeleteUserWorkloadsConfigMapRequest.newBuilder()
               .setName(
                   UserWorkloadsConfigMapName.of(
                           "[PROJECT]", "[LOCATION]", "[ENVIRONMENT]", "[USER_WORKLOADS_CONFIG_MAP]")
                       .toString())
               .build();
       environmentsClient.deleteUserWorkloadsConfigMap(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteUserWorkloadsConfigMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.DeleteUserWorkloadsConfigMapRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteUserWorkloadsConfigMap(String name)
    
    
    public final void deleteUserWorkloadsConfigMap(String name)

Deletes a user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       String name =
           UserWorkloadsConfigMapName.of(
                   "[PROJECT]", "[LOCATION]", "[ENVIRONMENT]", "[USER_WORKLOADS_CONFIG_MAP]")
               .toString();
       environmentsClient.deleteUserWorkloadsConfigMap(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ConfigMap to delete, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}/userWorkloadsConfigMaps/{userWorkloadsConfigMapId}"  
  
### deleteUserWorkloadsConfigMapCallable()
    
    
    public final UnaryCallable<DeleteUserWorkloadsConfigMapRequest,Empty> deleteUserWorkloadsConfigMapCallable()

Deletes a user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       DeleteUserWorkloadsConfigMapRequest request =
           DeleteUserWorkloadsConfigMapRequest.newBuilder()
               .setName(
                   UserWorkloadsConfigMapName.of(
                           "[PROJECT]", "[LOCATION]", "[ENVIRONMENT]", "[USER_WORKLOADS_CONFIG_MAP]")
                       .toString())
               .build();
       ApiFuture<Empty> future =
           environmentsClient.deleteUserWorkloadsConfigMapCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteUserWorkloadsConfigMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.DeleteUserWorkloadsConfigMapRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteUserWorkloadsSecret(@Nullable UserWorkloadsSecretName name)
    
    
    public final void deleteUserWorkloadsSecret(@Nullable UserWorkloadsSecretName name)

Deletes a user workloads Secret.

This method is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       UserWorkloadsSecretName name =
           UserWorkloadsSecretName.of(
               "[PROJECT]", "[LOCATION]", "[ENVIRONMENT]", "[USER_WORKLOADS_SECRET]");
       environmentsClient.deleteUserWorkloadsSecret(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.orchestration.airflow.service.v1.UserWorkloadsSecretName`  
Required. The Secret to delete, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}/userWorkloadsSecrets/{userWorkloadsSecretId}"  
  
### deleteUserWorkloadsSecret(DeleteUserWorkloadsSecretRequest request)
    
    
    public final void deleteUserWorkloadsSecret(DeleteUserWorkloadsSecretRequest request)

Deletes a user workloads Secret.

This method is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       DeleteUserWorkloadsSecretRequest request =
           DeleteUserWorkloadsSecretRequest.newBuilder()
               .setName(
                   UserWorkloadsSecretName.of(
                           "[PROJECT]", "[LOCATION]", "[ENVIRONMENT]", "[USER_WORKLOADS_SECRET]")
                       .toString())
               .build();
       environmentsClient.deleteUserWorkloadsSecret(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteUserWorkloadsSecretRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.DeleteUserWorkloadsSecretRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteUserWorkloadsSecret(String name)
    
    
    public final void deleteUserWorkloadsSecret(String name)

Deletes a user workloads Secret.

This method is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       String name =
           UserWorkloadsSecretName.of(
                   "[PROJECT]", "[LOCATION]", "[ENVIRONMENT]", "[USER_WORKLOADS_SECRET]")
               .toString();
       environmentsClient.deleteUserWorkloadsSecret(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The Secret to delete, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}/userWorkloadsSecrets/{userWorkloadsSecretId}"  
  
### deleteUserWorkloadsSecretCallable()
    
    
    public final UnaryCallable<DeleteUserWorkloadsSecretRequest,Empty> deleteUserWorkloadsSecretCallable()

Deletes a user workloads Secret.

This method is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       DeleteUserWorkloadsSecretRequest request =
           DeleteUserWorkloadsSecretRequest.newBuilder()
               .setName(
                   UserWorkloadsSecretName.of(
                           "[PROJECT]", "[LOCATION]", "[ENVIRONMENT]", "[USER_WORKLOADS_SECRET]")
                       .toString())
               .build();
       ApiFuture<Empty> future =
           environmentsClient.deleteUserWorkloadsSecretCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteUserWorkloadsSecretRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.DeleteUserWorkloadsSecretRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### executeAirflowCommand(ExecuteAirflowCommandRequest request)
    
    
    public final ExecuteAirflowCommandResponse executeAirflowCommand(ExecuteAirflowCommandRequest request)

Executes Airflow CLI command.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       ExecuteAirflowCommandRequest request =
           ExecuteAirflowCommandRequest.newBuilder()
               .setEnvironment("environment-85904877")
               .setCommand("command950394699")
               .setSubcommand("subcommand2099091723")
               .addAllParameters(new ArrayList<String>())
               .build();
       ExecuteAirflowCommandResponse response = environmentsClient.executeAirflowCommand(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ExecuteAirflowCommandRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.ExecuteAirflowCommandRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ExecuteAirflowCommandResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.ExecuteAirflowCommandResponse)` |   
  
### executeAirflowCommandCallable()
    
    
    public final UnaryCallable<ExecuteAirflowCommandRequest,ExecuteAirflowCommandResponse> executeAirflowCommandCallable()

Executes Airflow CLI command.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       ExecuteAirflowCommandRequest request =
           ExecuteAirflowCommandRequest.newBuilder()
               .setEnvironment("environment-85904877")
               .setCommand("command950394699")
               .setSubcommand("subcommand2099091723")
               .addAllParameters(new ArrayList<String>())
               .build();
       ApiFuture<ExecuteAirflowCommandResponse> future =
           environmentsClient.executeAirflowCommandCallable().futureCall(request);
       // Do something.
       ExecuteAirflowCommandResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ExecuteAirflowCommandRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.ExecuteAirflowCommandRequest),[ExecuteAirflowCommandResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.ExecuteAirflowCommandResponse)>` |   
  
### fetchDatabaseProperties(FetchDatabasePropertiesRequest request)
    
    
    public final FetchDatabasePropertiesResponse fetchDatabaseProperties(FetchDatabasePropertiesRequest request)

Fetches database properties.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       FetchDatabasePropertiesRequest request =
           FetchDatabasePropertiesRequest.newBuilder()
               .setEnvironment(
                   EnvironmentName.of("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]").toString())
               .build();
       FetchDatabasePropertiesResponse response =
           environmentsClient.fetchDatabaseProperties(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FetchDatabasePropertiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.FetchDatabasePropertiesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FetchDatabasePropertiesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.FetchDatabasePropertiesResponse)` |   
  
### fetchDatabasePropertiesCallable()
    
    
    public final UnaryCallable<FetchDatabasePropertiesRequest,FetchDatabasePropertiesResponse> fetchDatabasePropertiesCallable()

Fetches database properties.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       FetchDatabasePropertiesRequest request =
           FetchDatabasePropertiesRequest.newBuilder()
               .setEnvironment(
                   EnvironmentName.of("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]").toString())
               .build();
       ApiFuture<FetchDatabasePropertiesResponse> future =
           environmentsClient.fetchDatabasePropertiesCallable().futureCall(request);
       // Do something.
       FetchDatabasePropertiesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FetchDatabasePropertiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.FetchDatabasePropertiesRequest),[FetchDatabasePropertiesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.FetchDatabasePropertiesResponse)>` |   
  
### getEnvironment(GetEnvironmentRequest request)
    
    
    public final Environment getEnvironment(GetEnvironmentRequest request)

Get an existing environment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       GetEnvironmentRequest request =
           GetEnvironmentRequest.newBuilder().setName("name3373707").build();
       Environment response = environmentsClient.getEnvironment(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetEnvironmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.GetEnvironmentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Environment](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.Environment)` |   
  
### getEnvironment(String name)
    
    
    public final Environment getEnvironment(String name)

Get an existing environment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       String name = "name3373707";
       Environment response = environmentsClient.getEnvironment(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The resource name of the environment to get, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}"  
**Returns**  
---  
**Type** | **Description**  
`[Environment](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.Environment)` |   
  
### getEnvironmentCallable()
    
    
    public final UnaryCallable<GetEnvironmentRequest,Environment> getEnvironmentCallable()

Get an existing environment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       GetEnvironmentRequest request =
           GetEnvironmentRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Environment> future =
           environmentsClient.getEnvironmentCallable().futureCall(request);
       // Do something.
       Environment response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetEnvironmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.GetEnvironmentRequest),[Environment](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.Environment)>` |   
  
### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
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
`@org.jspecify.annotations.Nullable com.google.cloud.orchestration.airflow.service.v1.EnvironmentsSettings` |   
  
### getStub()
    
    
    public EnvironmentsStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[EnvironmentsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.stub.EnvironmentsStub)` |   
  
### getUserWorkloadsConfigMap(@Nullable UserWorkloadsConfigMapName name)
    
    
    public final UserWorkloadsConfigMap getUserWorkloadsConfigMap(@Nullable UserWorkloadsConfigMapName name)

Gets an existing user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       UserWorkloadsConfigMapName name =
           UserWorkloadsConfigMapName.of(
               "[PROJECT]", "[LOCATION]", "[ENVIRONMENT]", "[USER_WORKLOADS_CONFIG_MAP]");
       UserWorkloadsConfigMap response = environmentsClient.getUserWorkloadsConfigMap(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.orchestration.airflow.service.v1.UserWorkloadsConfigMapName`  
Required. The resource name of the ConfigMap to get, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}/userWorkloadsConfigMaps/{userWorkloadsConfigMapId}"  
**Returns**  
---  
**Type** | **Description**  
`[UserWorkloadsConfigMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.UserWorkloadsConfigMap)` |   
  
### getUserWorkloadsConfigMap(GetUserWorkloadsConfigMapRequest request)
    
    
    public final UserWorkloadsConfigMap getUserWorkloadsConfigMap(GetUserWorkloadsConfigMapRequest request)

Gets an existing user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       GetUserWorkloadsConfigMapRequest request =
           GetUserWorkloadsConfigMapRequest.newBuilder()
               .setName(
                   UserWorkloadsConfigMapName.of(
                           "[PROJECT]", "[LOCATION]", "[ENVIRONMENT]", "[USER_WORKLOADS_CONFIG_MAP]")
                       .toString())
               .build();
       UserWorkloadsConfigMap response = environmentsClient.getUserWorkloadsConfigMap(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetUserWorkloadsConfigMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.GetUserWorkloadsConfigMapRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[UserWorkloadsConfigMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.UserWorkloadsConfigMap)` |   
  
### getUserWorkloadsConfigMap(String name)
    
    
    public final UserWorkloadsConfigMap getUserWorkloadsConfigMap(String name)

Gets an existing user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       String name =
           UserWorkloadsConfigMapName.of(
                   "[PROJECT]", "[LOCATION]", "[ENVIRONMENT]", "[USER_WORKLOADS_CONFIG_MAP]")
               .toString();
       UserWorkloadsConfigMap response = environmentsClient.getUserWorkloadsConfigMap(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the ConfigMap to get, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}/userWorkloadsConfigMaps/{userWorkloadsConfigMapId}"  
**Returns**  
---  
**Type** | **Description**  
`[UserWorkloadsConfigMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.UserWorkloadsConfigMap)` |   
  
### getUserWorkloadsConfigMapCallable()
    
    
    public final UnaryCallable<GetUserWorkloadsConfigMapRequest,UserWorkloadsConfigMap> getUserWorkloadsConfigMapCallable()

Gets an existing user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       GetUserWorkloadsConfigMapRequest request =
           GetUserWorkloadsConfigMapRequest.newBuilder()
               .setName(
                   UserWorkloadsConfigMapName.of(
                           "[PROJECT]", "[LOCATION]", "[ENVIRONMENT]", "[USER_WORKLOADS_CONFIG_MAP]")
                       .toString())
               .build();
       ApiFuture<UserWorkloadsConfigMap> future =
           environmentsClient.getUserWorkloadsConfigMapCallable().futureCall(request);
       // Do something.
       UserWorkloadsConfigMap response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetUserWorkloadsConfigMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.GetUserWorkloadsConfigMapRequest),[UserWorkloadsConfigMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.UserWorkloadsConfigMap)>` |   
  
### getUserWorkloadsSecret(@Nullable UserWorkloadsSecretName name)
    
    
    public final UserWorkloadsSecret getUserWorkloadsSecret(@Nullable UserWorkloadsSecretName name)

Gets an existing user workloads Secret. Values of the "data" field in the response are cleared.

This method is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       UserWorkloadsSecretName name =
           UserWorkloadsSecretName.of(
               "[PROJECT]", "[LOCATION]", "[ENVIRONMENT]", "[USER_WORKLOADS_SECRET]");
       UserWorkloadsSecret response = environmentsClient.getUserWorkloadsSecret(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.orchestration.airflow.service.v1.UserWorkloadsSecretName`  
Required. The resource name of the Secret to get, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}/userWorkloadsSecrets/{userWorkloadsSecretId}"  
**Returns**  
---  
**Type** | **Description**  
`[UserWorkloadsSecret](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.UserWorkloadsSecret)` |   
  
### getUserWorkloadsSecret(GetUserWorkloadsSecretRequest request)
    
    
    public final UserWorkloadsSecret getUserWorkloadsSecret(GetUserWorkloadsSecretRequest request)

Gets an existing user workloads Secret. Values of the "data" field in the response are cleared.

This method is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       GetUserWorkloadsSecretRequest request =
           GetUserWorkloadsSecretRequest.newBuilder()
               .setName(
                   UserWorkloadsSecretName.of(
                           "[PROJECT]", "[LOCATION]", "[ENVIRONMENT]", "[USER_WORKLOADS_SECRET]")
                       .toString())
               .build();
       UserWorkloadsSecret response = environmentsClient.getUserWorkloadsSecret(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetUserWorkloadsSecretRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.GetUserWorkloadsSecretRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[UserWorkloadsSecret](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.UserWorkloadsSecret)` |   
  
### getUserWorkloadsSecret(String name)
    
    
    public final UserWorkloadsSecret getUserWorkloadsSecret(String name)

Gets an existing user workloads Secret. Values of the "data" field in the response are cleared.

This method is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       String name =
           UserWorkloadsSecretName.of(
                   "[PROJECT]", "[LOCATION]", "[ENVIRONMENT]", "[USER_WORKLOADS_SECRET]")
               .toString();
       UserWorkloadsSecret response = environmentsClient.getUserWorkloadsSecret(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Secret to get, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}/userWorkloadsSecrets/{userWorkloadsSecretId}"  
**Returns**  
---  
**Type** | **Description**  
`[UserWorkloadsSecret](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.UserWorkloadsSecret)` |   
  
### getUserWorkloadsSecretCallable()
    
    
    public final UnaryCallable<GetUserWorkloadsSecretRequest,UserWorkloadsSecret> getUserWorkloadsSecretCallable()

Gets an existing user workloads Secret. Values of the "data" field in the response are cleared.

This method is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       GetUserWorkloadsSecretRequest request =
           GetUserWorkloadsSecretRequest.newBuilder()
               .setName(
                   UserWorkloadsSecretName.of(
                           "[PROJECT]", "[LOCATION]", "[ENVIRONMENT]", "[USER_WORKLOADS_SECRET]")
                       .toString())
               .build();
       ApiFuture<UserWorkloadsSecret> future =
           environmentsClient.getUserWorkloadsSecretCallable().futureCall(request);
       // Do something.
       UserWorkloadsSecret response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetUserWorkloadsSecretRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.GetUserWorkloadsSecretRequest),[UserWorkloadsSecret](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.UserWorkloadsSecret)>` |   
  
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
  
### listEnvironments(ListEnvironmentsRequest request)
    
    
    public final EnvironmentsClient.ListEnvironmentsPagedResponse listEnvironments(ListEnvironmentsRequest request)

List environments.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       ListEnvironmentsRequest request =
           ListEnvironmentsRequest.newBuilder()
               .setParent("parent-995424086")
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
`request` | `[ListEnvironmentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.ListEnvironmentsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[EnvironmentsClient.ListEnvironmentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.EnvironmentsClient.ListEnvironmentsPagedResponse)` |   
  
### listEnvironments(String parent)
    
    
    public final EnvironmentsClient.ListEnvironmentsPagedResponse listEnvironments(String parent)

List environments.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       String parent = "parent-995424086";
       for (Environment element : environmentsClient.listEnvironments(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
List environments in the given project and location, in the form: "projects/{projectId}/locations/{locationId}"  
**Returns**  
---  
**Type** | **Description**  
`[EnvironmentsClient.ListEnvironmentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.EnvironmentsClient.ListEnvironmentsPagedResponse)` |   
  
### listEnvironmentsCallable()
    
    
    public final UnaryCallable<ListEnvironmentsRequest,ListEnvironmentsResponse> listEnvironmentsCallable()

List environments.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       ListEnvironmentsRequest request =
           ListEnvironmentsRequest.newBuilder()
               .setParent("parent-995424086")
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListEnvironmentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.ListEnvironmentsRequest),[ListEnvironmentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.ListEnvironmentsResponse)>` |   
  
### listEnvironmentsPagedCallable()
    
    
    public final UnaryCallable<ListEnvironmentsRequest,EnvironmentsClient.ListEnvironmentsPagedResponse> listEnvironmentsPagedCallable()

List environments.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       ListEnvironmentsRequest request =
           ListEnvironmentsRequest.newBuilder()
               .setParent("parent-995424086")
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListEnvironmentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.ListEnvironmentsRequest),[ListEnvironmentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.EnvironmentsClient.ListEnvironmentsPagedResponse)>` |   
  
### listUserWorkloadsConfigMaps(@Nullable EnvironmentName parent)
    
    
    public final EnvironmentsClient.ListUserWorkloadsConfigMapsPagedResponse listUserWorkloadsConfigMaps(@Nullable EnvironmentName parent)

Lists user workloads ConfigMaps.

This method is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       EnvironmentName parent = EnvironmentName.of("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]");
       for (UserWorkloadsConfigMap element :
           environmentsClient.listUserWorkloadsConfigMaps(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.orchestration.airflow.service.v1.EnvironmentName`  
Required. List ConfigMaps in the given environment, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}"  
**Returns**  
---  
**Type** | **Description**  
`[EnvironmentsClient.ListUserWorkloadsConfigMapsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.EnvironmentsClient.ListUserWorkloadsConfigMapsPagedResponse)` |   
  
### listUserWorkloadsConfigMaps(ListUserWorkloadsConfigMapsRequest request)
    
    
    public final EnvironmentsClient.ListUserWorkloadsConfigMapsPagedResponse listUserWorkloadsConfigMaps(ListUserWorkloadsConfigMapsRequest request)

Lists user workloads ConfigMaps.

This method is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       ListUserWorkloadsConfigMapsRequest request =
           ListUserWorkloadsConfigMapsRequest.newBuilder()
               .setParent(EnvironmentName.of("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (UserWorkloadsConfigMap element :
           environmentsClient.listUserWorkloadsConfigMaps(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListUserWorkloadsConfigMapsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.ListUserWorkloadsConfigMapsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[EnvironmentsClient.ListUserWorkloadsConfigMapsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.EnvironmentsClient.ListUserWorkloadsConfigMapsPagedResponse)` |   
  
### listUserWorkloadsConfigMaps(String parent)
    
    
    public final EnvironmentsClient.ListUserWorkloadsConfigMapsPagedResponse listUserWorkloadsConfigMaps(String parent)

Lists user workloads ConfigMaps.

This method is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       String parent = EnvironmentName.of("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]").toString();
       for (UserWorkloadsConfigMap element :
           environmentsClient.listUserWorkloadsConfigMaps(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. List ConfigMaps in the given environment, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}"  
**Returns**  
---  
**Type** | **Description**  
`[EnvironmentsClient.ListUserWorkloadsConfigMapsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.EnvironmentsClient.ListUserWorkloadsConfigMapsPagedResponse)` |   
  
### listUserWorkloadsConfigMapsCallable()
    
    
    public final UnaryCallable<ListUserWorkloadsConfigMapsRequest,ListUserWorkloadsConfigMapsResponse> listUserWorkloadsConfigMapsCallable()

Lists user workloads ConfigMaps.

This method is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       ListUserWorkloadsConfigMapsRequest request =
           ListUserWorkloadsConfigMapsRequest.newBuilder()
               .setParent(EnvironmentName.of("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListUserWorkloadsConfigMapsResponse response =
             environmentsClient.listUserWorkloadsConfigMapsCallable().call(request);
         for (UserWorkloadsConfigMap element : response.getUserWorkloadsConfigMapsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListUserWorkloadsConfigMapsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.ListUserWorkloadsConfigMapsRequest),[ListUserWorkloadsConfigMapsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.ListUserWorkloadsConfigMapsResponse)>` |   
  
### listUserWorkloadsConfigMapsPagedCallable()
    
    
    public final UnaryCallable<ListUserWorkloadsConfigMapsRequest,EnvironmentsClient.ListUserWorkloadsConfigMapsPagedResponse> listUserWorkloadsConfigMapsPagedCallable()

Lists user workloads ConfigMaps.

This method is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       ListUserWorkloadsConfigMapsRequest request =
           ListUserWorkloadsConfigMapsRequest.newBuilder()
               .setParent(EnvironmentName.of("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<UserWorkloadsConfigMap> future =
           environmentsClient.listUserWorkloadsConfigMapsPagedCallable().futureCall(request);
       // Do something.
       for (UserWorkloadsConfigMap element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListUserWorkloadsConfigMapsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.ListUserWorkloadsConfigMapsRequest),[ListUserWorkloadsConfigMapsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.EnvironmentsClient.ListUserWorkloadsConfigMapsPagedResponse)>` |   
  
### listUserWorkloadsSecrets(@Nullable EnvironmentName parent)
    
    
    public final EnvironmentsClient.ListUserWorkloadsSecretsPagedResponse listUserWorkloadsSecrets(@Nullable EnvironmentName parent)

Lists user workloads Secrets.

This method is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       EnvironmentName parent = EnvironmentName.of("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]");
       for (UserWorkloadsSecret element :
           environmentsClient.listUserWorkloadsSecrets(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.orchestration.airflow.service.v1.EnvironmentName`  
Required. List Secrets in the given environment, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}"  
**Returns**  
---  
**Type** | **Description**  
`[EnvironmentsClient.ListUserWorkloadsSecretsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.EnvironmentsClient.ListUserWorkloadsSecretsPagedResponse)` |   
  
### listUserWorkloadsSecrets(ListUserWorkloadsSecretsRequest request)
    
    
    public final EnvironmentsClient.ListUserWorkloadsSecretsPagedResponse listUserWorkloadsSecrets(ListUserWorkloadsSecretsRequest request)

Lists user workloads Secrets.

This method is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       ListUserWorkloadsSecretsRequest request =
           ListUserWorkloadsSecretsRequest.newBuilder()
               .setParent(EnvironmentName.of("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (UserWorkloadsSecret element :
           environmentsClient.listUserWorkloadsSecrets(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListUserWorkloadsSecretsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.ListUserWorkloadsSecretsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[EnvironmentsClient.ListUserWorkloadsSecretsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.EnvironmentsClient.ListUserWorkloadsSecretsPagedResponse)` |   
  
### listUserWorkloadsSecrets(String parent)
    
    
    public final EnvironmentsClient.ListUserWorkloadsSecretsPagedResponse listUserWorkloadsSecrets(String parent)

Lists user workloads Secrets.

This method is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       String parent = EnvironmentName.of("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]").toString();
       for (UserWorkloadsSecret element :
           environmentsClient.listUserWorkloadsSecrets(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. List Secrets in the given environment, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}"  
**Returns**  
---  
**Type** | **Description**  
`[EnvironmentsClient.ListUserWorkloadsSecretsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.EnvironmentsClient.ListUserWorkloadsSecretsPagedResponse)` |   
  
### listUserWorkloadsSecretsCallable()
    
    
    public final UnaryCallable<ListUserWorkloadsSecretsRequest,ListUserWorkloadsSecretsResponse> listUserWorkloadsSecretsCallable()

Lists user workloads Secrets.

This method is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       ListUserWorkloadsSecretsRequest request =
           ListUserWorkloadsSecretsRequest.newBuilder()
               .setParent(EnvironmentName.of("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListUserWorkloadsSecretsResponse response =
             environmentsClient.listUserWorkloadsSecretsCallable().call(request);
         for (UserWorkloadsSecret element : response.getUserWorkloadsSecretsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListUserWorkloadsSecretsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.ListUserWorkloadsSecretsRequest),[ListUserWorkloadsSecretsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.ListUserWorkloadsSecretsResponse)>` |   
  
### listUserWorkloadsSecretsPagedCallable()
    
    
    public final UnaryCallable<ListUserWorkloadsSecretsRequest,EnvironmentsClient.ListUserWorkloadsSecretsPagedResponse> listUserWorkloadsSecretsPagedCallable()

Lists user workloads Secrets.

This method is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       ListUserWorkloadsSecretsRequest request =
           ListUserWorkloadsSecretsRequest.newBuilder()
               .setParent(EnvironmentName.of("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<UserWorkloadsSecret> future =
           environmentsClient.listUserWorkloadsSecretsPagedCallable().futureCall(request);
       // Do something.
       for (UserWorkloadsSecret element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListUserWorkloadsSecretsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.ListUserWorkloadsSecretsRequest),[ListUserWorkloadsSecretsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.EnvironmentsClient.ListUserWorkloadsSecretsPagedResponse)>` |   
  
### listWorkloads(@Nullable EnvironmentName parent)
    
    
    public final EnvironmentsClient.ListWorkloadsPagedResponse listWorkloads(@Nullable EnvironmentName parent)

Lists workloads in a Cloud Composer environment. Workload is a unit that runs a single Composer component.

This method is supported for Cloud Composer environments in versions composer-2.*.*-airflow-*.*.* and newer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       EnvironmentName parent = EnvironmentName.of("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]");
       for (ListWorkloadsResponse.ComposerWorkload element :
           environmentsClient.listWorkloads(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.orchestration.airflow.service.v1.EnvironmentName`  
Required. The environment name to get workloads for, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}"  
**Returns**  
---  
**Type** | **Description**  
`[EnvironmentsClient.ListWorkloadsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.EnvironmentsClient.ListWorkloadsPagedResponse)` |   
  
### listWorkloads(ListWorkloadsRequest request)
    
    
    public final EnvironmentsClient.ListWorkloadsPagedResponse listWorkloads(ListWorkloadsRequest request)

Lists workloads in a Cloud Composer environment. Workload is a unit that runs a single Composer component.

This method is supported for Cloud Composer environments in versions composer-2.*.*-airflow-*.*.* and newer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       ListWorkloadsRequest request =
           ListWorkloadsRequest.newBuilder()
               .setParent(EnvironmentName.of("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (ListWorkloadsResponse.ComposerWorkload element :
           environmentsClient.listWorkloads(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListWorkloadsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.ListWorkloadsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[EnvironmentsClient.ListWorkloadsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.EnvironmentsClient.ListWorkloadsPagedResponse)` |   
  
### listWorkloads(String parent)
    
    
    public final EnvironmentsClient.ListWorkloadsPagedResponse listWorkloads(String parent)

Lists workloads in a Cloud Composer environment. Workload is a unit that runs a single Composer component.

This method is supported for Cloud Composer environments in versions composer-2.*.*-airflow-*.*.* and newer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       String parent = EnvironmentName.of("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]").toString();
       for (ListWorkloadsResponse.ComposerWorkload element :
           environmentsClient.listWorkloads(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The environment name to get workloads for, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}"  
**Returns**  
---  
**Type** | **Description**  
`[EnvironmentsClient.ListWorkloadsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.EnvironmentsClient.ListWorkloadsPagedResponse)` |   
  
### listWorkloadsCallable()
    
    
    public final UnaryCallable<ListWorkloadsRequest,ListWorkloadsResponse> listWorkloadsCallable()

Lists workloads in a Cloud Composer environment. Workload is a unit that runs a single Composer component.

This method is supported for Cloud Composer environments in versions composer-2.*.*-airflow-*.*.* and newer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       ListWorkloadsRequest request =
           ListWorkloadsRequest.newBuilder()
               .setParent(EnvironmentName.of("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListWorkloadsResponse response = environmentsClient.listWorkloadsCallable().call(request);
         for (ListWorkloadsResponse.ComposerWorkload element : response.getWorkloadsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListWorkloadsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.ListWorkloadsRequest),[ListWorkloadsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.ListWorkloadsResponse)>` |   
  
### listWorkloadsPagedCallable()
    
    
    public final UnaryCallable<ListWorkloadsRequest,EnvironmentsClient.ListWorkloadsPagedResponse> listWorkloadsPagedCallable()

Lists workloads in a Cloud Composer environment. Workload is a unit that runs a single Composer component.

This method is supported for Cloud Composer environments in versions composer-2.*.*-airflow-*.*.* and newer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       ListWorkloadsRequest request =
           ListWorkloadsRequest.newBuilder()
               .setParent(EnvironmentName.of("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<ListWorkloadsResponse.ComposerWorkload> future =
           environmentsClient.listWorkloadsPagedCallable().futureCall(request);
       // Do something.
       for (ListWorkloadsResponse.ComposerWorkload element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListWorkloadsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.ListWorkloadsRequest),[ListWorkloadsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.EnvironmentsClient.ListWorkloadsPagedResponse)>` |   
  
### loadSnapshotAsync(LoadSnapshotRequest request)
    
    
    public final OperationFuture<LoadSnapshotResponse,OperationMetadata> loadSnapshotAsync(LoadSnapshotRequest request)

Loads a snapshot of a Cloud Composer environment.

As a result of this operation, a snapshot of environment's specified in LoadSnapshotRequest is loaded into the environment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       LoadSnapshotRequest request =
           LoadSnapshotRequest.newBuilder()
               .setEnvironment("environment-85904877")
               .setSnapshotPath("snapshotPath-931648503")
               .setSkipPypiPackagesInstallation(true)
               .setSkipEnvironmentVariablesSetting(true)
               .setSkipAirflowOverridesSetting(true)
               .setSkipGcsDataCopying(true)
               .build();
       LoadSnapshotResponse response = environmentsClient.loadSnapshotAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[LoadSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.LoadSnapshotRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[LoadSnapshotResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.LoadSnapshotResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.OperationMetadata)>` |   
  
### loadSnapshotCallable()
    
    
    public final UnaryCallable<LoadSnapshotRequest,Operation> loadSnapshotCallable()

Loads a snapshot of a Cloud Composer environment.

As a result of this operation, a snapshot of environment's specified in LoadSnapshotRequest is loaded into the environment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       LoadSnapshotRequest request =
           LoadSnapshotRequest.newBuilder()
               .setEnvironment("environment-85904877")
               .setSnapshotPath("snapshotPath-931648503")
               .setSkipPypiPackagesInstallation(true)
               .setSkipEnvironmentVariablesSetting(true)
               .setSkipAirflowOverridesSetting(true)
               .setSkipGcsDataCopying(true)
               .build();
       ApiFuture<Operation> future = environmentsClient.loadSnapshotCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[LoadSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.LoadSnapshotRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### loadSnapshotOperationCallable()
    
    
    public final OperationCallable<LoadSnapshotRequest,LoadSnapshotResponse,OperationMetadata> loadSnapshotOperationCallable()

Loads a snapshot of a Cloud Composer environment.

As a result of this operation, a snapshot of environment's specified in LoadSnapshotRequest is loaded into the environment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       LoadSnapshotRequest request =
           LoadSnapshotRequest.newBuilder()
               .setEnvironment("environment-85904877")
               .setSnapshotPath("snapshotPath-931648503")
               .setSkipPypiPackagesInstallation(true)
               .setSkipEnvironmentVariablesSetting(true)
               .setSkipAirflowOverridesSetting(true)
               .setSkipGcsDataCopying(true)
               .build();
       OperationFuture<LoadSnapshotResponse, OperationMetadata> future =
           environmentsClient.loadSnapshotOperationCallable().futureCall(request);
       // Do something.
       LoadSnapshotResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[LoadSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.LoadSnapshotRequest),[LoadSnapshotResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.LoadSnapshotResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.OperationMetadata)>` |   
  
### pollAirflowCommand(PollAirflowCommandRequest request)
    
    
    public final PollAirflowCommandResponse pollAirflowCommand(PollAirflowCommandRequest request)

Polls Airflow CLI command execution and fetches logs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       PollAirflowCommandRequest request =
           PollAirflowCommandRequest.newBuilder()
               .setEnvironment("environment-85904877")
               .setExecutionId("executionId-454906285")
               .setPod("pod111173")
               .setPodNamespace("podNamespace463962262")
               .setNextLineNumber(1176642216)
               .build();
       PollAirflowCommandResponse response = environmentsClient.pollAirflowCommand(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PollAirflowCommandRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.PollAirflowCommandRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PollAirflowCommandResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.PollAirflowCommandResponse)` |   
  
### pollAirflowCommandCallable()
    
    
    public final UnaryCallable<PollAirflowCommandRequest,PollAirflowCommandResponse> pollAirflowCommandCallable()

Polls Airflow CLI command execution and fetches logs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       PollAirflowCommandRequest request =
           PollAirflowCommandRequest.newBuilder()
               .setEnvironment("environment-85904877")
               .setExecutionId("executionId-454906285")
               .setPod("pod111173")
               .setPodNamespace("podNamespace463962262")
               .setNextLineNumber(1176642216)
               .build();
       ApiFuture<PollAirflowCommandResponse> future =
           environmentsClient.pollAirflowCommandCallable().futureCall(request);
       // Do something.
       PollAirflowCommandResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PollAirflowCommandRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.PollAirflowCommandRequest),[PollAirflowCommandResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.PollAirflowCommandResponse)>` |   
  
### saveSnapshotAsync(SaveSnapshotRequest request)
    
    
    public final OperationFuture<SaveSnapshotResponse,OperationMetadata> saveSnapshotAsync(SaveSnapshotRequest request)

Creates a snapshots of a Cloud Composer environment.

As a result of this operation, snapshot of environment's state is stored in a location specified in the SaveSnapshotRequest.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       SaveSnapshotRequest request =
           SaveSnapshotRequest.newBuilder()
               .setEnvironment("environment-85904877")
               .setSnapshotLocation("snapshotLocation1625609625")
               .build();
       SaveSnapshotResponse response = environmentsClient.saveSnapshotAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SaveSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.SaveSnapshotRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[SaveSnapshotResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.SaveSnapshotResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.OperationMetadata)>` |   
  
### saveSnapshotCallable()
    
    
    public final UnaryCallable<SaveSnapshotRequest,Operation> saveSnapshotCallable()

Creates a snapshots of a Cloud Composer environment.

As a result of this operation, snapshot of environment's state is stored in a location specified in the SaveSnapshotRequest.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       SaveSnapshotRequest request =
           SaveSnapshotRequest.newBuilder()
               .setEnvironment("environment-85904877")
               .setSnapshotLocation("snapshotLocation1625609625")
               .build();
       ApiFuture<Operation> future = environmentsClient.saveSnapshotCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SaveSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.SaveSnapshotRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### saveSnapshotOperationCallable()
    
    
    public final OperationCallable<SaveSnapshotRequest,SaveSnapshotResponse,OperationMetadata> saveSnapshotOperationCallable()

Creates a snapshots of a Cloud Composer environment.

As a result of this operation, snapshot of environment's state is stored in a location specified in the SaveSnapshotRequest.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       SaveSnapshotRequest request =
           SaveSnapshotRequest.newBuilder()
               .setEnvironment("environment-85904877")
               .setSnapshotLocation("snapshotLocation1625609625")
               .build();
       OperationFuture<SaveSnapshotResponse, OperationMetadata> future =
           environmentsClient.saveSnapshotOperationCallable().futureCall(request);
       // Do something.
       SaveSnapshotResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SaveSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.SaveSnapshotRequest),[SaveSnapshotResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.SaveSnapshotResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.OperationMetadata)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### stopAirflowCommand(StopAirflowCommandRequest request)
    
    
    public final StopAirflowCommandResponse stopAirflowCommand(StopAirflowCommandRequest request)

Stops Airflow CLI command execution.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       StopAirflowCommandRequest request =
           StopAirflowCommandRequest.newBuilder()
               .setEnvironment("environment-85904877")
               .setExecutionId("executionId-454906285")
               .setPod("pod111173")
               .setPodNamespace("podNamespace463962262")
               .setForce(true)
               .build();
       StopAirflowCommandResponse response = environmentsClient.stopAirflowCommand(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[StopAirflowCommandRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.StopAirflowCommandRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[StopAirflowCommandResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.StopAirflowCommandResponse)` |   
  
### stopAirflowCommandCallable()
    
    
    public final UnaryCallable<StopAirflowCommandRequest,StopAirflowCommandResponse> stopAirflowCommandCallable()

Stops Airflow CLI command execution.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       StopAirflowCommandRequest request =
           StopAirflowCommandRequest.newBuilder()
               .setEnvironment("environment-85904877")
               .setExecutionId("executionId-454906285")
               .setPod("pod111173")
               .setPodNamespace("podNamespace463962262")
               .setForce(true)
               .build();
       ApiFuture<StopAirflowCommandResponse> future =
           environmentsClient.stopAirflowCommandCallable().futureCall(request);
       // Do something.
       StopAirflowCommandResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[StopAirflowCommandRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.StopAirflowCommandRequest),[StopAirflowCommandResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.StopAirflowCommandResponse)>` |   
  
### updateEnvironmentAsync(UpdateEnvironmentRequest request)
    
    
    public final OperationFuture<Environment,OperationMetadata> updateEnvironmentAsync(UpdateEnvironmentRequest request)

Update an environment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       UpdateEnvironmentRequest request =
           UpdateEnvironmentRequest.newBuilder()
               .setName("name3373707")
               .setEnvironment(Environment.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Environment response = environmentsClient.updateEnvironmentAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateEnvironmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.UpdateEnvironmentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Environment](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.Environment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.OperationMetadata)>` |   
  
### updateEnvironmentAsync(String name, Environment environment, FieldMask updateMask)
    
    
    public final OperationFuture<Environment,OperationMetadata> updateEnvironmentAsync(String name, Environment environment, FieldMask updateMask)

Update an environment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       String name = "name3373707";
       Environment environment = Environment.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Environment response =
           environmentsClient.updateEnvironmentAsync(name, environment, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The relative resource name of the environment to update, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}"  
`environment` | `[Environment](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.Environment)`  
A patch environment. Fields specified by the `updateMask` will be copied from the patch environment into the environment under update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. A comma-separated list of paths, relative to `Environment`, of fields to update. For example, to set the version of scikit-learn to install in the environment to 0.19.0 and to remove an existing installation of numpy, the `updateMask` parameter would include the following two `paths` values: "config.softwareConfig.pypiPackages.scikit-learn" and "config.softwareConfig.pypiPackages.numpy". The included patch environment would specify the scikit-learn version as follows: { "config":{ "softwareConfig":{ "pypiPackages":{ "scikit-learn":"==0.19.0" } } } } Note that in the above example, any existing PyPI packages other than scikit-learn and numpy will be unaffected. Only one update type may be included in a single request's `updateMask`. For example, one cannot update both the PyPI packages and labels in the same request. However, it is possible to update multiple members of a map field simultaneously in the same request. For example, to set the labels "label1" and "label2" while clearing "label3" (assuming it already exists), one can provide the paths "labels.label1", "labels.label2", and "labels.label3" and populate the patch environment as follows: { "labels":{ "label1":"new-label1-value" "label2":"new-label2-value" } } Note that in the above example, any existing labels that are not included in the `updateMask` will be unaffected. It is also possible to replace an entire map field by providing the map field's path in the `updateMask`. The new value of the field will be that which is provided in the patch environment. For example, to delete all pre-existing user-specified PyPI packages and install botocore at version 1.7.14, the `updateMask` would contain the path "config.softwareConfig.pypiPackages", and the patch environment would be the following: { "config":{ "softwareConfig":{ "pypiPackages":{ "botocore":"==1.7.14" } } } } **Note:** Only the following fields can be updated: 

  * `config.softwareConfig.pypiPackages` * Replace all custom custom PyPI packages. If a replacement package map is not included in `environment`, all custom PyPI packages are cleared. It is an error to provide both this mask and a mask specifying an individual package. 
  * `config.softwareConfig.pypiPackages.`packagename * Update the custom PyPI package *packagename*, preserving other packages. To delete the package, include it in `updateMask`, and omit the mapping for it in `environment.config.softwareConfig.pypiPackages`. It is an error to provide both a mask of this form and the `config.softwareConfig.pypiPackages` mask. 
  * `labels` * Replace all environment labels. If a replacement labels map is not included in `environment`, all labels are cleared. It is an error to provide both this mask and a mask specifying one or more individual labels. 
  * `labels.`labelName * Set the label named *labelName*, while preserving other labels. To delete the label, include it in `updateMask` and omit its mapping in `environment.labels`. It is an error to provide both a mask of this form and the `labels` mask. 
  * `config.nodeCount` * Horizontally scale the number of nodes in the environment. An integer greater than or equal to 3 must be provided in the `config.nodeCount` field. Supported for Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*. 
  * `config.webServerNetworkAccessControl` * Replace the environment's current `WebServerNetworkAccessControl`. 
  * `config.softwareConfig.airflowConfigOverrides` * Replace all Apache Airflow config overrides. If a replacement config overrides map is not included in `environment`, all config overrides are cleared. It is an error to provide both this mask and a mask specifying one or more individual config overrides. 
  * `config.softwareConfig.airflowConfigOverrides.`section-name * Override the Apache Airflow config property *name* in the section named *section*, preserving other properties. To delete the property override, include it in `updateMask` and omit its mapping in `environment.config.softwareConfig.airflowConfigOverrides`. It is an error to provide both a mask of this form and the `config.softwareConfig.airflowConfigOverrides` mask. 
  * `config.softwareConfig.envVariables` * Replace all environment variables. If a replacement environment variable map is not included in `environment`, all custom environment variables are cleared. 
  * `config.softwareConfig.schedulerCount` * Horizontally scale the number of schedulers in Airflow. A positive integer not greater than the number of nodes must be provided in the `config.softwareConfig.schedulerCount` field. Supported for Cloud Composer environments in versions composer-1.*.*-airflow-2.*.*. 
  * `config.databaseConfig.machineType` * Cloud SQL machine type used by Airflow database. It has to be one of: db-n1-standard-2, db-n1-standard-4, db-n1-standard-8 or db-n1-standard-16. Supported for Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*. 
  * `config.webServerConfig.machineType` * Machine type on which Airflow web server is running. It has to be one of: composer-n1-webserver-2, composer-n1-webserver-4 or composer-n1-webserver-8. Supported for Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*. 

  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Environment](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.Environment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.OperationMetadata)>` |   
  
### updateEnvironmentCallable()
    
    
    public final UnaryCallable<UpdateEnvironmentRequest,Operation> updateEnvironmentCallable()

Update an environment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       UpdateEnvironmentRequest request =
           UpdateEnvironmentRequest.newBuilder()
               .setName("name3373707")
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateEnvironmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.UpdateEnvironmentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateEnvironmentOperationCallable()
    
    
    public final OperationCallable<UpdateEnvironmentRequest,Environment,OperationMetadata> updateEnvironmentOperationCallable()

Update an environment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       UpdateEnvironmentRequest request =
           UpdateEnvironmentRequest.newBuilder()
               .setName("name3373707")
               .setEnvironment(Environment.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       OperationFuture<Environment, OperationMetadata> future =
           environmentsClient.updateEnvironmentOperationCallable().futureCall(request);
       // Do something.
       Environment response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateEnvironmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.UpdateEnvironmentRequest),[Environment](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.Environment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.OperationMetadata)>` |   
  
### updateUserWorkloadsConfigMap(UpdateUserWorkloadsConfigMapRequest request)
    
    
    public final UserWorkloadsConfigMap updateUserWorkloadsConfigMap(UpdateUserWorkloadsConfigMapRequest request)

Updates a user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       UpdateUserWorkloadsConfigMapRequest request =
           UpdateUserWorkloadsConfigMapRequest.newBuilder()
               .setUserWorkloadsConfigMap(UserWorkloadsConfigMap.newBuilder().build())
               .build();
       UserWorkloadsConfigMap response = environmentsClient.updateUserWorkloadsConfigMap(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateUserWorkloadsConfigMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.UpdateUserWorkloadsConfigMapRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[UserWorkloadsConfigMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.UserWorkloadsConfigMap)` |   
  
### updateUserWorkloadsConfigMap(UserWorkloadsConfigMap userWorkloadsConfigMap)
    
    
    public final UserWorkloadsConfigMap updateUserWorkloadsConfigMap(UserWorkloadsConfigMap userWorkloadsConfigMap)

Updates a user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       UserWorkloadsConfigMap userWorkloadsConfigMap = UserWorkloadsConfigMap.newBuilder().build();
       UserWorkloadsConfigMap response =
           environmentsClient.updateUserWorkloadsConfigMap(userWorkloadsConfigMap);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`userWorkloadsConfigMap` | `[UserWorkloadsConfigMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.UserWorkloadsConfigMap)`  
Optional. User workloads ConfigMap to override.  
**Returns**  
---  
**Type** | **Description**  
`[UserWorkloadsConfigMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.UserWorkloadsConfigMap)` |   
  
### updateUserWorkloadsConfigMapCallable()
    
    
    public final UnaryCallable<UpdateUserWorkloadsConfigMapRequest,UserWorkloadsConfigMap> updateUserWorkloadsConfigMapCallable()

Updates a user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       UpdateUserWorkloadsConfigMapRequest request =
           UpdateUserWorkloadsConfigMapRequest.newBuilder()
               .setUserWorkloadsConfigMap(UserWorkloadsConfigMap.newBuilder().build())
               .build();
       ApiFuture<UserWorkloadsConfigMap> future =
           environmentsClient.updateUserWorkloadsConfigMapCallable().futureCall(request);
       // Do something.
       UserWorkloadsConfigMap response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateUserWorkloadsConfigMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.UpdateUserWorkloadsConfigMapRequest),[UserWorkloadsConfigMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.UserWorkloadsConfigMap)>` |   
  
### updateUserWorkloadsSecret(UpdateUserWorkloadsSecretRequest request)
    
    
    public final UserWorkloadsSecret updateUserWorkloadsSecret(UpdateUserWorkloadsSecretRequest request)

Updates a user workloads Secret.

This method is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       UpdateUserWorkloadsSecretRequest request =
           UpdateUserWorkloadsSecretRequest.newBuilder()
               .setUserWorkloadsSecret(UserWorkloadsSecret.newBuilder().build())
               .build();
       UserWorkloadsSecret response = environmentsClient.updateUserWorkloadsSecret(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateUserWorkloadsSecretRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.UpdateUserWorkloadsSecretRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[UserWorkloadsSecret](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.UserWorkloadsSecret)` |   
  
### updateUserWorkloadsSecret(UserWorkloadsSecret userWorkloadsSecret)
    
    
    public final UserWorkloadsSecret updateUserWorkloadsSecret(UserWorkloadsSecret userWorkloadsSecret)

Updates a user workloads Secret.

This method is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       UserWorkloadsSecret userWorkloadsSecret = UserWorkloadsSecret.newBuilder().build();
       UserWorkloadsSecret response =
           environmentsClient.updateUserWorkloadsSecret(userWorkloadsSecret);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`userWorkloadsSecret` | `[UserWorkloadsSecret](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.UserWorkloadsSecret)`  
Optional. User workloads Secret to override.  
**Returns**  
---  
**Type** | **Description**  
`[UserWorkloadsSecret](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.UserWorkloadsSecret)` |   
  
### updateUserWorkloadsSecretCallable()
    
    
    public final UnaryCallable<UpdateUserWorkloadsSecretRequest,UserWorkloadsSecret> updateUserWorkloadsSecretCallable()

Updates a user workloads Secret.

This method is supported for Cloud Composer environments in versions composer-3-airflow-*.*.*-build.* and newer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EnvironmentsClient environmentsClient = EnvironmentsClient.create()) {
       UpdateUserWorkloadsSecretRequest request =
           UpdateUserWorkloadsSecretRequest.newBuilder()
               .setUserWorkloadsSecret(UserWorkloadsSecret.newBuilder().build())
               .build();
       ApiFuture<UserWorkloadsSecret> future =
           environmentsClient.updateUserWorkloadsSecretCallable().futureCall(request);
       // Do something.
       UserWorkloadsSecret response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateUserWorkloadsSecretRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.UpdateUserWorkloadsSecretRequest),[UserWorkloadsSecret](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.UserWorkloadsSecret)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
