---
url: https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document/
title: Document AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:00:17.290512+00:00
---

# Document AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI ](https://docs.cloud.google.com/document-ai/docs)
  * [ Reference ](https://docs.cloud.google.com/document-ai/docs/reference)



Send feedback 

#  Document Stay organized with collections  Save and categorize content based on your preferences. 

Document represents the canonical document resource in Document AI. It is an interchange format that provides insights into documents and allows for collaboration between users and Document AI to iterate and optimize for quality.

JSON representation  
---  
      
    
    {
      "docid": string,
      "mimeType": string,
      "text": string,
      "textStyles": [
        {
          object ([Style](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Style))
        }
      ],
      "pages": [
        {
          object ([Page](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Page))
        }
      ],
      "entities": [
        {
          object ([Entity](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Entity))
        }
      ],
      "entityRelations": [
        {
          object ([EntityRelation](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#EntityRelation))
        }
      ],
      "textChanges": [
        {
          object ([TextChange](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#TextChange))
        }
      ],
      "shardInfo": {
        object ([ShardInfo](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#ShardInfo))
      },
      "error": {
        object ([Status](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/Status))
      },
      "revisions": [
        {
          object ([Revision](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Revision))
        }
      ],
      "documentLayout": {
        object ([DocumentLayout](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#DocumentLayout))
      },
      "chunkedDocument": {
        object ([ChunkedDocument](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#ChunkedDocument))
      },
      "blobAssets": [
        {
          object ([BlobAsset](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#BlobAsset))
        }
      ],
      "entityValidationOutput": {
        object ([EntityValidationOutput](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#EntityValidationOutput))
      },
      "entitiesRevisions": [
        {
          object ([EntitiesRevision](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#EntitiesRevision))
        }
      ],
      "entitiesRevisionId": string,
    
      // Union field source can be only one of the following:
      "uri": string,
      "content": string
      // End of list of possible types for union field source.
    }  
  
Fields  
---  
`docid` |  `string` Optional. An internal identifier for document. Should be loggable (no PII).  
`mimeType` |  `string` An IANA published [media type (MIME type)](https://www.iana.org/assignments/media-types/media-types.xhtml).  
`text` |  `string` Optional. UTF-8 encoded text in reading order from the document.  
`textStyles[]  
**(deprecated)**` |  `object (`[Style](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Style)`)` This item is deprecated!Styles for the `[Document.text](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#FIELDS.text)`.  
`pages[]` |  `object (`[Page](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Page)`)` Visual page layout for the `[Document](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document)`.  
`entities[]` |  `object (`[Entity](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Entity)`)` A list of entities detected on `[Document.text](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#FIELDS.text)`. For document shards, entities in this list may cross shard boundaries.  
`entityRelations[]` |  `object (`[EntityRelation](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#EntityRelation)`)` Placeholder. Relationship among `[Document.entities](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#FIELDS.entities)`.  
`textChanges[]` |  `object (`[TextChange](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#TextChange)`)` Placeholder. A list of text corrections made to `[Document.text](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#FIELDS.text)`. This is usually used for annotating corrections to OCR mistakes. Text changes for a given revision may not overlap with each other.  
`shardInfo` |  `object (`[ShardInfo](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#ShardInfo)`)` Information about the sharding if this document is sharded part of a larger document. If the document is not sharded, this message is not specified.  
`error` |  `object (`[Status](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/Status)`)` Any error that occurred while processing this document.  
`revisions[]` |  `object (`[Revision](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Revision)`)` Placeholder. Revision history of this document.  
`documentLayout` |  `object (`[DocumentLayout](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#DocumentLayout)`)` Parsed layout of the document.  
`chunkedDocument` |  `object (`[ChunkedDocument](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#ChunkedDocument)`)` Document chunked based on chunking config.  
`blobAssets[]` |  `object (`[BlobAsset](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#BlobAsset)`)` Optional. The blob assets in this document. This is used to store the content of the inline blobs in this document, for example, image bytes, such that it can be referenced by other fields in the document via asset ID.  
`entityValidationOutput` |  `object (`[EntityValidationOutput](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#EntityValidationOutput)`)` The entity validation output for the document. This is the validation output for `document.entities` field.  
`entitiesRevisions[]` |  `object (`[EntitiesRevision](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#EntitiesRevision)`)` A list of entity revisions. The entity revisions are appended to the document in the processing order. This field can be used for comparing the entity extraction results at different stages of the processing.  
`entitiesRevisionId` |  `string` The entity revision ID that `document.entities` field is based on. If this field and `entitiesRevisions` are set, the entities in `document.entities` are the entities in the entity revision with this ID. The `document.entity_validation_output` field is the `entityValidationOutput` field in this entity revision.  
Union field `source`. Original source document from the user. `source` can be only one of the following:  
`uri` |  `string` Optional. Currently supports Google Cloud Storage URI of the form `gs://bucket_name/object_name`. Object versioning is not supported. For more information, refer to [Google Cloud Storage Request URIs](https://cloud.google.com/storage/docs/reference-uris).  
`content` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Optional. Inline document content, represented as a stream of bytes. Note: As with all `bytes` fields, protobuffers use a pure binary representation, whereas JSON representations use base64.A base64-encoded string.  
  
## Style

Annotation for common text style attributes. This adheres to CSS conventions as much as possible.

JSON representation  
---  
      
    
    {
      "textAnchor": {
        object ([TextAnchor](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#TextAnchor))
      },
      "color": {
        object ([Color](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/Color))
      },
      "backgroundColor": {
        object ([Color](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/Color))
      },
      "fontWeight": string,
      "textStyle": string,
      "textDecoration": string,
      "fontSize": {
        object ([FontSize](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#FontSize))
      },
      "fontFamily": string
    }  
  
Fields  
---  
`textAnchor` |  `object (`[TextAnchor](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#TextAnchor)`)` Text anchor indexing into the `[Document.text](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#FIELDS.text)`.  
`color` |  `object (`[Color](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/Color)`)` Text color.  
`backgroundColor` |  `object (`[Color](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/Color)`)` Text background color.  
`fontWeight` |  `string` [Font weight](https://www.w3schools.com/cssref/pr_font_weight.asp). Possible values are `normal`, `bold`, `bolder`, and `lighter`.  
`textStyle` |  `string` [Text style](https://www.w3schools.com/cssref/pr_font_font-style.asp). Possible values are `normal`, `italic`, and `oblique`.  
`textDecoration` |  `string` [Text decoration](https://www.w3schools.com/cssref/pr_text_text-decoration.asp). Follows CSS standard.   
`fontSize` |  `object (`[FontSize](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#FontSize)`)` Font size.  
`fontFamily` |  `string` Font family such as `Arial`, `Times New Roman`. <https://www.w3schools.com/cssref/pr_font_font-family.asp>  
  
## TextAnchor

Text reference indexing into the `[Document.text](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#FIELDS.text)`.

JSON representation  
---  
      
    
    {
      "textSegments": [
        {
          object ([TextSegment](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#TextSegment))
        }
      ],
      "content": string
    }  
  
Fields  
---  
`textSegments[]` |  `object (`[TextSegment](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#TextSegment)`)` The text segments from the `[Document.text](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#FIELDS.text)`.  
`content` |  `string` Contains the content of the text span so that users do not have to look it up in the textSegments. It is always populated for formFields.  
  
## TextSegment

A text segment in the `[Document.text](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#FIELDS.text)`. The indices may be out of bounds which indicate that the text extends into another document shard for large sharded documents. See `[ShardInfo.text_offset](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#ShardInfo.FIELDS.text_offset)`

JSON representation  
---  
      
    
    {
      "startIndex": string,
      "endIndex": string
    }  
  
Fields  
---  
`startIndex` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` `[TextSegment](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#TextSegment)` start UTF-8 char index in the `[Document.text](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#FIELDS.text)`.  
`endIndex` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` `[TextSegment](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#TextSegment)` half open end UTF-8 char index in the `[Document.text](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#FIELDS.text)`.  
  
## FontSize

Font size with unit.

JSON representation  
---  
      
    
    {
      "size": number,
      "unit": string
    }  
  
Fields  
---  
`size` |  `number` Font size for the text.  
`unit` |  `string` Unit for the font size. Follows CSS naming (such as `in`, `px`, and `pt`).  
  
## Page

A page in a `[Document](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document)`.

JSON representation  
---  
      
    
    {
      "pageNumber": integer,
      "image": {
        object ([Image](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Image))
      },
      "transforms": [
        {
          object ([Matrix](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Matrix))
        }
      ],
      "dimension": {
        object ([Dimension](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Dimension))
      },
      "layout": {
        object ([Layout](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Layout))
      },
      "detectedLanguages": [
        {
          object ([DetectedLanguage](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#DetectedLanguage))
        }
      ],
      "blocks": [
        {
          object ([Block](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Block))
        }
      ],
      "paragraphs": [
        {
          object ([Paragraph](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Paragraph))
        }
      ],
      "lines": [
        {
          object ([Line](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Line))
        }
      ],
      "tokens": [
        {
          object ([Token](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Token))
        }
      ],
      "visualElements": [
        {
          object ([VisualElement](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#VisualElement))
        }
      ],
      "tables": [
        {
          object ([Table](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Table))
        }
      ],
      "formFields": [
        {
          object ([FormField](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#FormField))
        }
      ],
      "symbols": [
        {
          object ([Symbol](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Symbol))
        }
      ],
      "detectedBarcodes": [
        {
          object ([DetectedBarcode](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#DetectedBarcode))
        }
      ],
      "imageQualityScores": {
        object ([ImageQualityScores](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#ImageQualityScores))
      },
      "provenance": {
        object ([Provenance](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Provenance))
      }
    }  
  
Fields  
---  
`pageNumber` |  `integer` 1-based index for current `[Page](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Page)` in a parent `[Document](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document)`. Useful when a page is taken out of a `[Document](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document)` for individual processing.  
`image` |  `object (`[Image](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Image)`)` Rendered image for this page. This image is preprocessed to remove any skew, rotation, and distortions such that the annotation bounding boxes can be upright and axis-aligned.  
`transforms[]` |  `object (`[Matrix](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Matrix)`)` Transformation matrices that were applied to the original document image to produce `[Page.image](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Page.FIELDS.image)`.  
`dimension` |  `object (`[Dimension](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Dimension)`)` Physical dimension of the page.  
`layout` |  `object (`[Layout](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Layout)`)` `[Layout](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Layout)` for the page.  
`detectedLanguages[]` |  `object (`[DetectedLanguage](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#DetectedLanguage)`)` A list of detected languages together with confidence.  
`blocks[]` |  `object (`[Block](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Block)`)` A list of visually detected text blocks on the page. A block has a set of lines (collected into paragraphs) that have a common line-spacing and orientation.  
`paragraphs[]` |  `object (`[Paragraph](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Paragraph)`)` A list of visually detected text paragraphs on the page. A collection of lines that a human would perceive as a paragraph.  
`lines[]` |  `object (`[Line](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Line)`)` A list of visually detected text lines on the page. A collection of tokens that a human would perceive as a line.  
`tokens[]` |  `object (`[Token](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Token)`)` A list of visually detected tokens on the page.  
`visualElements[]` |  `object (`[VisualElement](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#VisualElement)`)` A list of detected non-text visual elements, for example, checkbox, signature etc. on the page.  
`tables[]` |  `object (`[Table](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Table)`)` A list of visually detected tables on the page.  
`formFields[]` |  `object (`[FormField](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#FormField)`)` A list of visually detected form fields on the page.  
`symbols[]` |  `object (`[Symbol](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Symbol)`)` A list of visually detected symbols on the page.  
`detectedBarcodes[]` |  `object (`[DetectedBarcode](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#DetectedBarcode)`)` A list of detected barcodes.  
`imageQualityScores` |  `object (`[ImageQualityScores](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#ImageQualityScores)`)` Image quality scores.  
`provenance  
**(deprecated)**` |  `object (`[Provenance](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Provenance)`)` This item is deprecated!The history of this page.  
  
## Image

Rendered image contents for this page.

JSON representation  
---  
      
    
    {
      "content": string,
      "mimeType": string,
      "width": integer,
      "height": integer
    }  
  
Fields  
---  
`content` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Raw byte content of the image.A base64-encoded string.  
`mimeType` |  `string` Encoding [media type (MIME type)](https://www.iana.org/assignments/media-types/media-types.xhtml) for the image.  
`width` |  `integer` Width of the image in pixels.  
`height` |  `integer` Height of the image in pixels.  
  
## Matrix

Representation for transformation matrix, intended to be compatible and used with OpenCV format for image manipulation.

JSON representation  
---  
      
    
    {
      "rows": integer,
      "cols": integer,
      "type": integer,
      "data": string
    }  
  
Fields  
---  
`rows` |  `integer` Number of rows in the matrix.  
`cols` |  `integer` Number of columns in the matrix.  
`type` |  `integer` This encodes information about what data type the matrix uses. For example, 0 (CV_8U) is an unsigned 8-bit image. For the full list of OpenCV primitive data types, please refer to <https://docs.opencv.org/4.3.0/d1/d1b/group__core__hal__interface.html>  
`data` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` The matrix data.A base64-encoded string.  
  
## Dimension

Dimension for the page.

JSON representation  
---  
      
    
    {
      "width": number,
      "height": number,
      "unit": string
    }  
  
Fields  
---  
`width` |  `number` Page width.  
`height` |  `number` Page height.  
`unit` |  `string` Dimension unit.  
  
## Layout

Visual element describing a layout unit on a page.

JSON representation  
---  
      
    
    {
      "textAnchor": {
        object ([TextAnchor](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#TextAnchor))
      },
      "confidence": number,
      "boundingPoly": {
        object ([BoundingPoly](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#BoundingPoly))
      },
      "orientation": enum ([Orientation](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Orientation))
    }  
  
Fields  
---  
`textAnchor` |  `object (`[TextAnchor](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#TextAnchor)`)` Text anchor indexing into the `[Document.text](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#FIELDS.text)`.  
`confidence` |  `number` Confidence of the current `[Layout](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Layout)` within context of the object this layout is for. For example, confidence can be for a single token, a table, a visual element, etc. depending on context. Range `[0, 1]`.  
`boundingPoly` |  `object (`[BoundingPoly](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#BoundingPoly)`)` The bounding polygon for the `[Layout](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Layout)`.  
`orientation` |  `enum (`[Orientation](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Orientation)`)` Detected orientation for the `[Layout](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Layout)`.  
  
## BoundingPoly

A bounding polygon for the detected image annotation.

JSON representation  
---  
      
    
    {
      "vertices": [
        {
          object ([Vertex](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Vertex))
        }
      ],
      "normalizedVertices": [
        {
          object ([NormalizedVertex](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#NormalizedVertex))
        }
      ]
    }  
  
Fields  
---  
`vertices[]` |  `object (`[Vertex](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Vertex)`)` The bounding polygon vertices.  
`normalizedVertices[]` |  `object (`[NormalizedVertex](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#NormalizedVertex)`)` The bounding polygon normalized vertices.  
  
## Vertex

A vertex represents a 2D point in the image. NOTE: the vertex coordinates are in the same scale as the original image.

JSON representation  
---  
      
    
    {
      "x": integer,
      "y": integer
    }  
  
Fields  
---  
`x` |  `integer` X coordinate.  
`y` |  `integer` Y coordinate (starts from the top of the image).  
  
## NormalizedVertex

A vertex represents a 2D point in the image. NOTE: the normalized vertex coordinates are relative to the original image and range from 0 to 1.

JSON representation  
---  
      
    
    {
      "x": number,
      "y": number
    }  
  
Fields  
---  
`x` |  `number` X coordinate.  
`y` |  `number` Y coordinate (starts from the top of the image).  
  
## Orientation

Detected human reading orientation.

Enums  
---  
`ORIENTATION_UNSPECIFIED` | Unspecified orientation.  
`PAGE_UP` | Orientation is aligned with page up.  
`PAGE_RIGHT` | Orientation is aligned with page right. Turn the head 90 degrees clockwise from upright to read.  
`PAGE_DOWN` | Orientation is aligned with page down. Turn the head 180 degrees from upright to read.  
`PAGE_LEFT` | Orientation is aligned with page left. Turn the head 90 degrees counterclockwise from upright to read.  
  
## DetectedLanguage

Detected language for a structural component.

JSON representation  
---  
      
    
    {
      "languageCode": string,
      "confidence": number
    }  
  
Fields  
---  
`languageCode` |  `string` The [BCP-47 language code](https://www.unicode.org/reports/tr35/#Unicode_locale_identifier), such as `en-US` or `sr-Latn`.  
`confidence` |  `number` Confidence of detected language. Range `[0, 1]`.  
  
## Block

A block has a set of lines (collected into paragraphs) that have a common line-spacing and orientation.

JSON representation  
---  
      
    
    {
      "layout": {
        object ([Layout](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Layout))
      },
      "detectedLanguages": [
        {
          object ([DetectedLanguage](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#DetectedLanguage))
        }
      ],
      "provenance": {
        object ([Provenance](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Provenance))
      }
    }  
  
Fields  
---  
`layout` |  `object (`[Layout](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Layout)`)` `[Layout](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Layout)` for `[Block](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Block)`.  
`detectedLanguages[]` |  `object (`[DetectedLanguage](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#DetectedLanguage)`)` A list of detected languages together with confidence.  
`provenance  
**(deprecated)**` |  `object (`[Provenance](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Provenance)`)` This item is deprecated!The history of this annotation.  
  
## Provenance

Structure to identify provenance relationships between annotations in different revisions.

JSON representation  
---  
      
    
    {
      "revision": integer,
      "id": integer,
      "parents": [
        {
          object ([Parent](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Parent))
        }
      ],
      "type": enum ([OperationType](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#OperationType))
    }  
  
Fields  
---  
`revision  
**(deprecated)**` |  `integer` This item is deprecated!The index of the revision that produced this element.  
`id  
**(deprecated)**` |  `integer` This item is deprecated!The ID of this operation. Needs to be unique within the scope of the revision.  
`parents[]` |  `object (`[Parent](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Parent)`)` References to the original elements that are replaced.  
`type` |  `enum (`[OperationType](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#OperationType)`)` The type of provenance operation.  
  
## Parent

The parent element the current element is based on. Used for referencing/aligning, removal and replacement operations.

JSON representation  
---  
      
    
    {
      "revision": integer,
      "index": integer,
      "id": integer
    }  
  
Fields  
---  
`revision` |  `integer` The index of the index into current revision's parentIds list.  
`index` |  `integer` The index of the parent item in the corresponding item list (eg. list of entities, properties within entities, etc.) in the parent revision.  
`id  
**(deprecated)**` |  `integer` This item is deprecated!The ID of the parent provenance.  
  
## OperationType

If a processor or agent does an explicit operation on existing elements.

Enums  
---  
`OPERATION_TYPE_UNSPECIFIED` | Operation type unspecified. If no operation is specified a provenance entry is simply used to match against a `parent`.  
`ADD` | Add an element.  
`REMOVE` | Remove an element identified by `parent`.  
`UPDATE` | Updates any fields within the given provenance scope of the message. It overwrites the fields rather than replacing them. Use this when you want to update a field value of an entity without also updating all the child properties.  
`REPLACE` | Currently unused. Replace an element identified by `parent`.  
`EVAL_REQUESTED` | Deprecated. Request human review for the element identified by `parent`.This item is deprecated!  
`EVAL_APPROVED` | Deprecated. Element is reviewed and approved at human review, confidence will be set to 1.0.This item is deprecated!  
`EVAL_SKIPPED` | Deprecated. Element is skipped in the validation process.This item is deprecated!  
  
## Paragraph

A collection of lines that a human would perceive as a paragraph.

JSON representation  
---  
      
    
    {
      "layout": {
        object ([Layout](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Layout))
      },
      "detectedLanguages": [
        {
          object ([DetectedLanguage](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#DetectedLanguage))
        }
      ],
      "provenance": {
        object ([Provenance](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Provenance))
      }
    }  
  
Fields  
---  
`layout` |  `object (`[Layout](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Layout)`)` `[Layout](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Layout)` for `[Paragraph](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Paragraph)`.  
`detectedLanguages[]` |  `object (`[DetectedLanguage](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#DetectedLanguage)`)` A list of detected languages together with confidence.  
`provenance  
**(deprecated)**` |  `object (`[Provenance](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Provenance)`)` This item is deprecated!The history of this annotation.  
  
## Line

A collection of tokens that a human would perceive as a line. Does not cross column boundaries, can be horizontal, vertical, etc.

JSON representation  
---  
      
    
    {
      "layout": {
        object ([Layout](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Layout))
      },
      "detectedLanguages": [
        {
          object ([DetectedLanguage](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#DetectedLanguage))
        }
      ],
      "provenance": {
        object ([Provenance](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Provenance))
      }
    }  
  
Fields  
---  
`layout` |  `object (`[Layout](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Layout)`)` `[Layout](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Layout)` for `[Line](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Line)`.  
`detectedLanguages[]` |  `object (`[DetectedLanguage](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#DetectedLanguage)`)` A list of detected languages together with confidence.  
`provenance  
**(deprecated)**` |  `object (`[Provenance](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Provenance)`)` This item is deprecated!The history of this annotation.  
  
## Token

A detected token.

JSON representation  
---  
      
    
    {
      "layout": {
        object ([Layout](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Layout))
      },
      "detectedBreak": {
        object ([DetectedBreak](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#DetectedBreak))
      },
      "detectedLanguages": [
        {
          object ([DetectedLanguage](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#DetectedLanguage))
        }
      ],
      "provenance": {
        object ([Provenance](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Provenance))
      },
      "styleInfo": {
        object ([StyleInfo](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#StyleInfo))
      }
    }  
  
Fields  
---  
`layout` |  `object (`[Layout](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Layout)`)` `[Layout](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Layout)` for `[Token](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Token)`.  
`detectedBreak` |  `object (`[DetectedBreak](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#DetectedBreak)`)` Detected break at the end of a `[Token](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Token)`.  
`detectedLanguages[]` |  `object (`[DetectedLanguage](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#DetectedLanguage)`)` A list of detected languages together with confidence.  
`provenance  
**(deprecated)**` |  `object (`[Provenance](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Provenance)`)` This item is deprecated!The history of this annotation.  
`styleInfo` |  `object (`[StyleInfo](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#StyleInfo)`)` Text style attributes.  
  
## DetectedBreak

Detected break at the end of a `[Token](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Token)`.

JSON representation  
---  
      
    
    {
      "type": enum ([Type](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Type))
    }  
  
Fields  
---  
`type` |  `enum (`[Type](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Type)`)` Detected break type.  
  
## Type

Enum to denote the type of break found.

Enums  
---  
`TYPE_UNSPECIFIED` | Unspecified break type.  
`SPACE` | A single whitespace.  
`WIDE_SPACE` | A wider whitespace.  
`HYPHEN` | A hyphen that indicates that a token has been split across lines.  
  
## StyleInfo

Font and other text style attributes.

JSON representation  
---  
      
    
    {
      "fontSize": integer,
      "pixelFontSize": number,
      "letterSpacing": number,
      "fontType": string,
      "bold": boolean,
      "italic": boolean,
      "underlined": boolean,
      "strikeout": boolean,
      "subscript": boolean,
      "superscript": boolean,
      "smallcaps": boolean,
      "fontWeight": integer,
      "handwritten": boolean,
      "textColor": {
        object ([Color](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/Color))
      },
      "backgroundColor": {
        object ([Color](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/Color))
      }
    }  
  
Fields  
---  
`fontSize` |  `integer` Font size in points (`1` point is `¹⁄₇₂` inches).  
`pixelFontSize` |  `number` Font size in pixels, equal to _unrounded`[fontSize](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#StyleInfo.FIELDS.font_size)`_ * _resolution_ ÷ `72.0`.  
`letterSpacing` |  `number` Letter spacing in points.  
`fontType` |  `string` Name or style of the font.  
`bold` |  `boolean` Whether the text is bold (equivalent to `[fontWeight](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#StyleInfo.FIELDS.font_weight)` is at least `700`).  
`italic` |  `boolean` Whether the text is italic.  
`underlined` |  `boolean` Whether the text is underlined.  
`strikeout` |  `boolean` Whether the text is strikethrough. This feature is not supported yet.  
`subscript` |  `boolean` Whether the text is a subscript. This feature is not supported yet.  
`superscript` |  `boolean` Whether the text is a superscript. This feature is not supported yet.  
`smallcaps` |  `boolean` Whether the text is in small caps. This feature is not supported yet.  
`fontWeight` |  `integer` TrueType weight on a scale `100` (thin) to `1000` (ultra-heavy). Normal is `400`, bold is `700`.  
`handwritten` |  `boolean` Whether the text is handwritten.  
`textColor` |  `object (`[Color](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/Color)`)` Color of the text.  
`backgroundColor` |  `object (`[Color](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/Color)`)` Color of the background.  
  
## VisualElement

Detected non-text visual elements, for example, checkbox, signature etc. on the page.

JSON representation  
---  
      
    
    {
      "layout": {
        object ([Layout](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Layout))
      },
      "type": string,
      "detectedLanguages": [
        {
          object ([DetectedLanguage](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#DetectedLanguage))
        }
      ]
    }  
  
Fields  
---  
`layout` |  `object (`[Layout](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Layout)`)` `[Layout](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Layout)` for `[VisualElement](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#VisualElement)`.  
`type` |  `string` Type of the `[VisualElement](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#VisualElement)`.  
`detectedLanguages[]` |  `object (`[DetectedLanguage](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#DetectedLanguage)`)` A list of detected languages together with confidence.  
  
## Table

A table representation similar to HTML table structure.

JSON representation  
---  
      
    
    {
      "layout": {
        object ([Layout](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Layout))
      },
      "headerRows": [
        {
          object ([TableRow](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#TableRow))
        }
      ],
      "bodyRows": [
        {
          object ([TableRow](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#TableRow))
        }
      ],
      "detectedLanguages": [
        {
          object ([DetectedLanguage](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#DetectedLanguage))
        }
      ],
      "provenance": {
        object ([Provenance](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Provenance))
      }
    }  
  
Fields  
---  
`layout` |  `object (`[Layout](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Layout)`)` `[Layout](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Layout)` for `[Table](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Table)`.  
`headerRows[]` |  `object (`[TableRow](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#TableRow)`)` Header rows of the table.  
`bodyRows[]` |  `object (`[TableRow](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#TableRow)`)` Body rows of the table.  
`detectedLanguages[]` |  `object (`[DetectedLanguage](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#DetectedLanguage)`)` A list of detected languages together with confidence.  
`provenance  
**(deprecated)**` |  `object (`[Provenance](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Provenance)`)` This item is deprecated!The history of this table.  
  
## TableRow

A row of table cells.

JSON representation  
---  
      
    
    {
      "cells": [
        {
          object ([TableCell](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#TableCell))
        }
      ]
    }  
  
Fields  
---  
`cells[]` |  `object (`[TableCell](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#TableCell)`)` Cells that make up this row.  
  
## TableCell

A cell representation inside the table.

JSON representation  
---  
      
    
    {
      "layout": {
        object ([Layout](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Layout))
      },
      "rowSpan": integer,
      "colSpan": integer,
      "detectedLanguages": [
        {
          object ([DetectedLanguage](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#DetectedLanguage))
        }
      ]
    }  
  
Fields  
---  
`layout` |  `object (`[Layout](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Layout)`)` `[Layout](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Layout)` for `[TableCell](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#TableCell)`.  
`rowSpan` |  `integer` How many rows this cell spans.  
`colSpan` |  `integer` How many columns this cell spans.  
`detectedLanguages[]` |  `object (`[DetectedLanguage](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#DetectedLanguage)`)` A list of detected languages together with confidence.  
  
## FormField

A form field detected on the page.

JSON representation  
---  
      
    
    {
      "fieldName": {
        object ([Layout](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Layout))
      },
      "fieldValue": {
        object ([Layout](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Layout))
      },
      "nameDetectedLanguages": [
        {
          object ([DetectedLanguage](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#DetectedLanguage))
        }
      ],
      "valueDetectedLanguages": [
        {
          object ([DetectedLanguage](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#DetectedLanguage))
        }
      ],
      "valueType": string,
      "correctedKeyText": string,
      "correctedValueText": string,
      "provenance": {
        object ([Provenance](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Provenance))
      }
    }  
  
Fields  
---  
`fieldName` |  `object (`[Layout](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Layout)`)` `[Layout](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Layout)` for the `[FormField](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#FormField)` name. For example, `Address`, `Email`, `Grand total`, `Phone number`, etc.  
`fieldValue` |  `object (`[Layout](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Layout)`)` `[Layout](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Layout)` for the `[FormField](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#FormField)` value.  
`nameDetectedLanguages[]` |  `object (`[DetectedLanguage](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#DetectedLanguage)`)` A list of detected languages for name together with confidence.  
`valueDetectedLanguages[]` |  `object (`[DetectedLanguage](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#DetectedLanguage)`)` A list of detected languages for value together with confidence.  
`valueType` |  `string` If the value is non-textual, this field represents the type. Current valid values are:

  * blank (this indicates the `fieldValue` is normal text)
  * `unfilled_checkbox`
  * `filled_checkbox`

  
`correctedKeyText` |  `string` Created for Labeling UI to export key text. If corrections were made to the text identified by the `fieldName.text_anchor`, this field will contain the correction.  
`correctedValueText` |  `string` Created for Labeling UI to export value text. If corrections were made to the text identified by the `fieldValue.text_anchor`, this field will contain the correction.  
`provenance` |  `object (`[Provenance](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Provenance)`)` The history of this annotation.  
  
## Symbol

A detected symbol.

JSON representation  
---  
      
    
    {
      "layout": {
        object ([Layout](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Layout))
      },
      "detectedLanguages": [
        {
          object ([DetectedLanguage](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#DetectedLanguage))
        }
      ]
    }  
  
Fields  
---  
`layout` |  `object (`[Layout](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Layout)`)` `[Layout](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Layout)` for `[Symbol](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Symbol)`.  
`detectedLanguages[]` |  `object (`[DetectedLanguage](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#DetectedLanguage)`)` A list of detected languages together with confidence.  
  
## DetectedBarcode

A detected barcode.

JSON representation  
---  
      
    
    {
      "layout": {
        object ([Layout](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Layout))
      },
      "barcode": {
        object ([Barcode](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Barcode))
      }
    }  
  
Fields  
---  
`layout` |  `object (`[Layout](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Layout)`)` `[Layout](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Layout)` for `[DetectedBarcode](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#DetectedBarcode)`.  
`barcode` |  `object (`[Barcode](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Barcode)`)` Detailed barcode information of the `[DetectedBarcode](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#DetectedBarcode)`.  
  
## Barcode

Encodes the detailed information of a barcode.

JSON representation  
---  
      
    
    {
      "format": string,
      "valueFormat": string,
      "rawValue": string
    }  
  
Fields  
---  
`format` |  `string` Format of a barcode. The supported formats are:

  * `CODE_128`: Code 128 type.
  * `CODE_39`: Code 39 type.
  * `CODE_93`: Code 93 type.
  * `CODABAR`: Codabar type.
  * `DATA_MATRIX`: 2D Data Matrix type.
  * `ITF`: ITF type.
  * `EAN_13`: EAN-13 type.
  * `EAN_8`: EAN-8 type.
  * `QR_CODE`: 2D QR code type.
  * `UPC_A`: UPC-A type.
  * `UPC_E`: UPC-E type.
  * `PDF417`: PDF417 type.
  * `AZTEC`: 2D Aztec code type.
  * `DATABAR`: GS1 DataBar code type.

  
`valueFormat` |  `string` Value format describes the format of the value that a barcode encodes. The supported formats are:

  * `CONTACT_INFO`: Contact information.
  * `EMAIL`: Email address.
  * `ISBN`: ISBN identifier.
  * `PHONE`: Phone number.
  * `PRODUCT`: Product.
  * `SMS`: SMS message.
  * `TEXT`: Text string.
  * `URL`: URL address.
  * `WIFI`: Wifi information.
  * `GEO`: Geo-localization.
  * `CALENDAR_EVENT`: Calendar event.
  * `DRIVER_LICENSE`: Driver's license.

  
`rawValue` |  `string` Raw value encoded in the barcode. For example: `'MEBKM:TITLE:Google;URL:https://www.google.com;;'`.  
  
## ImageQualityScores

Image quality scores for the page image.

JSON representation  
---  
      
    
    {
      "qualityScore": number,
      "detectedDefects": [
        {
          object ([DetectedDefect](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#DetectedDefect))
        }
      ]
    }  
  
Fields  
---  
`qualityScore` |  `number` The overall quality score. Range `[0, 1]` where `1` is perfect quality.  
`detectedDefects[]` |  `object (`[DetectedDefect](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#DetectedDefect)`)` A list of detected defects.  
  
## DetectedDefect

Image Quality Defects

JSON representation  
---  
      
    
    {
      "type": string,
      "confidence": number
    }  
  
Fields  
---  
`type` |  `string` Name of the defect type. Supported values are:

  * `quality/defect_blurry`
  * `quality/defect_noisy`
  * `quality/defect_dark`
  * `quality/defect_faint`
  * `quality/defect_text_too_small`
  * `quality/defect_document_cutoff`
  * `quality/defect_text_cutoff`
  * `quality/defect_glare`

  
`confidence` |  `number` Confidence of detected defect. Range `[0, 1]` where `1` indicates strong confidence that the defect exists.  
  
## Entity

An entity that could be a phrase in the text or a property that belongs to the document. It is a known entity type, such as a person, an organization, or location.

JSON representation  
---  
      
    
    {
      "textAnchor": {
        object ([TextAnchor](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#TextAnchor))
      },
      "type": string,
      "mentionText": string,
      "mentionId": string,
      "confidence": number,
      "pageAnchor": {
        object ([PageAnchor](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#PageAnchor))
      },
      "id": string,
      "normalizedValue": {
        object ([NormalizedValue](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#NormalizedValue))
      },
      "properties": [
        {
          object ([Entity](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Entity))
        }
      ],
      "provenance": {
        object ([Provenance](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Provenance))
      },
      "redacted": boolean,
      "method": enum ([Method](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Method))
    }  
  
Fields  
---  
`textAnchor` |  `object (`[TextAnchor](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#TextAnchor)`)` Optional. Provenance of the entity. Text anchor indexing into the `[Document.text](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#FIELDS.text)`.  
`type` |  `string` Required. Entity type from a schema, for example, `Address`.  
`mentionText` |  `string` Optional. Text value of the entity, for example, `1600 Amphitheatre Pkwy`.  
`mentionId` |  `string` Optional. Deprecated. Use `id` field instead.  
`confidence` |  `number` Optional. Confidence of detected Schema entity. Range `[0, 1]`.  
`pageAnchor` |  `object (`[PageAnchor](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#PageAnchor)`)` Optional. Represents the provenance of this entity wrt. the location on the page where it was found.  
`id` |  `string` Optional. Canonical id. This will be a unique value in the entity list for this document.  
`normalizedValue` |  `object (`[NormalizedValue](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#NormalizedValue)`)` Optional. Normalized entity value. Absent if the extracted value could not be converted or the type (for example, address) is not supported for certain parsers. This field is also only populated for certain supported document types.  
`properties[]` |  `object (`[Entity](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Entity)`)` Optional. Entities can be nested to form a hierarchical data structure representing the content in the document.  
`provenance` |  `object (`[Provenance](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Provenance)`)` Optional. The history of this annotation.  
`redacted` |  `boolean` Optional. Whether the entity will be redacted for de-identification purposes.  
`method` |  `enum (`[Method](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Method)`)` Optional. Specifies how the entity's value is obtained.  
  
## PageAnchor

Referencing the visual context of the entity in the `[Document.pages](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#FIELDS.pages)`. Page anchors can be cross-page, consist of multiple bounding polygons and optionally reference specific layout element types.

JSON representation  
---  
      
    
    {
      "pageRefs": [
        {
          object ([PageRef](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#PageRef))
        }
      ]
    }  
  
Fields  
---  
`pageRefs[]` |  `object (`[PageRef](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#PageRef)`)` One or more references to visual page elements  
  
## PageRef

Represents a weak reference to a page element within a document.

JSON representation  
---  
      
    
    {
      "page": string,
      "layoutType": enum ([LayoutType](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#LayoutType)),
      "layoutId": string,
      "boundingPoly": {
        object ([BoundingPoly](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#BoundingPoly))
      },
      "confidence": number
    }  
  
Fields  
---  
`page` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. Index into the `[Document.pages](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#FIELDS.pages)` element, for example using `[Document.pages][pageRefs.page]` to locate the related page element. This field is skipped when its value is the default `0`. See <https://developers.google.com/protocol-buffers/docs/proto3#json>.  
`layoutType` |  `enum (`[LayoutType](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#LayoutType)`)` Optional. The type of the layout element that is being referenced if any.  
`layoutId  
**(deprecated)**` |  `string` This item is deprecated!Optional. Deprecated. Use `[PageRef.bounding_poly](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#PageRef.FIELDS.bounding_poly)` instead.  
`boundingPoly` |  `object (`[BoundingPoly](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#BoundingPoly)`)` Optional. Identifies the bounding polygon of a layout element on the page. If `layoutType` is set, the bounding polygon must be exactly the same to the layout element it's referring to.  
`confidence` |  `number` Optional. Confidence of detected page element, if applicable. Range `[0, 1]`.  
  
## LayoutType

The type of layout that is being referenced.

Enums  
---  
`LAYOUT_TYPE_UNSPECIFIED` | Layout Unspecified.  
`BLOCK` | References a `[Page.blocks](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Page.FIELDS.blocks)` element.  
`PARAGRAPH` | References a `[Page.paragraphs](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Page.FIELDS.paragraphs)` element.  
`LINE` | References a `[Page.lines](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Page.FIELDS.lines)` element.  
`TOKEN` | References a `[Page.tokens](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Page.FIELDS.tokens)` element.  
`VISUAL_ELEMENT` | References a `[Page.visual_elements](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Page.FIELDS.visual_elements)` element.  
`TABLE` | Refrrences a `[Page.tables](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Page.FIELDS.tables)` element.  
`FORM_FIELD` | References a `[Page.form_fields](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Page.FIELDS.form_fields)` element.  
  
## NormalizedValue

Parsed and normalized entity value.

JSON representation  
---  
      
    
    {
      "text": string,
    
      // Union field structured_value can be only one of the following:
      "moneyValue": {
        object ([Money](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/Money))
      },
      "dateValue": {
        object ([Date](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/Date))
      },
      "datetimeValue": {
        object ([DateTime](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/DateTime))
      },
      "addressValue": {
        object ([PostalAddress](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/PostalAddress))
      },
      "booleanValue": boolean,
      "integerValue": integer,
      "floatValue": number,
      "signatureValue": boolean
      // End of list of possible types for union field structured_value.
    }  
  
Fields  
---  
`text` |  `string` Optional. An optional field to store a normalized string. For some entity types, one of respective `structured_value` fields may also be populated. Also not all the types of `structured_value` will be normalized. For example, some processors may not generate `float` or `integer` normalized text by default.Below are sample formats mapped to structured values.

  * Money/Currency type (`moneyValue`) is in the ISO 4217 text format.
  * Date type (`dateValue`) is in the ISO 8601 text format.
  * Datetime type (`datetimeValue`) is in the ISO 8601 text format.

  
Union field `structured_value`. An optional structured entity value. Must match entity type defined in schema if known. If this field is present, the `text` field could also be populated. `structured_value` can be only one of the following:  
`moneyValue` |  `object (`[Money](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/Money)`)` Money value. See also: <https://github.com/googleapis/googleapis/blob/master/google/type/money.proto>  
`dateValue` |  `object (`[Date](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/Date)`)` Date value. Includes year, month, day. See also: <https://github.com/googleapis/googleapis/blob/master/google/type/date.proto>  
`datetimeValue` |  `object (`[DateTime](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/DateTime)`)` DateTime value. Includes date, time, and timezone. See also: <https://github.com/googleapis/googleapis/blob/master/google/type/datetime.proto>  
`addressValue` |  `object (`[PostalAddress](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/PostalAddress)`)` Postal address. See also: <https://github.com/googleapis/googleapis/blob/master/google/type/postal_address.proto>  
`booleanValue` |  `boolean` Boolean value. Can be used for entities with binary values, or for checkboxes.  
`integerValue` |  `integer` Integer value.  
`floatValue` |  `number` Float value.  
`signatureValue` |  `boolean` A signature, which is a graphical representation of a person's name, often used to sign a document.  
  
## Method

Specifies how the entity's value is obtained.

Enums  
---  
`METHOD_UNSPECIFIED` | When the method is not specified, it should be treated as `EXTRACT`.  
`EXTRACT` | The entity's value is directly extracted as-is from the document text.  
`DERIVE` | The entity's value is derived through inference and is not necessarily an exact text extraction from the document.  
  
## EntityRelation

Relationship between `[Entities](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Entity)`.

JSON representation  
---  
      
    
    {
      "subjectId": string,
      "objectId": string,
      "relation": string
    }  
  
Fields  
---  
`subjectId` |  `string` Subject entity id.  
`objectId` |  `string` Object entity id.  
`relation` |  `string` Relationship description.  
  
## TextChange

This message is used for text changes aka. OCR corrections.

JSON representation  
---  
      
    
    {
      "textAnchor": {
        object ([TextAnchor](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#TextAnchor))
      },
      "changedText": string,
      "provenance": [
        {
          object ([Provenance](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Provenance))
        }
      ]
    }  
  
Fields  
---  
`textAnchor` |  `object (`[TextAnchor](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#TextAnchor)`)` Provenance of the correction. Text anchor indexing into the `[Document.text](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#FIELDS.text)`. There can only be a single `TextAnchor.text_segments` element. If the start and end index of the text segment are the same, the text change is inserted before that index.  
`changedText` |  `string` The text that replaces the text identified in the `textAnchor`.  
`provenance[]  
**(deprecated)**` |  `object (`[Provenance](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Provenance)`)` This item is deprecated!The history of this annotation.  
  
## ShardInfo

For a large document, sharding may be performed to produce several document shards. Each document shard contains this field to detail which shard it is.

JSON representation  
---  
      
    
    {
      "shardIndex": string,
      "shardCount": string,
      "textOffset": string,
      "pageOffset": integer
    }  
  
Fields  
---  
`shardIndex` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The 0-based index of this shard.  
`shardCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Total number of shards.  
`textOffset` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The index of the first character in `[Document.text](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#FIELDS.text)` in the overall document global text.  
`pageOffset` |  `integer` The index of the first page in `[Document.pages](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#FIELDS.pages)` in the overall document global pages. Available for document shards created by the document splitter.  
  
## Revision

Contains past or forward revisions of this document.

JSON representation  
---  
      
    
    {
      "id": string,
      "parent": [
        integer
      ],
      "parentIds": [
        string
      ],
      "createTime": string,
      "humanReview": {
        object ([HumanReview](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#HumanReview))
      },
    
      // Union field source can be only one of the following:
      "agent": string,
      "processor": string
      // End of list of possible types for union field source.
    }  
  
Fields  
---  
`id` |  `string` ID of the revision, internally generated by doc proto storage. Unique within the context of the document.  
`parent[]  
**(deprecated)**` |  `integer` This item is deprecated!The revisions that this revision is based on. This can include one or more parent (when documents are merged.) This field represents the index into the `revisions` field.  
`parentIds[]` |  `string` The revisions that this revision is based on. Must include all the ids that have anything to do with this revision - eg. there are `provenance.parent.revision` fields that index into this field.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time that the revision was created, internally generated by doc proto storage at the time of create.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`humanReview` |  `object (`[HumanReview](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#HumanReview)`)` Human Review information of this revision.  
Union field `source`. Who/what made the change `source` can be only one of the following:  
`agent` |  `string` If the change was made by a person specify the name or ID of that person.  
`processor` |  `string` If the annotation was made by processor identify the processor by its resource name.  
  
## HumanReview

Human Review information of the document.

JSON representation  
---  
      
    
    {
      "state": string,
      "stateMessage": string
    }  
  
Fields  
---  
`state` |  `string` Human review state. For example, `requested`, `succeeded`, `rejected`.  
`stateMessage` |  `string` A message providing more details about the current state of processing. For example, the rejection reason when the state is `rejected`.  
  
## DocumentLayout

Represents the parsed layout of a document as a collection of blocks that the document is divided into.

JSON representation  
---  
      
    
    {
      "blocks": [
        {
          object ([DocumentLayoutBlock](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#DocumentLayoutBlock))
        }
      ]
    }  
  
Fields  
---  
`blocks[]` |  `object (`[DocumentLayoutBlock](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#DocumentLayoutBlock)`)` List of blocks in the document.  
  
## DocumentLayoutBlock

Represents a block. A block could be one of the various types (text, table, list) supported.

JSON representation  
---  
      
    
    {
      "blockId": string,
      "pageSpan": {
        object ([LayoutPageSpan](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#LayoutPageSpan))
      },
      "boundingBox": {
        object ([BoundingPoly](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#BoundingPoly))
      },
    
      // Union field block can be only one of the following:
      "textBlock": {
        object ([LayoutTextBlock](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#LayoutTextBlock))
      },
      "tableBlock": {
        object ([LayoutTableBlock](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#LayoutTableBlock))
      },
      "listBlock": {
        object ([LayoutListBlock](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#LayoutListBlock))
      },
      "imageBlock": {
        object ([LayoutImageBlock](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#LayoutImageBlock))
      }
      // End of list of possible types for union field block.
    }  
  
Fields  
---  
`blockId` |  `string` ID of the block.  
`pageSpan` |  `object (`[LayoutPageSpan](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#LayoutPageSpan)`)` Page span of the block.  
`boundingBox` |  `object (`[BoundingPoly](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#BoundingPoly)`)` Identifies the bounding box for the block.  
Union field `block`.`block` can be only one of the following:  
`textBlock` |  `object (`[LayoutTextBlock](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#LayoutTextBlock)`)` Block consisting of text content.  
`tableBlock` |  `object (`[LayoutTableBlock](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#LayoutTableBlock)`)` Block consisting of table content/structure.  
`listBlock` |  `object (`[LayoutListBlock](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#LayoutListBlock)`)` Block consisting of list content/structure.  
`imageBlock` |  `object (`[LayoutImageBlock](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#LayoutImageBlock)`)` Block consisting of image content.  
  
## LayoutTextBlock

Represents a text type block.

JSON representation  
---  
      
    
    {
      "text": string,
      "type": string,
      "blocks": [
        {
          object ([DocumentLayoutBlock](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#DocumentLayoutBlock))
        }
      ],
      "annotations": {
        object ([Annotations](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Annotations))
      }
    }  
  
Fields  
---  
`text` |  `string` Text content stored in the block.  
`type` |  `string` Type of the text in the block. Available options are: `paragraph`, `subtitle`, `heading-1`, `heading-2`, `heading-3`, `heading-4`, `heading-5`, `header`, `footer`.  
`blocks[]` |  `object (`[DocumentLayoutBlock](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#DocumentLayoutBlock)`)` A text block could further have child blocks. Repeated blocks support further hierarchies and nested blocks.  
`annotations` |  `object (`[Annotations](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Annotations)`)` Annotation of the text block.  
  
## Annotations

Represents the annotation of a block or a chunk.

JSON representation  
---  
      
    
    {
      "description": string
    }  
  
Fields  
---  
`description` |  `string` The description of the content with this annotation.  
  
## LayoutTableBlock

Represents a table type block.

JSON representation  
---  
      
    
    {
      "headerRows": [
        {
          object ([LayoutTableRow](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#LayoutTableRow))
        }
      ],
      "bodyRows": [
        {
          object ([LayoutTableRow](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#LayoutTableRow))
        }
      ],
      "caption": string,
      "annotations": {
        object ([Annotations](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Annotations))
      }
    }  
  
Fields  
---  
`headerRows[]` |  `object (`[LayoutTableRow](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#LayoutTableRow)`)` Header rows at the top of the table.  
`bodyRows[]` |  `object (`[LayoutTableRow](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#LayoutTableRow)`)` Body rows containing main table content.  
`caption` |  `string` Table caption/title.  
`annotations` |  `object (`[Annotations](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Annotations)`)` Annotation of the table block.  
  
## LayoutTableRow

Represents a row in a table.

JSON representation  
---  
      
    
    {
      "cells": [
        {
          object ([LayoutTableCell](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#LayoutTableCell))
        }
      ]
    }  
  
Fields  
---  
`cells[]` |  `object (`[LayoutTableCell](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#LayoutTableCell)`)` A table row is a list of table cells.  
  
## LayoutTableCell

Represents a cell in a table row.

JSON representation  
---  
      
    
    {
      "blocks": [
        {
          object ([DocumentLayoutBlock](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#DocumentLayoutBlock))
        }
      ],
      "rowSpan": integer,
      "colSpan": integer
    }  
  
Fields  
---  
`blocks[]` |  `object (`[DocumentLayoutBlock](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#DocumentLayoutBlock)`)` A table cell is a list of blocks. Repeated blocks support further hierarchies and nested blocks.  
`rowSpan` |  `integer` How many rows this cell spans.  
`colSpan` |  `integer` How many columns this cell spans.  
  
## LayoutListBlock

Represents a list type block.

JSON representation  
---  
      
    
    {
      "listEntries": [
        {
          object ([LayoutListEntry](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#LayoutListEntry))
        }
      ],
      "type": string
    }  
  
Fields  
---  
`listEntries[]` |  `object (`[LayoutListEntry](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#LayoutListEntry)`)` List entries that constitute a list block.  
`type` |  `string` Type of the listEntries (if exist). Available options are `ordered` and `unordered`.  
  
## LayoutListEntry

Represents an entry in the list.

JSON representation  
---  
      
    
    {
      "blocks": [
        {
          object ([DocumentLayoutBlock](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#DocumentLayoutBlock))
        }
      ]
    }  
  
Fields  
---  
`blocks[]` |  `object (`[DocumentLayoutBlock](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#DocumentLayoutBlock)`)` A list entry is a list of blocks. Repeated blocks support further hierarchies and nested blocks.  
  
## LayoutImageBlock

Represents an image type block.

JSON representation  
---  
      
    
    {
      "mimeType": string,
      "imageText": string,
      "annotations": {
        object ([Annotations](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Annotations))
      },
    
      // Union field image_source can be only one of the following:
      "blobAssetId": string,
      "gcsUri": string,
      "dataUri": string
      // End of list of possible types for union field image_source.
    }  
  
Fields  
---  
`mimeType` |  `string` Mime type of the image. An IANA published [media type (MIME type)](https://www.iana.org/assignments/media-types/media-types.xhtml).  
`imageText` |  `string` Text extracted from the image using OCR or alt text describing the image.  
`annotations` |  `object (`[Annotations](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Annotations)`)` Annotation of the image block.  
Union field `image_source`. Source of the image. `image_source` can be only one of the following:  
`blobAssetId` |  `string` Optional. Asset ID of the inline image. If set, find the image content in the blobAssets field.  
`gcsUri` |  `string` Optional. Google Cloud Storage URI of the image.  
`dataUri` |  `string` Optional. Data URI of the image. It is composed of four parts: a prefix (data:), a MIME type indicating the type of data, an optional base64 token if non-textual, and the data itself: data:[][;base64],  
  
## LayoutPageSpan

Represents where the block starts and ends in the document.

JSON representation  
---  
      
    
    {
      "pageStart": integer,
      "pageEnd": integer
    }  
  
Fields  
---  
`pageStart` |  `integer` Page where block starts in the document.  
`pageEnd` |  `integer` Page where block ends in the document.  
  
## ChunkedDocument

Represents the chunks that the document is divided into.

JSON representation  
---  
      
    
    {
      "chunks": [
        {
          object ([Chunk](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Chunk))
        }
      ]
    }  
  
Fields  
---  
`chunks[]` |  `object (`[Chunk](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Chunk)`)` List of chunks.  
  
## Chunk

Represents a chunk.

JSON representation  
---  
      
    
    {
      "chunkId": string,
      "sourceBlockIds": [
        string
      ],
      "content": string,
      "pageSpan": {
        object ([ChunkPageSpan](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#ChunkPageSpan))
      },
      "pageHeaders": [
        {
          object ([ChunkPageHeader](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#ChunkPageHeader))
        }
      ],
      "pageFooters": [
        {
          object ([ChunkPageFooter](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#ChunkPageFooter))
        }
      ],
      "chunkFields": [
        {
          object ([ChunkField](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#ChunkField))
        }
      ]
    }  
  
Fields  
---  
`chunkId` |  `string` ID of the chunk.  
`sourceBlockIds[]` |  `string` Unused.  
`content` |  `string` Text content of the chunk.  
`pageSpan` |  `object (`[ChunkPageSpan](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#ChunkPageSpan)`)` Page span of the chunk.  
`pageHeaders[]` |  `object (`[ChunkPageHeader](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#ChunkPageHeader)`)` Page headers associated with the chunk.  
`pageFooters[]` |  `object (`[ChunkPageFooter](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#ChunkPageFooter)`)` Page footers associated with the chunk.  
`chunkFields[]` |  `object (`[ChunkField](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#ChunkField)`)` Chunk fields inside this chunk.  
  
## ChunkPageSpan

Represents where the chunk starts and ends in the document.

JSON representation  
---  
      
    
    {
      "pageStart": integer,
      "pageEnd": integer
    }  
  
Fields  
---  
`pageStart` |  `integer` Page where chunk starts in the document.  
`pageEnd` |  `integer` Page where chunk ends in the document.  
  
## ChunkPageHeader

Represents the page header associated with the chunk.

JSON representation  
---  
      
    
    {
      "text": string,
      "pageSpan": {
        object ([ChunkPageSpan](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#ChunkPageSpan))
      }
    }  
  
Fields  
---  
`text` |  `string` Header in text format.  
`pageSpan` |  `object (`[ChunkPageSpan](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#ChunkPageSpan)`)` Page span of the header.  
  
## ChunkPageFooter

Represents the page footer associated with the chunk.

JSON representation  
---  
      
    
    {
      "text": string,
      "pageSpan": {
        object ([ChunkPageSpan](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#ChunkPageSpan))
      }
    }  
  
Fields  
---  
`text` |  `string` Footer in text format.  
`pageSpan` |  `object (`[ChunkPageSpan](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#ChunkPageSpan)`)` Page span of the footer.  
  
## ChunkField

The chunk field in the chunk. A chunk field could be one of the various types (for example, image, table) supported.

JSON representation  
---  
      
    
    {
    
      // Union field field_type can be only one of the following:
      "imageChunkField": {
        object ([ImageChunkField](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#ImageChunkField))
      },
      "tableChunkField": {
        object ([TableChunkField](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#TableChunkField))
      }
      // End of list of possible types for union field field_type.
    }  
  
Fields  
---  
Union field `field_type`. The type of the chunk field. `field_type` can be only one of the following:  
`imageChunkField` |  `object (`[ImageChunkField](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#ImageChunkField)`)` The image chunk field in the chunk.  
`tableChunkField` |  `object (`[TableChunkField](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#TableChunkField)`)` The table chunk field in the chunk.  
  
## ImageChunkField

The image chunk field in the chunk.

JSON representation  
---  
      
    
    {
      "annotations": {
        object ([Annotations](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Annotations))
      },
    
      // Union field image_source can be only one of the following:
      "blobAssetId": string,
      "gcsUri": string,
      "dataUri": string
      // End of list of possible types for union field image_source.
    }  
  
Fields  
---  
`annotations` |  `object (`[Annotations](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Annotations)`)` Annotation of the image chunk field.  
Union field `image_source`. Source of the image. `image_source` can be only one of the following:  
`blobAssetId` |  `string` Optional. Asset ID of the inline image. If set, find the image content in the blobAssets field.  
`gcsUri` |  `string` Optional. Google Cloud Storage URI of the image.  
`dataUri` |  `string` Optional. Data URI of the image. It is composed of four parts: a prefix (data:), a MIME type indicating the type of data, an optional base64 token if non-textual, and the data itself: data:[][;base64],  
  
## TableChunkField

The table chunk field in the chunk.

JSON representation  
---  
      
    
    {
      "annotations": {
        object ([Annotations](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Annotations))
      }
    }  
  
Fields  
---  
`annotations` |  `object (`[Annotations](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Annotations)`)` Annotation of the table chunk field.  
  
## BlobAsset

Represents a blob asset. It's used to store the content of the inline blob in this document, for example, image bytes, such that it can be referenced by other fields in the document via asset ID.

JSON representation  
---  
      
    
    {
      "assetId": string,
      "content": string,
      "mimeType": string
    }  
  
Fields  
---  
`assetId` |  `string` Optional. The ID of the blob asset.  
`content` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Optional. The content of the blob asset, for example, image bytes.A base64-encoded string.  
`mimeType` |  `string` The mime type of the blob asset. An IANA published [media type (MIME type)](https://www.iana.org/assignments/media-types/media-types.xhtml).  
  
## EntityValidationOutput

The output of the validation given the document and the validation rules.

JSON representation  
---  
      
    
    {
      "validationResults": [
        {
          object ([ValidationResult](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#ValidationResult))
        }
      ],
      "passAllRules": boolean
    }  
  
Fields  
---  
`validationResults[]` |  `object (`[ValidationResult](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#ValidationResult)`)` The result of each validation rule.  
`passAllRules` |  `boolean` The overall result of the validation, true if all applicable rules are valid.  
  
## ValidationResult

Validation result for a single validation rule.

JSON representation  
---  
      
    
    {
      "rule": string,
      "ruleName": string,
      "ruleDescription": string,
      "validationResultType": enum ([ValidationResultType](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#ValidationResultType)),
      "validationDetails": string
    }  
  
Fields  
---  
`rule` |  `string` Optional. The name of the rule resource that is used for validation. Format: `projects/{project}/locations/{location}/rules/{rule}`  
`ruleName` |  `string` The display name of the validation rule.  
`ruleDescription` |  `string` The description of the validation rule.  
`validationResultType` |  `enum (`[ValidationResultType](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#ValidationResultType)`)` The result of the validation rule.  
`validationDetails` |  `string` The detailed information of the running the validation process using the entity from the document based on the validation rule.  
  
## ValidationResultType

The result of the validation rule.

Enums  
---  
`VALIDATION_RESULT_TYPE_UNSPECIFIED` | The validation result type is unspecified.  
`VALIDATION_RESULT_TYPE_VALID` | The validation is valid.  
`VALIDATION_RESULT_TYPE_INVALID` | The validation is invalid.  
`VALIDATION_RESULT_TYPE_SKIPPED` | The validation is skipped.  
`VALIDATION_RESULT_TYPE_NOT_APPLICABLE` | The validation is not applicable.  
  
## EntitiesRevision

Entity revision.

JSON representation  
---  
      
    
    {
      "revisionId": string,
      "entities": [
        {
          object ([Entity](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Entity))
        }
      ],
      "entityValidationOutput": {
        object ([EntityValidationOutput](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#EntityValidationOutput))
      },
      "provenance": {
        object ([Provenance](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Provenance))
      }
    }  
  
Fields  
---  
`revisionId` |  `string` The revision id.  
`entities[]` |  `object (`[Entity](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Entity)`)` The entities in this revision.  
`entityValidationOutput` |  `object (`[EntityValidationOutput](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#EntityValidationOutput)`)` The entity validation output for this revision.  
`provenance` |  `object (`[Provenance](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Provenance)`)` Optional. The history of this revision.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
