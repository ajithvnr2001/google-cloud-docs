---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/latest/Google.Cloud.GkeBackup.V1.DeleteRestoreChannelRequest
title: Backup for GKE v1 API - Class DeleteRestoreChannelRequest (2.9.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:42:14.064041+00:00
---

# Backup for GKE v1 API - Class DeleteRestoreChannelRequest (2.9.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/latest/Google.Cloud.GkeBackup.V1.DeleteRestoreChannelRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Backup for GKE v1 API - Class DeleteRestoreChannelRequest (2.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.9.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/latest/Google.Cloud.GkeBackup.V1.DeleteRestoreChannelRequest)
  * [ 2.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/2.8.0/Google.Cloud.GkeBackup.V1.DeleteRestoreChannelRequest)
  * [ 2.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/2.7.0/Google.Cloud.GkeBackup.V1.DeleteRestoreChannelRequest)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/2.6.0/Google.Cloud.GkeBackup.V1.DeleteRestoreChannelRequest)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/2.5.0/Google.Cloud.GkeBackup.V1.DeleteRestoreChannelRequest)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/2.4.0/Google.Cloud.GkeBackup.V1.DeleteRestoreChannelRequest)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/2.3.0/Google.Cloud.GkeBackup.V1.DeleteRestoreChannelRequest)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/2.2.0/Google.Cloud.GkeBackup.V1.DeleteRestoreChannelRequest)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/2.1.0/Google.Cloud.GkeBackup.V1.DeleteRestoreChannelRequest)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/2.0.0/Google.Cloud.GkeBackup.V1.DeleteRestoreChannelRequest)
  * [ 1.0.0-beta01 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/1.0.0-beta01/Google.Cloud.GkeBackup.V1.DeleteRestoreChannelRequest)


    
    
    public sealed class DeleteRestoreChannelRequest : IMessage<DeleteRestoreChannelRequest>, IEquatable<DeleteRestoreChannelRequest>, IDeepCloneable<DeleteRestoreChannelRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Backup for GKE v1 API class DeleteRestoreChannelRequest.

Request message for DeleteRestoreChannel.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DeleteRestoreChannelRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[DeleteRestoreChannelRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/latest/Google.Cloud.GkeBackup.V1.DeleteRestoreChannelRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DeleteRestoreChannelRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/latest/Google.Cloud.GkeBackup.V1.DeleteRestoreChannelRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[DeleteRestoreChannelRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/latest/Google.Cloud.GkeBackup.V1.DeleteRestoreChannelRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.GkeBackup.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/latest/Google.Cloud.GkeBackup.V1)

## Assembly

Google.Cloud.GkeBackup.V1.dll

## Constructors 

### DeleteRestoreChannelRequest()
    
    
    public DeleteRestoreChannelRequest()

### DeleteRestoreChannelRequest(DeleteRestoreChannelRequest)
    
    
    public DeleteRestoreChannelRequest(DeleteRestoreChannelRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[DeleteRestoreChannelRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/latest/Google.Cloud.GkeBackup.V1.DeleteRestoreChannelRequest)`  
  
  
## Properties 

### Etag
    
    
    public string Etag { get; set; }

Optional. If provided, this value must match the current value of the target RestoreChannel's [etag][google.cloud.gkebackup.v1.RestoreChannel.etag] field or the request is rejected.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. Fully qualified RestoreChannel name. Format: `projects/*/locations/*/restoreChannels/*`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### RestoreChannelName
    
    
    public RestoreChannelName RestoreChannelName { get; set; }

[RestoreChannelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/latest/Google.Cloud.GkeBackup.V1.RestoreChannelName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/latest/Google.Cloud.GkeBackup.V1.DeleteRestoreChannelRequest#Google_Cloud_GkeBackup_V1_DeleteRestoreChannelRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[RestoreChannelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/latest/Google.Cloud.GkeBackup.V1.RestoreChannelName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
