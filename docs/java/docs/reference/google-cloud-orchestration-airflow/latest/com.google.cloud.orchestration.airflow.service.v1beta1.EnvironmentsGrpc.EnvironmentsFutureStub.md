---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.EnvironmentsGrpc.EnvironmentsFutureStub
title: Class EnvironmentsGrpc.EnvironmentsFutureStub (1.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:37:05.041077+00:00
---

# Class EnvironmentsGrpc.EnvironmentsFutureStub (1.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.EnvironmentsGrpc.EnvironmentsFutureStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class EnvironmentsGrpc.EnvironmentsFutureStub (1.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.99.0 (latest)  1.95.0  1.94.0  1.93.0  1.91.0  1.88.0  1.87.0  1.85.0  1.83.0  1.82.0  1.80.0  1.78.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.70.0  1.68.0  1.67.0  1.64.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0 
    
    
    public static final class EnvironmentsGrpc.EnvironmentsFutureStub extends AbstractFutureStub<EnvironmentsGrpc.EnvironmentsFutureStub>

A stub to allow clients to do ListenableFuture-style rpc calls to service Environments.

Managed Apache Airflow Environments.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractFutureStub > EnvironmentsGrpc.EnvironmentsFutureStub

## Inherited Members

io.grpc.stub.AbstractFutureStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractFutureStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.<T>withOption(io.grpc.CallOptions.Key<T>,T)

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.getCallOptions()

io.grpc.stub.AbstractStub.getChannel()

io.grpc.stub.AbstractStub.withCallCredentials(io.grpc.CallCredentials)

io.grpc.stub.AbstractStub.withChannel(io.grpc.Channel)

io.grpc.stub.AbstractStub.withCompression(java.lang.String)

io.grpc.stub.AbstractStub.withDeadline(io.grpc.Deadline)

io.grpc.stub.AbstractStub.withDeadlineAfter(java.time.Duration)

io.grpc.stub.AbstractStub.withDeadlineAfter(long,java.util.concurrent.TimeUnit)

io.grpc.stub.AbstractStub.withExecutor(java.util.concurrent.Executor)

io.grpc.stub.AbstractStub.withInterceptors(io.grpc.ClientInterceptor...)

io.grpc.stub.AbstractStub.withMaxInboundMessageSize(int)

io.grpc.stub.AbstractStub.withMaxOutboundMessageSize(int)

io.grpc.stub.AbstractStub.withOnReadyThreshold(int)

io.grpc.stub.AbstractStub.withWaitForReady()

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

## Methods 

### build(Channel channel, CallOptions callOptions)
    
    
    protected EnvironmentsGrpc.EnvironmentsFutureStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[EnvironmentsGrpc.EnvironmentsFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.EnvironmentsGrpc.EnvironmentsFutureStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### checkUpgrade(CheckUpgradeRequest request)
    
    
    public ListenableFuture<Operation> checkUpgrade(CheckUpgradeRequest request)

Check if an upgrade operation on the environment will succeed. In case of problems detailed info can be found in the returned Operation.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CheckUpgradeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.CheckUpgradeRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createEnvironment(CreateEnvironmentRequest request)
    
    
    public ListenableFuture<Operation> createEnvironment(CreateEnvironmentRequest request)

Create a new environment.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateEnvironmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.CreateEnvironmentRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createUserWorkloadsConfigMap(CreateUserWorkloadsConfigMapRequest request)
    
    
    public ListenableFuture<UserWorkloadsConfigMap> createUserWorkloadsConfigMap(CreateUserWorkloadsConfigMapRequest request)

Creates a user workloads ConfigMap. This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateUserWorkloadsConfigMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.CreateUserWorkloadsConfigMapRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[UserWorkloadsConfigMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.UserWorkloadsConfigMap)>` |   
  
### createUserWorkloadsSecret(CreateUserWorkloadsSecretRequest request)
    
    
    public ListenableFuture<UserWorkloadsSecret> createUserWorkloadsSecret(CreateUserWorkloadsSecretRequest request)

Creates a user workloads Secret. This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateUserWorkloadsSecretRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.CreateUserWorkloadsSecretRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[UserWorkloadsSecret](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.UserWorkloadsSecret)>` |   
  
### databaseFailover(DatabaseFailoverRequest request)
    
    
    public ListenableFuture<Operation> databaseFailover(DatabaseFailoverRequest request)

Triggers database failover (only for highly resilient environments).

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DatabaseFailoverRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.DatabaseFailoverRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteEnvironment(DeleteEnvironmentRequest request)
    
    
    public ListenableFuture<Operation> deleteEnvironment(DeleteEnvironmentRequest request)

Delete an environment.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteEnvironmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.DeleteEnvironmentRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteUserWorkloadsConfigMap(DeleteUserWorkloadsConfigMapRequest request)
    
    
    public ListenableFuture<Empty> deleteUserWorkloadsConfigMap(DeleteUserWorkloadsConfigMapRequest request)

Deletes a user workloads ConfigMap. This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteUserWorkloadsConfigMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.DeleteUserWorkloadsConfigMapRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteUserWorkloadsSecret(DeleteUserWorkloadsSecretRequest request)
    
    
    public ListenableFuture<Empty> deleteUserWorkloadsSecret(DeleteUserWorkloadsSecretRequest request)

Deletes a user workloads Secret. This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteUserWorkloadsSecretRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.DeleteUserWorkloadsSecretRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### executeAirflowCommand(ExecuteAirflowCommandRequest request)
    
    
    public ListenableFuture<ExecuteAirflowCommandResponse> executeAirflowCommand(ExecuteAirflowCommandRequest request)

Executes Airflow CLI command.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ExecuteAirflowCommandRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.ExecuteAirflowCommandRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ExecuteAirflowCommandResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.ExecuteAirflowCommandResponse)>` |   
  
### fetchDatabaseProperties(FetchDatabasePropertiesRequest request)
    
    
    public ListenableFuture<FetchDatabasePropertiesResponse> fetchDatabaseProperties(FetchDatabasePropertiesRequest request)

Fetches database properties.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FetchDatabasePropertiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.FetchDatabasePropertiesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[FetchDatabasePropertiesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.FetchDatabasePropertiesResponse)>` |   
  
### getEnvironment(GetEnvironmentRequest request)
    
    
    public ListenableFuture<Environment> getEnvironment(GetEnvironmentRequest request)

Get an existing environment.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetEnvironmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.GetEnvironmentRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Environment](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.Environment)>` |   
  
### getUserWorkloadsConfigMap(GetUserWorkloadsConfigMapRequest request)
    
    
    public ListenableFuture<UserWorkloadsConfigMap> getUserWorkloadsConfigMap(GetUserWorkloadsConfigMapRequest request)

Gets an existing user workloads ConfigMap. This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetUserWorkloadsConfigMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.GetUserWorkloadsConfigMapRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[UserWorkloadsConfigMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.UserWorkloadsConfigMap)>` |   
  
