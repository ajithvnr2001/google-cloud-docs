---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.ListMcpServersResponseOrBuilder
title: Interface ListMcpServersResponseOrBuilder (0.6.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:17:10.907819+00:00
---

# Interface ListMcpServersResponseOrBuilder (0.6.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.ListMcpServersResponseOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ListMcpServersResponseOrBuilder (0.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.0 (latest)  0.2.0  0.1.0 
    
    
    public interface ListMcpServersResponseOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getMcpServers(int index)
    
    
    public abstract McpServer getMcpServers(int index)

The list of McpServers.

`repeated .google.cloud.agentregistry.v1.McpServer mcp_servers = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[McpServer](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.McpServer)` |   
  
### getMcpServersCount()
    
    
    public abstract int getMcpServersCount()

The list of McpServers.

`repeated .google.cloud.agentregistry.v1.McpServer mcp_servers = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getMcpServersList()
    
    
    public abstract List<McpServer> getMcpServersList()

The list of McpServers.

`repeated .google.cloud.agentregistry.v1.McpServer mcp_servers = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[McpServer](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.McpServer)>` |   
  
### getMcpServersOrBuilder(int index)
    
    
    public abstract McpServerOrBuilder getMcpServersOrBuilder(int index)

The list of McpServers.

`repeated .google.cloud.agentregistry.v1.McpServer mcp_servers = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[McpServerOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.McpServerOrBuilder)` |   
  
### getMcpServersOrBuilderList()
    
    
    public abstract List<? extends McpServerOrBuilder> getMcpServersOrBuilderList()

The list of McpServers.

`repeated .google.cloud.agentregistry.v1.McpServer mcp_servers = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.agentregistry.v1.McpServerOrBuilder>` |   
  
### getNextPageToken()
    
    
    public abstract String getNextPageToken()

A token identifying a page of results the server should return.

`string next_page_token = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The nextPageToken.  
  
### getNextPageTokenBytes()
    
    
    public abstract ByteString getNextPageTokenBytes()

A token identifying a page of results the server should return.

`string next_page_token = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for nextPageToken.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
