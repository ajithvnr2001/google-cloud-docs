---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.McpServerOrBuilder
title: Interface McpServerOrBuilder (0.18.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:28:20.823445+00:00
---

# Interface McpServerOrBuilder (0.18.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.McpServerOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface McpServerOrBuilder (0.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.18.0 (latest)  0.14.0  0.13.0  0.12.0  0.10.0  0.7.0  0.6.0  0.4.0  0.2.0  0.1.0 
    
    
    public interface McpServerOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCapabilities()
    
    
    public abstract Struct getCapabilities()

The capabilities that a server may support. Known capabilities defined in <https://modelcontextprotocol.io/specification/2025-06-18/schema#servercapabilities> and additional capabilities defined by the servers.

`.google.protobuf.Struct capabilities = 6;`

**Returns**  
---  
**Type** | **Description**  
`[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)` | The capabilities.  
  
### getCapabilitiesOrBuilder()
    
    
    public abstract StructOrBuilder getCapabilitiesOrBuilder()

The capabilities that a server may support. Known capabilities defined in <https://modelcontextprotocol.io/specification/2025-06-18/schema#servercapabilities> and additional capabilities defined by the servers.

`.google.protobuf.Struct capabilities = 6;`

**Returns**  
---  
**Type** | **Description**  
`[StructOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.StructOrBuilder.html)` |   
  
### getDescription()
    
    
    public abstract String getDescription()

Optional. A human-readable description of the MCP Server's functionality.

`string description = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public abstract ByteString getDescriptionBytes()

Optional. A human-readable description of the MCP Server's functionality.

`string description = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getDisplayName()
    
    
    public abstract String getDisplayName()

Optional. A human readable name for the MCP server.

`string display_name = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public abstract ByteString getDisplayNameBytes()

Optional. A human readable name for the MCP server.

`string display_name = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getName()
    
    
    public abstract String getName()

Identifier. The resource name of the MCP Server. Format: `projects/{project}/locations/{location}/mcpServers/{mcp_server}`. Example: projects/12345/locations/us-central1/mcpServers/google:bigquery.googleapis.com:mcp for 1p projects/12345/locations/us-central1/mcpServers/apphub:starbucks for 2p

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Identifier. The resource name of the MCP Server. Format: `projects/{project}/locations/{location}/mcpServers/{mcp_server}`. Example: projects/12345/locations/us-central1/mcpServers/google:bigquery.googleapis.com:mcp for 1p projects/12345/locations/us-central1/mcpServers/apphub:starbucks for 2p

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getState()
    
    
    public abstract State getState()

Output only. The state of the MCP Server.

` .google.cloud.apiregistry.v1.State state = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[State](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.State)` | The state.  
  
### getStateValue()
    
    
    public abstract int getStateValue()

Output only. The state of the MCP Server.

` .google.cloud.apiregistry.v1.State state = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for state.  
  
### getUrls(int index)
    
    
    public abstract String getUrls(int index)

The base URL of the MCP server. Example: [geolocation.googleapis.com/mcp].

`repeated string urls = 4;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The urls at the given index.  
  
### getUrlsBytes(int index)
    
    
    public abstract ByteString getUrlsBytes(int index)

The base URL of the MCP server. Example: [geolocation.googleapis.com/mcp].

`repeated string urls = 4;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the urls at the given index.  
  
### getUrlsCount()
    
    
    public abstract int getUrlsCount()

The base URL of the MCP server. Example: [geolocation.googleapis.com/mcp].

`repeated string urls = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of urls.  
  
### getUrlsList()
    
    
    public abstract List<String> getUrlsList()

The base URL of the MCP server. Example: [geolocation.googleapis.com/mcp].

`repeated string urls = 4;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the urls.  
  
### hasCapabilities()
    
    
    public abstract boolean hasCapabilities()

The capabilities that a server may support. Known capabilities defined in <https://modelcontextprotocol.io/specification/2025-06-18/schema#servercapabilities> and additional capabilities defined by the servers.

`.google.protobuf.Struct capabilities = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the capabilities field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
