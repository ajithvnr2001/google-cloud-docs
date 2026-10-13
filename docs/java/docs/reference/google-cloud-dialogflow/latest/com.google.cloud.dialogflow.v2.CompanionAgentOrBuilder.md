---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CompanionAgentOrBuilder
title: Interface CompanionAgentOrBuilder (4.105.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:13:12.307612+00:00
---

# Interface CompanionAgentOrBuilder (4.105.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CompanionAgentOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface CompanionAgentOrBuilder (4.105.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.105.0 (latest)  4.101.0  4.100.0  4.99.0  4.97.0  4.94.0  4.93.0  4.91.0  4.89.0  4.88.0  4.87.0  4.86.0  4.84.0  4.82.0  4.81.0  4.80.0  4.79.0  4.78.0  4.76.0  4.74.0  4.73.0  4.70.0  4.69.0  4.68.0  4.66.0  4.65.0  4.64.0  4.63.0  4.62.0  4.61.0  4.60.0  4.59.0  4.58.0  4.57.0  4.55.0  4.54.0  4.53.0  4.52.0  4.51.0  4.50.0  4.49.0  4.48.0  4.47.0  4.46.0  4.45.0  4.43.0  4.42.0  4.41.0  4.40.0  4.39.0  4.38.0  4.37.0  4.36.0  4.35.0  4.34.0  4.33.0  4.30.0  4.29.0  4.28.0  4.27.0  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.1  4.8.6  4.7.5  4.6.0  4.5.11  4.4.0  4.3.1 
    
    
    public interface CompanionAgentOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCesToolSpecs(int index)
    
    
    public abstract CesToolSpec getCesToolSpecs(int index)

Optional. List of CES tool specs that the companion agent can choose from.

` repeated .google.cloud.dialogflow.v2.CesToolSpec ces_tool_specs = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CesToolSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CesToolSpec)` |   
  
### getCesToolSpecsCount()
    
    
    public abstract int getCesToolSpecsCount()

Optional. List of CES tool specs that the companion agent can choose from.

` repeated .google.cloud.dialogflow.v2.CesToolSpec ces_tool_specs = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getCesToolSpecsList()
    
    
    public abstract List<CesToolSpec> getCesToolSpecsList()

Optional. List of CES tool specs that the companion agent can choose from.

` repeated .google.cloud.dialogflow.v2.CesToolSpec ces_tool_specs = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CesToolSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CesToolSpec)>` |   
  
### getCesToolSpecsOrBuilder(int index)
    
    
    public abstract CesToolSpecOrBuilder getCesToolSpecsOrBuilder(int index)

Optional. List of CES tool specs that the companion agent can choose from.

` repeated .google.cloud.dialogflow.v2.CesToolSpec ces_tool_specs = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CesToolSpecOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CesToolSpecOrBuilder)` |   
  
### getCesToolSpecsOrBuilderList()
    
    
    public abstract List<? extends CesToolSpecOrBuilder> getCesToolSpecsOrBuilderList()

Optional. List of CES tool specs that the companion agent can choose from.

` repeated .google.cloud.dialogflow.v2.CesToolSpec ces_tool_specs = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.dialogflow.v2.CesToolSpecOrBuilder>` |   
  
### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Output only. Creation time of this companion agent.

`.google.protobuf.Timestamp create_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. Creation time of this companion agent.

`.google.protobuf.Timestamp create_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDescription()
    
    
    public abstract String getDescription()

Optional. Description for the companion agent.

`string description = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public abstract ByteString getDescriptionBytes()

Optional. Description for the companion agent.

`string description = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getDisplayName()
    
    
    public abstract String getDisplayName()

Optional. Display name for the companion agent. Character limit is 63.

`string display_name = 8 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public abstract ByteString getDisplayNameBytes()

Optional. Display name for the companion agent. Character limit is 63.

