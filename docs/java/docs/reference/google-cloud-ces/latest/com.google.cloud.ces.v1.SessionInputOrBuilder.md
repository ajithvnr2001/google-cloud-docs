---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.SessionInputOrBuilder
title: Interface SessionInputOrBuilder (0.15.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:27:59.642600+00:00
---

# Interface SessionInputOrBuilder (0.15.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.SessionInputOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface SessionInputOrBuilder (0.15.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.0 (latest)  0.11.0  0.10.0  0.9.0  0.7.0  0.4.0  0.3.0  0.1.0 
    
    
    public interface SessionInputOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAudio()
    
    
    public abstract ByteString getAudio()

Optional. Audio data from the end user.

`bytes audio = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The audio.  
  
### getBlob()
    
    
    public abstract Blob getBlob()

Optional. Blob data from the end user.

`.google.cloud.ces.v1.Blob blob = 7 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.Blob)` | The blob.  
  
### getBlobOrBuilder()
    
    
    public abstract BlobOrBuilder getBlobOrBuilder()

Optional. Blob data from the end user.

`.google.cloud.ces.v1.Blob blob = 7 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[BlobOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.BlobOrBuilder)` |   
  
### getDtmf()
    
    
    public abstract String getDtmf()

Optional. DTMF digits from the end user.

`string dtmf = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The dtmf.  
  
### getDtmfBytes()
    
    
    public abstract ByteString getDtmfBytes()

Optional. DTMF digits from the end user.

`string dtmf = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for dtmf.  
  
### getEvent()
    
    
    public abstract Event getEvent()

Optional. Event input.

`.google.cloud.ces.v1.Event event = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[Event](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.Event)` | The event.  
  
### getEventOrBuilder()
    
    
    public abstract EventOrBuilder getEventOrBuilder()

Optional. Event input.

`.google.cloud.ces.v1.Event event = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[EventOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.EventOrBuilder)` |   
  
### getImage()
    
    
    public abstract Image getImage()

Optional. Image data from the end user.

`.google.cloud.ces.v1.Image image = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.Image)` | The image.  
  
### getImageOrBuilder()
    
    
    public abstract ImageOrBuilder getImageOrBuilder()

Optional. Image data from the end user.

`.google.cloud.ces.v1.Image image = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ImageOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.ImageOrBuilder)` |   
  
### getInputTypeCase()
    
    
    public abstract SessionInput.InputTypeCase getInputTypeCase()

**Returns**  
---  
**Type** | **Description**  
`[SessionInput.InputTypeCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.SessionInput.InputTypeCase)` |   
  
### getText()
    
    
    public abstract String getText()

Optional. Text data from the end user.

`string text = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The text.  
  
### getTextBytes()
    
    
    public abstract ByteString getTextBytes()

Optional. Text data from the end user.

`string text = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for text.  
  
### getToolResponses()
    
    
    public abstract ToolResponses getToolResponses()

Optional. Execution results for the tool calls from the client.

` .google.cloud.ces.v1.ToolResponses tool_responses = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ToolResponses](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.ToolResponses)` | The toolResponses.  
  
### getToolResponsesOrBuilder()
    
    
    public abstract ToolResponsesOrBuilder getToolResponsesOrBuilder()

Optional. Execution results for the tool calls from the client.

` .google.cloud.ces.v1.ToolResponses tool_responses = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ToolResponsesOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.ToolResponsesOrBuilder)` |   
  
### getVariables()
    
    
    public abstract Struct getVariables()

Optional. Contextual variables for the session, keyed by name. Only variables declared in the app will be used by the CES agent.

Unrecognized variables will still be sent to the Dialogflow agent as additional session parameters.

`.google.protobuf.Struct variables = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)` | The variables.  
  
### getVariablesOrBuilder()
    
    
    public abstract StructOrBuilder getVariablesOrBuilder()

Optional. Contextual variables for the session, keyed by name. Only variables declared in the app will be used by the CES agent.

Unrecognized variables will still be sent to the Dialogflow agent as additional session parameters.

`.google.protobuf.Struct variables = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[StructOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.StructOrBuilder.html)` |   
  
### getWillContinue()
    
    
    public abstract boolean getWillContinue()

Optional. A flag to indicate if the current message is a fragment of a larger input in the bidi streaming session.

When set to `true`, the agent defers processing until it receives a subsequent message where `will_continue` is `false`, or until the system detects an endpoint in the audio input.

NOTE: This field does not apply to audio and DTMF inputs, as they are always processed automatically based on the endpointing signal.

`bool will_continue = 8 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The willContinue.  
  
### hasAudio()
    
    
    public abstract boolean hasAudio()

Optional. Audio data from the end user.

`bytes audio = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the audio field is set.  
  
### hasBlob()
    
    
    public abstract boolean hasBlob()

Optional. Blob data from the end user.

`.google.cloud.ces.v1.Blob blob = 7 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the blob field is set.  
  
### hasDtmf()
    
    
    public abstract boolean hasDtmf()

Optional. DTMF digits from the end user.

`string dtmf = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the dtmf field is set.  
  
### hasEvent()
    
    
    public abstract boolean hasEvent()

Optional. Event input.

`.google.cloud.ces.v1.Event event = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the event field is set.  
  
### hasImage()
    
    
    public abstract boolean hasImage()

Optional. Image data from the end user.

`.google.cloud.ces.v1.Image image = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the image field is set.  
  
### hasText()
    
    
    public abstract boolean hasText()

Optional. Text data from the end user.

`string text = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the text field is set.  
  
### hasToolResponses()
    
    
    public abstract boolean hasToolResponses()

Optional. Execution results for the tool calls from the client.

` .google.cloud.ces.v1.ToolResponses tool_responses = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the toolResponses field is set.  
  
### hasVariables()
    
    
    public abstract boolean hasVariables()

Optional. Contextual variables for the session, keyed by name. Only variables declared in the app will be used by the CES agent.

Unrecognized variables will still be sent to the Dialogflow agent as additional session parameters.

`.google.protobuf.Struct variables = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the variables field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
