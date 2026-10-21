---
url: https://docs.cloud.google.com/storage/docs/object-enrichments/models/
title: Supported models and schemas \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:49:05.524736+00:00
---

# Supported models and schemas  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/object-enrichments/models/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Supported models and schemas Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

When you configure object enrichments, you choose which machine learning models analyze your stored objects. Each model evaluates eligible images or PDF documents and attaches structured metadata directly to your Cloud Storage objects.

This page describes each supported model, its eligibility requirements, and its output schema to help you parse and query enrichment metadata in BigQuery or through an API.

## Relationship between models and object enrichments

You activate models by creating a [feature configuration (`FeatureConfig`)](https://docs.cloud.google.com/storage/docs/json_api/v1/featureConfigs) that specifies which buckets to scan and which models to run. During asynchronous processing, Cloud Storage evaluates eligible objects by using your chosen models and generates structured JSON metadata called object enrichments.

Each model produces a dedicated JSON payload that Cloud Storage attaches directly to the object as a Google-managed object context under the `contexts.custom` property. A unique context key prefixed with `google:annotation:` identifies each payload.

Depending on your workflow, you can consume this metadata in two ways:

  * **Inspect individual objects** : Retrieve enrichments for a specific object by using object APIs, such as the [`viewFullContext` method](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/viewFullContext) ([Preview](https://docs.cloud.google.com/products#product-launch-stages)).
  * **Analyze at scale** : Query enriched metadata across all objects in a bucket by using [Storage Insights datasets](https://docs.cloud.google.com/storage/docs/insights/datasets) and standard SQL in [BigQuery](https://docs.cloud.google.com/storage/docs/object-enrichments/analyze-bigquery).



## Face detection

Use the `face-detector` model to detect human faces in stored images. The model detects bounding polygons for entire heads and individual faces, and locates 36 facial landmarks, such as eyes, nose, and mouth. It also calculates head orientation angles, such as roll, pan, and tilt, and assesses emotional expression likelihoods.

### Model details

  * **Model name** : `face-detector`
  * **Context key** : `google:annotation:face-detector-v1`
  * **Eligible objects** : Image objects 20 MiB or smaller with a supported `Content-Type` of `BMP`, `GIF`, `ICO`, `JPEG`, `PNG`, `TIFF`, or `WEBP`.



### Output schema

The model outputs a JSON object containing `modelName`, `modelVersion`, and a `faceAnnotationGroup` with an array of `faceAnnotations`. If model execution fails, the JSON object contains an `error` object instead of `faceAnnotationGroup`.

Field | Type | Range | Description  
---|---|---|---  
`modelName` | `string` | N/A | The name of the machine learning model that generated this enrichment.  
`modelVersion` | `string` | N/A | The version of the machine learning model that generated this enrichment.  
`faceAnnotationGroup` | `object` | N/A | Top-level container object for face detection enrichments. Present when model execution succeeds.  
`faceAnnotationGroup.faceAnnotations[]` | `array` | N/A | A list of detected faces in the image.  
`faceAnnotationGroup.faceAnnotations[].boundingPoly` | `object` | N/A | The `BoundingPoly` enclosing the entire head and face, scaled to original image dimensions.  
`faceAnnotationGroup.faceAnnotations[].faceDetectionBoundingPoly` | `object` | N/A | The `BoundingPoly` for face detection. Tighter than `boundingPoly`, enclosing only the skin and visible facial features.  
`faceAnnotationGroup.faceAnnotations[].landmarks[]` | `array` | N/A | A list of detected `FaceLandmark` objects representing specific facial features.  
`faceAnnotationGroup.faceAnnotations[].rollAngle` | `number` | `-180` to `180` | Clockwise or counter-clockwise rotation of the face, in degrees.  
`faceAnnotationGroup.faceAnnotations[].panAngle` | `number` | `-180` to `180` | Horizontal angle the face is pointing left or right, in degrees.  
`faceAnnotationGroup.faceAnnotations[].tiltAngle` | `number` | `-180` to `180` | Vertical pitch angle the face is pointing up or down, in degrees.  
`faceAnnotationGroup.faceAnnotations[].detectionConfidence` | `number` | `0` to `1` (0% to 100%) | Confidence score for the overall face detection.  
`faceAnnotationGroup.faceAnnotations[].landmarkingConfidence` | `number` | `0` to `1` (0% to 100%) | Confidence score for facial landmark positioning.  
`faceAnnotationGroup.faceAnnotations[].joyProbability` | `number` | `0` to `1` (0% to 100%) | Likelihood that the face expresses joy.  
`faceAnnotationGroup.faceAnnotations[].sorrowProbability` | `number` | `0` to `1` (0% to 100%) | Likelihood that the face expresses sorrow.  
`faceAnnotationGroup.faceAnnotations[].angerProbability` | `number` | `0` to `1` (0% to 100%) | Likelihood that the face expresses anger.  
`faceAnnotationGroup.faceAnnotations[].surpriseProbability` | `number` | `0` to `1` (0% to 100%) | Likelihood that the face expresses surprise.  
`faceAnnotationGroup.faceAnnotations[].underExposedProbability` | `number` | `0` to `1` (0% to 100%) | Likelihood that the face in the image is underexposed.  
`faceAnnotationGroup.faceAnnotations[].blurredProbability` | `number` | `0` to `1` (0% to 100%) | Likelihood that the face in the image is blurred.  
`faceAnnotationGroup.faceAnnotations[].headwearProbability` | `number` | `0` to `1` (0% to 100%) | Likelihood that the person is wearing headwear, such as a hat or cap.  
`error` | `object` | N/A | A `google.rpc.Status` object containing `code` and `message`. Populated only when model execution fails.  
  
#### BoundingPoly

The `BoundingPoly` object represents a bounding polygon enclosing a detected image feature.

Field | Type | Range | Description  
---|---|---|---  
`vertices[]` | `array` | N/A | Bounding polygon coordinates using absolute pixel `Vertex` objects.  
`normalizedVertices[]` | `array` | N/A | Bounding polygon coordinates using relative `NormalizedVertex` objects, scaled from `0` to `1`.  
  
#### Vertex

The `Vertex` object represents a 2D coordinate point scaled to the original image dimensions.

Field | Type | Range | Description  
---|---|---|---  
`x` | `integer` | `0` or greater | Horizontal X coordinate, in pixels from the left edge.  
`y` | `integer` | `0` or greater | Vertical Y coordinate, in pixels from the top edge.  
  
#### NormalizedVertex

The `NormalizedVertex` object represents a 2D coordinate point expressed as a ratio relative to original image dimensions.

Field | Type | Range | Description  
---|---|---|---  
`x` | `number` | `0` to `1` | Horizontal X coordinate relative to image width, where `0.0` is the left edge and `1.0` is the right edge.  
`y` | `number` | `0` to `1` | Vertical Y coordinate relative to image height, where `0.0` is the top edge and `1.0` is the bottom edge.  
  
#### FaceLandmark

The `FaceLandmark` object represents a specific facial landmark detected within a face.

Field | Type | Range | Description  
---|---|---|---  
`type` | `enum` | See Landmark type | The specific facial landmark detected.  
`position` | `object` | N/A | The 3D `Position` of the landmark.  
  
#### Landmark type

The model recognizes 36 specific facial landmarks:

  * `TYPE_UNSPECIFIED`
  * `LEFT_EYE`
  * `RIGHT_EYE`
  * `LEFT_OF_LEFT_EYEBROW`
  * `RIGHT_OF_LEFT_EYEBROW`
  * `LEFT_OF_RIGHT_EYEBROW`
  * `RIGHT_OF_RIGHT_EYEBROW`
  * `MIDPOINT_BETWEEN_EYES`
  * `NOSE_TIP`
  * `UPPER_LIP`
  * `LOWER_LIP`
  * `MOUTH_LEFT`
  * `MOUTH_RIGHT`
  * `MOUTH_CENTER`
  * `NOSE_BOTTOM_RIGHT`
  * `NOSE_BOTTOM_LEFT`
  * `NOSE_BOTTOM_CENTER`
  * `LEFT_EYE_TOP_BOUNDARY`
  * `LEFT_EYE_RIGHT_CORNER`
  * `LEFT_EYE_BOTTOM_BOUNDARY`
  * `LEFT_EYE_LEFT_CORNER`
  * `RIGHT_EYE_TOP_BOUNDARY`
  * `RIGHT_EYE_RIGHT_CORNER`
  * `RIGHT_EYE_BOTTOM_BOUNDARY`
  * `RIGHT_EYE_LEFT_CORNER`
  * `LEFT_EYEBROW_UPPER_MIDPOINT`
  * `RIGHT_EYEBROW_UPPER_MIDPOINT`
  * `LEFT_EAR_TRAGION`
  * `RIGHT_EAR_TRAGION`
  * `LEFT_EYE_PUPIL`
  * `RIGHT_EYE_PUPIL`
  * `FOREHEAD_GLABELLA`
  * `CHIN_GNATHION`
  * `CHIN_LEFT_GONION`
  * `CHIN_RIGHT_GONION`
  * `LEFT_CHEEK_CENTER`
  * `RIGHT_CHEEK_CENTER`



#### Position

The `Position` object represents the 3D coordinates of a facial landmark.

Field | Type | Range | Description  
---|---|---|---  
`x` | `number` | N/A | Horizontal X coordinate.  
`y` | `number` | N/A | Vertical Y coordinate.  
`z` | `number` | N/A | Depth coordinate relative to the face plane, where smaller values are closer to the camera.  
  
### Sample output
    
    
    {
      "modelName": "face-detector",
      "modelVersion": "v1",
      "faceAnnotationGroup": {
        "faceAnnotations": [
          {
            "boundingPoly": {
              "vertices": [
                { "x": 1079, "y": 148 },
                { "x": 2152, "y": 148 },
                { "x": 2152, "y": 1396 },
                { "x": 1079, "y": 1396 }
              ],
              "normalizedVertices": [
                { "x": 0.35, "y": 0.12 },
                { "x": 0.70, "y": 0.12 },
                { "x": 0.70, "y": 0.95 },
                { "x": 0.35, "y": 0.95 }
              ]
            },
            "faceDetectionBoundingPoly": {
              "vertices": [
                { "x": 1190, "y": 427 },
                { "x": 2037, "y": 427 },
                { "x": 2037, "y": 1285 },
                { "x": 1190, "y": 1285 }
              ]
            },
            "landmarks": [
              {
                "type": "LEFT_EYE",
                "position": { "x": 1368.8, "y": 737.6, "z": 0.0016 }
              },
              {
                "type": "RIGHT_EYE",
                "position": { "x": 1659.2, "y": 755.1, "z": -116.4 }
              }
            ],
            "rollAngle": 1.959,
            "panAngle": -21.954,
            "tiltAngle": -2.267,
            "detectionConfidence": 0.98,
            "landmarkingConfidence": 0.61,
            "joyProbability": 0.18,
            "headwearProbability": 0.80
          }
        ]
      }
    }
    

## Object detection

Use the `object-detector` model to detect and track multiple distinct objects in an image. For each identified object, the model provides an entity name, a Knowledge Graph entity ID (`knowledgeGraphId`), a confidence score, and bounding coordinates.

### Model details

  * **Model name** : `object-detector`
  * **Context key** : `google:annotation:object-detector-v1`
  * **Eligible objects** : Image objects 20 MiB or smaller with a supported `Content-Type` of `BMP`, `GIF`, `ICO`, `JPEG`, `PNG`, `TIFF`, or `WEBP`.



### Output schema

The model outputs a JSON object containing `modelName`, `modelVersion`, and an `objectAnnotationGroup` with an array of `objectAnnotations`. If model execution fails, the JSON object contains an `error` object instead of `objectAnnotationGroup`.

Field | Type | Range | Description  
---|---|---|---  
`modelName` | `string` | N/A | The name of the machine learning model that generated this enrichment.  
`modelVersion` | `string` | N/A | The version of the machine learning model that generated this enrichment.  
`objectAnnotationGroup` | `object` | N/A | Top-level container object for object detection enrichments. Present when model execution succeeds.  
`objectAnnotationGroup.objectAnnotations[]` | `array` | N/A | A list of detected objects in the image.  
`objectAnnotationGroup.objectAnnotations[].knowledgeGraphId` | `string` | N/A | The Google Knowledge Graph entity ID for the detected object.  
`objectAnnotationGroup.objectAnnotations[].name` | `string` | N/A | The name or label of the detected object, such as `"Person"` or `"Chair"`.  
`objectAnnotationGroup.objectAnnotations[].score` | `number` | `0` to `1` (0% to 100%) | Confidence score for the object detection.  
`objectAnnotationGroup.objectAnnotations[].boundingPoly` | `object` | N/A | The `BoundingPoly` around the object, containing pixel coordinates (`vertices`) and normalized coordinates (`normalizedVertices`).  
`error` | `object` | N/A | A `google.rpc.Status` object containing `code` and `message`. Populated only when model execution fails.  
  
### Sample output
    
    
    {
      "modelName": "object-detector",
      "modelVersion": "v1",
      "objectAnnotationGroup": {
        "objectAnnotations": [
          {
            "knowledgeGraphId": "/m/01g317",
            "name": "Person",
            "score": 0.89,
            "boundingPoly": {
              "normalizedVertices": [
                { "x": 0.1, "y": 0.15 },
                { "x": 0.2, "y": 0.15 },
                { "x": 0.2, "y": 0.3 },
                { "x": 0.1, "y": 0.3 }
              ]
            }
          }
        ]
      }
    }
    

## General image labeling

Use the `label-detector` model to generate descriptive labels, keywords, and broad semantic categories for images. The model identifies general entities, scenery, activities, and locations, such as `Landscape`, `Urban`, or `Night`, making your visual assets searchable and catalogable.

### Model details

  * **Model name** : `label-detector`
  * **Context key** : `google:annotation:label-detector-v1`
  * **Eligible objects** : Image objects 20 MiB or smaller with a supported `Content-Type` of `BMP`, `GIF`, `ICO`, `JPEG`, `PNG`, `TIFF`, or `WEBP`.



### Output schema

The model outputs a JSON object containing `modelName`, `modelVersion`, and a `labelAnnotationGroup` with an array of `labelAnnotations`. If model execution fails, the JSON object contains an `error` object instead of `labelAnnotationGroup`.

Field | Type | Range | Description  
---|---|---|---  
`modelName` | `string` | N/A | The name of the machine learning model that generated this enrichment.  
`modelVersion` | `string` | N/A | The version of the machine learning model that generated this enrichment.  
`labelAnnotationGroup` | `object` | N/A | Top-level container object for image label enrichments. Present when model execution succeeds.  
`labelAnnotationGroup.labelAnnotations[]` | `array` | N/A | A list of detected labels and categories.  
`labelAnnotationGroup.labelAnnotations[].knowledgeGraphId` | `string` | N/A | The Google Knowledge Graph entity ID for the label.  
`labelAnnotationGroup.labelAnnotations[].description` | `string` | N/A | Textual description or label name for the detected entity.  
`labelAnnotationGroup.labelAnnotations[].score` | `number` | `0` to `1` (0% to 100%) | Confidence score for the label.  
`labelAnnotationGroup.labelAnnotations[].topicality` | `number` | `0` to `1` (0% to 100%) | Relevancy of the label to the primary subject of the image, where higher scores indicate greater prominence.  
`error` | `object` | N/A | A `google.rpc.Status` object containing `code` and `message`. Populated only when model execution fails.  
  
### Sample output
    
    
    {
      "modelName": "label-detector",
      "modelVersion": "v1",
      "labelAnnotationGroup": {
        "labelAnnotations": [
          {
            "knowledgeGraphId": "/m/01d74z",
            "description": "Night",
            "score": 0.92,
            "topicality": 0.19
          }
        ]
      }
    }
    

## Explicit content detection

Use the `content-safety` model to screen uploaded images for sensitive, explicit, or inappropriate content. The model evaluates images against Google safety policies. It assesses the likelihood of adult, violent, and other sensitive material to help you automate content moderation workflows.

### Model details

  * **Model name** : `content-safety`
  * **Context key** : `google:annotation:content-safety-v1`
  * **Eligible objects** : Image objects 20 MiB or smaller with a supported `Content-Type` of `BMP`, `GIF`, `ICO`, `JPEG`, `PNG`, `TIFF`, or `WEBP`.



### Output schema

The model outputs a JSON object containing `modelName`, `modelVersion`, and a `contentSafetyAnnotation` object with likelihood ratings. If model execution fails, the JSON object contains an `error` object instead of `contentSafetyAnnotation`.

Field | Type | Values / Range | Description  
---|---|---|---  
`modelName` | `string` | N/A | The name of the machine learning model that generated this enrichment.  
`modelVersion` | `string` | N/A | The version of the machine learning model that generated this enrichment.  
`contentSafetyAnnotation` | `object` | N/A | Top-level container object for content analysis results. Present when model execution succeeds.  
`contentSafetyAnnotation.adultContentLikelihood` | `string` | `VERY_UNLIKELY`, `UNLIKELY`, `POSSIBLE`, `LIKELY`, `VERY_LIKELY` | Likelihood that the image contains adult content.  
`contentSafetyAnnotation.violentContentLikelihood` | `string` | `VERY_UNLIKELY`, `UNLIKELY`, `POSSIBLE`, `LIKELY`, `VERY_LIKELY` | Likelihood that the image depicts violence.  
`error` | `object` | N/A | A `google.rpc.Status` object containing `code` and `message`. Populated only when model execution fails.  
  
### Sample output
    
    
    {
      "modelName": "content-safety",
      "modelVersion": "v1",
      "contentSafetyAnnotation": {
        "adultContentLikelihood": "VERY_UNLIKELY",
        "violentContentLikelihood": "UNLIKELY"
      }
    }
    

## PDF classification

Use the `pdf-classification` model to automatically categorize PDF documents based on their textual and visual structure. The model assigns standardized hierarchical categories for business, industry, and topics. These categories help you organize large document collections, ground generative AI retrieval, and route documents to downstream workflows.

### Model details

  * **Model name** : `pdf-classification`
  * **Context key** : `google:annotation:pdf-classification-v1`
  * **Eligible objects** : PDF document objects 20 MiB or smaller with a `Content-Type` of `application/pdf`.



### Output schema

The model outputs a JSON object containing `modelName`, `modelVersion`, and a `pdfClassificationCategoryList` with an array of classified `categories`. If model execution fails, the JSON object contains an `error` object instead of `pdfClassificationCategoryList`.

Field | Type | Range | Description  
---|---|---|---  
`modelName` | `string` | N/A | The name of the machine learning model that generated this enrichment.  
`modelVersion` | `string` | N/A | The version of the machine learning model that generated this enrichment.  
`pdfClassificationCategoryList` | `object` | N/A | Top-level container object for PDF classification results. Present when model execution succeeds.  
`pdfClassificationCategoryList.categories[]` | `array` | N/A | A list of detected classification categories.  
`pdfClassificationCategoryList.categories[].label` | `string` | See [PDF classification categories](https://docs.cloud.google.com/storage/docs/object-enrichments/pdf-categories) | The hierarchical category path, such as `"/Finance/Accounting & Auditing/Tax Preparation & Planning"`.  
`pdfClassificationCategoryList.categories[].score` | `number` | `0` to `1` (0% to 100%) | Confidence score for the assigned category.  
`error` | `object` | N/A | A `google.rpc.Status` object containing `code` and `message`. Populated only when model execution fails.  
  
#### Supported categories

The `pdf-classification` model assigns standardized hierarchical content categories to PDF documents.

Categories are structured hierarchically with forward slashes (`/`) separating category depth. They begin with a broad top-level vertical and narrow to specific subcategories:

  * **Top-level verticals** : Broad subject domains, such as `/Finance`, `/Law & Government`, or `/Computers & Electronics`.
  * **Subcategories** : Specific subjects within a vertical, such as `/Finance/Accounting & Auditing/Tax Preparation & Planning`.
  * **`/Other` subcategories**: Categories for content that aligns with the parent category but doesn't fit into any specific child subcategory.



If a document covers multiple distinct topics, the model can assign multiple high-confidence categories to a single PDF object.

##### Top-level categories

The model classifies PDF documents across 27 top-level categories:

  * `/Adult`
  * `/Arts & Entertainment`
  * `/Autos & Vehicles`
  * `/Beauty & Fitness`
  * `/Books & Literature`
  * `/Business & Industrial`
  * `/Computers & Electronics`
  * `/Finance`
  * `/Food & Drink`
  * `/Games`
  * `/Health`
  * `/Hobbies & Leisure`
  * `/Home & Garden`
  * `/Internet & Telecom`
  * `/Jobs & Education`
  * `/Law & Government`
  * `/News`
  * `/Online Communities`
  * `/People & Society`
  * `/Pets & Animals`
  * `/Real Estate`
  * `/Reference`
  * `/Science`
  * `/Sensitive Subjects`
  * `/Shopping`
  * `/Sports`
  * `/Travel & Transportation`



Subcategories follow the hierarchical path `/Top-Level-Vertical/Subcategory`, with optional deeper levels, under these top-level categories. For the complete list of all supported category paths, see [PDF classification categories](https://docs.cloud.google.com/storage/docs/object-enrichments/pdf-categories).

### Sample output
    
    
    {
      "modelName": "pdf-classification",
      "modelVersion": "v1",
      "pdfClassificationCategoryList": {
        "categories": [
          {
            "label": "/Finance/Accounting & Auditing/Tax Preparation & Planning",
            "score": 0.85
          },
          {
            "label": "/Business & Industrial/Printing & Publishing/Document & Printing Services",
            "score": 0.25
          }
        ]
      }
    }
    

## What's next

  * [Read about object enrichments](https://docs.cloud.google.com/storage/docs/object-enrichments/overview).
  * [Configure object enrichments](https://docs.cloud.google.com/storage/docs/object-enrichments/configure-object-enrichments).
  * [Manage object enrichments](https://docs.cloud.google.com/storage/docs/object-enrichments/manage-object-enrichments).
  * [Analyze object enrichments in BigQuery](https://docs.cloud.google.com/storage/docs/object-enrichments/analyze-bigquery).
  * [Review the `featureConfigs` JSON API resource](https://docs.cloud.google.com/storage/docs/json_api/v1/featureConfigs).
  * [Troubleshoot object enrichments issues](https://docs.cloud.google.com/storage/docs/storage-intelligence/troubleshooting#object-enrichments-errors).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
