---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.KnowledgeConnectorSettingsOrBuilder
title: Interface KnowledgeConnectorSettingsOrBuilder (0.110.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:20:29.798138+00:00
---

# Interface KnowledgeConnectorSettingsOrBuilder (0.110.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.KnowledgeConnectorSettingsOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface KnowledgeConnectorSettingsOrBuilder (0.110.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.110.0 (latest)  0.106.0  0.105.0  0.104.0  0.102.0  0.99.0  0.98.0  0.96.0  0.94.0  0.93.0  0.92.0  0.91.0  0.89.0  0.87.0  0.86.0  0.85.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.75.0  0.74.0  0.73.0  0.71.0  0.70.0  0.69.0  0.68.0  0.67.0  0.66.0  0.65.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.7  0.13.1  0.12.1  0.11.5 
    
    
    public interface KnowledgeConnectorSettingsOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getDataStoreConnections(int index)
    
    
    public abstract DataStoreConnection getDataStoreConnections(int index)

Optional. List of related data store connections.

` repeated .google.cloud.dialogflow.cx.v3.DataStoreConnection data_store_connections = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataStoreConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DataStoreConnection)` |   
  
### getDataStoreConnectionsCount()
    
    
    public abstract int getDataStoreConnectionsCount()

Optional. List of related data store connections.

` repeated .google.cloud.dialogflow.cx.v3.DataStoreConnection data_store_connections = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getDataStoreConnectionsList()
    
    
    public abstract List<DataStoreConnection> getDataStoreConnectionsList()

Optional. List of related data store connections.

` repeated .google.cloud.dialogflow.cx.v3.DataStoreConnection data_store_connections = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[DataStoreConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DataStoreConnection)>` |   
  
### getDataStoreConnectionsOrBuilder(int index)
    
    
    public abstract DataStoreConnectionOrBuilder getDataStoreConnectionsOrBuilder(int index)

Optional. List of related data store connections.

` repeated .google.cloud.dialogflow.cx.v3.DataStoreConnection data_store_connections = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataStoreConnectionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DataStoreConnectionOrBuilder)` |   
  
### getDataStoreConnectionsOrBuilderList()
    
    
    public abstract List<? extends DataStoreConnectionOrBuilder> getDataStoreConnectionsOrBuilderList()

Optional. List of related data store connections.

` repeated .google.cloud.dialogflow.cx.v3.DataStoreConnection data_store_connections = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.dialogflow.cx.v3.DataStoreConnectionOrBuilder>` |   
  
### getEnabled()
    
    
    public abstract boolean getEnabled()

Whether Knowledge Connector is enabled or not.

`bool enabled = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enabled.  
  
### getTargetCase()
    
    
    public abstract KnowledgeConnectorSettings.TargetCase getTargetCase()

**Returns**  
---  
**Type** | **Description**  
`[KnowledgeConnectorSettings.TargetCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.KnowledgeConnectorSettings.TargetCase)` |   
  
### getTargetFlow()
    
    
    public abstract String getTargetFlow()

The target flow to transition to. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>`.

`string target_flow = 5 [(.google.api.resource_reference) = { ... }`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The targetFlow.  
  
### getTargetFlowBytes()
    
    
    public abstract ByteString getTargetFlowBytes()

The target flow to transition to. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>`.

`string target_flow = 5 [(.google.api.resource_reference) = { ... }`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for targetFlow.  
  
### getTargetPage()
    
    
    public abstract String getTargetPage()

The target page to transition to. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/pages/<PageID>`.

`string target_page = 4 [(.google.api.resource_reference) = { ... }`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The targetPage.  
  
### getTargetPageBytes()
    
    
    public abstract ByteString getTargetPageBytes()

The target page to transition to. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/pages/<PageID>`.

`string target_page = 4 [(.google.api.resource_reference) = { ... }`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for targetPage.  
  
### getTriggerFulfillment()
    
    
    public abstract Fulfillment getTriggerFulfillment()

The fulfillment to be triggered.

When the answers from the Knowledge Connector are selected by Dialogflow, you can utitlize the request scoped parameter `$request.knowledge.answers` (contains up to the 5 highest confidence answers) and `$request.knowledge.questions` (contains the corresponding questions) to construct the fulfillment.

`.google.cloud.dialogflow.cx.v3.Fulfillment trigger_fulfillment = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Fulfillment](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Fulfillment)` | The triggerFulfillment.  
  
### getTriggerFulfillmentOrBuilder()
    
    
    public abstract FulfillmentOrBuilder getTriggerFulfillmentOrBuilder()

The fulfillment to be triggered.

When the answers from the Knowledge Connector are selected by Dialogflow, you can utitlize the request scoped parameter `$request.knowledge.answers` (contains up to the 5 highest confidence answers) and `$request.knowledge.questions` (contains the corresponding questions) to construct the fulfillment.

`.google.cloud.dialogflow.cx.v3.Fulfillment trigger_fulfillment = 3;`

**Returns**  
---  
**Type** | **Description**  
`[FulfillmentOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.FulfillmentOrBuilder)` |   
  
### hasTargetFlow()
    
    
    public abstract boolean hasTargetFlow()

The target flow to transition to. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>`.

`string target_flow = 5 [(.google.api.resource_reference) = { ... }`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the targetFlow field is set.  
  
### hasTargetPage()
    
    
    public abstract boolean hasTargetPage()

The target page to transition to. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/pages/<PageID>`.

`string target_page = 4 [(.google.api.resource_reference) = { ... }`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the targetPage field is set.  
  
### hasTriggerFulfillment()
    
    
    public abstract boolean hasTriggerFulfillment()

The fulfillment to be triggered.

When the answers from the Knowledge Connector are selected by Dialogflow, you can utitlize the request scoped parameter `$request.knowledge.answers` (contains up to the 5 highest confidence answers) and `$request.knowledge.questions` (contains the corresponding questions) to construct the fulfillment.

`.google.cloud.dialogflow.cx.v3.Fulfillment trigger_fulfillment = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the triggerFulfillment field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
