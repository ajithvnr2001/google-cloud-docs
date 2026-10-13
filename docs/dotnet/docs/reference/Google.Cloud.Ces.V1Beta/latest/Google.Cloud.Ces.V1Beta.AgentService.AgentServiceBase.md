---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentService.AgentServiceBase
title: Gemini Enterprise for Customer Experience v1beta API - Class AgentService.AgentServiceBase (1.0.0-beta09) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:39:45.403064+00:00
---

# Gemini Enterprise for Customer Experience v1beta API - Class AgentService.AgentServiceBase (1.0.0-beta09)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentService.AgentServiceBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Gemini Enterprise for Customer Experience v1beta API - Class AgentService.AgentServiceBase (1.0.0-beta09) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta09 (latest)  1.0.0-beta08 
    
    
    [BindServiceMethod(typeof(AgentService), "BindService")]
    public abstract class AgentService.AgentServiceBase

Reference documentation and code samples for the Gemini Enterprise for Customer Experience v1beta API class AgentService.AgentServiceBase.

Base class for server-side implementations of AgentService

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AgentService.AgentServiceBase

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Ces.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta)

## Assembly

Google.Cloud.Ces.V1Beta.dll

## Methods 

### BatchDeleteConversations(BatchDeleteConversationsRequest, ServerCallContext)
    
    
    public virtual Task<Operation> BatchDeleteConversations(BatchDeleteConversationsRequest request, ServerCallContext context)

Batch deletes the specified conversations.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchDeleteConversationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.BatchDeleteConversationsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### CreateAgent(CreateAgentRequest, ServerCallContext)
    
    
    public virtual Task<Agent> CreateAgent(CreateAgentRequest request, ServerCallContext context)

Creates a new agent in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateAgentRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)` | The response to send back to the client (wrapped by a task).  
  
### CreateApp(CreateAppRequest, ServerCallContext)
    
    
    public virtual Task<Operation> CreateApp(CreateAppRequest request, ServerCallContext context)

Creates a new app in the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateAppRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### CreateAppVersion(CreateAppVersionRequest, ServerCallContext)
    
    
    public virtual Task<AppVersion> CreateAppVersion(CreateAppVersionRequest request, ServerCallContext context)

Creates a new app version in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAppVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateAppVersionRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)` | The response to send back to the client (wrapped by a task).  
  
### CreateDeployment(CreateDeploymentRequest, ServerCallContext)
    
    
    public virtual Task<Deployment> CreateDeployment(CreateDeploymentRequest request, ServerCallContext context)

Creates a new deployment in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateDeploymentRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)` | The response to send back to the client (wrapped by a task).  
  
### CreateExample(CreateExampleRequest, ServerCallContext)
    
    
    public virtual Task<Example> CreateExample(CreateExampleRequest request, ServerCallContext context)

Creates a new example in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateExampleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateExampleRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)` | The response to send back to the client (wrapped by a task).  
  
### CreateGuardrail(CreateGuardrailRequest, ServerCallContext)
    
    
    public virtual Task<Guardrail> CreateGuardrail(CreateGuardrailRequest request, ServerCallContext context)

Creates a new guardrail in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateGuardrailRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateGuardrailRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)` | The response to send back to the client (wrapped by a task).  
  
### CreateTool(CreateToolRequest, ServerCallContext)
    
    
    public virtual Task<Tool> CreateTool(CreateToolRequest request, ServerCallContext context)

Creates a new tool in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateToolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateToolRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` | The response to send back to the client (wrapped by a task).  
  
### CreateToolset(CreateToolsetRequest, ServerCallContext)
    
    
    public virtual Task<Toolset> CreateToolset(CreateToolsetRequest request, ServerCallContext context)

