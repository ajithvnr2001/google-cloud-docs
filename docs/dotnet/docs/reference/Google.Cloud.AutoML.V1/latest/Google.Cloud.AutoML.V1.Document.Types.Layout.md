---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.Document.Types.Layout
title: Google AutoML v1 API - Class Document.Types.Layout (3.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:15:00.804948+00:00
---

# Google AutoML v1 API - Class Document.Types.Layout (3.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.Document.Types.Layout

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google AutoML v1 API - Class Document.Types.Layout (3.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.6.0 (latest)  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class Document.Types.Layout : IMessage<Document.Types.Layout>, IEquatable<Document.Types.Layout>, IDeepCloneable<Document.Types.Layout>, IBufferMessage, IMessage

Reference documentation and code samples for the Google AutoML v1 API class Document.Types.Layout.

Describes the layout information of a [text_segment][google.cloud.automl.v1.Document.Layout.text_segment] in the document.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Document.Types.Layout

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.Document)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.Document.Types)[Layout](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.Document.Types.Layout), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.Document)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.Document.Types)[Layout](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.Document.Types.Layout), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.Document)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.Document.Types)[Layout](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.Document.Types.Layout), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AutoML.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1)

## Assembly

Google.Cloud.AutoML.V1.dll

## Constructors 

### Layout()
    
    
    public Layout()

### Layout(Layout)
    
    
    public Layout(Document.Types.Layout other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.Document)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.Document.Types)[Layout](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.Document.Types.Layout)`  
  
  
## Properties 

### BoundingPoly
    
    
    public BoundingPoly BoundingPoly { get; set; }

The position of the [text_segment][google.cloud.automl.v1.Document.Layout.text_segment] in the page. Contains exactly 4 [normalized_vertices][google.cloud.automl.v1p1beta.BoundingPoly.normalized_vertices] and they are connected by edges in the order provided, which will represent a rectangle parallel to the frame. The [NormalizedVertex-s][google.cloud.automl.v1p1beta.NormalizedVertex] are relative to the page. Coordinates are based on top-left as point (0,0).

**Property Value**  
---  
**Type** | **Description**  
`[BoundingPoly](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.BoundingPoly)` |   
  
### PageNumber
    
    
    public int PageNumber { get; set; }

Page number of the [text_segment][google.cloud.automl.v1.Document.Layout.text_segment] in the original document, starts from 1.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### TextSegment
    
    
    public TextSegment TextSegment { get; set; }

Text Segment that represents a segment in [document_text][google.cloud.automl.v1p1beta.Document.document_text].

**Property Value**  
---  
**Type** | **Description**  
`[TextSegment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.TextSegment)` |   
  
### TextSegmentType
    
    
    public Document.Types.Layout.Types.TextSegmentType TextSegmentType { get; set; }

The type of the [text_segment][google.cloud.automl.v1.Document.Layout.text_segment] in document.

**Property Value**  
---  
**Type** | **Description**  
`[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.Document)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.Document.Types)[Layout](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.Document.Types.Layout)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.Document.Types.Layout.Types)[TextSegmentType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.Document.Types.Layout.Types.TextSegmentType)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
