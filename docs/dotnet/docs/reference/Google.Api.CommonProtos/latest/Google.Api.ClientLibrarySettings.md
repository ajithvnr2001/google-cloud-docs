---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ClientLibrarySettings
title: Class ClientLibrarySettings (2.17.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:43.505588+00:00
---

# Class ClientLibrarySettings (2.17.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ClientLibrarySettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Class ClientLibrarySettings (2.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.17.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ClientLibrarySettings)
  * [ 2.15.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.15.0/Google.Api.ClientLibrarySettings)
  * [ 2.10.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.10.0/Google.Api.ClientLibrarySettings)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.2.0/Google.Api.ClientLibrarySettings)


    
    
    public sealed class ClientLibrarySettings : IMessage<ClientLibrarySettings>, IEquatable<ClientLibrarySettings>, IDeepCloneable<ClientLibrarySettings>, IBufferMessage, IMessage

Details about how and where to publish client libraries.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ClientLibrarySettings

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ClientLibrarySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ClientLibrarySettings), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ClientLibrarySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ClientLibrarySettings), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ClientLibrarySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ClientLibrarySettings), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals\(system-object-system-object\))

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals)

## Namespace

[Google.Api](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api)

## Assembly

Google.Api.CommonProtos.dll

## Constructors 

### ClientLibrarySettings()
    
    
    public ClientLibrarySettings()

### ClientLibrarySettings(ClientLibrarySettings)
    
    
    public ClientLibrarySettings(ClientLibrarySettings other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ClientLibrarySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ClientLibrarySettings)`  
  
  
## Fields 

### CppSettingsFieldNumber
    
    
    public const int CppSettingsFieldNumber = 22

Field number for the "cpp_settings" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### DotnetSettingsFieldNumber
    
    
    public const int DotnetSettingsFieldNumber = 26

Field number for the "dotnet_settings" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### GoSettingsFieldNumber
    
    
    public const int GoSettingsFieldNumber = 28

Field number for the "go_settings" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### JavaSettingsFieldNumber
    
    
    public const int JavaSettingsFieldNumber = 21

Field number for the "java_settings" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### LaunchStageFieldNumber
    
    
    public const int LaunchStageFieldNumber = 2

Field number for the "launch_stage" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### NodeSettingsFieldNumber
    
    
    public const int NodeSettingsFieldNumber = 25

Field number for the "node_settings" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PhpSettingsFieldNumber
    
    
    public const int PhpSettingsFieldNumber = 23

Field number for the "php_settings" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PythonSettingsFieldNumber
    
    
    public const int PythonSettingsFieldNumber = 24

Field number for the "python_settings" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### RestNumericEnumsFieldNumber
    
    
    public const int RestNumericEnumsFieldNumber = 3

Field number for the "rest_numeric_enums" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### RubySettingsFieldNumber
    
    
    public const int RubySettingsFieldNumber = 27

Field number for the "ruby_settings" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### VersionFieldNumber
    
    
    public const int VersionFieldNumber = 1

Field number for the "version" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
## Properties 

### CppSettings
    
    
    public CppSettings CppSettings { get; set; }

Settings for C++ client libraries.

**Property Value**  
---  
**Type** | **Description**  
`[CppSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.CppSettings)` |   
  
### Descriptor
    
    
    public static MessageDescriptor Descriptor { get; }

**Property Value**  
---  
**Type** | **Description**  
`[MessageDescriptor](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Reflection.MessageDescriptor.html)` |   
  
### DotnetSettings
    
    
    public DotnetSettings DotnetSettings { get; set; }

Settings for .NET client libraries.

**Property Value**  
---  
**Type** | **Description**  
`[DotnetSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.DotnetSettings)` |   
  
### GoSettings
    
    
    public GoSettings GoSettings { get; set; }

Settings for Go client libraries.

**Property Value**  
---  
**Type** | **Description**  
`[GoSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.GoSettings)` |   
  
### JavaSettings
    
    
    public JavaSettings JavaSettings { get; set; }

Settings for legacy Java features, supported in the Service YAML.

**Property Value**  
---  
**Type** | **Description**  
`[JavaSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.JavaSettings)` |   
  
### LaunchStage
    
    
    public LaunchStage LaunchStage { get; set; }

Launch stage of this version of the API.

**Property Value**  
---  
**Type** | **Description**  
`[LaunchStage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.LaunchStage)` |   
  
### NodeSettings
    
    
    public NodeSettings NodeSettings { get; set; }

Settings for Node client libraries.

**Property Value**  
---  
**Type** | **Description**  
`[NodeSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.NodeSettings)` |   
  
### Parser
    
    
    public static MessageParser<ClientLibrarySettings> Parser { get; }

**Property Value**  
---  
**Type** | **Description**  
`[MessageParser](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.MessageParser-1.html)[ClientLibrarySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ClientLibrarySettings)` |   
  
### PhpSettings
    
    
    public PhpSettings PhpSettings { get; set; }

Settings for PHP client libraries.

**Property Value**  
---  
**Type** | **Description**  
`[PhpSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.PhpSettings)` |   
  
### PythonSettings
    
    
    public PythonSettings PythonSettings { get; set; }

Settings for Python client libraries.

**Property Value**  
---  
**Type** | **Description**  
`[PythonSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.PythonSettings)` |   
  
### RestNumericEnums
    
    
    public bool RestNumericEnums { get; set; }

When using transport=rest, the client request will encode enums as numbers rather than strings.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### RubySettings
    
    
    public RubySettings RubySettings { get; set; }

Settings for Ruby client libraries.

**Property Value**  
---  
**Type** | **Description**  
`[RubySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.RubySettings)` |   
  
### Version
    
    
    public string Version { get; set; }

Version of the API to apply these settings to. This is the full protobuf package for the API, ending in the version element. Examples: "google.cloud.speech.v1" and "google.spanner.admin.database.v1".

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
## Methods 

### CalculateSize()
    
    
    public int CalculateSize()

**Returns**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### Clone()
    
    
    public ClientLibrarySettings Clone()

**Returns**  
---  
**Type** | **Description**  
`[ClientLibrarySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ClientLibrarySettings)` |   
  
### Equals(ClientLibrarySettings)
    
    
    public bool Equals(ClientLibrarySettings other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ClientLibrarySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ClientLibrarySettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Equals(object)
    
    
    public override bool Equals(object other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[object](https://learn.microsoft.com/dotnet/api/system.object)`  
  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
**Overrides**

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals\(system-object\))

### GetHashCode()
    
    
    public override int GetHashCode()

**Returns**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
**Overrides**

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

### MergeFrom(ClientLibrarySettings)
    
    
    public void MergeFrom(ClientLibrarySettings other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ClientLibrarySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ClientLibrarySettings)`  
  
  
### MergeFrom(CodedInputStream)
    
    
    public void MergeFrom(CodedInputStream input)

**Parameter**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.CodedInputStream.html)`  
  
  
### ToString()
    
    
    public override string ToString()

**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Overrides**

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

### WriteTo(CodedOutputStream)
    
    
    public void WriteTo(CodedOutputStream output)

**Parameter**  
---  
**Name** | **Description**  
`output` | `[CodedOutputStream](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.CodedOutputStream.html)`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
