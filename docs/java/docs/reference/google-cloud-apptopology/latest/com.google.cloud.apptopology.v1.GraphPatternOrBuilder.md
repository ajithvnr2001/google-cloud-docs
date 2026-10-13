---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.GraphPatternOrBuilder
title: Interface GraphPatternOrBuilder (0.3.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:40:04.143672+00:00
---

# Interface GraphPatternOrBuilder (0.3.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.GraphPatternOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface GraphPatternOrBuilder (0.3.0) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public interface GraphPatternOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getNeighbors(int index)
    
    
    public abstract ConnectedNodePattern getNeighbors(int index)

Optional. Pattern matcher to match the connected subgraphs; all of these are ANDed.

` repeated .google.cloud.apptopology.v1.ConnectedNodePattern neighbors = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConnectedNodePattern](https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.ConnectedNodePattern)` |   
  
### getNeighborsCount()
    
    
    public abstract int getNeighborsCount()

Optional. Pattern matcher to match the connected subgraphs; all of these are ANDed.

` repeated .google.cloud.apptopology.v1.ConnectedNodePattern neighbors = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getNeighborsList()
    
    
    public abstract List<ConnectedNodePattern> getNeighborsList()

Optional. Pattern matcher to match the connected subgraphs; all of these are ANDed.

` repeated .google.cloud.apptopology.v1.ConnectedNodePattern neighbors = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ConnectedNodePattern](https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.ConnectedNodePattern)>` |   
  
### getNeighborsOrBuilder(int index)
    
    
    public abstract ConnectedNodePatternOrBuilder getNeighborsOrBuilder(int index)

Optional. Pattern matcher to match the connected subgraphs; all of these are ANDed.

` repeated .google.cloud.apptopology.v1.ConnectedNodePattern neighbors = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConnectedNodePatternOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.ConnectedNodePatternOrBuilder)` |   
  
### getNeighborsOrBuilderList()
    
    
    public abstract List<? extends ConnectedNodePatternOrBuilder> getNeighborsOrBuilderList()

Optional. Pattern matcher to match the connected subgraphs; all of these are ANDed.

` repeated .google.cloud.apptopology.v1.ConnectedNodePattern neighbors = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.apptopology.v1.ConnectedNodePatternOrBuilder>` |   
  
### getStartingNode()
    
    
    public abstract NodePattern getStartingNode()

Required. Pattern matcher to select the starting nodes in the graph.

` .google.cloud.apptopology.v1.NodePattern starting_node = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[NodePattern](https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.NodePattern)` | The startingNode.  
  
### getStartingNodeOrBuilder()
    
    
    public abstract NodePatternOrBuilder getStartingNodeOrBuilder()

Required. Pattern matcher to select the starting nodes in the graph.

` .google.cloud.apptopology.v1.NodePattern starting_node = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[NodePatternOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.NodePatternOrBuilder)` |   
  
### hasStartingNode()
    
    
    public abstract boolean hasStartingNode()

Required. Pattern matcher to select the starting nodes in the graph.

` .google.cloud.apptopology.v1.NodePattern starting_node = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the startingNode field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
