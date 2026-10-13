---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.WidgetTool.DataMappingOrBuilder
title: Interface WidgetTool.DataMappingOrBuilder (0.15.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:56:59.258252+00:00
---

# Interface WidgetTool.DataMappingOrBuilder (0.15.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.WidgetTool.DataMappingOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface WidgetTool.DataMappingOrBuilder (0.15.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.0 (latest)  0.11.0  0.10.0  0.9.0  0.7.0  0.4.0  0.3.0  0.1.0 
    
    
    public static interface WidgetTool.DataMappingOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsFieldMappings(String key)
    
    
    public abstract boolean containsFieldMappings(String key)

Optional. A map of widget input parameter fields to the corresponding output fields of the source tool.

`map<string, string> field_mappings = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getFieldMappings() (deprecated)
    
    
    public abstract Map<String,String> getFieldMappings()

Use [#getFieldMappingsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.WidgetTool.DataMappingOrBuilder#com_google_cloud_ces_v1beta_WidgetTool_DataMappingOrBuilder_getFieldMappingsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getFieldMappingsCount()
    
    
    public abstract int getFieldMappingsCount()

Optional. A map of widget input parameter fields to the corresponding output fields of the source tool.

`map<string, string> field_mappings = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getFieldMappingsMap()
    
    
    public abstract Map<String,String> getFieldMappingsMap()

Optional. A map of widget input parameter fields to the corresponding output fields of the source tool.

`map<string, string> field_mappings = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getFieldMappingsOrDefault(String key, String defaultValue)
    
    
    public abstract String getFieldMappingsOrDefault(String key, String defaultValue)

Optional. A map of widget input parameter fields to the corresponding output fields of the source tool.

`map<string, string> field_mappings = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getFieldMappingsOrThrow(String key)
    
    
    public abstract String getFieldMappingsOrThrow(String key)

Optional. A map of widget input parameter fields to the corresponding output fields of the source tool.

`map<string, string> field_mappings = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getMode()
    
    
    public abstract WidgetTool.DataMapping.Mode getMode()

Optional. The mode of the data mapping.

` .google.cloud.ces.v1beta.WidgetTool.DataMapping.Mode mode = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[WidgetTool.DataMapping.Mode](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.WidgetTool.DataMapping.Mode)` | The mode.  
  
### getModeValue()
    
    
    public abstract int getModeValue()

Optional. The mode of the data mapping.

` .google.cloud.ces.v1beta.WidgetTool.DataMapping.Mode mode = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for mode.  
  
### getPythonFunction()
    
    
    public abstract PythonFunction getPythonFunction()

Optional. Configuration for a Python function used to transform the source tool's output into the widget's input format.

` .google.cloud.ces.v1beta.PythonFunction python_function = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[PythonFunction](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.PythonFunction)` | The pythonFunction.  
  
### getPythonFunctionOrBuilder()
    
    
    public abstract PythonFunctionOrBuilder getPythonFunctionOrBuilder()

Optional. Configuration for a Python function used to transform the source tool's output into the widget's input format.

` .google.cloud.ces.v1beta.PythonFunction python_function = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[PythonFunctionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.PythonFunctionOrBuilder)` |   
  
### getPythonScript() (deprecated)
    
    
    public abstract String getPythonScript()

**Deprecated.** _google.cloud.ces.v1beta.WidgetTool.DataMapping.python_script is deprecated. See google/cloud/ces/v1beta/widget_tool.proto;l=97_

Deprecated: Use `python_function` instead.

`string python_script = 3 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The pythonScript.  
  
### getPythonScriptBytes() (deprecated)
    
    
    public abstract ByteString getPythonScriptBytes()

**Deprecated.** _google.cloud.ces.v1beta.WidgetTool.DataMapping.python_script is deprecated. See google/cloud/ces/v1beta/widget_tool.proto;l=97_

Deprecated: Use `python_function` instead.

`string python_script = 3 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for pythonScript.  
  
### getSourceToolName()
    
    
    public abstract String getSourceToolName()

Optional. The resource name of the tool that provides the data for the widget (e.g., a search tool or a custom function). Format: `projects/{project}/locations/{location}/agents/{agent}/tools/{tool}`

`string source_tool_name = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The sourceToolName.  
  
### getSourceToolNameBytes()
    
    
    public abstract ByteString getSourceToolNameBytes()

Optional. The resource name of the tool that provides the data for the widget (e.g., a search tool or a custom function). Format: `projects/{project}/locations/{location}/agents/{agent}/tools/{tool}`

`string source_tool_name = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for sourceToolName.  
  
### hasPythonFunction()
    
    
    public abstract boolean hasPythonFunction()

Optional. Configuration for a Python function used to transform the source tool's output into the widget's input format.

` .google.cloud.ces.v1beta.PythonFunction python_function = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the pythonFunction field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
