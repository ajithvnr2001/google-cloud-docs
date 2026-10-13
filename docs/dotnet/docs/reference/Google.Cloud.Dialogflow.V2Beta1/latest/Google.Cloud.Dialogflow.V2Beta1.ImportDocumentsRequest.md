---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ImportDocumentsRequest
title: Google Cloud Dialogflow v2beta1 API - Class ImportDocumentsRequest (1.0.0-beta33) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:39:33.619359+00:00
---

# Google Cloud Dialogflow v2beta1 API - Class ImportDocumentsRequest (1.0.0-beta33)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ImportDocumentsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Dialogflow v2beta1 API - Class ImportDocumentsRequest (1.0.0-beta33) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta33 (latest)  1.0.0-beta32 
    
    
    public sealed class ImportDocumentsRequest : IMessage<ImportDocumentsRequest>, IEquatable<ImportDocumentsRequest>, IDeepCloneable<ImportDocumentsRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Dialogflow v2beta1 API class ImportDocumentsRequest.

Request message for [Documents.ImportDocuments][google.cloud.dialogflow.v2beta1.Documents.ImportDocuments].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ImportDocumentsRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ImportDocumentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ImportDocumentsRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ImportDocumentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ImportDocumentsRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ImportDocumentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ImportDocumentsRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dialogflow.V2Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1)

## Assembly

Google.Cloud.Dialogflow.V2Beta1.dll

## Constructors 

### ImportDocumentsRequest()
    
    
    public ImportDocumentsRequest()

### ImportDocumentsRequest(ImportDocumentsRequest)
    
    
    public ImportDocumentsRequest(ImportDocumentsRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ImportDocumentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ImportDocumentsRequest)`  
  
  
## Properties 

### DocumentTemplate
    
    
    public ImportDocumentTemplate DocumentTemplate { get; set; }

Required. Document template used for importing all the documents.

**Property Value**  
---  
**Type** | **Description**  
`[ImportDocumentTemplate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ImportDocumentTemplate)` |   
  
### GcsSource
    
    
    public GcsSources GcsSource { get; set; }

Optional. The Google Cloud Storage location for the documents. The path can include a wildcard.

These URIs may have the forms `gs://<bucket-name>/<object-name>`. `gs://<bucket-name>/<object-path>/*.<extension>`.

**Property Value**  
---  
**Type** | **Description**  
`[GcsSources](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GcsSources)` |   
  
### ImportGcsCustomMetadata
    
    
    public bool ImportGcsCustomMetadata { get; set; }

Whether to import custom metadata from Google Cloud Storage. Only valid when the document source is Google Cloud Storage URI.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The knowledge base to import documents into. Format: `projects/<Project ID>/locations/<Location ID>/knowledgeBases/<Knowledge Base ID>`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsKnowledgeBaseName
    
    
    public KnowledgeBaseName ParentAsKnowledgeBaseName { get; set; }

[KnowledgeBaseName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.KnowledgeBaseName)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ImportDocumentsRequest#Google_Cloud_Dialogflow_V2Beta1_ImportDocumentsRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[KnowledgeBaseName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.KnowledgeBaseName)` |   
  
### SourceCase
    
    
    public ImportDocumentsRequest.SourceOneofCase SourceCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[ImportDocumentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ImportDocumentsRequest)[SourceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ImportDocumentsRequest.SourceOneofCase)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
