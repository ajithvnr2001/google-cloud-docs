---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafkaConnect.ManagedKafkaConnectBase
title: Managed Service for Apache Kafka API v1 API - Class ManagedKafkaConnect.ManagedKafkaConnectBase (1.0.0-beta08) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:06:49.004776+00:00
---

# Managed Service for Apache Kafka API v1 API - Class ManagedKafkaConnect.ManagedKafkaConnectBase (1.0.0-beta08)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafkaConnect.ManagedKafkaConnectBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Managed Service for Apache Kafka API v1 API - Class ManagedKafkaConnect.ManagedKafkaConnectBase (1.0.0-beta08) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.0.0-beta08 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafkaConnect.ManagedKafkaConnectBase)
  * [ 1.0.0-beta07 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/1.0.0-beta07/Google.Cloud.ManagedKafka.V1.ManagedKafkaConnect.ManagedKafkaConnectBase)


    
    
    [BindServiceMethod(typeof(ManagedKafkaConnect), "BindService")]
    public abstract class ManagedKafkaConnect.ManagedKafkaConnectBase

Reference documentation and code samples for the Managed Service for Apache Kafka API v1 API class ManagedKafkaConnect.ManagedKafkaConnectBase.

Base class for server-side implementations of ManagedKafkaConnect

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ManagedKafkaConnect.ManagedKafkaConnectBase

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ManagedKafka.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1)

## Assembly

Google.Cloud.ManagedKafka.V1.dll

## Methods 

### CreateConnectCluster(CreateConnectClusterRequest, ServerCallContext)
    
    
    public virtual Task<Operation> CreateConnectCluster(CreateConnectClusterRequest request, ServerCallContext context)

Creates a new Kafka Connect cluster in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateConnectClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.CreateConnectClusterRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### CreateConnector(CreateConnectorRequest, ServerCallContext)
    
    
    public virtual Task<Connector> CreateConnector(CreateConnectorRequest request, ServerCallContext context)

Creates a new connector in a given Connect cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateConnectorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.CreateConnectorRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector)` | The response to send back to the client (wrapped by a task).  
  
### DeleteConnectCluster(DeleteConnectClusterRequest, ServerCallContext)
    
    
    public virtual Task<Operation> DeleteConnectCluster(DeleteConnectClusterRequest request, ServerCallContext context)

Deletes a single Connect cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteConnectClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.DeleteConnectClusterRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### DeleteConnector(DeleteConnectorRequest, ServerCallContext)
    
    
    public virtual Task<Empty> DeleteConnector(DeleteConnectorRequest request, ServerCallContext context)

Deletes a connector.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteConnectorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.DeleteConnectorRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response to send back to the client (wrapped by a task).  
  
### GetConnectCluster(GetConnectClusterRequest, ServerCallContext)
    
    
    public virtual Task<ConnectCluster> GetConnectCluster(GetConnectClusterRequest request, ServerCallContext context)

Returns the properties of a single Kafka Connect cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetConnectClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.GetConnectClusterRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ConnectCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectCluster)` | The response to send back to the client (wrapped by a task).  
  
### GetConnector(GetConnectorRequest, ServerCallContext)
    
    
    public virtual Task<Connector> GetConnector(GetConnectorRequest request, ServerCallContext context)

Returns the properties of a single connector.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetConnectorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.GetConnectorRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector)` | The response to send back to the client (wrapped by a task).  
  
### ListConnectClusters(ListConnectClustersRequest, ServerCallContext)
    
    
    public virtual Task<ListConnectClustersResponse> ListConnectClusters(ListConnectClustersRequest request, ServerCallContext context)

Lists the Kafka Connect clusters in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListConnectClustersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListConnectClustersRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListConnectClustersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListConnectClustersResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListConnectors(ListConnectorsRequest, ServerCallContext)
    
    
    public virtual Task<ListConnectorsResponse> ListConnectors(ListConnectorsRequest request, ServerCallContext context)

Lists the connectors in a given Connect cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListConnectorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListConnectorsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListConnectorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListConnectorsResponse)` | The response to send back to the client (wrapped by a task).  
  
### PauseConnector(PauseConnectorRequest, ServerCallContext)
    
    
    public virtual Task<PauseConnectorResponse> PauseConnector(PauseConnectorRequest request, ServerCallContext context)

Pauses the connector and its tasks.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PauseConnectorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.PauseConnectorRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PauseConnectorResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.PauseConnectorResponse)` | The response to send back to the client (wrapped by a task).  
  
### RestartConnector(RestartConnectorRequest, ServerCallContext)
    
    
    public virtual Task<RestartConnectorResponse> RestartConnector(RestartConnectorRequest request, ServerCallContext context)

Restarts the connector.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RestartConnectorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.RestartConnectorRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[RestartConnectorResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.RestartConnectorResponse)` | The response to send back to the client (wrapped by a task).  
  
### ResumeConnector(ResumeConnectorRequest, ServerCallContext)
    
    
    public virtual Task<ResumeConnectorResponse> ResumeConnector(ResumeConnectorRequest request, ServerCallContext context)

Resumes the connector and its tasks.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ResumeConnectorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ResumeConnectorRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ResumeConnectorResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ResumeConnectorResponse)` | The response to send back to the client (wrapped by a task).  
  
### StopConnector(StopConnectorRequest, ServerCallContext)
    
    
    public virtual Task<StopConnectorResponse> StopConnector(StopConnectorRequest request, ServerCallContext context)

Stops the connector.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StopConnectorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.StopConnectorRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[StopConnectorResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.StopConnectorResponse)` | The response to send back to the client (wrapped by a task).  
  
### UpdateConnectCluster(UpdateConnectClusterRequest, ServerCallContext)
    
    
    public virtual Task<Operation> UpdateConnectCluster(UpdateConnectClusterRequest request, ServerCallContext context)

Updates the properties of a single Kafka Connect cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateConnectClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.UpdateConnectClusterRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### UpdateConnector(UpdateConnectorRequest, ServerCallContext)
    
    
    public virtual Task<Connector> UpdateConnector(UpdateConnectorRequest request, ServerCallContext context)

Updates the properties of a connector.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateConnectorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.UpdateConnectorRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