Creates a new toolset in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateToolsetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateToolsetRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)` | The response to send back to the client (wrapped by a task).  
  
### DeleteAgent(DeleteAgentRequest, ServerCallContext)
    
    
    public virtual Task<Empty> DeleteAgent(DeleteAgentRequest request, ServerCallContext context)

Deletes the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteAgentRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response to send back to the client (wrapped by a task).  
  
### DeleteApp(DeleteAppRequest, ServerCallContext)
    
    
    public virtual Task<Operation> DeleteApp(DeleteAppRequest request, ServerCallContext context)

Deletes the specified app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteAppRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### DeleteAppVersion(DeleteAppVersionRequest, ServerCallContext)
    
    
    public virtual Task<Empty> DeleteAppVersion(DeleteAppVersionRequest request, ServerCallContext context)

Deletes the specified app version.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAppVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteAppVersionRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response to send back to the client (wrapped by a task).  
  
### DeleteConversation(DeleteConversationRequest, ServerCallContext)
    
    
    public virtual Task<Empty> DeleteConversation(DeleteConversationRequest request, ServerCallContext context)

Deletes the specified conversation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteConversationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteConversationRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response to send back to the client (wrapped by a task).  
  
### DeleteDeployment(DeleteDeploymentRequest, ServerCallContext)
    
    
    public virtual Task<Empty> DeleteDeployment(DeleteDeploymentRequest request, ServerCallContext context)

Deletes the specified deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteDeploymentRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response to send back to the client (wrapped by a task).  
  
### DeleteExample(DeleteExampleRequest, ServerCallContext)
    
    
    public virtual Task<Empty> DeleteExample(DeleteExampleRequest request, ServerCallContext context)

Deletes the specified example.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteExampleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteExampleRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response to send back to the client (wrapped by a task).  
  
### DeleteGuardrail(DeleteGuardrailRequest, ServerCallContext)
    
    
    public virtual Task<Empty> DeleteGuardrail(DeleteGuardrailRequest request, ServerCallContext context)

Deletes the specified guardrail.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteGuardrailRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteGuardrailRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response to send back to the client (wrapped by a task).  
  
### DeleteTool(DeleteToolRequest, ServerCallContext)
    
    
    public virtual Task<Empty> DeleteTool(DeleteToolRequest request, ServerCallContext context)

Deletes the specified tool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteToolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteToolRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response to send back to the client (wrapped by a task).  
  
### DeleteToolset(DeleteToolsetRequest, ServerCallContext)
    
    
    public virtual Task<Empty> DeleteToolset(DeleteToolsetRequest request, ServerCallContext context)

Deletes the specified toolset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteToolsetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteToolsetRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response to send back to the client (wrapped by a task).  
  
### ExportApp(ExportAppRequest, ServerCallContext)
    
    
    public virtual Task<Operation> ExportApp(ExportAppRequest request, ServerCallContext context)

Exports the specified app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExportAppRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### GenerateAppResource(GenerateAppResourceRequest, ServerCallContext)
    
    
    public virtual Task<Operation> GenerateAppResource(GenerateAppResourceRequest request, ServerCallContext context)

Generates specific resources (e.g. agent) in the app using LLM assistant.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateAppResourceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### GetAgent(GetAgentRequest, ServerCallContext)
    
    
    public virtual Task<Agent> GetAgent(GetAgentRequest request, ServerCallContext context)

Gets details of the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetAgentRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)` | The response to send back to the client (wrapped by a task).  
  
### GetApp(GetAppRequest, ServerCallContext)
    
    
    public virtual Task<App> GetApp(GetAppRequest request, ServerCallContext context)

Gets details of the specified app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetAppRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)` | The response to send back to the client (wrapped by a task).  
  
### GetAppVersion(GetAppVersionRequest, ServerCallContext)
    
    
    public virtual Task<AppVersion> GetAppVersion(GetAppVersionRequest request, ServerCallContext context)

Gets details of the specified app version.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAppVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetAppVersionRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)` | The response to send back to the client (wrapped by a task).  
  
### GetChangelog(GetChangelogRequest, ServerCallContext)
    
    
    public virtual Task<Changelog> GetChangelog(GetChangelogRequest request, ServerCallContext context)

