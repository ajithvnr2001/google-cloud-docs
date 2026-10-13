---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1.TextToSpeech.TextToSpeechBase
title: Google Cloud Text-to-Speech v1beta1 API - Class TextToSpeech.TextToSpeechBase (2.0.0-beta18) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:19:10.770251+00:00
---

# Google Cloud Text-to-Speech v1beta1 API - Class TextToSpeech.TextToSpeechBase (2.0.0-beta18)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1.TextToSpeech.TextToSpeechBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Text-to-Speech v1beta1 API - Class TextToSpeech.TextToSpeechBase (2.0.0-beta18) Stay organized with collections  Save and categorize content based on your preferences. 

2.0.0-beta18 (latest)  2.0.0-beta17  1.0.0-beta04 
    
    
    [BindServiceMethod(typeof(TextToSpeech), "BindService")]
    public abstract class TextToSpeech.TextToSpeechBase

Reference documentation and code samples for the Google Cloud Text-to-Speech v1beta1 API class TextToSpeech.TextToSpeechBase.

Base class for server-side implementations of TextToSpeech

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > TextToSpeech.TextToSpeechBase

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.TextToSpeech.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1)

## Assembly

Google.Cloud.TextToSpeech.V1Beta1.dll

## Methods 

### ListVoices(ListVoicesRequest, ServerCallContext)
    
    
    public virtual Task<ListVoicesResponse> ListVoices(ListVoicesRequest request, ServerCallContext context)

Returns a list of Voice supported for synthesis.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListVoicesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1.ListVoicesRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListVoicesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1.ListVoicesResponse)` | The response to send back to the client (wrapped by a task).  
  
### StreamingSynthesize(IAsyncStreamReader<StreamingSynthesizeRequest>, IServerStreamWriter<StreamingSynthesizeResponse>, ServerCallContext)
    
    
    public virtual Task StreamingSynthesize(IAsyncStreamReader<StreamingSynthesizeRequest> requestStream, IServerStreamWriter<StreamingSynthesizeResponse> responseStream, ServerCallContext context)

Performs bidirectional streaming speech synthesis: receives audio while sending text.

**Parameters**  
---  
**Name** | **Description**  
`requestStream` | `[IAsyncStreamReader](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.IAsyncStreamReader-1.html)[StreamingSynthesizeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1.StreamingSynthesizeRequest)`  
Used for reading requests from the client.  
`responseStream` | `[IServerStreamWriter](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.IServerStreamWriter-1.html)[StreamingSynthesizeResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1.StreamingSynthesizeResponse)`  
Used for sending responses back to the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task indicating completion of the handler.  
  
### SynthesizeSpeech(SynthesizeSpeechRequest, ServerCallContext)
    
    
    public virtual Task<SynthesizeSpeechResponse> SynthesizeSpeech(SynthesizeSpeechRequest request, ServerCallContext context)

Synthesizes speech synchronously: receive results after all text input has been processed.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SynthesizeSpeechRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1.SynthesizeSpeechRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SynthesizeSpeechResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1.SynthesizeSpeechResponse)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-23 UTC."],[],[]] 
