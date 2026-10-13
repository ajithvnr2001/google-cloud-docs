---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1beta.McpToolOrBuilder
title: Interface McpToolOrBuilder (0.18.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:28:31.618645+00:00
---

# Interface McpToolOrBuilder (0.18.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1beta.McpToolOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface McpToolOrBuilder (0.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.18.0 (latest)  0.14.0  0.13.0  0.12.0  0.10.0  0.7.0  0.6.0  0.4.0  0.2.0  0.1.0 
    
    
    public interface McpToolOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAnnotations()
    
    
    public abstract Struct getAnnotations()

Optional key-value object that allows developers to provide additional information regarding tool properties, behavior, and usage best practices. Annotations or tags to facilitate semantic search across tools ("semantic tags") are not in the MVP scope. When implemented, the first set of supported annotations will likely be the standard, predefined annotations from the open-source MCP spec. These include:

  * title: A human-readable title for the tool, useful for UI display.
  * readOnlyHint: If true, indicates the tool does not modify its environment.
  * destructiveHint: If true, the tool may perform destructive updates (only meaningful when readOnlyHint is false).
  * idempotentHint: If true, calling the tool repeatedly with the same arguments has no additional effect (only meaningful when readOnlyHint is false).
  * openWorldHint: If true, the tool may interact with an "open world" of external entities.



`.google.protobuf.Struct annotations = 7;`

**Returns**  
---  
**Type** | **Description**  
`[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)` | The annotations.  
  
### getAnnotationsOrBuilder()
    
    
    public abstract StructOrBuilder getAnnotationsOrBuilder()

Optional key-value object that allows developers to provide additional information regarding tool properties, behavior, and usage best practices. Annotations or tags to facilitate semantic search across tools ("semantic tags") are not in the MVP scope. When implemented, the first set of supported annotations will likely be the standard, predefined annotations from the open-source MCP spec. These include:

  * title: A human-readable title for the tool, useful for UI display.
  * readOnlyHint: If true, indicates the tool does not modify its environment.
  * destructiveHint: If true, the tool may perform destructive updates (only meaningful when readOnlyHint is false).
  * idempotentHint: If true, calling the tool repeatedly with the same arguments has no additional effect (only meaningful when readOnlyHint is false).
  * openWorldHint: If true, the tool may interact with an "open world" of external entities.



`.google.protobuf.Struct annotations = 7;`

**Returns**  
---  
**Type** | **Description**  
`[StructOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.StructOrBuilder.html)` |   
  
### getDescription()
    
    
    public abstract String getDescription()

A human-readable description of the tool's functionality.

`string description = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public abstract ByteString getDescriptionBytes()

A human-readable description of the tool's functionality.

`string description = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getDisplayName()
    
    
    public abstract String getDisplayName()

Optional. A human-readable name for the tool, suitable for display.

`string display_name = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public abstract ByteString getDisplayNameBytes()

Optional. A human-readable name for the tool, suitable for display.

`string display_name = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getInputSchema()
    
    
    public abstract Struct getInputSchema()

A JSON Schema object defining the expected parameters for invoking the tool.

`.google.protobuf.Struct input_schema = 5;`

**Returns**  
---  
**Type** | **Description**  
`[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)` | The inputSchema.  
  
### getInputSchemaOrBuilder()
    
    
    public abstract StructOrBuilder getInputSchemaOrBuilder()

A JSON Schema object defining the expected parameters for invoking the tool.

`.google.protobuf.Struct input_schema = 5;`

**Returns**  
---  
**Type** | **Description**  
`[StructOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.StructOrBuilder.html)` |   
  
### getMcpServerUrls(int index)
    
    
    public abstract String getMcpServerUrls(int index)

Automatically populated reference to MCP Server. Helpful when multiple tools are requested across different MCP Servers.

`repeated string mcp_server_urls = 4;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The mcpServerUrls at the given index.  
  
### getMcpServerUrlsBytes(int index)
    
    
    public abstract ByteString getMcpServerUrlsBytes(int index)

Automatically populated reference to MCP Server. Helpful when multiple tools are requested across different MCP Servers.

`repeated string mcp_server_urls = 4;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the mcpServerUrls at the given index.  
  
### getMcpServerUrlsCount()
    
    
    public abstract int getMcpServerUrlsCount()

Automatically populated reference to MCP Server. Helpful when multiple tools are requested across different MCP Servers.

`repeated string mcp_server_urls = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of mcpServerUrls.  
  
### getMcpServerUrlsList()
    
    
    public abstract List<String> getMcpServerUrlsList()

Automatically populated reference to MCP Server. Helpful when multiple tools are requested across different MCP Servers.

`repeated string mcp_server_urls = 4;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the mcpServerUrls.  
  
### getName()
    
    
    public abstract String getName()

Identifier. The resource name of the McpTool. Format: `projects/{project}/locations/{location}/mcpServers/{mcp_server}/mcpTools/{mcp_tool}`. Example: projects/12345/locations/us-central1/mcpServers/google:bigquery.googleapis.com:mcp/mcpTools/insert_job for 1p projects/12345/locations/us-central1/mcpServers/apphub:starbucks/mcpTools/order_pizza for 2p

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Identifier. The resource name of the McpTool. Format: `projects/{project}/locations/{location}/mcpServers/{mcp_server}/mcpTools/{mcp_tool}`. Example: projects/12345/locations/us-central1/mcpServers/google:bigquery.googleapis.com:mcp/mcpTools/insert_job for 1p projects/12345/locations/us-central1/mcpServers/apphub:starbucks/mcpTools/order_pizza for 2p

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getOutputSchema()
    
    
    public abstract Struct getOutputSchema()

Optional. A JSON Schema object defining the expected structure of the tool's output.

`.google.protobuf.Struct output_schema = 6;`

**Returns**  
---  
**Type** | **Description**  
`[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)` | The outputSchema.  
  
### getOutputSchemaOrBuilder()
    
    
    public abstract StructOrBuilder getOutputSchemaOrBuilder()

Optional. A JSON Schema object defining the expected structure of the tool's output.

`.google.protobuf.Struct output_schema = 6;`

**Returns**  
---  
**Type** | **Description**  
`[StructOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.StructOrBuilder.html)` |   
  
### hasAnnotations()
    
    
    public abstract boolean hasAnnotations()

Optional key-value object that allows developers to provide additional information regarding tool properties, behavior, and usage best practices. Annotations or tags to facilitate semantic search across tools ("semantic tags") are not in the MVP scope. When implemented, the first set of supported annotations will likely be the standard, predefined annotations from the open-source MCP spec. These include:

  * title: A human-readable title for the tool, useful for UI display.
  * readOnlyHint: If true, indicates the tool does not modify its environment.
  * destructiveHint: If true, the tool may perform destructive updates (only meaningful when readOnlyHint is false).
  * idempotentHint: If true, calling the tool repeatedly with the same arguments has no additional effect (only meaningful when readOnlyHint is false).
  * openWorldHint: If true, the tool may interact with an "open world" of external entities.



`.google.protobuf.Struct annotations = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the annotations field is set.  
  
### hasInputSchema()
    
    
    public abstract boolean hasInputSchema()

A JSON Schema object defining the expected parameters for invoking the tool.

`.google.protobuf.Struct input_schema = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the inputSchema field is set.  
  
### hasOutputSchema()
    
    
    public abstract boolean hasOutputSchema()

Optional. A JSON Schema object defining the expected structure of the tool's output.

`.google.protobuf.Struct output_schema = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the outputSchema field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
