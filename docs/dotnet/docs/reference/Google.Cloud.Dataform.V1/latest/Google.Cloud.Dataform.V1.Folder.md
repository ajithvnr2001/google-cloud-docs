---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.Folder
title: Dataform v1 API - Class Folder (1.2.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:39:30.903651+00:00
---

# Dataform v1 API - Class Folder (1.2.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.Folder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Dataform v1 API - Class Folder (1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.0 (latest)  1.1.0  1.0.0 
    
    
    public sealed class Folder : IMessage<Folder>, IEquatable<Folder>, IDeepCloneable<Folder>, IBufferMessage, IMessage

Reference documentation and code samples for the Dataform v1 API class Folder.

Represents a Dataform Folder. This is a resource that is used to organize Files and other Folders and provide hierarchical access controls.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Folder

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.Folder), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.Folder), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.Folder), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dataform.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1)

## Assembly

Google.Cloud.Dataform.V1.dll

## Constructors 

### Folder()
    
    
    public Folder()

### Folder(Folder)
    
    
    public Folder(Folder other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.Folder)`  
  
  
## Properties 

### ContainingFolder
    
    
    public string ContainingFolder { get; set; }

Optional. The containing Folder resource name. This should take the format: projects/{project}/locations/{location}/folders/{folder}, projects/{project}/locations/{location}/teamFolders/{teamFolder}, or just "" if this is a root Folder. This field can only be updated through MoveFolder.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### CreateTime
    
    
    public Timestamp CreateTime { get; set; }

Output only. The timestamp of when the Folder was created.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### CreatorIamPrincipal
    
    
    public string CreatorIamPrincipal { get; set; }

Output only. The IAM principal identifier of the creator of the Folder.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DisplayName
    
    
    public string DisplayName { get; set; }

Required. The Folder's user-friendly name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### FolderName
    
    
    public FolderName FolderName { get; set; }

[FolderName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.FolderName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.Folder#Google_Cloud_Dataform_V1_Folder_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[FolderName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.FolderName)` |   
  
### HasCreatorIamPrincipal
    
    
    public bool HasCreatorIamPrincipal { get; }

Gets whether the "creator_iam_principal" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasInternalMetadata
    
    
    public bool HasInternalMetadata { get; }

Gets whether the "internal_metadata" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### InternalMetadata
    
    
    public string InternalMetadata { get; set; }

Output only. All the metadata information that is used internally to serve the resource. For example: timestamps, flags, status fields, etc. The format of this field is a JSON string.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Identifier. The Folder's name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### TeamFolderName
    
    
    public string TeamFolderName { get; set; }

Output only. The resource name of the TeamFolder that this Folder is associated with. This should take the format: projects/{project}/locations/{location}/teamFolders/{teamFolder}. If this is not set, the Folder is not associated with a TeamFolder and is a UserFolder.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### UpdateTime
    
    
    public Timestamp UpdateTime { get; set; }

Output only. The timestamp of when the Folder was last updated.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
