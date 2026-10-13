---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TraceBlockOrBuilder
title: Interface TraceBlockOrBuilder (0.110.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:48:48.430623+00:00
---

# Interface TraceBlockOrBuilder (0.110.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TraceBlockOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface TraceBlockOrBuilder (0.110.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.110.0 (latest)  0.106.0  0.105.0  0.104.0  0.102.0  0.99.0  0.98.0  0.96.0  0.94.0  0.93.0  0.92.0  0.91.0  0.89.0  0.87.0  0.86.0  0.85.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.75.0  0.74.0  0.73.0  0.71.0  0.70.0  0.69.0  0.68.0  0.67.0  0.66.0  0.65.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.7  0.13.1  0.12.1  0.11.5 
    
    
    public interface TraceBlockOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getActions(int index)
    
    
    public abstract Action getActions(int index)

The actions performed by the agent and the user during this session.

`repeated .google.cloud.dialogflow.cx.v3.Action actions = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Action)` |   
  
### getActionsCount()
    
    
    public abstract int getActionsCount()

The actions performed by the agent and the user during this session.

`repeated .google.cloud.dialogflow.cx.v3.Action actions = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getActionsList()
    
    
    public abstract List<Action> getActionsList()

The actions performed by the agent and the user during this session.

`repeated .google.cloud.dialogflow.cx.v3.Action actions = 3;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Action)>` |   
  
### getActionsOrBuilder(int index)
    
    
    public abstract ActionOrBuilder getActionsOrBuilder(int index)

The actions performed by the agent and the user during this session.

`repeated .google.cloud.dialogflow.cx.v3.Action actions = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ActionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ActionOrBuilder)` |   
  
### getActionsOrBuilderList()
    
    
    public abstract List<? extends ActionOrBuilder> getActionsOrBuilderList()

The actions performed by the agent and the user during this session.

`repeated .google.cloud.dialogflow.cx.v3.Action actions = 3;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.dialogflow.cx.v3.ActionOrBuilder>` |   
  
### getCompleteTime()
    
    
    public abstract Timestamp getCompleteTime()

Output only. Timestamp of the end of the trace block.

` .google.protobuf.Timestamp complete_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The completeTime.  
  
### getCompleteTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCompleteTimeOrBuilder()

Output only. Timestamp of the end of the trace block.

` .google.protobuf.Timestamp complete_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getEndState()
    
    
    public abstract OutputState getEndState()

Optional. Output only. The end state of the trace block.

` .google.cloud.dialogflow.cx.v3.OutputState end_state = 7 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[OutputState](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.OutputState)` | The endState.  
  
### getEndStateValue()
    
    
    public abstract int getEndStateValue()

Optional. Output only. The end state of the trace block.

` .google.cloud.dialogflow.cx.v3.OutputState end_state = 7 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for endState.  
  
### getFlowTraceMetadata()
    
    
    public abstract FlowTraceMetadata getFlowTraceMetadata()

Metadata of the flow trace.

`.google.cloud.dialogflow.cx.v3.FlowTraceMetadata flow_trace_metadata = 2;`

**Returns**  
---  
**Type** | **Description**  
`[FlowTraceMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.FlowTraceMetadata)` | The flowTraceMetadata.  
  
### getFlowTraceMetadataOrBuilder()
    
    
    public abstract FlowTraceMetadataOrBuilder getFlowTraceMetadataOrBuilder()

Metadata of the flow trace.

`.google.cloud.dialogflow.cx.v3.FlowTraceMetadata flow_trace_metadata = 2;`

**Returns**  
---  
**Type** | **Description**  
`[FlowTraceMetadataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.FlowTraceMetadataOrBuilder)` |   
  
### getInputParameters()
    
    
    public abstract Struct getInputParameters()

Optional. A list of input parameters of the trace block.

`.google.protobuf.Struct input_parameters = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)` | The inputParameters.  
  
### getInputParametersOrBuilder()
    
    
    public abstract StructOrBuilder getInputParametersOrBuilder()

Optional. A list of input parameters of the trace block.

`.google.protobuf.Struct input_parameters = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[StructOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.StructOrBuilder.html)` |   
  
### getOutputParameters()
    
    
    public abstract Struct getOutputParameters()

Optional. A list of output parameters of the trace block.

`.google.protobuf.Struct output_parameters = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)` | The outputParameters.  
  
### getOutputParametersOrBuilder()
    
    
    public abstract StructOrBuilder getOutputParametersOrBuilder()

