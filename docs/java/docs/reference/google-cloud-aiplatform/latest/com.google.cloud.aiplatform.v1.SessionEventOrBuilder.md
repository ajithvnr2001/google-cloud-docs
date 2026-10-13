---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SessionEventOrBuilder
title: Interface SessionEventOrBuilder (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:51:12.868094+00:00
---

# Interface SessionEventOrBuilder (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SessionEventOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface SessionEventOrBuilder (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 
    
    
    public interface SessionEventOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getActions()
    
    
    public abstract EventActions getActions()

Optional. Actions executed by the agent.

` .google.cloud.aiplatform.v1.EventActions actions = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[EventActions](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EventActions)` | The actions.  
  
### getActionsOrBuilder()
    
    
    public abstract EventActionsOrBuilder getActionsOrBuilder()

Optional. Actions executed by the agent.

` .google.cloud.aiplatform.v1.EventActions actions = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[EventActionsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EventActionsOrBuilder)` |   
  
### getAuthor()
    
    
    public abstract String getAuthor()

Required. The name of the agent that sent the event, or user.

`string author = 3 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The author.  
  
### getAuthorBytes()
    
    
    public abstract ByteString getAuthorBytes()

Required. The name of the agent that sent the event, or user.

`string author = 3 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for author.  
  
### getContent()
    
    
    public abstract Content getContent()

Optional. Content of the event provided by the author.

` .google.cloud.aiplatform.v1.Content content = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Content](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Content)` | The content.  
  
### getContentOrBuilder()
    
    
    public abstract ContentOrBuilder getContentOrBuilder()

Optional. Content of the event provided by the author.

` .google.cloud.aiplatform.v1.Content content = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ContentOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ContentOrBuilder)` |   
  
### getErrorCode()
    
    
    public abstract String getErrorCode()

Optional. Error code if the response is an error. Code varies by model.

`string error_code = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The errorCode.  
  
### getErrorCodeBytes()
    
    
    public abstract ByteString getErrorCodeBytes()

Optional. Error code if the response is an error. Code varies by model.

`string error_code = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for errorCode.  
  
### getErrorMessage()
    
    
    public abstract String getErrorMessage()

Optional. Error message if the response is an error.

`string error_message = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The errorMessage.  
  
### getErrorMessageBytes()
    
    
    public abstract ByteString getErrorMessageBytes()

Optional. Error message if the response is an error.

`string error_message = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for errorMessage.  
  
### getEventMetadata()
    
    
    public abstract EventMetadata getEventMetadata()

Optional. Metadata relating to this event.

` .google.cloud.aiplatform.v1.EventMetadata event_metadata = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[EventMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EventMetadata)` | The eventMetadata.  
  
### getEventMetadataOrBuilder()
    
    
    public abstract EventMetadataOrBuilder getEventMetadataOrBuilder()

Optional. Metadata relating to this event.

` .google.cloud.aiplatform.v1.EventMetadata event_metadata = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[EventMetadataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EventMetadataOrBuilder)` |   
  
### getInvocationId()
    
    
    public abstract String getInvocationId()

Required. The invocation id of the event, multiple events can have the same invocation id.

`string invocation_id = 5 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The invocationId.  
  
### getInvocationIdBytes()
    
    
    public abstract ByteString getInvocationIdBytes()

Required. The invocation id of the event, multiple events can have the same invocation id.

`string invocation_id = 5 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for invocationId.  
  
### getName()
    
    
    public abstract String getName()

Identifier. The resource name of the event. Format:`projects/{project}/locations/{location}/reasoningEngines/{reasoning_engine}/sessions/{session}/events/{event}`.

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Identifier. The resource name of the event. Format:`projects/{project}/locations/{location}/reasoningEngines/{reasoning_engine}/sessions/{session}/events/{event}`.

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getRawEvent()
    
    
    public abstract Struct getRawEvent()

Optional. Weakly typed raw event data in proto struct format.

`.google.protobuf.Struct raw_event = 12 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)` | The rawEvent.  
  
### getRawEventOrBuilder()
    
    
    public abstract StructOrBuilder getRawEventOrBuilder()

Optional. Weakly typed raw event data in proto struct format.

`.google.protobuf.Struct raw_event = 12 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[StructOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.StructOrBuilder.html)` |   
  
### getTimestamp()
    
    
    public abstract Timestamp getTimestamp()

Required. Timestamp when the event was created on client side.

`.google.protobuf.Timestamp timestamp = 8 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The timestamp.  
  
### getTimestampOrBuilder()
    
    
    public abstract TimestampOrBuilder getTimestampOrBuilder()

Required. Timestamp when the event was created on client side.

`.google.protobuf.Timestamp timestamp = 8 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasActions()
    
    
    public abstract boolean hasActions()

Optional. Actions executed by the agent.

` .google.cloud.aiplatform.v1.EventActions actions = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the actions field is set.  
  
### hasContent()
    
    
    public abstract boolean hasContent()

Optional. Content of the event provided by the author.

` .google.cloud.aiplatform.v1.Content content = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the content field is set.  
  
### hasEventMetadata()
    
    
    public abstract boolean hasEventMetadata()

Optional. Metadata relating to this event.

` .google.cloud.aiplatform.v1.EventMetadata event_metadata = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the eventMetadata field is set.  
  
### hasRawEvent()
    
    
    public abstract boolean hasRawEvent()

Optional. Weakly typed raw event data in proto struct format.

`.google.protobuf.Struct raw_event = 12 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the rawEvent field is set.  
  
### hasTimestamp()
    
    
    public abstract boolean hasTimestamp()

Required. Timestamp when the event was created on client side.

`.google.protobuf.Timestamp timestamp = 8 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the timestamp field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
