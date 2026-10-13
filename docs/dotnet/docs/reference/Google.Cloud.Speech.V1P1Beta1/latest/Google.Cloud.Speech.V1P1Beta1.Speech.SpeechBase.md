---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.Speech.SpeechBase
title: Google Cloud Speech v1p1beta1 API - Class Speech.SpeechBase (3.0.0-beta10) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:44:28.959471+00:00
---

# Google Cloud Speech v1p1beta1 API - Class Speech.SpeechBase (3.0.0-beta10)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.Speech.SpeechBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Speech v1p1beta1 API - Class Speech.SpeechBase (3.0.0-beta10) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.0.0-beta10 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.Speech.SpeechBase)
  * [ 3.0.0-beta09 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/3.0.0-beta09/Google.Cloud.Speech.V1P1Beta1.Speech.SpeechBase)
  * [ 2.0.0-beta09 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/2.0.0-beta09/Google.Cloud.Speech.V1P1Beta1.Speech.SpeechBase)


    
    
    [BindServiceMethod(typeof(Speech), "BindService")]
    public abstract class Speech.SpeechBase

Reference documentation and code samples for the Google Cloud Speech v1p1beta1 API class Speech.SpeechBase.

Base class for server-side implementations of Speech

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Speech.SpeechBase

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

### LongRunningRecognize(LongRunningRecognizeRequest, ServerCallContext)
    
    
    public virtual Task<Operation> LongRunningRecognize(LongRunningRecognizeRequest request, ServerCallContext context)

Performs asynchronous speech recognition: receive results via the google.longrunning.Operations interface. Returns either an `Operation.error` or an `Operation.response` which contains a `LongRunningRecognizeResponse` message. For more information on asynchronous speech recognition, see the [how-to](https://cloud.google.com/speech-to-text/docs/async-recognize).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[LongRunningRecognizeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.LongRunningRecognizeRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### Recognize(RecognizeRequest, ServerCallContext)
    
    
    public virtual Task<RecognizeResponse> Recognize(RecognizeRequest request, ServerCallContext context)

Performs synchronous speech recognition: receive results after all audio has been sent and processed.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RecognizeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.RecognizeRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[RecognizeResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.RecognizeResponse)` | The response to send back to the client (wrapped by a task).  
  
### StreamingRecognize(IAsyncStreamReader<StreamingRecognizeRequest>, IServerStreamWriter<StreamingRecognizeResponse>, ServerCallContext)
    
    
    public virtual Task StreamingRecognize(IAsyncStreamReader<StreamingRecognizeRequest> requestStream, IServerStreamWriter<StreamingRecognizeResponse> responseStream, ServerCallContext context)

Performs bidirectional streaming speech recognition: receive results while sending audio. This method is only available via the gRPC API (not REST).

**Parameters**  
---  
**Name** | **Description**  
`requestStream` | `[IAsyncStreamReader](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.IAsyncStreamReader-1.html)[StreamingRecognizeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.StreamingRecognizeRequest)`  
Used for reading requests from the client.  
`responseStream` | `[IServerStreamWriter](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.IServerStreamWriter-1.html)[StreamingRecognizeResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.StreamingRecognizeResponse)`  
Used for sending responses back to the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task indicating completion of the handler.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
