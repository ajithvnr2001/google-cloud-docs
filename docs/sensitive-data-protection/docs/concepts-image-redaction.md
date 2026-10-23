---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-image-redaction/
title: Image inspection and redaction \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:09:43.466262+00:00
---

# Image inspection and redaction  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-image-redaction/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Image inspection and redaction Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the image inspection and redaction capabilities of Sensitive Data Protection.

Using [infoType detectors](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference), Sensitive Data Protection inspects a base64-encoded image and detects sensitive data within the image. Sensitive Data Protection can then return information about the location of sensitive data within the image or redact the sensitive data by masking it with an opaque rectangle.

Inspection and redaction are two distinct operations:

  * _Inspection_ : Sensitive Data Protection inspects the submitted base64-encoded image for the specified infoTypes. It returns the detected InfoTypes, along with one or more set of pixel coordinates and dimensions. Each set of pixel coordinate and dimension values indicates the bottom-left corner and the dimensions of bounding boxes, respectively. Each bounding box corresponds to all or part of a Sensitive Data Protection finding.
  * _Redaction_ : Sensitive Data Protection inspects the submitted base64-encoded image for the specified infoTypes. Sensitive Data Protection redacts any sensitive data findings by masking them with opaque rectangles. It returns the redacted base64-encoded image in the same image format as the original image. You can also configure the color of the redaction boxes in the request.



## When to use image inspection and redaction

The following are some common use cases:

  * **Obfuscate sensitive data in scanned documents** : Mask driver's licenses, national identity cards, and credit card numbers from uploaded PDF or image attachments before processing in downstream workflows.
  * **Sanitize customer support uploads** : Automatically redact account numbers and personal contact details in user-submitted screenshots before tickets are routed to support agents.
  * **Locate sensitive elements in digital media** : Inspect images to retrieve bounding-box pixel coordinates of detected text, allowing custom applications to review or selectively blur targeted regions.
  * **Prepare visual datasets for machine learning** : Mask sensitive personal data from training image corpora to comply with privacy guidelines while preserving surrounding visual context.



## About image inspection

The Sensitive Data Protection inspection service accepts a base64-encoded image and then searches the image for any data that matches its inspection criteria. Sensitive Data Protection returns the locations of any sensitive data that it detects.

Consider the following image.

[ ![Original image that contains sensitive objects.](https://docs.cloud.google.com/static/sensitive-data-protection/docs/images/objects-in-image.png)](https://docs.cloud.google.com/static/sensitive-data-protection/docs/images/objects-in-image.png) Original image (click to enlarge).

The image inspection process is as follows:

  1. You send a [`content.inspect`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.content/inspect) request to the DLP API. The request contains the base64-encoded image and the inspection configuration, which contains your detection criteria.
  2. Sensitive Data Protection scans the image using the inspection configuration and identifies any matches.
  3. Sensitive Data Protection returns the coordinates and dimensions of the regions within the image where it found sensitive data according to your detection criteria.



The returned coordinates indicate where to find the sensitive data. Be aware that Sensitive Data Protection often uses multiple boxes to indicate where a single instance of sensitive data is in the image.

If Sensitive Data Protection doesn't find any data in the image that corresponds to your detection criteria, it returns an empty, successful HTTP 200 response.

## About image redaction

Image redaction is similar to image inspection, with one additional step. After Sensitive Data Protection identifies the locations of sensitive data within the image, instead of returning the coordinates of the areas that contain the data, it places opaque rectangles on those areas, returning a redacted, base64-encoded image.

[ ![Redacted image with sensitive data obscured.](https://docs.cloud.google.com/static/sensitive-data-protection/docs/images/objects-redacted.png)](https://docs.cloud.google.com/static/sensitive-data-protection/docs/images/objects-redacted.png) Redacted image (click to enlarge).

The image redaction process is as follows:

  1. You send an [`image.redact`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.image/redact) request to the DLP API. The request contains the base64-encoded image and the image redaction configuration, which contains your detection criteria.
  2. Sensitive Data Protection scans the image using the image redaction configuration and identifies any matches.
  3. Sensitive Data Protection redacts all detected sensitive data by covering it with an opaque rectangle. It then encodes the image in base64 and returns the redacted image in the request response.



If Sensitive Data Protection doesn't find any data in the image that corresponds to your detection criteria, it returns the base64-encoded image unchanged.

## Image detection features

This section describes the image detection features that you can apply to your inspection and redaction operations. For all these features, you need to perform the scan in a [location that supports image scanning](https://docs.cloud.google.com/sensitive-data-protection/docs/locations#location-specific_limitations).

### Recognize text in images

Sensitive Data Protection uses optical character recognition (OCR) to detect text within images. Sensitive Data Protection analyzes the detected text similarly to how it analyzes a body of text.

To detect text in images, specify any text-based infoType, such as `PERSON_NAME` and `CREDIT_CARD_NUMBER` in your inspection or redaction configuration.

### Recognize objects and themes in images

Sensitive Data Protection can analyze the pixels and features of images that aren't primarily text-based. Sensitive Data Protection uses this technique for the following features.

#### Object detection

Sensitive Data Protection can classify and redact objects in images. For example, you can configure your scans to detect photo ID cards, persons, and license plates in images.

To detect objects in images, specify [object infoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference#objects-images) in your inspection or redaction configuration.

For more information, see the following:

  * [Inspect an image for sensitive objects](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-images#inspect_an_image_for_sensitive_objects)
  * [Object redaction](https://docs.cloud.google.com/sensitive-data-protection/docs/redacting-sensitive-data-images#object-redaction)



#### Image safety classification

Sensitive Data Protection can classify and redact images based on their thematic content. This feature helps you identify images that contain sensitive or harmful subject matter according to predefined safety categories.

Sensitive Data Protection analyzes an image's overall context and meaning to determine if it belongs to categories such as sexually explicit or violent content. You can use this feature to support content moderation and enforce acceptable use policies.

When performing image safety classification, Sensitive Data Protection analyzes the entire image. Unlike object detection, which identifies specific items within an image, this feature assesses the image's subject matter as a whole. If you configure redaction based on image safety, this feature redacts the entire image.

To perform image safety classification, specify [image context infoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference#image-context) in your inspection or redaction configuration.

##### Limitations for generated images

The models that Sensitive Data Protection uses for image safety classification are primarily trained and evaluated on real-world images. Although these models can provide some value for analyzing AI-generated images, their effectiveness in detecting all types of policy-violating content in AI-generated images can vary.

If you use [image context infoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference#image-context) on AI-generated images, the following might not be detected:

  * Nuanced or subtle content
  * Context-dependent scenarios, such as private settings
  * Non-graphic depictions of sensitive themes



The performance of these classifiers on AI-generated images might not match the performance observed with natural images. We recommend that you conduct thorough testing for your specific generative AI use cases to ensure that the results meet your safety requirements. Don't rely solely on these classifiers for safety assurances in high-risk generative AI applications.

## What's next

  * Learn how to [inspect images for sensitive data using Sensitive Data Protection](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-images).
  * Learn how to [redact sensitive data from images using Sensitive Data Protection](https://docs.cloud.google.com/sensitive-data-protection/docs/redacting-sensitive-data-images).
  * Learn more about [creating a de-identified copy of data in storage](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-deidentify-storage).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
