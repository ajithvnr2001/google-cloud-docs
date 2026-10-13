---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.generativeai.ChatSession
title: Class ChatSession (1.48.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:57:16.237536+00:00
---

# Class ChatSession (1.48.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.generativeai.ChatSession

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ChatSession (1.48.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.48.0 (latest)  1.47.0  1.45.0  1.43.0  1.42.0  1.40.0  1.38.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.30.0  1.28.0  1.27.0  1.24.0  1.23.0  1.22.0  1.20.1  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.8.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public final class ChatSession

**Deprecated.** _This class and its package are deprecated. See the[ migration guide](https://cloud.google.com/vertex-ai/generative-ai/docs/deprecations/genai-vertexai-sdk#java) for more details._

Represents a conversation between the user and the model.

Note: this class is NOT thread-safe.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ChatSession

## Inherited Members

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

## Constructors 

### ChatSession(GenerativeModel model) (deprecated)
    
    
    public ChatSession(GenerativeModel model)

Creates a new chat session given a GenerativeModel instance. Configurations of the chat (e.g., GenerationConfig) inherits from the model.

**Parameter**  
---  
**Name** | **Description**  
`model` | `[GenerativeModel](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.generativeai.GenerativeModel)`  
  
  
## Methods 

### getHistory() (deprecated)
    
    
    public ImmutableList<Content> getHistory()

Returns the history of the conversation.

**Returns**  
---  
**Type** | **Description**  
`com.google.common.collect.ImmutableList<[Content](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Content)>` | a history of the conversation as an immutable list of [Content](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Content).  
  
### sendMessage(Content content) (deprecated)
    
    
    public GenerateContentResponse sendMessage(Content content)

Sends a message to the model and returns a response.

**Parameter**  
---  
**Name** | **Description**  
`content` | `[Content](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Content)`  
the content to be sent.  
**Returns**  
---  
**Type** | **Description**  
`[GenerateContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.GenerateContentResponse)` | a response.  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### sendMessage(String text) (deprecated)
    
    
    public GenerateContentResponse sendMessage(String text)

Sends a message to the model and returns a response.

**Parameter**  
---  
**Name** | **Description**  
`text` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the message to be sent.  
**Returns**  
---  
**Type** | **Description**  
`[GenerateContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.GenerateContentResponse)` | a response.  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### sendMessageStream(Content content) (deprecated)
    
    
    public ResponseStream<GenerateContentResponse> sendMessageStream(Content content)

Sends a message to the model and returns a stream of responses.

**Parameter**  
---  
**Name** | **Description**  
`content` | `[Content](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Content)`  
the content to be sent.  
**Returns**  
---  
**Type** | **Description**  
`[ResponseStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.generativeai.ResponseStream)<[GenerateContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.GenerateContentResponse)>` | an iterable in which each element is a GenerateContentResponse. Can be converted to stream by stream() method.  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### sendMessageStream(String text) (deprecated)
    
    
    public ResponseStream<GenerateContentResponse> sendMessageStream(String text)

Sends a message to the model and returns a stream of responses.

**Parameter**  
---  
**Name** | **Description**  
`text` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the message to be sent.  
**Returns**  
---  
**Type** | **Description**  
`[ResponseStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.generativeai.ResponseStream)<[GenerateContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.GenerateContentResponse)>` | an iterable in which each element is a GenerateContentResponse. Can be converted to stream by stream() method.  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### setHistory(List<Content> history) (deprecated)
    
    
    public void setHistory(List<Content> history)

Sets the history to a list of Content.

**Parameter**  
---  
**Name** | **Description**  
`history` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Content](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Content)>`  
A list of [Content](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Content) containing interleaving conversation between "user" and "model".  
  
### withAutomaticFunctionCallingResponder(AutomaticFunctionCallingResponder automaticFunctionCallingResponder) (deprecated)
    
    
    public ChatSession withAutomaticFunctionCallingResponder(AutomaticFunctionCallingResponder automaticFunctionCallingResponder)

Creates a copy of the current ChatSession with updated AutomaticFunctionCallingResponder.

**Parameter**  
---  
**Name** | **Description**  
`automaticFunctionCallingResponder` | `[AutomaticFunctionCallingResponder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.generativeai.AutomaticFunctionCallingResponder)`  
an [AutomaticFunctionCallingResponder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.generativeai.AutomaticFunctionCallingResponder) instance that will be used in the new ChatSession.  
**Returns**  
---  
**Type** | **Description**  
`[ChatSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.generativeai.ChatSession)` | a new [ChatSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.generativeai.ChatSession) instance with the specified AutomaticFunctionCallingResponder.  
  
### withGenerationConfig(GenerationConfig generationConfig) (deprecated)
    
    
    public ChatSession withGenerationConfig(GenerationConfig generationConfig)

Creates a copy of the current ChatSession with updated GenerationConfig.

**Parameter**  
---  
**Name** | **Description**  
`generationConfig` | `[GenerationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.GenerationConfig)`  
a [com.google.cloud.vertexai.api.GenerationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.GenerationConfig) that will be used in the new ChatSession.  
**Returns**  
---  
**Type** | **Description**  
`[ChatSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.generativeai.ChatSession)` | a new [ChatSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.generativeai.ChatSession) instance with the specified GenerationConfig.  
  
### withSafetySettings(List<SafetySetting> safetySettings) (deprecated)
    
    
    public ChatSession withSafetySettings(List<SafetySetting> safetySettings)

Creates a copy of the current ChatSession with updated SafetySettings.

**Parameter**  
---  
**Name** | **Description**  
`safetySettings` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[SafetySetting](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.SafetySetting)>`  
a [com.google.cloud.vertexai.api.SafetySetting](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.SafetySetting) that will be used in the new ChatSession.  
**Returns**  
---  
**Type** | **Description**  
`[ChatSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.generativeai.ChatSession)` | a new [ChatSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.generativeai.ChatSession) instance with the specified SafetySettings.  
  
### withSystemInstruction(Content systemInstruction) (deprecated)
    
    
    public ChatSession withSystemInstruction(Content systemInstruction)

Creates a copy of the current ChatSession with updated SystemInstruction.

**Parameter**  
---  
**Name** | **Description**  
`systemInstruction` | `[Content](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Content)`  
a [com.google.cloud.vertexai.api.Content](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Content) containing system instructions.  
**Returns**  
---  
**Type** | **Description**  
`[ChatSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.generativeai.ChatSession)` | a new [ChatSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.generativeai.ChatSession) instance with the specified ToolConfigs.  
  
### withToolConfig(ToolConfig toolConfig) (deprecated)
    
    
    public ChatSession withToolConfig(ToolConfig toolConfig)

Creates a copy of the current ChatSession with updated ToolConfig.

**Parameter**  
---  
**Name** | **Description**  
`toolConfig` | `[ToolConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.ToolConfig)`  
a [com.google.cloud.vertexai.api.ToolConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.ToolConfig) that will be used in the new ChatSession.  
**Returns**  
---  
**Type** | **Description**  
`[ChatSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.generativeai.ChatSession)` | a new [ChatSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.generativeai.ChatSession) instance with the specified ToolConfigs.  
  
### withTools(List<Tool> tools) (deprecated)
    
    
    public ChatSession withTools(List<Tool> tools)

Creates a copy of the current ChatSession with updated Tools.

**Parameter**  
---  
**Name** | **Description**  
`tools` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Tool](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Tool)>`  
a [com.google.cloud.vertexai.api.Tool](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Tool) that will be used in the new ChatSession.  
**Returns**  
---  
**Type** | **Description**  
`[ChatSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.generativeai.ChatSession)` | a new [ChatSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.generativeai.ChatSession) instance with the specified Tools.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-30 UTC."],[],[]] 
