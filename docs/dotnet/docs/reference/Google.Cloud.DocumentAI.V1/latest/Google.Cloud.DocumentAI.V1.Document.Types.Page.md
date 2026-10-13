---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page
title: Cloud Document AI v1 API - Class Document.Types.Page (3.25.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:22:54.294814+00:00
---

# Cloud Document AI v1 API - Class Document.Types.Page (3.25.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Document AI v1 API - Class Document.Types.Page (3.25.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.25.0 (latest)  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.0.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class Document.Types.Page : IMessage<Document.Types.Page>, IEquatable<Document.Types.Page>, IDeepCloneable<Document.Types.Page>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Document AI v1 API class Document.Types.Page.

A page in a [Document][google.cloud.documentai.v1.Document].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Document.Types.Page

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types)[Page](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types)[Page](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types)[Page](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DocumentAI.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1)

## Assembly

Google.Cloud.DocumentAI.V1.dll

## Constructors 

### Page()
    
    
    public Page()

### Page(Page)
    
    
    public Page(Document.Types.Page other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types)[Page](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page)`  
  
  
## Properties 

### Blocks
    
    
    public RepeatedField<Document.Types.Page.Types.Block> Blocks { get; }

A list of visually detected text blocks on the page. A block has a set of lines (collected into paragraphs) that have a common line-spacing and orientation.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types)[Page](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types)[Block](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types.Block)` |   
  
### DetectedBarcodes
    
    
    public RepeatedField<Document.Types.Page.Types.DetectedBarcode> DetectedBarcodes { get; }

A list of detected barcodes.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types)[Page](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types)[DetectedBarcode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types.DetectedBarcode)` |   
  
### DetectedLanguages
    
    
    public RepeatedField<Document.Types.Page.Types.DetectedLanguage> DetectedLanguages { get; }

A list of detected languages together with confidence.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types)[Page](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types)[DetectedLanguage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types.DetectedLanguage)` |   
  
### Dimension
    
    
    public Document.Types.Page.Types.Dimension Dimension { get; set; }

Physical dimension of the page.

**Property Value**  
---  
**Type** | **Description**  
`[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types)[Page](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types)[Dimension](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types.Dimension)` |   
  
### FormFields
    
    
    public RepeatedField<Document.Types.Page.Types.FormField> FormFields { get; }

A list of visually detected form fields on the page.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types)[Page](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types)[FormField](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types.FormField)` |   
  
### Image
    
    
    public Document.Types.Page.Types.Image Image { get; set; }

Rendered image for this page. This image is preprocessed to remove any skew, rotation, and distortions such that the annotation bounding boxes can be upright and axis-aligned.

**Property Value**  
---  
**Type** | **Description**  
`[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types)[Page](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types)[Image](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types.Image)` |   
  
### ImageQualityScores
    
    
    public Document.Types.Page.Types.ImageQualityScores ImageQualityScores { get; set; }

Image quality scores.

**Property Value**  
---  
**Type** | **Description**  
`[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types)[Page](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types)[ImageQualityScores](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types.ImageQualityScores)` |   
  
### Layout
    
    
    public Document.Types.Page.Types.Layout Layout { get; set; }

[Layout][google.cloud.documentai.v1.Document.Page.Layout] for the page.

**Property Value**  
---  
**Type** | **Description**  
`[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types)[Page](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types)[Layout](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types.Layout)` |   
  
### Lines
    
    
    public RepeatedField<Document.Types.Page.Types.Line> Lines { get; }

A list of visually detected text lines on the page. A collection of tokens that a human would perceive as a line.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types)[Page](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types)[Line](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types.Line)` |   
  
### PageNumber
    
    
    public int PageNumber { get; set; }

1-based index for current [Page][google.cloud.documentai.v1.Document.Page] in a parent [Document][google.cloud.documentai.v1.Document]. Useful when a page is taken out of a [Document][google.cloud.documentai.v1.Document] for individual processing.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### Paragraphs
    
    
    public RepeatedField<Document.Types.Page.Types.Paragraph> Paragraphs { get; }

A list of visually detected text paragraphs on the page. A collection of lines that a human would perceive as a paragraph.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types)[Page](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types)[Paragraph](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types.Paragraph)` |   
  
### Provenance
    
    
    [Obsolete]
    public Document.Types.Provenance Provenance { get; set; }

The history of this page.

**Property Value**  
---  
**Type** | **Description**  
`[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types)[Provenance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Provenance)` |   
  
### Symbols
    
    
    public RepeatedField<Document.Types.Page.Types.Symbol> Symbols { get; }

A list of visually detected symbols on the page.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types)[Page](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types)[Symbol](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types.Symbol)` |   
  
### Tables
    
    
    public RepeatedField<Document.Types.Page.Types.Table> Tables { get; }

A list of visually detected tables on the page.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types)[Page](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types)[Table](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types.Table)` |   
  
### Tokens
    
    
    public RepeatedField<Document.Types.Page.Types.Token> Tokens { get; }

A list of visually detected tokens on the page.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types)[Page](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types)[Token](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types.Token)` |   
  
### Transforms
    
    
    public RepeatedField<Document.Types.Page.Types.Matrix> Transforms { get; }

Transformation matrices that were applied to the original document image to produce [Page.image][google.cloud.documentai.v1.Document.Page.image].

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types)[Page](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types)[Matrix](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types.Matrix)` |   
  
### VisualElements
    
    
    public RepeatedField<Document.Types.Page.Types.VisualElement> VisualElements { get; }

A list of detected non-text visual elements, for example, checkbox, signature etc. on the page.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types)[Page](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types)[VisualElement](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types.VisualElement)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-23 UTC."],[],[]] 
