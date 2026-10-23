---
url: https://docs.cloud.google.com/vision/docs/features-list/
title: Features list \u00a0|\u00a0 Cloud Vision API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:24:51.661301+00:00
---

# Features list  |  Cloud Vision API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/docs/features-list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Vision API ](https://docs.cloud.google.com/vision/docs)
  * [ Guides ](https://docs.cloud.google.com/vision/docs/features-list)



Send feedback 

#  Features list Stay organized with collections  Save and categorize content based on your preferences. 

Vision API lets you use the following features:

All feature types  
---  
  
### [Text detection](https://docs.cloud.google.com/vision/docs/ocr)

![Road sign image](https://docs.cloud.google.com/static/vision/docs/images/sign_text.png) | 

  * Optical character recognition (OCR) for an image; text recognition and conversion to machine-coded text. Identifies and extracts UTF-8 text in an image.
  * **Images** : Optimized for _**sparse**_ areas of text within a larger image.
  * **Response** : Returns both a list of words identified with text, bounding boxes, and `textAnnotations`, as well as the structural hierarchy for the OCR detected text (`fullTextAnnotation`).
    * Hierarchy of extracted text structure: 
      * TextAnnotation -> Page -> Block -> Paragraph -> Word -> Symbol.
      * Each structural component from Page on may further have their own properties such as detected languages, breaks, etc.
  * **Languages supported** : Works with currently [supported, mapped, and experimental](https://docs.cloud.google.com/vision/docs/languages) languages.
  * Feature enum value: `TEXT_DETECTION`.

  
  
### [Document text detection (dense text / handwriting)](https://docs.cloud.google.com/vision/docs/pdf)

![Dense image with annotations](https://docs.cloud.google.com/static/vision/docs/images/document_text_highlighted.png)![handwriting image](https://docs.cloud.google.com/static/vision/docs/images/detect_handwriting_OCR-detect-handwriting_SMALL.png) | 

  * Optical character recognition (OCR) for a file (PDF/TIFF) or dense text image; dense text recognition and conversion to machine-coded text. 
  * **Files** : Optimized for document files (PDF/TIFF). 
  * **Images** : Optimized for **_dense_** areas of text in an image (images that are documents), and images that contain handwriting. 
  * **Response** : Returns the structural hierarchy for the OCR detected text (`fullTextAnnotation`). 
    * Hierarchy of extracted text structure: 
      * TextAnnotation -> Page -> Block -> Paragraph -> Word -> Symbol.
      * Each structural component from Page on may further have their own properties such as detected languages, breaks, etc.
  * **Languages supported** : Works with currently [supported, mapped, and experimental](https://docs.cloud.google.com/vision/docs/languages) languages. 
  * Feature enum value: `DOCUMENT_TEXT_DETECTION`. 
    * Takes precedence when both `DOCUMENT_TEXT_DETECTION` and `TEXT_DETECTION` are requested. 

If you are detecting text in scanned documents, try [Document AI](https://docs.cloud.google.com/document-ai/docs/overview) for optical character recognition, structured form parsing, and entity extraction. You can use the [Document AI Toolbox](https://docs.cloud.google.com/document-ai/docs/handle-response#toolbox) to convert output from the Document AI format to the Cloud Vision format.   
  
### [Landmark detection](https://docs.cloud.google.com/vision/docs/detecting-landmarks) 1

![St Basil's Cathedral image](https://docs.cloud.google.com/static/vision/docs/images/moscow.png) | 

  * Provides the name of the landmark, a confidence score and a bounding box in the image for the landmark. 
  * Gives coordinates for the detected entity. 

  
  
### [Logo detection](https://docs.cloud.google.com/vision/docs/detecting-logos) 2

![annotated logo](https://docs.cloud.google.com/static/vision/docs/images/logo_annotated.png) | 

  * Provides a textual description of the entity identified, a confidence score, and a bounding polygon for the logo in the file. 

  
  
### [Label detection](https://docs.cloud.google.com/vision/docs/labels) 3

![Shanghai street image](https://docs.cloud.google.com/static/vision/docs/images/shanghai_labels.png) | 

  * Provides generalized labels for an image.
  * For each label returns a textual description, confidence score, and topicality rating.

  
  
### [Image properties](https://docs.cloud.google.com/vision/docs/detecting-properties) 4

![Bali image with properties](https://docs.cloud.google.com/static/vision/docs/images/bali_small_w_properties.jpeg) | 

  * Returns dominant colors in an image.
  * Each color is represented in the RGBA color space, has a confidence score, and displays the fraction of pixels occupied by the color [0, 1].

  
  
### [Object localization](https://docs.cloud.google.com/vision/docs/object-localizer) 5

![image with bounding boxes](https://docs.cloud.google.com/static/vision/docs/images/bicycle.jpg) | 

  * Provides general label and bounding box annotations for multiple objects recognized in a single image. 
  * For each object detected the following elements are returned: a textual description, a confidence score, and normalized vertices [0,1] for the bounding polygon around the object. 
Need customized object detection? With [AutoML Vision Object Detection](https://docs.cloud.google.com/vision/automl/object-detection/docs) you can create a custom machine learning model for your specific image object detection use case.  
  
  
### [Crop hint detection](https://docs.cloud.google.com/vision/docs/detecting-crop-hints) 6

![image with cropped version](https://docs.cloud.google.com/static/vision/docs/images/crop_both.jpeg) | 

  * Provides a bounding polygon for the cropped image, a confidence score, and an importance fraction of this salient region with respect to the original image for each request.
  * You can provide up to 16 image ratio values (width:height) for a single image.

  
  
### [Web entities and pages](https://docs.cloud.google.com/vision/docs/detecting-web) 7

![image with web entities table](https://docs.cloud.google.com/static/vision/docs/images/web_entities.png) | 

  * Provides a series of related Web content to an image.
  * Returns the following information: 
    * **Web entities** : Inferred entities (labels/descriptions) from similar images on the Web.
    * **Full matching images** : A list of URLs for fully matching images of any size on the Internet.
    * **Partial matching images** : A list of URLs for images that share key-point features, such as a cropped version of the original image.
    * **Pages with matching images** : A list of Webpages (identified by page URL, page title, matching image URL) with an image that satisfies the conditions described above.
    * **Visually similar images** : A list of URLs for images that share some features with the original image.
    * **Best guess label** : A best guess as to the topic of the requested image inferred from similar images on the Internet.

  
  
### [Explicit content detection (SafeSearch)](https://docs.cloud.google.com/vision/docs/detecting-safe-search)

| 

  * Provides likelihood ratings for the following explicit content categories: `adult`, `spoof`, `medical`, `violence`, and `racy`.
  * Likelihoods ratings are expressed as 6 different values: `UNKNOWN`, `VERY_UNLIKELY`, `UNLIKELY`, `POSSIBLE`, `LIKELY`, or `VERY_LIKELY`.

  
  
### [Face detection](https://docs.cloud.google.com/vision/docs/detecting-faces)

![sample image with face detection](https://docs.cloud.google.com/static/vision-ai/docs/images/face_detection2x.png) | 

  * Locates faces with bounding polygons, and identifies specific facial "landmarks" such as eyes, ears, nose, mouth, etc. along with their corresponding confidence values. 
  * Returns likelihood ratings for general image properties (underexposed, blurred, headwear present). 
  * Likelihoods ratings are expressed as 6 different values: `UNKNOWN`, `VERY_UNLIKELY`, `UNLIKELY`, `POSSIBLE`, `LIKELY`, or `VERY_LIKELY`. 
  * **Specific individual[Facial Recognition](https://en.wikipedia.org/wiki/Facial_recognition_system) is not supported.**

  
  
1\. _Image credit_ : [Nikolay Vorobyev](https://unsplash.com/photos/jaH3QF46gAY) on [Unsplash](https://unsplash.com/) (_annotations added_). ↩

2\. _Image credit_ : [Robert Scoble](https://www.flickr.com/photos/scobleizer/4249731778/) ([CC BY 2.0](https://creativecommons.org/licenses/by/2.0/), _annotation added_). ↩

3\. _Image credit_ : [Alex Knight](https://unsplash.com/photos/wfwUpfVqrKU) on [Unsplash](https://unsplash.com/). ↩

4\. _Image credit_ : [Jeremy Bishop](https://unsplash.com/photos/QUwLZNchflk) on [Unsplash](https://unsplash.com/). ↩

5\. _Image credit:_ [Bogdan Dada](https://unsplash.com/photos/J9cBJjlpYKU) on [Unsplash](https://unsplash.com/) (_annotations added_). ↩

6\. _Image credit_ : [ Yasmin Dangor](https://images.unsplash.com/photo-1526398018-f9ee0723f228?ixlib=rb-1.2.1&auto=format&fit=crop&w=1400&q=80) on [Unsplash](https://unsplash.com/) (_original and cropped image shown_). ↩

7\. _Image credit_ : [Quinten de Graaf](https://unsplash.com/photos/KB0Ipylp7dc) on [Unsplash](https://unsplash.com/). ↩

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
