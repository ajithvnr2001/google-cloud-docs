---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ToolCallResult
title: Google Cloud Dialogflow v2beta1 API - Class ToolCallResult (1.0.0-beta33) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:15:52.433008+00:00
---

# Google Cloud Dialogflow v2beta1 API - Class ToolCallResult (1.0.0-beta33)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ToolCallResult

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Dialogflow v2beta1 API - Class ToolCallResult (1.0.0-beta33) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta33 (latest)  1.0.0-beta32 
    
    
    public sealed class ToolCallResult : IMessage<ToolCallResult>, IEquatable<ToolCallResult>, IDeepCloneable<ToolCallResult>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Dialogflow v2beta1 API class ToolCallResult.

The result of calling a tool's action.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ToolCallResult

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ToolCallResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ToolCallResult), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ToolCallResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ToolCallResult), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ToolCallResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ToolCallResult), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dialogflow.V2Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1)

## Assembly

Google.Cloud.Dialogflow.V2Beta1.dll

## Constructors 

### ToolCallResult()
    
    
    public ToolCallResult()

### ToolCallResult(ToolCallResult)
    
    
    public ToolCallResult(ToolCallResult other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ToolCallResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ToolCallResult)`  
  
  
## Properties 

### Action
    
    
    public string Action { get; set; }

Optional. The name of the tool's action associated with this call.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### AnswerRecord
    
    
    public string AnswerRecord { get; set; }

Optional. The answer record associated with this tool call result.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### CesApp
    
    
    public string CesApp { get; set; }

Optional. CES app name for this call. Format: `projects/<ProjectID>/locations/<LocationID>/apps/<AppID>`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### CesAppAsAppName
    
    
    public AppName CesAppAsAppName { get; set; }

[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.AppName)-typed view over the [CesApp](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ToolCallResult#Google_Cloud_Dialogflow_V2Beta1_ToolCallResult_CesApp) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.AppName)` |   
  
### CesTool
    
    
    public string CesTool { get; set; }

Optional. CES tool name for this call. Format: `projects/<ProjectID>/locations/<LocationID>/apps/<AppID>/tools/<ToolID>`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### CesToolAsCesToolName
    
    
    public CesToolName CesToolAsCesToolName { get; set; }

[CesToolName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.CesToolName)-typed view over the [CesTool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ToolCallResult#Google_Cloud_Dialogflow_V2Beta1_ToolCallResult_CesTool) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[CesToolName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.CesToolName)` |   
  
### CesToolset
    
    
    public string CesToolset { get; set; }

Optional. CES toolset name for this call. Format: `projects/<ProjectID>/locations/<LocationID>/apps/<AppID>/toolsets/ToolsetID>`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### CesToolsetAsToolsetName
    
    
    public ToolsetName CesToolsetAsToolsetName { get; set; }

[ToolsetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ToolsetName)-typed view over the [CesToolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ToolCallResult#Google_Cloud_Dialogflow_V2Beta1_ToolCallResult_CesToolset) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ToolsetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ToolsetName)` |   
  
### Content
    
    
    public string Content { get; set; }

Optional. Only populated if the response content is utf-8 encoded.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### CreateTime
    
    
    public Timestamp CreateTime { get; set; }

Output only. Create time of the tool call result.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### Error
    
    
    public ToolCallResult.Types.Error Error { get; set; }

Optional. The tool call's error.

**Property Value**  
---  
**Type** | **Description**  
`[ToolCallResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ToolCallResult)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ToolCallResult.Types)[Error](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ToolCallResult.Types.Error)` |   
  
### HasCesApp
    
    
    public bool HasCesApp { get; }

Gets whether the "ces_app" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasCesTool
    
    
    public bool HasCesTool { get; }

Gets whether the "ces_tool" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasCesToolset
    
    
    public bool HasCesToolset { get; }

Gets whether the "ces_toolset" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasContent
    
    
    public bool HasContent { get; }

Gets whether the "content" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasRawContent
    
    
    public bool HasRawContent { get; }

Gets whether the "raw_content" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasTool
    
    
    public bool HasTool { get; }

Gets whether the "tool" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### RawContent
    
    
    public ByteString RawContent { get; set; }

Optional. Only populated if the response content is not utf-8 encoded. (by definition byte fields are base64 encoded).

**Property Value**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)` |   
  
### ResultCase
    
    
    public ToolCallResult.ResultOneofCase ResultCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[ToolCallResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ToolCallResult)[ResultOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ToolCallResult.ResultOneofCase)` |   
  
### SourceCase
    
    
    public ToolCallResult.SourceOneofCase SourceCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[ToolCallResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ToolCallResult)[SourceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ToolCallResult.SourceOneofCase)` |   
  
### Tool
    
    
    public string Tool { get; set; }

Optional. The [tool][google.cloud.dialogflow.v2beta1.Tool] associated with this call. Format: `projects/<ProjectID>/locations/<LocationID>/tools/<ToolID>`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ToolAsToolName
    
    
    public ToolName ToolAsToolName { get; set; }

[ToolName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ToolName)-typed view over the [Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ToolCallResult#Google_Cloud_Dialogflow_V2Beta1_ToolCallResult_Tool) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ToolName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ToolName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
