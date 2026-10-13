---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ConfigVariable
title: API hub v1 API - Class ConfigVariable (1.2.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:10:00.800628+00:00
---

# API hub v1 API - Class ConfigVariable (1.2.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ConfigVariable

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  API hub v1 API - Class ConfigVariable (1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.2.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ConfigVariable)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/1.1.0/Google.Cloud.ApiHub.V1.ConfigVariable)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/1.0.0/Google.Cloud.ApiHub.V1.ConfigVariable)


    
    
    public sealed class ConfigVariable : IMessage<ConfigVariable>, IEquatable<ConfigVariable>, IDeepCloneable<ConfigVariable>, IBufferMessage, IMessage

Reference documentation and code samples for the API hub v1 API class ConfigVariable.

ConfigVariable represents a additional configuration variable present in a PluginInstance Config or AuthConfig, based on a ConfigVariableTemplate.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ConfigVariable

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ConfigVariable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ConfigVariable), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ConfigVariable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ConfigVariable), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ConfigVariable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ConfigVariable), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ApiHub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1)

## Assembly

Google.Cloud.ApiHub.V1.dll

## Constructors 

### ConfigVariable()
    
    
    public ConfigVariable()

### ConfigVariable(ConfigVariable)
    
    
    public ConfigVariable(ConfigVariable other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ConfigVariable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ConfigVariable)`  
  
  
## Properties 

### BoolValue
    
    
    public bool BoolValue { get; set; }

Optional. The config variable value in case of config variable of type boolean.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### EnumValue
    
    
    public ConfigValueOption EnumValue { get; set; }

Optional. The config variable value in case of config variable of type enum.

**Property Value**  
---  
**Type** | **Description**  
`[ConfigValueOption](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ConfigValueOption)` |   
  
### HasBoolValue
    
    
    public bool HasBoolValue { get; }

Gets whether the "bool_value" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasIntValue
    
    
    public bool HasIntValue { get; }

Gets whether the "int_value" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasStringValue
    
    
    public bool HasStringValue { get; }

Gets whether the "string_value" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### IntValue
    
    
    public long IntValue { get; set; }

Optional. The config variable value in case of config variable of type integer.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### Key
    
    
    public string Key { get; set; }

Output only. Key will be the [id][google.cloud.apihub.v1.ConfigVariableTemplate.id] to uniquely identify the config variable.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### MultiIntValues
    
    
    public ConfigVariable.Types.MultiIntValues MultiIntValues { get; set; }

Optional. The config variable value in case of config variable of type multi integer.

**Property Value**  
---  
**Type** | **Description**  
`[ConfigVariable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ConfigVariable)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ConfigVariable.Types)[MultiIntValues](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ConfigVariable.Types.MultiIntValues)` |   
  
### MultiSelectValues
    
    
    public ConfigVariable.Types.MultiSelectValues MultiSelectValues { get; set; }

Optional. The config variable value in case of config variable of type multi select.

**Property Value**  
---  
**Type** | **Description**  
`[ConfigVariable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ConfigVariable)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ConfigVariable.Types)[MultiSelectValues](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ConfigVariable.Types.MultiSelectValues)` |   
  
### MultiStringValues
    
    
    public ConfigVariable.Types.MultiStringValues MultiStringValues { get; set; }

Optional. The config variable value in case of config variable of type multi string.

**Property Value**  
---  
**Type** | **Description**  
`[ConfigVariable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ConfigVariable)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ConfigVariable.Types)[MultiStringValues](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ConfigVariable.Types.MultiStringValues)` |   
  
### SecretValue
    
    
    public Secret SecretValue { get; set; }

Optional. The config variable value in case of config variable of type secret.

**Property Value**  
---  
**Type** | **Description**  
`[Secret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.Secret)` |   
  
### StringValue
    
    
    public string StringValue { get; set; }

Optional. The config variable value in case of config variable of type string.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ValueCase
    
    
    public ConfigVariable.ValueOneofCase ValueCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[ConfigVariable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ConfigVariable)[ValueOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ConfigVariable.ValueOneofCase)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
