---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.Document.Types.Entity
title: Cloud Document AI v1beta3 API - Class Document.Types.Entity (2.0.0-beta30) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:49:46.235395+00:00
---

# Cloud Document AI v1beta3 API - Class Document.Types.Entity (2.0.0-beta30)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.Document.Types.Entity

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Document AI v1beta3 API - Class Document.Types.Entity (2.0.0-beta30) Stay organized with collections  Save and categorize content based on your preferences. 

2.0.0-beta30 (latest)  2.0.0-beta29  1.0.0-beta04 
    
    
    public sealed class Document.Types.Entity : IMessage<Document.Types.Entity>, IEquatable<Document.Types.Entity>, IDeepCloneable<Document.Types.Entity>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Document AI v1beta3 API class Document.Types.Entity.

An entity that could be a phrase in the text or a property that belongs to the document. It is a known entity type, such as a person, an organization, or location.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Document.Types.Entity

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.Document)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.Document.Types)[Entity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.Document.Types.Entity), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.Document)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.Document.Types)[Entity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.Document.Types.Entity), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.Document)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.Document.Types)[Entity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.Document.Types.Entity), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DocumentAI.V1Beta3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3)

## Assembly

Google.Cloud.DocumentAI.V1Beta3.dll

## Constructors 

### Entity()
    
    
    public Entity()

### Entity(Entity)
    
    
    public Entity(Document.Types.Entity other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.Document)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.Document.Types)[Entity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.Document.Types.Entity)`  
  
  
## Properties 

### Confidence
    
    
    public float Confidence { get; set; }

Optional. Confidence of detected Schema entity. Range `[0, 1]`.

**Property Value**  
---  
**Type** | **Description**  
`[float](https://learn.microsoft.com/dotnet/api/system.single)` |   
  
### Id
    
    
    public string Id { get; set; }

Optional. Canonical id. This will be a unique value in the entity list for this document.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### MentionId
    
    
    public string MentionId { get; set; }

Optional. Deprecated. Use `id` field instead.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### MentionText
    
    
    public string MentionText { get; set; }

Optional. Text value of the entity, for example, `1600 Amphitheatre Pkwy`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Method
    
    
    public Document.Types.Entity.Types.Method Method { get; set; }

Optional. Specifies how the entity's value is obtained.

**Property Value**  
---  
**Type** | **Description**  
`[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.Document)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.Document.Types)[Entity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.Document.Types.Entity)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.Document.Types.Entity.Types)[Method](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.Document.Types.Entity.Types.Method)` |   
  
### NormalizedValue
    
    
    public Document.Types.Entity.Types.NormalizedValue NormalizedValue { get; set; }

Optional. Normalized entity value. Absent if the extracted value could not be converted or the type (for example, address) is not supported for certain parsers. This field is also only populated for certain supported document types.

**Property Value**  
---  
**Type** | **Description**  
`[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.Document)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.Document.Types)[Entity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.Document.Types.Entity)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.Document.Types.Entity.Types)[NormalizedValue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.Document.Types.Entity.Types.NormalizedValue)` |   
  
### PageAnchor
    
    
    public Document.Types.PageAnchor PageAnchor { get; set; }

Optional. Represents the provenance of this entity wrt. the location on the page where it was found.

**Property Value**  
---  
**Type** | **Description**  
`[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.Document)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.Document.Types)[PageAnchor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.Document.Types.PageAnchor)` |   
  
### Properties
    
    
    public RepeatedField<Document.Types.Entity> Properties { get; }

Optional. Entities can be nested to form a hierarchical data structure representing the content in the document.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.Document)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.Document.Types)[Entity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.Document.Types.Entity)` |   
  
### Provenance
    
    
    public Document.Types.Provenance Provenance { get; set; }

Optional. The history of this annotation.

**Property Value**  
---  
**Type** | **Description**  
`[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.Document)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.Document.Types)[Provenance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.Document.Types.Provenance)` |   
  
### Redacted
    
    
    public bool Redacted { get; set; }

Optional. Whether the entity will be redacted for de-identification purposes.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### TextAnchor
    
    
    public Document.Types.TextAnchor TextAnchor { get; set; }

Optional. Provenance of the entity. Text anchor indexing into the [Document.text][google.cloud.documentai.v1beta3.Document.text].

**Property Value**  
---  
**Type** | **Description**  
`[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.Document)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.Document.Types)[TextAnchor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.Document.Types.TextAnchor)` |   
  
### Type
    
    
    public string Type { get; set; }

Required. Entity type from a schema, for example, `Address`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-16 UTC."],[],[]] 
