---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse/
title: AnnotateImageResponse \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:13:42.192180+00:00
---

# AnnotateImageResponse  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  AnnotateImageResponse Stay organized with collections  Save and categorize content based on your preferences. 

Response to an image annotation request.

JSON representation  
---  
      
    
    {
      "textAnnotations": [
        {
          object ([EntityAnnotation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse#EntityAnnotation))
        }
      ],
      "fullTextAnnotation": {
        object ([TextAnnotation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse#TextAnnotation))
      },
      "error": {
        object ([Status](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/Status))
      },
      "context": {
        object ([ImageAnnotationContext](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse#ImageAnnotationContext))
      }
    }  
  
Fields  
---  
`textAnnotations[]` |  `object (`[EntityAnnotation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse#EntityAnnotation)`)` If present, text (OCR) detection has completed successfully.  
`fullTextAnnotation` |  `object (`[TextAnnotation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse#TextAnnotation)`)` If present, text (OCR) detection or document (OCR) text detection has completed successfully. This annotation provides the structural hierarchy for the OCR detected text.  
`error` |  `object (`[Status](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/Status)`)` If set, represents the error message for the operation. Note that filled-in image annotations are guaranteed to be correct, even when `error` is set.  
`context` |  `object (`[ImageAnnotationContext](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse#ImageAnnotationContext)`)` If present, contextual information is needed to understand where this image comes from.  
  
## EntityAnnotation

Set of detected entity features.

JSON representation  
---  
      
    
    {
      "mid": string,
      "locale": string,
      "description": string,
      "score": number,
      "confidence": number,
      "topicality": number,
      "boundingPoly": {
        object ([BoundingPoly](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse#BoundingPoly))
      },
      "properties": [
        {
          object ([Property](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse#Property))
        }
      ]
    }  
  
Fields  
---  
`mid` |  `string` Opaque entity ID. Some IDs may be available in [Google Knowledge Graph Search API](https://developers.google.com/knowledge-graph/).  
`locale` |  `string` The language code for the locale in which the entity textual `description` is expressed.  
`description` |  `string` Entity textual description, expressed in its `locale` language.  
`score` |  `number` Overall score of the result. Range [0, 1].  
`confidence  
**(deprecated)**` |  `number` This item is deprecated!**Deprecated. Use`score` instead.** The accuracy of the entity detection in an image. For example, for an image in which the "Eiffel Tower" entity is detected, this field represents the confidence that there is a tower in the query image. Range [0, 1].  
`topicality` |  `number` The relevancy of the ICA (Image Content Annotation) label to the image. For example, the relevancy of "tower" is likely higher to an image containing the detected "Eiffel Tower" than to an image containing a detected distant towering building, even though the confidence that there is a tower in each image may be the same. Range [0, 1].  
`boundingPoly` |  `object (`[BoundingPoly](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse#BoundingPoly)`)` Image region to which this entity belongs. Not produced for `LABEL_DETECTION` features.  
`properties[]` |  `object (`[Property](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse#Property)`)` Some entities may have optional user-supplied `Property` (name/value) fields, such a score or string that qualifies the entity.  
  
## BoundingPoly

A bounding polygon for the detected image annotation.

JSON representation  
---  
      
    
    {
      "vertices": [
        {
          object ([Vertex](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse#Vertex))
        }
      ],
      "normalizedVertices": [
        {
          object ([NormalizedVertex](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse#NormalizedVertex))
        }
      ]
    }  
  
Fields  
---  
`vertices[]` |  `object (`[Vertex](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse#Vertex)`)` The bounding polygon vertices.  
`normalizedVertices[]` |  `object (`[NormalizedVertex](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse#NormalizedVertex)`)` The bounding polygon normalized vertices.  
  
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
`y` |  `integer` Y coordinate.  
  
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
`y` |  `number` Y coordinate.  
  
## Property

A `Property` consists of a user-supplied name/value pair.

JSON representation  
---  
      
    
    {
      "name": string,
      "value": string,
      "uint64Value": string
    }  
  
Fields  
---  
`name` |  `string` Name of the property.  
`value` |  `string` Value of the property.  
`uint64Value` |  `string` Value of numeric properties.  
  
## TextAnnotation

`TextAnnotation` contains a structured representation of OCR-extracted text. The hierarchy of an OCR-extracted text structure is like this: 

`TextAnnotation` _- > Page -> Block -> Paragraph -> Word -> Symbol_

Each structural component, starting from Page, might have properties, which describe detected languages, breaks, etc. For more information, refer to the `[TextAnnotation.TextProperty](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse#TextProperty)` message definition that follows. JSON representation  
---  
      
    
    {
      "pages": [
        {
          object ([Page](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse#Page))
        }
      ],
      "text": string
    }  
  
Fields  
---  
`pages[]` |  `object (`[Page](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse#Page)`)` List of pages detected by OCR.  
`text` |  `string` UTF-8 text detected on the pages.  
  
## Page

Detected page from OCR.

JSON representation  
---  
      
    
    {
      "property": {
        object ([TextProperty](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse#TextProperty))
      },
      "width": integer,
      "height": integer,
      "blocks": [
        {
          object ([Block](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse#Block))
        }
      ],
      "confidence": number
    }  
  
Fields  
---  
`property` |  `object (`[TextProperty](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse#TextProperty)`)` Additional information detected on the page.  
`width` |  `integer` Page width. For PDFs the unit is points. For images (including TIFFs) the unit is pixels.  
`height` |  `integer` Page height. For PDFs the unit is points. For images (including TIFFs) the unit is pixels.  
`blocks[]` |  `object (`[Block](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse#Block)`)` List of blocks of text, images etc on this page.  
`confidence` |  `number` Confidence of the OCR results on the page. Range [0, 1].  
  
## TextProperty

Additional information detected on the structural component.

JSON representation  
---  
      
    
    {
      "detectedLanguages": [
        {
          object ([DetectedLanguage](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse#DetectedLanguage))
        }
      ],
      "detectedBreak": {
        object ([DetectedBreak](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse#DetectedBreak))
      }
    }  
  
Fields  
---  
`detectedLanguages[]` |  `object (`[DetectedLanguage](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse#DetectedLanguage)`)` A list of detected languages together with confidence.  
`detectedBreak` |  `object (`[DetectedBreak](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse#DetectedBreak)`)` Detected start or end of a text segment.  
  
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
`languageCode` |  `string` The BCP-47 language code, such as "en-US" or "sr-Latn". For more information, see <https://www.unicode.org/reports/tr35/#Unicode_locale_identifier>.  
`confidence` |  `number` Confidence of detected language. Range [0, 1].  
  
## DetectedBreak

Detected start or end of a structural component.

JSON representation  
---  
      
    
    {
      "type": enum ([BreakType](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse#BreakType)),
      "isPrefix": boolean
    }  
  
Fields  
---  
`type` |  `enum (`[BreakType](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse#BreakType)`)` Detected break type.  
`isPrefix` |  `boolean` True if break prepends the element.  
  
## BreakType

Enum to denote the type of break found. New line, space etc.

Enums  
---  
`UNKNOWN` | Unknown break label type.  
`SPACE` | Regular space.  
`SURE_SPACE` | Sure space (very wide).  
`EOL_SURE_SPACE` | Line-wrapping break.  
`HYPHEN` | End-line hyphen that is not present in text; does not co-occur with `SPACE`, `LEADER_SPACE`, or `LINE_BREAK`.  
`LINE_BREAK` | Line break that ends a paragraph.  
  
## Block

Logical element on the page.

JSON representation  
---  
      
    
    {
      "property": {
        object ([TextProperty](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse#TextProperty))
      },
      "boundingBox": {
        object ([BoundingPoly](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse#BoundingPoly))
      },
      "paragraphs": [
        {
          object ([Paragraph](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse#Paragraph))
        }
      ],
      "blockType": enum ([BlockType](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse#BlockType)),
      "confidence": number
    }  
  
Fields  
---  
`property` |  `object (`[TextProperty](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse#TextProperty)`)` Additional information detected for the block.  
`boundingBox` |  `object (`[BoundingPoly](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse#BoundingPoly)`)` The bounding box for the block. The vertices are in the order of top-left, top-right, bottom-right, bottom-left. When a rotation of the bounding box is detected the rotation is represented as around the top-left corner as defined when the text is read in the 'natural' orientation. For example:

  * when the text is horizontal it might look like:


    
    
        0----1
        |    |
        3----2
    

  * when it's rotated 180 degrees around the top-left corner it becomes:


    
    
        2----3
        |    |
        1----0
    

and the vertex order will still be (0, 1, 2, 3).  
`paragraphs[]` |  `object (`[Paragraph](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse#Paragraph)`)` List of paragraphs in this block (if this blocks is of type text).  
`blockType` |  `enum (`[BlockType](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse#BlockType)`)` Detected block type (text, image etc) for this block.  
`confidence` |  `number` Confidence of the OCR results on the block. Range [0, 1].  
  
## Paragraph

Structural unit of text representing a number of words in certain order.

JSON representation  
---  
      
    
    {
      "property": {
        object ([TextProperty](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse#TextProperty))
      },
      "boundingBox": {
        object ([BoundingPoly](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse#BoundingPoly))
      },
      "words": [
        {
          object ([Word](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse#Word))
        }
      ],
      "confidence": number
    }  
  
Fields  
---  
`property` |  `object (`[TextProperty](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse#TextProperty)`)` Additional information detected for the paragraph.  
`boundingBox` |  `object (`[BoundingPoly](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse#BoundingPoly)`)` The bounding box for the paragraph. The vertices are in the order of top-left, top-right, bottom-right, bottom-left. When a rotation of the bounding box is detected the rotation is represented as around the top-left corner as defined when the text is read in the 'natural' orientation. For example: * when the text is horizontal it might look like: 0----1 | | 3----2 * when it's rotated 180 degrees around the top-left corner it becomes: 2----3 | | 1----0 and the vertex order will still be (0, 1, 2, 3).  
`words[]` |  `object (`[Word](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse#Word)`)` List of all words in this paragraph.  
`confidence` |  `number` Confidence of the OCR results for the paragraph. Range [0, 1].  
  
## Word

A word representation.

JSON representation  
---  
      
    
    {
      "property": {
        object ([TextProperty](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse#TextProperty))
      },
      "boundingBox": {
        object ([BoundingPoly](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse#BoundingPoly))
      },
      "symbols": [
        {
          object ([Symbol](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse#Symbol))
        }
      ],
      "confidence": number
    }  
  
Fields  
---  
`property` |  `object (`[TextProperty](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse#TextProperty)`)` Additional information detected for the word.  
`boundingBox` |  `object (`[BoundingPoly](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse#BoundingPoly)`)` The bounding box for the word. The vertices are in the order of top-left, top-right, bottom-right, bottom-left. When a rotation of the bounding box is detected the rotation is represented as around the top-left corner as defined when the text is read in the 'natural' orientation. For example: * when the text is horizontal it might look like: 0----1 | | 3----2 * when it's rotated 180 degrees around the top-left corner it becomes: 2----3 | | 1----0 and the vertex order will still be (0, 1, 2, 3).  
`symbols[]` |  `object (`[Symbol](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse#Symbol)`)` List of symbols in the word. The order of the symbols follows the natural reading order.  
`confidence` |  `number` Confidence of the OCR results for the word. Range [0, 1].  
  
## Symbol

A single symbol representation.

JSON representation  
---  
      
    
    {
      "property": {
        object ([TextProperty](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse#TextProperty))
      },
      "boundingBox": {
        object ([BoundingPoly](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse#BoundingPoly))
      },
      "text": string,
      "confidence": number
    }  
  
Fields  
---  
`property` |  `object (`[TextProperty](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse#TextProperty)`)` Additional information detected for the symbol.  
`boundingBox` |  `object (`[BoundingPoly](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateImageResponse#BoundingPoly)`)` The bounding box for the symbol. The vertices are in the order of top-left, top-right, bottom-right, bottom-left. When a rotation of the bounding box is detected the rotation is represented as around the top-left corner as defined when the text is read in the 'natural' orientation. For example: * when the text is horizontal it might look like: 0----1 | | 3----2 * when it's rotated 180 degrees around the top-left corner it becomes: 2----3 | | 1----0 and the vertex order will still be (0, 1, 2, 3).  
`text` |  `string` The actual UTF-8 representation of the symbol.  
`confidence` |  `number` Confidence of the OCR results for the symbol. Range [0, 1].  
  
## BlockType

Type of a block (text, image etc) as identified by OCR.

Enums  
---  
`UNKNOWN` | Unknown block type.  
`TEXT` | Regular text block.  
`TABLE` | Table block.  
`PICTURE` | Image block.  
`RULER` | Horizontal/vertical line box.  
`BARCODE` | Barcode block.  
  
## ImageAnnotationContext

If an image was produced from a file (e.g. a PDF), this message gives information about the source of that image.

JSON representation  
---  
      
    
    {
      "uri": string,
      "pageNumber": integer
    }  
  
Fields  
---  
`uri` |  `string` The URI of the file used to produce the image.  
`pageNumber` |  `integer` If the file was a PDF or TIFF, this field gives the page number within the file used to produce the image.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-10 UTC."],[],[]] 
