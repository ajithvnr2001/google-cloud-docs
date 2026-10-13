---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.ProcessRequest
title: Cloud Document AI v1beta3 API - Class ProcessRequest (2.0.0-beta30) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:22:49.379010+00:00
---

# Cloud Document AI v1beta3 API - Class ProcessRequest (2.0.0-beta30)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.ProcessRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Document AI v1beta3 API - Class ProcessRequest (2.0.0-beta30) Stay organized with collections  Save and categorize content based on your preferences. 

2.0.0-beta30 (latest)  2.0.0-beta29  1.0.0-beta04 
    
    
    public sealed class ProcessRequest : IMessage<ProcessRequest>, IEquatable<ProcessRequest>, IDeepCloneable<ProcessRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Document AI v1beta3 API class ProcessRequest.

Request message for the [ProcessDocument][google.cloud.documentai.v1beta3.DocumentProcessorService.ProcessDocument] method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ProcessRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ProcessRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.ProcessRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ProcessRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.ProcessRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ProcessRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.ProcessRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DocumentAI.V1Beta3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3)

## Assembly

Google.Cloud.DocumentAI.V1Beta3.dll

## Constructors 

### ProcessRequest()
    
    
    public ProcessRequest()

### ProcessRequest(ProcessRequest)
    
    
    public ProcessRequest(ProcessRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ProcessRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.ProcessRequest)`  
  
  
## Properties 

### Document
    
    
    [Obsolete]
    public Document Document { get; set; }

The document payload, the [content][google.cloud.documentai.v1beta3.Document.content] and [mime_type][google.cloud.documentai.v1beta3.Document.mime_type] fields must be set.

**Property Value**  
---  
**Type** | **Description**  
`[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.Document)` |   
  
### FieldMask
    
    
    public FieldMask FieldMask { get; set; }

Specifies which fields to include in the [ProcessResponse.document][google.cloud.documentai.v1beta3.ProcessResponse.document] output. Only supports top-level document and pages field, so it must be in the form of `{document_field_name}` or `pages.{page_field_name}`.

**Property Value**  
---  
**Type** | **Description**  
`[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)` |   
  
### GcsDocument
    
    
    public GcsDocument GcsDocument { get; set; }

A raw document on Google Cloud Storage.

**Property Value**  
---  
**Type** | **Description**  
`[GcsDocument](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.GcsDocument)` |   
  
### ImagelessMode
    
    
    public bool ImagelessMode { get; set; }

Optional. Option to remove images from the document.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### InlineDocument
    
    
    public Document InlineDocument { get; set; }

An inline document proto.

**Property Value**  
---  
**Type** | **Description**  
`[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.Document)` |   
  
### Labels
    
    
    public MapField<string, string> Labels { get; }

Optional. The labels with user-defined metadata for the request.

Label keys and values can be no longer than 63 characters (Unicode codepoints) and can only contain lowercase letters, numeric characters, underscores, and dashes. International characters are allowed. Label values are optional. Label keys must start with a letter.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. The resource name of the [Processor][google.cloud.documentai.v1beta3.Processor] or [ProcessorVersion][google.cloud.documentai.v1beta3.ProcessorVersion] to use for processing. If a [Processor][google.cloud.documentai.v1beta3.Processor] is specified, the server will use its [default version][google.cloud.documentai.v1beta3.Processor.default_processor_version]. Format: `projects/{project}/locations/{location}/processors/{processor}`, or `projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processorVersion}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ProcessOptions
    
    
    public ProcessOptions ProcessOptions { get; set; }

Inference-time options for the process API

**Property Value**  
---  
**Type** | **Description**  
`[ProcessOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.ProcessOptions)` |   
  
### RawDocument
    
    
    public RawDocument RawDocument { get; set; }

A raw document content (bytes).

**Property Value**  
---  
**Type** | **Description**  
`[RawDocument](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.RawDocument)` |   
  
### ResourceName
    
    
    public IResourceName ResourceName { get; set; }

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.ProcessRequest#Google_Cloud_DocumentAI_V1Beta3_ProcessRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html)` |   
  
### SkipHumanReview
    
    
    [Obsolete]
    public bool SkipHumanReview { get; set; }

Whether human review should be skipped for this request. Default to `false`.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### SourceCase
    
    
    public ProcessRequest.SourceOneofCase SourceCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[ProcessRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.ProcessRequest)[SourceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.ProcessRequest.SourceOneofCase)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-16 UTC."],[],[]] 
