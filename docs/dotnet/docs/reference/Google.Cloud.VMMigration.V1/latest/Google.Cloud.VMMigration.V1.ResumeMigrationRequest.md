---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/Google.Cloud.VMMigration.V1.ResumeMigrationRequest
title: VM Migration v1 API - Class ResumeMigrationRequest (2.9.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:17:22.621950+00:00
---

# VM Migration v1 API - Class ResumeMigrationRequest (2.9.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/Google.Cloud.VMMigration.V1.ResumeMigrationRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  VM Migration v1 API - Class ResumeMigrationRequest (2.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.9.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/Google.Cloud.VMMigration.V1.ResumeMigrationRequest)
  * [ 2.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/2.8.0/Google.Cloud.VMMigration.V1.ResumeMigrationRequest)
  * [ 2.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/2.7.0/Google.Cloud.VMMigration.V1.ResumeMigrationRequest)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/2.6.0/Google.Cloud.VMMigration.V1.ResumeMigrationRequest)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/2.5.0/Google.Cloud.VMMigration.V1.ResumeMigrationRequest)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/2.4.0/Google.Cloud.VMMigration.V1.ResumeMigrationRequest)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/2.3.0/Google.Cloud.VMMigration.V1.ResumeMigrationRequest)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/2.2.0/Google.Cloud.VMMigration.V1.ResumeMigrationRequest)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/2.1.0/Google.Cloud.VMMigration.V1.ResumeMigrationRequest)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/2.0.0/Google.Cloud.VMMigration.V1.ResumeMigrationRequest)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/1.0.0/Google.Cloud.VMMigration.V1.ResumeMigrationRequest)


    
    
    public sealed class ResumeMigrationRequest : IMessage<ResumeMigrationRequest>, IEquatable<ResumeMigrationRequest>, IDeepCloneable<ResumeMigrationRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the VM Migration v1 API class ResumeMigrationRequest.

Request message for 'ResumeMigration' request.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ResumeMigrationRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ResumeMigrationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/Google.Cloud.VMMigration.V1.ResumeMigrationRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ResumeMigrationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/Google.Cloud.VMMigration.V1.ResumeMigrationRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ResumeMigrationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/Google.Cloud.VMMigration.V1.ResumeMigrationRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.VMMigration.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/Google.Cloud.VMMigration.V1)

## Assembly

Google.Cloud.VMMigration.V1.dll

## Constructors 

### ResumeMigrationRequest()
    
    
    public ResumeMigrationRequest()

### ResumeMigrationRequest(ResumeMigrationRequest)
    
    
    public ResumeMigrationRequest(ResumeMigrationRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ResumeMigrationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/Google.Cloud.VMMigration.V1.ResumeMigrationRequest)`  
  
  
## Properties 

### MigratingVm
    
    
    public string MigratingVm { get; set; }

Required. The name of the MigratingVm.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### MigratingVmAsMigratingVmName
    
    
    public MigratingVmName MigratingVmAsMigratingVmName { get; set; }

[MigratingVmName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/Google.Cloud.VMMigration.V1.MigratingVmName)-typed view over the [MigratingVm](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/Google.Cloud.VMMigration.V1.ResumeMigrationRequest#Google_Cloud_VMMigration_V1_ResumeMigrationRequest_MigratingVm) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[MigratingVmName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/Google.Cloud.VMMigration.V1.MigratingVmName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