`string display_name = 8 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getName()
    
    
    public abstract String getName()

Identifier. The unique identifier of the companion agent. Format: `projects/{project}/locations/{location}/companionAgents/{companion_agent}`

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Identifier. The unique identifier of the companion agent. Format: `projects/{project}/locations/{location}/companionAgents/{companion_agent}`

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getSkillConfigs(int index)
    
    
    public abstract CompanionAgent.SkillConfig getSkillConfigs(int index)

Optional. List of skill configs for the companion agent. Allows at most one instance of each SkillConfig type.

` repeated .google.cloud.dialogflow.v2.CompanionAgent.SkillConfig skill_configs = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CompanionAgent.SkillConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CompanionAgent.SkillConfig)` |   
  
### getSkillConfigsCount()
    
    
    public abstract int getSkillConfigsCount()

Optional. List of skill configs for the companion agent. Allows at most one instance of each SkillConfig type.

` repeated .google.cloud.dialogflow.v2.CompanionAgent.SkillConfig skill_configs = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getSkillConfigsList()
    
    
    public abstract List<CompanionAgent.SkillConfig> getSkillConfigsList()

Optional. List of skill configs for the companion agent. Allows at most one instance of each SkillConfig type.

` repeated .google.cloud.dialogflow.v2.CompanionAgent.SkillConfig skill_configs = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[SkillConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CompanionAgent.SkillConfig)>` |   
  
### getSkillConfigsOrBuilder(int index)
    
    
    public abstract CompanionAgent.SkillConfigOrBuilder getSkillConfigsOrBuilder(int index)

Optional. List of skill configs for the companion agent. Allows at most one instance of each SkillConfig type.

` repeated .google.cloud.dialogflow.v2.CompanionAgent.SkillConfig skill_configs = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CompanionAgent.SkillConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CompanionAgent.SkillConfigOrBuilder)` |   
  
### getSkillConfigsOrBuilderList()
    
    
    public abstract List<? extends CompanionAgent.SkillConfigOrBuilder> getSkillConfigsOrBuilderList()

Optional. List of skill configs for the companion agent. Allows at most one instance of each SkillConfig type.

` repeated .google.cloud.dialogflow.v2.CompanionAgent.SkillConfig skill_configs = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.dialogflow.v2.CompanionAgent.SkillConfigOrBuilder>` |   
  
### getToolsetTools(int index)
    
    
    public abstract ToolsetTool getToolsetTools(int index)

Optional. List of CES toolset specs that the companion agent can choose from.

` repeated .google.cloud.dialogflow.v2.ToolsetTool toolset_tools = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ToolsetTool](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ToolsetTool)` |   
  
### getToolsetToolsCount()
    
    
    public abstract int getToolsetToolsCount()

Optional. List of CES toolset specs that the companion agent can choose from.

` repeated .google.cloud.dialogflow.v2.ToolsetTool toolset_tools = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getToolsetToolsList()
    
    
    public abstract List<ToolsetTool> getToolsetToolsList()

Optional. List of CES toolset specs that the companion agent can choose from.

` repeated .google.cloud.dialogflow.v2.ToolsetTool toolset_tools = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ToolsetTool](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ToolsetTool)>` |   
  
### getToolsetToolsOrBuilder(int index)
    
    
    public abstract ToolsetToolOrBuilder getToolsetToolsOrBuilder(int index)

Optional. List of CES toolset specs that the companion agent can choose from.

` repeated .google.cloud.dialogflow.v2.ToolsetTool toolset_tools = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ToolsetToolOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ToolsetToolOrBuilder)` |   
  
### getToolsetToolsOrBuilderList()
    
    
    public abstract List<? extends ToolsetToolOrBuilder> getToolsetToolsOrBuilderList()

Optional. List of CES toolset specs that the companion agent can choose from.

` repeated .google.cloud.dialogflow.v2.ToolsetTool toolset_tools = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.dialogflow.v2.ToolsetToolOrBuilder>` |   
  
### getUpdateTime()
    
    
    public abstract Timestamp getUpdateTime()

Output only. Update time of this companion agent.

`.google.protobuf.Timestamp update_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getUpdateTimeOrBuilder()

Output only. Update time of this companion agent.

`.google.protobuf.Timestamp update_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. Creation time of this companion agent.

`.google.protobuf.Timestamp create_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasUpdateTime()
    
    
    public abstract boolean hasUpdateTime()

Output only. Update time of this companion agent.

`.google.protobuf.Timestamp update_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
