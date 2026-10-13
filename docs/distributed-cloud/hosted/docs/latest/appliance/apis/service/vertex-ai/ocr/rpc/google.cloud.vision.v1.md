---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1
title: Package google.cloud.vision.v1 \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:16:09.719540+00:00
---

# Package google.cloud.vision.v1  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  Package google.cloud.vision.v1 Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[ImageAnnotator](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.ImageAnnotator)` (interface)
  * `[AnnotateFileRequest](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.AnnotateFileRequest)` (message)
  * `[AnnotateFileResponse](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.AnnotateFileResponse)` (message)
  * `[AnnotateImageRequest](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.AnnotateImageRequest)` (message)
  * `[AnnotateImageResponse](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.AnnotateImageResponse)` (message)
  * `[BatchAnnotateFilesRequest](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.BatchAnnotateFilesRequest)` (message)
  * `[BatchAnnotateFilesResponse](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.BatchAnnotateFilesResponse)` (message)
  * `[BatchAnnotateImagesRequest](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.BatchAnnotateImagesRequest)` (message)
  * `[BatchAnnotateImagesResponse](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.BatchAnnotateImagesResponse)` (message)
  * `[Block](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.Block)` (message)
  * `[Block.BlockType](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.Block.BlockType)` (enum)
  * `[BoundingPoly](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.BoundingPoly)` (message)
  * `[EntityAnnotation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.EntityAnnotation)` (message)
  * `[Feature](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.Feature)` (message)
  * `[Feature.Type](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.Feature.Type)` (enum)
  * `[Image](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.Image)` (message)
  * `[ImageAnnotationContext](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.ImageAnnotationContext)` (message)
  * `[ImageContext](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.ImageContext)` (message)
  * `[InputConfig](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.InputConfig)` (message)
  * `[NormalizedVertex](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.NormalizedVertex)` (message)
  * `[Page](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.Page)` (message)
  * `[Paragraph](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.Paragraph)` (message)
  * `[Property](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.Property)` (message)
  * `[Symbol](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.Symbol)` (message)
  * `[TextAnnotation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.TextAnnotation)` (message)
  * `[TextAnnotation.DetectedBreak](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.TextAnnotation.DetectedBreak)` (message)
  * `[TextAnnotation.DetectedBreak.BreakType](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.TextAnnotation.DetectedBreak.BreakType)` (enum)
  * `[TextAnnotation.DetectedLanguage](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.TextAnnotation.DetectedLanguage)` (message)
  * `[TextAnnotation.TextProperty](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.TextAnnotation.TextProperty)` (message)
  * `[TextDetectionParams](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.TextDetectionParams)` (message)
  * `[Vertex](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.Vertex)` (message)
  * `[Word](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.Word)` (message)



## ImageAnnotator

Service that performs Google Cloud Vision API detection tasks over client images, such as face, landmark, logo, label, and text detection. The ImageAnnotator service returns detected entities from the images.

BatchAnnotateFiles  
---  
` rpc BatchAnnotateFiles(`[BatchAnnotateFilesRequest](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.BatchAnnotateFilesRequest)`) returns (`[BatchAnnotateFilesResponse](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.BatchAnnotateFilesResponse)`) ` Service that performs image detection and annotation for a batch of files. Now only "application/pdf", "image/tiff" and "image/gif" are supported.This service will extract at most 5 (customers can specify which 5 in AnnotateFileRequest.pages) frames (gif) or pages (pdf or tiff) from each file provided and perform detection and annotation for each image extracted.

Authorization Scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-vision`

  
BatchAnnotateImages  
---  
` rpc BatchAnnotateImages(`[BatchAnnotateImagesRequest](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.BatchAnnotateImagesRequest)`) returns (`[BatchAnnotateImagesResponse](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.BatchAnnotateImagesResponse)`) ` Run image detection and annotation for a batch of images.

Authorization Scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-vision`

  
  
## AnnotateFileRequest

A request to annotate one single file, e.g. a PDF, TIFF or GIF file.