Optional. A list of output parameters of the trace block.

`.google.protobuf.Struct output_parameters = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[StructOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.StructOrBuilder.html)` |   
  
### getPlaybookTraceMetadata()
    
    
    public abstract PlaybookTraceMetadata getPlaybookTraceMetadata()

Metadata of the playbook trace.

`.google.cloud.dialogflow.cx.v3.PlaybookTraceMetadata playbook_trace_metadata = 1;`

**Returns**  
---  
**Type** | **Description**  
`[PlaybookTraceMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.PlaybookTraceMetadata)` | The playbookTraceMetadata.  
  
### getPlaybookTraceMetadataOrBuilder()
    
    
    public abstract PlaybookTraceMetadataOrBuilder getPlaybookTraceMetadataOrBuilder()

Metadata of the playbook trace.

`.google.cloud.dialogflow.cx.v3.PlaybookTraceMetadata playbook_trace_metadata = 1;`

**Returns**  
---  
**Type** | **Description**  
`[PlaybookTraceMetadataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.PlaybookTraceMetadataOrBuilder)` |   
  
### getSpeechProcessingMetadata()
    
    
    public abstract SpeechProcessingMetadata getSpeechProcessingMetadata()

Metadata of the speech-to-text and speech-to-text processing.

`.google.cloud.dialogflow.cx.v3.SpeechProcessingMetadata speech_processing_metadata = 8; `

**Returns**  
---  
**Type** | **Description**  
`[SpeechProcessingMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SpeechProcessingMetadata)` | The speechProcessingMetadata.  
  
### getSpeechProcessingMetadataOrBuilder()
    
    
    public abstract SpeechProcessingMetadataOrBuilder getSpeechProcessingMetadataOrBuilder()

Metadata of the speech-to-text and speech-to-text processing.

`.google.cloud.dialogflow.cx.v3.SpeechProcessingMetadata speech_processing_metadata = 8; `

**Returns**  
---  
**Type** | **Description**  
`[SpeechProcessingMetadataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SpeechProcessingMetadataOrBuilder)` |   
  
### getStartTime()
    
    
    public abstract Timestamp getStartTime()

Output only. Timestamp of the start of the trace block.

`.google.protobuf.Timestamp start_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The startTime.  
  
### getStartTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getStartTimeOrBuilder()

Output only. Timestamp of the start of the trace block.

`.google.protobuf.Timestamp start_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getTraceMetadataCase()
    
    
    public abstract TraceBlock.TraceMetadataCase getTraceMetadataCase()

**Returns**  
---  
**Type** | **Description**  
`[TraceBlock.TraceMetadataCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TraceBlock.TraceMetadataCase)` |   
  
### hasCompleteTime()
    
    
    public abstract boolean hasCompleteTime()

Output only. Timestamp of the end of the trace block.

` .google.protobuf.Timestamp complete_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the completeTime field is set.  
  
### hasFlowTraceMetadata()
    
    
    public abstract boolean hasFlowTraceMetadata()

Metadata of the flow trace.

`.google.cloud.dialogflow.cx.v3.FlowTraceMetadata flow_trace_metadata = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the flowTraceMetadata field is set.  
  
### hasInputParameters()
    
    
    public abstract boolean hasInputParameters()

Optional. A list of input parameters of the trace block.

`.google.protobuf.Struct input_parameters = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the inputParameters field is set.  
  
### hasOutputParameters()
    
    
    public abstract boolean hasOutputParameters()

Optional. A list of output parameters of the trace block.

`.google.protobuf.Struct output_parameters = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the outputParameters field is set.  
  
### hasPlaybookTraceMetadata()
    
    
    public abstract boolean hasPlaybookTraceMetadata()

Metadata of the playbook trace.

`.google.cloud.dialogflow.cx.v3.PlaybookTraceMetadata playbook_trace_metadata = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the playbookTraceMetadata field is set.  
  
### hasSpeechProcessingMetadata()
    
    
    public abstract boolean hasSpeechProcessingMetadata()

Metadata of the speech-to-text and speech-to-text processing.

`.google.cloud.dialogflow.cx.v3.SpeechProcessingMetadata speech_processing_metadata = 8; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the speechProcessingMetadata field is set.  
  
### hasStartTime()
    
    
    public abstract boolean hasStartTime()

Output only. Timestamp of the start of the trace block.

`.google.protobuf.Timestamp start_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the startTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
