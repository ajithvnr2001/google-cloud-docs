---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/latest/Google.Cloud.ServiceManagement.V1.ConfigFile
title: Service Management v1 API - Class ConfigFile (2.5.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:09:37.432972+00:00
---

# Service Management v1 API - Class ConfigFile (2.5.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/latest/Google.Cloud.ServiceManagement.V1.ConfigFile

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Service Management v1 API - Class ConfigFile (2.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.5.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/latest/Google.Cloud.ServiceManagement.V1.ConfigFile)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/2.4.0/Google.Cloud.ServiceManagement.V1.ConfigFile)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/2.3.0/Google.Cloud.ServiceManagement.V1.ConfigFile)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/2.2.0/Google.Cloud.ServiceManagement.V1.ConfigFile)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/2.1.0/Google.Cloud.ServiceManagement.V1.ConfigFile)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/2.0.0/Google.Cloud.ServiceManagement.V1.ConfigFile)
  * [ 1.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/1.5.0/Google.Cloud.ServiceManagement.V1.ConfigFile)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/1.4.0/Google.Cloud.ServiceManagement.V1.ConfigFile)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/1.3.0/Google.Cloud.ServiceManagement.V1.ConfigFile)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/1.2.0/Google.Cloud.ServiceManagement.V1.ConfigFile)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/1.1.0/Google.Cloud.ServiceManagement.V1.ConfigFile)


    
    
    public sealed class ConfigFile : IMessage<ConfigFile>, IEquatable<ConfigFile>, IDeepCloneable<ConfigFile>, IBufferMessage, IMessage

Reference documentation and code samples for the Service Management v1 API class ConfigFile.

Generic specification of a source configuration file

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ConfigFile

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ConfigFile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/latest/Google.Cloud.ServiceManagement.V1.ConfigFile), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ConfigFile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/latest/Google.Cloud.ServiceManagement.V1.ConfigFile), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ConfigFile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/latest/Google.Cloud.ServiceManagement.V1.ConfigFile), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ServiceManagement.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/latest/Google.Cloud.ServiceManagement.V1)

## Assembly

Google.Cloud.ServiceManagement.V1.dll

## Constructors 

### ConfigFile()
    
    
    public ConfigFile()

### ConfigFile(ConfigFile)
    
    
    public ConfigFile(ConfigFile other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ConfigFile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/latest/Google.Cloud.ServiceManagement.V1.ConfigFile)`  
  
  
## Properties 

### FileContents
    
    
    public ByteString FileContents { get; set; }

The bytes that constitute the file.

**Property Value**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)` |   
  
### FilePath
    
    
    public string FilePath { get; set; }

The file name of the configuration file (full or relative path).

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### FileType
    
    
    public ConfigFile.Types.FileType FileType { get; set; }

The type of configuration file this represents.

**Property Value**  
---  
**Type** | **Description**  
`[ConfigFile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/latest/Google.Cloud.ServiceManagement.V1.ConfigFile)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/latest/Google.Cloud.ServiceManagement.V1.ConfigFile.Types)[FileType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/latest/Google.Cloud.ServiceManagement.V1.ConfigFile.Types.FileType)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