### getUserWorkloadsSecret(GetUserWorkloadsSecretRequest request)
    
    
    public ListenableFuture<UserWorkloadsSecret> getUserWorkloadsSecret(GetUserWorkloadsSecretRequest request)

Gets an existing user workloads Secret. Values of the "data" field in the response are cleared. This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetUserWorkloadsSecretRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.GetUserWorkloadsSecretRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[UserWorkloadsSecret](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.UserWorkloadsSecret)>` |   
  
### listEnvironments(ListEnvironmentsRequest request)
    
    
    public ListenableFuture<ListEnvironmentsResponse> listEnvironments(ListEnvironmentsRequest request)

List environments.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListEnvironmentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.ListEnvironmentsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListEnvironmentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.ListEnvironmentsResponse)>` |   
  
### listUserWorkloadsConfigMaps(ListUserWorkloadsConfigMapsRequest request)
    
    
    public ListenableFuture<ListUserWorkloadsConfigMapsResponse> listUserWorkloadsConfigMaps(ListUserWorkloadsConfigMapsRequest request)

Lists user workloads ConfigMaps. This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListUserWorkloadsConfigMapsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.ListUserWorkloadsConfigMapsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListUserWorkloadsConfigMapsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.ListUserWorkloadsConfigMapsResponse)>` |   
  
### listUserWorkloadsSecrets(ListUserWorkloadsSecretsRequest request)
    
    
    public ListenableFuture<ListUserWorkloadsSecretsResponse> listUserWorkloadsSecrets(ListUserWorkloadsSecretsRequest request)

Lists user workloads Secrets. This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListUserWorkloadsSecretsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.ListUserWorkloadsSecretsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListUserWorkloadsSecretsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.ListUserWorkloadsSecretsResponse)>` |   
  
