---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.UploadedPythonPackage
title: Cloud Build v1 API - Class UploadedPythonPackage (2.21.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:32:27.336964+00:00
---

# Cloud Build v1 API - Class UploadedPythonPackage (2.21.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.UploadedPythonPackage

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Build v1 API - Class UploadedPythonPackage (2.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.21.0 (latest)  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class UploadedPythonPackage : IMessage<UploadedPythonPackage>, IEquatable<UploadedPythonPackage>, IDeepCloneable<UploadedPythonPackage>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Build v1 API class UploadedPythonPackage.

Artifact uploaded using the PythonPackage directive.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > UploadedPythonPackage

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[UploadedPythonPackage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.UploadedPythonPackage), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[UploadedPythonPackage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.UploadedPythonPackage), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[UploadedPythonPackage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.UploadedPythonPackage), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.CloudBuild.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1)

## Assembly

Google.Cloud.CloudBuild.V1.dll

## Constructors 

### UploadedPythonPackage()
    
    
    public UploadedPythonPackage()

### UploadedPythonPackage(UploadedPythonPackage)
    
    
    public UploadedPythonPackage(UploadedPythonPackage other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[UploadedPythonPackage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.UploadedPythonPackage)`  
  
  
## Properties 

### ArtifactRegistryPackage
    
    
    public string ArtifactRegistryPackage { get; set; }

Output only. Path to the artifact in Artifact Registry.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### FileHashes
    
    
    public FileHashes FileHashes { get; set; }

Hash types and values of the Python Artifact.

**Property Value**  
---  
**Type** | **Description**  
`[FileHashes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.FileHashes)` |   
  
### PushTiming
    
    
    public TimeSpan PushTiming { get; set; }

Output only. Stores timing information for pushing the specified artifact.

**Property Value**  
---  
**Type** | **Description**  
`[TimeSpan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.TimeSpan)` |   
  
### Uri
    
    
    public string Uri { get; set; }

URI of the uploaded artifact.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
