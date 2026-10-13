---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.McpServerFloorSetting
title: Model Armor v1beta API - Class McpServerFloorSetting (1.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:44:23.893163+00:00
---

# Model Armor v1beta API - Class McpServerFloorSetting (1.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.McpServerFloorSetting

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Model Armor v1beta API - Class McpServerFloorSetting (1.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta06 (latest)  1.0.0-beta05 
    
    
    public sealed class McpServerFloorSetting : IMessage<McpServerFloorSetting>, IEquatable<McpServerFloorSetting>, IDeepCloneable<McpServerFloorSetting>, IBufferMessage, IMessage

Reference documentation and code samples for the Model Armor v1beta API class McpServerFloorSetting.

Message describing MCP Server Floor Setting.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > McpServerFloorSetting

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[McpServerFloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.McpServerFloorSetting), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[McpServerFloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.McpServerFloorSetting), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[McpServerFloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.McpServerFloorSetting), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ModelArmor.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta)

## Assembly

Google.Cloud.ModelArmor.V1Beta.dll

## Constructors 

### McpServerFloorSetting()
    
    
    public McpServerFloorSetting()

### McpServerFloorSetting(McpServerFloorSetting)
    
    
    public McpServerFloorSetting(McpServerFloorSetting other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[McpServerFloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.McpServerFloorSetting)`  
  
  
## Properties 

### Apis
    
    
    public RepeatedField<string> Apis { get; }

Optional. List of MCP servers for which the MCP floor setting is applicable. Examples: "bigquery.googleapis.com/mcp", "run.googleapis.com/mcp" Empty list denotes that the floor setting is applicable to all MCP servers.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### EnableCloudLogging
    
    
    public bool EnableCloudLogging { get; set; }

Optional. If true, log Model Armor filter results to Cloud Logging.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### EnforcementTypeCase
    
    
    public McpServerFloorSetting.EnforcementTypeOneofCase EnforcementTypeCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[McpServerFloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.McpServerFloorSetting)[EnforcementTypeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.McpServerFloorSetting.EnforcementTypeOneofCase)` |   
  
### HasInspectAndBlock
    
    
    public bool HasInspectAndBlock { get; }

Gets whether the "inspect_and_block" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasInspectOnly
    
    
    public bool HasInspectOnly { get; }

Gets whether the "inspect_only" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### InspectAndBlock
    
    
    public bool InspectAndBlock { get; set; }

Optional. If true, Model Armor filters will be run in inspect and block mode. Requests that trip Model Armor filters will be blocked.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### InspectOnly
    
    
    public bool InspectOnly { get; set; }

Optional. If true, Model Armor filters will be run in inspect only mode. No action will be taken on the request.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-05 UTC."],[],[]] 
