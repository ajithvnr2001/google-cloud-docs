---
url: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.visionai.v1.ProcessorOrBuilder
title: Interface ProcessorOrBuilder (0.16.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:44:41.069956+00:00
---

# Interface ProcessorOrBuilder (0.16.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.visionai.v1.ProcessorOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ProcessorOrBuilder (0.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 0.16.0 (latest) ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.visionai.v1.ProcessorOrBuilder)
  * [ 0.15.0 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.15.0/com.google.events.cloud.visionai.v1.ProcessorOrBuilder)
  * [ 0.14.1 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.14.1/com.google.events.cloud.visionai.v1.ProcessorOrBuilder)


    
    
    public interface ProcessorOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsLabels(String key)
    
    
    public abstract boolean containsLabels(String key)

Labels as key value pairs.

`map<string, string> labels = 4;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getConfigurationTypeurl()
    
    
    public abstract String getConfigurationTypeurl()

Output only. The corresponding configuration can be used in the Application to customize the behavior of the processor.

`string configuration_typeurl = 14;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The configurationTypeurl.  
  
### getConfigurationTypeurlBytes()
    
    
    public abstract ByteString getConfigurationTypeurlBytes()

Output only. The corresponding configuration can be used in the Application to customize the behavior of the processor.

`string configuration_typeurl = 14;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for configurationTypeurl.  
  
### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Output only. [Output only] Create timestamp.

`.google.protobuf.Timestamp create_time = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. [Output only] Create timestamp.

`.google.protobuf.Timestamp create_time = 2;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getCustomProcessorSourceInfo()
    
    
    public abstract CustomProcessorSourceInfo getCustomProcessorSourceInfo()

Source info for customer created processor.

` .google.events.cloud.visionai.v1.CustomProcessorSourceInfo custom_processor_source_info = 7; `

**Returns**  
---  
**Type** | **Description**  
`[CustomProcessorSourceInfo](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.visionai.v1.CustomProcessorSourceInfo)` | The customProcessorSourceInfo.  
  
### getCustomProcessorSourceInfoOrBuilder()
    
    
    public abstract CustomProcessorSourceInfoOrBuilder getCustomProcessorSourceInfoOrBuilder()

Source info for customer created processor.

` .google.events.cloud.visionai.v1.CustomProcessorSourceInfo custom_processor_source_info = 7; `

**Returns**  
---  
**Type** | **Description**  
`[CustomProcessorSourceInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.visionai.v1.CustomProcessorSourceInfoOrBuilder)` |   
  
### getDescription()
    
    
    public abstract String getDescription()

Illustrative sentences for describing the functionality of the processor.

`string description = 10;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public abstract ByteString getDescriptionBytes()

Illustrative sentences for describing the functionality of the processor.

`string description = 10;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getDisplayName()
    
    
    public abstract String getDisplayName()

Required. A user friendly display name for the processor.

`string display_name = 5;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public abstract ByteString getDisplayNameBytes()

Required. A user friendly display name for the processor.

`string display_name = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getLabels()
    
    
    public abstract Map<String,String> getLabels()

Use [#getLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.visionai.v1.ProcessorOrBuilder#com_google_events_cloud_visionai_v1_ProcessorOrBuilder_getLabelsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsCount()
    
    
    public abstract int getLabelsCount()

Labels as key value pairs.

`map<string, string> labels = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLabelsMap()
    
    
    public abstract Map<String,String> getLabelsMap()

Labels as key value pairs.

`map<string, string> labels = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsOrDefault(String key, String defaultValue)
    
    
    public abstract String getLabelsOrDefault(String key, String defaultValue)

Labels as key value pairs.

`map<string, string> labels = 4;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getLabelsOrThrow(String key)
    
    
    public abstract String getLabelsOrThrow(String key)

Labels as key value pairs.

`map<string, string> labels = 4;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getModelType()
    
    
    public abstract ModelType getModelType()

Model Type.

`.google.events.cloud.visionai.v1.ModelType model_type = 13;`

**Returns**  
---  
**Type** | **Description**  
`[ModelType](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.visionai.v1.ModelType)` | The modelType.  
  
### getModelTypeValue()
    
    
    public abstract int getModelTypeValue()

Model Type.

`.google.events.cloud.visionai.v1.ModelType model_type = 13;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for modelType.  
  
### getName()
    
    
    public abstract String getName()

name of resource.

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

name of resource.

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getProcessorIoSpec()
    
    
    public abstract ProcessorIOSpec getProcessorIoSpec()

Output only. [Output only] The input / output specifications of a processor, each type of processor has fixed input / output specs which cannot be altered by customer.

`.google.events.cloud.visionai.v1.ProcessorIOSpec processor_io_spec = 11;`

**Returns**  
---  
**Type** | **Description**  
`[ProcessorIOSpec](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.visionai.v1.ProcessorIOSpec)` | The processorIoSpec.  
  
### getProcessorIoSpecOrBuilder()
    
    
    public abstract ProcessorIOSpecOrBuilder getProcessorIoSpecOrBuilder()

Output only. [Output only] The input / output specifications of a processor, each type of processor has fixed input / output specs which cannot be altered by customer.

`.google.events.cloud.visionai.v1.ProcessorIOSpec processor_io_spec = 11;`

**Returns**  
---  
**Type** | **Description**  
`[ProcessorIOSpecOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.visionai.v1.ProcessorIOSpecOrBuilder)` |   
  
### getProcessorType()
    
    
    public abstract Processor.ProcessorType getProcessorType()

Output only. Processor Type.

`.google.events.cloud.visionai.v1.Processor.ProcessorType processor_type = 6;`

**Returns**  
---  
**Type** | **Description**  
`[Processor.ProcessorType](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.visionai.v1.Processor.ProcessorType)` | The processorType.  
  
### getProcessorTypeValue()
    
    
    public abstract int getProcessorTypeValue()

Output only. Processor Type.

`.google.events.cloud.visionai.v1.Processor.ProcessorType processor_type = 6;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for processorType.  
  
### getState()
    
    
    public abstract Processor.ProcessorState getState()

Output only. State of the Processor.

`.google.events.cloud.visionai.v1.Processor.ProcessorState state = 8;`

**Returns**  
---  
**Type** | **Description**  
`[Processor.ProcessorState](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.visionai.v1.Processor.ProcessorState)` | The state.  
  
### getStateValue()
    
    
    public abstract int getStateValue()

Output only. State of the Processor.

`.google.events.cloud.visionai.v1.Processor.ProcessorState state = 8;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for state.  
  
### getSupportedAnnotationTypes(int index)
    
    
    public abstract StreamAnnotationType getSupportedAnnotationTypes(int index)

` repeated .google.events.cloud.visionai.v1.StreamAnnotationType supported_annotation_types = 15; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[StreamAnnotationType](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.visionai.v1.StreamAnnotationType)` | The supportedAnnotationTypes at the given index.  
  
### getSupportedAnnotationTypesCount()
    
    
    public abstract int getSupportedAnnotationTypesCount()

` repeated .google.events.cloud.visionai.v1.StreamAnnotationType supported_annotation_types = 15; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of supportedAnnotationTypes.  
  
### getSupportedAnnotationTypesList()
    
    
    public abstract List<StreamAnnotationType> getSupportedAnnotationTypesList()

` repeated .google.events.cloud.visionai.v1.StreamAnnotationType supported_annotation_types = 15; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[StreamAnnotationType](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.visionai.v1.StreamAnnotationType)>` | A list containing the supportedAnnotationTypes.  
  
### getSupportedAnnotationTypesValue(int index)
    
    
    public abstract int getSupportedAnnotationTypesValue(int index)

` repeated .google.events.cloud.visionai.v1.StreamAnnotationType supported_annotation_types = 15; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire of supportedAnnotationTypes at the given index.  
  
### getSupportedAnnotationTypesValueList()
    
    
    public abstract List<Integer> getSupportedAnnotationTypesValueList()

` repeated .google.events.cloud.visionai.v1.StreamAnnotationType supported_annotation_types = 15; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>` | A list containing the enum numeric values on the wire for supportedAnnotationTypes.  
  
### getSupportsPostProcessing()
    
    
    public abstract boolean getSupportsPostProcessing()

Indicates if the processor supports post processing.

`bool supports_post_processing = 17;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The supportsPostProcessing.  
  
### getUpdateTime()
    
    
    public abstract Timestamp getUpdateTime()

Output only. [Output only] Update timestamp.

`.google.protobuf.Timestamp update_time = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getUpdateTimeOrBuilder()

Output only. [Output only] Update timestamp.

`.google.protobuf.Timestamp update_time = 3;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. [Output only] Create timestamp.

`.google.protobuf.Timestamp create_time = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasCustomProcessorSourceInfo()
    
    
    public abstract boolean hasCustomProcessorSourceInfo()

Source info for customer created processor.

` .google.events.cloud.visionai.v1.CustomProcessorSourceInfo custom_processor_source_info = 7; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the customProcessorSourceInfo field is set.  
  
### hasProcessorIoSpec()
    
    
    public abstract boolean hasProcessorIoSpec()

Output only. [Output only] The input / output specifications of a processor, each type of processor has fixed input / output specs which cannot be altered by customer.

`.google.events.cloud.visionai.v1.ProcessorIOSpec processor_io_spec = 11;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the processorIoSpec field is set.  
  
### hasUpdateTime()
    
    
    public abstract boolean hasUpdateTime()

Output only. [Output only] Update timestamp.

`.google.protobuf.Timestamp update_time = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
