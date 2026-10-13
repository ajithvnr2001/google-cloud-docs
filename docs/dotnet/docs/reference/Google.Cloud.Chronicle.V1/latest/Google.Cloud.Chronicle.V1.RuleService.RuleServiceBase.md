---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.RuleService.RuleServiceBase
title: Chronicle v1 API - Class RuleService.RuleServiceBase (1.1.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:16:46.250851+00:00
---

# Chronicle v1 API - Class RuleService.RuleServiceBase (1.1.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.RuleService.RuleServiceBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Chronicle v1 API - Class RuleService.RuleServiceBase (1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0 
    
    
    [BindServiceMethod(typeof(RuleService), "BindService")]
    public abstract class RuleService.RuleServiceBase

Reference documentation and code samples for the Chronicle v1 API class RuleService.RuleServiceBase.

Base class for server-side implementations of RuleService

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > RuleService.RuleServiceBase

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Chronicle.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1)

## Assembly

Google.Cloud.Chronicle.V1.dll

## Methods 

### CreateRetrohunt(CreateRetrohuntRequest, ServerCallContext)
    
    
    public virtual Task<Operation> CreateRetrohunt(CreateRetrohuntRequest request, ServerCallContext context)

Create a Retrohunt.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateRetrohuntRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CreateRetrohuntRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### CreateRule(CreateRuleRequest, ServerCallContext)
    
    
    public virtual Task<Rule> CreateRule(CreateRuleRequest request, ServerCallContext context)

Creates a new Rule.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateRuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CreateRuleRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Rule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.Rule)` | The response to send back to the client (wrapped by a task).  
  
### DeleteRule(DeleteRuleRequest, ServerCallContext)
    
    
    public virtual Task<Empty> DeleteRule(DeleteRuleRequest request, ServerCallContext context)

Deletes a Rule.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteRuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DeleteRuleRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response to send back to the client (wrapped by a task).  
  
### GetRetrohunt(GetRetrohuntRequest, ServerCallContext)
    
    
    public virtual Task<Retrohunt> GetRetrohunt(GetRetrohuntRequest request, ServerCallContext context)

Get a Retrohunt.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRetrohuntRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.GetRetrohuntRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Retrohunt](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.Retrohunt)` | The response to send back to the client (wrapped by a task).  
  
### GetRule(GetRuleRequest, ServerCallContext)
    
    
    public virtual Task<Rule> GetRule(GetRuleRequest request, ServerCallContext context)

Gets a Rule.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.GetRuleRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Rule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.Rule)` | The response to send back to the client (wrapped by a task).  
  
### GetRuleDeployment(GetRuleDeploymentRequest, ServerCallContext)
    
    
    public virtual Task<RuleDeployment> GetRuleDeployment(GetRuleDeploymentRequest request, ServerCallContext context)

Gets a RuleDeployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRuleDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.GetRuleDeploymentRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[RuleDeployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.RuleDeployment)` | The response to send back to the client (wrapped by a task).  
  
### ListRetrohunts(ListRetrohuntsRequest, ServerCallContext)
    
    
    public virtual Task<ListRetrohuntsResponse> ListRetrohunts(ListRetrohuntsRequest request, ServerCallContext context)

List Retrohunts.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRetrohuntsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.ListRetrohuntsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListRetrohuntsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.ListRetrohuntsResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListRuleDeployments(ListRuleDeploymentsRequest, ServerCallContext)
    
    
    public virtual Task<ListRuleDeploymentsResponse> ListRuleDeployments(ListRuleDeploymentsRequest request, ServerCallContext context)

Lists RuleDeployments across all Rules.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRuleDeploymentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.ListRuleDeploymentsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListRuleDeploymentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.ListRuleDeploymentsResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListRuleRevisions(ListRuleRevisionsRequest, ServerCallContext)
    
    
    public virtual Task<ListRuleRevisionsResponse> ListRuleRevisions(ListRuleRevisionsRequest request, ServerCallContext context)

Lists all revisions of the rule.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRuleRevisionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.ListRuleRevisionsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListRuleRevisionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.ListRuleRevisionsResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListRules(ListRulesRequest, ServerCallContext)
    
    
    public virtual Task<ListRulesResponse> ListRules(ListRulesRequest request, ServerCallContext context)

Lists Rules.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRulesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.ListRulesRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListRulesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.ListRulesResponse)` | The response to send back to the client (wrapped by a task).  
  
### UpdateRule(UpdateRuleRequest, ServerCallContext)
    
    
    public virtual Task<Rule> UpdateRule(UpdateRuleRequest request, ServerCallContext context)

Updates a Rule.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateRuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.UpdateRuleRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Rule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.Rule)` | The response to send back to the client (wrapped by a task).  
  
### UpdateRuleDeployment(UpdateRuleDeploymentRequest, ServerCallContext)
    
    
    public virtual Task<RuleDeployment> UpdateRuleDeployment(UpdateRuleDeploymentRequest request, ServerCallContext context)

Updates a RuleDeployment. Failures are not necessarily atomic. If there is a request to update multiple fields, and any update to a single field fails, an error will be returned, but other fields may remain successfully updated.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateRuleDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.UpdateRuleDeploymentRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[RuleDeployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.RuleDeployment)` | The response to send back to the client (wrapped by a task).  
  
### VerifyRuleText(VerifyRuleTextRequest, ServerCallContext)
    
    
    public virtual Task<VerifyRuleTextResponse> VerifyRuleText(VerifyRuleTextRequest request, ServerCallContext context)

Verifies the given rule text.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[VerifyRuleTextRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.VerifyRuleTextRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[VerifyRuleTextResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.VerifyRuleTextResponse)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
