---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SessionService.SessionServiceBase
title: Gemini Enterprise for Customer Experience v1beta API - Class SessionService.SessionServiceBase (1.0.0-beta09) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:00:59.099032+00:00
---

# Gemini Enterprise for Customer Experience v1beta API - Class SessionService.SessionServiceBase (1.0.0-beta09)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SessionService.SessionServiceBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Gemini Enterprise for Customer Experience v1beta API - Class SessionService.SessionServiceBase (1.0.0-beta09) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta09 (latest)  1.0.0-beta08 
    
    
    [BindServiceMethod(typeof(SessionService), "BindService")]
    public abstract class SessionService.SessionServiceBase

Reference documentation and code samples for the Gemini Enterprise for Customer Experience v1beta API class SessionService.SessionServiceBase.

Base class for server-side implementations of SessionService

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > SessionService.SessionServiceBase

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

### BidiRunSession(IAsyncStreamReader<BidiSessionClientMessage>, IServerStreamWriter<BidiSessionServerMessage>, ServerCallContext)
    
    
    public virtual Task BidiRunSession(IAsyncStreamReader<BidiSessionClientMessage> requestStream, IServerStreamWriter<BidiSessionServerMessage> responseStream, ServerCallContext context)

Establishes a bidirectional streaming connection with the CES agent. The agent processes continuous multimodal inputs (e.g., text, audio) and generates real-time multimodal output streams.

\--- Client Request Stream --- The client streams requests in the following order:

  1. Initialization: The first message must contain [SessionConfig][google.cloud.ces.v1beta.BidiSessionClientMessage.config]. For audio sessions, this should also include [InputAudioConfig][google.cloud.ces.v1beta.SessionConfig.input_audio_config] and [OutputAudioConfig][google.cloud.ces.v1beta.SessionConfig.output_audio_config] to define audio processing and synthesis parameters.

  2. Interaction: Subsequent messages stream [SessionInput][google.cloud.ces.v1beta.BidiSessionClientMessage.realtime_input] containing real-time user input data.

  3. Termination: The client should half-close the stream when there is no more user input. It should also half-close upon receiving [EndSession][google.cloud.ces.v1beta.BidiSessionServerMessage.end_session] or [GoAway][google.cloud.ces.v1beta.BidiSessionServerMessage.go_away] from the agent.




\--- Server Response Stream --- For each interaction turn, the agent streams messages in the following sequence:

  1. Speech Recognition (First N messages): Contains [RecognitionResult][google.cloud.ces.v1beta.BidiSessionServerMessage.recognition_result] representing the concatenated user speech segments captured so far. This is only populated for audio sessions.

  2. Response (Next M messages): Contains [SessionOutput][google.cloud.ces.v1beta.BidiSessionServerMessage.session_output] delivering the agent's response in various modalities (e.g., text, audio).

  3. Turn Completion (Final message of the turn): Contains [SessionOutput][google.cloud.ces.v1beta.BidiSessionServerMessage.session_output] with [turn_completed][google.cloud.ces.v1beta.SessionOutput.turn_completed] set to true. This signals the end of the current turn and includes [DiagnosticInfo][google.cloud.ces.v1beta.SessionOutput.diagnostic_info] with execution details.




\--- Audio Best Practices ---

  1. Streaming: Stream [audio data][google.cloud.ces.v1beta.SessionInput.audio] **CONTINUOUSLY** , even during silence. Recommended chunk size: 40-120ms (balances latency vs. efficiency).

  2. Playback & Interruption: Play [audio responses][google.cloud.ces.v1beta.SessionOutput.audio] upon receipt. Stop playback immediately if an [InterruptionSignal][google.cloud.ces.v1beta.BidiSessionServerMessage.interruption_signal] is received (e.g., user barge-in or new agent response).




**Parameters**  
---  
**Name** | **Description**  
`requestStream` | `[IAsyncStreamReader](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.IAsyncStreamReader-1.html)[BidiSessionClientMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.BidiSessionClientMessage)`  
Used for reading requests from the client.  
`responseStream` | `[IServerStreamWriter](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.IServerStreamWriter-1.html)[BidiSessionServerMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.BidiSessionServerMessage)`  
Used for sending responses back to the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task indicating completion of the handler.  
  
### RunSession(RunSessionRequest, ServerCallContext)
    
    
    public virtual Task<RunSessionResponse> RunSession(RunSessionRequest request, ServerCallContext context)

Initiates a single-turn interaction with the CES agent within a session.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RunSessionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.RunSessionRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[RunSessionResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.RunSessionResponse)` | The response to send back to the client (wrapped by a task).  
  
### StreamRunSession(RunSessionRequest, IServerStreamWriter<RunSessionResponse>, ServerCallContext)
    
    
    public virtual Task StreamRunSession(RunSessionRequest request, IServerStreamWriter<RunSessionResponse> responseStream, ServerCallContext context)

Initiates a single-turn interaction with the CES agent. Uses server-side streaming to deliver incremental results and partial responses as they are generated.

By default, complete responses (e.g., messages from callbacks or full LLM responses) are sent to the client as soon as they are available. To enable streaming individual text chunks directly from the model, set [enable_text_streaming][google.cloud.ces.v1beta.SessionConfig.enable_text_streaming] to true.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RunSessionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.RunSessionRequest)`  
The request received from the client.  
`responseStream` | `[IServerStreamWriter](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.IServerStreamWriter-1.html)[RunSessionResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.RunSessionResponse)`  
Used for sending responses back to the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task indicating completion of the handler.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
