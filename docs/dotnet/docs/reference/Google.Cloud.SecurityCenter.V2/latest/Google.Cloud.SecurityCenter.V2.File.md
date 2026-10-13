---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.File
title: Security Command Center v2 API - Class File (1.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:41:54.162345+00:00
---

# Security Command Center v2 API - Class File (1.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.File

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Security Command Center v2 API - Class File (1.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.6.0 (latest)  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class File : IMessage<File>, IEquatable<File>, IDeepCloneable<File>, IBufferMessage, IMessage

Reference documentation and code samples for the Security Command Center v2 API class File.

File information about the related binary/library used by an executable, or the script used by a script interpreter

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > File

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[File](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.File), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[File](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.File), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[File](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.File), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.SecurityCenter.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2)

## Assembly

Google.Cloud.SecurityCenter.V2.dll

## Constructors 

### File()
    
    
    public File()

### File(File)
    
    
    public File(File other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[File](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.File)`  
  
  
## Properties 

### Contents
    
    
    public string Contents { get; set; }

Prefix of the file contents as a JSON-encoded string.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DiskPath
    
    
    public File.Types.DiskPath DiskPath { get; set; }

Path of the file in terms of underlying disk/partition identifiers.

**Property Value**  
---  
**Type** | **Description**  
`[File](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.File)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.File.Types)[DiskPath](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.File.Types.DiskPath)` |   
  
### HashedSize
    
    
    public long HashedSize { get; set; }

The length in bytes of the file prefix that was hashed. If hashed_size == size, any hashes reported represent the entire file.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### Operations
    
    
    public RepeatedField<File.Types.FileOperation> Operations { get; }

Operation(s) performed on a file.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[File](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.File)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.File.Types)[FileOperation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.File.Types.FileOperation)` |   
  
### PartiallyHashed
    
    
    public bool PartiallyHashed { get; set; }

True when the hash covers only a prefix of the file.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Path
    
    
    public string Path { get; set; }

Absolute path of the file as a JSON encoded string.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Sha256
    
    
    public string Sha256 { get; set; }

SHA256 hash of the first hashed_size bytes of the file encoded as a hex string. If hashed_size == size, sha256 represents the SHA256 hash of the entire file.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Size
    
    
    public long Size { get; set; }

Size of the file in bytes.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
