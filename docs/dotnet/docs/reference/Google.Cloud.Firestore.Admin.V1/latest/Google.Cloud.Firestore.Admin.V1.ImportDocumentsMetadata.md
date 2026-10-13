---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.ImportDocumentsMetadata
title: Firestore Admin v1 API - Class ImportDocumentsMetadata (3.19.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:20:16.028942+00:00
---

# Firestore Admin v1 API - Class ImportDocumentsMetadata (3.19.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.ImportDocumentsMetadata

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Firestore Admin v1 API - Class ImportDocumentsMetadata (3.19.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.19.0 (latest)  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class ImportDocumentsMetadata : IMessage<ImportDocumentsMetadata>, IEquatable<ImportDocumentsMetadata>, IDeepCloneable<ImportDocumentsMetadata>, IBufferMessage, IMessage

Reference documentation and code samples for the Firestore Admin v1 API class ImportDocumentsMetadata.

Metadata for [google.longrunning.Operation][google.longrunning.Operation] results from [FirestoreAdmin.ImportDocuments][google.firestore.admin.v1.FirestoreAdmin.ImportDocuments].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ImportDocumentsMetadata

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ImportDocumentsMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.ImportDocumentsMetadata), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ImportDocumentsMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.ImportDocumentsMetadata), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ImportDocumentsMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.ImportDocumentsMetadata), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Firestore.Admin.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1)

## Assembly

Google.Cloud.Firestore.Admin.V1.dll

## Constructors 

### ImportDocumentsMetadata()
    
    
    public ImportDocumentsMetadata()

### ImportDocumentsMetadata(ImportDocumentsMetadata)
    
    
    public ImportDocumentsMetadata(ImportDocumentsMetadata other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ImportDocumentsMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.ImportDocumentsMetadata)`  
  
  
## Properties 

### CollectionIds
    
    
    public RepeatedField<string> CollectionIds { get; }

Which collection IDs are being imported.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### EndTime
    
    
    public Timestamp EndTime { get; set; }

The time this operation completed. Will be unset if operation still in progress.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### InputUriPrefix
    
    
    public string InputUriPrefix { get; set; }

The location of the documents being imported.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### NamespaceIds
    
    
    public RepeatedField<string> NamespaceIds { get; }

Which namespace IDs are being imported.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### OperationState
    
    
    public OperationState OperationState { get; set; }

The state of the import operation.

**Property Value**  
---  
**Type** | **Description**  
`[OperationState](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.OperationState)` |   
  
### ProgressBytes
    
    
    public Progress ProgressBytes { get; set; }

The progress, in bytes, of this operation.

**Property Value**  
---  
**Type** | **Description**  
`[Progress](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.Progress)` |   
  
### ProgressDocuments
    
    
    public Progress ProgressDocuments { get; set; }

The progress, in documents, of this operation.

**Property Value**  
---  
**Type** | **Description**  
`[Progress](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.Progress)` |   
  
### StartTime
    
    
    public Timestamp StartTime { get; set; }

The time this operation started.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-05 UTC."],[],[]] 