Fields  
---  
`input_config` |  ``[InputConfig](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.InputConfig)`` Required. Information about the input file.  
`features[]` |  ``[Feature](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.Feature)`` Required. Requested features.  
`image_context` |  ``[ImageContext](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.ImageContext)`` Additional context that may accompany the image(s) in the file.  
`pages[]` |  `int32` Pages of the file to perform image annotation.Pages starts from 1, we assume the first page of the file is page 1. At most 5 pages are supported per request. Pages can be negative.Page 1 means the first page. Page 2 means the second page. Page -1 means the last page. Page -2 means the second to the last page.If the file is GIF instead of PDF or TIFF, page refers to GIF frames.If this field is empty, by default the service performs image annotation for the first 5 pages of the file.  
  
## AnnotateFileResponse

Response to a single file annotation request. A file may contain one or more images, which individually have their own responses.

Fields  
---  
`input_config` |  ``[InputConfig](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.InputConfig)`` Information about the file for which this response is generated.  
`responses[]` |  ``[AnnotateImageResponse](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.AnnotateImageResponse)`` Individual responses to images found within the file. This field will be empty if the `error` field is set.  
`total_pages` |  `int32` This field gives the total number of pages in the file.  
`error` |  ``[Status](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.rpc#google.rpc.Status)`` If set, represents the error message for the failed request. The `responses` field will not be set in this case.  
  
## AnnotateImageRequest

Request for performing Google Cloud Vision API tasks over a user-provided image, with user-requested features, and with context information.

Fields  
---  
`image` |  ``[Image](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.Image)`` The image to be processed.  
`features[]` |  ``[Feature](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.Feature)`` Requested features.  
`image_context` |  ``[ImageContext](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.ImageContext)`` Additional context that may accompany the image.  
  
## AnnotateImageResponse

Response to an image annotation request.

Fields  
---  
`text_annotations[]` |  ``[EntityAnnotation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.EntityAnnotation)`` If present, text (OCR) detection has completed successfully.  
`full_text_annotation` |  ``[TextAnnotation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.TextAnnotation)`` If present, text (OCR) detection or document (OCR) text detection has completed successfully. This annotation provides the structural hierarchy for the OCR detected text.  
`error` |  ``[Status](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.rpc#google.rpc.Status)`` If set, represents the error message for the operation. Note that filled-in image annotations are guaranteed to be correct, even when `error` is set.  
`context` |  ``[ImageAnnotationContext](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.ImageAnnotationContext)`` If present, contextual information is needed to understand where this image comes from.  
  
## BatchAnnotateFilesRequest

A list of requests to annotate files using the BatchAnnotateFiles API.

Fields  
---  
`requests[]` |  ``[AnnotateFileRequest](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.AnnotateFileRequest)`` Required. The list of file annotation requests. Right now we support only one AnnotateFileRequest in BatchAnnotateFilesRequest.  
`parent` |  `string` Optional. Target project and location to make a call.Format: `projects/{project-id}/locations/{location-id}`.If no parent is specified, a region will be chosen automatically.Supported location-ids: `us`: USA country only, `asia`: East asia areas, like Japan, Taiwan, `eu`: The European Union.Example: `projects/project-A/locations/eu`.  
  
## BatchAnnotateFilesResponse

A list of file annotation responses.

Fields  
---  
`responses[]` |  ``[AnnotateFileResponse](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.AnnotateFileResponse)`` The list of file annotation responses, each response corresponding to each AnnotateFileRequest in BatchAnnotateFilesRequest.  
  
## BatchAnnotateImagesRequest

Multiple image annotation requests are batched into a single service call.

Fields  
---  
`requests[]` |  ``[AnnotateImageRequest](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.AnnotateImageRequest)`` Required. Individual image annotation requests for this batch.  
`parent` |  `string` Optional. Target project and location to make a call.Format: `projects/{project-id}/locations/{location-id}`.If no parent is specified, a region will be chosen automatically.Supported location-ids: `us`: USA country only, `asia`: East asia areas, like Japan, Taiwan, `eu`: The European Union.Example: `projects/project-A/locations/eu`.  
  
## BatchAnnotateImagesResponse

Response to a batch image annotation request.

Fields  
---  
`responses[]` |  ``[AnnotateImageResponse](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.AnnotateImageResponse)`` Individual responses to image annotation requests within the batch.  
  
## Block

Logical element on the page.

Fields  
---  
`property` |  ``[TextProperty](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.TextAnnotation.TextProperty)`` Additional information detected for the block.  
`bounding_box` |  ``[BoundingPoly](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.BoundingPoly)`` The bounding box for the block. The vertices are in the order of top-left, top-right, bottom-right, bottom-left. When a rotation of the bounding box is detected the rotation is represented as around the top-left corner as defined when the text is read in the 'natural' orientation. For example:

  * when the text is horizontal it might look like:


    
    
        0----1
        |    |
        3----2
    

  * when it's rotated 180 degrees around the top-left corner it becomes:


    
    
        2----3
        |    |
        1----0
    

and the vertex order will still be (0, 1, 2, 3).  
`paragraphs[]` |  ``[Paragraph](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.Paragraph)`` List of paragraphs in this block (if this blocks is of type text).  
`block_type` |  ``[BlockType](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.Block.BlockType)`` Detected block type (text, image etc) for this block.  
`confidence` |  `float` Confidence of the OCR results on the block. Range [0, 1].  
  
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
  
## BoundingPoly

A bounding polygon for the detected image annotation.

Fields  
---  
`vertices[]` |  ``[Vertex](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.Vertex)`` The bounding polygon vertices.  
`normalized_vertices[]` |  ``[NormalizedVertex](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.NormalizedVertex)`` The bounding polygon normalized vertices.  
  
## EntityAnnotation

Set of detected entity features.

Fields  
---  
`mid` |  `string` Opaque entity ID. Some IDs may be available in [Google Knowledge Graph Search API](https://developers.google.com/knowledge-graph/).  
`locale` |  `string` The language code for the locale in which the entity textual `description` is expressed.  
`description` |  `string` Entity textual description, expressed in its `locale` language.  
`score` |  `float` Overall score of the result. Range [0, 1].  
`confidence  
**(deprecated)**` |  `float` This item is deprecated!**Deprecated. Use`score` instead.** The accuracy of the entity detection in an image. For example, for an image in which the "Eiffel Tower" entity is detected, this field represents the confidence that there is a tower in the query image. Range [0, 1].  
`topicality` |  `float` The relevancy of the ICA (Image Content Annotation) label to the image. For example, the relevancy of "tower" is likely higher to an image containing the detected "Eiffel Tower" than to an image containing a detected distant towering building, even though the confidence that there is a tower in each image may be the same. Range [0, 1].  
`bounding_poly` |  ``[BoundingPoly](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.BoundingPoly)`` Image region to which this entity belongs. Not produced for `LABEL_DETECTION` features.  
`properties[]` |  ``[Property](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.Property)`` Some entities may have optional user-supplied `Property` (name/value) fields, such a score or string that qualifies the entity.  
  
## Feature

The type of Google Cloud Vision API detection to perform, and the maximum number of results to return for that type. Multiple `Feature` objects can be specified in the `features` list.

Fields  
---  
`type` |  ``[Type](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.Feature.Type)`` The feature type.  
`model` |  `string` Model to use for the feature. Supported values: "builtin/stable" (the default if unset) and "builtin/latest". `DOCUMENT_TEXT_DETECTION` and `TEXT_DETECTION` also support "builtin/weekly" for the bleeding edge release updated weekly.  
  
## Type

Type of Google Cloud Vision API feature to be extracted.

Enums  
---  
`TYPE_UNSPECIFIED` | Unspecified feature type.  
`TEXT_DETECTION` | Run text detection / optical character recognition (OCR). Text detection is optimized for areas of text within a larger image; if the image is a document, use `DOCUMENT_TEXT_DETECTION` instead.  
`DOCUMENT_TEXT_DETECTION` | Run dense text document OCR. Takes precedence when both `DOCUMENT_TEXT_DETECTION` and `TEXT_DETECTION` are present.  
  
## Image

Client image to perform Google Cloud Vision API tasks over.

Fields  
---  
`content` |  `bytes` Image content, represented as a stream of bytes. Note: As with all `bytes` fields, protobuffers use a pure binary representation, whereas JSON representations use base64.Currently, this field only works for BatchAnnotateImages requests.  
  
## ImageAnnotationContext

If an image was produced from a file (e.g. a PDF), this message gives information about the source of that image.

Fields  
---  
`uri` |  `string` The URI of the file used to produce the image.  
`page_number` |  `int32` If the file was a PDF or TIFF, this field gives the page number within the file used to produce the image.  
  
## ImageContext

Image context and/or feature-specific parameters.

Fields  
---  
`language_hints[]` |  `string` List of languages to use for TEXT_DETECTION. In most cases, an empty value yields the best results since it enables automatic language detection. For languages based on the Latin alphabet, setting `language_hints` is not needed. In rare cases, when the language of the text in the image is known, setting a hint will help get better results (although it will be a significant hindrance if the hint is wrong). Text detection returns an error if one or more of the specified languages is not one of the [supported languages](https://cloud.google.com/vision/docs/languages).  
`text_detection_params` |  ``[TextDetectionParams](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.TextDetectionParams)`` Parameters for text detection and document text detection.  
  
## InputConfig

The desired input location and metadata.

Fields  
---  
`content` |  `bytes` File content, represented as a stream of bytes. Note: As with all `bytes` fields, protobuffers use a pure binary representation, whereas JSON representations use base64.Currently, this field only works for BatchAnnotateFiles requests.  
`mime_type` |  `string` The type of the file. Currently only "application/pdf", "image/tiff" and "image/gif" are supported. Wildcards are not supported.  
  
## NormalizedVertex

A vertex represents a 2D point in the image. NOTE: the normalized vertex coordinates are relative to the original image and range from 0 to 1.

Fields  
---  
`x` |  `float` X coordinate.  
`y` |  `float` Y coordinate.  
  
## Page

Detected page from OCR.

Fields  
---  
`property` |  ``[TextProperty](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.TextAnnotation.TextProperty)`` Additional information detected on the page.  
`width` |  `int32` Page width. For PDFs the unit is points. For images (including TIFFs) the unit is pixels.  
`height` |  `int32` Page height. For PDFs the unit is points. For images (including TIFFs) the unit is pixels.  
`blocks[]` |  ``[Block](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.Block)`` List of blocks of text, images etc on this page.  
`confidence` |  `float` Confidence of the OCR results on the page. Range [0, 1].  
  
## Paragraph

Structural unit of text representing a number of words in certain order.

Fields  
---  
`property` |  ``[TextProperty](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.TextAnnotation.TextProperty)`` Additional information detected for the paragraph.  
`bounding_box` |  ``[BoundingPoly](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.BoundingPoly)`` The bounding box for the paragraph. The vertices are in the order of top-left, top-right, bottom-right, bottom-left. When a rotation of the bounding box is detected the rotation is represented as around the top-left corner as defined when the text is read in the 'natural' orientation. For example: * when the text is horizontal it might look like: 0----1 | | 3----2 * when it's rotated 180 degrees around the top-left corner it becomes: 2----3 | | 1----0 and the vertex order will still be (0, 1, 2, 3).  
`words[]` |  ``[Word](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.Word)`` List of all words in this paragraph.  
`confidence` |  `float` Confidence of the OCR results for the paragraph. Range [0, 1].  
  
## Property

A `Property` consists of a user-supplied name/value pair.

Fields  
---  
`name` |  `string` Name of the property.  
`value` |  `string` Value of the property.  
`uint64_value` |  `uint64` Value of numeric properties.  
  
## Symbol

A single symbol representation.

Fields  
---  
`property` |  ``[TextProperty](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.TextAnnotation.TextProperty)`` Additional information detected for the symbol.  
`bounding_box` |  ``[BoundingPoly](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.BoundingPoly)`` The bounding box for the symbol. The vertices are in the order of top-left, top-right, bottom-right, bottom-left. When a rotation of the bounding box is detected the rotation is represented as around the top-left corner as defined when the text is read in the 'natural' orientation. For example: * when the text is horizontal it might look like: 0----1 | | 3----2 * when it's rotated 180 degrees around the top-left corner it becomes: 2----3 | | 1----0 and the vertex order will still be (0, 1, 2, 3).  
`text` |  `string` The actual UTF-8 representation of the symbol.  
`confidence` |  `float` Confidence of the OCR results for the symbol. Range [0, 1].  
  
## TextAnnotation

`TextAnnotation` contains a structured representation of OCR-extracted text. The hierarchy of an OCR-extracted text structure is like this: 

`TextAnnotation` _- > Page -> Block -> Paragraph -> Word -> Symbol_

Each structural component, starting from Page, might have properties, which describe detected languages, breaks, etc. For more details, refer to the `[TextAnnotation.TextProperty](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.TextAnnotation.TextProperty)` message definition that follows. Fields  
---  
`pages[]` |  ``[Page](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.Page)`` List of pages detected by OCR.  
`text` |  `string` UTF-8 text detected on the pages.  
  
## DetectedBreak

Detected start or end of a structural component.

Fields  
---  
`type` |  ``[BreakType](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.TextAnnotation.DetectedBreak.BreakType)`` Detected break type.  
`is_prefix` |  `bool` True if break prepends the element.  
  
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
  
## DetectedLanguage

Detected language for a structural component.

Fields  
---  
`language_code` |  `string` The BCP-47 language code, such as "en-US" or "sr-Latn". For more information, see <https://www.unicode.org/reports/tr35/#Unicode_locale_identifier>.  
`confidence` |  `float` Confidence of detected language. Range [0, 1].  
  
## TextProperty

Additional information detected on the structural component.

Fields  
---  
`detected_languages[]` |  ``[DetectedLanguage](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.TextAnnotation.DetectedLanguage)`` A list of detected languages together with confidence.  
`detected_break` |  ``[DetectedBreak](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.TextAnnotation.DetectedBreak)`` Detected start or end of a text segment.  
  
## TextDetectionParams

Parameters for text detections. This is used to control TEXT_DETECTION and DOCUMENT_TEXT_DETECTION features.

Fields  
---  
`enable_text_detection_confidence_score` |  `bool` By default, Cloud Vision API only includes confidence score for DOCUMENT_TEXT_DETECTION result. Set the flag to true to include confidence score for TEXT_DETECTION as well.  
`advanced_ocr_options[]` |  `string` A list of advanced OCR options to fine-tune OCR behavior.  
  
## Vertex

A vertex represents a 2D point in the image. NOTE: the vertex coordinates are in the same scale as the original image.

Fields  
---  
`x` |  `int32` X coordinate.  
`y` |  `int32` Y coordinate.  
  
## Word

A word representation.

Fields  
---  
`property` |  ``[TextProperty](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.TextAnnotation.TextProperty)`` Additional information detected for the word.  
`bounding_box` |  ``[BoundingPoly](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.BoundingPoly)`` The bounding box for the word. The vertices are in the order of top-left, top-right, bottom-right, bottom-left. When a rotation of the bounding box is detected the rotation is represented as around the top-left corner as defined when the text is read in the 'natural' orientation. For example: * when the text is horizontal it might look like: 0----1 | | 3----2 * when it's rotated 180 degrees around the top-left corner it becomes: 2----3 | | 1----0 and the vertex order will still be (0, 1, 2, 3).  
`symbols[]` |  ``[Symbol](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rpc/google.cloud.vision.v1#google.cloud.vision.v1.Symbol)`` List of symbols in the word. The order of the symbols follows the natural reading order.  
`confidence` |  `float` Confidence of the OCR results for the word. Range [0, 1].  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-11 UTC."],[],[]] 
