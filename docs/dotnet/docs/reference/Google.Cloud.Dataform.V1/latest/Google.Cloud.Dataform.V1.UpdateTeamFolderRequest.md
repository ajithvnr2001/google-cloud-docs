---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.UpdateTeamFolderRequest
title: Dataform v1 API - Class UpdateTeamFolderRequest (1.2.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:40:16.776840+00:00
---

# Dataform v1 API - Class UpdateTeamFolderRequest (1.2.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.UpdateTeamFolderRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Dataform v1 API - Class UpdateTeamFolderRequest (1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.0 (latest)  1.1.0  1.0.0 
    
    
    public sealed class UpdateTeamFolderRequest : IMessage<UpdateTeamFolderRequest>, IEquatable<UpdateTeamFolderRequest>, IDeepCloneable<UpdateTeamFolderRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Dataform v1 API class UpdateTeamFolderRequest.

`UpdateTeamFolder` request message.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > UpdateTeamFolderRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[UpdateTeamFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.UpdateTeamFolderRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[UpdateTeamFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.UpdateTeamFolderRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[UpdateTeamFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.UpdateTeamFolderRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dataform.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1)

## Assembly

Google.Cloud.Dataform.V1.dll

## Constructors 

### UpdateTeamFolderRequest()
    
    
    public UpdateTeamFolderRequest()

### UpdateTeamFolderRequest(UpdateTeamFolderRequest)
    
    
    public UpdateTeamFolderRequest(UpdateTeamFolderRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[UpdateTeamFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.UpdateTeamFolderRequest)`  
  
  
## Properties 

### TeamFolder
    
    
    public TeamFolder TeamFolder { get; set; }

Required. The updated TeamFolder.

**Property Value**  
---  
**Type** | **Description**  
`[TeamFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.TeamFolder)` |   
  
### UpdateMask
    
    
    public FieldMask UpdateMask { get; set; }

Optional. Specifies the fields to be updated in the Folder. If left unset, all fields will be updated.

**Property Value**  
---  
**Type** | **Description**  
`[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
