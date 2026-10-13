---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.AgentServiceGrpc.AgentServiceFutureStub
title: Class AgentServiceGrpc.AgentServiceFutureStub (0.15.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:05:02.661064+00:00
---

# Class AgentServiceGrpc.AgentServiceFutureStub (0.15.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.AgentServiceGrpc.AgentServiceFutureStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class AgentServiceGrpc.AgentServiceFutureStub (0.15.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.0 (latest)  0.11.0  0.10.0  0.9.0  0.7.0  0.4.0  0.3.0  0.1.0 
    
    
    public static final class AgentServiceGrpc.AgentServiceFutureStub extends AbstractFutureStub<AgentServiceGrpc.AgentServiceFutureStub>

A stub to allow clients to do ListenableFuture-style rpc calls to service AgentService.

The service that manages agent-related resources in Gemini Enterprise for Customer Engagement (CES).

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractFutureStub > AgentServiceGrpc.AgentServiceFutureStub

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

### batchDeleteConversations(BatchDeleteConversationsRequest request)
    
    
    public ListenableFuture<Operation> batchDeleteConversations(BatchDeleteConversationsRequest request)

Batch deletes the specified conversations.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchDeleteConversationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.BatchDeleteConversationsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### build(Channel channel, CallOptions callOptions)
    
    
    protected AgentServiceGrpc.AgentServiceFutureStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[AgentServiceGrpc.AgentServiceFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.AgentServiceGrpc.AgentServiceFutureStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createAgent(CreateAgentRequest request)
    
    
    public ListenableFuture<Agent> createAgent(CreateAgentRequest request)

Creates a new agent in the given app.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.CreateAgentRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.Agent)>` |   
  
### createApp(CreateAppRequest request)
    
    
    public ListenableFuture<Operation> createApp(CreateAppRequest request)

Creates a new app in the given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateAppRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.CreateAppRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createAppVersion(CreateAppVersionRequest request)
    
    
    public ListenableFuture<AppVersion> createAppVersion(CreateAppVersionRequest request)

Creates a new app version in the given app.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateAppVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.CreateAppVersionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[AppVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.AppVersion)>` |   
  
### createDeployment(CreateDeploymentRequest request)
    
    
    public ListenableFuture<Deployment> createDeployment(CreateDeploymentRequest request)

Creates a new deployment in the given app.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.CreateDeploymentRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Deployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.Deployment)>` |   
  
### createExample(CreateExampleRequest request)
    
    
    public ListenableFuture<Example> createExample(CreateExampleRequest request)

Creates a new example in the given app.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateExampleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.CreateExampleRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Example](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.Example)>` |   
  
### createGuardrail(CreateGuardrailRequest request)
    
    
    public ListenableFuture<Guardrail> createGuardrail(CreateGuardrailRequest request)

Creates a new guardrail in the given app.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateGuardrailRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.CreateGuardrailRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Guardrail](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.Guardrail)>` |   
  
### createTool(CreateToolRequest request)
    
    
    public ListenableFuture<Tool> createTool(CreateToolRequest request)

Creates a new tool in the given app.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateToolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.CreateToolRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Tool](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.Tool)>` |   
  
### createToolset(CreateToolsetRequest request)
    
    
    public ListenableFuture<Toolset> createToolset(CreateToolsetRequest request)