### listWorkloads(ListWorkloadsRequest request)
    
    
    public ListenableFuture<ListWorkloadsResponse> listWorkloads(ListWorkloadsRequest request)

Lists workloads in a Cloud Composer environment. Workload is a unit that runs a single Composer component. This method is supported for Cloud Composer environments in versions composer-2._._ -airflow-_._.* and newer.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListWorkloadsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.ListWorkloadsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListWorkloadsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.ListWorkloadsResponse)>` |   
  
### loadSnapshot(LoadSnapshotRequest request)
    
    
    public ListenableFuture<Operation> loadSnapshot(LoadSnapshotRequest request)

Loads a snapshot of a Cloud Composer environment. As a result of this operation, a snapshot of environment's specified in LoadSnapshotRequest is loaded into the environment.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[LoadSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.LoadSnapshotRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### pollAirflowCommand(PollAirflowCommandRequest request)
    
    
    public ListenableFuture<PollAirflowCommandResponse> pollAirflowCommand(PollAirflowCommandRequest request)

Polls Airflow CLI command execution and fetches logs.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PollAirflowCommandRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.PollAirflowCommandRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[PollAirflowCommandResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.PollAirflowCommandResponse)>` |   
  
### restartWebServer(RestartWebServerRequest request)
    
    
    public ListenableFuture<Operation> restartWebServer(RestartWebServerRequest request)

Restart Airflow web server.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RestartWebServerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.RestartWebServerRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### saveSnapshot(SaveSnapshotRequest request)
    
    
    public ListenableFuture<Operation> saveSnapshot(SaveSnapshotRequest request)

Creates a snapshots of a Cloud Composer environment. As a result of this operation, snapshot of environment's state is stored in a location specified in the SaveSnapshotRequest.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SaveSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.SaveSnapshotRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### stopAirflowCommand(StopAirflowCommandRequest request)
    
    
    public ListenableFuture<StopAirflowCommandResponse> stopAirflowCommand(StopAirflowCommandRequest request)

Stops Airflow CLI command execution.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[StopAirflowCommandRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.StopAirflowCommandRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[StopAirflowCommandResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.StopAirflowCommandResponse)>` |   
  
### updateEnvironment(UpdateEnvironmentRequest request)
    
    
    public ListenableFuture<Operation> updateEnvironment(UpdateEnvironmentRequest request)

Update an environment.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateEnvironmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.UpdateEnvironmentRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateUserWorkloadsConfigMap(UpdateUserWorkloadsConfigMapRequest request)
    
    
    public ListenableFuture<UserWorkloadsConfigMap> updateUserWorkloadsConfigMap(UpdateUserWorkloadsConfigMapRequest request)

Updates a user workloads ConfigMap. This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateUserWorkloadsConfigMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.UpdateUserWorkloadsConfigMapRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[UserWorkloadsConfigMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.UserWorkloadsConfigMap)>` |   
  
### updateUserWorkloadsSecret(UpdateUserWorkloadsSecretRequest request)
    
    
    public ListenableFuture<UserWorkloadsSecret> updateUserWorkloadsSecret(UpdateUserWorkloadsSecretRequest request)

Updates a user workloads Secret. This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateUserWorkloadsSecretRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.UpdateUserWorkloadsSecretRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[UserWorkloadsSecret](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.UserWorkloadsSecret)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
