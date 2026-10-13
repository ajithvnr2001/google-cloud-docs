---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.StreamAssistRequestOrBuilder
title: Interface StreamAssistRequestOrBuilder (0.95.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:52:43.746736+00:00
---

# Interface StreamAssistRequestOrBuilder (0.95.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.StreamAssistRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface StreamAssistRequestOrBuilder (0.95.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.95.0 (latest)  0.91.0  0.90.0  0.89.0  0.87.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.70.0  0.69.0  0.68.0  0.66.0  0.64.0  0.63.0  0.60.0  0.59.0  0.58.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface StreamAssistRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAgentsSpec()
    
    
    public abstract StreamAssistRequest.AgentsSpec getAgentsSpec()

Optional. Specification of agents that are used to serve the request.

` .google.cloud.discoveryengine.v1beta.StreamAssistRequest.AgentsSpec agents_spec = 22 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[StreamAssistRequest.AgentsSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.StreamAssistRequest.AgentsSpec)` | The agentsSpec.  
  
### getAgentsSpecOrBuilder()
    
    
    public abstract StreamAssistRequest.AgentsSpecOrBuilder getAgentsSpecOrBuilder()

Optional. Specification of agents that are used to serve the request.

` .google.cloud.discoveryengine.v1beta.StreamAssistRequest.AgentsSpec agents_spec = 22 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[StreamAssistRequest.AgentsSpecOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.StreamAssistRequest.AgentsSpecOrBuilder)` |   
  
### getGenerationSpec()
    
    
    public abstract StreamAssistRequest.GenerationSpec getGenerationSpec()

Optional. Specification of the generation configuration for the request.

` .google.cloud.discoveryengine.v1beta.StreamAssistRequest.GenerationSpec generation_spec = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[StreamAssistRequest.GenerationSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.StreamAssistRequest.GenerationSpec)` | The generationSpec.  
  
### getGenerationSpecOrBuilder()
    
    
    public abstract StreamAssistRequest.GenerationSpecOrBuilder getGenerationSpecOrBuilder()

Optional. Specification of the generation configuration for the request.

` .google.cloud.discoveryengine.v1beta.StreamAssistRequest.GenerationSpec generation_spec = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[StreamAssistRequest.GenerationSpecOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.StreamAssistRequest.GenerationSpecOrBuilder)` |   
  
### getName()
    
    
    public abstract String getName()

Required. The resource name of the Assistant. Format: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}/assistants/{assistant}`

` string name = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Required. The resource name of the Assistant. Format: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}/assistants/{assistant}`

` string name = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getQuery()
    
    
    public abstract Query getQuery()

Optional. Current user query.

Empty query is only supported if `file_ids` are provided. In this case, the answer will be generated based on those context files.

` .google.cloud.discoveryengine.v1beta.Query query = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.Query)` | The query.  
  
### getQueryOrBuilder()
    
    
    public abstract QueryOrBuilder getQueryOrBuilder()

Optional. Current user query.

Empty query is only supported if `file_ids` are provided. In this case, the answer will be generated based on those context files.

` .google.cloud.discoveryengine.v1beta.Query query = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[QueryOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.QueryOrBuilder)` |   
  
### getSession()
    
    
    public abstract String getSession()

Optional. The session to use for the request. If specified, the assistant has access to the session history, and the query and the answer are stored there.

If `-` is specified as the session ID, or it is left empty, then a new session is created with an automatically generated ID.

Format: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}/sessions/{session}`

` string session = 3 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The session.  
  
### getSessionBytes()
    
    
    public abstract ByteString getSessionBytes()

Optional. The session to use for the request. If specified, the assistant has access to the session history, and the query and the answer are stored there.

If `-` is specified as the session ID, or it is left empty, then a new session is created with an automatically generated ID.

Format: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}/sessions/{session}`

` string session = 3 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for session.  
  
### getToolsSpec()
    
    
    public abstract StreamAssistRequest.ToolsSpec getToolsSpec()

Optional. Specification of tools that are used to serve the request.

` .google.cloud.discoveryengine.v1beta.StreamAssistRequest.ToolsSpec tools_spec = 18 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[StreamAssistRequest.ToolsSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.StreamAssistRequest.ToolsSpec)` | The toolsSpec.  
  
### getToolsSpecOrBuilder()
    
    
    public abstract StreamAssistRequest.ToolsSpecOrBuilder getToolsSpecOrBuilder()

Optional. Specification of tools that are used to serve the request.

` .google.cloud.discoveryengine.v1beta.StreamAssistRequest.ToolsSpec tools_spec = 18 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[StreamAssistRequest.ToolsSpecOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.StreamAssistRequest.ToolsSpecOrBuilder)` |   
  
### getUserMetadata()
    
    
    public abstract AssistUserMetadata getUserMetadata()

Optional. Information about the user initiating the query.

` .google.cloud.discoveryengine.v1beta.AssistUserMetadata user_metadata = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[AssistUserMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.AssistUserMetadata)` | The userMetadata.  
  
### getUserMetadataOrBuilder()
    
    
    public abstract AssistUserMetadataOrBuilder getUserMetadataOrBuilder()

Optional. Information about the user initiating the query.

` .google.cloud.discoveryengine.v1beta.AssistUserMetadata user_metadata = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[AssistUserMetadataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.AssistUserMetadataOrBuilder)` |   
  
### hasAgentsSpec()
    
    
    public abstract boolean hasAgentsSpec()

Optional. Specification of agents that are used to serve the request.

` .google.cloud.discoveryengine.v1beta.StreamAssistRequest.AgentsSpec agents_spec = 22 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the agentsSpec field is set.  
  
### hasGenerationSpec()
    
    
    public abstract boolean hasGenerationSpec()

Optional. Specification of the generation configuration for the request.

` .google.cloud.discoveryengine.v1beta.StreamAssistRequest.GenerationSpec generation_spec = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the generationSpec field is set.  
  
### hasQuery()
    
    
    public abstract boolean hasQuery()

Optional. Current user query.

Empty query is only supported if `file_ids` are provided. In this case, the answer will be generated based on those context files.

` .google.cloud.discoveryengine.v1beta.Query query = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the query field is set.  
  
### hasToolsSpec()
    
    
    public abstract boolean hasToolsSpec()

Optional. Specification of tools that are used to serve the request.

` .google.cloud.discoveryengine.v1beta.StreamAssistRequest.ToolsSpec tools_spec = 18 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the toolsSpec field is set.  
  
### hasUserMetadata()
    
    
    public abstract boolean hasUserMetadata()

Optional. Information about the user initiating the query.

` .google.cloud.discoveryengine.v1beta.AssistUserMetadata user_metadata = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the userMetadata field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
