---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AgentServiceClient
title: Class AgentServiceClient (0.15.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:55:55.308207+00:00
---

# Class AgentServiceClient (0.15.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AgentServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class AgentServiceClient (0.15.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.0 (latest)  0.11.0  0.10.0  0.9.0  0.7.0  0.4.0  0.3.0  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-ces/google-cloud-ces/src/main/java/com/google/cloud/ces/v1beta/AgentServiceClient.java)| [Product Reference](https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps)| [RPC Documentation](https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/reference/rpc)  
---|---|---  
  
Service Description: The service that manages agent-related resources in Gemini Enterprise for Customer Engagement (CES).

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       AppName name = AppName.of("[PROJECT]", "[LOCATION]", "[APP]");
       App response = agentServiceClient.getApp(name);
     }
     

Note: close() needs to be called on the AgentServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListApps |  Lists apps in the given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listApps(ListAppsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listApps(LocationName parent) 
  * listApps(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listAppsPagedCallable() 
  * listAppsCallable() 

  
GetApp |  Gets details of the specified app. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getApp(GetAppRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getApp(AppName name) 
  * getApp(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getAppCallable() 

  
CreateApp |  Creates a new app in the given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createAppAsync(CreateAppRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createAppAsync(LocationName parent, App app) 
  * createAppAsync(String parent, App app) 
  * createAppAsync(LocationName parent, App app, String appId) 
  * createAppAsync(String parent, App app, String appId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createAppOperationCallable() 
  * createAppCallable() 

  
UpdateApp |  Updates the specified app. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateApp(UpdateAppRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateApp(App app, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateAppCallable() 

  
DeleteApp |  Deletes the specified app. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAppAsync(DeleteAppRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAppAsync(AppName name) 
  * deleteAppAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteAppOperationCallable() 
  * deleteAppCallable() 

  
ExportApp |  Exports the specified app. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * exportAppAsync(ExportAppRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * exportAppAsync(AppName name) 
  * exportAppAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * exportAppOperationCallable() 
  * exportAppCallable() 

  
ImportApp |  Imports the specified app. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * importAppAsync(ImportAppRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * importAppAsync(LocationName parent, String displayName, String appId) 
  * importAppAsync(String parent, String displayName, String appId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * importAppOperationCallable() 
  * importAppCallable() 

  
GetSecuritySettings |  Retrieves the security settings for the project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getSecuritySettings(GetSecuritySettingsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getSecuritySettings(SecuritySettingsName name) 
  * getSecuritySettings(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getSecuritySettingsCallable() 

  
UpdateSecuritySettings |  Updates the security settings for the project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateSecuritySettings(UpdateSecuritySettingsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateSecuritySettings(SecuritySettings securitySettings, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateSecuritySettingsCallable() 

  
ListAgents |  Lists agents in the given app. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listAgents(ListAgentsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listAgents(AppName parent) 
  * listAgents(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listAgentsPagedCallable() 
  * listAgentsCallable() 

  
GetAgent |  Gets details of the specified agent. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getAgent(GetAgentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getAgent(AgentName name) 
  * getAgent(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getAgentCallable() 

  
CreateAgent |  Creates a new agent in the given app. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createAgent(CreateAgentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createAgent(AppName parent, Agent agent) 
  * createAgent(String parent, Agent agent) 
  * createAgent(AppName parent, Agent agent, String agentId) 
  * createAgent(String parent, Agent agent, String agentId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createAgentCallable() 

  
UpdateAgent |  Updates the specified agent. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateAgent(UpdateAgentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateAgent(Agent agent, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateAgentCallable() 

  
DeleteAgent |  Deletes the specified agent. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAgent(DeleteAgentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteAgent(AgentName name) 
  * deleteAgent(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteAgentCallable() 

  
ListExamples |  Lists examples in the given app. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listExamples(ListExamplesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listExamples(AppName parent) 
  * listExamples(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listExamplesPagedCallable() 
  * listExamplesCallable() 

  
GetExample |  Gets details of the specified example. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getExample(GetExampleRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getExample(ExampleName name) 
  * getExample(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getExampleCallable() 

  
CreateExample |  Creates a new example in the given app. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createExample(CreateExampleRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createExample(AppName parent, Example example) 
  * createExample(String parent, Example example) 
  * createExample(AppName parent, Example example, String exampleId) 
  * createExample(String parent, Example example, String exampleId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createExampleCallable() 

  
UpdateExample |  Updates the specified example. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateExample(UpdateExampleRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateExample(Example example, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateExampleCallable() 

  
DeleteExample |  Deletes the specified example. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteExample(DeleteExampleRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteExample(ExampleName name) 
  * deleteExample(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteExampleCallable() 

  
ListTools |  Lists tools in the given app. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listTools(ListToolsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listTools(AppName parent) 
  * listTools(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listToolsPagedCallable() 
  * listToolsCallable() 

  
GetTool |  Gets details of the specified tool. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getTool(GetToolRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getTool(ToolName name) 
  * getTool(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getToolCallable() 

  
ListConversations |  Lists conversations in the given app. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listConversations(ListConversationsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listConversations(AppName parent) 
  * listConversations(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listConversationsPagedCallable() 
  * listConversationsCallable() 

  
GetConversation |  Gets details of the specified conversation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getConversation(GetConversationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getConversation(ConversationName name) 
  * getConversation(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getConversationCallable() 

  
DeleteConversation |  Deletes the specified conversation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteConversation(DeleteConversationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteConversation(ConversationName name) 
  * deleteConversation(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteConversationCallable() 

  
BatchDeleteConversations |  Batch deletes the specified conversations. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchDeleteConversationsAsync(BatchDeleteConversationsRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * batchDeleteConversationsAsync(AppName parent) 
  * batchDeleteConversationsAsync(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchDeleteConversationsOperationCallable() 
  * batchDeleteConversationsCallable() 

  
CreateTool |  Creates a new tool in the given app. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createTool(CreateToolRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createTool(AppName parent, Tool tool) 
  * createTool(String parent, Tool tool) 
  * createTool(AppName parent, Tool tool, String toolId) 
  * createTool(String parent, Tool tool, String toolId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createToolCallable() 

  
UpdateTool |  Updates the specified tool. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateTool(UpdateToolRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateTool(Tool tool, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateToolCallable() 

  
DeleteTool |  Deletes the specified tool. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteTool(DeleteToolRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteTool(ToolName name) 
  * deleteTool(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteToolCallable() 

  
ListGuardrails |  Lists guardrails in the given app. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listGuardrails(ListGuardrailsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listGuardrails(AppName parent) 
  * listGuardrails(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listGuardrailsPagedCallable() 
  * listGuardrailsCallable() 

  
GetGuardrail |  Gets details of the specified guardrail. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getGuardrail(GetGuardrailRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getGuardrail(GuardrailName name) 
  * getGuardrail(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getGuardrailCallable() 

  
CreateGuardrail |  Creates a new guardrail in the given app. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createGuardrail(CreateGuardrailRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createGuardrail(AppName parent, Guardrail guardrail) 
  * createGuardrail(String parent, Guardrail guardrail) 
  * createGuardrail(AppName parent, Guardrail guardrail, String guardrailId) 
  * createGuardrail(String parent, Guardrail guardrail, String guardrailId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createGuardrailCallable() 

  
UpdateGuardrail |  Updates the specified guardrail. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateGuardrail(UpdateGuardrailRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateGuardrail(Guardrail guardrail, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateGuardrailCallable() 

  
DeleteGuardrail |  Deletes the specified guardrail. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteGuardrail(DeleteGuardrailRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteGuardrail(GuardrailName name) 
  * deleteGuardrail(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteGuardrailCallable() 

  
ListDeployments |  Lists deployments in the given app. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listDeployments(ListDeploymentsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listDeployments(AppName parent) 
  * listDeployments(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listDeploymentsPagedCallable() 
  * listDeploymentsCallable() 

  
GetDeployment |  Gets details of the specified deployment. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getDeployment(GetDeploymentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getDeployment(DeploymentName name) 
  * getDeployment(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getDeploymentCallable() 

  
CreateDeployment |  Creates a new deployment in the given app. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createDeployment(CreateDeploymentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createDeployment(AppName parent, Deployment deployment) 
  * createDeployment(String parent, Deployment deployment) 
  * createDeployment(AppName parent, Deployment deployment, String deploymentId) 
  * createDeployment(String parent, Deployment deployment, String deploymentId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createDeploymentCallable() 

  
UpdateDeployment |  Updates the specified deployment. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateDeployment(UpdateDeploymentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateDeployment(Deployment deployment, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateDeploymentCallable() 

  
DeleteDeployment |  Deletes the specified deployment. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteDeployment(DeleteDeploymentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteDeployment(DeploymentName name) 
  * deleteDeployment(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteDeploymentCallable() 

  
ListToolsets |  Lists toolsets in the given app. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listToolsets(ListToolsetsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listToolsets(AppName parent) 
  * listToolsets(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listToolsetsPagedCallable() 
  * listToolsetsCallable() 

  
GetToolset |  Gets details of the specified toolset. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getToolset(GetToolsetRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getToolset(ToolsetName name) 
  * getToolset(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getToolsetCallable() 

  
CreateToolset |  Creates a new toolset in the given app. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createToolset(CreateToolsetRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createToolset(AppName parent, Toolset toolset) 
  * createToolset(String parent, Toolset toolset) 
  * createToolset(AppName parent, Toolset toolset, String toolsetId) 
  * createToolset(String parent, Toolset toolset, String toolsetId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createToolsetCallable() 

  
UpdateToolset |  Updates the specified toolset. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateToolset(UpdateToolsetRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateToolset(Toolset toolset, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateToolsetCallable() 

  
DeleteToolset |  Deletes the specified toolset. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteToolset(DeleteToolsetRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteToolset(ToolsetName name) 
  * deleteToolset(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteToolsetCallable() 

  
ListAppVersions |  Lists all app versions in the given app. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listAppVersions(ListAppVersionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listAppVersions(AppName parent) 
  * listAppVersions(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listAppVersionsPagedCallable() 
  * listAppVersionsCallable() 

  
GetAppVersion |  Gets details of the specified app version. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getAppVersion(GetAppVersionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getAppVersion(AppVersionName name) 
  * getAppVersion(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getAppVersionCallable() 

  
CreateAppVersion |  Creates a new app version in the given app. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createAppVersion(CreateAppVersionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createAppVersion(AppName parent, AppVersion appVersion) 
  * createAppVersion(String parent, AppVersion appVersion) 
  * createAppVersion(AppName parent, AppVersion appVersion, String appVersionId) 
  * createAppVersion(String parent, AppVersion appVersion, String appVersionId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createAppVersionCallable() 

  
DeleteAppVersion |  Deletes the specified app version. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAppVersion(DeleteAppVersionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteAppVersion(AppVersionName name) 
  * deleteAppVersion(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteAppVersionCallable() 

  
RestoreAppVersion |  Restores the specified app version. This will create a new app version from the current draft app and overwrite the current draft with the specified app version. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * restoreAppVersionAsync(RestoreAppVersionRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * restoreAppVersionAsync(AppVersionName name) 
  * restoreAppVersionAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * restoreAppVersionOperationCallable() 
  * restoreAppVersionCallable() 

  
GenerateAppResource |  Generates specific resources (e.g. agent) in the app using LLM assistant. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * generateAppResourceAsync(GenerateAppResourceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * generateAppResourceAsync(AppName parent) 
  * generateAppResourceAsync(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * generateAppResourceOperationCallable() 
  * generateAppResourceCallable() 

  
ListChangelogs |  Lists the changelogs of the specified app. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listChangelogs(ListChangelogsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listChangelogs(AppName parent) 
  * listChangelogs(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listChangelogsPagedCallable() 
  * listChangelogsCallable() 

  
GetChangelog |  Gets the specified changelog. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getChangelog(GetChangelogRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getChangelog(ChangelogName name) 
  * getChangelog(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getChangelogCallable() 

  
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

This class can be customized by passing in a custom instance of AgentServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AgentServiceSettings agentServiceSettings =
         AgentServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     AgentServiceClient agentServiceClient = AgentServiceClient.create(agentServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AgentServiceSettings agentServiceSettings =
         AgentServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     AgentServiceClient agentServiceClient = AgentServiceClient.create(agentServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AgentServiceSettings agentServiceSettings = AgentServiceSettings.newHttpJsonBuilder().build();
     AgentServiceClient agentServiceClient = AgentServiceClient.create(agentServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > AgentServiceClient

## Static Methods 

### create()
    
    
    public static final AgentServiceClient create()

Constructs an instance of AgentServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[AgentServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AgentServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(AgentServiceSettings settings)
    
    
    public static final AgentServiceClient create(AgentServiceSettings settings)

Constructs an instance of AgentServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[AgentServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AgentServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AgentServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AgentServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(AgentServiceStub stub)
    
    
    public static final AgentServiceClient create(AgentServiceStub stub)

Constructs an instance of AgentServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(AgentServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[AgentServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.stub.AgentServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AgentServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AgentServiceClient)` |   
  
## Constructors 

### AgentServiceClient(AgentServiceSettings settings)
    
    
    protected AgentServiceClient(AgentServiceSettings settings)

Constructs an instance of AgentServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[AgentServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AgentServiceSettings)`  
  
  
### AgentServiceClient(AgentServiceStub stub)
    
    
    protected AgentServiceClient(AgentServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[AgentServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.stub.AgentServiceStub)`  
  
  
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
  
### batchDeleteConversationsAsync(@Nullable AppName parent)
    
    
    public final OperationFuture<BatchDeleteConversationsResponse,OperationMetadata> batchDeleteConversationsAsync(@Nullable AppName parent)

Batch deletes the specified conversations.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       AppName parent = AppName.of("[PROJECT]", "[LOCATION]", "[APP]");
       BatchDeleteConversationsResponse response =
           agentServiceClient.batchDeleteConversationsAsync(parent).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.AppName`  
Required. The resource name of the app to delete conversations from. Format: `projects/{project}/locations/{location}/apps/{app}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BatchDeleteConversationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.BatchDeleteConversationsResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.OperationMetadata)>` |   
  
### batchDeleteConversationsAsync(BatchDeleteConversationsRequest request)
    
    
    public final OperationFuture<BatchDeleteConversationsResponse,OperationMetadata> batchDeleteConversationsAsync(BatchDeleteConversationsRequest request)

Batch deletes the specified conversations.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       BatchDeleteConversationsRequest request =
           BatchDeleteConversationsRequest.newBuilder()
               .setParent(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .addAllConversations(new ArrayList<String>())
               .build();
       BatchDeleteConversationsResponse response =
           agentServiceClient.batchDeleteConversationsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchDeleteConversationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.BatchDeleteConversationsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BatchDeleteConversationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.BatchDeleteConversationsResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.OperationMetadata)>` |   
  
### batchDeleteConversationsAsync(String parent)
    
    
    public final OperationFuture<BatchDeleteConversationsResponse,OperationMetadata> batchDeleteConversationsAsync(String parent)

Batch deletes the specified conversations.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       String parent = AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString();
       BatchDeleteConversationsResponse response =
           agentServiceClient.batchDeleteConversationsAsync(parent).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the app to delete conversations from. Format: `projects/{project}/locations/{location}/apps/{app}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BatchDeleteConversationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.BatchDeleteConversationsResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.OperationMetadata)>` |   
  
### batchDeleteConversationsCallable()
    
    
    public final UnaryCallable<BatchDeleteConversationsRequest,Operation> batchDeleteConversationsCallable()

Batch deletes the specified conversations.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       BatchDeleteConversationsRequest request =
           BatchDeleteConversationsRequest.newBuilder()
               .setParent(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .addAllConversations(new ArrayList<String>())
               .build();
       ApiFuture<Operation> future =
           agentServiceClient.batchDeleteConversationsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchDeleteConversationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.BatchDeleteConversationsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### batchDeleteConversationsOperationCallable()
    
    
    public final OperationCallable<BatchDeleteConversationsRequest,BatchDeleteConversationsResponse,OperationMetadata> batchDeleteConversationsOperationCallable()

Batch deletes the specified conversations.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       BatchDeleteConversationsRequest request =
           BatchDeleteConversationsRequest.newBuilder()
               .setParent(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .addAllConversations(new ArrayList<String>())
               .build();
       OperationFuture<BatchDeleteConversationsResponse, OperationMetadata> future =
           agentServiceClient.batchDeleteConversationsOperationCallable().futureCall(request);
       // Do something.
       BatchDeleteConversationsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[BatchDeleteConversationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.BatchDeleteConversationsRequest),[BatchDeleteConversationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.BatchDeleteConversationsResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.OperationMetadata)>` |   
  
### close()
    
    
    public final void close()

### createAgent(@Nullable AppName parent, Agent agent)
    
    
    public final Agent createAgent(@Nullable AppName parent, Agent agent)

Creates a new agent in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       AppName parent = AppName.of("[PROJECT]", "[LOCATION]", "[APP]");
       Agent agent = Agent.newBuilder().build();
       Agent response = agentServiceClient.createAgent(parent, agent);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.AppName`  
Required. The resource name of the app to create an agent in.  
`agent` | `[Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Agent)`  
Required. The agent to create.  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Agent)` |   
  
### createAgent(@Nullable AppName parent, Agent agent, String agentId)
    
    
    public final Agent createAgent(@Nullable AppName parent, Agent agent, String agentId)

Creates a new agent in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       AppName parent = AppName.of("[PROJECT]", "[LOCATION]", "[APP]");
       Agent agent = Agent.newBuilder().build();
       String agentId = "agentId-1060987136";
       Agent response = agentServiceClient.createAgent(parent, agent, agentId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.AppName`  
Required. The resource name of the app to create an agent in.  
`agent` | `[Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Agent)`  
Required. The agent to create.  
`agentId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The ID to use for the agent, which will become the final component of the agent's resource name. If not provided, a unique ID will be automatically assigned for the agent.  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Agent)` |   
  
### createAgent(CreateAgentRequest request)
    
    
    public final Agent createAgent(CreateAgentRequest request)

Creates a new agent in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       CreateAgentRequest request =
           CreateAgentRequest.newBuilder()
               .setParent(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .setAgentId("agentId-1060987136")
               .setAgent(Agent.newBuilder().build())
               .build();
       Agent response = agentServiceClient.createAgent(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.CreateAgentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Agent)` |   
  
### createAgent(String parent, Agent agent)
    
    
    public final Agent createAgent(String parent, Agent agent)

Creates a new agent in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       String parent = AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString();
       Agent agent = Agent.newBuilder().build();
       Agent response = agentServiceClient.createAgent(parent, agent);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the app to create an agent in.  
`agent` | `[Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Agent)`  
Required. The agent to create.  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Agent)` |   
  
### createAgent(String parent, Agent agent, String agentId)
    
    
    public final Agent createAgent(String parent, Agent agent, String agentId)

Creates a new agent in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       String parent = AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString();
       Agent agent = Agent.newBuilder().build();
       String agentId = "agentId-1060987136";
       Agent response = agentServiceClient.createAgent(parent, agent, agentId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the app to create an agent in.  
`agent` | `[Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Agent)`  
Required. The agent to create.  
`agentId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The ID to use for the agent, which will become the final component of the agent's resource name. If not provided, a unique ID will be automatically assigned for the agent.  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Agent)` |   
  
### createAgentCallable()
    
    
    public final UnaryCallable<CreateAgentRequest,Agent> createAgentCallable()

Creates a new agent in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       CreateAgentRequest request =
           CreateAgentRequest.newBuilder()
               .setParent(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .setAgentId("agentId-1060987136")
               .setAgent(Agent.newBuilder().build())
               .build();
       ApiFuture<Agent> future = agentServiceClient.createAgentCallable().futureCall(request);
       // Do something.
       Agent response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.CreateAgentRequest),[Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Agent)>` |   
  
### createAppAsync(@Nullable LocationName parent, App app)
    
    
    public final OperationFuture<App,OperationMetadata> createAppAsync(@Nullable LocationName parent, App app)

Creates a new app in the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       App app = App.newBuilder().build();
       App response = agentServiceClient.createAppAsync(parent, app).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.LocationName`  
Required. The resource name of the location to create an app in.  
`app` | `[App](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.App)`  
Required. The app to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[App](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.App),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.OperationMetadata)>` |   
  
### createAppAsync(@Nullable LocationName parent, App app, String appId)
    
    
    public final OperationFuture<App,OperationMetadata> createAppAsync(@Nullable LocationName parent, App app, String appId)

Creates a new app in the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       App app = App.newBuilder().build();
       String appId = "appId93028124";
       App response = agentServiceClient.createAppAsync(parent, app, appId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.LocationName`  
Required. The resource name of the location to create an app in.  
`app` | `[App](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.App)`  
Required. The app to create.  
`appId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The ID to use for the app, which will become the final component of the app's resource name. If not provided, a unique ID will be automatically assigned for the app.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[App](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.App),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.OperationMetadata)>` |   
  
### createAppAsync(CreateAppRequest request)
    
    
    public final OperationFuture<App,OperationMetadata> createAppAsync(CreateAppRequest request)

Creates a new app in the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       CreateAppRequest request =
           CreateAppRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setAppId("appId93028124")
               .setApp(App.newBuilder().build())
               .build();
       App response = agentServiceClient.createAppAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateAppRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.CreateAppRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[App](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.App),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.OperationMetadata)>` |   
  
### createAppAsync(String parent, App app)
    
    
    public final OperationFuture<App,OperationMetadata> createAppAsync(String parent, App app)

Creates a new app in the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       App app = App.newBuilder().build();
       App response = agentServiceClient.createAppAsync(parent, app).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the location to create an app in.  
`app` | `[App](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.App)`  
Required. The app to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[App](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.App),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.OperationMetadata)>` |   
  
### createAppAsync(String parent, App app, String appId)
    
    
    public final OperationFuture<App,OperationMetadata> createAppAsync(String parent, App app, String appId)

Creates a new app in the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       App app = App.newBuilder().build();
       String appId = "appId93028124";
       App response = agentServiceClient.createAppAsync(parent, app, appId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the location to create an app in.  
`app` | `[App](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.App)`  
Required. The app to create.  
`appId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The ID to use for the app, which will become the final component of the app's resource name. If not provided, a unique ID will be automatically assigned for the app.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[App](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.App),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.OperationMetadata)>` |   
  
### createAppCallable()
    
    
    public final UnaryCallable<CreateAppRequest,Operation> createAppCallable()

Creates a new app in the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       CreateAppRequest request =
           CreateAppRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setAppId("appId93028124")
               .setApp(App.newBuilder().build())
               .build();
       ApiFuture<Operation> future = agentServiceClient.createAppCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateAppRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.CreateAppRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createAppOperationCallable()
    
    
    public final OperationCallable<CreateAppRequest,App,OperationMetadata> createAppOperationCallable()

Creates a new app in the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       CreateAppRequest request =
           CreateAppRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setAppId("appId93028124")
               .setApp(App.newBuilder().build())
               .build();
       OperationFuture<App, OperationMetadata> future =
           agentServiceClient.createAppOperationCallable().futureCall(request);
       // Do something.
       App response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateAppRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.CreateAppRequest),[App](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.App),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.OperationMetadata)>` |   
  
### createAppVersion(@Nullable AppName parent, AppVersion appVersion)
    
    
    public final AppVersion createAppVersion(@Nullable AppName parent, AppVersion appVersion)

Creates a new app version in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       AppName parent = AppName.of("[PROJECT]", "[LOCATION]", "[APP]");
       AppVersion appVersion = AppVersion.newBuilder().build();
       AppVersion response = agentServiceClient.createAppVersion(parent, appVersion);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.AppName`  
Required. The resource name of the app to create an app version in.  
`appVersion` | `[AppVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AppVersion)`  
Required. The app version to create.  
**Returns**  
---  
**Type** | **Description**  
`[AppVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AppVersion)` |   
  
### createAppVersion(@Nullable AppName parent, AppVersion appVersion, String appVersionId)
    
    
    public final AppVersion createAppVersion(@Nullable AppName parent, AppVersion appVersion, String appVersionId)

Creates a new app version in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       AppName parent = AppName.of("[PROJECT]", "[LOCATION]", "[APP]");
       AppVersion appVersion = AppVersion.newBuilder().build();
       String appVersionId = "appVersionId303221490";
       AppVersion response = agentServiceClient.createAppVersion(parent, appVersion, appVersionId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.AppName`  
Required. The resource name of the app to create an app version in.  
`appVersion` | `[AppVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AppVersion)`  
Required. The app version to create.  
`appVersionId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The ID to use for the app version, which will become the final component of the app version's resource name. If not provided, a unique ID will be automatically assigned for the app version.  
**Returns**  
---  
**Type** | **Description**  
`[AppVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AppVersion)` |   
  
### createAppVersion(CreateAppVersionRequest request)
    
    
    public final AppVersion createAppVersion(CreateAppVersionRequest request)

Creates a new app version in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       CreateAppVersionRequest request =
           CreateAppVersionRequest.newBuilder()
               .setParent(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .setAppVersionId("appVersionId303221490")
               .setAppVersion(AppVersion.newBuilder().build())
               .build();
       AppVersion response = agentServiceClient.createAppVersion(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateAppVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.CreateAppVersionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AppVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AppVersion)` |   
  
### createAppVersion(String parent, AppVersion appVersion)
    
    
    public final AppVersion createAppVersion(String parent, AppVersion appVersion)

Creates a new app version in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       String parent = AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString();
       AppVersion appVersion = AppVersion.newBuilder().build();
       AppVersion response = agentServiceClient.createAppVersion(parent, appVersion);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the app to create an app version in.  
`appVersion` | `[AppVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AppVersion)`  
Required. The app version to create.  
**Returns**  
---  
**Type** | **Description**  
`[AppVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AppVersion)` |   
  
### createAppVersion(String parent, AppVersion appVersion, String appVersionId)
    
    
    public final AppVersion createAppVersion(String parent, AppVersion appVersion, String appVersionId)

Creates a new app version in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       String parent = AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString();
       AppVersion appVersion = AppVersion.newBuilder().build();
       String appVersionId = "appVersionId303221490";
       AppVersion response = agentServiceClient.createAppVersion(parent, appVersion, appVersionId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the app to create an app version in.  
`appVersion` | `[AppVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AppVersion)`  
Required. The app version to create.  
`appVersionId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The ID to use for the app version, which will become the final component of the app version's resource name. If not provided, a unique ID will be automatically assigned for the app version.  
**Returns**  
---  
**Type** | **Description**  
`[AppVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AppVersion)` |   
  
### createAppVersionCallable()
    
    
    public final UnaryCallable<CreateAppVersionRequest,AppVersion> createAppVersionCallable()

Creates a new app version in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       CreateAppVersionRequest request =
           CreateAppVersionRequest.newBuilder()
               .setParent(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .setAppVersionId("appVersionId303221490")
               .setAppVersion(AppVersion.newBuilder().build())
               .build();
       ApiFuture<AppVersion> future =
           agentServiceClient.createAppVersionCallable().futureCall(request);
       // Do something.
       AppVersion response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateAppVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.CreateAppVersionRequest),[AppVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AppVersion)>` |   
  
### createDeployment(@Nullable AppName parent, Deployment deployment)
    
    
    public final Deployment createDeployment(@Nullable AppName parent, Deployment deployment)

Creates a new deployment in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       AppName parent = AppName.of("[PROJECT]", "[LOCATION]", "[APP]");
       Deployment deployment = Deployment.newBuilder().build();
       Deployment response = agentServiceClient.createDeployment(parent, deployment);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.AppName`  
Required. The parent app. Format: `projects/{project}/locations/{location}/apps/{app}`  
`deployment` | `[Deployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Deployment)`  
Required. The deployment to create.  
**Returns**  
---  
**Type** | **Description**  
`[Deployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Deployment)` |   
  
### createDeployment(@Nullable AppName parent, Deployment deployment, String deploymentId)
    
    
    public final Deployment createDeployment(@Nullable AppName parent, Deployment deployment, String deploymentId)

Creates a new deployment in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       AppName parent = AppName.of("[PROJECT]", "[LOCATION]", "[APP]");
       Deployment deployment = Deployment.newBuilder().build();
       String deploymentId = "deploymentId-136894784";
       Deployment response = agentServiceClient.createDeployment(parent, deployment, deploymentId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.AppName`  
Required. The parent app. Format: `projects/{project}/locations/{location}/apps/{app}`  
`deployment` | `[Deployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Deployment)`  
Required. The deployment to create.  
`deploymentId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The ID to use for the deployment, which will become the final component of the deployment's resource name. If not provided, a unique ID will be automatically assigned for the deployment.  
**Returns**  
---  
**Type** | **Description**  
`[Deployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Deployment)` |   
  
### createDeployment(CreateDeploymentRequest request)
    
    
    public final Deployment createDeployment(CreateDeploymentRequest request)

Creates a new deployment in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       CreateDeploymentRequest request =
           CreateDeploymentRequest.newBuilder()
               .setParent(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .setDeploymentId("deploymentId-136894784")
               .setDeployment(Deployment.newBuilder().build())
               .build();
       Deployment response = agentServiceClient.createDeployment(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.CreateDeploymentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Deployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Deployment)` |   
  
### createDeployment(String parent, Deployment deployment)
    
    
    public final Deployment createDeployment(String parent, Deployment deployment)

Creates a new deployment in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       String parent = AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString();
       Deployment deployment = Deployment.newBuilder().build();
       Deployment response = agentServiceClient.createDeployment(parent, deployment);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent app. Format: `projects/{project}/locations/{location}/apps/{app}`  
`deployment` | `[Deployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Deployment)`  
Required. The deployment to create.  
**Returns**  
---  
**Type** | **Description**  
`[Deployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Deployment)` |   
  
### createDeployment(String parent, Deployment deployment, String deploymentId)
    
    
    public final Deployment createDeployment(String parent, Deployment deployment, String deploymentId)

Creates a new deployment in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       String parent = AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString();
       Deployment deployment = Deployment.newBuilder().build();
       String deploymentId = "deploymentId-136894784";
       Deployment response = agentServiceClient.createDeployment(parent, deployment, deploymentId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent app. Format: `projects/{project}/locations/{location}/apps/{app}`  
`deployment` | `[Deployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Deployment)`  
Required. The deployment to create.  
`deploymentId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The ID to use for the deployment, which will become the final component of the deployment's resource name. If not provided, a unique ID will be automatically assigned for the deployment.  
**Returns**  
---  
**Type** | **Description**  
`[Deployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Deployment)` |   
  
### createDeploymentCallable()
    
    
    public final UnaryCallable<CreateDeploymentRequest,Deployment> createDeploymentCallable()

Creates a new deployment in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       CreateDeploymentRequest request =
           CreateDeploymentRequest.newBuilder()
               .setParent(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .setDeploymentId("deploymentId-136894784")
               .setDeployment(Deployment.newBuilder().build())
               .build();
       ApiFuture<Deployment> future =
           agentServiceClient.createDeploymentCallable().futureCall(request);
       // Do something.
       Deployment response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.CreateDeploymentRequest),[Deployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Deployment)>` |   
  
### createExample(@Nullable AppName parent, Example example)
    
    
    public final Example createExample(@Nullable AppName parent, Example example)

Creates a new example in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       AppName parent = AppName.of("[PROJECT]", "[LOCATION]", "[APP]");
       Example example = Example.newBuilder().build();
       Example response = agentServiceClient.createExample(parent, example);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.AppName`  
Required. The resource name of the app to create an example in.  
`example` | `[Example](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Example)`  
Required. The example to create.  
**Returns**  
---  
**Type** | **Description**  
`[Example](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Example)` |   
  
### createExample(@Nullable AppName parent, Example example, String exampleId)
    
    
    public final Example createExample(@Nullable AppName parent, Example example, String exampleId)

Creates a new example in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       AppName parent = AppName.of("[PROJECT]", "[LOCATION]", "[APP]");
       Example example = Example.newBuilder().build();
       String exampleId = "exampleId-64591835";
       Example response = agentServiceClient.createExample(parent, example, exampleId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.AppName`  
Required. The resource name of the app to create an example in.  
`example` | `[Example](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Example)`  
Required. The example to create.  
`exampleId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The ID to use for the example, which will become the final component of the example's resource name. If not provided, a unique ID will be automatically assigned for the example.  
**Returns**  
---  
**Type** | **Description**  
`[Example](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Example)` |   
  
### createExample(CreateExampleRequest request)
    
    
    public final Example createExample(CreateExampleRequest request)

Creates a new example in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       CreateExampleRequest request =
           CreateExampleRequest.newBuilder()
               .setParent(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .setExampleId("exampleId-64591835")
               .setExample(Example.newBuilder().build())
               .build();
       Example response = agentServiceClient.createExample(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateExampleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.CreateExampleRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Example](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Example)` |   
  
### createExample(String parent, Example example)
    
    
    public final Example createExample(String parent, Example example)

Creates a new example in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       String parent = AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString();
       Example example = Example.newBuilder().build();
       Example response = agentServiceClient.createExample(parent, example);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the app to create an example in.  
`example` | `[Example](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Example)`  
Required. The example to create.  
**Returns**  
---  
**Type** | **Description**  
`[Example](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Example)` |   
  
### createExample(String parent, Example example, String exampleId)
    
    
    public final Example createExample(String parent, Example example, String exampleId)

Creates a new example in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       String parent = AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString();
       Example example = Example.newBuilder().build();
       String exampleId = "exampleId-64591835";
       Example response = agentServiceClient.createExample(parent, example, exampleId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the app to create an example in.  
`example` | `[Example](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Example)`  
Required. The example to create.  
`exampleId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The ID to use for the example, which will become the final component of the example's resource name. If not provided, a unique ID will be automatically assigned for the example.  
**Returns**  
---  
**Type** | **Description**  
`[Example](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Example)` |   
  
### createExampleCallable()
    
    
    public final UnaryCallable<CreateExampleRequest,Example> createExampleCallable()

Creates a new example in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       CreateExampleRequest request =
           CreateExampleRequest.newBuilder()
               .setParent(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .setExampleId("exampleId-64591835")
               .setExample(Example.newBuilder().build())
               .build();
       ApiFuture<Example> future = agentServiceClient.createExampleCallable().futureCall(request);
       // Do something.
       Example response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateExampleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.CreateExampleRequest),[Example](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Example)>` |   
  
### createGuardrail(@Nullable AppName parent, Guardrail guardrail)
    
    
    public final Guardrail createGuardrail(@Nullable AppName parent, Guardrail guardrail)

Creates a new guardrail in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       AppName parent = AppName.of("[PROJECT]", "[LOCATION]", "[APP]");
       Guardrail guardrail = Guardrail.newBuilder().build();
       Guardrail response = agentServiceClient.createGuardrail(parent, guardrail);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.AppName`  
Required. The resource name of the app to create a guardrail in.  
`guardrail` | `[Guardrail](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Guardrail)`  
Required. The guardrail to create.  
**Returns**  
---  
**Type** | **Description**  
`[Guardrail](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Guardrail)` |   
  
### createGuardrail(@Nullable AppName parent, Guardrail guardrail, String guardrailId)
    
    
    public final Guardrail createGuardrail(@Nullable AppName parent, Guardrail guardrail, String guardrailId)

Creates a new guardrail in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       AppName parent = AppName.of("[PROJECT]", "[LOCATION]", "[APP]");
       Guardrail guardrail = Guardrail.newBuilder().build();
       String guardrailId = "guardrailId1875412786";
       Guardrail response = agentServiceClient.createGuardrail(parent, guardrail, guardrailId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.AppName`  
Required. The resource name of the app to create a guardrail in.  
`guardrail` | `[Guardrail](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Guardrail)`  
Required. The guardrail to create.  
`guardrailId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The ID to use for the guardrail, which will become the final component of the guardrail's resource name. If not provided, a unique ID will be automatically assigned for the guardrail.  
**Returns**  
---  
**Type** | **Description**  
`[Guardrail](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Guardrail)` |   
  
### createGuardrail(CreateGuardrailRequest request)
    
    
    public final Guardrail createGuardrail(CreateGuardrailRequest request)

Creates a new guardrail in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       CreateGuardrailRequest request =
           CreateGuardrailRequest.newBuilder()
               .setParent(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .setGuardrailId("guardrailId1875412786")
               .setGuardrail(Guardrail.newBuilder().build())
               .build();
       Guardrail response = agentServiceClient.createGuardrail(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateGuardrailRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.CreateGuardrailRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Guardrail](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Guardrail)` |   
  
### createGuardrail(String parent, Guardrail guardrail)
    
    
    public final Guardrail createGuardrail(String parent, Guardrail guardrail)

Creates a new guardrail in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       String parent = AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString();
       Guardrail guardrail = Guardrail.newBuilder().build();
       Guardrail response = agentServiceClient.createGuardrail(parent, guardrail);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the app to create a guardrail in.  
`guardrail` | `[Guardrail](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Guardrail)`  
Required. The guardrail to create.  
**Returns**  
---  
**Type** | **Description**  
`[Guardrail](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Guardrail)` |   
  
### createGuardrail(String parent, Guardrail guardrail, String guardrailId)
    
    
    public final Guardrail createGuardrail(String parent, Guardrail guardrail, String guardrailId)

Creates a new guardrail in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       String parent = AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString();
       Guardrail guardrail = Guardrail.newBuilder().build();
       String guardrailId = "guardrailId1875412786";
       Guardrail response = agentServiceClient.createGuardrail(parent, guardrail, guardrailId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the app to create a guardrail in.  
`guardrail` | `[Guardrail](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Guardrail)`  
Required. The guardrail to create.  
`guardrailId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The ID to use for the guardrail, which will become the final component of the guardrail's resource name. If not provided, a unique ID will be automatically assigned for the guardrail.  
**Returns**  
---  
**Type** | **Description**  
`[Guardrail](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Guardrail)` |   
  
### createGuardrailCallable()
    
    
    public final UnaryCallable<CreateGuardrailRequest,Guardrail> createGuardrailCallable()

Creates a new guardrail in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       CreateGuardrailRequest request =
           CreateGuardrailRequest.newBuilder()
               .setParent(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .setGuardrailId("guardrailId1875412786")
               .setGuardrail(Guardrail.newBuilder().build())
               .build();
       ApiFuture<Guardrail> future =
           agentServiceClient.createGuardrailCallable().futureCall(request);
       // Do something.
       Guardrail response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateGuardrailRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.CreateGuardrailRequest),[Guardrail](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Guardrail)>` |   
  
### createTool(@Nullable AppName parent, Tool tool)
    
    
    public final Tool createTool(@Nullable AppName parent, Tool tool)

Creates a new tool in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       AppName parent = AppName.of("[PROJECT]", "[LOCATION]", "[APP]");
       Tool tool = Tool.newBuilder().build();
       Tool response = agentServiceClient.createTool(parent, tool);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.AppName`  
Required. The resource name of the app to create a tool in.  
`tool` | `[Tool](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Tool)`  
Required. The tool to create.  
**Returns**  
---  
**Type** | **Description**  
`[Tool](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Tool)` |   
  
### createTool(@Nullable AppName parent, Tool tool, String toolId)
    
    
    public final Tool createTool(@Nullable AppName parent, Tool tool, String toolId)

Creates a new tool in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       AppName parent = AppName.of("[PROJECT]", "[LOCATION]", "[APP]");
       Tool tool = Tool.newBuilder().build();
       String toolId = "toolId-868061997";
       Tool response = agentServiceClient.createTool(parent, tool, toolId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.AppName`  
Required. The resource name of the app to create a tool in.  
`tool` | `[Tool](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Tool)`  
Required. The tool to create.  
`toolId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The ID to use for the tool, which will become the final component of the tool's resource name. If not provided, a unique ID will be automatically assigned for the tool.  
**Returns**  
---  
**Type** | **Description**  
`[Tool](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Tool)` |   
  
### createTool(CreateToolRequest request)
    
    
    public final Tool createTool(CreateToolRequest request)

Creates a new tool in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       CreateToolRequest request =
           CreateToolRequest.newBuilder()
               .setParent(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .setToolId("toolId-868061997")
               .setTool(Tool.newBuilder().build())
               .build();
       Tool response = agentServiceClient.createTool(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateToolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.CreateToolRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Tool](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Tool)` |   
  
### createTool(String parent, Tool tool)
    
    
    public final Tool createTool(String parent, Tool tool)

Creates a new tool in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       String parent = AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString();
       Tool tool = Tool.newBuilder().build();
       Tool response = agentServiceClient.createTool(parent, tool);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the app to create a tool in.  
`tool` | `[Tool](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Tool)`  
Required. The tool to create.  
**Returns**  
---  
**Type** | **Description**  
`[Tool](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Tool)` |   
  
### createTool(String parent, Tool tool, String toolId)
    
    
    public final Tool createTool(String parent, Tool tool, String toolId)

Creates a new tool in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       String parent = AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString();
       Tool tool = Tool.newBuilder().build();
       String toolId = "toolId-868061997";
       Tool response = agentServiceClient.createTool(parent, tool, toolId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the app to create a tool in.  
`tool` | `[Tool](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Tool)`  
Required. The tool to create.  
`toolId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The ID to use for the tool, which will become the final component of the tool's resource name. If not provided, a unique ID will be automatically assigned for the tool.  
**Returns**  
---  
**Type** | **Description**  
`[Tool](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Tool)` |   
  
### createToolCallable()
    
    
    public final UnaryCallable<CreateToolRequest,Tool> createToolCallable()

Creates a new tool in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       CreateToolRequest request =
           CreateToolRequest.newBuilder()
               .setParent(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .setToolId("toolId-868061997")
               .setTool(Tool.newBuilder().build())
               .build();
       ApiFuture<Tool> future = agentServiceClient.createToolCallable().futureCall(request);
       // Do something.
       Tool response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateToolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.CreateToolRequest),[Tool](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Tool)>` |   
  
### createToolset(@Nullable AppName parent, Toolset toolset)
    
    
    public final Toolset createToolset(@Nullable AppName parent, Toolset toolset)

Creates a new toolset in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       AppName parent = AppName.of("[PROJECT]", "[LOCATION]", "[APP]");
       Toolset toolset = Toolset.newBuilder().build();
       Toolset response = agentServiceClient.createToolset(parent, toolset);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.AppName`  
Required. The resource name of the app to create a toolset in.  
`toolset` | `[Toolset](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Toolset)`  
Required. The toolset to create.  
**Returns**  
---  
**Type** | **Description**  
`[Toolset](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Toolset)` |   
  
### createToolset(@Nullable AppName parent, Toolset toolset, String toolsetId)
    
    
    public final Toolset createToolset(@Nullable AppName parent, Toolset toolset, String toolsetId)

Creates a new toolset in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       AppName parent = AppName.of("[PROJECT]", "[LOCATION]", "[APP]");
       Toolset toolset = Toolset.newBuilder().build();
       String toolsetId = "toolsetId-397931899";
       Toolset response = agentServiceClient.createToolset(parent, toolset, toolsetId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.AppName`  
Required. The resource name of the app to create a toolset in.  
`toolset` | `[Toolset](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Toolset)`  
Required. The toolset to create.  
`toolsetId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The ID to use for the toolset, which will become the final component of the toolset's resource name. If not provided, a unique ID will be automatically assigned for the toolset.  
**Returns**  
---  
**Type** | **Description**  
`[Toolset](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Toolset)` |   
  
### createToolset(CreateToolsetRequest request)
    
    
    public final Toolset createToolset(CreateToolsetRequest request)

Creates a new toolset in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       CreateToolsetRequest request =
           CreateToolsetRequest.newBuilder()
               .setParent(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .setToolsetId("toolsetId-397931899")
               .setToolset(Toolset.newBuilder().build())
               .build();
       Toolset response = agentServiceClient.createToolset(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateToolsetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.CreateToolsetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Toolset](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Toolset)` |   
  
### createToolset(String parent, Toolset toolset)
    
    
    public final Toolset createToolset(String parent, Toolset toolset)

Creates a new toolset in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       String parent = AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString();
       Toolset toolset = Toolset.newBuilder().build();
       Toolset response = agentServiceClient.createToolset(parent, toolset);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the app to create a toolset in.  
`toolset` | `[Toolset](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Toolset)`  
Required. The toolset to create.  
**Returns**  
---  
**Type** | **Description**  
`[Toolset](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Toolset)` |   
  
### createToolset(String parent, Toolset toolset, String toolsetId)
    
    
    public final Toolset createToolset(String parent, Toolset toolset, String toolsetId)

Creates a new toolset in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       String parent = AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString();
       Toolset toolset = Toolset.newBuilder().build();
       String toolsetId = "toolsetId-397931899";
       Toolset response = agentServiceClient.createToolset(parent, toolset, toolsetId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the app to create a toolset in.  
`toolset` | `[Toolset](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Toolset)`  
Required. The toolset to create.  
`toolsetId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The ID to use for the toolset, which will become the final component of the toolset's resource name. If not provided, a unique ID will be automatically assigned for the toolset.  
**Returns**  
---  
**Type** | **Description**  
`[Toolset](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Toolset)` |   
  
### createToolsetCallable()
    
    
    public final UnaryCallable<CreateToolsetRequest,Toolset> createToolsetCallable()

Creates a new toolset in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       CreateToolsetRequest request =
           CreateToolsetRequest.newBuilder()
               .setParent(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .setToolsetId("toolsetId-397931899")
               .setToolset(Toolset.newBuilder().build())
               .build();
       ApiFuture<Toolset> future = agentServiceClient.createToolsetCallable().futureCall(request);
       // Do something.
       Toolset response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateToolsetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.CreateToolsetRequest),[Toolset](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Toolset)>` |   
  
### deleteAgent(@Nullable AgentName name)
    
    
    public final void deleteAgent(@Nullable AgentName name)

Deletes the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       AgentName name = AgentName.of("[PROJECT]", "[LOCATION]", "[APP]", "[AGENT]");
       agentServiceClient.deleteAgent(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.AgentName`  
Required. The resource name of the agent to delete.  
  
### deleteAgent(DeleteAgentRequest request)
    
    
    public final void deleteAgent(DeleteAgentRequest request)

Deletes the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       DeleteAgentRequest request =
           DeleteAgentRequest.newBuilder()
               .setName(AgentName.of("[PROJECT]", "[LOCATION]", "[APP]", "[AGENT]").toString())
               .setForce(true)
               .setEtag("etag3123477")
               .build();
       agentServiceClient.deleteAgent(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.DeleteAgentRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteAgent(String name)
    
    
    public final void deleteAgent(String name)

Deletes the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       String name = AgentName.of("[PROJECT]", "[LOCATION]", "[APP]", "[AGENT]").toString();
       agentServiceClient.deleteAgent(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the agent to delete.  
  
### deleteAgentCallable()
    
    
    public final UnaryCallable<DeleteAgentRequest,Empty> deleteAgentCallable()

Deletes the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       DeleteAgentRequest request =
           DeleteAgentRequest.newBuilder()
               .setName(AgentName.of("[PROJECT]", "[LOCATION]", "[APP]", "[AGENT]").toString())
               .setForce(true)
               .setEtag("etag3123477")
               .build();
       ApiFuture<Empty> future = agentServiceClient.deleteAgentCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.DeleteAgentRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteAppAsync(@Nullable AppName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteAppAsync(@Nullable AppName name)

Deletes the specified app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       AppName name = AppName.of("[PROJECT]", "[LOCATION]", "[APP]");
       agentServiceClient.deleteAppAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.AppName`  
Required. The resource name of the app to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.OperationMetadata)>` |   
  
### deleteAppAsync(DeleteAppRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteAppAsync(DeleteAppRequest request)

Deletes the specified app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       DeleteAppRequest request =
           DeleteAppRequest.newBuilder()
               .setName(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .setEtag("etag3123477")
               .build();
       agentServiceClient.deleteAppAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteAppRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.DeleteAppRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.OperationMetadata)>` |   
  
### deleteAppAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteAppAsync(String name)

Deletes the specified app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       String name = AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString();
       agentServiceClient.deleteAppAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the app to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.OperationMetadata)>` |   
  
### deleteAppCallable()
    
    
    public final UnaryCallable<DeleteAppRequest,Operation> deleteAppCallable()

Deletes the specified app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       DeleteAppRequest request =
           DeleteAppRequest.newBuilder()
               .setName(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .setEtag("etag3123477")
               .build();
       ApiFuture<Operation> future = agentServiceClient.deleteAppCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteAppRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.DeleteAppRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteAppOperationCallable()
    
    
    public final OperationCallable<DeleteAppRequest,Empty,OperationMetadata> deleteAppOperationCallable()

Deletes the specified app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       DeleteAppRequest request =
           DeleteAppRequest.newBuilder()
               .setName(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .setEtag("etag3123477")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           agentServiceClient.deleteAppOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteAppRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.DeleteAppRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.OperationMetadata)>` |   
  
### deleteAppVersion(@Nullable AppVersionName name)
    
    
    public final void deleteAppVersion(@Nullable AppVersionName name)

Deletes the specified app version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       AppVersionName name = AppVersionName.of("[PROJECT]", "[LOCATION]", "[APP]", "[VERSION]");
       agentServiceClient.deleteAppVersion(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.AppVersionName`  
Required. The resource name of the app version to delete.  
  
### deleteAppVersion(DeleteAppVersionRequest request)
    
    
    public final void deleteAppVersion(DeleteAppVersionRequest request)

Deletes the specified app version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       DeleteAppVersionRequest request =
           DeleteAppVersionRequest.newBuilder()
               .setName(
                   AppVersionName.of("[PROJECT]", "[LOCATION]", "[APP]", "[VERSION]").toString())
               .setEtag("etag3123477")
               .build();
       agentServiceClient.deleteAppVersion(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteAppVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.DeleteAppVersionRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteAppVersion(String name)
    
    
    public final void deleteAppVersion(String name)

Deletes the specified app version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       String name = AppVersionName.of("[PROJECT]", "[LOCATION]", "[APP]", "[VERSION]").toString();
       agentServiceClient.deleteAppVersion(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the app version to delete.  
  
### deleteAppVersionCallable()
    
    
    public final UnaryCallable<DeleteAppVersionRequest,Empty> deleteAppVersionCallable()

Deletes the specified app version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       DeleteAppVersionRequest request =
           DeleteAppVersionRequest.newBuilder()
               .setName(
                   AppVersionName.of("[PROJECT]", "[LOCATION]", "[APP]", "[VERSION]").toString())
               .setEtag("etag3123477")
               .build();
       ApiFuture<Empty> future = agentServiceClient.deleteAppVersionCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteAppVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.DeleteAppVersionRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteConversation(@Nullable ConversationName name)
    
    
    public final void deleteConversation(@Nullable ConversationName name)

Deletes the specified conversation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       ConversationName name =
           ConversationName.of("[PROJECT]", "[LOCATION]", "[APP]", "[CONVERSATION]");
       agentServiceClient.deleteConversation(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.ConversationName`  
Required. The resource name of the conversation to delete.  
  
### deleteConversation(DeleteConversationRequest request)
    
    
    public final void deleteConversation(DeleteConversationRequest request)

Deletes the specified conversation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       DeleteConversationRequest request =
           DeleteConversationRequest.newBuilder()
               .setName(
                   ConversationName.of("[PROJECT]", "[LOCATION]", "[APP]", "[CONVERSATION]")
                       .toString())
               .build();
       agentServiceClient.deleteConversation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteConversationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.DeleteConversationRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteConversation(String name)
    
    
    public final void deleteConversation(String name)

Deletes the specified conversation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       String name =
           ConversationName.of("[PROJECT]", "[LOCATION]", "[APP]", "[CONVERSATION]").toString();
       agentServiceClient.deleteConversation(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the conversation to delete.  
  
### deleteConversationCallable()
    
    
    public final UnaryCallable<DeleteConversationRequest,Empty> deleteConversationCallable()

Deletes the specified conversation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       DeleteConversationRequest request =
           DeleteConversationRequest.newBuilder()
               .setName(
                   ConversationName.of("[PROJECT]", "[LOCATION]", "[APP]", "[CONVERSATION]")
                       .toString())
               .build();
       ApiFuture<Empty> future = agentServiceClient.deleteConversationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteConversationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.DeleteConversationRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteDeployment(@Nullable DeploymentName name)
    
    
    public final void deleteDeployment(@Nullable DeploymentName name)

Deletes the specified deployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       DeploymentName name = DeploymentName.of("[PROJECT]", "[LOCATION]", "[APP]", "[DEPLOYMENT]");
       agentServiceClient.deleteDeployment(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.DeploymentName`  
Required. The name of the deployment to delete. Format: `projects/{project}/locations/{location}/apps/{app}/deployments/{deployment}`  
  
### deleteDeployment(DeleteDeploymentRequest request)
    
    
    public final void deleteDeployment(DeleteDeploymentRequest request)

Deletes the specified deployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       DeleteDeploymentRequest request =
           DeleteDeploymentRequest.newBuilder()
               .setName(
                   DeploymentName.of("[PROJECT]", "[LOCATION]", "[APP]", "[DEPLOYMENT]").toString())
               .setEtag("etag3123477")
               .build();
       agentServiceClient.deleteDeployment(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.DeleteDeploymentRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteDeployment(String name)
    
    
    public final void deleteDeployment(String name)

Deletes the specified deployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       String name =
           DeploymentName.of("[PROJECT]", "[LOCATION]", "[APP]", "[DEPLOYMENT]").toString();
       agentServiceClient.deleteDeployment(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the deployment to delete. Format: `projects/{project}/locations/{location}/apps/{app}/deployments/{deployment}`  
  
### deleteDeploymentCallable()
    
    
    public final UnaryCallable<DeleteDeploymentRequest,Empty> deleteDeploymentCallable()

Deletes the specified deployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       DeleteDeploymentRequest request =
           DeleteDeploymentRequest.newBuilder()
               .setName(
                   DeploymentName.of("[PROJECT]", "[LOCATION]", "[APP]", "[DEPLOYMENT]").toString())
               .setEtag("etag3123477")
               .build();
       ApiFuture<Empty> future = agentServiceClient.deleteDeploymentCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.DeleteDeploymentRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteExample(@Nullable ExampleName name)
    
    
    public final void deleteExample(@Nullable ExampleName name)

Deletes the specified example.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       ExampleName name = ExampleName.of("[PROJECT]", "[LOCATION]", "[APP]", "[EXAMPLE]");
       agentServiceClient.deleteExample(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.ExampleName`  
Required. The resource name of the example to delete.  
  
### deleteExample(DeleteExampleRequest request)
    
    
    public final void deleteExample(DeleteExampleRequest request)

Deletes the specified example.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       DeleteExampleRequest request =
           DeleteExampleRequest.newBuilder()
               .setName(ExampleName.of("[PROJECT]", "[LOCATION]", "[APP]", "[EXAMPLE]").toString())
               .setEtag("etag3123477")
               .build();
       agentServiceClient.deleteExample(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteExampleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.DeleteExampleRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteExample(String name)
    
    
    public final void deleteExample(String name)

Deletes the specified example.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       String name = ExampleName.of("[PROJECT]", "[LOCATION]", "[APP]", "[EXAMPLE]").toString();
       agentServiceClient.deleteExample(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the example to delete.  
  
### deleteExampleCallable()
    
    
    public final UnaryCallable<DeleteExampleRequest,Empty> deleteExampleCallable()

Deletes the specified example.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       DeleteExampleRequest request =
           DeleteExampleRequest.newBuilder()
               .setName(ExampleName.of("[PROJECT]", "[LOCATION]", "[APP]", "[EXAMPLE]").toString())
               .setEtag("etag3123477")
               .build();
       ApiFuture<Empty> future = agentServiceClient.deleteExampleCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteExampleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.DeleteExampleRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteGuardrail(@Nullable GuardrailName name)
    
    
    public final void deleteGuardrail(@Nullable GuardrailName name)

Deletes the specified guardrail.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       GuardrailName name = GuardrailName.of("[PROJECT]", "[LOCATION]", "[APP]", "[GUARDRAIL]");
       agentServiceClient.deleteGuardrail(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.GuardrailName`  
Required. The resource name of the guardrail to delete.  
  
### deleteGuardrail(DeleteGuardrailRequest request)
    
    
    public final void deleteGuardrail(DeleteGuardrailRequest request)

Deletes the specified guardrail.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       DeleteGuardrailRequest request =
           DeleteGuardrailRequest.newBuilder()
               .setName(
                   GuardrailName.of("[PROJECT]", "[LOCATION]", "[APP]", "[GUARDRAIL]").toString())
               .setForce(true)
               .setEtag("etag3123477")
               .build();
       agentServiceClient.deleteGuardrail(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteGuardrailRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.DeleteGuardrailRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteGuardrail(String name)
    
    
    public final void deleteGuardrail(String name)

Deletes the specified guardrail.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       String name = GuardrailName.of("[PROJECT]", "[LOCATION]", "[APP]", "[GUARDRAIL]").toString();
       agentServiceClient.deleteGuardrail(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the guardrail to delete.  
  
### deleteGuardrailCallable()
    
    
    public final UnaryCallable<DeleteGuardrailRequest,Empty> deleteGuardrailCallable()

Deletes the specified guardrail.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       DeleteGuardrailRequest request =
           DeleteGuardrailRequest.newBuilder()
               .setName(
                   GuardrailName.of("[PROJECT]", "[LOCATION]", "[APP]", "[GUARDRAIL]").toString())
               .setForce(true)
               .setEtag("etag3123477")
               .build();
       ApiFuture<Empty> future = agentServiceClient.deleteGuardrailCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteGuardrailRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.DeleteGuardrailRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteTool(@Nullable ToolName name)
    
    
    public final void deleteTool(@Nullable ToolName name)

Deletes the specified tool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       ToolName name = ToolName.of("[PROJECT]", "[LOCATION]", "[APP]", "[TOOL]");
       agentServiceClient.deleteTool(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.ToolName`  
Required. The resource name of the tool to delete.  
  
### deleteTool(DeleteToolRequest request)
    
    
    public final void deleteTool(DeleteToolRequest request)

Deletes the specified tool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       DeleteToolRequest request =
           DeleteToolRequest.newBuilder()
               .setName(ToolName.of("[PROJECT]", "[LOCATION]", "[APP]", "[TOOL]").toString())
               .setForce(true)
               .setEtag("etag3123477")
               .build();
       agentServiceClient.deleteTool(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteToolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.DeleteToolRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteTool(String name)
    
    
    public final void deleteTool(String name)

Deletes the specified tool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       String name = ToolName.of("[PROJECT]", "[LOCATION]", "[APP]", "[TOOL]").toString();
       agentServiceClient.deleteTool(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the tool to delete.  
  
### deleteToolCallable()
    
    
    public final UnaryCallable<DeleteToolRequest,Empty> deleteToolCallable()

Deletes the specified tool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       DeleteToolRequest request =
           DeleteToolRequest.newBuilder()
               .setName(ToolName.of("[PROJECT]", "[LOCATION]", "[APP]", "[TOOL]").toString())
               .setForce(true)
               .setEtag("etag3123477")
               .build();
       ApiFuture<Empty> future = agentServiceClient.deleteToolCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteToolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.DeleteToolRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteToolset(@Nullable ToolsetName name)
    
    
    public final void deleteToolset(@Nullable ToolsetName name)

Deletes the specified toolset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       ToolsetName name = ToolsetName.of("[PROJECT]", "[LOCATION]", "[APP]", "[TOOLSET]");
       agentServiceClient.deleteToolset(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.ToolsetName`  
Required. The resource name of the toolset to delete.  
  
### deleteToolset(DeleteToolsetRequest request)
    
    
    public final void deleteToolset(DeleteToolsetRequest request)

Deletes the specified toolset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       DeleteToolsetRequest request =
           DeleteToolsetRequest.newBuilder()
               .setName(ToolsetName.of("[PROJECT]", "[LOCATION]", "[APP]", "[TOOLSET]").toString())
               .setForce(true)
               .setEtag("etag3123477")
               .build();
       agentServiceClient.deleteToolset(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteToolsetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.DeleteToolsetRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteToolset(String name)
    
    
    public final void deleteToolset(String name)

Deletes the specified toolset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       String name = ToolsetName.of("[PROJECT]", "[LOCATION]", "[APP]", "[TOOLSET]").toString();
       agentServiceClient.deleteToolset(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the toolset to delete.  
  
### deleteToolsetCallable()
    
    
    public final UnaryCallable<DeleteToolsetRequest,Empty> deleteToolsetCallable()

Deletes the specified toolset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       DeleteToolsetRequest request =
           DeleteToolsetRequest.newBuilder()
               .setName(ToolsetName.of("[PROJECT]", "[LOCATION]", "[APP]", "[TOOLSET]").toString())
               .setForce(true)
               .setEtag("etag3123477")
               .build();
       ApiFuture<Empty> future = agentServiceClient.deleteToolsetCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteToolsetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.DeleteToolsetRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### exportAppAsync(@Nullable AppName name)
    
    
    public final OperationFuture<ExportAppResponse,OperationMetadata> exportAppAsync(@Nullable AppName name)

Exports the specified app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       AppName name = AppName.of("[PROJECT]", "[LOCATION]", "[APP]");
       ExportAppResponse response = agentServiceClient.exportAppAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.AppName`  
Required. The resource name of the app to export.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExportAppResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ExportAppResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.OperationMetadata)>` |   
  
### exportAppAsync(ExportAppRequest request)
    
    
    public final OperationFuture<ExportAppResponse,OperationMetadata> exportAppAsync(ExportAppRequest request)

Exports the specified app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       ExportAppRequest request =
           ExportAppRequest.newBuilder()
               .setName(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .setGcsUri("gcsUri-1251224875")
               .setAppVersion(
                   AppVersionName.of("[PROJECT]", "[LOCATION]", "[APP]", "[VERSION]").toString())
               .build();
       ExportAppResponse response = agentServiceClient.exportAppAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ExportAppRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ExportAppRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExportAppResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ExportAppResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.OperationMetadata)>` |   
  
### exportAppAsync(String name)
    
    
    public final OperationFuture<ExportAppResponse,OperationMetadata> exportAppAsync(String name)

Exports the specified app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       String name = AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString();
       ExportAppResponse response = agentServiceClient.exportAppAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the app to export.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExportAppResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ExportAppResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.OperationMetadata)>` |   
  
### exportAppCallable()
    
    
    public final UnaryCallable<ExportAppRequest,Operation> exportAppCallable()

Exports the specified app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       ExportAppRequest request =
           ExportAppRequest.newBuilder()
               .setName(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .setGcsUri("gcsUri-1251224875")
               .setAppVersion(
                   AppVersionName.of("[PROJECT]", "[LOCATION]", "[APP]", "[VERSION]").toString())
               .build();
       ApiFuture<Operation> future = agentServiceClient.exportAppCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ExportAppRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ExportAppRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### exportAppOperationCallable()
    
    
    public final OperationCallable<ExportAppRequest,ExportAppResponse,OperationMetadata> exportAppOperationCallable()

Exports the specified app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       ExportAppRequest request =
           ExportAppRequest.newBuilder()
               .setName(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .setGcsUri("gcsUri-1251224875")
               .setAppVersion(
                   AppVersionName.of("[PROJECT]", "[LOCATION]", "[APP]", "[VERSION]").toString())
               .build();
       OperationFuture<ExportAppResponse, OperationMetadata> future =
           agentServiceClient.exportAppOperationCallable().futureCall(request);
       // Do something.
       ExportAppResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ExportAppRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ExportAppRequest),[ExportAppResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ExportAppResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.OperationMetadata)>` |   
  
### generateAppResourceAsync(@Nullable AppName parent)
    
    
    public final OperationFuture<GenerateAppResourceResponse,GenerateAppResourceOperationMetadata> generateAppResourceAsync(@Nullable AppName parent)

Generates specific resources (e.g. agent) in the app using LLM assistant.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       AppName parent = AppName.of("[PROJECT]", "[LOCATION]", "[APP]");
       GenerateAppResourceResponse response =
           agentServiceClient.generateAppResourceAsync(parent).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.AppName`  
Required. The resource name of the app to generate the resource for.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[GenerateAppResourceResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.GenerateAppResourceResponse),[GenerateAppResourceOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.GenerateAppResourceOperationMetadata)>` |   
  
### generateAppResourceAsync(GenerateAppResourceRequest request)
    
    
    public final OperationFuture<GenerateAppResourceResponse,GenerateAppResourceOperationMetadata> generateAppResourceAsync(GenerateAppResourceRequest request)

Generates specific resources (e.g. agent) in the app using LLM assistant.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       GenerateAppResourceRequest request =
           GenerateAppResourceRequest.newBuilder()
               .setParent(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .addAllRefineInstructions(
                   new ArrayList<GenerateAppResourceRequest.RefineInstructions>())
               .setToolGenerationConfig(
                   GenerateAppResourceRequest.ToolGenerationConfig.newBuilder().build())
               .setAppGenerationConfig(
                   GenerateAppResourceRequest.AppGenerationConfig.newBuilder().build())
               .setEvaluationGenerationConfig(
                   GenerateAppResourceRequest.EvaluationGenerationConfig.newBuilder().build())
               .setEvaluationPersonasGenerationConfig(
                   GenerateAppResourceRequest.EvaluationPersonasGenerationConfig.newBuilder()
                       .build())
               .setQualityReportGenerationConfig(
                   GenerateAppResourceRequest.QualityReportGenerationConfig.newBuilder().build())
               .setHillClimbingFixConfig(
                   GenerateAppResourceRequest.HillClimbingFixConfig.newBuilder().build())
               .build();
       GenerateAppResourceResponse response =
           agentServiceClient.generateAppResourceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GenerateAppResourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.GenerateAppResourceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[GenerateAppResourceResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.GenerateAppResourceResponse),[GenerateAppResourceOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.GenerateAppResourceOperationMetadata)>` |   
  
### generateAppResourceAsync(String parent)
    
    
    public final OperationFuture<GenerateAppResourceResponse,GenerateAppResourceOperationMetadata> generateAppResourceAsync(String parent)

Generates specific resources (e.g. agent) in the app using LLM assistant.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       String parent = AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString();
       GenerateAppResourceResponse response =
           agentServiceClient.generateAppResourceAsync(parent).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the app to generate the resource for.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[GenerateAppResourceResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.GenerateAppResourceResponse),[GenerateAppResourceOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.GenerateAppResourceOperationMetadata)>` |   
  
### generateAppResourceCallable()
    
    
    public final UnaryCallable<GenerateAppResourceRequest,Operation> generateAppResourceCallable()

Generates specific resources (e.g. agent) in the app using LLM assistant.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       GenerateAppResourceRequest request =
           GenerateAppResourceRequest.newBuilder()
               .setParent(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .addAllRefineInstructions(
                   new ArrayList<GenerateAppResourceRequest.RefineInstructions>())
               .setToolGenerationConfig(
                   GenerateAppResourceRequest.ToolGenerationConfig.newBuilder().build())
               .setAppGenerationConfig(
                   GenerateAppResourceRequest.AppGenerationConfig.newBuilder().build())
               .setEvaluationGenerationConfig(
                   GenerateAppResourceRequest.EvaluationGenerationConfig.newBuilder().build())
               .setEvaluationPersonasGenerationConfig(
                   GenerateAppResourceRequest.EvaluationPersonasGenerationConfig.newBuilder()
                       .build())
               .setQualityReportGenerationConfig(
                   GenerateAppResourceRequest.QualityReportGenerationConfig.newBuilder().build())
               .setHillClimbingFixConfig(
                   GenerateAppResourceRequest.HillClimbingFixConfig.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           agentServiceClient.generateAppResourceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GenerateAppResourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.GenerateAppResourceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### generateAppResourceOperationCallable()
    
    
    public final OperationCallable<GenerateAppResourceRequest,GenerateAppResourceResponse,GenerateAppResourceOperationMetadata> generateAppResourceOperationCallable()

Generates specific resources (e.g. agent) in the app using LLM assistant.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       GenerateAppResourceRequest request =
           GenerateAppResourceRequest.newBuilder()
               .setParent(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .addAllRefineInstructions(
                   new ArrayList<GenerateAppResourceRequest.RefineInstructions>())
               .setToolGenerationConfig(
                   GenerateAppResourceRequest.ToolGenerationConfig.newBuilder().build())
               .setAppGenerationConfig(
                   GenerateAppResourceRequest.AppGenerationConfig.newBuilder().build())
               .setEvaluationGenerationConfig(
                   GenerateAppResourceRequest.EvaluationGenerationConfig.newBuilder().build())
               .setEvaluationPersonasGenerationConfig(
                   GenerateAppResourceRequest.EvaluationPersonasGenerationConfig.newBuilder()
                       .build())
               .setQualityReportGenerationConfig(
                   GenerateAppResourceRequest.QualityReportGenerationConfig.newBuilder().build())
               .setHillClimbingFixConfig(
                   GenerateAppResourceRequest.HillClimbingFixConfig.newBuilder().build())
               .build();
       OperationFuture<GenerateAppResourceResponse, GenerateAppResourceOperationMetadata> future =
           agentServiceClient.generateAppResourceOperationCallable().futureCall(request);
       // Do something.
       GenerateAppResourceResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[GenerateAppResourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.GenerateAppResourceRequest),[GenerateAppResourceResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.GenerateAppResourceResponse),[GenerateAppResourceOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.GenerateAppResourceOperationMetadata)>` |   
  
### getAgent(@Nullable AgentName name)
    
    
    public final Agent getAgent(@Nullable AgentName name)

Gets details of the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       AgentName name = AgentName.of("[PROJECT]", "[LOCATION]", "[APP]", "[AGENT]");
       Agent response = agentServiceClient.getAgent(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.AgentName`  
Required. The resource name of the agent to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Agent)` |   
  
### getAgent(GetAgentRequest request)
    
    
    public final Agent getAgent(GetAgentRequest request)

Gets details of the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       GetAgentRequest request =
           GetAgentRequest.newBuilder()
               .setName(AgentName.of("[PROJECT]", "[LOCATION]", "[APP]", "[AGENT]").toString())
               .build();
       Agent response = agentServiceClient.getAgent(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.GetAgentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Agent)` |   
  
### getAgent(String name)
    
    
    public final Agent getAgent(String name)

Gets details of the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       String name = AgentName.of("[PROJECT]", "[LOCATION]", "[APP]", "[AGENT]").toString();
       Agent response = agentServiceClient.getAgent(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the agent to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Agent)` |   
  
### getAgentCallable()
    
    
    public final UnaryCallable<GetAgentRequest,Agent> getAgentCallable()

Gets details of the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       GetAgentRequest request =
           GetAgentRequest.newBuilder()
               .setName(AgentName.of("[PROJECT]", "[LOCATION]", "[APP]", "[AGENT]").toString())
               .build();
       ApiFuture<Agent> future = agentServiceClient.getAgentCallable().futureCall(request);
       // Do something.
       Agent response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.GetAgentRequest),[Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Agent)>` |   
  
### getApp(@Nullable AppName name)
    
    
    public final App getApp(@Nullable AppName name)

Gets details of the specified app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       AppName name = AppName.of("[PROJECT]", "[LOCATION]", "[APP]");
       App response = agentServiceClient.getApp(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.AppName`  
Required. The resource name of the app to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`[App](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.App)` |   
  
### getApp(GetAppRequest request)
    
    
    public final App getApp(GetAppRequest request)

Gets details of the specified app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       GetAppRequest request =
           GetAppRequest.newBuilder()
               .setName(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .build();
       App response = agentServiceClient.getApp(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAppRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.GetAppRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[App](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.App)` |   
  
### getApp(String name)
    
    
    public final App getApp(String name)

Gets details of the specified app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       String name = AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString();
       App response = agentServiceClient.getApp(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the app to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`[App](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.App)` |   
  
### getAppCallable()
    
    
    public final UnaryCallable<GetAppRequest,App> getAppCallable()

Gets details of the specified app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       GetAppRequest request =
           GetAppRequest.newBuilder()
               .setName(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .build();
       ApiFuture<App> future = agentServiceClient.getAppCallable().futureCall(request);
       // Do something.
       App response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetAppRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.GetAppRequest),[App](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.App)>` |   
  
### getAppVersion(@Nullable AppVersionName name)
    
    
    public final AppVersion getAppVersion(@Nullable AppVersionName name)

Gets details of the specified app version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       AppVersionName name = AppVersionName.of("[PROJECT]", "[LOCATION]", "[APP]", "[VERSION]");
       AppVersion response = agentServiceClient.getAppVersion(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.AppVersionName`  
Required. The resource name of the app version to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`[AppVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AppVersion)` |   
  
### getAppVersion(GetAppVersionRequest request)
    
    
    public final AppVersion getAppVersion(GetAppVersionRequest request)

Gets details of the specified app version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       GetAppVersionRequest request =
           GetAppVersionRequest.newBuilder()
               .setName(
                   AppVersionName.of("[PROJECT]", "[LOCATION]", "[APP]", "[VERSION]").toString())
               .build();
       AppVersion response = agentServiceClient.getAppVersion(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAppVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.GetAppVersionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AppVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AppVersion)` |   
  
### getAppVersion(String name)
    
    
    public final AppVersion getAppVersion(String name)

Gets details of the specified app version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       String name = AppVersionName.of("[PROJECT]", "[LOCATION]", "[APP]", "[VERSION]").toString();
       AppVersion response = agentServiceClient.getAppVersion(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the app version to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`[AppVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AppVersion)` |   
  
### getAppVersionCallable()
    
    
    public final UnaryCallable<GetAppVersionRequest,AppVersion> getAppVersionCallable()

Gets details of the specified app version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       GetAppVersionRequest request =
           GetAppVersionRequest.newBuilder()
               .setName(
                   AppVersionName.of("[PROJECT]", "[LOCATION]", "[APP]", "[VERSION]").toString())
               .build();
       ApiFuture<AppVersion> future = agentServiceClient.getAppVersionCallable().futureCall(request);
       // Do something.
       AppVersion response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetAppVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.GetAppVersionRequest),[AppVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AppVersion)>` |   
  
### getChangelog(@Nullable ChangelogName name)
    
    
    public final Changelog getChangelog(@Nullable ChangelogName name)

Gets the specified changelog.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       ChangelogName name = ChangelogName.of("[PROJECT]", "[LOCATION]", "[APP]", "[CHANGELOG]");
       Changelog response = agentServiceClient.getChangelog(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.ChangelogName`  
Required. The resource name of the changelog to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`[Changelog](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Changelog)` |   
  
### getChangelog(GetChangelogRequest request)
    
    
    public final Changelog getChangelog(GetChangelogRequest request)

Gets the specified changelog.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       GetChangelogRequest request =
           GetChangelogRequest.newBuilder()
               .setName(
                   ChangelogName.of("[PROJECT]", "[LOCATION]", "[APP]", "[CHANGELOG]").toString())
               .build();
       Changelog response = agentServiceClient.getChangelog(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetChangelogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.GetChangelogRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Changelog](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Changelog)` |   
  
### getChangelog(String name)
    
    
    public final Changelog getChangelog(String name)

Gets the specified changelog.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       String name = ChangelogName.of("[PROJECT]", "[LOCATION]", "[APP]", "[CHANGELOG]").toString();
       Changelog response = agentServiceClient.getChangelog(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the changelog to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`[Changelog](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Changelog)` |   
  
### getChangelogCallable()
    
    
    public final UnaryCallable<GetChangelogRequest,Changelog> getChangelogCallable()

Gets the specified changelog.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       GetChangelogRequest request =
           GetChangelogRequest.newBuilder()
               .setName(
                   ChangelogName.of("[PROJECT]", "[LOCATION]", "[APP]", "[CHANGELOG]").toString())
               .build();
       ApiFuture<Changelog> future = agentServiceClient.getChangelogCallable().futureCall(request);
       // Do something.
       Changelog response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetChangelogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.GetChangelogRequest),[Changelog](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Changelog)>` |   
  
### getConversation(@Nullable ConversationName name)
    
    
    public final Conversation getConversation(@Nullable ConversationName name)

Gets details of the specified conversation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       ConversationName name =
           ConversationName.of("[PROJECT]", "[LOCATION]", "[APP]", "[CONVERSATION]");
       Conversation response = agentServiceClient.getConversation(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.ConversationName`  
Required. The resource name of the conversation to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`[Conversation](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Conversation)` |   
  
### getConversation(GetConversationRequest request)
    
    
    public final Conversation getConversation(GetConversationRequest request)

Gets details of the specified conversation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       GetConversationRequest request =
           GetConversationRequest.newBuilder()
               .setName(
                   ConversationName.of("[PROJECT]", "[LOCATION]", "[APP]", "[CONVERSATION]")
                       .toString())
               .build();
       Conversation response = agentServiceClient.getConversation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetConversationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.GetConversationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Conversation](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Conversation)` |   
  
### getConversation(String name)
    
    
    public final Conversation getConversation(String name)

Gets details of the specified conversation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       String name =
           ConversationName.of("[PROJECT]", "[LOCATION]", "[APP]", "[CONVERSATION]").toString();
       Conversation response = agentServiceClient.getConversation(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the conversation to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`[Conversation](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Conversation)` |   
  
### getConversationCallable()
    
    
    public final UnaryCallable<GetConversationRequest,Conversation> getConversationCallable()

Gets details of the specified conversation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       GetConversationRequest request =
           GetConversationRequest.newBuilder()
               .setName(
                   ConversationName.of("[PROJECT]", "[LOCATION]", "[APP]", "[CONVERSATION]")
                       .toString())
               .build();
       ApiFuture<Conversation> future =
           agentServiceClient.getConversationCallable().futureCall(request);
       // Do something.
       Conversation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetConversationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.GetConversationRequest),[Conversation](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Conversation)>` |   
  
### getDeployment(@Nullable DeploymentName name)
    
    
    public final Deployment getDeployment(@Nullable DeploymentName name)

Gets details of the specified deployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       DeploymentName name = DeploymentName.of("[PROJECT]", "[LOCATION]", "[APP]", "[DEPLOYMENT]");
       Deployment response = agentServiceClient.getDeployment(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.DeploymentName`  
Required. The name of the deployment. Format: `projects/{project}/locations/{location}/apps/{app}/deployments/{deployment}`  
**Returns**  
---  
**Type** | **Description**  
`[Deployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Deployment)` |   
  
### getDeployment(GetDeploymentRequest request)
    
    
    public final Deployment getDeployment(GetDeploymentRequest request)

Gets details of the specified deployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       GetDeploymentRequest request =
           GetDeploymentRequest.newBuilder()
               .setName(
                   DeploymentName.of("[PROJECT]", "[LOCATION]", "[APP]", "[DEPLOYMENT]").toString())
               .build();
       Deployment response = agentServiceClient.getDeployment(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.GetDeploymentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Deployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Deployment)` |   
  
### getDeployment(String name)
    
    
    public final Deployment getDeployment(String name)

Gets details of the specified deployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       String name =
           DeploymentName.of("[PROJECT]", "[LOCATION]", "[APP]", "[DEPLOYMENT]").toString();
       Deployment response = agentServiceClient.getDeployment(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the deployment. Format: `projects/{project}/locations/{location}/apps/{app}/deployments/{deployment}`  
**Returns**  
---  
**Type** | **Description**  
`[Deployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Deployment)` |   
  
### getDeploymentCallable()
    
    
    public final UnaryCallable<GetDeploymentRequest,Deployment> getDeploymentCallable()

Gets details of the specified deployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       GetDeploymentRequest request =
           GetDeploymentRequest.newBuilder()
               .setName(
                   DeploymentName.of("[PROJECT]", "[LOCATION]", "[APP]", "[DEPLOYMENT]").toString())
               .build();
       ApiFuture<Deployment> future = agentServiceClient.getDeploymentCallable().futureCall(request);
       // Do something.
       Deployment response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.GetDeploymentRequest),[Deployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Deployment)>` |   
  
### getExample(@Nullable ExampleName name)
    
    
    public final Example getExample(@Nullable ExampleName name)

Gets details of the specified example.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       ExampleName name = ExampleName.of("[PROJECT]", "[LOCATION]", "[APP]", "[EXAMPLE]");
       Example response = agentServiceClient.getExample(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.ExampleName`  
Required. The resource name of the example to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`[Example](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Example)` |   
  
### getExample(GetExampleRequest request)
    
    
    public final Example getExample(GetExampleRequest request)

Gets details of the specified example.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       GetExampleRequest request =
           GetExampleRequest.newBuilder()
               .setName(ExampleName.of("[PROJECT]", "[LOCATION]", "[APP]", "[EXAMPLE]").toString())
               .build();
       Example response = agentServiceClient.getExample(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetExampleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.GetExampleRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Example](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Example)` |   
  
### getExample(String name)
    
    
    public final Example getExample(String name)

Gets details of the specified example.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       String name = ExampleName.of("[PROJECT]", "[LOCATION]", "[APP]", "[EXAMPLE]").toString();
       Example response = agentServiceClient.getExample(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the example to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`[Example](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Example)` |   
  
### getExampleCallable()
    
    
    public final UnaryCallable<GetExampleRequest,Example> getExampleCallable()

Gets details of the specified example.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       GetExampleRequest request =
           GetExampleRequest.newBuilder()
               .setName(ExampleName.of("[PROJECT]", "[LOCATION]", "[APP]", "[EXAMPLE]").toString())
               .build();
       ApiFuture<Example> future = agentServiceClient.getExampleCallable().futureCall(request);
       // Do something.
       Example response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetExampleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.GetExampleRequest),[Example](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Example)>` |   
  
### getGuardrail(@Nullable GuardrailName name)
    
    
    public final Guardrail getGuardrail(@Nullable GuardrailName name)

Gets details of the specified guardrail.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       GuardrailName name = GuardrailName.of("[PROJECT]", "[LOCATION]", "[APP]", "[GUARDRAIL]");
       Guardrail response = agentServiceClient.getGuardrail(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.GuardrailName`  
Required. The resource name of the guardrail to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`[Guardrail](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Guardrail)` |   
  
### getGuardrail(GetGuardrailRequest request)
    
    
    public final Guardrail getGuardrail(GetGuardrailRequest request)

Gets details of the specified guardrail.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       GetGuardrailRequest request =
           GetGuardrailRequest.newBuilder()
               .setName(
                   GuardrailName.of("[PROJECT]", "[LOCATION]", "[APP]", "[GUARDRAIL]").toString())
               .build();
       Guardrail response = agentServiceClient.getGuardrail(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetGuardrailRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.GetGuardrailRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Guardrail](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Guardrail)` |   
  
### getGuardrail(String name)
    
    
    public final Guardrail getGuardrail(String name)

Gets details of the specified guardrail.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       String name = GuardrailName.of("[PROJECT]", "[LOCATION]", "[APP]", "[GUARDRAIL]").toString();
       Guardrail response = agentServiceClient.getGuardrail(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the guardrail to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`[Guardrail](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Guardrail)` |   
  
### getGuardrailCallable()
    
    
    public final UnaryCallable<GetGuardrailRequest,Guardrail> getGuardrailCallable()

Gets details of the specified guardrail.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       GetGuardrailRequest request =
           GetGuardrailRequest.newBuilder()
               .setName(
                   GuardrailName.of("[PROJECT]", "[LOCATION]", "[APP]", "[GUARDRAIL]").toString())
               .build();
       ApiFuture<Guardrail> future = agentServiceClient.getGuardrailCallable().futureCall(request);
       // Do something.
       Guardrail response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetGuardrailRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.GetGuardrailRequest),[Guardrail](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Guardrail)>` |   
  
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
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = agentServiceClient.getLocation(request);
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
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = agentServiceClient.getLocationCallable().futureCall(request);
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
  
### getSecuritySettings(@Nullable SecuritySettingsName name)
    
    
    public final SecuritySettings getSecuritySettings(@Nullable SecuritySettingsName name)

Retrieves the security settings for the project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       SecuritySettingsName name = SecuritySettingsName.of("[PROJECT]", "[LOCATION]");
       SecuritySettings response = agentServiceClient.getSecuritySettings(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.SecuritySettingsName`  
Required. The resource name of the security settings to retrieve. Format: `projects/{project}/locations/{location}/securitySettings`  
**Returns**  
---  
**Type** | **Description**  
`[SecuritySettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.SecuritySettings)` |   
  
### getSecuritySettings(GetSecuritySettingsRequest request)
    
    
    public final SecuritySettings getSecuritySettings(GetSecuritySettingsRequest request)

Retrieves the security settings for the project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       GetSecuritySettingsRequest request =
           GetSecuritySettingsRequest.newBuilder()
               .setName(SecuritySettingsName.of("[PROJECT]", "[LOCATION]").toString())
               .build();
       SecuritySettings response = agentServiceClient.getSecuritySettings(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSecuritySettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.GetSecuritySettingsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SecuritySettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.SecuritySettings)` |   
  
### getSecuritySettings(String name)
    
    
    public final SecuritySettings getSecuritySettings(String name)

Retrieves the security settings for the project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       String name = SecuritySettingsName.of("[PROJECT]", "[LOCATION]").toString();
       SecuritySettings response = agentServiceClient.getSecuritySettings(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the security settings to retrieve. Format: `projects/{project}/locations/{location}/securitySettings`  
**Returns**  
---  
**Type** | **Description**  
`[SecuritySettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.SecuritySettings)` |   
  
### getSecuritySettingsCallable()
    
    
    public final UnaryCallable<GetSecuritySettingsRequest,SecuritySettings> getSecuritySettingsCallable()

Retrieves the security settings for the project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       GetSecuritySettingsRequest request =
           GetSecuritySettingsRequest.newBuilder()
               .setName(SecuritySettingsName.of("[PROJECT]", "[LOCATION]").toString())
               .build();
       ApiFuture<SecuritySettings> future =
           agentServiceClient.getSecuritySettingsCallable().futureCall(request);
       // Do something.
       SecuritySettings response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetSecuritySettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.GetSecuritySettingsRequest),[SecuritySettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.SecuritySettings)>` |   
  
### getSettings()
    
    
    public final @Nullable AgentServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.AgentServiceSettings` |   
  
### getStub()
    
    
    public AgentServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[AgentServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.stub.AgentServiceStub)` |   
  
### getTool(@Nullable ToolName name)
    
    
    public final Tool getTool(@Nullable ToolName name)

Gets details of the specified tool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       ToolName name = ToolName.of("[PROJECT]", "[LOCATION]", "[APP]", "[TOOL]");
       Tool response = agentServiceClient.getTool(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.ToolName`  
Required. The resource name of the tool to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`[Tool](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Tool)` |   
  
### getTool(GetToolRequest request)
    
    
    public final Tool getTool(GetToolRequest request)

Gets details of the specified tool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       GetToolRequest request =
           GetToolRequest.newBuilder()
               .setName(ToolName.of("[PROJECT]", "[LOCATION]", "[APP]", "[TOOL]").toString())
               .build();
       Tool response = agentServiceClient.getTool(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetToolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.GetToolRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Tool](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Tool)` |   
  
### getTool(String name)
    
    
    public final Tool getTool(String name)

Gets details of the specified tool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       String name = ToolName.of("[PROJECT]", "[LOCATION]", "[APP]", "[TOOL]").toString();
       Tool response = agentServiceClient.getTool(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the tool to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`[Tool](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Tool)` |   
  
### getToolCallable()
    
    
    public final UnaryCallable<GetToolRequest,Tool> getToolCallable()

Gets details of the specified tool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       GetToolRequest request =
           GetToolRequest.newBuilder()
               .setName(ToolName.of("[PROJECT]", "[LOCATION]", "[APP]", "[TOOL]").toString())
               .build();
       ApiFuture<Tool> future = agentServiceClient.getToolCallable().futureCall(request);
       // Do something.
       Tool response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetToolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.GetToolRequest),[Tool](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Tool)>` |   
  
### getToolset(@Nullable ToolsetName name)
    
    
    public final Toolset getToolset(@Nullable ToolsetName name)

Gets details of the specified toolset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       ToolsetName name = ToolsetName.of("[PROJECT]", "[LOCATION]", "[APP]", "[TOOLSET]");
       Toolset response = agentServiceClient.getToolset(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.ToolsetName`  
Required. The resource name of the toolset to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`[Toolset](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Toolset)` |   
  
### getToolset(GetToolsetRequest request)
    
    
    public final Toolset getToolset(GetToolsetRequest request)

Gets details of the specified toolset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       GetToolsetRequest request =
           GetToolsetRequest.newBuilder()
               .setName(ToolsetName.of("[PROJECT]", "[LOCATION]", "[APP]", "[TOOLSET]").toString())
               .build();
       Toolset response = agentServiceClient.getToolset(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetToolsetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.GetToolsetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Toolset](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Toolset)` |   
  
### getToolset(String name)
    
    
    public final Toolset getToolset(String name)

Gets details of the specified toolset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       String name = ToolsetName.of("[PROJECT]", "[LOCATION]", "[APP]", "[TOOLSET]").toString();
       Toolset response = agentServiceClient.getToolset(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the toolset to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`[Toolset](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Toolset)` |   
  
### getToolsetCallable()
    
    
    public final UnaryCallable<GetToolsetRequest,Toolset> getToolsetCallable()

Gets details of the specified toolset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       GetToolsetRequest request =
           GetToolsetRequest.newBuilder()
               .setName(ToolsetName.of("[PROJECT]", "[LOCATION]", "[APP]", "[TOOLSET]").toString())
               .build();
       ApiFuture<Toolset> future = agentServiceClient.getToolsetCallable().futureCall(request);
       // Do something.
       Toolset response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetToolsetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.GetToolsetRequest),[Toolset](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Toolset)>` |   
  
### importAppAsync(@Nullable LocationName parent, String displayName, String appId)
    
    
    public final OperationFuture<ImportAppResponse,OperationMetadata> importAppAsync(@Nullable LocationName parent, String displayName, String appId)

Imports the specified app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       String displayName = "displayName1714148973";
       String appId = "appId93028124";
       ImportAppResponse response =
           agentServiceClient.importAppAsync(parent, displayName, appId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.LocationName`  
Required. The parent resource name with the location of the app to import.  
`displayName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The display name of the app to import. 

  * If the app is created on import, and the display name is specified, the imported app will use this display name. If a conflict is detected with an existing app, a timestamp will be appended to the display name to make it unique. 
  * If the app is a reimport, this field should not be set. Providing a display name during reimport will result in an INVALID_ARGUMENT error. 

  
`appId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The ID to use for the imported app. 

  * If not specified, a unique ID will be automatically assigned for the app. 
  * Otherwise, the imported app will use this ID as the final component of its resource name. If an app with the same ID already exists at the specified location in the project, the content of the existing app will be replaced. 

  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ImportAppResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ImportAppResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.OperationMetadata)>` |   
  
### importAppAsync(ImportAppRequest request)
    
    
    public final OperationFuture<ImportAppResponse,OperationMetadata> importAppAsync(ImportAppRequest request)

Imports the specified app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       ImportAppRequest request =
           ImportAppRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setDisplayName("displayName1714148973")
               .setAppId("appId93028124")
               .setImportOptions(ImportAppRequest.ImportOptions.newBuilder().build())
               .setIgnoreAppLock(true)
               .build();
       ImportAppResponse response = agentServiceClient.importAppAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ImportAppRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ImportAppRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ImportAppResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ImportAppResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.OperationMetadata)>` |   
  
### importAppAsync(String parent, String displayName, String appId)
    
    
    public final OperationFuture<ImportAppResponse,OperationMetadata> importAppAsync(String parent, String displayName, String appId)

Imports the specified app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       String displayName = "displayName1714148973";
       String appId = "appId93028124";
       ImportAppResponse response =
           agentServiceClient.importAppAsync(parent, displayName, appId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource name with the location of the app to import.  
`displayName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The display name of the app to import. 

  * If the app is created on import, and the display name is specified, the imported app will use this display name. If a conflict is detected with an existing app, a timestamp will be appended to the display name to make it unique. 
  * If the app is a reimport, this field should not be set. Providing a display name during reimport will result in an INVALID_ARGUMENT error. 

  
`appId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The ID to use for the imported app. 

  * If not specified, a unique ID will be automatically assigned for the app. 
  * Otherwise, the imported app will use this ID as the final component of its resource name. If an app with the same ID already exists at the specified location in the project, the content of the existing app will be replaced. 

  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ImportAppResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ImportAppResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.OperationMetadata)>` |   
  
### importAppCallable()
    
    
    public final UnaryCallable<ImportAppRequest,Operation> importAppCallable()

Imports the specified app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       ImportAppRequest request =
           ImportAppRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setDisplayName("displayName1714148973")
               .setAppId("appId93028124")
               .setImportOptions(ImportAppRequest.ImportOptions.newBuilder().build())
               .setIgnoreAppLock(true)
               .build();
       ApiFuture<Operation> future = agentServiceClient.importAppCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ImportAppRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ImportAppRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### importAppOperationCallable()
    
    
    public final OperationCallable<ImportAppRequest,ImportAppResponse,OperationMetadata> importAppOperationCallable()

Imports the specified app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       ImportAppRequest request =
           ImportAppRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setDisplayName("displayName1714148973")
               .setAppId("appId93028124")
               .setImportOptions(ImportAppRequest.ImportOptions.newBuilder().build())
               .setIgnoreAppLock(true)
               .build();
       OperationFuture<ImportAppResponse, OperationMetadata> future =
           agentServiceClient.importAppOperationCallable().futureCall(request);
       // Do something.
       ImportAppResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ImportAppRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ImportAppRequest),[ImportAppResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ImportAppResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.OperationMetadata)>` |   
  
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
  
### listAgents(@Nullable AppName parent)
    
    
    public final AgentServiceClient.ListAgentsPagedResponse listAgents(@Nullable AppName parent)

Lists agents in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       AppName parent = AppName.of("[PROJECT]", "[LOCATION]", "[APP]");
       for (Agent element : agentServiceClient.listAgents(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.AppName`  
Required. The resource name of the app to list agents from.  
**Returns**  
---  
**Type** | **Description**  
`[AgentServiceClient.ListAgentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AgentServiceClient.ListAgentsPagedResponse)` |   
  
### listAgents(ListAgentsRequest request)
    
    
    public final AgentServiceClient.ListAgentsPagedResponse listAgents(ListAgentsRequest request)

Lists agents in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       ListAgentsRequest request =
           ListAgentsRequest.newBuilder()
               .setParent(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Agent element : agentServiceClient.listAgents(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAgentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListAgentsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AgentServiceClient.ListAgentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AgentServiceClient.ListAgentsPagedResponse)` |   
  
### listAgents(String parent)
    
    
    public final AgentServiceClient.ListAgentsPagedResponse listAgents(String parent)

Lists agents in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       String parent = AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString();
       for (Agent element : agentServiceClient.listAgents(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the app to list agents from.  
**Returns**  
---  
**Type** | **Description**  
`[AgentServiceClient.ListAgentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AgentServiceClient.ListAgentsPagedResponse)` |   
  
### listAgentsCallable()
    
    
    public final UnaryCallable<ListAgentsRequest,ListAgentsResponse> listAgentsCallable()

Lists agents in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       ListAgentsRequest request =
           ListAgentsRequest.newBuilder()
               .setParent(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListAgentsResponse response = agentServiceClient.listAgentsCallable().call(request);
         for (Agent element : response.getAgentsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAgentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListAgentsRequest),[ListAgentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListAgentsResponse)>` |   
  
### listAgentsPagedCallable()
    
    
    public final UnaryCallable<ListAgentsRequest,AgentServiceClient.ListAgentsPagedResponse> listAgentsPagedCallable()

Lists agents in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       ListAgentsRequest request =
           ListAgentsRequest.newBuilder()
               .setParent(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Agent> future = agentServiceClient.listAgentsPagedCallable().futureCall(request);
       // Do something.
       for (Agent element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAgentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListAgentsRequest),[ListAgentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AgentServiceClient.ListAgentsPagedResponse)>` |   
  
### listAppVersions(@Nullable AppName parent)
    
    
    public final AgentServiceClient.ListAppVersionsPagedResponse listAppVersions(@Nullable AppName parent)

Lists all app versions in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       AppName parent = AppName.of("[PROJECT]", "[LOCATION]", "[APP]");
       for (AppVersion element : agentServiceClient.listAppVersions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.AppName`  
Required. The resource name of the app to list app versions from.  
**Returns**  
---  
**Type** | **Description**  
`[AgentServiceClient.ListAppVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AgentServiceClient.ListAppVersionsPagedResponse)` |   
  
### listAppVersions(ListAppVersionsRequest request)
    
    
    public final AgentServiceClient.ListAppVersionsPagedResponse listAppVersions(ListAppVersionsRequest request)

Lists all app versions in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       ListAppVersionsRequest request =
           ListAppVersionsRequest.newBuilder()
               .setParent(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (AppVersion element : agentServiceClient.listAppVersions(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAppVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListAppVersionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AgentServiceClient.ListAppVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AgentServiceClient.ListAppVersionsPagedResponse)` |   
  
### listAppVersions(String parent)
    
    
    public final AgentServiceClient.ListAppVersionsPagedResponse listAppVersions(String parent)

Lists all app versions in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       String parent = AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString();
       for (AppVersion element : agentServiceClient.listAppVersions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the app to list app versions from.  
**Returns**  
---  
**Type** | **Description**  
`[AgentServiceClient.ListAppVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AgentServiceClient.ListAppVersionsPagedResponse)` |   
  
### listAppVersionsCallable()
    
    
    public final UnaryCallable<ListAppVersionsRequest,ListAppVersionsResponse> listAppVersionsCallable()

Lists all app versions in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       ListAppVersionsRequest request =
           ListAppVersionsRequest.newBuilder()
               .setParent(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListAppVersionsResponse response =
             agentServiceClient.listAppVersionsCallable().call(request);
         for (AppVersion element : response.getAppVersionsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAppVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListAppVersionsRequest),[ListAppVersionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListAppVersionsResponse)>` |   
  
### listAppVersionsPagedCallable()
    
    
    public final UnaryCallable<ListAppVersionsRequest,AgentServiceClient.ListAppVersionsPagedResponse> listAppVersionsPagedCallable()

Lists all app versions in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       ListAppVersionsRequest request =
           ListAppVersionsRequest.newBuilder()
               .setParent(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<AppVersion> future =
           agentServiceClient.listAppVersionsPagedCallable().futureCall(request);
       // Do something.
       for (AppVersion element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAppVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListAppVersionsRequest),[ListAppVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AgentServiceClient.ListAppVersionsPagedResponse)>` |   
  
### listApps(@Nullable LocationName parent)
    
    
    public final AgentServiceClient.ListAppsPagedResponse listApps(@Nullable LocationName parent)

Lists apps in the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (App element : agentServiceClient.listApps(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.LocationName`  
Required. The resource name of the location to list apps from.  
**Returns**  
---  
**Type** | **Description**  
`[AgentServiceClient.ListAppsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AgentServiceClient.ListAppsPagedResponse)` |   
  
### listApps(ListAppsRequest request)
    
    
    public final AgentServiceClient.ListAppsPagedResponse listApps(ListAppsRequest request)

Lists apps in the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       ListAppsRequest request =
           ListAppsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (App element : agentServiceClient.listApps(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAppsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListAppsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AgentServiceClient.ListAppsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AgentServiceClient.ListAppsPagedResponse)` |   
  
### listApps(String parent)
    
    
    public final AgentServiceClient.ListAppsPagedResponse listApps(String parent)

Lists apps in the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (App element : agentServiceClient.listApps(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the location to list apps from.  
**Returns**  
---  
**Type** | **Description**  
`[AgentServiceClient.ListAppsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AgentServiceClient.ListAppsPagedResponse)` |   
  
### listAppsCallable()
    
    
    public final UnaryCallable<ListAppsRequest,ListAppsResponse> listAppsCallable()

Lists apps in the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       ListAppsRequest request =
           ListAppsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListAppsResponse response = agentServiceClient.listAppsCallable().call(request);
         for (App element : response.getAppsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAppsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListAppsRequest),[ListAppsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListAppsResponse)>` |   
  
### listAppsPagedCallable()
    
    
    public final UnaryCallable<ListAppsRequest,AgentServiceClient.ListAppsPagedResponse> listAppsPagedCallable()

Lists apps in the given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       ListAppsRequest request =
           ListAppsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<App> future = agentServiceClient.listAppsPagedCallable().futureCall(request);
       // Do something.
       for (App element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAppsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListAppsRequest),[ListAppsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AgentServiceClient.ListAppsPagedResponse)>` |   
  
### listChangelogs(@Nullable AppName parent)
    
    
    public final AgentServiceClient.ListChangelogsPagedResponse listChangelogs(@Nullable AppName parent)

Lists the changelogs of the specified app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       AppName parent = AppName.of("[PROJECT]", "[LOCATION]", "[APP]");
       for (Changelog element : agentServiceClient.listChangelogs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.AppName`  
Required. The resource name of the app to list changelogs from.  
**Returns**  
---  
**Type** | **Description**  
`[AgentServiceClient.ListChangelogsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AgentServiceClient.ListChangelogsPagedResponse)` |   
  
### listChangelogs(ListChangelogsRequest request)
    
    
    public final AgentServiceClient.ListChangelogsPagedResponse listChangelogs(ListChangelogsRequest request)

Lists the changelogs of the specified app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       ListChangelogsRequest request =
           ListChangelogsRequest.newBuilder()
               .setParent(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Changelog element : agentServiceClient.listChangelogs(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListChangelogsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListChangelogsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AgentServiceClient.ListChangelogsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AgentServiceClient.ListChangelogsPagedResponse)` |   
  
### listChangelogs(String parent)
    
    
    public final AgentServiceClient.ListChangelogsPagedResponse listChangelogs(String parent)

Lists the changelogs of the specified app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       String parent = AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString();
       for (Changelog element : agentServiceClient.listChangelogs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the app to list changelogs from.  
**Returns**  
---  
**Type** | **Description**  
`[AgentServiceClient.ListChangelogsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AgentServiceClient.ListChangelogsPagedResponse)` |   
  
### listChangelogsCallable()
    
    
    public final UnaryCallable<ListChangelogsRequest,ListChangelogsResponse> listChangelogsCallable()

Lists the changelogs of the specified app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       ListChangelogsRequest request =
           ListChangelogsRequest.newBuilder()
               .setParent(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListChangelogsResponse response = agentServiceClient.listChangelogsCallable().call(request);
         for (Changelog element : response.getChangelogsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListChangelogsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListChangelogsRequest),[ListChangelogsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListChangelogsResponse)>` |   
  
### listChangelogsPagedCallable()
    
    
    public final UnaryCallable<ListChangelogsRequest,AgentServiceClient.ListChangelogsPagedResponse> listChangelogsPagedCallable()

Lists the changelogs of the specified app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       ListChangelogsRequest request =
           ListChangelogsRequest.newBuilder()
               .setParent(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Changelog> future =
           agentServiceClient.listChangelogsPagedCallable().futureCall(request);
       // Do something.
       for (Changelog element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListChangelogsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListChangelogsRequest),[ListChangelogsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AgentServiceClient.ListChangelogsPagedResponse)>` |   
  
### listConversations(@Nullable AppName parent)
    
    
    public final AgentServiceClient.ListConversationsPagedResponse listConversations(@Nullable AppName parent)

Lists conversations in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       AppName parent = AppName.of("[PROJECT]", "[LOCATION]", "[APP]");
       for (Conversation element : agentServiceClient.listConversations(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.AppName`  
Required. The resource name of the app to list conversations from.  
**Returns**  
---  
**Type** | **Description**  
`[AgentServiceClient.ListConversationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AgentServiceClient.ListConversationsPagedResponse)` |   
  
### listConversations(ListConversationsRequest request)
    
    
    public final AgentServiceClient.ListConversationsPagedResponse listConversations(ListConversationsRequest request)

Lists conversations in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       ListConversationsRequest request =
           ListConversationsRequest.newBuilder()
               .setParent(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .addAllSources(new ArrayList<Conversation.Source>())
               .build();
       for (Conversation element : agentServiceClient.listConversations(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListConversationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListConversationsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AgentServiceClient.ListConversationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AgentServiceClient.ListConversationsPagedResponse)` |   
  
### listConversations(String parent)
    
    
    public final AgentServiceClient.ListConversationsPagedResponse listConversations(String parent)

Lists conversations in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       String parent = AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString();
       for (Conversation element : agentServiceClient.listConversations(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the app to list conversations from.  
**Returns**  
---  
**Type** | **Description**  
`[AgentServiceClient.ListConversationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AgentServiceClient.ListConversationsPagedResponse)` |   
  
### listConversationsCallable()
    
    
    public final UnaryCallable<ListConversationsRequest,ListConversationsResponse> listConversationsCallable()

Lists conversations in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       ListConversationsRequest request =
           ListConversationsRequest.newBuilder()
               .setParent(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .addAllSources(new ArrayList<Conversation.Source>())
               .build();
       while (true) {
         ListConversationsResponse response =
             agentServiceClient.listConversationsCallable().call(request);
         for (Conversation element : response.getConversationsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListConversationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListConversationsRequest),[ListConversationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListConversationsResponse)>` |   
  
### listConversationsPagedCallable()
    
    
    public final UnaryCallable<ListConversationsRequest,AgentServiceClient.ListConversationsPagedResponse> listConversationsPagedCallable()

Lists conversations in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       ListConversationsRequest request =
           ListConversationsRequest.newBuilder()
               .setParent(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .addAllSources(new ArrayList<Conversation.Source>())
               .build();
       ApiFuture<Conversation> future =
           agentServiceClient.listConversationsPagedCallable().futureCall(request);
       // Do something.
       for (Conversation element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListConversationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListConversationsRequest),[ListConversationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AgentServiceClient.ListConversationsPagedResponse)>` |   
  
### listDeployments(@Nullable AppName parent)
    
    
    public final AgentServiceClient.ListDeploymentsPagedResponse listDeployments(@Nullable AppName parent)

Lists deployments in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       AppName parent = AppName.of("[PROJECT]", "[LOCATION]", "[APP]");
       for (Deployment element : agentServiceClient.listDeployments(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.AppName`  
Required. The parent app. Format: `projects/{project}/locations/{location}/apps/{app}`  
**Returns**  
---  
**Type** | **Description**  
`[AgentServiceClient.ListDeploymentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AgentServiceClient.ListDeploymentsPagedResponse)` |   
  
### listDeployments(ListDeploymentsRequest request)
    
    
    public final AgentServiceClient.ListDeploymentsPagedResponse listDeployments(ListDeploymentsRequest request)

Lists deployments in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       ListDeploymentsRequest request =
           ListDeploymentsRequest.newBuilder()
               .setParent(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Deployment element : agentServiceClient.listDeployments(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDeploymentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListDeploymentsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AgentServiceClient.ListDeploymentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AgentServiceClient.ListDeploymentsPagedResponse)` |   
  
### listDeployments(String parent)
    
    
    public final AgentServiceClient.ListDeploymentsPagedResponse listDeployments(String parent)

Lists deployments in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       String parent = AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString();
       for (Deployment element : agentServiceClient.listDeployments(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent app. Format: `projects/{project}/locations/{location}/apps/{app}`  
**Returns**  
---  
**Type** | **Description**  
`[AgentServiceClient.ListDeploymentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AgentServiceClient.ListDeploymentsPagedResponse)` |   
  
### listDeploymentsCallable()
    
    
    public final UnaryCallable<ListDeploymentsRequest,ListDeploymentsResponse> listDeploymentsCallable()

Lists deployments in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       ListDeploymentsRequest request =
           ListDeploymentsRequest.newBuilder()
               .setParent(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListDeploymentsResponse response =
             agentServiceClient.listDeploymentsCallable().call(request);
         for (Deployment element : response.getDeploymentsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDeploymentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListDeploymentsRequest),[ListDeploymentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListDeploymentsResponse)>` |   
  
### listDeploymentsPagedCallable()
    
    
    public final UnaryCallable<ListDeploymentsRequest,AgentServiceClient.ListDeploymentsPagedResponse> listDeploymentsPagedCallable()

Lists deployments in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       ListDeploymentsRequest request =
           ListDeploymentsRequest.newBuilder()
               .setParent(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Deployment> future =
           agentServiceClient.listDeploymentsPagedCallable().futureCall(request);
       // Do something.
       for (Deployment element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDeploymentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListDeploymentsRequest),[ListDeploymentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AgentServiceClient.ListDeploymentsPagedResponse)>` |   
  
### listExamples(@Nullable AppName parent)
    
    
    public final AgentServiceClient.ListExamplesPagedResponse listExamples(@Nullable AppName parent)

Lists examples in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       AppName parent = AppName.of("[PROJECT]", "[LOCATION]", "[APP]");
       for (Example element : agentServiceClient.listExamples(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.AppName`  
Required. The resource name of the app to list examples from.  
**Returns**  
---  
**Type** | **Description**  
`[AgentServiceClient.ListExamplesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AgentServiceClient.ListExamplesPagedResponse)` |   
  
### listExamples(ListExamplesRequest request)
    
    
    public final AgentServiceClient.ListExamplesPagedResponse listExamples(ListExamplesRequest request)

Lists examples in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       ListExamplesRequest request =
           ListExamplesRequest.newBuilder()
               .setParent(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Example element : agentServiceClient.listExamples(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListExamplesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListExamplesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AgentServiceClient.ListExamplesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AgentServiceClient.ListExamplesPagedResponse)` |   
  
### listExamples(String parent)
    
    
    public final AgentServiceClient.ListExamplesPagedResponse listExamples(String parent)

Lists examples in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       String parent = AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString();
       for (Example element : agentServiceClient.listExamples(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the app to list examples from.  
**Returns**  
---  
**Type** | **Description**  
`[AgentServiceClient.ListExamplesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AgentServiceClient.ListExamplesPagedResponse)` |   
  
### listExamplesCallable()
    
    
    public final UnaryCallable<ListExamplesRequest,ListExamplesResponse> listExamplesCallable()

Lists examples in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       ListExamplesRequest request =
           ListExamplesRequest.newBuilder()
               .setParent(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListExamplesResponse response = agentServiceClient.listExamplesCallable().call(request);
         for (Example element : response.getExamplesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListExamplesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListExamplesRequest),[ListExamplesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListExamplesResponse)>` |   
  
### listExamplesPagedCallable()
    
    
    public final UnaryCallable<ListExamplesRequest,AgentServiceClient.ListExamplesPagedResponse> listExamplesPagedCallable()

Lists examples in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       ListExamplesRequest request =
           ListExamplesRequest.newBuilder()
               .setParent(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Example> future =
           agentServiceClient.listExamplesPagedCallable().futureCall(request);
       // Do something.
       for (Example element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListExamplesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListExamplesRequest),[ListExamplesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AgentServiceClient.ListExamplesPagedResponse)>` |   
  
### listGuardrails(@Nullable AppName parent)
    
    
    public final AgentServiceClient.ListGuardrailsPagedResponse listGuardrails(@Nullable AppName parent)

Lists guardrails in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       AppName parent = AppName.of("[PROJECT]", "[LOCATION]", "[APP]");
       for (Guardrail element : agentServiceClient.listGuardrails(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.AppName`  
Required. The resource name of the app to list guardrails from.  
**Returns**  
---  
**Type** | **Description**  
`[AgentServiceClient.ListGuardrailsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AgentServiceClient.ListGuardrailsPagedResponse)` |   
  
### listGuardrails(ListGuardrailsRequest request)
    
    
    public final AgentServiceClient.ListGuardrailsPagedResponse listGuardrails(ListGuardrailsRequest request)

Lists guardrails in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       ListGuardrailsRequest request =
           ListGuardrailsRequest.newBuilder()
               .setParent(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Guardrail element : agentServiceClient.listGuardrails(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListGuardrailsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListGuardrailsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AgentServiceClient.ListGuardrailsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AgentServiceClient.ListGuardrailsPagedResponse)` |   
  
### listGuardrails(String parent)
    
    
    public final AgentServiceClient.ListGuardrailsPagedResponse listGuardrails(String parent)

Lists guardrails in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       String parent = AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString();
       for (Guardrail element : agentServiceClient.listGuardrails(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the app to list guardrails from.  
**Returns**  
---  
**Type** | **Description**  
`[AgentServiceClient.ListGuardrailsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AgentServiceClient.ListGuardrailsPagedResponse)` |   
  
### listGuardrailsCallable()
    
    
    public final UnaryCallable<ListGuardrailsRequest,ListGuardrailsResponse> listGuardrailsCallable()

Lists guardrails in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       ListGuardrailsRequest request =
           ListGuardrailsRequest.newBuilder()
               .setParent(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListGuardrailsResponse response = agentServiceClient.listGuardrailsCallable().call(request);
         for (Guardrail element : response.getGuardrailsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGuardrailsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListGuardrailsRequest),[ListGuardrailsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListGuardrailsResponse)>` |   
  
### listGuardrailsPagedCallable()
    
    
    public final UnaryCallable<ListGuardrailsRequest,AgentServiceClient.ListGuardrailsPagedResponse> listGuardrailsPagedCallable()

Lists guardrails in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       ListGuardrailsRequest request =
           ListGuardrailsRequest.newBuilder()
               .setParent(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Guardrail> future =
           agentServiceClient.listGuardrailsPagedCallable().futureCall(request);
       // Do something.
       for (Guardrail element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGuardrailsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListGuardrailsRequest),[ListGuardrailsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AgentServiceClient.ListGuardrailsPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final AgentServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : agentServiceClient.listLocations(request).iterateAll()) {
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
`[AgentServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AgentServiceClient.ListLocationsPagedResponse)` |   
  
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
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response = agentServiceClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,AgentServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           agentServiceClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AgentServiceClient.ListLocationsPagedResponse)>` |   
  
### listTools(@Nullable AppName parent)
    
    
    public final AgentServiceClient.ListToolsPagedResponse listTools(@Nullable AppName parent)

Lists tools in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       AppName parent = AppName.of("[PROJECT]", "[LOCATION]", "[APP]");
       for (Tool element : agentServiceClient.listTools(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.AppName`  
Required. The resource name of the app to list tools from.  
**Returns**  
---  
**Type** | **Description**  
`[AgentServiceClient.ListToolsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AgentServiceClient.ListToolsPagedResponse)` |   
  
### listTools(ListToolsRequest request)
    
    
    public final AgentServiceClient.ListToolsPagedResponse listTools(ListToolsRequest request)

Lists tools in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       ListToolsRequest request =
           ListToolsRequest.newBuilder()
               .setParent(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Tool element : agentServiceClient.listTools(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListToolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListToolsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AgentServiceClient.ListToolsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AgentServiceClient.ListToolsPagedResponse)` |   
  
### listTools(String parent)
    
    
    public final AgentServiceClient.ListToolsPagedResponse listTools(String parent)

Lists tools in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       String parent = AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString();
       for (Tool element : agentServiceClient.listTools(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the app to list tools from.  
**Returns**  
---  
**Type** | **Description**  
`[AgentServiceClient.ListToolsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AgentServiceClient.ListToolsPagedResponse)` |   
  
### listToolsCallable()
    
    
    public final UnaryCallable<ListToolsRequest,ListToolsResponse> listToolsCallable()

Lists tools in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       ListToolsRequest request =
           ListToolsRequest.newBuilder()
               .setParent(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListToolsResponse response = agentServiceClient.listToolsCallable().call(request);
         for (Tool element : response.getToolsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListToolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListToolsRequest),[ListToolsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListToolsResponse)>` |   
  
### listToolsPagedCallable()
    
    
    public final UnaryCallable<ListToolsRequest,AgentServiceClient.ListToolsPagedResponse> listToolsPagedCallable()

Lists tools in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       ListToolsRequest request =
           ListToolsRequest.newBuilder()
               .setParent(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Tool> future = agentServiceClient.listToolsPagedCallable().futureCall(request);
       // Do something.
       for (Tool element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListToolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListToolsRequest),[ListToolsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AgentServiceClient.ListToolsPagedResponse)>` |   
  
### listToolsets(@Nullable AppName parent)
    
    
    public final AgentServiceClient.ListToolsetsPagedResponse listToolsets(@Nullable AppName parent)

Lists toolsets in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       AppName parent = AppName.of("[PROJECT]", "[LOCATION]", "[APP]");
       for (Toolset element : agentServiceClient.listToolsets(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.AppName`  
Required. The resource name of the app to list toolsets from.  
**Returns**  
---  
**Type** | **Description**  
`[AgentServiceClient.ListToolsetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AgentServiceClient.ListToolsetsPagedResponse)` |   
  
### listToolsets(ListToolsetsRequest request)
    
    
    public final AgentServiceClient.ListToolsetsPagedResponse listToolsets(ListToolsetsRequest request)

Lists toolsets in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       ListToolsetsRequest request =
           ListToolsetsRequest.newBuilder()
               .setParent(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Toolset element : agentServiceClient.listToolsets(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListToolsetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListToolsetsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AgentServiceClient.ListToolsetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AgentServiceClient.ListToolsetsPagedResponse)` |   
  
### listToolsets(String parent)
    
    
    public final AgentServiceClient.ListToolsetsPagedResponse listToolsets(String parent)

Lists toolsets in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       String parent = AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString();
       for (Toolset element : agentServiceClient.listToolsets(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the app to list toolsets from.  
**Returns**  
---  
**Type** | **Description**  
`[AgentServiceClient.ListToolsetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AgentServiceClient.ListToolsetsPagedResponse)` |   
  
### listToolsetsCallable()
    
    
    public final UnaryCallable<ListToolsetsRequest,ListToolsetsResponse> listToolsetsCallable()

Lists toolsets in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       ListToolsetsRequest request =
           ListToolsetsRequest.newBuilder()
               .setParent(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListToolsetsResponse response = agentServiceClient.listToolsetsCallable().call(request);
         for (Toolset element : response.getToolsetsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListToolsetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListToolsetsRequest),[ListToolsetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListToolsetsResponse)>` |   
  
### listToolsetsPagedCallable()
    
    
    public final UnaryCallable<ListToolsetsRequest,AgentServiceClient.ListToolsetsPagedResponse> listToolsetsPagedCallable()

Lists toolsets in the given app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       ListToolsetsRequest request =
           ListToolsetsRequest.newBuilder()
               .setParent(AppName.of("[PROJECT]", "[LOCATION]", "[APP]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Toolset> future =
           agentServiceClient.listToolsetsPagedCallable().futureCall(request);
       // Do something.
       for (Toolset element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListToolsetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListToolsetsRequest),[ListToolsetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.AgentServiceClient.ListToolsetsPagedResponse)>` |   
  
### restoreAppVersionAsync(@Nullable AppVersionName name)
    
    
    public final OperationFuture<RestoreAppVersionResponse,OperationMetadata> restoreAppVersionAsync(@Nullable AppVersionName name)

Restores the specified app version. This will create a new app version from the current draft app and overwrite the current draft with the specified app version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       AppVersionName name = AppVersionName.of("[PROJECT]", "[LOCATION]", "[APP]", "[VERSION]");
       RestoreAppVersionResponse response = agentServiceClient.restoreAppVersionAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.ces.v1beta.AppVersionName`  
Required. The resource name of the app version to restore.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[RestoreAppVersionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.RestoreAppVersionResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.OperationMetadata)>` |   
  
### restoreAppVersionAsync(RestoreAppVersionRequest request)
    
    
    public final OperationFuture<RestoreAppVersionResponse,OperationMetadata> restoreAppVersionAsync(RestoreAppVersionRequest request)

Restores the specified app version. This will create a new app version from the current draft app and overwrite the current draft with the specified app version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       RestoreAppVersionRequest request =
           RestoreAppVersionRequest.newBuilder()
               .setName(
                   AppVersionName.of("[PROJECT]", "[LOCATION]", "[APP]", "[VERSION]").toString())
               .build();
       RestoreAppVersionResponse response = agentServiceClient.restoreAppVersionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RestoreAppVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.RestoreAppVersionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[RestoreAppVersionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.RestoreAppVersionResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.OperationMetadata)>` |   
  
### restoreAppVersionAsync(String name)
    
    
    public final OperationFuture<RestoreAppVersionResponse,OperationMetadata> restoreAppVersionAsync(String name)

Restores the specified app version. This will create a new app version from the current draft app and overwrite the current draft with the specified app version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       String name = AppVersionName.of("[PROJECT]", "[LOCATION]", "[APP]", "[VERSION]").toString();
       RestoreAppVersionResponse response = agentServiceClient.restoreAppVersionAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the app version to restore.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[RestoreAppVersionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.RestoreAppVersionResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.OperationMetadata)>` |   
  
### restoreAppVersionCallable()
    
    
    public final UnaryCallable<RestoreAppVersionRequest,Operation> restoreAppVersionCallable()

Restores the specified app version. This will create a new app version from the current draft app and overwrite the current draft with the specified app version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       RestoreAppVersionRequest request =
           RestoreAppVersionRequest.newBuilder()
               .setName(
                   AppVersionName.of("[PROJECT]", "[LOCATION]", "[APP]", "[VERSION]").toString())
               .build();
       ApiFuture<Operation> future =
           agentServiceClient.restoreAppVersionCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RestoreAppVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.RestoreAppVersionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### restoreAppVersionOperationCallable()
    
    
    public final OperationCallable<RestoreAppVersionRequest,RestoreAppVersionResponse,OperationMetadata> restoreAppVersionOperationCallable()

Restores the specified app version. This will create a new app version from the current draft app and overwrite the current draft with the specified app version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       RestoreAppVersionRequest request =
           RestoreAppVersionRequest.newBuilder()
               .setName(
                   AppVersionName.of("[PROJECT]", "[LOCATION]", "[APP]", "[VERSION]").toString())
               .build();
       OperationFuture<RestoreAppVersionResponse, OperationMetadata> future =
           agentServiceClient.restoreAppVersionOperationCallable().futureCall(request);
       // Do something.
       RestoreAppVersionResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RestoreAppVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.RestoreAppVersionRequest),[RestoreAppVersionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.RestoreAppVersionResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.OperationMetadata)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateAgent(Agent agent, FieldMask updateMask)
    
    
    public final Agent updateAgent(Agent agent, FieldMask updateMask)

Updates the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       Agent agent = Agent.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Agent response = agentServiceClient.updateAgent(agent, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`agent` | `[Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Agent)`  
Required. The agent to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Field mask is used to control which fields get updated. If the mask is not present, all fields will be updated.  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Agent)` |   
  
### updateAgent(UpdateAgentRequest request)
    
    
    public final Agent updateAgent(UpdateAgentRequest request)

Updates the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       UpdateAgentRequest request =
           UpdateAgentRequest.newBuilder()
               .setAgent(Agent.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Agent response = agentServiceClient.updateAgent(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.UpdateAgentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Agent)` |   
  
### updateAgentCallable()
    
    
    public final UnaryCallable<UpdateAgentRequest,Agent> updateAgentCallable()

Updates the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       UpdateAgentRequest request =
           UpdateAgentRequest.newBuilder()
               .setAgent(Agent.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Agent> future = agentServiceClient.updateAgentCallable().futureCall(request);
       // Do something.
       Agent response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.UpdateAgentRequest),[Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Agent)>` |   
  
### updateApp(App app, FieldMask updateMask)
    
    
    public final App updateApp(App app, FieldMask updateMask)

Updates the specified app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       App app = App.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       App response = agentServiceClient.updateApp(app, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`app` | `[App](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.App)`  
Required. The app to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Field mask is used to control which fields get updated. If the mask is not present, all fields will be updated.  
**Returns**  
---  
**Type** | **Description**  
`[App](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.App)` |   
  
### updateApp(UpdateAppRequest request)
    
    
    public final App updateApp(UpdateAppRequest request)

Updates the specified app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       UpdateAppRequest request =
           UpdateAppRequest.newBuilder()
               .setApp(App.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       App response = agentServiceClient.updateApp(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateAppRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.UpdateAppRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[App](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.App)` |   
  
### updateAppCallable()
    
    
    public final UnaryCallable<UpdateAppRequest,App> updateAppCallable()

Updates the specified app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       UpdateAppRequest request =
           UpdateAppRequest.newBuilder()
               .setApp(App.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<App> future = agentServiceClient.updateAppCallable().futureCall(request);
       // Do something.
       App response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateAppRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.UpdateAppRequest),[App](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.App)>` |   
  
### updateDeployment(Deployment deployment, FieldMask updateMask)
    
    
    public final Deployment updateDeployment(Deployment deployment, FieldMask updateMask)

Updates the specified deployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       Deployment deployment = Deployment.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Deployment response = agentServiceClient.updateDeployment(deployment, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`deployment` | `[Deployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Deployment)`  
Required. The deployment to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The list of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[Deployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Deployment)` |   
  
### updateDeployment(UpdateDeploymentRequest request)
    
    
    public final Deployment updateDeployment(UpdateDeploymentRequest request)

Updates the specified deployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       UpdateDeploymentRequest request =
           UpdateDeploymentRequest.newBuilder()
               .setDeployment(Deployment.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Deployment response = agentServiceClient.updateDeployment(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.UpdateDeploymentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Deployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Deployment)` |   
  
### updateDeploymentCallable()
    
    
    public final UnaryCallable<UpdateDeploymentRequest,Deployment> updateDeploymentCallable()

Updates the specified deployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       UpdateDeploymentRequest request =
           UpdateDeploymentRequest.newBuilder()
               .setDeployment(Deployment.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Deployment> future =
           agentServiceClient.updateDeploymentCallable().futureCall(request);
       // Do something.
       Deployment response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.UpdateDeploymentRequest),[Deployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Deployment)>` |   
  
### updateExample(Example example, FieldMask updateMask)
    
    
    public final Example updateExample(Example example, FieldMask updateMask)

Updates the specified example.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       Example example = Example.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Example response = agentServiceClient.updateExample(example, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`example` | `[Example](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Example)`  
Required. The example to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Field mask is used to control which fields get updated. If the mask is not present, all fields will be updated.  
**Returns**  
---  
**Type** | **Description**  
`[Example](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Example)` |   
  
### updateExample(UpdateExampleRequest request)
    
    
    public final Example updateExample(UpdateExampleRequest request)

Updates the specified example.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       UpdateExampleRequest request =
           UpdateExampleRequest.newBuilder()
               .setExample(Example.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Example response = agentServiceClient.updateExample(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateExampleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.UpdateExampleRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Example](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Example)` |   
  
### updateExampleCallable()
    
    
    public final UnaryCallable<UpdateExampleRequest,Example> updateExampleCallable()

Updates the specified example.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       UpdateExampleRequest request =
           UpdateExampleRequest.newBuilder()
               .setExample(Example.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Example> future = agentServiceClient.updateExampleCallable().futureCall(request);
       // Do something.
       Example response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateExampleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.UpdateExampleRequest),[Example](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Example)>` |   
  
### updateGuardrail(Guardrail guardrail, FieldMask updateMask)
    
    
    public final Guardrail updateGuardrail(Guardrail guardrail, FieldMask updateMask)

Updates the specified guardrail.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       Guardrail guardrail = Guardrail.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Guardrail response = agentServiceClient.updateGuardrail(guardrail, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`guardrail` | `[Guardrail](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Guardrail)`  
Required. The guardrail to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Field mask is used to control which fields get updated. If the mask is not present, all fields will be updated.  
**Returns**  
---  
**Type** | **Description**  
`[Guardrail](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Guardrail)` |   
  
### updateGuardrail(UpdateGuardrailRequest request)
    
    
    public final Guardrail updateGuardrail(UpdateGuardrailRequest request)

Updates the specified guardrail.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       UpdateGuardrailRequest request =
           UpdateGuardrailRequest.newBuilder()
               .setGuardrail(Guardrail.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Guardrail response = agentServiceClient.updateGuardrail(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateGuardrailRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.UpdateGuardrailRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Guardrail](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Guardrail)` |   
  
### updateGuardrailCallable()
    
    
    public final UnaryCallable<UpdateGuardrailRequest,Guardrail> updateGuardrailCallable()

Updates the specified guardrail.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       UpdateGuardrailRequest request =
           UpdateGuardrailRequest.newBuilder()
               .setGuardrail(Guardrail.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Guardrail> future =
           agentServiceClient.updateGuardrailCallable().futureCall(request);
       // Do something.
       Guardrail response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateGuardrailRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.UpdateGuardrailRequest),[Guardrail](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Guardrail)>` |   
  
### updateSecuritySettings(SecuritySettings securitySettings, FieldMask updateMask)
    
    
    public final SecuritySettings updateSecuritySettings(SecuritySettings securitySettings, FieldMask updateMask)

Updates the security settings for the project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       SecuritySettings securitySettings = SecuritySettings.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       SecuritySettings response =
           agentServiceClient.updateSecuritySettings(securitySettings, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`securitySettings` | `[SecuritySettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.SecuritySettings)`  
Required. The security settings to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Field mask is used to control which fields get updated. If the mask is not present, all fields will be updated.  
**Returns**  
---  
**Type** | **Description**  
`[SecuritySettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.SecuritySettings)` |   
  
### updateSecuritySettings(UpdateSecuritySettingsRequest request)
    
    
    public final SecuritySettings updateSecuritySettings(UpdateSecuritySettingsRequest request)

Updates the security settings for the project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       UpdateSecuritySettingsRequest request =
           UpdateSecuritySettingsRequest.newBuilder()
               .setSecuritySettings(SecuritySettings.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       SecuritySettings response = agentServiceClient.updateSecuritySettings(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateSecuritySettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.UpdateSecuritySettingsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SecuritySettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.SecuritySettings)` |   
  
### updateSecuritySettingsCallable()
    
    
    public final UnaryCallable<UpdateSecuritySettingsRequest,SecuritySettings> updateSecuritySettingsCallable()

Updates the security settings for the project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       UpdateSecuritySettingsRequest request =
           UpdateSecuritySettingsRequest.newBuilder()
               .setSecuritySettings(SecuritySettings.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<SecuritySettings> future =
           agentServiceClient.updateSecuritySettingsCallable().futureCall(request);
       // Do something.
       SecuritySettings response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateSecuritySettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.UpdateSecuritySettingsRequest),[SecuritySettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.SecuritySettings)>` |   
  
### updateTool(Tool tool, FieldMask updateMask)
    
    
    public final Tool updateTool(Tool tool, FieldMask updateMask)

Updates the specified tool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       Tool tool = Tool.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Tool response = agentServiceClient.updateTool(tool, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`tool` | `[Tool](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Tool)`  
Required. The tool to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Field mask is used to control which fields get updated. If the mask is not present, all fields will be updated.  
**Returns**  
---  
**Type** | **Description**  
`[Tool](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Tool)` |   
  
### updateTool(UpdateToolRequest request)
    
    
    public final Tool updateTool(UpdateToolRequest request)

Updates the specified tool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       UpdateToolRequest request =
           UpdateToolRequest.newBuilder()
               .setTool(Tool.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Tool response = agentServiceClient.updateTool(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateToolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.UpdateToolRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Tool](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Tool)` |   
  
### updateToolCallable()
    
    
    public final UnaryCallable<UpdateToolRequest,Tool> updateToolCallable()

Updates the specified tool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       UpdateToolRequest request =
           UpdateToolRequest.newBuilder()
               .setTool(Tool.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Tool> future = agentServiceClient.updateToolCallable().futureCall(request);
       // Do something.
       Tool response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateToolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.UpdateToolRequest),[Tool](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Tool)>` |   
  
### updateToolset(Toolset toolset, FieldMask updateMask)
    
    
    public final Toolset updateToolset(Toolset toolset, FieldMask updateMask)

Updates the specified toolset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       Toolset toolset = Toolset.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Toolset response = agentServiceClient.updateToolset(toolset, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`toolset` | `[Toolset](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Toolset)`  
Required. The toolset to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Field mask is used to control which fields get updated. If the mask is not present, all fields will be updated.  
**Returns**  
---  
**Type** | **Description**  
`[Toolset](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Toolset)` |   
  
### updateToolset(UpdateToolsetRequest request)
    
    
    public final Toolset updateToolset(UpdateToolsetRequest request)

Updates the specified toolset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       UpdateToolsetRequest request =
           UpdateToolsetRequest.newBuilder()
               .setToolset(Toolset.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Toolset response = agentServiceClient.updateToolset(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateToolsetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.UpdateToolsetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Toolset](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Toolset)` |   
  
### updateToolsetCallable()
    
    
    public final UnaryCallable<UpdateToolsetRequest,Toolset> updateToolsetCallable()

Updates the specified toolset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentServiceClient agentServiceClient = AgentServiceClient.create()) {
       UpdateToolsetRequest request =
           UpdateToolsetRequest.newBuilder()
               .setToolset(Toolset.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Toolset> future = agentServiceClient.updateToolsetCallable().futureCall(request);
       // Do something.
       Toolset response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateToolsetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.UpdateToolsetRequest),[Toolset](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Toolset)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
