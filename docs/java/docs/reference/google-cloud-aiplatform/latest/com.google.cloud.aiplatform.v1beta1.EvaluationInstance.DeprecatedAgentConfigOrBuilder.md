---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.EvaluationInstance.DeprecatedAgentConfigOrBuilder
title: Interface EvaluationInstance.DeprecatedAgentConfigOrBuilder (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:30:03.630864+00:00
---

# Interface EvaluationInstance.DeprecatedAgentConfigOrBuilder (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.EvaluationInstance.DeprecatedAgentConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface EvaluationInstance.DeprecatedAgentConfigOrBuilder (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 
    
    
    public static interface EvaluationInstance.DeprecatedAgentConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAgentId() (deprecated)
    
    
    public abstract String getAgentId()

Optional. Unique identifier of the agent. This ID is used to refer to this agent, e.g., in AgentEvent.author, or in the `sub_agents` field. It must be unique within the `agents` map.

`string agent_id = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The agentId.  
  
### getAgentIdBytes() (deprecated)
    
    
    public abstract ByteString getAgentIdBytes()

Optional. Unique identifier of the agent. This ID is used to refer to this agent, e.g., in AgentEvent.author, or in the `sub_agents` field. It must be unique within the `agents` map.

`string agent_id = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for agentId.  
  
### getAgentType() (deprecated)
    
    
    public abstract String getAgentType()

Optional. The type or class of the agent (e.g., "LlmAgent", "RouterAgent", "ToolUseAgent"). Useful for the autorater to understand the expected behavior of the agent.

`string agent_type = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The agentType.  
  
### getAgentTypeBytes() (deprecated)
    
    
    public abstract ByteString getAgentTypeBytes()

Optional. The type or class of the agent (e.g., "LlmAgent", "RouterAgent", "ToolUseAgent"). Useful for the autorater to understand the expected behavior of the agent.

`string agent_type = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for agentType.  
  
### getDescription() (deprecated)
    
    
    public abstract String getDescription()

Optional. A high-level description of the agent's role and responsibilities. Critical for evaluating if the agent is routing tasks correctly.

`string description = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes() (deprecated)
    
    
    public abstract ByteString getDescriptionBytes()

Optional. A high-level description of the agent's role and responsibilities. Critical for evaluating if the agent is routing tasks correctly.

`string description = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getDeveloperInstruction() (deprecated)
    
    
    public abstract EvaluationInstance.InstanceData getDeveloperInstruction()

Optional. Contains instructions from the developer for the agent. Can be static or a dynamic prompt template used with the `AgentEvent.state_delta` field.

` .google.cloud.aiplatform.v1beta1.EvaluationInstance.InstanceData developer_instruction = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[EvaluationInstance.InstanceData](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.EvaluationInstance.InstanceData)` | The developerInstruction.  
  
### getDeveloperInstructionOrBuilder() (deprecated)
    
    
    public abstract EvaluationInstance.InstanceDataOrBuilder getDeveloperInstructionOrBuilder()

Optional. Contains instructions from the developer for the agent. Can be static or a dynamic prompt template used with the `AgentEvent.state_delta` field.

` .google.cloud.aiplatform.v1beta1.EvaluationInstance.InstanceData developer_instruction = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[EvaluationInstance.InstanceDataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.EvaluationInstance.InstanceDataOrBuilder)` |   
  
### getSubAgents(int index) (deprecated)
    
    
    public abstract String getSubAgents(int index)

Optional. The list of valid agent IDs (names) that this agent can delegate to. This defines the directed edges in the agent system graph topology.

`repeated string sub_agents = 7 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The subAgents at the given index.  
  
### getSubAgentsBytes(int index) (deprecated)
    
    
    public abstract ByteString getSubAgentsBytes(int index)

Optional. The list of valid agent IDs (names) that this agent can delegate to. This defines the directed edges in the agent system graph topology.

`repeated string sub_agents = 7 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the subAgents at the given index.  
  
### getSubAgentsCount() (deprecated)
    
    
    public abstract int getSubAgentsCount()

Optional. The list of valid agent IDs (names) that this agent can delegate to. This defines the directed edges in the agent system graph topology.

`repeated string sub_agents = 7 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of subAgents.  
  
### getSubAgentsList() (deprecated)
    
    
    public abstract List<String> getSubAgentsList()

Optional. The list of valid agent IDs (names) that this agent can delegate to. This defines the directed edges in the agent system graph topology.

`repeated string sub_agents = 7 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the subAgents.  
  
### getTools() (deprecated)
    
    
    public abstract EvaluationInstance.DeprecatedAgentConfig.Tools getTools()

List of tools.

` .google.cloud.aiplatform.v1beta1.EvaluationInstance.DeprecatedAgentConfig.Tools tools = 2; `

**Returns**  
---  
**Type** | **Description**  
`[EvaluationInstance.DeprecatedAgentConfig.Tools](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.EvaluationInstance.DeprecatedAgentConfig.Tools)` | The tools.  
  
### getToolsDataCase() (deprecated)
    
    
    public abstract EvaluationInstance.DeprecatedAgentConfig.ToolsDataCase getToolsDataCase()

**Returns**  
---  
**Type** | **Description**  
`[EvaluationInstance.DeprecatedAgentConfig.ToolsDataCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.EvaluationInstance.DeprecatedAgentConfig.ToolsDataCase)` |   
  
### getToolsOrBuilder() (deprecated)
    
    
    public abstract EvaluationInstance.DeprecatedAgentConfig.ToolsOrBuilder getToolsOrBuilder()

List of tools.

` .google.cloud.aiplatform.v1beta1.EvaluationInstance.DeprecatedAgentConfig.Tools tools = 2; `

**Returns**  
---  
**Type** | **Description**  
`[EvaluationInstance.DeprecatedAgentConfig.ToolsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.EvaluationInstance.DeprecatedAgentConfig.ToolsOrBuilder)` |   
  
### getToolsText() (deprecated)
    
    
    public abstract String getToolsText()

A JSON string containing a list of tools available to an agent with info such as name, description, parameters and required parameters.

`string tools_text = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The toolsText.  
  
### getToolsTextBytes() (deprecated)
    
    
    public abstract ByteString getToolsTextBytes()

A JSON string containing a list of tools available to an agent with info such as name, description, parameters and required parameters.

`string tools_text = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for toolsText.  
  
### hasDeveloperInstruction() (deprecated)
    
    
    public abstract boolean hasDeveloperInstruction()

Optional. Contains instructions from the developer for the agent. Can be static or a dynamic prompt template used with the `AgentEvent.state_delta` field.

` .google.cloud.aiplatform.v1beta1.EvaluationInstance.InstanceData developer_instruction = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the developerInstruction field is set.  
  
### hasTools() (deprecated)
    
    
    public abstract boolean hasTools()

List of tools.

` .google.cloud.aiplatform.v1beta1.EvaluationInstance.DeprecatedAgentConfig.Tools tools = 2; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the tools field is set.  
  
### hasToolsText() (deprecated)
    
    
    public abstract boolean hasToolsText()

A JSON string containing a list of tools available to an agent with info such as name, description, parameters and required parameters.

`string tools_text = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the toolsText field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