Gets the specified changelog.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetChangelogRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetChangelogRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Changelog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Changelog)` | The response to send back to the client (wrapped by a task).  
  
### GetConversation(GetConversationRequest, ServerCallContext)
    
    
    public virtual Task<Conversation> GetConversation(GetConversationRequest request, ServerCallContext context)

Gets details of the specified conversation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetConversationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetConversationRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation)` | The response to send back to the client (wrapped by a task).  
  
### GetDeployment(GetDeploymentRequest, ServerCallContext)
    
    
    public virtual Task<Deployment> GetDeployment(GetDeploymentRequest request, ServerCallContext context)

Gets details of the specified deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetDeploymentRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)` | The response to send back to the client (wrapped by a task).  
  
### GetExample(GetExampleRequest, ServerCallContext)
    
    
    public virtual Task<Example> GetExample(GetExampleRequest request, ServerCallContext context)

Gets details of the specified example.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetExampleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetExampleRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)` | The response to send back to the client (wrapped by a task).  
  
### GetGuardrail(GetGuardrailRequest, ServerCallContext)
    
    
    public virtual Task<Guardrail> GetGuardrail(GetGuardrailRequest request, ServerCallContext context)

Gets details of the specified guardrail.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGuardrailRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetGuardrailRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)` | The response to send back to the client (wrapped by a task).  
  
### GetSecuritySettings(GetSecuritySettingsRequest, ServerCallContext)
    
    
    public virtual Task<SecuritySettings> GetSecuritySettings(GetSecuritySettingsRequest request, ServerCallContext context)

Retrieves the security settings for the project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSecuritySettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetSecuritySettingsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SecuritySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SecuritySettings)` | The response to send back to the client (wrapped by a task).  
  
### GetTool(GetToolRequest, ServerCallContext)
    
    
    public virtual Task<Tool> GetTool(GetToolRequest request, ServerCallContext context)

Gets details of the specified tool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetToolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetToolRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` | The response to send back to the client (wrapped by a task).  
  
### GetToolset(GetToolsetRequest, ServerCallContext)
    
    
    public virtual Task<Toolset> GetToolset(GetToolsetRequest request, ServerCallContext context)

Gets details of the specified toolset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetToolsetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetToolsetRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)` | The response to send back to the client (wrapped by a task).  
  
### ImportApp(ImportAppRequest, ServerCallContext)
    
    
    public virtual Task<Operation> ImportApp(ImportAppRequest request, ServerCallContext context)

Imports the specified app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ImportAppRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### ListAgents(ListAgentsRequest, ServerCallContext)
    
    
    public virtual Task<ListAgentsResponse> ListAgents(ListAgentsRequest request, ServerCallContext context)

Lists agents in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAgentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAgentsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListAgentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAgentsResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListAppVersions(ListAppVersionsRequest, ServerCallContext)
    
    
    public virtual Task<ListAppVersionsResponse> ListAppVersions(ListAppVersionsRequest request, ServerCallContext context)

Lists all app versions in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAppVersionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAppVersionsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListAppVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAppVersionsResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListApps(ListAppsRequest, ServerCallContext)
    
    
    public virtual Task<ListAppsResponse> ListApps(ListAppsRequest request, ServerCallContext context)

Lists apps in the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAppsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAppsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListAppsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAppsResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListChangelogs(ListChangelogsRequest, ServerCallContext)
    
    
    public virtual Task<ListChangelogsResponse> ListChangelogs(ListChangelogsRequest request, ServerCallContext context)

Lists the changelogs of the specified app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListChangelogsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListChangelogsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListChangelogsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListChangelogsResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListConversations(ListConversationsRequest, ServerCallContext)
    
    
    public virtual Task<ListConversationsResponse> ListConversations(ListConversationsRequest request, ServerCallContext context)

Lists conversations in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListConversationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListConversationsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListConversationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListConversationsResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListDeployments(ListDeploymentsRequest, ServerCallContext)
    
    
    public virtual Task<ListDeploymentsResponse> ListDeployments(ListDeploymentsRequest request, ServerCallContext context)

