---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.ModelArmor.ModelArmorBase
title: Model Armor v1beta API - Class ModelArmor.ModelArmorBase (1.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:44:25.249734+00:00
---

# Model Armor v1beta API - Class ModelArmor.ModelArmorBase (1.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.ModelArmor.ModelArmorBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Model Armor v1beta API - Class ModelArmor.ModelArmorBase (1.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta06 (latest)  1.0.0-beta05 
    
    
    [BindServiceMethod(typeof(ModelArmor), "BindService")]
    public abstract class ModelArmor.ModelArmorBase

Reference documentation and code samples for the Model Armor v1beta API class ModelArmor.ModelArmorBase.

Base class for server-side implementations of ModelArmor

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ModelArmor.ModelArmorBase

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ModelArmor.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta)

## Assembly

Google.Cloud.ModelArmor.V1Beta.dll

## Methods 

### CreateTemplate(CreateTemplateRequest, ServerCallContext)
    
    
    public virtual Task<Template> CreateTemplate(CreateTemplateRequest request, ServerCallContext context)

Creates a new Template in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.CreateTemplateRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)` | The response to send back to the client (wrapped by a task).  
  
### DeleteTemplate(DeleteTemplateRequest, ServerCallContext)
    
    
    public virtual Task<Empty> DeleteTemplate(DeleteTemplateRequest request, ServerCallContext context)

Deletes a single Template.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.DeleteTemplateRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response to send back to the client (wrapped by a task).  
  
### GetFloorSetting(GetFloorSettingRequest, ServerCallContext)
    
    
    public virtual Task<FloorSetting> GetFloorSetting(GetFloorSettingRequest request, ServerCallContext context)

Gets details of a single floor setting of a project

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFloorSettingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.GetFloorSettingRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.FloorSetting)` | The response to send back to the client (wrapped by a task).  
  
### GetTemplate(GetTemplateRequest, ServerCallContext)
    
    
    public virtual Task<Template> GetTemplate(GetTemplateRequest request, ServerCallContext context)

Gets details of a single Template.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.GetTemplateRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)` | The response to send back to the client (wrapped by a task).  
  
### ListTemplates(ListTemplatesRequest, ServerCallContext)
    
    
    public virtual Task<ListTemplatesResponse> ListTemplates(ListTemplatesRequest request, ServerCallContext context)

Lists Templates in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListTemplatesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.ListTemplatesRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListTemplatesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.ListTemplatesResponse)` | The response to send back to the client (wrapped by a task).  
  
### SanitizeModelResponse(SanitizeModelResponseRequest, ServerCallContext)
    
    
    public virtual Task<SanitizeModelResponseResponse> SanitizeModelResponse(SanitizeModelResponseRequest request, ServerCallContext context)

Sanitizes Model Response.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SanitizeModelResponseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.SanitizeModelResponseRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SanitizeModelResponseResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.SanitizeModelResponseResponse)` | The response to send back to the client (wrapped by a task).  
  
### SanitizeUserPrompt(SanitizeUserPromptRequest, ServerCallContext)
    
    
    public virtual Task<SanitizeUserPromptResponse> SanitizeUserPrompt(SanitizeUserPromptRequest request, ServerCallContext context)

Sanitizes User Prompt.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SanitizeUserPromptRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.SanitizeUserPromptRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SanitizeUserPromptResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.SanitizeUserPromptResponse)` | The response to send back to the client (wrapped by a task).  
  
### StreamSanitizeModelResponse(IAsyncStreamReader<SanitizeModelResponseRequest>, IServerStreamWriter<SanitizeModelResponseResponse>, ServerCallContext)
    
    
    public virtual Task StreamSanitizeModelResponse(IAsyncStreamReader<SanitizeModelResponseRequest> requestStream, IServerStreamWriter<SanitizeModelResponseResponse> responseStream, ServerCallContext context)

Streaming version of Sanitizes Model Response.

**Parameters**  
---  
**Name** | **Description**  
`requestStream` | `[IAsyncStreamReader](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.IAsyncStreamReader-1.html)[SanitizeModelResponseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.SanitizeModelResponseRequest)`  
Used for reading requests from the client.  
`responseStream` | `[IServerStreamWriter](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.IServerStreamWriter-1.html)[SanitizeModelResponseResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.SanitizeModelResponseResponse)`  
Used for sending responses back to the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task indicating completion of the handler.  
  
### StreamSanitizeUserPrompt(IAsyncStreamReader<SanitizeUserPromptRequest>, IServerStreamWriter<SanitizeUserPromptResponse>, ServerCallContext)
    
    
    public virtual Task StreamSanitizeUserPrompt(IAsyncStreamReader<SanitizeUserPromptRequest> requestStream, IServerStreamWriter<SanitizeUserPromptResponse> responseStream, ServerCallContext context)

Streaming version of Sanitize User Prompt.

**Parameters**  
---  
**Name** | **Description**  
`requestStream` | `[IAsyncStreamReader](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.IAsyncStreamReader-1.html)[SanitizeUserPromptRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.SanitizeUserPromptRequest)`  
Used for reading requests from the client.  
`responseStream` | `[IServerStreamWriter](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.IServerStreamWriter-1.html)[SanitizeUserPromptResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.SanitizeUserPromptResponse)`  
Used for sending responses back to the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task indicating completion of the handler.  
  
### UpdateFloorSetting(UpdateFloorSettingRequest, ServerCallContext)
    
    
    public virtual Task<FloorSetting> UpdateFloorSetting(UpdateFloorSettingRequest request, ServerCallContext context)

Updates the parameters of a single floor setting of a project

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFloorSettingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.UpdateFloorSettingRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.FloorSetting)` | The response to send back to the client (wrapped by a task).  
  
### UpdateTemplate(UpdateTemplateRequest, ServerCallContext)
    
    
    public virtual Task<Template> UpdateTemplate(UpdateTemplateRequest request, ServerCallContext context)

Updates the parameters of a single Template.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.UpdateTemplateRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-05 UTC."],[],[]] 
