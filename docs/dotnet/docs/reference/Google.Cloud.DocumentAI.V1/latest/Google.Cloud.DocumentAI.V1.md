---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1
title: Cloud Document AI v1 API - Namespace Google.Cloud.DocumentAI.V1 (3.25.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:58:28.120545+00:00
---

# Cloud Document AI v1 API - Namespace Google.Cloud.DocumentAI.V1 (3.25.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Document AI v1 API - Namespace Google.Cloud.DocumentAI.V1 (3.25.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.25.0 (latest)  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.0.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 

## Classes 

### [Barcode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Barcode)

Encodes the detailed information of a barcode.

### [BatchDocumentsInputConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.BatchDocumentsInputConfig)

The common config to specify a set of documents used as input.

### [BatchProcessMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.BatchProcessMetadata)

The long-running operation metadata for [BatchProcessDocuments][google.cloud.documentai.v1.DocumentProcessorService.BatchProcessDocuments].

### [BatchProcessMetadata.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.BatchProcessMetadata.Types)

Container for nested types declared in the BatchProcessMetadata message type.

### [BatchProcessMetadata.Types.IndividualProcessStatus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.BatchProcessMetadata.Types.IndividualProcessStatus)

The status of a each individual document in the batch process.

### [BatchProcessRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.BatchProcessRequest)

Request message for [BatchProcessDocuments][google.cloud.documentai.v1.DocumentProcessorService.BatchProcessDocuments].

### [BatchProcessResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.BatchProcessResponse)

Response message for [BatchProcessDocuments][google.cloud.documentai.v1.DocumentProcessorService.BatchProcessDocuments].

### [BoundingPoly](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.BoundingPoly)

A bounding polygon for the detected image annotation.

### [CommonOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.CommonOperationMetadata)

The common metadata for long running operations.

### [CommonOperationMetadata.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.CommonOperationMetadata.Types)

Container for nested types declared in the CommonOperationMetadata message type.

### [CreateProcessorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.CreateProcessorRequest)

Request message for the [CreateProcessor][google.cloud.documentai.v1.DocumentProcessorService.CreateProcessor] method. Notice this request is sent to a regionalized backend service. If the [ProcessorType][google.cloud.documentai.v1.ProcessorType] isn't available in that region, the creation fails.

### [DeleteProcessorMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DeleteProcessorMetadata)

The long-running operation metadata for the [DeleteProcessor][google.cloud.documentai.v1.DocumentProcessorService.DeleteProcessor] method.

### [DeleteProcessorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DeleteProcessorRequest)

Request message for the [DeleteProcessor][google.cloud.documentai.v1.DocumentProcessorService.DeleteProcessor] method.

### [DeleteProcessorVersionMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DeleteProcessorVersionMetadata)

The long-running operation metadata for the [DeleteProcessorVersion][google.cloud.documentai.v1.DocumentProcessorService.DeleteProcessorVersion] method.

### [DeleteProcessorVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DeleteProcessorVersionRequest)

Request message for the [DeleteProcessorVersion][google.cloud.documentai.v1.DocumentProcessorService.DeleteProcessorVersion] method.

### [DeployProcessorVersionMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DeployProcessorVersionMetadata)

The long-running operation metadata for the [DeployProcessorVersion][google.cloud.documentai.v1.DocumentProcessorService.DeployProcessorVersion] method.

### [DeployProcessorVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DeployProcessorVersionRequest)

Request message for the [DeployProcessorVersion][google.cloud.documentai.v1.DocumentProcessorService.DeployProcessorVersion] method.

### [DeployProcessorVersionResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DeployProcessorVersionResponse)

Response message for the [DeployProcessorVersion][google.cloud.documentai.v1.DocumentProcessorService.DeployProcessorVersion] method.

### [DisableProcessorMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DisableProcessorMetadata)

The long-running operation metadata for the [DisableProcessor][google.cloud.documentai.v1.DocumentProcessorService.DisableProcessor] method.

### [DisableProcessorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DisableProcessorRequest)

Request message for the [DisableProcessor][google.cloud.documentai.v1.DocumentProcessorService.DisableProcessor] method.

### [DisableProcessorResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DisableProcessorResponse)

Response message for the [DisableProcessor][google.cloud.documentai.v1.DocumentProcessorService.DisableProcessor] method. Intentionally empty proto for adding fields in future.

### [Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document)

Document represents the canonical document resource in Document AI. It is an interchange format that provides insights into documents and allows for collaboration between users and Document AI to iterate and optimize for quality.

### [Document.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types)

Container for nested types declared in the Document message type.

### [Document.Types.Annotations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Annotations)

Represents the annotation of a block or a chunk.

### [Document.Types.BlobAsset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.BlobAsset)

Represents a blob asset. It's used to store the content of the inline blob in this document, for example, image bytes, such that it can be referenced by other fields in the document via asset ID.

### [Document.Types.ChunkedDocument](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.ChunkedDocument)

Represents the chunks that the document is divided into.

### [Document.Types.ChunkedDocument.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.ChunkedDocument.Types)

Container for nested types declared in the ChunkedDocument message type.

### [Document.Types.ChunkedDocument.Types.Chunk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.ChunkedDocument.Types.Chunk)

Represents a chunk.

### [Document.Types.ChunkedDocument.Types.Chunk.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.ChunkedDocument.Types.Chunk.Types)

Container for nested types declared in the Chunk message type.

### [Document.Types.ChunkedDocument.Types.Chunk.Types.ChunkField](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.ChunkedDocument.Types.Chunk.Types.ChunkField)

The chunk field in the chunk. A chunk field could be one of the various types (for example, image, table) supported.

### [Document.Types.ChunkedDocument.Types.Chunk.Types.ChunkPageFooter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.ChunkedDocument.Types.Chunk.Types.ChunkPageFooter)

Represents the page footer associated with the chunk.

### [Document.Types.ChunkedDocument.Types.Chunk.Types.ChunkPageHeader](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.ChunkedDocument.Types.Chunk.Types.ChunkPageHeader)

Represents the page header associated with the chunk.

### [Document.Types.ChunkedDocument.Types.Chunk.Types.ChunkPageSpan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.ChunkedDocument.Types.Chunk.Types.ChunkPageSpan)

Represents where the chunk starts and ends in the document.

### [Document.Types.ChunkedDocument.Types.Chunk.Types.ImageChunkField](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.ChunkedDocument.Types.Chunk.Types.ImageChunkField)

The image chunk field in the chunk.

### [Document.Types.ChunkedDocument.Types.Chunk.Types.TableChunkField](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.ChunkedDocument.Types.Chunk.Types.TableChunkField)

The table chunk field in the chunk.

### [Document.Types.DocumentLayout](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.DocumentLayout)

Represents the parsed layout of a document as a collection of blocks that the document is divided into.

### [Document.Types.DocumentLayout.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.DocumentLayout.Types)

Container for nested types declared in the DocumentLayout message type.

### [Document.Types.DocumentLayout.Types.DocumentLayoutBlock](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.DocumentLayout.Types.DocumentLayoutBlock)

Represents a block. A block could be one of the various types (text, table, list) supported.

### [Document.Types.DocumentLayout.Types.DocumentLayoutBlock.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.DocumentLayout.Types.DocumentLayoutBlock.Types)

Container for nested types declared in the DocumentLayoutBlock message type.

### [Document.Types.DocumentLayout.Types.DocumentLayoutBlock.Types.LayoutImageBlock](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.DocumentLayout.Types.DocumentLayoutBlock.Types.LayoutImageBlock)

Represents an image type block.

### [Document.Types.DocumentLayout.Types.DocumentLayoutBlock.Types.LayoutListBlock](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.DocumentLayout.Types.DocumentLayoutBlock.Types.LayoutListBlock)

Represents a list type block.

### [Document.Types.DocumentLayout.Types.DocumentLayoutBlock.Types.LayoutListEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.DocumentLayout.Types.DocumentLayoutBlock.Types.LayoutListEntry)

Represents an entry in the list.

### [Document.Types.DocumentLayout.Types.DocumentLayoutBlock.Types.LayoutPageSpan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.DocumentLayout.Types.DocumentLayoutBlock.Types.LayoutPageSpan)

Represents where the block starts and ends in the document.

### [Document.Types.DocumentLayout.Types.DocumentLayoutBlock.Types.LayoutTableBlock](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.DocumentLayout.Types.DocumentLayoutBlock.Types.LayoutTableBlock)

Represents a table type block.

### [Document.Types.DocumentLayout.Types.DocumentLayoutBlock.Types.LayoutTableCell](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.DocumentLayout.Types.DocumentLayoutBlock.Types.LayoutTableCell)

Represents a cell in a table row.

### [Document.Types.DocumentLayout.Types.DocumentLayoutBlock.Types.LayoutTableRow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.DocumentLayout.Types.DocumentLayoutBlock.Types.LayoutTableRow)

Represents a row in a table.

### [Document.Types.DocumentLayout.Types.DocumentLayoutBlock.Types.LayoutTextBlock](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.DocumentLayout.Types.DocumentLayoutBlock.Types.LayoutTextBlock)

Represents a text type block.

### [Document.Types.EntitiesRevision](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.EntitiesRevision)

Entity revision.

### [Document.Types.Entity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Entity)

An entity that could be a phrase in the text or a property that belongs to the document. It is a known entity type, such as a person, an organization, or location.

### [Document.Types.Entity.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Entity.Types)

Container for nested types declared in the Entity message type.

### [Document.Types.Entity.Types.NormalizedValue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Entity.Types.NormalizedValue)

Parsed and normalized entity value.

### [Document.Types.EntityRelation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.EntityRelation)

Relationship between [Entities][google.cloud.documentai.v1.Document.Entity].

### [Document.Types.EntityValidationOutput](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.EntityValidationOutput)

The output of the validation given the document and the validation rules.

### [Document.Types.EntityValidationOutput.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.EntityValidationOutput.Types)

Container for nested types declared in the EntityValidationOutput message type.

### [Document.Types.EntityValidationOutput.Types.ValidationResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.EntityValidationOutput.Types.ValidationResult)

Validation result for a single validation rule.

### [Document.Types.EntityValidationOutput.Types.ValidationResult.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.EntityValidationOutput.Types.ValidationResult.Types)

Container for nested types declared in the ValidationResult message type.

### [Document.Types.Page](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page)

A page in a [Document][google.cloud.documentai.v1.Document].

### [Document.Types.Page.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types)

Container for nested types declared in the Page message type.

### [Document.Types.Page.Types.Block](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types.Block)

A block has a set of lines (collected into paragraphs) that have a common line-spacing and orientation.

### [Document.Types.Page.Types.DetectedBarcode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types.DetectedBarcode)

A detected barcode.

### [Document.Types.Page.Types.DetectedLanguage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types.DetectedLanguage)

Detected language for a structural component.

### [Document.Types.Page.Types.Dimension](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types.Dimension)

Dimension for the page.

### [Document.Types.Page.Types.FormField](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types.FormField)

A form field detected on the page.

### [Document.Types.Page.Types.Image](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types.Image)

Rendered image contents for this page.

### [Document.Types.Page.Types.ImageQualityScores](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types.ImageQualityScores)

Image quality scores for the page image.

### [Document.Types.Page.Types.ImageQualityScores.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types.ImageQualityScores.Types)

Container for nested types declared in the ImageQualityScores message type.

### [Document.Types.Page.Types.ImageQualityScores.Types.DetectedDefect](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types.ImageQualityScores.Types.DetectedDefect)

Image Quality Defects

### [Document.Types.Page.Types.Layout](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types.Layout)

Visual element describing a layout unit on a page.

### [Document.Types.Page.Types.Layout.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types.Layout.Types)

Container for nested types declared in the Layout message type.

### [Document.Types.Page.Types.Line](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types.Line)

A collection of tokens that a human would perceive as a line. Does not cross column boundaries, can be horizontal, vertical, etc.

### [Document.Types.Page.Types.Matrix](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types.Matrix)

Representation for transformation matrix, intended to be compatible and used with OpenCV format for image manipulation.

### [Document.Types.Page.Types.Paragraph](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types.Paragraph)

A collection of lines that a human would perceive as a paragraph.

### [Document.Types.Page.Types.Symbol](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types.Symbol)

A detected symbol.

### [Document.Types.Page.Types.Table](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types.Table)

A table representation similar to HTML table structure.

### [Document.Types.Page.Types.Table.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types.Table.Types)

Container for nested types declared in the Table message type.

### [Document.Types.Page.Types.Table.Types.TableCell](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types.Table.Types.TableCell)

A cell representation inside the table.

### [Document.Types.Page.Types.Table.Types.TableRow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types.Table.Types.TableRow)

A row of table cells.

### [Document.Types.Page.Types.Token](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types.Token)

A detected token.

### [Document.Types.Page.Types.Token.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types.Token.Types)

Container for nested types declared in the Token message type.

### [Document.Types.Page.Types.Token.Types.DetectedBreak](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types.Token.Types.DetectedBreak)

Detected break at the end of a [Token][google.cloud.documentai.v1.Document.Page.Token].

### [Document.Types.Page.Types.Token.Types.DetectedBreak.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types.Token.Types.DetectedBreak.Types)

Container for nested types declared in the DetectedBreak message type.

### [Document.Types.Page.Types.Token.Types.StyleInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types.Token.Types.StyleInfo)

Font and other text style attributes.

### [Document.Types.Page.Types.VisualElement](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types.VisualElement)

Detected non-text visual elements, for example, checkbox, signature etc. on the page.

### [Document.Types.PageAnchor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.PageAnchor)

Referencing the visual context of the entity in the [Document.pages][google.cloud.documentai.v1.Document.pages]. Page anchors can be cross-page, consist of multiple bounding polygons and optionally reference specific layout element types.

### [Document.Types.PageAnchor.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.PageAnchor.Types)

Container for nested types declared in the PageAnchor message type.

### [Document.Types.PageAnchor.Types.PageRef](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.PageAnchor.Types.PageRef)

Represents a weak reference to a page element within a document.

### [Document.Types.PageAnchor.Types.PageRef.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.PageAnchor.Types.PageRef.Types)

Container for nested types declared in the PageRef message type.

### [Document.Types.Provenance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Provenance)

Structure to identify provenance relationships between annotations in different revisions.

### [Document.Types.Provenance.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Provenance.Types)

Container for nested types declared in the Provenance message type.

### [Document.Types.Provenance.Types.Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Provenance.Types.Parent)

The parent element the current element is based on. Used for referencing/aligning, removal and replacement operations.

### [Document.Types.Revision](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Revision)

Contains past or forward revisions of this document.

### [Document.Types.Revision.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Revision.Types)

Container for nested types declared in the Revision message type.

### [Document.Types.Revision.Types.HumanReview](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Revision.Types.HumanReview)

Human Review information of the document.

### [Document.Types.ShardInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.ShardInfo)

For a large document, sharding may be performed to produce several document shards. Each document shard contains this field to detail which shard it is.

### [Document.Types.Style](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Style)

Annotation for common text style attributes. This adheres to CSS conventions as much as possible.

### [Document.Types.Style.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Style.Types)

Container for nested types declared in the Style message type.

### [Document.Types.Style.Types.FontSize](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Style.Types.FontSize)

Font size with unit.

### [Document.Types.TextAnchor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.TextAnchor)

Text reference indexing into the [Document.text][google.cloud.documentai.v1.Document.text].

### [Document.Types.TextAnchor.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.TextAnchor.Types)

Container for nested types declared in the TextAnchor message type.

### [Document.Types.TextAnchor.Types.TextSegment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.TextAnchor.Types.TextSegment)

A text segment in the [Document.text][google.cloud.documentai.v1.Document.text]. The indices may be out of bounds which indicate that the text extends into another document shard for large sharded documents. See [ShardInfo.text_offset][google.cloud.documentai.v1.Document.ShardInfo.text_offset]

### [Document.Types.TextChange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.TextChange)

This message is used for text changes aka. OCR corrections.

### [DocumentOutputConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentOutputConfig)

Config that controls the output of documents. All documents will be written as a JSON file.

### [DocumentOutputConfig.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentOutputConfig.Types)

Container for nested types declared in the DocumentOutputConfig message type.

### [DocumentOutputConfig.Types.GcsOutputConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentOutputConfig.Types.GcsOutputConfig)

The configuration used when outputting documents.

### [DocumentOutputConfig.Types.GcsOutputConfig.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentOutputConfig.Types.GcsOutputConfig.Types)

Container for nested types declared in the GcsOutputConfig message type.

### [DocumentOutputConfig.Types.GcsOutputConfig.Types.ShardingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentOutputConfig.Types.GcsOutputConfig.Types.ShardingConfig)

The sharding config for the output document.

### [DocumentProcessorService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentProcessorService)

Service to call Document AI to process documents according to the processor's definition. Processors are built using state-of-the-art Google AI such as natural language, computer vision, and translation to extract structured information from unstructured or semi-structured documents.

### [DocumentProcessorService.DocumentProcessorServiceBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentProcessorService.DocumentProcessorServiceBase)

Base class for server-side implementations of DocumentProcessorService

### [DocumentProcessorService.DocumentProcessorServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentProcessorService.DocumentProcessorServiceClient)

Client for DocumentProcessorService

### [DocumentProcessorServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentProcessorServiceClient)

DocumentProcessorService client wrapper, for convenient use.

### [DocumentProcessorServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentProcessorServiceClientBuilder)

Builder class for [DocumentProcessorServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentProcessorServiceClient) to provide simple configuration of credentials, endpoint etc.

### [DocumentProcessorServiceClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentProcessorServiceClientImpl)

DocumentProcessorService client wrapper implementation, for convenient use.

### [DocumentProcessorServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentProcessorServiceSettings)

Settings for [DocumentProcessorServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentProcessorServiceClient) instances.

### [DocumentSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentSchema)

The schema defines the output of the processed document by a processor.

### [DocumentSchema.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentSchema.Types)

Container for nested types declared in the DocumentSchema message type.

### [DocumentSchema.Types.EntityType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentSchema.Types.EntityType)

EntityType is the wrapper of a label of the corresponding model with detailed attributes and limitations for entity-based processors. Multiple types can also compose a dependency tree to represent nested types.

### [DocumentSchema.Types.EntityType.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentSchema.Types.EntityType.Types)

Container for nested types declared in the EntityType message type.

### [DocumentSchema.Types.EntityType.Types.EnumValues](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentSchema.Types.EntityType.Types.EnumValues)

Defines the a list of enum values.

### [DocumentSchema.Types.EntityType.Types.Property](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentSchema.Types.EntityType.Types.Property)

Defines properties that can be part of the entity type.

### [DocumentSchema.Types.EntityType.Types.Property.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentSchema.Types.EntityType.Types.Property.Types)

Container for nested types declared in the Property message type.

### [DocumentSchema.Types.Metadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentSchema.Types.Metadata)

Metadata for global schema behavior.

### [EnableProcessorMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.EnableProcessorMetadata)

The long-running operation metadata for the [EnableProcessor][google.cloud.documentai.v1.DocumentProcessorService.EnableProcessor] method.

### [EnableProcessorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.EnableProcessorRequest)

Request message for the [EnableProcessor][google.cloud.documentai.v1.DocumentProcessorService.EnableProcessor] method.

### [EnableProcessorResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.EnableProcessorResponse)

Response message for the [EnableProcessor][google.cloud.documentai.v1.DocumentProcessorService.EnableProcessor] method. Intentionally empty proto for adding fields in future.

### [EvaluateProcessorVersionMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.EvaluateProcessorVersionMetadata)

Metadata of the [EvaluateProcessorVersion][google.cloud.documentai.v1.DocumentProcessorService.EvaluateProcessorVersion] method.

### [EvaluateProcessorVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.EvaluateProcessorVersionRequest)

Evaluates the given [ProcessorVersion][google.cloud.documentai.v1.ProcessorVersion] against the supplied documents.

### [EvaluateProcessorVersionResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.EvaluateProcessorVersionResponse)

Response of the [EvaluateProcessorVersion][google.cloud.documentai.v1.DocumentProcessorService.EvaluateProcessorVersion] method.

### [Evaluation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Evaluation)

An evaluation of a ProcessorVersion's performance.

### [Evaluation.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Evaluation.Types)

Container for nested types declared in the Evaluation message type.

### [Evaluation.Types.ConfidenceLevelMetrics](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Evaluation.Types.ConfidenceLevelMetrics)

Evaluations metrics, at a specific confidence level.

### [Evaluation.Types.Counters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Evaluation.Types.Counters)

Evaluation counters for the documents that were used.

### [Evaluation.Types.Metrics](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Evaluation.Types.Metrics)

Evaluation metrics, either in aggregate or about a specific entity.

### [Evaluation.Types.MultiConfidenceMetrics](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Evaluation.Types.MultiConfidenceMetrics)

Metrics across multiple confidence levels.

### [Evaluation.Types.MultiConfidenceMetrics.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Evaluation.Types.MultiConfidenceMetrics.Types)

Container for nested types declared in the MultiConfidenceMetrics message type.

### [EvaluationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.EvaluationName)

Resource name for the `Evaluation` resource.

### [EvaluationReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.EvaluationReference)

Gives a short summary of an evaluation, and links to the evaluation itself.

### [FetchProcessorTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.FetchProcessorTypesRequest)

Request message for the [FetchProcessorTypes][google.cloud.documentai.v1.DocumentProcessorService.FetchProcessorTypes] method. Some processor types may require the project be added to an allowlist.

### [FetchProcessorTypesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.FetchProcessorTypesResponse)

Response message for the [FetchProcessorTypes][google.cloud.documentai.v1.DocumentProcessorService.FetchProcessorTypes] method.

### [GcsDocument](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.GcsDocument)

Specifies a document stored on Cloud Storage.

### [GcsDocuments](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.GcsDocuments)

Specifies a set of documents on Cloud Storage.

### [GcsPrefix](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.GcsPrefix)

Specifies all documents on Cloud Storage with a common prefix.

### [GetEvaluationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.GetEvaluationRequest)

Retrieves a specific Evaluation.

### [GetProcessorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.GetProcessorRequest)

Request message for the [GetProcessor][google.cloud.documentai.v1.DocumentProcessorService.GetProcessor] method.

### [GetProcessorTypeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.GetProcessorTypeRequest)

Request message for the [GetProcessorType][google.cloud.documentai.v1.DocumentProcessorService.GetProcessorType] method.

### [GetProcessorVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.GetProcessorVersionRequest)

Request message for the [GetProcessorVersion][google.cloud.documentai.v1.DocumentProcessorService.GetProcessorVersion] method.

### [HumanReviewConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.HumanReviewConfigName)

Resource name for the `HumanReviewConfig` resource.

### [HumanReviewStatus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.HumanReviewStatus)

The status of human review on a processed document.

### [HumanReviewStatus.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.HumanReviewStatus.Types)

Container for nested types declared in the HumanReviewStatus message type.

### [ListEvaluationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ListEvaluationsRequest)

Retrieves a list of evaluations for a given [ProcessorVersion][google.cloud.documentai.v1.ProcessorVersion].

### [ListEvaluationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ListEvaluationsResponse)

The response from `ListEvaluations`.

### [ListProcessorTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ListProcessorTypesRequest)

Request message for the [ListProcessorTypes][google.cloud.documentai.v1.DocumentProcessorService.ListProcessorTypes] method. Some processor types may require the project be added to an allowlist.

### [ListProcessorTypesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ListProcessorTypesResponse)

Response message for the [ListProcessorTypes][google.cloud.documentai.v1.DocumentProcessorService.ListProcessorTypes] method.

### [ListProcessorVersionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ListProcessorVersionsRequest)

Request message for list all processor versions belongs to a processor.

### [ListProcessorVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ListProcessorVersionsResponse)

Response message for the [ListProcessorVersions][google.cloud.documentai.v1.DocumentProcessorService.ListProcessorVersions] method.

### [ListProcessorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ListProcessorsRequest)

Request message for list all processors belongs to a project.

### [ListProcessorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ListProcessorsResponse)

Response message for the [ListProcessors][google.cloud.documentai.v1.DocumentProcessorService.ListProcessors] method.

### [NormalizedVertex](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.NormalizedVertex)

A vertex represents a 2D point in the image. NOTE: the normalized vertex coordinates are relative to the original image and range from 0 to 1.

### [OcrConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.OcrConfig)

Config for Document OCR.

### [OcrConfig.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.OcrConfig.Types)

Container for nested types declared in the OcrConfig message type.

### [OcrConfig.Types.Hints](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.OcrConfig.Types.Hints)

Hints for OCR Engine

### [OcrConfig.Types.PremiumFeatures](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.OcrConfig.Types.PremiumFeatures)

Configurations for premium OCR features.

### [ProcessOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessOptions)

Options for Process API

### [ProcessOptions.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessOptions.Types)

Container for nested types declared in the ProcessOptions message type.

### [ProcessOptions.Types.IndividualPageSelector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessOptions.Types.IndividualPageSelector)

A list of individual page numbers.

### [ProcessOptions.Types.LayoutConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessOptions.Types.LayoutConfig)

Serving config for layout parser processor.

### [ProcessOptions.Types.LayoutConfig.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessOptions.Types.LayoutConfig.Types)

Container for nested types declared in the LayoutConfig message type.

### [ProcessOptions.Types.LayoutConfig.Types.ChunkingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessOptions.Types.LayoutConfig.Types.ChunkingConfig)

Serving config for chunking.

### [ProcessRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessRequest)

Request message for the [ProcessDocument][google.cloud.documentai.v1.DocumentProcessorService.ProcessDocument] method.

### [ProcessResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessResponse)

Response message for the [ProcessDocument][google.cloud.documentai.v1.DocumentProcessorService.ProcessDocument] method.

### [Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Processor)

The first-class citizen for Document AI. Each processor defines how to extract structural information from a document.

### [Processor.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Processor.Types)

Container for nested types declared in the Processor message type.

### [ProcessorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessorName)

Resource name for the `Processor` resource.

### [ProcessorType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessorType)

A processor type is responsible for performing a certain document understanding task on a certain type of document.

### [ProcessorType.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessorType.Types)

Container for nested types declared in the ProcessorType message type.

### [ProcessorType.Types.LocationInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessorType.Types.LocationInfo)

The location information about where the processor is available.

### [ProcessorTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessorTypeName)

Resource name for the `ProcessorType` resource.

### [ProcessorVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessorVersion)

A processor version is an implementation of a processor. Each processor can have multiple versions, pretrained by Google internally or uptrained by the customer. A processor can only have one default version at a time. Its document-processing behavior is defined by that version.

### [ProcessorVersion.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessorVersion.Types)

Container for nested types declared in the ProcessorVersion message type.

### [ProcessorVersion.Types.DeprecationInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessorVersion.Types.DeprecationInfo)

Information about the upcoming deprecation of this processor version.

### [ProcessorVersion.Types.GenAiModelInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessorVersion.Types.GenAiModelInfo)

Information about Generative AI model-based processor versions.

### [ProcessorVersion.Types.GenAiModelInfo.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessorVersion.Types.GenAiModelInfo.Types)

Container for nested types declared in the GenAiModelInfo message type.

### [ProcessorVersion.Types.GenAiModelInfo.Types.CustomGenAiModelInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessorVersion.Types.GenAiModelInfo.Types.CustomGenAiModelInfo)

Information for a custom Generative AI model created by the user. These are created with `Create New Version` in either the `Call foundation model` or `Fine tuning` tabs.

### [ProcessorVersion.Types.GenAiModelInfo.Types.CustomGenAiModelInfo.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessorVersion.Types.GenAiModelInfo.Types.CustomGenAiModelInfo.Types)

Container for nested types declared in the CustomGenAiModelInfo message type.

### [ProcessorVersion.Types.GenAiModelInfo.Types.FoundationGenAiModelInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessorVersion.Types.GenAiModelInfo.Types.FoundationGenAiModelInfo)

Information for a pretrained Google-managed foundation model.

### [ProcessorVersionAlias](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessorVersionAlias)

Contains the alias and the aliased resource name of processor version.

### [ProcessorVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessorVersionName)

Resource name for the `ProcessorVersion` resource.

### [RawDocument](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.RawDocument)

Payload message of raw document content (bytes).

### [ReviewDocumentOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ReviewDocumentOperationMetadata)

The long-running operation metadata for the [ReviewDocument][google.cloud.documentai.v1.DocumentProcessorService.ReviewDocument] method.

### [ReviewDocumentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ReviewDocumentRequest)

Request message for the [ReviewDocument][google.cloud.documentai.v1.DocumentProcessorService.ReviewDocument] method.

### [ReviewDocumentRequest.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ReviewDocumentRequest.Types)

Container for nested types declared in the ReviewDocumentRequest message type.

### [ReviewDocumentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ReviewDocumentResponse)

Response message for the [ReviewDocument][google.cloud.documentai.v1.DocumentProcessorService.ReviewDocument] method.

### [ReviewDocumentResponse.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ReviewDocumentResponse.Types)

Container for nested types declared in the ReviewDocumentResponse message type.

### [SetDefaultProcessorVersionMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.SetDefaultProcessorVersionMetadata)

The long-running operation metadata for the [SetDefaultProcessorVersion][google.cloud.documentai.v1.DocumentProcessorService.SetDefaultProcessorVersion] method.

### [SetDefaultProcessorVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.SetDefaultProcessorVersionRequest)

Request message for the [SetDefaultProcessorVersion][google.cloud.documentai.v1.DocumentProcessorService.SetDefaultProcessorVersion] method.

### [SetDefaultProcessorVersionResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.SetDefaultProcessorVersionResponse)

Response message for the [SetDefaultProcessorVersion][google.cloud.documentai.v1.DocumentProcessorService.SetDefaultProcessorVersion] method.

### [TrainProcessorVersionMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.TrainProcessorVersionMetadata)

The metadata that represents a processor version being created.

### [TrainProcessorVersionMetadata.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.TrainProcessorVersionMetadata.Types)

Container for nested types declared in the TrainProcessorVersionMetadata message type.

### [TrainProcessorVersionMetadata.Types.DatasetValidation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.TrainProcessorVersionMetadata.Types.DatasetValidation)

The dataset validation information. This includes any and all errors with documents and the dataset.

### [TrainProcessorVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.TrainProcessorVersionRequest)

Request message for the [TrainProcessorVersion][google.cloud.documentai.v1.DocumentProcessorService.TrainProcessorVersion] method.

### [TrainProcessorVersionRequest.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.TrainProcessorVersionRequest.Types)

Container for nested types declared in the TrainProcessorVersionRequest message type.

### [TrainProcessorVersionRequest.Types.CustomDocumentExtractionOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.TrainProcessorVersionRequest.Types.CustomDocumentExtractionOptions)

Options to control the training of the Custom Document Extraction (CDE) Processor.

### [TrainProcessorVersionRequest.Types.CustomDocumentExtractionOptions.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.TrainProcessorVersionRequest.Types.CustomDocumentExtractionOptions.Types)

Container for nested types declared in the CustomDocumentExtractionOptions message type.

### [TrainProcessorVersionRequest.Types.FoundationModelTuningOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.TrainProcessorVersionRequest.Types.FoundationModelTuningOptions)

Options to control foundation model tuning of the processor.

### [TrainProcessorVersionRequest.Types.InputData](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.TrainProcessorVersionRequest.Types.InputData)

The input data used to train a new [ProcessorVersion][google.cloud.documentai.v1.ProcessorVersion].

### [TrainProcessorVersionResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.TrainProcessorVersionResponse)

The response for [TrainProcessorVersion][google.cloud.documentai.v1.DocumentProcessorService.TrainProcessorVersion].

### [UndeployProcessorVersionMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.UndeployProcessorVersionMetadata)

The long-running operation metadata for the [UndeployProcessorVersion][google.cloud.documentai.v1.DocumentProcessorService.UndeployProcessorVersion] method.

### [UndeployProcessorVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.UndeployProcessorVersionRequest)

Request message for the [UndeployProcessorVersion][google.cloud.documentai.v1.DocumentProcessorService.UndeployProcessorVersion] method.

### [UndeployProcessorVersionResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.UndeployProcessorVersionResponse)

Response message for the [UndeployProcessorVersion][google.cloud.documentai.v1.DocumentProcessorService.UndeployProcessorVersion] method.

### [Vertex](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Vertex)

A vertex represents a 2D point in the image. NOTE: the vertex coordinates are in the same scale as the original image.

## Enums 

### [BatchDocumentsInputConfig.SourceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.BatchDocumentsInputConfig.SourceOneofCase)

Enum of possible cases for the "source" oneof.

### [BatchProcessMetadata.Types.State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.BatchProcessMetadata.Types.State)

Possible states of the batch processing operation.

### [CommonOperationMetadata.Types.State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.CommonOperationMetadata.Types.State)

State of the longrunning operation.

### [Document.SourceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.SourceOneofCase)

Enum of possible cases for the "source" oneof.

### [Document.Types.ChunkedDocument.Types.Chunk.Types.ChunkField.FieldTypeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.ChunkedDocument.Types.Chunk.Types.ChunkField.FieldTypeOneofCase)

Enum of possible cases for the "field_type" oneof.

### [Document.Types.ChunkedDocument.Types.Chunk.Types.ImageChunkField.ImageSourceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.ChunkedDocument.Types.Chunk.Types.ImageChunkField.ImageSourceOneofCase)

Enum of possible cases for the "image_source" oneof.

### [Document.Types.DocumentLayout.Types.DocumentLayoutBlock.BlockOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.DocumentLayout.Types.DocumentLayoutBlock.BlockOneofCase)

Enum of possible cases for the "block" oneof.

### [Document.Types.DocumentLayout.Types.DocumentLayoutBlock.Types.LayoutImageBlock.ImageSourceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.DocumentLayout.Types.DocumentLayoutBlock.Types.LayoutImageBlock.ImageSourceOneofCase)

Enum of possible cases for the "image_source" oneof.

### [Document.Types.Entity.Types.Method](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Entity.Types.Method)

Specifies how the entity's value is obtained.

### [Document.Types.Entity.Types.NormalizedValue.StructuredValueOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Entity.Types.NormalizedValue.StructuredValueOneofCase)

Enum of possible cases for the "structured_value" oneof.

### [Document.Types.EntityValidationOutput.Types.ValidationResult.Types.ValidationResultType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.EntityValidationOutput.Types.ValidationResult.Types.ValidationResultType)

The result of the validation rule.

### [Document.Types.Page.Types.Layout.Types.Orientation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types.Layout.Types.Orientation)

Detected human reading orientation.

### [Document.Types.Page.Types.Token.Types.DetectedBreak.Types.Type](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Page.Types.Token.Types.DetectedBreak.Types.Type)

Enum to denote the type of break found.

### [Document.Types.PageAnchor.Types.PageRef.Types.LayoutType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.PageAnchor.Types.PageRef.Types.LayoutType)

The type of layout that is being referenced.

### [Document.Types.Provenance.Types.OperationType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Provenance.Types.OperationType)

If a processor or agent does an explicit operation on existing elements.

### [Document.Types.Revision.SourceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Document.Types.Revision.SourceOneofCase)

Enum of possible cases for the "source" oneof.

### [DocumentOutputConfig.DestinationOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentOutputConfig.DestinationOneofCase)

Enum of possible cases for the "destination" oneof.

### [DocumentSchema.Types.EntityType.Types.Property.Types.Method](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentSchema.Types.EntityType.Types.Property.Types.Method)

Specifies how the entity's value is obtained from the document.

### [DocumentSchema.Types.EntityType.Types.Property.Types.OccurrenceType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentSchema.Types.EntityType.Types.Property.Types.OccurrenceType)

Types of occurrences of the entity type in the document. This represents the number of instances, not mentions, of an entity. For example, a bank statement might only have one `account_number`, but this account number can be mentioned in several places on the document. In this case, the `account_number` is considered a `REQUIRED_ONCE` entity type. If, on the other hand, we expect a bank statement to contain the status of multiple different accounts for the customers, the occurrence type is set to `REQUIRED_MULTIPLE`.

### [DocumentSchema.Types.EntityType.ValueSourceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.DocumentSchema.Types.EntityType.ValueSourceOneofCase)

Enum of possible cases for the "value_source" oneof.

### [Evaluation.Types.MultiConfidenceMetrics.Types.MetricsType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Evaluation.Types.MultiConfidenceMetrics.Types.MetricsType)

A type that determines how metrics should be interpreted.

### [EvaluationName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.EvaluationName.ResourceNameType)

The possible contents of [EvaluationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.EvaluationName).

### [HumanReviewConfigName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.HumanReviewConfigName.ResourceNameType)

The possible contents of [HumanReviewConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.HumanReviewConfigName).

### [HumanReviewStatus.Types.State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.HumanReviewStatus.Types.State)

The final state of human review on a processed document.

### [ProcessOptions.PageRangeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessOptions.PageRangeOneofCase)

Enum of possible cases for the "page_range" oneof.

### [ProcessRequest.SourceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessRequest.SourceOneofCase)

Enum of possible cases for the "source" oneof.

### [Processor.Types.State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.Processor.Types.State)

The possible states of the processor.

### [ProcessorName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessorName.ResourceNameType)

The possible contents of [ProcessorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessorName).

### [ProcessorTypeName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessorTypeName.ResourceNameType)

The possible contents of [ProcessorTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessorTypeName).

### [ProcessorVersion.Types.GenAiModelInfo.ModelInfoOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessorVersion.Types.GenAiModelInfo.ModelInfoOneofCase)

Enum of possible cases for the "model_info" oneof.

### [ProcessorVersion.Types.GenAiModelInfo.Types.CustomGenAiModelInfo.Types.CustomModelType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessorVersion.Types.GenAiModelInfo.Types.CustomGenAiModelInfo.Types.CustomModelType)

The type of custom model created by the user.

### [ProcessorVersion.Types.ModelType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessorVersion.Types.ModelType)

The possible model types of the processor version.

### [ProcessorVersion.Types.State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessorVersion.Types.State)

The possible states of the processor version.

### [ProcessorVersionName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessorVersionName.ResourceNameType)

The possible contents of [ProcessorVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessorVersionName).

### [ReviewDocumentRequest.SourceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ReviewDocumentRequest.SourceOneofCase)

Enum of possible cases for the "source" oneof.

### [ReviewDocumentRequest.Types.Priority](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ReviewDocumentRequest.Types.Priority)

The priority level of the human review task.

### [ReviewDocumentResponse.Types.State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ReviewDocumentResponse.Types.State)

Possible states of the review operation.

### [TrainProcessorVersionRequest.ProcessorFlagsOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.TrainProcessorVersionRequest.ProcessorFlagsOneofCase)

Enum of possible cases for the "processor_flags" oneof.

### [TrainProcessorVersionRequest.Types.CustomDocumentExtractionOptions.Types.TrainingMethod](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.TrainProcessorVersionRequest.Types.CustomDocumentExtractionOptions.Types.TrainingMethod)

Training Method for CDE. `TRAINING_METHOD_UNSPECIFIED` will fall back to `MODEL_BASED`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-23 UTC."],[],[]] 