Creates a new toolset in the given app.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateToolsetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.CreateToolsetRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Toolset](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.Toolset)>` |   
  
### deleteAgent(DeleteAgentRequest request)
    
    
    public ListenableFuture<Empty> deleteAgent(DeleteAgentRequest request)

Deletes the specified agent.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.DeleteAgentRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteApp(DeleteAppRequest request)
    
    
    public ListenableFuture<Operation> deleteApp(DeleteAppRequest request)

Deletes the specified app.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteAppRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.DeleteAppRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteAppVersion(DeleteAppVersionRequest request)
    
    
    public ListenableFuture<Empty> deleteAppVersion(DeleteAppVersionRequest request)

Deletes the specified app version.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteAppVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.DeleteAppVersionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteConversation(DeleteConversationRequest request)
    
    
    public ListenableFuture<Empty> deleteConversation(DeleteConversationRequest request)

Deletes the specified conversation.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteConversationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.DeleteConversationRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteDeployment(DeleteDeploymentRequest request)
    
    
    public ListenableFuture<Empty> deleteDeployment(DeleteDeploymentRequest request)

Deletes the specified deployment.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.DeleteDeploymentRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteExample(DeleteExampleRequest request)
    
    
    public ListenableFuture<Empty> deleteExample(DeleteExampleRequest request)

Deletes the specified example.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteExampleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.DeleteExampleRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteGuardrail(DeleteGuardrailRequest request)
    
    
    public ListenableFuture<Empty> deleteGuardrail(DeleteGuardrailRequest request)

Deletes the specified guardrail.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteGuardrailRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.DeleteGuardrailRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteTool(DeleteToolRequest request)
    
    
    public ListenableFuture<Empty> deleteTool(DeleteToolRequest request)

Deletes the specified tool.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteToolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.DeleteToolRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteToolset(DeleteToolsetRequest request)
    
    
    public ListenableFuture<Empty> deleteToolset(DeleteToolsetRequest request)

Deletes the specified toolset.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteToolsetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.DeleteToolsetRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### exportApp(ExportAppRequest request)
    
    
    public ListenableFuture<Operation> exportApp(ExportAppRequest request)

Exports the specified app.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ExportAppRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.ExportAppRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getAgent(GetAgentRequest request)
    
    
    public ListenableFuture<Agent> getAgent(GetAgentRequest request)

Gets details of the specified agent.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.GetAgentRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.Agent)>` |   
  
### getApp(GetAppRequest request)
    
    
    public ListenableFuture<App> getApp(GetAppRequest request)

Gets details of the specified app.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAppRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.GetAppRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[App](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.App)>` |   
  
### getAppVersion(GetAppVersionRequest request)
    
    
    public ListenableFuture<AppVersion> getAppVersion(GetAppVersionRequest request)

Gets details of the specified app version.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAppVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.GetAppVersionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[AppVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.AppVersion)>` |   
  
### getChangelog(GetChangelogRequest request)
    
    
    public ListenableFuture<Changelog> getChangelog(GetChangelogRequest request)

Gets the specified changelog.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetChangelogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.GetChangelogRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Changelog](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.Changelog)>` |   
  
### getConversation(GetConversationRequest request)
    
    
    public ListenableFuture<Conversation> getConversation(GetConversationRequest request)

Gets details of the specified conversation.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetConversationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.GetConversationRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Conversation](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.Conversation)>` |   
  
### getDeployment(GetDeploymentRequest request)
    
    
    public ListenableFuture<Deployment> getDeployment(GetDeploymentRequest request)

Gets details of the specified deployment.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.GetDeploymentRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Deployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.Deployment)>` |   
  
### getExample(GetExampleRequest request)
    
    
    public ListenableFuture<Example> getExample(GetExampleRequest request)

Gets details of the specified example.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetExampleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.GetExampleRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Example](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.Example)>` |   
  
### getGuardrail(GetGuardrailRequest request)
    
    
    public ListenableFuture<Guardrail> getGuardrail(GetGuardrailRequest request)

Gets details of the specified guardrail.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetGuardrailRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.GetGuardrailRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Guardrail](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.Guardrail)>` |   
  
### getTool(GetToolRequest request)
    
    
    public ListenableFuture<Tool> getTool(GetToolRequest request)

Gets details of the specified tool.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetToolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.GetToolRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Tool](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.Tool)>` |   
  
### getToolset(GetToolsetRequest request)
    
    
    public ListenableFuture<Toolset> getToolset(GetToolsetRequest request)

Gets details of the specified toolset.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetToolsetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.GetToolsetRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Toolset](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.Toolset)>` |   
  
### importApp(ImportAppRequest request)
    
    
    public ListenableFuture<Operation> importApp(ImportAppRequest request)

Imports the specified app.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ImportAppRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.ImportAppRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### listAgents(ListAgentsRequest request)
    
    
    public ListenableFuture<ListAgentsResponse> listAgents(ListAgentsRequest request)

Lists agents in the given app.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAgentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.ListAgentsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListAgentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.ListAgentsResponse)>` |   
  
### listAppVersions(ListAppVersionsRequest request)
    
    
    public ListenableFuture<ListAppVersionsResponse> listAppVersions(ListAppVersionsRequest request)

