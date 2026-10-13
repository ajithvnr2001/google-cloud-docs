---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.Adaptation.AdaptationBase
title: Google Cloud Speech v1p1beta1 API - Class Adaptation.AdaptationBase (3.0.0-beta10) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:48:11.510936+00:00
---

# Google Cloud Speech v1p1beta1 API - Class Adaptation.AdaptationBase (3.0.0-beta10)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.Adaptation.AdaptationBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Speech v1p1beta1 API - Class Adaptation.AdaptationBase (3.0.0-beta10) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.0.0-beta10 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.Adaptation.AdaptationBase)
  * [ 3.0.0-beta09 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/3.0.0-beta09/Google.Cloud.Speech.V1P1Beta1.Adaptation.AdaptationBase)
  * [ 2.0.0-beta09 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/2.0.0-beta09/Google.Cloud.Speech.V1P1Beta1.Adaptation.AdaptationBase)


    
    
    [BindServiceMethod(typeof(Adaptation), "BindService")]
    public abstract class Adaptation.AdaptationBase

Reference documentation and code samples for the Google Cloud Speech v1p1beta1 API class Adaptation.AdaptationBase.

Base class for server-side implementations of Adaptation

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Adaptation.AdaptationBase

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Speech.V1P1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1)

## Assembly

Google.Cloud.Speech.V1P1Beta1.dll

## Methods 

### CreateCustomClass(CreateCustomClassRequest, ServerCallContext)
    
    
    public virtual Task<CustomClass> CreateCustomClass(CreateCustomClassRequest request, ServerCallContext context)

Create a custom class.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateCustomClassRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.CreateCustomClassRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CustomClass](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.CustomClass)` | The response to send back to the client (wrapped by a task).  
  
### CreatePhraseSet(CreatePhraseSetRequest, ServerCallContext)
    
    
    public virtual Task<PhraseSet> CreatePhraseSet(CreatePhraseSetRequest request, ServerCallContext context)

Create a set of phrase hints. Each item in the set can be a single word or a multi-word phrase. The items in the PhraseSet are favored by the recognition model when you send a call that includes the PhraseSet.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreatePhraseSetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.CreatePhraseSetRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PhraseSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.PhraseSet)` | The response to send back to the client (wrapped by a task).  
  
### DeleteCustomClass(DeleteCustomClassRequest, ServerCallContext)
    
    
    public virtual Task<Empty> DeleteCustomClass(DeleteCustomClassRequest request, ServerCallContext context)

Delete a custom class.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteCustomClassRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.DeleteCustomClassRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response to send back to the client (wrapped by a task).  
  
### DeletePhraseSet(DeletePhraseSetRequest, ServerCallContext)
    
    
    public virtual Task<Empty> DeletePhraseSet(DeletePhraseSetRequest request, ServerCallContext context)

Delete a phrase set.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeletePhraseSetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.DeletePhraseSetRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response to send back to the client (wrapped by a task).  
  
### GetCustomClass(GetCustomClassRequest, ServerCallContext)
    
    
    public virtual Task<CustomClass> GetCustomClass(GetCustomClassRequest request, ServerCallContext context)

Get a custom class.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCustomClassRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.GetCustomClassRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CustomClass](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.CustomClass)` | The response to send back to the client (wrapped by a task).  
  
### GetPhraseSet(GetPhraseSetRequest, ServerCallContext)
    
    
    public virtual Task<PhraseSet> GetPhraseSet(GetPhraseSetRequest request, ServerCallContext context)

Get a phrase set.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPhraseSetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.GetPhraseSetRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PhraseSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.PhraseSet)` | The response to send back to the client (wrapped by a task).  
  
### ListCustomClasses(ListCustomClassesRequest, ServerCallContext)
    
    
    public virtual Task<ListCustomClassesResponse> ListCustomClasses(ListCustomClassesRequest request, ServerCallContext context)

List custom classes.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListCustomClassesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.ListCustomClassesRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListCustomClassesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.ListCustomClassesResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListPhraseSet(ListPhraseSetRequest, ServerCallContext)
    
    
    public virtual Task<ListPhraseSetResponse> ListPhraseSet(ListPhraseSetRequest request, ServerCallContext context)

List phrase sets.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListPhraseSetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.ListPhraseSetRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListPhraseSetResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.ListPhraseSetResponse)` | The response to send back to the client (wrapped by a task).  
  
### UpdateCustomClass(UpdateCustomClassRequest, ServerCallContext)
    
    
    public virtual Task<CustomClass> UpdateCustomClass(UpdateCustomClassRequest request, ServerCallContext context)

Update a custom class.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateCustomClassRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.UpdateCustomClassRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CustomClass](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.CustomClass)` | The response to send back to the client (wrapped by a task).  
  
### UpdatePhraseSet(UpdatePhraseSetRequest, ServerCallContext)
    
    
    public virtual Task<PhraseSet> UpdatePhraseSet(UpdatePhraseSetRequest request, ServerCallContext context)

Update a phrase set.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdatePhraseSetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.UpdatePhraseSetRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PhraseSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.PhraseSet)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
