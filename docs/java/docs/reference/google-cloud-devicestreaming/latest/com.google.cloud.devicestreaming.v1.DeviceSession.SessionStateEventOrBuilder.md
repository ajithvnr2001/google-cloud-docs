---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-devicestreaming/latest/com.google.cloud.devicestreaming.v1.DeviceSession.SessionStateEventOrBuilder
title: Interface DeviceSession.SessionStateEventOrBuilder (0.39.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:55:32.219492+00:00
---

# Interface DeviceSession.SessionStateEventOrBuilder (0.39.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-devicestreaming/latest/com.google.cloud.devicestreaming.v1.DeviceSession.SessionStateEventOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface DeviceSession.SessionStateEventOrBuilder (0.39.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.39.0 (latest)  0.35.0  0.34.0  0.33.0  0.31.0  0.28.0  0.27.0  0.25.0  0.23.0  0.22.0  0.21.0  0.20.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.10.0  0.8.0  0.7.0  0.4.0  0.3.0  0.2.0 
    
    
    public static interface DeviceSession.SessionStateEventOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getEventTime()
    
    
    public abstract Timestamp getEventTime()

Output only. The time that the session_state first encountered that state.

`.google.protobuf.Timestamp event_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The eventTime.  
  
### getEventTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getEventTimeOrBuilder()

Output only. The time that the session_state first encountered that state.

`.google.protobuf.Timestamp event_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getSessionState()
    
    
    public abstract DeviceSession.SessionState getSessionState()

Output only. The session_state tracked by this event

` .google.cloud.devicestreaming.v1.DeviceSession.SessionState session_state = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[DeviceSession.SessionState](https://docs.cloud.google.com/java/docs/reference/google-cloud-devicestreaming/latest/com.google.cloud.devicestreaming.v1.DeviceSession.SessionState)` | The sessionState.  
  
### getSessionStateValue()
    
    
    public abstract int getSessionStateValue()

Output only. The session_state tracked by this event

` .google.cloud.devicestreaming.v1.DeviceSession.SessionState session_state = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for sessionState.  
  
### getStateMessage()
    
    
    public abstract String getStateMessage()

Output only. A human-readable message to explain the state.

`string state_message = 3 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The stateMessage.  
  
### getStateMessageBytes()
    
    
    public abstract ByteString getStateMessageBytes()

Output only. A human-readable message to explain the state.

`string state_message = 3 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for stateMessage.  
  
### hasEventTime()
    
    
    public abstract boolean hasEventTime()

Output only. The time that the session_state first encountered that state.

`.google.protobuf.Timestamp event_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the eventTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
