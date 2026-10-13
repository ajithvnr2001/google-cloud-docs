---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.OracleDatabase.OracleDatabaseClient
title: Oracle Database@Google Cloud v1 API - Class OracleDatabase.OracleDatabaseClient (1.8.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:33:49.918576+00:00
---

# Oracle Database@Google Cloud v1 API - Class OracleDatabase.OracleDatabaseClient (1.8.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.OracleDatabase.OracleDatabaseClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Oracle Database@Google Cloud v1 API - Class OracleDatabase.OracleDatabaseClient (1.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.0 (latest)  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public class OracleDatabase.OracleDatabaseClient : ClientBase<OracleDatabase.OracleDatabaseClient>

Reference documentation and code samples for the Oracle Database@Google Cloud v1 API class OracleDatabase.OracleDatabaseClient.

Client for OracleDatabase

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html)[OracleDatabase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.OracleDatabase)[OracleDatabaseClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.OracleDatabase.OracleDatabaseClient) > OracleDatabase.OracleDatabaseClient

## Inherited Members

[ClientBase<OracleDatabase.OracleDatabaseClient>.WithHost(string)](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html#Grpc_Core_ClientBase_1_WithHost_System_String_)

[ClientBase.CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html#Grpc_Core_ClientBase_CallInvoker)

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.OracleDatabase.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1)

## Assembly

Google.Cloud.OracleDatabase.V1.dll

## Constructors 

### OracleDatabaseClient()
    
    
    protected OracleDatabaseClient()

Protected parameterless constructor to allow creation of test doubles.

### OracleDatabaseClient(CallInvoker)
    
    
    public OracleDatabaseClient(CallInvoker callInvoker)

Creates a new client for OracleDatabase that uses a custom `CallInvoker`.

**Parameter**  
---  
**Name** | **Description**  
`callInvoker` | `[CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallInvoker.html)`  
The callInvoker to use to make remote calls.  
  
### OracleDatabaseClient(ChannelBase)
    
    
    public OracleDatabaseClient(ChannelBase channel)

Creates a new client for OracleDatabase

**Parameter**  
---  
**Name** | **Description**  
`channel` | `[ChannelBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ChannelBase.html)`  
The channel to use to make remote calls.  
  
### OracleDatabaseClient(ClientBaseConfiguration)
    
    
    protected OracleDatabaseClient(ClientBase.ClientBaseConfiguration configuration)

Protected constructor to allow creation of configured clients.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
The client configuration.  
  
## Methods 

### ConfigureExascaleCloudExadataInfrastructure(ConfigureExascaleCloudExadataInfrastructureRequest, CallOptions)
    
    
    public virtual Operation ConfigureExascaleCloudExadataInfrastructure(ConfigureExascaleCloudExadataInfrastructureRequest request, CallOptions options)

Configures Exascale for a single Exadata Infrastructure.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ConfigureExascaleCloudExadataInfrastructureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ConfigureExascaleCloudExadataInfrastructureRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### ConfigureExascaleCloudExadataInfrastructure(ConfigureExascaleCloudExadataInfrastructureRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation ConfigureExascaleCloudExadataInfrastructure(ConfigureExascaleCloudExadataInfrastructureRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Configures Exascale for a single Exadata Infrastructure.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ConfigureExascaleCloudExadataInfrastructureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ConfigureExascaleCloudExadataInfrastructureRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### ConfigureExascaleCloudExadataInfrastructureAsync(ConfigureExascaleCloudExadataInfrastructureRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> ConfigureExascaleCloudExadataInfrastructureAsync(ConfigureExascaleCloudExadataInfrastructureRequest request, CallOptions options)

Configures Exascale for a single Exadata Infrastructure.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ConfigureExascaleCloudExadataInfrastructureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ConfigureExascaleCloudExadataInfrastructureRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### ConfigureExascaleCloudExadataInfrastructureAsync(ConfigureExascaleCloudExadataInfrastructureRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> ConfigureExascaleCloudExadataInfrastructureAsync(ConfigureExascaleCloudExadataInfrastructureRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Configures Exascale for a single Exadata Infrastructure.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ConfigureExascaleCloudExadataInfrastructureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ConfigureExascaleCloudExadataInfrastructureRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateAutonomousDatabase(CreateAutonomousDatabaseRequest, CallOptions)
    
    
    public virtual Operation CreateAutonomousDatabase(CreateAutonomousDatabaseRequest request, CallOptions options)

Creates a new Autonomous Database in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAutonomousDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CreateAutonomousDatabaseRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateAutonomousDatabase(CreateAutonomousDatabaseRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation CreateAutonomousDatabase(CreateAutonomousDatabaseRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new Autonomous Database in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAutonomousDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CreateAutonomousDatabaseRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateAutonomousDatabaseAsync(CreateAutonomousDatabaseRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> CreateAutonomousDatabaseAsync(CreateAutonomousDatabaseRequest request, CallOptions options)

Creates a new Autonomous Database in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAutonomousDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CreateAutonomousDatabaseRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateAutonomousDatabaseAsync(CreateAutonomousDatabaseRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> CreateAutonomousDatabaseAsync(CreateAutonomousDatabaseRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new Autonomous Database in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAutonomousDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CreateAutonomousDatabaseRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateCloudExadataInfrastructure(CreateCloudExadataInfrastructureRequest, CallOptions)
    
    
    public virtual Operation CreateCloudExadataInfrastructure(CreateCloudExadataInfrastructureRequest request, CallOptions options)

Creates a new Exadata Infrastructure in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateCloudExadataInfrastructureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CreateCloudExadataInfrastructureRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateCloudExadataInfrastructure(CreateCloudExadataInfrastructureRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation CreateCloudExadataInfrastructure(CreateCloudExadataInfrastructureRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new Exadata Infrastructure in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateCloudExadataInfrastructureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CreateCloudExadataInfrastructureRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateCloudExadataInfrastructureAsync(CreateCloudExadataInfrastructureRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> CreateCloudExadataInfrastructureAsync(CreateCloudExadataInfrastructureRequest request, CallOptions options)

Creates a new Exadata Infrastructure in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateCloudExadataInfrastructureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CreateCloudExadataInfrastructureRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateCloudExadataInfrastructureAsync(CreateCloudExadataInfrastructureRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> CreateCloudExadataInfrastructureAsync(CreateCloudExadataInfrastructureRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new Exadata Infrastructure in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateCloudExadataInfrastructureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CreateCloudExadataInfrastructureRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateCloudVmCluster(CreateCloudVmClusterRequest, CallOptions)
    
    
    public virtual Operation CreateCloudVmCluster(CreateCloudVmClusterRequest request, CallOptions options)

Creates a new VM Cluster in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateCloudVmClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CreateCloudVmClusterRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateCloudVmCluster(CreateCloudVmClusterRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation CreateCloudVmCluster(CreateCloudVmClusterRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new VM Cluster in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateCloudVmClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CreateCloudVmClusterRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateCloudVmClusterAsync(CreateCloudVmClusterRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> CreateCloudVmClusterAsync(CreateCloudVmClusterRequest request, CallOptions options)

Creates a new VM Cluster in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateCloudVmClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CreateCloudVmClusterRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateCloudVmClusterAsync(CreateCloudVmClusterRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> CreateCloudVmClusterAsync(CreateCloudVmClusterRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new VM Cluster in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateCloudVmClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CreateCloudVmClusterRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateDbSystem(CreateDbSystemRequest, CallOptions)
    
    
    public virtual Operation CreateDbSystem(CreateDbSystemRequest request, CallOptions options)

Creates a new DbSystem in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDbSystemRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CreateDbSystemRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateDbSystem(CreateDbSystemRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation CreateDbSystem(CreateDbSystemRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new DbSystem in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDbSystemRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CreateDbSystemRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateDbSystemAsync(CreateDbSystemRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> CreateDbSystemAsync(CreateDbSystemRequest request, CallOptions options)

Creates a new DbSystem in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDbSystemRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CreateDbSystemRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateDbSystemAsync(CreateDbSystemRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> CreateDbSystemAsync(CreateDbSystemRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new DbSystem in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDbSystemRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CreateDbSystemRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateExadbVmCluster(CreateExadbVmClusterRequest, CallOptions)
    
    
    public virtual Operation CreateExadbVmCluster(CreateExadbVmClusterRequest request, CallOptions options)

Creates a new Exadb (Exascale) VM Cluster resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateExadbVmClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CreateExadbVmClusterRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateExadbVmCluster(CreateExadbVmClusterRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation CreateExadbVmCluster(CreateExadbVmClusterRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new Exadb (Exascale) VM Cluster resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateExadbVmClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CreateExadbVmClusterRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateExadbVmClusterAsync(CreateExadbVmClusterRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> CreateExadbVmClusterAsync(CreateExadbVmClusterRequest request, CallOptions options)

Creates a new Exadb (Exascale) VM Cluster resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateExadbVmClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CreateExadbVmClusterRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateExadbVmClusterAsync(CreateExadbVmClusterRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> CreateExadbVmClusterAsync(CreateExadbVmClusterRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new Exadb (Exascale) VM Cluster resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateExadbVmClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CreateExadbVmClusterRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateExascaleDbStorageVault(CreateExascaleDbStorageVaultRequest, CallOptions)
    
    
    public virtual Operation CreateExascaleDbStorageVault(CreateExascaleDbStorageVaultRequest request, CallOptions options)

Creates a new ExascaleDB Storage Vault resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateExascaleDbStorageVaultRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CreateExascaleDbStorageVaultRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateExascaleDbStorageVault(CreateExascaleDbStorageVaultRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation CreateExascaleDbStorageVault(CreateExascaleDbStorageVaultRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new ExascaleDB Storage Vault resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateExascaleDbStorageVaultRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CreateExascaleDbStorageVaultRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateExascaleDbStorageVaultAsync(CreateExascaleDbStorageVaultRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> CreateExascaleDbStorageVaultAsync(CreateExascaleDbStorageVaultRequest request, CallOptions options)

Creates a new ExascaleDB Storage Vault resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateExascaleDbStorageVaultRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CreateExascaleDbStorageVaultRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateExascaleDbStorageVaultAsync(CreateExascaleDbStorageVaultRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> CreateExascaleDbStorageVaultAsync(CreateExascaleDbStorageVaultRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new ExascaleDB Storage Vault resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateExascaleDbStorageVaultRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CreateExascaleDbStorageVaultRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateGoldengateConnection(CreateGoldengateConnectionRequest, CallOptions)
    
    
    public virtual Operation CreateGoldengateConnection(CreateGoldengateConnectionRequest request, CallOptions options)

Creates a new GoldengateConnection in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateGoldengateConnectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CreateGoldengateConnectionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateGoldengateConnection(CreateGoldengateConnectionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation CreateGoldengateConnection(CreateGoldengateConnectionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new GoldengateConnection in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateGoldengateConnectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CreateGoldengateConnectionRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateGoldengateConnectionAssignment(CreateGoldengateConnectionAssignmentRequest, CallOptions)
    
    
    public virtual Operation CreateGoldengateConnectionAssignment(CreateGoldengateConnectionAssignmentRequest request, CallOptions options)

Creates a new GoldengateConnectionAssignment in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateGoldengateConnectionAssignmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CreateGoldengateConnectionAssignmentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateGoldengateConnectionAssignment(CreateGoldengateConnectionAssignmentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation CreateGoldengateConnectionAssignment(CreateGoldengateConnectionAssignmentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new GoldengateConnectionAssignment in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateGoldengateConnectionAssignmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CreateGoldengateConnectionAssignmentRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateGoldengateConnectionAssignmentAsync(CreateGoldengateConnectionAssignmentRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> CreateGoldengateConnectionAssignmentAsync(CreateGoldengateConnectionAssignmentRequest request, CallOptions options)

Creates a new GoldengateConnectionAssignment in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateGoldengateConnectionAssignmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CreateGoldengateConnectionAssignmentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateGoldengateConnectionAssignmentAsync(CreateGoldengateConnectionAssignmentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> CreateGoldengateConnectionAssignmentAsync(CreateGoldengateConnectionAssignmentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new GoldengateConnectionAssignment in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateGoldengateConnectionAssignmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CreateGoldengateConnectionAssignmentRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateGoldengateConnectionAsync(CreateGoldengateConnectionRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> CreateGoldengateConnectionAsync(CreateGoldengateConnectionRequest request, CallOptions options)

Creates a new GoldengateConnection in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateGoldengateConnectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CreateGoldengateConnectionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateGoldengateConnectionAsync(CreateGoldengateConnectionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> CreateGoldengateConnectionAsync(CreateGoldengateConnectionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new GoldengateConnection in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateGoldengateConnectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CreateGoldengateConnectionRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateGoldengateDeployment(CreateGoldengateDeploymentRequest, CallOptions)
    
    
    public virtual Operation CreateGoldengateDeployment(CreateGoldengateDeploymentRequest request, CallOptions options)

Creates a new GoldengateDeployment in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateGoldengateDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CreateGoldengateDeploymentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateGoldengateDeployment(CreateGoldengateDeploymentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation CreateGoldengateDeployment(CreateGoldengateDeploymentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new GoldengateDeployment in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateGoldengateDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CreateGoldengateDeploymentRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateGoldengateDeploymentAsync(CreateGoldengateDeploymentRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> CreateGoldengateDeploymentAsync(CreateGoldengateDeploymentRequest request, CallOptions options)

Creates a new GoldengateDeployment in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateGoldengateDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CreateGoldengateDeploymentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateGoldengateDeploymentAsync(CreateGoldengateDeploymentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> CreateGoldengateDeploymentAsync(CreateGoldengateDeploymentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new GoldengateDeployment in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateGoldengateDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CreateGoldengateDeploymentRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateLocationsClient()
    
    
    public virtual Locations.LocationsClient CreateLocationsClient()

Creates a new instance of [Locations.LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.Locations.LocationsClient.html) using the same call invoker as this client.

**Returns**  
---  
**Type** | **Description**  
`[Locations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.Locations.html)[LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.Locations.LocationsClient.html)` | A new [Locations.LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.Locations.LocationsClient.html) for the same target as this client.  
  
### CreateOdbNetwork(CreateOdbNetworkRequest, CallOptions)
    
    
    public virtual Operation CreateOdbNetwork(CreateOdbNetworkRequest request, CallOptions options)

Creates a new ODB Network in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateOdbNetworkRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CreateOdbNetworkRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateOdbNetwork(CreateOdbNetworkRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation CreateOdbNetwork(CreateOdbNetworkRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new ODB Network in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateOdbNetworkRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CreateOdbNetworkRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateOdbNetworkAsync(CreateOdbNetworkRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> CreateOdbNetworkAsync(CreateOdbNetworkRequest request, CallOptions options)

Creates a new ODB Network in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateOdbNetworkRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CreateOdbNetworkRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateOdbNetworkAsync(CreateOdbNetworkRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> CreateOdbNetworkAsync(CreateOdbNetworkRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new ODB Network in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateOdbNetworkRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CreateOdbNetworkRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateOdbSubnet(CreateOdbSubnetRequest, CallOptions)
    
    
    public virtual Operation CreateOdbSubnet(CreateOdbSubnetRequest request, CallOptions options)

Creates a new ODB Subnet in a given ODB Network.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateOdbSubnetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CreateOdbSubnetRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateOdbSubnet(CreateOdbSubnetRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation CreateOdbSubnet(CreateOdbSubnetRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new ODB Subnet in a given ODB Network.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateOdbSubnetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CreateOdbSubnetRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateOdbSubnetAsync(CreateOdbSubnetRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> CreateOdbSubnetAsync(CreateOdbSubnetRequest request, CallOptions options)

Creates a new ODB Subnet in a given ODB Network.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateOdbSubnetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CreateOdbSubnetRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateOdbSubnetAsync(CreateOdbSubnetRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> CreateOdbSubnetAsync(CreateOdbSubnetRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new ODB Subnet in a given ODB Network.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateOdbSubnetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CreateOdbSubnetRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateOperationsClient()
    
    
    public virtual Operations.OperationsClient CreateOperationsClient()

Creates a new instance of [Operations.OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operations.OperationsClient.html) using the same call invoker as this client.

**Returns**  
---  
**Type** | **Description**  
`[Operations](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operations.html)[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operations.OperationsClient.html)` | A new Operations client for the same target as this client.  
  
### DeleteAutonomousDatabase(DeleteAutonomousDatabaseRequest, CallOptions)
    
    
    public virtual Operation DeleteAutonomousDatabase(DeleteAutonomousDatabaseRequest request, CallOptions options)

Deletes a single Autonomous Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAutonomousDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DeleteAutonomousDatabaseRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteAutonomousDatabase(DeleteAutonomousDatabaseRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeleteAutonomousDatabase(DeleteAutonomousDatabaseRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single Autonomous Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAutonomousDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DeleteAutonomousDatabaseRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteAutonomousDatabaseAsync(DeleteAutonomousDatabaseRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteAutonomousDatabaseAsync(DeleteAutonomousDatabaseRequest request, CallOptions options)

Deletes a single Autonomous Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAutonomousDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DeleteAutonomousDatabaseRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteAutonomousDatabaseAsync(DeleteAutonomousDatabaseRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteAutonomousDatabaseAsync(DeleteAutonomousDatabaseRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single Autonomous Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAutonomousDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DeleteAutonomousDatabaseRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteCloudExadataInfrastructure(DeleteCloudExadataInfrastructureRequest, CallOptions)
    
    
    public virtual Operation DeleteCloudExadataInfrastructure(DeleteCloudExadataInfrastructureRequest request, CallOptions options)

Deletes a single Exadata Infrastructure.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteCloudExadataInfrastructureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DeleteCloudExadataInfrastructureRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteCloudExadataInfrastructure(DeleteCloudExadataInfrastructureRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeleteCloudExadataInfrastructure(DeleteCloudExadataInfrastructureRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single Exadata Infrastructure.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteCloudExadataInfrastructureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DeleteCloudExadataInfrastructureRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteCloudExadataInfrastructureAsync(DeleteCloudExadataInfrastructureRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteCloudExadataInfrastructureAsync(DeleteCloudExadataInfrastructureRequest request, CallOptions options)

Deletes a single Exadata Infrastructure.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteCloudExadataInfrastructureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DeleteCloudExadataInfrastructureRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteCloudExadataInfrastructureAsync(DeleteCloudExadataInfrastructureRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteCloudExadataInfrastructureAsync(DeleteCloudExadataInfrastructureRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single Exadata Infrastructure.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteCloudExadataInfrastructureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DeleteCloudExadataInfrastructureRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteCloudVmCluster(DeleteCloudVmClusterRequest, CallOptions)
    
    
    public virtual Operation DeleteCloudVmCluster(DeleteCloudVmClusterRequest request, CallOptions options)

Deletes a single VM Cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteCloudVmClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DeleteCloudVmClusterRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteCloudVmCluster(DeleteCloudVmClusterRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeleteCloudVmCluster(DeleteCloudVmClusterRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single VM Cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteCloudVmClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DeleteCloudVmClusterRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteCloudVmClusterAsync(DeleteCloudVmClusterRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteCloudVmClusterAsync(DeleteCloudVmClusterRequest request, CallOptions options)

Deletes a single VM Cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteCloudVmClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DeleteCloudVmClusterRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteCloudVmClusterAsync(DeleteCloudVmClusterRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteCloudVmClusterAsync(DeleteCloudVmClusterRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single VM Cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteCloudVmClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DeleteCloudVmClusterRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteDbSystem(DeleteDbSystemRequest, CallOptions)
    
    
    public virtual Operation DeleteDbSystem(DeleteDbSystemRequest request, CallOptions options)

Deletes a single DbSystem.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDbSystemRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DeleteDbSystemRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteDbSystem(DeleteDbSystemRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeleteDbSystem(DeleteDbSystemRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single DbSystem.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDbSystemRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DeleteDbSystemRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteDbSystemAsync(DeleteDbSystemRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteDbSystemAsync(DeleteDbSystemRequest request, CallOptions options)

Deletes a single DbSystem.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDbSystemRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DeleteDbSystemRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteDbSystemAsync(DeleteDbSystemRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteDbSystemAsync(DeleteDbSystemRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single DbSystem.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDbSystemRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DeleteDbSystemRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteExadbVmCluster(DeleteExadbVmClusterRequest, CallOptions)
    
    
    public virtual Operation DeleteExadbVmCluster(DeleteExadbVmClusterRequest request, CallOptions options)

Deletes a single Exadb (Exascale) VM Cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteExadbVmClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DeleteExadbVmClusterRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteExadbVmCluster(DeleteExadbVmClusterRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeleteExadbVmCluster(DeleteExadbVmClusterRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single Exadb (Exascale) VM Cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteExadbVmClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DeleteExadbVmClusterRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteExadbVmClusterAsync(DeleteExadbVmClusterRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteExadbVmClusterAsync(DeleteExadbVmClusterRequest request, CallOptions options)

Deletes a single Exadb (Exascale) VM Cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteExadbVmClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DeleteExadbVmClusterRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteExadbVmClusterAsync(DeleteExadbVmClusterRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteExadbVmClusterAsync(DeleteExadbVmClusterRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single Exadb (Exascale) VM Cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteExadbVmClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DeleteExadbVmClusterRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteExascaleDbStorageVault(DeleteExascaleDbStorageVaultRequest, CallOptions)
    
    
    public virtual Operation DeleteExascaleDbStorageVault(DeleteExascaleDbStorageVaultRequest request, CallOptions options)

Deletes a single ExascaleDB Storage Vault.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteExascaleDbStorageVaultRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DeleteExascaleDbStorageVaultRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteExascaleDbStorageVault(DeleteExascaleDbStorageVaultRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeleteExascaleDbStorageVault(DeleteExascaleDbStorageVaultRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single ExascaleDB Storage Vault.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteExascaleDbStorageVaultRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DeleteExascaleDbStorageVaultRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteExascaleDbStorageVaultAsync(DeleteExascaleDbStorageVaultRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteExascaleDbStorageVaultAsync(DeleteExascaleDbStorageVaultRequest request, CallOptions options)

Deletes a single ExascaleDB Storage Vault.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteExascaleDbStorageVaultRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DeleteExascaleDbStorageVaultRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteExascaleDbStorageVaultAsync(DeleteExascaleDbStorageVaultRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteExascaleDbStorageVaultAsync(DeleteExascaleDbStorageVaultRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single ExascaleDB Storage Vault.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteExascaleDbStorageVaultRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DeleteExascaleDbStorageVaultRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteGoldengateConnection(DeleteGoldengateConnectionRequest, CallOptions)
    
    
    public virtual Operation DeleteGoldengateConnection(DeleteGoldengateConnectionRequest request, CallOptions options)

Deletes a single GoldengateConnection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteGoldengateConnectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DeleteGoldengateConnectionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteGoldengateConnection(DeleteGoldengateConnectionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeleteGoldengateConnection(DeleteGoldengateConnectionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single GoldengateConnection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteGoldengateConnectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DeleteGoldengateConnectionRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteGoldengateConnectionAssignment(DeleteGoldengateConnectionAssignmentRequest, CallOptions)
    
    
    public virtual Operation DeleteGoldengateConnectionAssignment(DeleteGoldengateConnectionAssignmentRequest request, CallOptions options)

Deletes a single GoldengateConnectionAssignment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteGoldengateConnectionAssignmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DeleteGoldengateConnectionAssignmentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteGoldengateConnectionAssignment(DeleteGoldengateConnectionAssignmentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeleteGoldengateConnectionAssignment(DeleteGoldengateConnectionAssignmentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single GoldengateConnectionAssignment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteGoldengateConnectionAssignmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DeleteGoldengateConnectionAssignmentRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteGoldengateConnectionAssignmentAsync(DeleteGoldengateConnectionAssignmentRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteGoldengateConnectionAssignmentAsync(DeleteGoldengateConnectionAssignmentRequest request, CallOptions options)

Deletes a single GoldengateConnectionAssignment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteGoldengateConnectionAssignmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DeleteGoldengateConnectionAssignmentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteGoldengateConnectionAssignmentAsync(DeleteGoldengateConnectionAssignmentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteGoldengateConnectionAssignmentAsync(DeleteGoldengateConnectionAssignmentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single GoldengateConnectionAssignment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteGoldengateConnectionAssignmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DeleteGoldengateConnectionAssignmentRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteGoldengateConnectionAsync(DeleteGoldengateConnectionRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteGoldengateConnectionAsync(DeleteGoldengateConnectionRequest request, CallOptions options)

Deletes a single GoldengateConnection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteGoldengateConnectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DeleteGoldengateConnectionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteGoldengateConnectionAsync(DeleteGoldengateConnectionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteGoldengateConnectionAsync(DeleteGoldengateConnectionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single GoldengateConnection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteGoldengateConnectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DeleteGoldengateConnectionRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteGoldengateDeployment(DeleteGoldengateDeploymentRequest, CallOptions)
    
    
    public virtual Operation DeleteGoldengateDeployment(DeleteGoldengateDeploymentRequest request, CallOptions options)

Deletes a single GoldengateDeployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteGoldengateDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DeleteGoldengateDeploymentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteGoldengateDeployment(DeleteGoldengateDeploymentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeleteGoldengateDeployment(DeleteGoldengateDeploymentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single GoldengateDeployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteGoldengateDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DeleteGoldengateDeploymentRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteGoldengateDeploymentAsync(DeleteGoldengateDeploymentRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteGoldengateDeploymentAsync(DeleteGoldengateDeploymentRequest request, CallOptions options)

Deletes a single GoldengateDeployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteGoldengateDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DeleteGoldengateDeploymentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteGoldengateDeploymentAsync(DeleteGoldengateDeploymentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteGoldengateDeploymentAsync(DeleteGoldengateDeploymentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single GoldengateDeployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteGoldengateDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DeleteGoldengateDeploymentRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteOdbNetwork(DeleteOdbNetworkRequest, CallOptions)
    
    
    public virtual Operation DeleteOdbNetwork(DeleteOdbNetworkRequest request, CallOptions options)

Deletes a single ODB Network.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteOdbNetworkRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DeleteOdbNetworkRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteOdbNetwork(DeleteOdbNetworkRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeleteOdbNetwork(DeleteOdbNetworkRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single ODB Network.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteOdbNetworkRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DeleteOdbNetworkRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteOdbNetworkAsync(DeleteOdbNetworkRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteOdbNetworkAsync(DeleteOdbNetworkRequest request, CallOptions options)

Deletes a single ODB Network.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteOdbNetworkRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DeleteOdbNetworkRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteOdbNetworkAsync(DeleteOdbNetworkRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteOdbNetworkAsync(DeleteOdbNetworkRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single ODB Network.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteOdbNetworkRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DeleteOdbNetworkRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteOdbSubnet(DeleteOdbSubnetRequest, CallOptions)
    
    
    public virtual Operation DeleteOdbSubnet(DeleteOdbSubnetRequest request, CallOptions options)

Deletes a single ODB Subnet.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteOdbSubnetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DeleteOdbSubnetRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteOdbSubnet(DeleteOdbSubnetRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeleteOdbSubnet(DeleteOdbSubnetRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single ODB Subnet.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteOdbSubnetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DeleteOdbSubnetRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteOdbSubnetAsync(DeleteOdbSubnetRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteOdbSubnetAsync(DeleteOdbSubnetRequest request, CallOptions options)

Deletes a single ODB Subnet.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteOdbSubnetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DeleteOdbSubnetRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteOdbSubnetAsync(DeleteOdbSubnetRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteOdbSubnetAsync(DeleteOdbSubnetRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single ODB Subnet.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteOdbSubnetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DeleteOdbSubnetRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### FailoverAutonomousDatabase(FailoverAutonomousDatabaseRequest, CallOptions)
    
    
    public virtual Operation FailoverAutonomousDatabase(FailoverAutonomousDatabaseRequest request, CallOptions options)

Initiates a failover to target autonomous database from the associated primary database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FailoverAutonomousDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.FailoverAutonomousDatabaseRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### FailoverAutonomousDatabase(FailoverAutonomousDatabaseRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation FailoverAutonomousDatabase(FailoverAutonomousDatabaseRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Initiates a failover to target autonomous database from the associated primary database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FailoverAutonomousDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.FailoverAutonomousDatabaseRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### FailoverAutonomousDatabaseAsync(FailoverAutonomousDatabaseRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> FailoverAutonomousDatabaseAsync(FailoverAutonomousDatabaseRequest request, CallOptions options)

Initiates a failover to target autonomous database from the associated primary database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FailoverAutonomousDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.FailoverAutonomousDatabaseRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### FailoverAutonomousDatabaseAsync(FailoverAutonomousDatabaseRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> FailoverAutonomousDatabaseAsync(FailoverAutonomousDatabaseRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Initiates a failover to target autonomous database from the associated primary database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FailoverAutonomousDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.FailoverAutonomousDatabaseRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### GenerateAutonomousDatabaseWallet(GenerateAutonomousDatabaseWalletRequest, CallOptions)
    
    
    public virtual GenerateAutonomousDatabaseWalletResponse GenerateAutonomousDatabaseWallet(GenerateAutonomousDatabaseWalletRequest request, CallOptions options)

Generates a wallet for an Autonomous Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateAutonomousDatabaseWalletRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GenerateAutonomousDatabaseWalletRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[GenerateAutonomousDatabaseWalletResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GenerateAutonomousDatabaseWalletResponse)` | The response received from the server.  
  
### GenerateAutonomousDatabaseWallet(GenerateAutonomousDatabaseWalletRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual GenerateAutonomousDatabaseWalletResponse GenerateAutonomousDatabaseWallet(GenerateAutonomousDatabaseWalletRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Generates a wallet for an Autonomous Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateAutonomousDatabaseWalletRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GenerateAutonomousDatabaseWalletRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[GenerateAutonomousDatabaseWalletResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GenerateAutonomousDatabaseWalletResponse)` | The response received from the server.  
  
### GenerateAutonomousDatabaseWalletAsync(GenerateAutonomousDatabaseWalletRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<GenerateAutonomousDatabaseWalletResponse> GenerateAutonomousDatabaseWalletAsync(GenerateAutonomousDatabaseWalletRequest request, CallOptions options)

Generates a wallet for an Autonomous Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateAutonomousDatabaseWalletRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GenerateAutonomousDatabaseWalletRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[GenerateAutonomousDatabaseWalletResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GenerateAutonomousDatabaseWalletResponse)` | The call object.  
  
### GenerateAutonomousDatabaseWalletAsync(GenerateAutonomousDatabaseWalletRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<GenerateAutonomousDatabaseWalletResponse> GenerateAutonomousDatabaseWalletAsync(GenerateAutonomousDatabaseWalletRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Generates a wallet for an Autonomous Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateAutonomousDatabaseWalletRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GenerateAutonomousDatabaseWalletRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[GenerateAutonomousDatabaseWalletResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GenerateAutonomousDatabaseWalletResponse)` | The call object.  
  
### GetAutonomousDatabase(GetAutonomousDatabaseRequest, CallOptions)
    
    
    public virtual AutonomousDatabase GetAutonomousDatabase(GetAutonomousDatabaseRequest request, CallOptions options)

Gets the details of a single Autonomous Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAutonomousDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetAutonomousDatabaseRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AutonomousDatabase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabase)` | The response received from the server.  
  
### GetAutonomousDatabase(GetAutonomousDatabaseRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AutonomousDatabase GetAutonomousDatabase(GetAutonomousDatabaseRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets the details of a single Autonomous Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAutonomousDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetAutonomousDatabaseRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AutonomousDatabase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabase)` | The response received from the server.  
  
### GetAutonomousDatabaseAsync(GetAutonomousDatabaseRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<AutonomousDatabase> GetAutonomousDatabaseAsync(GetAutonomousDatabaseRequest request, CallOptions options)

Gets the details of a single Autonomous Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAutonomousDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetAutonomousDatabaseRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[AutonomousDatabase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabase)` | The call object.  
  
### GetAutonomousDatabaseAsync(GetAutonomousDatabaseRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<AutonomousDatabase> GetAutonomousDatabaseAsync(GetAutonomousDatabaseRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets the details of a single Autonomous Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAutonomousDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetAutonomousDatabaseRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[AutonomousDatabase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabase)` | The call object.  
  
### GetAutonomousDatabaseRefreshableClones(GetAutonomousDatabaseRefreshableClonesRequest, CallOptions)
    
    
    public virtual AutonomousDatabaseRefreshableClones GetAutonomousDatabaseRefreshableClones(GetAutonomousDatabaseRefreshableClonesRequest request, CallOptions options)

Gets the refreshable clones for a given Autonomous Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAutonomousDatabaseRefreshableClonesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetAutonomousDatabaseRefreshableClonesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AutonomousDatabaseRefreshableClones](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseRefreshableClones)` | The response received from the server.  
  
### GetAutonomousDatabaseRefreshableClones(GetAutonomousDatabaseRefreshableClonesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AutonomousDatabaseRefreshableClones GetAutonomousDatabaseRefreshableClones(GetAutonomousDatabaseRefreshableClonesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets the refreshable clones for a given Autonomous Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAutonomousDatabaseRefreshableClonesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetAutonomousDatabaseRefreshableClonesRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AutonomousDatabaseRefreshableClones](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseRefreshableClones)` | The response received from the server.  
  
### GetAutonomousDatabaseRefreshableClonesAsync(GetAutonomousDatabaseRefreshableClonesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<AutonomousDatabaseRefreshableClones> GetAutonomousDatabaseRefreshableClonesAsync(GetAutonomousDatabaseRefreshableClonesRequest request, CallOptions options)

Gets the refreshable clones for a given Autonomous Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAutonomousDatabaseRefreshableClonesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetAutonomousDatabaseRefreshableClonesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[AutonomousDatabaseRefreshableClones](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseRefreshableClones)` | The call object.  
  
### GetAutonomousDatabaseRefreshableClonesAsync(GetAutonomousDatabaseRefreshableClonesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<AutonomousDatabaseRefreshableClones> GetAutonomousDatabaseRefreshableClonesAsync(GetAutonomousDatabaseRefreshableClonesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets the refreshable clones for a given Autonomous Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAutonomousDatabaseRefreshableClonesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetAutonomousDatabaseRefreshableClonesRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[AutonomousDatabaseRefreshableClones](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseRefreshableClones)` | The call object.  
  
### GetCloudExadataInfrastructure(GetCloudExadataInfrastructureRequest, CallOptions)
    
    
    public virtual CloudExadataInfrastructure GetCloudExadataInfrastructure(GetCloudExadataInfrastructureRequest request, CallOptions options)

Gets details of a single Exadata Infrastructure.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCloudExadataInfrastructureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetCloudExadataInfrastructureRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[CloudExadataInfrastructure](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CloudExadataInfrastructure)` | The response received from the server.  
  
### GetCloudExadataInfrastructure(GetCloudExadataInfrastructureRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual CloudExadataInfrastructure GetCloudExadataInfrastructure(GetCloudExadataInfrastructureRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single Exadata Infrastructure.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCloudExadataInfrastructureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetCloudExadataInfrastructureRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[CloudExadataInfrastructure](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CloudExadataInfrastructure)` | The response received from the server.  
  
### GetCloudExadataInfrastructureAsync(GetCloudExadataInfrastructureRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<CloudExadataInfrastructure> GetCloudExadataInfrastructureAsync(GetCloudExadataInfrastructureRequest request, CallOptions options)

Gets details of a single Exadata Infrastructure.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCloudExadataInfrastructureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetCloudExadataInfrastructureRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[CloudExadataInfrastructure](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CloudExadataInfrastructure)` | The call object.  
  
### GetCloudExadataInfrastructureAsync(GetCloudExadataInfrastructureRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<CloudExadataInfrastructure> GetCloudExadataInfrastructureAsync(GetCloudExadataInfrastructureRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single Exadata Infrastructure.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCloudExadataInfrastructureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetCloudExadataInfrastructureRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[CloudExadataInfrastructure](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CloudExadataInfrastructure)` | The call object.  
  
### GetCloudVmCluster(GetCloudVmClusterRequest, CallOptions)
    
    
    public virtual CloudVmCluster GetCloudVmCluster(GetCloudVmClusterRequest request, CallOptions options)

Gets details of a single VM Cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCloudVmClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetCloudVmClusterRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[CloudVmCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CloudVmCluster)` | The response received from the server.  
  
### GetCloudVmCluster(GetCloudVmClusterRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual CloudVmCluster GetCloudVmCluster(GetCloudVmClusterRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single VM Cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCloudVmClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetCloudVmClusterRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[CloudVmCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CloudVmCluster)` | The response received from the server.  
  
### GetCloudVmClusterAsync(GetCloudVmClusterRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<CloudVmCluster> GetCloudVmClusterAsync(GetCloudVmClusterRequest request, CallOptions options)

Gets details of a single VM Cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCloudVmClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetCloudVmClusterRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[CloudVmCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CloudVmCluster)` | The call object.  
  
### GetCloudVmClusterAsync(GetCloudVmClusterRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<CloudVmCluster> GetCloudVmClusterAsync(GetCloudVmClusterRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single VM Cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCloudVmClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetCloudVmClusterRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[CloudVmCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CloudVmCluster)` | The call object.  
  
### GetDatabase(GetDatabaseRequest, CallOptions)
    
    
    public virtual Database GetDatabase(GetDatabaseRequest request, CallOptions options)

Gets details of a single Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetDatabaseRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Database](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.Database)` | The response received from the server.  
  
### GetDatabase(GetDatabaseRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Database GetDatabase(GetDatabaseRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetDatabaseRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Database](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.Database)` | The response received from the server.  
  
### GetDatabaseAsync(GetDatabaseRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Database> GetDatabaseAsync(GetDatabaseRequest request, CallOptions options)

Gets details of a single Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetDatabaseRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Database](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.Database)` | The call object.  
  
### GetDatabaseAsync(GetDatabaseRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Database> GetDatabaseAsync(GetDatabaseRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetDatabaseRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Database](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.Database)` | The call object.  
  
### GetDbSystem(GetDbSystemRequest, CallOptions)
    
    
    public virtual DbSystem GetDbSystem(GetDbSystemRequest request, CallOptions options)

Gets details of a single DbSystem.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDbSystemRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetDbSystemRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[DbSystem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DbSystem)` | The response received from the server.  
  
### GetDbSystem(GetDbSystemRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual DbSystem GetDbSystem(GetDbSystemRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single DbSystem.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDbSystemRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetDbSystemRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[DbSystem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DbSystem)` | The response received from the server.  
  
### GetDbSystemAsync(GetDbSystemRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<DbSystem> GetDbSystemAsync(GetDbSystemRequest request, CallOptions options)

Gets details of a single DbSystem.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDbSystemRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetDbSystemRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[DbSystem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DbSystem)` | The call object.  
  
### GetDbSystemAsync(GetDbSystemRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<DbSystem> GetDbSystemAsync(GetDbSystemRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single DbSystem.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDbSystemRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetDbSystemRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[DbSystem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DbSystem)` | The call object.  
  
### GetExadbVmCluster(GetExadbVmClusterRequest, CallOptions)
    
    
    public virtual ExadbVmCluster GetExadbVmCluster(GetExadbVmClusterRequest request, CallOptions options)

Gets details of a single Exadb (Exascale) VM Cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetExadbVmClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetExadbVmClusterRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ExadbVmCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ExadbVmCluster)` | The response received from the server.  
  
### GetExadbVmCluster(GetExadbVmClusterRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ExadbVmCluster GetExadbVmCluster(GetExadbVmClusterRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single Exadb (Exascale) VM Cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetExadbVmClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetExadbVmClusterRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ExadbVmCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ExadbVmCluster)` | The response received from the server.  
  
### GetExadbVmClusterAsync(GetExadbVmClusterRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ExadbVmCluster> GetExadbVmClusterAsync(GetExadbVmClusterRequest request, CallOptions options)

Gets details of a single Exadb (Exascale) VM Cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetExadbVmClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetExadbVmClusterRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ExadbVmCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ExadbVmCluster)` | The call object.  
  
### GetExadbVmClusterAsync(GetExadbVmClusterRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ExadbVmCluster> GetExadbVmClusterAsync(GetExadbVmClusterRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single Exadb (Exascale) VM Cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetExadbVmClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetExadbVmClusterRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ExadbVmCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ExadbVmCluster)` | The call object.  
  
### GetExascaleDbStorageVault(GetExascaleDbStorageVaultRequest, CallOptions)
    
    
    public virtual ExascaleDbStorageVault GetExascaleDbStorageVault(GetExascaleDbStorageVaultRequest request, CallOptions options)

Gets details of a single ExascaleDB Storage Vault.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetExascaleDbStorageVaultRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetExascaleDbStorageVaultRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ExascaleDbStorageVault](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ExascaleDbStorageVault)` | The response received from the server.  
  
### GetExascaleDbStorageVault(GetExascaleDbStorageVaultRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ExascaleDbStorageVault GetExascaleDbStorageVault(GetExascaleDbStorageVaultRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single ExascaleDB Storage Vault.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetExascaleDbStorageVaultRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetExascaleDbStorageVaultRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ExascaleDbStorageVault](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ExascaleDbStorageVault)` | The response received from the server.  
  
### GetExascaleDbStorageVaultAsync(GetExascaleDbStorageVaultRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ExascaleDbStorageVault> GetExascaleDbStorageVaultAsync(GetExascaleDbStorageVaultRequest request, CallOptions options)

Gets details of a single ExascaleDB Storage Vault.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetExascaleDbStorageVaultRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetExascaleDbStorageVaultRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ExascaleDbStorageVault](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ExascaleDbStorageVault)` | The call object.  
  
### GetExascaleDbStorageVaultAsync(GetExascaleDbStorageVaultRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ExascaleDbStorageVault> GetExascaleDbStorageVaultAsync(GetExascaleDbStorageVaultRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single ExascaleDB Storage Vault.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetExascaleDbStorageVaultRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetExascaleDbStorageVaultRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ExascaleDbStorageVault](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ExascaleDbStorageVault)` | The call object.  
  
### GetGoldengateConnection(GetGoldengateConnectionRequest, CallOptions)
    
    
    public virtual GoldengateConnection GetGoldengateConnection(GetGoldengateConnectionRequest request, CallOptions options)

Gets details of a single GoldengateConnection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGoldengateConnectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetGoldengateConnectionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[GoldengateConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GoldengateConnection)` | The response received from the server.  
  
### GetGoldengateConnection(GetGoldengateConnectionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual GoldengateConnection GetGoldengateConnection(GetGoldengateConnectionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single GoldengateConnection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGoldengateConnectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetGoldengateConnectionRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[GoldengateConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GoldengateConnection)` | The response received from the server.  
  
### GetGoldengateConnectionAssignment(GetGoldengateConnectionAssignmentRequest, CallOptions)
    
    
    public virtual GoldengateConnectionAssignment GetGoldengateConnectionAssignment(GetGoldengateConnectionAssignmentRequest request, CallOptions options)

Gets details of a single GoldengateConnectionAssignment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGoldengateConnectionAssignmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetGoldengateConnectionAssignmentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[GoldengateConnectionAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GoldengateConnectionAssignment)` | The response received from the server.  
  
### GetGoldengateConnectionAssignment(GetGoldengateConnectionAssignmentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual GoldengateConnectionAssignment GetGoldengateConnectionAssignment(GetGoldengateConnectionAssignmentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single GoldengateConnectionAssignment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGoldengateConnectionAssignmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetGoldengateConnectionAssignmentRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[GoldengateConnectionAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GoldengateConnectionAssignment)` | The response received from the server.  
  
### GetGoldengateConnectionAssignmentAsync(GetGoldengateConnectionAssignmentRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<GoldengateConnectionAssignment> GetGoldengateConnectionAssignmentAsync(GetGoldengateConnectionAssignmentRequest request, CallOptions options)

Gets details of a single GoldengateConnectionAssignment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGoldengateConnectionAssignmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetGoldengateConnectionAssignmentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[GoldengateConnectionAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GoldengateConnectionAssignment)` | The call object.  
  
### GetGoldengateConnectionAssignmentAsync(GetGoldengateConnectionAssignmentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<GoldengateConnectionAssignment> GetGoldengateConnectionAssignmentAsync(GetGoldengateConnectionAssignmentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single GoldengateConnectionAssignment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGoldengateConnectionAssignmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetGoldengateConnectionAssignmentRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[GoldengateConnectionAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GoldengateConnectionAssignment)` | The call object.  
  
### GetGoldengateConnectionAsync(GetGoldengateConnectionRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<GoldengateConnection> GetGoldengateConnectionAsync(GetGoldengateConnectionRequest request, CallOptions options)

Gets details of a single GoldengateConnection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGoldengateConnectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetGoldengateConnectionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[GoldengateConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GoldengateConnection)` | The call object.  
  
### GetGoldengateConnectionAsync(GetGoldengateConnectionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<GoldengateConnection> GetGoldengateConnectionAsync(GetGoldengateConnectionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single GoldengateConnection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGoldengateConnectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetGoldengateConnectionRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[GoldengateConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GoldengateConnection)` | The call object.  
  
### GetGoldengateDeployment(GetGoldengateDeploymentRequest, CallOptions)
    
    
    public virtual GoldengateDeployment GetGoldengateDeployment(GetGoldengateDeploymentRequest request, CallOptions options)

Gets details of a single GoldengateDeployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGoldengateDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetGoldengateDeploymentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[GoldengateDeployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GoldengateDeployment)` | The response received from the server.  
  
### GetGoldengateDeployment(GetGoldengateDeploymentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual GoldengateDeployment GetGoldengateDeployment(GetGoldengateDeploymentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single GoldengateDeployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGoldengateDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetGoldengateDeploymentRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[GoldengateDeployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GoldengateDeployment)` | The response received from the server.  
  
### GetGoldengateDeploymentAsync(GetGoldengateDeploymentRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<GoldengateDeployment> GetGoldengateDeploymentAsync(GetGoldengateDeploymentRequest request, CallOptions options)

Gets details of a single GoldengateDeployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGoldengateDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetGoldengateDeploymentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[GoldengateDeployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GoldengateDeployment)` | The call object.  
  
### GetGoldengateDeploymentAsync(GetGoldengateDeploymentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<GoldengateDeployment> GetGoldengateDeploymentAsync(GetGoldengateDeploymentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single GoldengateDeployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGoldengateDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetGoldengateDeploymentRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[GoldengateDeployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GoldengateDeployment)` | The call object.  
  
### GetOdbNetwork(GetOdbNetworkRequest, CallOptions)
    
    
    public virtual OdbNetwork GetOdbNetwork(GetOdbNetworkRequest request, CallOptions options)

Gets details of a single ODB Network.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetOdbNetworkRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetOdbNetworkRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[OdbNetwork](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.OdbNetwork)` | The response received from the server.  
  
### GetOdbNetwork(GetOdbNetworkRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual OdbNetwork GetOdbNetwork(GetOdbNetworkRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single ODB Network.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetOdbNetworkRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetOdbNetworkRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[OdbNetwork](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.OdbNetwork)` | The response received from the server.  
  
### GetOdbNetworkAsync(GetOdbNetworkRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<OdbNetwork> GetOdbNetworkAsync(GetOdbNetworkRequest request, CallOptions options)

Gets details of a single ODB Network.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetOdbNetworkRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetOdbNetworkRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[OdbNetwork](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.OdbNetwork)` | The call object.  
  
### GetOdbNetworkAsync(GetOdbNetworkRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<OdbNetwork> GetOdbNetworkAsync(GetOdbNetworkRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single ODB Network.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetOdbNetworkRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetOdbNetworkRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[OdbNetwork](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.OdbNetwork)` | The call object.  
  
### GetOdbSubnet(GetOdbSubnetRequest, CallOptions)
    
    
    public virtual OdbSubnet GetOdbSubnet(GetOdbSubnetRequest request, CallOptions options)

Gets details of a single ODB Subnet.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetOdbSubnetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetOdbSubnetRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[OdbSubnet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.OdbSubnet)` | The response received from the server.  
  
### GetOdbSubnet(GetOdbSubnetRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual OdbSubnet GetOdbSubnet(GetOdbSubnetRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single ODB Subnet.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetOdbSubnetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetOdbSubnetRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[OdbSubnet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.OdbSubnet)` | The response received from the server.  
  
### GetOdbSubnetAsync(GetOdbSubnetRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<OdbSubnet> GetOdbSubnetAsync(GetOdbSubnetRequest request, CallOptions options)

Gets details of a single ODB Subnet.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetOdbSubnetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetOdbSubnetRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[OdbSubnet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.OdbSubnet)` | The call object.  
  
### GetOdbSubnetAsync(GetOdbSubnetRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<OdbSubnet> GetOdbSubnetAsync(GetOdbSubnetRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single ODB Subnet.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetOdbSubnetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetOdbSubnetRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[OdbSubnet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.OdbSubnet)` | The call object.  
  
### GetPluggableDatabase(GetPluggableDatabaseRequest, CallOptions)
    
    
    public virtual PluggableDatabase GetPluggableDatabase(GetPluggableDatabaseRequest request, CallOptions options)

Gets details of a single PluggableDatabase.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPluggableDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetPluggableDatabaseRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[PluggableDatabase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.PluggableDatabase)` | The response received from the server.  
  
### GetPluggableDatabase(GetPluggableDatabaseRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual PluggableDatabase GetPluggableDatabase(GetPluggableDatabaseRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single PluggableDatabase.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPluggableDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetPluggableDatabaseRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[PluggableDatabase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.PluggableDatabase)` | The response received from the server.  
  
### GetPluggableDatabaseAsync(GetPluggableDatabaseRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<PluggableDatabase> GetPluggableDatabaseAsync(GetPluggableDatabaseRequest request, CallOptions options)

Gets details of a single PluggableDatabase.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPluggableDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetPluggableDatabaseRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[PluggableDatabase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.PluggableDatabase)` | The call object.  
  
### GetPluggableDatabaseAsync(GetPluggableDatabaseRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<PluggableDatabase> GetPluggableDatabaseAsync(GetPluggableDatabaseRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single PluggableDatabase.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPluggableDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetPluggableDatabaseRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[PluggableDatabase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.PluggableDatabase)` | The call object.  
  
### ListAutonomousDatabaseBackups(ListAutonomousDatabaseBackupsRequest, CallOptions)
    
    
    public virtual ListAutonomousDatabaseBackupsResponse ListAutonomousDatabaseBackups(ListAutonomousDatabaseBackupsRequest request, CallOptions options)

Lists the long-term and automatic backups of an Autonomous Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAutonomousDatabaseBackupsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListAutonomousDatabaseBackupsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListAutonomousDatabaseBackupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListAutonomousDatabaseBackupsResponse)` | The response received from the server.  
  
### ListAutonomousDatabaseBackups(ListAutonomousDatabaseBackupsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListAutonomousDatabaseBackupsResponse ListAutonomousDatabaseBackups(ListAutonomousDatabaseBackupsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists the long-term and automatic backups of an Autonomous Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAutonomousDatabaseBackupsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListAutonomousDatabaseBackupsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListAutonomousDatabaseBackupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListAutonomousDatabaseBackupsResponse)` | The response received from the server.  
  
### ListAutonomousDatabaseBackupsAsync(ListAutonomousDatabaseBackupsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListAutonomousDatabaseBackupsResponse> ListAutonomousDatabaseBackupsAsync(ListAutonomousDatabaseBackupsRequest request, CallOptions options)

Lists the long-term and automatic backups of an Autonomous Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAutonomousDatabaseBackupsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListAutonomousDatabaseBackupsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListAutonomousDatabaseBackupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListAutonomousDatabaseBackupsResponse)` | The call object.  
  
### ListAutonomousDatabaseBackupsAsync(ListAutonomousDatabaseBackupsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListAutonomousDatabaseBackupsResponse> ListAutonomousDatabaseBackupsAsync(ListAutonomousDatabaseBackupsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists the long-term and automatic backups of an Autonomous Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAutonomousDatabaseBackupsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListAutonomousDatabaseBackupsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListAutonomousDatabaseBackupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListAutonomousDatabaseBackupsResponse)` | The call object.  
  
### ListAutonomousDatabaseCharacterSets(ListAutonomousDatabaseCharacterSetsRequest, CallOptions)
    
    
    public virtual ListAutonomousDatabaseCharacterSetsResponse ListAutonomousDatabaseCharacterSets(ListAutonomousDatabaseCharacterSetsRequest request, CallOptions options)

Lists Autonomous Database Character Sets in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAutonomousDatabaseCharacterSetsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListAutonomousDatabaseCharacterSetsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListAutonomousDatabaseCharacterSetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListAutonomousDatabaseCharacterSetsResponse)` | The response received from the server.  
  
### ListAutonomousDatabaseCharacterSets(ListAutonomousDatabaseCharacterSetsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListAutonomousDatabaseCharacterSetsResponse ListAutonomousDatabaseCharacterSets(ListAutonomousDatabaseCharacterSetsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists Autonomous Database Character Sets in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAutonomousDatabaseCharacterSetsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListAutonomousDatabaseCharacterSetsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListAutonomousDatabaseCharacterSetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListAutonomousDatabaseCharacterSetsResponse)` | The response received from the server.  
  
### ListAutonomousDatabaseCharacterSetsAsync(ListAutonomousDatabaseCharacterSetsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListAutonomousDatabaseCharacterSetsResponse> ListAutonomousDatabaseCharacterSetsAsync(ListAutonomousDatabaseCharacterSetsRequest request, CallOptions options)

Lists Autonomous Database Character Sets in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAutonomousDatabaseCharacterSetsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListAutonomousDatabaseCharacterSetsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListAutonomousDatabaseCharacterSetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListAutonomousDatabaseCharacterSetsResponse)` | The call object.  
  
### ListAutonomousDatabaseCharacterSetsAsync(ListAutonomousDatabaseCharacterSetsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListAutonomousDatabaseCharacterSetsResponse> ListAutonomousDatabaseCharacterSetsAsync(ListAutonomousDatabaseCharacterSetsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists Autonomous Database Character Sets in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAutonomousDatabaseCharacterSetsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListAutonomousDatabaseCharacterSetsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListAutonomousDatabaseCharacterSetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListAutonomousDatabaseCharacterSetsResponse)` | The call object.  
  
### ListAutonomousDatabases(ListAutonomousDatabasesRequest, CallOptions)
    
    
    public virtual ListAutonomousDatabasesResponse ListAutonomousDatabases(ListAutonomousDatabasesRequest request, CallOptions options)

Lists the Autonomous Databases in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAutonomousDatabasesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListAutonomousDatabasesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListAutonomousDatabasesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListAutonomousDatabasesResponse)` | The response received from the server.  
  
### ListAutonomousDatabases(ListAutonomousDatabasesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListAutonomousDatabasesResponse ListAutonomousDatabases(ListAutonomousDatabasesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists the Autonomous Databases in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAutonomousDatabasesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListAutonomousDatabasesRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListAutonomousDatabasesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListAutonomousDatabasesResponse)` | The response received from the server.  
  
### ListAutonomousDatabasesAsync(ListAutonomousDatabasesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListAutonomousDatabasesResponse> ListAutonomousDatabasesAsync(ListAutonomousDatabasesRequest request, CallOptions options)

Lists the Autonomous Databases in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAutonomousDatabasesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListAutonomousDatabasesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListAutonomousDatabasesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListAutonomousDatabasesResponse)` | The call object.  
  
### ListAutonomousDatabasesAsync(ListAutonomousDatabasesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListAutonomousDatabasesResponse> ListAutonomousDatabasesAsync(ListAutonomousDatabasesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists the Autonomous Databases in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAutonomousDatabasesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListAutonomousDatabasesRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListAutonomousDatabasesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListAutonomousDatabasesResponse)` | The call object.  
  
### ListAutonomousDbVersions(ListAutonomousDbVersionsRequest, CallOptions)
    
    
    public virtual ListAutonomousDbVersionsResponse ListAutonomousDbVersions(ListAutonomousDbVersionsRequest request, CallOptions options)

Lists all the available Autonomous Database versions for a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAutonomousDbVersionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListAutonomousDbVersionsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListAutonomousDbVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListAutonomousDbVersionsResponse)` | The response received from the server.  
  
### ListAutonomousDbVersions(ListAutonomousDbVersionsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListAutonomousDbVersionsResponse ListAutonomousDbVersions(ListAutonomousDbVersionsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all the available Autonomous Database versions for a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAutonomousDbVersionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListAutonomousDbVersionsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListAutonomousDbVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListAutonomousDbVersionsResponse)` | The response received from the server.  
  
### ListAutonomousDbVersionsAsync(ListAutonomousDbVersionsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListAutonomousDbVersionsResponse> ListAutonomousDbVersionsAsync(ListAutonomousDbVersionsRequest request, CallOptions options)

Lists all the available Autonomous Database versions for a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAutonomousDbVersionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListAutonomousDbVersionsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListAutonomousDbVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListAutonomousDbVersionsResponse)` | The call object.  
  
### ListAutonomousDbVersionsAsync(ListAutonomousDbVersionsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListAutonomousDbVersionsResponse> ListAutonomousDbVersionsAsync(ListAutonomousDbVersionsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all the available Autonomous Database versions for a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAutonomousDbVersionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListAutonomousDbVersionsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListAutonomousDbVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListAutonomousDbVersionsResponse)` | The call object.  
  
### ListCloudExadataInfrastructures(ListCloudExadataInfrastructuresRequest, CallOptions)
    
    
    public virtual ListCloudExadataInfrastructuresResponse ListCloudExadataInfrastructures(ListCloudExadataInfrastructuresRequest request, CallOptions options)

Lists Exadata Infrastructures in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListCloudExadataInfrastructuresRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListCloudExadataInfrastructuresRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListCloudExadataInfrastructuresResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListCloudExadataInfrastructuresResponse)` | The response received from the server.  
  
### ListCloudExadataInfrastructures(ListCloudExadataInfrastructuresRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListCloudExadataInfrastructuresResponse ListCloudExadataInfrastructures(ListCloudExadataInfrastructuresRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists Exadata Infrastructures in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListCloudExadataInfrastructuresRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListCloudExadataInfrastructuresRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListCloudExadataInfrastructuresResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListCloudExadataInfrastructuresResponse)` | The response received from the server.  
  
### ListCloudExadataInfrastructuresAsync(ListCloudExadataInfrastructuresRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListCloudExadataInfrastructuresResponse> ListCloudExadataInfrastructuresAsync(ListCloudExadataInfrastructuresRequest request, CallOptions options)

Lists Exadata Infrastructures in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListCloudExadataInfrastructuresRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListCloudExadataInfrastructuresRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListCloudExadataInfrastructuresResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListCloudExadataInfrastructuresResponse)` | The call object.  
  
### ListCloudExadataInfrastructuresAsync(ListCloudExadataInfrastructuresRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListCloudExadataInfrastructuresResponse> ListCloudExadataInfrastructuresAsync(ListCloudExadataInfrastructuresRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists Exadata Infrastructures in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListCloudExadataInfrastructuresRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListCloudExadataInfrastructuresRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListCloudExadataInfrastructuresResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListCloudExadataInfrastructuresResponse)` | The call object.  
  
### ListCloudVmClusters(ListCloudVmClustersRequest, CallOptions)
    
    
    public virtual ListCloudVmClustersResponse ListCloudVmClusters(ListCloudVmClustersRequest request, CallOptions options)

Lists the VM Clusters in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListCloudVmClustersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListCloudVmClustersRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListCloudVmClustersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListCloudVmClustersResponse)` | The response received from the server.  
  
### ListCloudVmClusters(ListCloudVmClustersRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListCloudVmClustersResponse ListCloudVmClusters(ListCloudVmClustersRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists the VM Clusters in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListCloudVmClustersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListCloudVmClustersRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListCloudVmClustersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListCloudVmClustersResponse)` | The response received from the server.  
  
### ListCloudVmClustersAsync(ListCloudVmClustersRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListCloudVmClustersResponse> ListCloudVmClustersAsync(ListCloudVmClustersRequest request, CallOptions options)

Lists the VM Clusters in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListCloudVmClustersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListCloudVmClustersRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListCloudVmClustersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListCloudVmClustersResponse)` | The call object.  
  
### ListCloudVmClustersAsync(ListCloudVmClustersRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListCloudVmClustersResponse> ListCloudVmClustersAsync(ListCloudVmClustersRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists the VM Clusters in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListCloudVmClustersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListCloudVmClustersRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListCloudVmClustersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListCloudVmClustersResponse)` | The call object.  
  
### ListDatabaseCharacterSets(ListDatabaseCharacterSetsRequest, CallOptions)
    
    
    public virtual ListDatabaseCharacterSetsResponse ListDatabaseCharacterSets(ListDatabaseCharacterSetsRequest request, CallOptions options)

List DatabaseCharacterSets for the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDatabaseCharacterSetsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDatabaseCharacterSetsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListDatabaseCharacterSetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDatabaseCharacterSetsResponse)` | The response received from the server.  
  
### ListDatabaseCharacterSets(ListDatabaseCharacterSetsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListDatabaseCharacterSetsResponse ListDatabaseCharacterSets(ListDatabaseCharacterSetsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

List DatabaseCharacterSets for the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDatabaseCharacterSetsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDatabaseCharacterSetsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListDatabaseCharacterSetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDatabaseCharacterSetsResponse)` | The response received from the server.  
  
### ListDatabaseCharacterSetsAsync(ListDatabaseCharacterSetsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListDatabaseCharacterSetsResponse> ListDatabaseCharacterSetsAsync(ListDatabaseCharacterSetsRequest request, CallOptions options)

List DatabaseCharacterSets for the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDatabaseCharacterSetsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDatabaseCharacterSetsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListDatabaseCharacterSetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDatabaseCharacterSetsResponse)` | The call object.  
  
### ListDatabaseCharacterSetsAsync(ListDatabaseCharacterSetsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListDatabaseCharacterSetsResponse> ListDatabaseCharacterSetsAsync(ListDatabaseCharacterSetsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

List DatabaseCharacterSets for the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDatabaseCharacterSetsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDatabaseCharacterSetsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListDatabaseCharacterSetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDatabaseCharacterSetsResponse)` | The call object.  
  
### ListDatabases(ListDatabasesRequest, CallOptions)
    
    
    public virtual ListDatabasesResponse ListDatabases(ListDatabasesRequest request, CallOptions options)

Lists all the Databases for the given project, location and DbSystem.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDatabasesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDatabasesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListDatabasesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDatabasesResponse)` | The response received from the server.  
  
### ListDatabases(ListDatabasesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListDatabasesResponse ListDatabases(ListDatabasesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all the Databases for the given project, location and DbSystem.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDatabasesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDatabasesRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListDatabasesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDatabasesResponse)` | The response received from the server.  
  
### ListDatabasesAsync(ListDatabasesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListDatabasesResponse> ListDatabasesAsync(ListDatabasesRequest request, CallOptions options)

Lists all the Databases for the given project, location and DbSystem.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDatabasesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDatabasesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListDatabasesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDatabasesResponse)` | The call object.  
  
### ListDatabasesAsync(ListDatabasesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListDatabasesResponse> ListDatabasesAsync(ListDatabasesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all the Databases for the given project, location and DbSystem.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDatabasesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDatabasesRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListDatabasesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDatabasesResponse)` | The call object.  
  
### ListDbNodes(ListDbNodesRequest, CallOptions)
    
    
    public virtual ListDbNodesResponse ListDbNodes(ListDbNodesRequest request, CallOptions options)

Lists the database nodes of a VM Cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDbNodesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDbNodesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListDbNodesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDbNodesResponse)` | The response received from the server.  
  
### ListDbNodes(ListDbNodesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListDbNodesResponse ListDbNodes(ListDbNodesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists the database nodes of a VM Cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDbNodesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDbNodesRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListDbNodesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDbNodesResponse)` | The response received from the server.  
  
### ListDbNodesAsync(ListDbNodesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListDbNodesResponse> ListDbNodesAsync(ListDbNodesRequest request, CallOptions options)

Lists the database nodes of a VM Cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDbNodesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDbNodesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListDbNodesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDbNodesResponse)` | The call object.  
  
### ListDbNodesAsync(ListDbNodesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListDbNodesResponse> ListDbNodesAsync(ListDbNodesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists the database nodes of a VM Cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDbNodesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDbNodesRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListDbNodesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDbNodesResponse)` | The call object.  
  
### ListDbServers(ListDbServersRequest, CallOptions)
    
    
    public virtual ListDbServersResponse ListDbServers(ListDbServersRequest request, CallOptions options)

Lists the database servers of an Exadata Infrastructure instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDbServersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDbServersRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListDbServersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDbServersResponse)` | The response received from the server.  
  
### ListDbServers(ListDbServersRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListDbServersResponse ListDbServers(ListDbServersRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists the database servers of an Exadata Infrastructure instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDbServersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDbServersRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListDbServersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDbServersResponse)` | The response received from the server.  
  
### ListDbServersAsync(ListDbServersRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListDbServersResponse> ListDbServersAsync(ListDbServersRequest request, CallOptions options)

Lists the database servers of an Exadata Infrastructure instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDbServersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDbServersRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListDbServersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDbServersResponse)` | The call object.  
  
### ListDbServersAsync(ListDbServersRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListDbServersResponse> ListDbServersAsync(ListDbServersRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists the database servers of an Exadata Infrastructure instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDbServersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDbServersRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListDbServersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDbServersResponse)` | The call object.  
  
### ListDbSystemInitialStorageSizes(ListDbSystemInitialStorageSizesRequest, CallOptions)
    
    
    public virtual ListDbSystemInitialStorageSizesResponse ListDbSystemInitialStorageSizes(ListDbSystemInitialStorageSizesRequest request, CallOptions options)

Lists all the DbSystemInitialStorageSizes for the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDbSystemInitialStorageSizesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDbSystemInitialStorageSizesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListDbSystemInitialStorageSizesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDbSystemInitialStorageSizesResponse)` | The response received from the server.  
  
### ListDbSystemInitialStorageSizes(ListDbSystemInitialStorageSizesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListDbSystemInitialStorageSizesResponse ListDbSystemInitialStorageSizes(ListDbSystemInitialStorageSizesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all the DbSystemInitialStorageSizes for the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDbSystemInitialStorageSizesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDbSystemInitialStorageSizesRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListDbSystemInitialStorageSizesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDbSystemInitialStorageSizesResponse)` | The response received from the server.  
  
### ListDbSystemInitialStorageSizesAsync(ListDbSystemInitialStorageSizesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListDbSystemInitialStorageSizesResponse> ListDbSystemInitialStorageSizesAsync(ListDbSystemInitialStorageSizesRequest request, CallOptions options)

Lists all the DbSystemInitialStorageSizes for the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDbSystemInitialStorageSizesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDbSystemInitialStorageSizesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListDbSystemInitialStorageSizesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDbSystemInitialStorageSizesResponse)` | The call object.  
  
### ListDbSystemInitialStorageSizesAsync(ListDbSystemInitialStorageSizesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListDbSystemInitialStorageSizesResponse> ListDbSystemInitialStorageSizesAsync(ListDbSystemInitialStorageSizesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all the DbSystemInitialStorageSizes for the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDbSystemInitialStorageSizesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDbSystemInitialStorageSizesRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListDbSystemInitialStorageSizesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDbSystemInitialStorageSizesResponse)` | The call object.  
  
### ListDbSystemShapes(ListDbSystemShapesRequest, CallOptions)
    
    
    public virtual ListDbSystemShapesResponse ListDbSystemShapes(ListDbSystemShapesRequest request, CallOptions options)

Lists the database system shapes available for the project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDbSystemShapesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDbSystemShapesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListDbSystemShapesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDbSystemShapesResponse)` | The response received from the server.  
  
### ListDbSystemShapes(ListDbSystemShapesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListDbSystemShapesResponse ListDbSystemShapes(ListDbSystemShapesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists the database system shapes available for the project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDbSystemShapesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDbSystemShapesRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListDbSystemShapesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDbSystemShapesResponse)` | The response received from the server.  
  
### ListDbSystemShapesAsync(ListDbSystemShapesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListDbSystemShapesResponse> ListDbSystemShapesAsync(ListDbSystemShapesRequest request, CallOptions options)

Lists the database system shapes available for the project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDbSystemShapesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDbSystemShapesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListDbSystemShapesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDbSystemShapesResponse)` | The call object.  
  
### ListDbSystemShapesAsync(ListDbSystemShapesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListDbSystemShapesResponse> ListDbSystemShapesAsync(ListDbSystemShapesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists the database system shapes available for the project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDbSystemShapesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDbSystemShapesRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListDbSystemShapesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDbSystemShapesResponse)` | The call object.  
  
### ListDbSystems(ListDbSystemsRequest, CallOptions)
    
    
    public virtual ListDbSystemsResponse ListDbSystems(ListDbSystemsRequest request, CallOptions options)

Lists all the DbSystems for the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDbSystemsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDbSystemsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListDbSystemsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDbSystemsResponse)` | The response received from the server.  
  
### ListDbSystems(ListDbSystemsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListDbSystemsResponse ListDbSystems(ListDbSystemsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all the DbSystems for the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDbSystemsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDbSystemsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListDbSystemsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDbSystemsResponse)` | The response received from the server.  
  
### ListDbSystemsAsync(ListDbSystemsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListDbSystemsResponse> ListDbSystemsAsync(ListDbSystemsRequest request, CallOptions options)

Lists all the DbSystems for the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDbSystemsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDbSystemsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListDbSystemsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDbSystemsResponse)` | The call object.  
  
### ListDbSystemsAsync(ListDbSystemsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListDbSystemsResponse> ListDbSystemsAsync(ListDbSystemsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all the DbSystems for the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDbSystemsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDbSystemsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListDbSystemsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDbSystemsResponse)` | The call object.  
  
### ListDbVersions(ListDbVersionsRequest, CallOptions)
    
    
    public virtual ListDbVersionsResponse ListDbVersions(ListDbVersionsRequest request, CallOptions options)

List DbVersions for the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDbVersionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDbVersionsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListDbVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDbVersionsResponse)` | The response received from the server.  
  
### ListDbVersions(ListDbVersionsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListDbVersionsResponse ListDbVersions(ListDbVersionsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

List DbVersions for the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDbVersionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDbVersionsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListDbVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDbVersionsResponse)` | The response received from the server.  
  
### ListDbVersionsAsync(ListDbVersionsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListDbVersionsResponse> ListDbVersionsAsync(ListDbVersionsRequest request, CallOptions options)

List DbVersions for the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDbVersionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDbVersionsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListDbVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDbVersionsResponse)` | The call object.  
  
### ListDbVersionsAsync(ListDbVersionsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListDbVersionsResponse> ListDbVersionsAsync(ListDbVersionsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

List DbVersions for the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDbVersionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDbVersionsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListDbVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListDbVersionsResponse)` | The call object.  
  
### ListEntitlements(ListEntitlementsRequest, CallOptions)
    
    
    public virtual ListEntitlementsResponse ListEntitlements(ListEntitlementsRequest request, CallOptions options)

Lists the entitlements in a given project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListEntitlementsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListEntitlementsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListEntitlementsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListEntitlementsResponse)` | The response received from the server.  
  
### ListEntitlements(ListEntitlementsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListEntitlementsResponse ListEntitlements(ListEntitlementsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists the entitlements in a given project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListEntitlementsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListEntitlementsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListEntitlementsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListEntitlementsResponse)` | The response received from the server.  
  
### ListEntitlementsAsync(ListEntitlementsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListEntitlementsResponse> ListEntitlementsAsync(ListEntitlementsRequest request, CallOptions options)

Lists the entitlements in a given project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListEntitlementsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListEntitlementsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListEntitlementsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListEntitlementsResponse)` | The call object.  
  
### ListEntitlementsAsync(ListEntitlementsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListEntitlementsResponse> ListEntitlementsAsync(ListEntitlementsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists the entitlements in a given project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListEntitlementsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListEntitlementsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListEntitlementsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListEntitlementsResponse)` | The call object.  
  
### ListExadbVmClusters(ListExadbVmClustersRequest, CallOptions)
    
    
    public virtual ListExadbVmClustersResponse ListExadbVmClusters(ListExadbVmClustersRequest request, CallOptions options)

Lists all the Exadb (Exascale) VM Clusters for the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListExadbVmClustersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListExadbVmClustersRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListExadbVmClustersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListExadbVmClustersResponse)` | The response received from the server.  
  
### ListExadbVmClusters(ListExadbVmClustersRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListExadbVmClustersResponse ListExadbVmClusters(ListExadbVmClustersRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all the Exadb (Exascale) VM Clusters for the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListExadbVmClustersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListExadbVmClustersRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListExadbVmClustersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListExadbVmClustersResponse)` | The response received from the server.  
  
### ListExadbVmClustersAsync(ListExadbVmClustersRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListExadbVmClustersResponse> ListExadbVmClustersAsync(ListExadbVmClustersRequest request, CallOptions options)

Lists all the Exadb (Exascale) VM Clusters for the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListExadbVmClustersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListExadbVmClustersRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListExadbVmClustersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListExadbVmClustersResponse)` | The call object.  
  
### ListExadbVmClustersAsync(ListExadbVmClustersRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListExadbVmClustersResponse> ListExadbVmClustersAsync(ListExadbVmClustersRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all the Exadb (Exascale) VM Clusters for the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListExadbVmClustersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListExadbVmClustersRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListExadbVmClustersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListExadbVmClustersResponse)` | The call object.  
  
### ListExascaleDbStorageVaults(ListExascaleDbStorageVaultsRequest, CallOptions)
    
    
    public virtual ListExascaleDbStorageVaultsResponse ListExascaleDbStorageVaults(ListExascaleDbStorageVaultsRequest request, CallOptions options)

Lists all the ExascaleDB Storage Vaults for the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListExascaleDbStorageVaultsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListExascaleDbStorageVaultsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListExascaleDbStorageVaultsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListExascaleDbStorageVaultsResponse)` | The response received from the server.  
  
### ListExascaleDbStorageVaults(ListExascaleDbStorageVaultsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListExascaleDbStorageVaultsResponse ListExascaleDbStorageVaults(ListExascaleDbStorageVaultsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all the ExascaleDB Storage Vaults for the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListExascaleDbStorageVaultsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListExascaleDbStorageVaultsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListExascaleDbStorageVaultsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListExascaleDbStorageVaultsResponse)` | The response received from the server.  
  
### ListExascaleDbStorageVaultsAsync(ListExascaleDbStorageVaultsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListExascaleDbStorageVaultsResponse> ListExascaleDbStorageVaultsAsync(ListExascaleDbStorageVaultsRequest request, CallOptions options)

Lists all the ExascaleDB Storage Vaults for the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListExascaleDbStorageVaultsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListExascaleDbStorageVaultsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListExascaleDbStorageVaultsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListExascaleDbStorageVaultsResponse)` | The call object.  
  
### ListExascaleDbStorageVaultsAsync(ListExascaleDbStorageVaultsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListExascaleDbStorageVaultsResponse> ListExascaleDbStorageVaultsAsync(ListExascaleDbStorageVaultsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all the ExascaleDB Storage Vaults for the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListExascaleDbStorageVaultsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListExascaleDbStorageVaultsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListExascaleDbStorageVaultsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListExascaleDbStorageVaultsResponse)` | The call object.  
  
### ListGiVersions(ListGiVersionsRequest, CallOptions)
    
    
    public virtual ListGiVersionsResponse ListGiVersions(ListGiVersionsRequest request, CallOptions options)

Lists all the valid Oracle Grid Infrastructure (GI) versions for the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGiVersionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGiVersionsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListGiVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGiVersionsResponse)` | The response received from the server.  
  
### ListGiVersions(ListGiVersionsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListGiVersionsResponse ListGiVersions(ListGiVersionsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all the valid Oracle Grid Infrastructure (GI) versions for the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGiVersionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGiVersionsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListGiVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGiVersionsResponse)` | The response received from the server.  
  
### ListGiVersionsAsync(ListGiVersionsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListGiVersionsResponse> ListGiVersionsAsync(ListGiVersionsRequest request, CallOptions options)

Lists all the valid Oracle Grid Infrastructure (GI) versions for the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGiVersionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGiVersionsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListGiVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGiVersionsResponse)` | The call object.  
  
### ListGiVersionsAsync(ListGiVersionsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListGiVersionsResponse> ListGiVersionsAsync(ListGiVersionsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all the valid Oracle Grid Infrastructure (GI) versions for the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGiVersionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGiVersionsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListGiVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGiVersionsResponse)` | The call object.  
  
### ListGoldengateConnectionAssignments(ListGoldengateConnectionAssignmentsRequest, CallOptions)
    
    
    public virtual ListGoldengateConnectionAssignmentsResponse ListGoldengateConnectionAssignments(ListGoldengateConnectionAssignmentsRequest request, CallOptions options)

Lists GoldengateConnectionAssignments in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGoldengateConnectionAssignmentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateConnectionAssignmentsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListGoldengateConnectionAssignmentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateConnectionAssignmentsResponse)` | The response received from the server.  
  
### ListGoldengateConnectionAssignments(ListGoldengateConnectionAssignmentsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListGoldengateConnectionAssignmentsResponse ListGoldengateConnectionAssignments(ListGoldengateConnectionAssignmentsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists GoldengateConnectionAssignments in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGoldengateConnectionAssignmentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateConnectionAssignmentsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListGoldengateConnectionAssignmentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateConnectionAssignmentsResponse)` | The response received from the server.  
  
### ListGoldengateConnectionAssignmentsAsync(ListGoldengateConnectionAssignmentsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListGoldengateConnectionAssignmentsResponse> ListGoldengateConnectionAssignmentsAsync(ListGoldengateConnectionAssignmentsRequest request, CallOptions options)

Lists GoldengateConnectionAssignments in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGoldengateConnectionAssignmentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateConnectionAssignmentsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListGoldengateConnectionAssignmentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateConnectionAssignmentsResponse)` | The call object.  
  
### ListGoldengateConnectionAssignmentsAsync(ListGoldengateConnectionAssignmentsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListGoldengateConnectionAssignmentsResponse> ListGoldengateConnectionAssignmentsAsync(ListGoldengateConnectionAssignmentsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists GoldengateConnectionAssignments in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGoldengateConnectionAssignmentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateConnectionAssignmentsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListGoldengateConnectionAssignmentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateConnectionAssignmentsResponse)` | The call object.  
  
### ListGoldengateConnectionTypes(ListGoldengateConnectionTypesRequest, CallOptions)
    
    
    public virtual ListGoldengateConnectionTypesResponse ListGoldengateConnectionTypes(ListGoldengateConnectionTypesRequest request, CallOptions options)

Lists GoldengateConnectionTypes in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGoldengateConnectionTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateConnectionTypesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListGoldengateConnectionTypesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateConnectionTypesResponse)` | The response received from the server.  
  
### ListGoldengateConnectionTypes(ListGoldengateConnectionTypesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListGoldengateConnectionTypesResponse ListGoldengateConnectionTypes(ListGoldengateConnectionTypesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists GoldengateConnectionTypes in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGoldengateConnectionTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateConnectionTypesRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListGoldengateConnectionTypesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateConnectionTypesResponse)` | The response received from the server.  
  
### ListGoldengateConnectionTypesAsync(ListGoldengateConnectionTypesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListGoldengateConnectionTypesResponse> ListGoldengateConnectionTypesAsync(ListGoldengateConnectionTypesRequest request, CallOptions options)

Lists GoldengateConnectionTypes in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGoldengateConnectionTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateConnectionTypesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListGoldengateConnectionTypesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateConnectionTypesResponse)` | The call object.  
  
### ListGoldengateConnectionTypesAsync(ListGoldengateConnectionTypesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListGoldengateConnectionTypesResponse> ListGoldengateConnectionTypesAsync(ListGoldengateConnectionTypesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists GoldengateConnectionTypes in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGoldengateConnectionTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateConnectionTypesRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListGoldengateConnectionTypesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateConnectionTypesResponse)` | The call object.  
  
### ListGoldengateConnections(ListGoldengateConnectionsRequest, CallOptions)
    
    
    public virtual ListGoldengateConnectionsResponse ListGoldengateConnections(ListGoldengateConnectionsRequest request, CallOptions options)

Lists all the GoldengateConnections for the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGoldengateConnectionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateConnectionsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListGoldengateConnectionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateConnectionsResponse)` | The response received from the server.  
  
### ListGoldengateConnections(ListGoldengateConnectionsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListGoldengateConnectionsResponse ListGoldengateConnections(ListGoldengateConnectionsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all the GoldengateConnections for the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGoldengateConnectionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateConnectionsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListGoldengateConnectionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateConnectionsResponse)` | The response received from the server.  
  
### ListGoldengateConnectionsAsync(ListGoldengateConnectionsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListGoldengateConnectionsResponse> ListGoldengateConnectionsAsync(ListGoldengateConnectionsRequest request, CallOptions options)

Lists all the GoldengateConnections for the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGoldengateConnectionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateConnectionsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListGoldengateConnectionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateConnectionsResponse)` | The call object.  
  
### ListGoldengateConnectionsAsync(ListGoldengateConnectionsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListGoldengateConnectionsResponse> ListGoldengateConnectionsAsync(ListGoldengateConnectionsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all the GoldengateConnections for the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGoldengateConnectionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateConnectionsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListGoldengateConnectionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateConnectionsResponse)` | The call object.  
  
### ListGoldengateDeploymentEnvironments(ListGoldengateDeploymentEnvironmentsRequest, CallOptions)
    
    
    public virtual ListGoldengateDeploymentEnvironmentsResponse ListGoldengateDeploymentEnvironments(ListGoldengateDeploymentEnvironmentsRequest request, CallOptions options)

Lists GoldengateDeploymentEnvironments in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGoldengateDeploymentEnvironmentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateDeploymentEnvironmentsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListGoldengateDeploymentEnvironmentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateDeploymentEnvironmentsResponse)` | The response received from the server.  
  
### ListGoldengateDeploymentEnvironments(ListGoldengateDeploymentEnvironmentsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListGoldengateDeploymentEnvironmentsResponse ListGoldengateDeploymentEnvironments(ListGoldengateDeploymentEnvironmentsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists GoldengateDeploymentEnvironments in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGoldengateDeploymentEnvironmentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateDeploymentEnvironmentsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListGoldengateDeploymentEnvironmentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateDeploymentEnvironmentsResponse)` | The response received from the server.  
  
### ListGoldengateDeploymentEnvironmentsAsync(ListGoldengateDeploymentEnvironmentsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListGoldengateDeploymentEnvironmentsResponse> ListGoldengateDeploymentEnvironmentsAsync(ListGoldengateDeploymentEnvironmentsRequest request, CallOptions options)

Lists GoldengateDeploymentEnvironments in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGoldengateDeploymentEnvironmentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateDeploymentEnvironmentsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListGoldengateDeploymentEnvironmentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateDeploymentEnvironmentsResponse)` | The call object.  
  
### ListGoldengateDeploymentEnvironmentsAsync(ListGoldengateDeploymentEnvironmentsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListGoldengateDeploymentEnvironmentsResponse> ListGoldengateDeploymentEnvironmentsAsync(ListGoldengateDeploymentEnvironmentsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists GoldengateDeploymentEnvironments in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGoldengateDeploymentEnvironmentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateDeploymentEnvironmentsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListGoldengateDeploymentEnvironmentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateDeploymentEnvironmentsResponse)` | The call object.  
  
### ListGoldengateDeploymentTypes(ListGoldengateDeploymentTypesRequest, CallOptions)
    
    
    public virtual ListGoldengateDeploymentTypesResponse ListGoldengateDeploymentTypes(ListGoldengateDeploymentTypesRequest request, CallOptions options)

Lists GoldenGateDeploymentTypes in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGoldengateDeploymentTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateDeploymentTypesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListGoldengateDeploymentTypesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateDeploymentTypesResponse)` | The response received from the server.  
  
### ListGoldengateDeploymentTypes(ListGoldengateDeploymentTypesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListGoldengateDeploymentTypesResponse ListGoldengateDeploymentTypes(ListGoldengateDeploymentTypesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists GoldenGateDeploymentTypes in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGoldengateDeploymentTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateDeploymentTypesRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListGoldengateDeploymentTypesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateDeploymentTypesResponse)` | The response received from the server.  
  
### ListGoldengateDeploymentTypesAsync(ListGoldengateDeploymentTypesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListGoldengateDeploymentTypesResponse> ListGoldengateDeploymentTypesAsync(ListGoldengateDeploymentTypesRequest request, CallOptions options)

Lists GoldenGateDeploymentTypes in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGoldengateDeploymentTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateDeploymentTypesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListGoldengateDeploymentTypesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateDeploymentTypesResponse)` | The call object.  
  
### ListGoldengateDeploymentTypesAsync(ListGoldengateDeploymentTypesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListGoldengateDeploymentTypesResponse> ListGoldengateDeploymentTypesAsync(ListGoldengateDeploymentTypesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists GoldenGateDeploymentTypes in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGoldengateDeploymentTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateDeploymentTypesRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListGoldengateDeploymentTypesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateDeploymentTypesResponse)` | The call object.  
  
### ListGoldengateDeploymentVersions(ListGoldengateDeploymentVersionsRequest, CallOptions)
    
    
    public virtual ListGoldengateDeploymentVersionsResponse ListGoldengateDeploymentVersions(ListGoldengateDeploymentVersionsRequest request, CallOptions options)

Lists GoldengateDeploymentVersions in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGoldengateDeploymentVersionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateDeploymentVersionsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListGoldengateDeploymentVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateDeploymentVersionsResponse)` | The response received from the server.  
  
### ListGoldengateDeploymentVersions(ListGoldengateDeploymentVersionsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListGoldengateDeploymentVersionsResponse ListGoldengateDeploymentVersions(ListGoldengateDeploymentVersionsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists GoldengateDeploymentVersions in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGoldengateDeploymentVersionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateDeploymentVersionsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListGoldengateDeploymentVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateDeploymentVersionsResponse)` | The response received from the server.  
  
### ListGoldengateDeploymentVersionsAsync(ListGoldengateDeploymentVersionsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListGoldengateDeploymentVersionsResponse> ListGoldengateDeploymentVersionsAsync(ListGoldengateDeploymentVersionsRequest request, CallOptions options)

Lists GoldengateDeploymentVersions in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGoldengateDeploymentVersionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateDeploymentVersionsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListGoldengateDeploymentVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateDeploymentVersionsResponse)` | The call object.  
  
### ListGoldengateDeploymentVersionsAsync(ListGoldengateDeploymentVersionsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListGoldengateDeploymentVersionsResponse> ListGoldengateDeploymentVersionsAsync(ListGoldengateDeploymentVersionsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists GoldengateDeploymentVersions in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGoldengateDeploymentVersionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateDeploymentVersionsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListGoldengateDeploymentVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateDeploymentVersionsResponse)` | The call object.  
  
### ListGoldengateDeployments(ListGoldengateDeploymentsRequest, CallOptions)
    
    
    public virtual ListGoldengateDeploymentsResponse ListGoldengateDeployments(ListGoldengateDeploymentsRequest request, CallOptions options)

Lists all the GoldengateDeployments for the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGoldengateDeploymentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateDeploymentsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListGoldengateDeploymentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateDeploymentsResponse)` | The response received from the server.  
  
### ListGoldengateDeployments(ListGoldengateDeploymentsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListGoldengateDeploymentsResponse ListGoldengateDeployments(ListGoldengateDeploymentsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all the GoldengateDeployments for the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGoldengateDeploymentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateDeploymentsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListGoldengateDeploymentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateDeploymentsResponse)` | The response received from the server.  
  
### ListGoldengateDeploymentsAsync(ListGoldengateDeploymentsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListGoldengateDeploymentsResponse> ListGoldengateDeploymentsAsync(ListGoldengateDeploymentsRequest request, CallOptions options)

Lists all the GoldengateDeployments for the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGoldengateDeploymentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateDeploymentsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListGoldengateDeploymentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateDeploymentsResponse)` | The call object.  
  
### ListGoldengateDeploymentsAsync(ListGoldengateDeploymentsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListGoldengateDeploymentsResponse> ListGoldengateDeploymentsAsync(ListGoldengateDeploymentsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all the GoldengateDeployments for the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGoldengateDeploymentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateDeploymentsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListGoldengateDeploymentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateDeploymentsResponse)` | The call object.  
  
### ListMinorVersions(ListMinorVersionsRequest, CallOptions)
    
    
    public virtual ListMinorVersionsResponse ListMinorVersions(ListMinorVersionsRequest request, CallOptions options)

Lists all the valid minor versions for the given project, location, gi version and shape family.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListMinorVersionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListMinorVersionsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListMinorVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListMinorVersionsResponse)` | The response received from the server.  
  
### ListMinorVersions(ListMinorVersionsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListMinorVersionsResponse ListMinorVersions(ListMinorVersionsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all the valid minor versions for the given project, location, gi version and shape family.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListMinorVersionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListMinorVersionsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListMinorVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListMinorVersionsResponse)` | The response received from the server.  
  
### ListMinorVersionsAsync(ListMinorVersionsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListMinorVersionsResponse> ListMinorVersionsAsync(ListMinorVersionsRequest request, CallOptions options)

Lists all the valid minor versions for the given project, location, gi version and shape family.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListMinorVersionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListMinorVersionsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListMinorVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListMinorVersionsResponse)` | The call object.  
  
### ListMinorVersionsAsync(ListMinorVersionsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListMinorVersionsResponse> ListMinorVersionsAsync(ListMinorVersionsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all the valid minor versions for the given project, location, gi version and shape family.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListMinorVersionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListMinorVersionsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListMinorVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListMinorVersionsResponse)` | The call object.  
  
### ListOdbNetworks(ListOdbNetworksRequest, CallOptions)
    
    
    public virtual ListOdbNetworksResponse ListOdbNetworks(ListOdbNetworksRequest request, CallOptions options)

Lists the ODB Networks in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListOdbNetworksRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListOdbNetworksRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListOdbNetworksResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListOdbNetworksResponse)` | The response received from the server.  
  
### ListOdbNetworks(ListOdbNetworksRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListOdbNetworksResponse ListOdbNetworks(ListOdbNetworksRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists the ODB Networks in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListOdbNetworksRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListOdbNetworksRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListOdbNetworksResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListOdbNetworksResponse)` | The response received from the server.  
  
### ListOdbNetworksAsync(ListOdbNetworksRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListOdbNetworksResponse> ListOdbNetworksAsync(ListOdbNetworksRequest request, CallOptions options)

Lists the ODB Networks in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListOdbNetworksRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListOdbNetworksRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListOdbNetworksResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListOdbNetworksResponse)` | The call object.  
  
### ListOdbNetworksAsync(ListOdbNetworksRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListOdbNetworksResponse> ListOdbNetworksAsync(ListOdbNetworksRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists the ODB Networks in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListOdbNetworksRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListOdbNetworksRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListOdbNetworksResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListOdbNetworksResponse)` | The call object.  
  
### ListOdbSubnets(ListOdbSubnetsRequest, CallOptions)
    
    
    public virtual ListOdbSubnetsResponse ListOdbSubnets(ListOdbSubnetsRequest request, CallOptions options)

Lists all the ODB Subnets in a given ODB Network.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListOdbSubnetsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListOdbSubnetsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListOdbSubnetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListOdbSubnetsResponse)` | The response received from the server.  
  
### ListOdbSubnets(ListOdbSubnetsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListOdbSubnetsResponse ListOdbSubnets(ListOdbSubnetsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all the ODB Subnets in a given ODB Network.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListOdbSubnetsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListOdbSubnetsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListOdbSubnetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListOdbSubnetsResponse)` | The response received from the server.  
  
### ListOdbSubnetsAsync(ListOdbSubnetsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListOdbSubnetsResponse> ListOdbSubnetsAsync(ListOdbSubnetsRequest request, CallOptions options)

Lists all the ODB Subnets in a given ODB Network.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListOdbSubnetsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListOdbSubnetsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListOdbSubnetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListOdbSubnetsResponse)` | The call object.  
  
### ListOdbSubnetsAsync(ListOdbSubnetsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListOdbSubnetsResponse> ListOdbSubnetsAsync(ListOdbSubnetsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all the ODB Subnets in a given ODB Network.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListOdbSubnetsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListOdbSubnetsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListOdbSubnetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListOdbSubnetsResponse)` | The call object.  
  
### ListPluggableDatabases(ListPluggableDatabasesRequest, CallOptions)
    
    
    public virtual ListPluggableDatabasesResponse ListPluggableDatabases(ListPluggableDatabasesRequest request, CallOptions options)

Lists all the PluggableDatabases for the given project, location and Container Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListPluggableDatabasesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListPluggableDatabasesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListPluggableDatabasesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListPluggableDatabasesResponse)` | The response received from the server.  
  
### ListPluggableDatabases(ListPluggableDatabasesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListPluggableDatabasesResponse ListPluggableDatabases(ListPluggableDatabasesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all the PluggableDatabases for the given project, location and Container Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListPluggableDatabasesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListPluggableDatabasesRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListPluggableDatabasesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListPluggableDatabasesResponse)` | The response received from the server.  
  
### ListPluggableDatabasesAsync(ListPluggableDatabasesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListPluggableDatabasesResponse> ListPluggableDatabasesAsync(ListPluggableDatabasesRequest request, CallOptions options)

Lists all the PluggableDatabases for the given project, location and Container Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListPluggableDatabasesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListPluggableDatabasesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListPluggableDatabasesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListPluggableDatabasesResponse)` | The call object.  
  
### ListPluggableDatabasesAsync(ListPluggableDatabasesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListPluggableDatabasesResponse> ListPluggableDatabasesAsync(ListPluggableDatabasesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all the PluggableDatabases for the given project, location and Container Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListPluggableDatabasesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListPluggableDatabasesRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListPluggableDatabasesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListPluggableDatabasesResponse)` | The call object.  
  
### NewInstance(ClientBaseConfiguration)
    
    
    protected override OracleDatabase.OracleDatabaseClient NewInstance(ClientBase.ClientBaseConfiguration configuration)

Creates a new instance of client from given `ClientBaseConfiguration`.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.OracleDatabase)[OracleDatabaseClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.OracleDatabase.OracleDatabaseClient)` |   
**Overrides**

Grpc.Core.ClientBase<Google.Cloud.OracleDatabase.V1.OracleDatabase.OracleDatabaseClient>.NewInstance(Grpc.Core.ClientBase.ClientBaseConfiguration)

### RefreshAutonomousDatabase(RefreshAutonomousDatabaseRequest, CallOptions)
    
    
    public virtual Operation RefreshAutonomousDatabase(RefreshAutonomousDatabaseRequest request, CallOptions options)

Refreshes the refreshable clone of an Autonomous Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RefreshAutonomousDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.RefreshAutonomousDatabaseRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### RefreshAutonomousDatabase(RefreshAutonomousDatabaseRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation RefreshAutonomousDatabase(RefreshAutonomousDatabaseRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Refreshes the refreshable clone of an Autonomous Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RefreshAutonomousDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.RefreshAutonomousDatabaseRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### RefreshAutonomousDatabaseAsync(RefreshAutonomousDatabaseRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> RefreshAutonomousDatabaseAsync(RefreshAutonomousDatabaseRequest request, CallOptions options)

Refreshes the refreshable clone of an Autonomous Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RefreshAutonomousDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.RefreshAutonomousDatabaseRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### RefreshAutonomousDatabaseAsync(RefreshAutonomousDatabaseRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> RefreshAutonomousDatabaseAsync(RefreshAutonomousDatabaseRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Refreshes the refreshable clone of an Autonomous Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RefreshAutonomousDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.RefreshAutonomousDatabaseRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### RemoveVirtualMachineExadbVmCluster(RemoveVirtualMachineExadbVmClusterRequest, CallOptions)
    
    
    public virtual Operation RemoveVirtualMachineExadbVmCluster(RemoveVirtualMachineExadbVmClusterRequest request, CallOptions options)

Removes virtual machines from an existing exadb vm cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemoveVirtualMachineExadbVmClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.RemoveVirtualMachineExadbVmClusterRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### RemoveVirtualMachineExadbVmCluster(RemoveVirtualMachineExadbVmClusterRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation RemoveVirtualMachineExadbVmCluster(RemoveVirtualMachineExadbVmClusterRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Removes virtual machines from an existing exadb vm cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemoveVirtualMachineExadbVmClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.RemoveVirtualMachineExadbVmClusterRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### RemoveVirtualMachineExadbVmClusterAsync(RemoveVirtualMachineExadbVmClusterRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> RemoveVirtualMachineExadbVmClusterAsync(RemoveVirtualMachineExadbVmClusterRequest request, CallOptions options)

Removes virtual machines from an existing exadb vm cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemoveVirtualMachineExadbVmClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.RemoveVirtualMachineExadbVmClusterRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### RemoveVirtualMachineExadbVmClusterAsync(RemoveVirtualMachineExadbVmClusterRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> RemoveVirtualMachineExadbVmClusterAsync(RemoveVirtualMachineExadbVmClusterRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Removes virtual machines from an existing exadb vm cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemoveVirtualMachineExadbVmClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.RemoveVirtualMachineExadbVmClusterRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### RestartAutonomousDatabase(RestartAutonomousDatabaseRequest, CallOptions)
    
    
    public virtual Operation RestartAutonomousDatabase(RestartAutonomousDatabaseRequest request, CallOptions options)

Restarts an Autonomous Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RestartAutonomousDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.RestartAutonomousDatabaseRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### RestartAutonomousDatabase(RestartAutonomousDatabaseRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation RestartAutonomousDatabase(RestartAutonomousDatabaseRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Restarts an Autonomous Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RestartAutonomousDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.RestartAutonomousDatabaseRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### RestartAutonomousDatabaseAsync(RestartAutonomousDatabaseRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> RestartAutonomousDatabaseAsync(RestartAutonomousDatabaseRequest request, CallOptions options)

Restarts an Autonomous Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RestartAutonomousDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.RestartAutonomousDatabaseRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### RestartAutonomousDatabaseAsync(RestartAutonomousDatabaseRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> RestartAutonomousDatabaseAsync(RestartAutonomousDatabaseRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Restarts an Autonomous Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RestartAutonomousDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.RestartAutonomousDatabaseRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### RestoreAutonomousDatabase(RestoreAutonomousDatabaseRequest, CallOptions)
    
    
    public virtual Operation RestoreAutonomousDatabase(RestoreAutonomousDatabaseRequest request, CallOptions options)

Restores a single Autonomous Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RestoreAutonomousDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.RestoreAutonomousDatabaseRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### RestoreAutonomousDatabase(RestoreAutonomousDatabaseRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation RestoreAutonomousDatabase(RestoreAutonomousDatabaseRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Restores a single Autonomous Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RestoreAutonomousDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.RestoreAutonomousDatabaseRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### RestoreAutonomousDatabaseAsync(RestoreAutonomousDatabaseRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> RestoreAutonomousDatabaseAsync(RestoreAutonomousDatabaseRequest request, CallOptions options)

Restores a single Autonomous Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RestoreAutonomousDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.RestoreAutonomousDatabaseRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### RestoreAutonomousDatabaseAsync(RestoreAutonomousDatabaseRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> RestoreAutonomousDatabaseAsync(RestoreAutonomousDatabaseRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Restores a single Autonomous Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RestoreAutonomousDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.RestoreAutonomousDatabaseRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### StartAutonomousDatabase(StartAutonomousDatabaseRequest, CallOptions)
    
    
    public virtual Operation StartAutonomousDatabase(StartAutonomousDatabaseRequest request, CallOptions options)

Starts an Autonomous Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StartAutonomousDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.StartAutonomousDatabaseRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### StartAutonomousDatabase(StartAutonomousDatabaseRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation StartAutonomousDatabase(StartAutonomousDatabaseRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Starts an Autonomous Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StartAutonomousDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.StartAutonomousDatabaseRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### StartAutonomousDatabaseAsync(StartAutonomousDatabaseRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> StartAutonomousDatabaseAsync(StartAutonomousDatabaseRequest request, CallOptions options)

Starts an Autonomous Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StartAutonomousDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.StartAutonomousDatabaseRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### StartAutonomousDatabaseAsync(StartAutonomousDatabaseRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> StartAutonomousDatabaseAsync(StartAutonomousDatabaseRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Starts an Autonomous Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StartAutonomousDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.StartAutonomousDatabaseRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### StartGoldengateDeployment(StartGoldengateDeploymentRequest, CallOptions)
    
    
    public virtual Operation StartGoldengateDeployment(StartGoldengateDeploymentRequest request, CallOptions options)

Starts a single GoldengateDeployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StartGoldengateDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.StartGoldengateDeploymentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### StartGoldengateDeployment(StartGoldengateDeploymentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation StartGoldengateDeployment(StartGoldengateDeploymentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Starts a single GoldengateDeployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StartGoldengateDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.StartGoldengateDeploymentRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### StartGoldengateDeploymentAsync(StartGoldengateDeploymentRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> StartGoldengateDeploymentAsync(StartGoldengateDeploymentRequest request, CallOptions options)

Starts a single GoldengateDeployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StartGoldengateDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.StartGoldengateDeploymentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### StartGoldengateDeploymentAsync(StartGoldengateDeploymentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> StartGoldengateDeploymentAsync(StartGoldengateDeploymentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Starts a single GoldengateDeployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StartGoldengateDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.StartGoldengateDeploymentRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### StopAutonomousDatabase(StopAutonomousDatabaseRequest, CallOptions)
    
    
    public virtual Operation StopAutonomousDatabase(StopAutonomousDatabaseRequest request, CallOptions options)

Stops an Autonomous Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StopAutonomousDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.StopAutonomousDatabaseRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### StopAutonomousDatabase(StopAutonomousDatabaseRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation StopAutonomousDatabase(StopAutonomousDatabaseRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Stops an Autonomous Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StopAutonomousDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.StopAutonomousDatabaseRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### StopAutonomousDatabaseAsync(StopAutonomousDatabaseRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> StopAutonomousDatabaseAsync(StopAutonomousDatabaseRequest request, CallOptions options)

Stops an Autonomous Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StopAutonomousDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.StopAutonomousDatabaseRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### StopAutonomousDatabaseAsync(StopAutonomousDatabaseRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> StopAutonomousDatabaseAsync(StopAutonomousDatabaseRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Stops an Autonomous Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StopAutonomousDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.StopAutonomousDatabaseRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### StopGoldengateDeployment(StopGoldengateDeploymentRequest, CallOptions)
    
    
    public virtual Operation StopGoldengateDeployment(StopGoldengateDeploymentRequest request, CallOptions options)

Stops a single GoldengateDeployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StopGoldengateDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.StopGoldengateDeploymentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### StopGoldengateDeployment(StopGoldengateDeploymentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation StopGoldengateDeployment(StopGoldengateDeploymentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Stops a single GoldengateDeployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StopGoldengateDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.StopGoldengateDeploymentRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### StopGoldengateDeploymentAsync(StopGoldengateDeploymentRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> StopGoldengateDeploymentAsync(StopGoldengateDeploymentRequest request, CallOptions options)

Stops a single GoldengateDeployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StopGoldengateDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.StopGoldengateDeploymentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### StopGoldengateDeploymentAsync(StopGoldengateDeploymentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> StopGoldengateDeploymentAsync(StopGoldengateDeploymentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Stops a single GoldengateDeployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StopGoldengateDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.StopGoldengateDeploymentRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### SwitchoverAutonomousDatabase(SwitchoverAutonomousDatabaseRequest, CallOptions)
    
    
    public virtual Operation SwitchoverAutonomousDatabase(SwitchoverAutonomousDatabaseRequest request, CallOptions options)

Initiates a switchover of specified autonomous database to the associated peer database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SwitchoverAutonomousDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.SwitchoverAutonomousDatabaseRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### SwitchoverAutonomousDatabase(SwitchoverAutonomousDatabaseRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation SwitchoverAutonomousDatabase(SwitchoverAutonomousDatabaseRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Initiates a switchover of specified autonomous database to the associated peer database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SwitchoverAutonomousDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.SwitchoverAutonomousDatabaseRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### SwitchoverAutonomousDatabaseAsync(SwitchoverAutonomousDatabaseRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> SwitchoverAutonomousDatabaseAsync(SwitchoverAutonomousDatabaseRequest request, CallOptions options)

Initiates a switchover of specified autonomous database to the associated peer database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SwitchoverAutonomousDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.SwitchoverAutonomousDatabaseRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### SwitchoverAutonomousDatabaseAsync(SwitchoverAutonomousDatabaseRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> SwitchoverAutonomousDatabaseAsync(SwitchoverAutonomousDatabaseRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Initiates a switchover of specified autonomous database to the associated peer database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SwitchoverAutonomousDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.SwitchoverAutonomousDatabaseRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### TestGoldengateConnectionAssignment(TestGoldengateConnectionAssignmentRequest, CallOptions)
    
    
    public virtual TestGoldengateConnectionAssignmentResponse TestGoldengateConnectionAssignment(TestGoldengateConnectionAssignmentRequest request, CallOptions options)

Tests a single GoldengateConnectionAssignment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TestGoldengateConnectionAssignmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.TestGoldengateConnectionAssignmentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[TestGoldengateConnectionAssignmentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.TestGoldengateConnectionAssignmentResponse)` | The response received from the server.  
  
### TestGoldengateConnectionAssignment(TestGoldengateConnectionAssignmentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual TestGoldengateConnectionAssignmentResponse TestGoldengateConnectionAssignment(TestGoldengateConnectionAssignmentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Tests a single GoldengateConnectionAssignment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TestGoldengateConnectionAssignmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.TestGoldengateConnectionAssignmentRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[TestGoldengateConnectionAssignmentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.TestGoldengateConnectionAssignmentResponse)` | The response received from the server.  
  
### TestGoldengateConnectionAssignmentAsync(TestGoldengateConnectionAssignmentRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<TestGoldengateConnectionAssignmentResponse> TestGoldengateConnectionAssignmentAsync(TestGoldengateConnectionAssignmentRequest request, CallOptions options)

Tests a single GoldengateConnectionAssignment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TestGoldengateConnectionAssignmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.TestGoldengateConnectionAssignmentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[TestGoldengateConnectionAssignmentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.TestGoldengateConnectionAssignmentResponse)` | The call object.  
  
### TestGoldengateConnectionAssignmentAsync(TestGoldengateConnectionAssignmentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<TestGoldengateConnectionAssignmentResponse> TestGoldengateConnectionAssignmentAsync(TestGoldengateConnectionAssignmentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Tests a single GoldengateConnectionAssignment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TestGoldengateConnectionAssignmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.TestGoldengateConnectionAssignmentRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[TestGoldengateConnectionAssignmentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.TestGoldengateConnectionAssignmentResponse)` | The call object.  
  
### UpdateAutonomousDatabase(UpdateAutonomousDatabaseRequest, CallOptions)
    
    
    public virtual Operation UpdateAutonomousDatabase(UpdateAutonomousDatabaseRequest request, CallOptions options)

Updates the parameters of a single Autonomous Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAutonomousDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.UpdateAutonomousDatabaseRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### UpdateAutonomousDatabase(UpdateAutonomousDatabaseRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation UpdateAutonomousDatabase(UpdateAutonomousDatabaseRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the parameters of a single Autonomous Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAutonomousDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.UpdateAutonomousDatabaseRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### UpdateAutonomousDatabaseAsync(UpdateAutonomousDatabaseRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateAutonomousDatabaseAsync(UpdateAutonomousDatabaseRequest request, CallOptions options)

Updates the parameters of a single Autonomous Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAutonomousDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.UpdateAutonomousDatabaseRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### UpdateAutonomousDatabaseAsync(UpdateAutonomousDatabaseRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateAutonomousDatabaseAsync(UpdateAutonomousDatabaseRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the parameters of a single Autonomous Database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAutonomousDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.UpdateAutonomousDatabaseRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### UpdateExadbVmCluster(UpdateExadbVmClusterRequest, CallOptions)
    
    
    public virtual Operation UpdateExadbVmCluster(UpdateExadbVmClusterRequest request, CallOptions options)

Updates a single Exadb (Exascale) VM Cluster. To add virtual machines to existing exadb vm cluster, only pass the node count.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateExadbVmClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.UpdateExadbVmClusterRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### UpdateExadbVmCluster(UpdateExadbVmClusterRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation UpdateExadbVmCluster(UpdateExadbVmClusterRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates a single Exadb (Exascale) VM Cluster. To add virtual machines to existing exadb vm cluster, only pass the node count.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateExadbVmClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.UpdateExadbVmClusterRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### UpdateExadbVmClusterAsync(UpdateExadbVmClusterRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateExadbVmClusterAsync(UpdateExadbVmClusterRequest request, CallOptions options)

Updates a single Exadb (Exascale) VM Cluster. To add virtual machines to existing exadb vm cluster, only pass the node count.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateExadbVmClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.UpdateExadbVmClusterRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### UpdateExadbVmClusterAsync(UpdateExadbVmClusterRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateExadbVmClusterAsync(UpdateExadbVmClusterRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates a single Exadb (Exascale) VM Cluster. To add virtual machines to existing exadb vm cluster, only pass the node count.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateExadbVmClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.UpdateExadbVmClusterRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-18 UTC."],[],[]] 