Lists deployments in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDeploymentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListDeploymentsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListDeploymentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListDeploymentsResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListExamples(ListExamplesRequest, ServerCallContext)
    
    
    public virtual Task<ListExamplesResponse> ListExamples(ListExamplesRequest request, ServerCallContext context)

Lists examples in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListExamplesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListExamplesRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListExamplesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListExamplesResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListGuardrails(ListGuardrailsRequest, ServerCallContext)
    
    
    public virtual Task<ListGuardrailsResponse> ListGuardrails(ListGuardrailsRequest request, ServerCallContext context)

Lists guardrails in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGuardrailsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListGuardrailsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListGuardrailsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListGuardrailsResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListTools(ListToolsRequest, ServerCallContext)
    
    
    public virtual Task<ListToolsResponse> ListTools(ListToolsRequest request, ServerCallContext context)

Lists tools in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListToolsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListToolsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListToolsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListToolsResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListToolsets(ListToolsetsRequest, ServerCallContext)
    
    
    public virtual Task<ListToolsetsResponse> ListToolsets(ListToolsetsRequest request, ServerCallContext context)

Lists toolsets in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListToolsetsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListToolsetsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListToolsetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListToolsetsResponse)` | The response to send back to the client (wrapped by a task).  
  
### RestoreAppVersion(RestoreAppVersionRequest, ServerCallContext)
    
    
    public virtual Task<Operation> RestoreAppVersion(RestoreAppVersionRequest request, ServerCallContext context)

Restores the specified app version. This will create a new app version from the current draft app and overwrite the current draft with the specified app version.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RestoreAppVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.RestoreAppVersionRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### UpdateAgent(UpdateAgentRequest, ServerCallContext)
    
    
    public virtual Task<Agent> UpdateAgent(UpdateAgentRequest request, ServerCallContext context)

Updates the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateAgentRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)` | The response to send back to the client (wrapped by a task).  
  
### UpdateApp(UpdateAppRequest, ServerCallContext)
    
    
    public virtual Task<App> UpdateApp(UpdateAppRequest request, ServerCallContext context)

Updates the specified app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateAppRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)` | The response to send back to the client (wrapped by a task).  
  
### UpdateDeployment(UpdateDeploymentRequest, ServerCallContext)
    
    
    public virtual Task<Deployment> UpdateDeployment(UpdateDeploymentRequest request, ServerCallContext context)

Updates the specified deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateDeploymentRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)` | The response to send back to the client (wrapped by a task).  
  
### UpdateExample(UpdateExampleRequest, ServerCallContext)
    
    
    public virtual Task<Example> UpdateExample(UpdateExampleRequest request, ServerCallContext context)

Updates the specified example.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateExampleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateExampleRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)` | The response to send back to the client (wrapped by a task).  
  
### UpdateGuardrail(UpdateGuardrailRequest, ServerCallContext)
    
    
    public virtual Task<Guardrail> UpdateGuardrail(UpdateGuardrailRequest request, ServerCallContext context)

Updates the specified guardrail.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateGuardrailRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateGuardrailRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)` | The response to send back to the client (wrapped by a task).  
  
### UpdateSecuritySettings(UpdateSecuritySettingsRequest, ServerCallContext)
    
    
    public virtual Task<SecuritySettings> UpdateSecuritySettings(UpdateSecuritySettingsRequest request, ServerCallContext context)

Updates the security settings for the project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSecuritySettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateSecuritySettingsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SecuritySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SecuritySettings)` | The response to send back to the client (wrapped by a task).  
  
### UpdateTool(UpdateToolRequest, ServerCallContext)
    
    
    public virtual Task<Tool> UpdateTool(UpdateToolRequest request, ServerCallContext context)

Updates the specified tool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateToolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateToolRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` | The response to send back to the client (wrapped by a task).  
  
### UpdateToolset(UpdateToolsetRequest, ServerCallContext)
    
    
    public virtual Task<Toolset> UpdateToolset(UpdateToolsetRequest request, ServerCallContext context)

Updates the specified toolset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateToolsetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateToolsetRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