Lists all app versions in the given app.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAppVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.ListAppVersionsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListAppVersionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.ListAppVersionsResponse)>` |   
  
### listApps(ListAppsRequest request)
    
    
    public ListenableFuture<ListAppsResponse> listApps(ListAppsRequest request)

Lists apps in the given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAppsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.ListAppsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListAppsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.ListAppsResponse)>` |   
  
### listChangelogs(ListChangelogsRequest request)
    
    
    public ListenableFuture<ListChangelogsResponse> listChangelogs(ListChangelogsRequest request)

Lists the changelogs of the specified app.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListChangelogsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.ListChangelogsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListChangelogsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.ListChangelogsResponse)>` |   
  
### listConversations(ListConversationsRequest request)
    
    
    public ListenableFuture<ListConversationsResponse> listConversations(ListConversationsRequest request)

Lists conversations in the given app.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListConversationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.ListConversationsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListConversationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.ListConversationsResponse)>` |   
  
### listDeployments(ListDeploymentsRequest request)
    
    
    public ListenableFuture<ListDeploymentsResponse> listDeployments(ListDeploymentsRequest request)

Lists deployments in the given app.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDeploymentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.ListDeploymentsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListDeploymentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.ListDeploymentsResponse)>` |   
  
### listExamples(ListExamplesRequest request)
    
    
    public ListenableFuture<ListExamplesResponse> listExamples(ListExamplesRequest request)

Lists examples in the given app.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListExamplesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.ListExamplesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListExamplesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.ListExamplesResponse)>` |   
  
### listGuardrails(ListGuardrailsRequest request)
    
    
    public ListenableFuture<ListGuardrailsResponse> listGuardrails(ListGuardrailsRequest request)

Lists guardrails in the given app.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListGuardrailsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.ListGuardrailsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListGuardrailsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.ListGuardrailsResponse)>` |   
  
### listTools(ListToolsRequest request)
    
    
    public ListenableFuture<ListToolsResponse> listTools(ListToolsRequest request)

Lists tools in the given app.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListToolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.ListToolsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListToolsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.ListToolsResponse)>` |   
  
### listToolsets(ListToolsetsRequest request)
    
    
    public ListenableFuture<ListToolsetsResponse> listToolsets(ListToolsetsRequest request)

Lists toolsets in the given app.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListToolsetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.ListToolsetsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListToolsetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.ListToolsetsResponse)>` |   
  
### restoreAppVersion(RestoreAppVersionRequest request)
    
    
    public ListenableFuture<Operation> restoreAppVersion(RestoreAppVersionRequest request)

Restores the specified app version. This will create a new app version from the current draft app and overwrite the current draft with the specified app version.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RestoreAppVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.RestoreAppVersionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateAgent(UpdateAgentRequest request)
    
    
    public ListenableFuture<Agent> updateAgent(UpdateAgentRequest request)

Updates the specified agent.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.UpdateAgentRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.Agent)>` |   
  
### updateApp(UpdateAppRequest request)
    
    
    public ListenableFuture<App> updateApp(UpdateAppRequest request)

Updates the specified app.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateAppRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.UpdateAppRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[App](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.App)>` |   
  
### updateDeployment(UpdateDeploymentRequest request)
    
    
    public ListenableFuture<Deployment> updateDeployment(UpdateDeploymentRequest request)

Updates the specified deployment.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.UpdateDeploymentRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Deployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.Deployment)>` |   
  
### updateExample(UpdateExampleRequest request)
    
    
    public ListenableFuture<Example> updateExample(UpdateExampleRequest request)

Updates the specified example.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateExampleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.UpdateExampleRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Example](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.Example)>` |   
  
### updateGuardrail(UpdateGuardrailRequest request)
    
    
    public ListenableFuture<Guardrail> updateGuardrail(UpdateGuardrailRequest request)

Updates the specified guardrail.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateGuardrailRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.UpdateGuardrailRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Guardrail](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.Guardrail)>` |   
  
### updateTool(UpdateToolRequest request)
    
    
    public ListenableFuture<Tool> updateTool(UpdateToolRequest request)

Updates the specified tool.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateToolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.UpdateToolRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Tool](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.Tool)>` |   
  
### updateToolset(UpdateToolsetRequest request)
    
    
    public ListenableFuture<Toolset> updateToolset(UpdateToolsetRequest request)

Updates the specified toolset.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateToolsetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.UpdateToolsetRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Toolset](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.Toolset)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
