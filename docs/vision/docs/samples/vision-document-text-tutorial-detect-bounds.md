---
url: https://docs.cloud.google.com/vision/docs/samples/vision-document-text-tutorial-detect-bounds/
title: Detect text in a document: Bounds \u00a0|\u00a0 Cloud Vision API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:02.323857+00:00
---

# Detect text in a document: Bounds  |  Cloud Vision API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/docs/samples/vision-document-text-tutorial-detect-bounds/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Vision API ](https://docs.cloud.google.com/vision/docs)
  * [ Samples ](https://docs.cloud.google.com/vision/docs/samples)



#  Detect text in a document: Bounds Stay organized with collections  Save and categorize content based on your preferences. 

Returns the bounds for the boxes around the text detected in a document.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Dense document text detection tutorial](https://docs.cloud.google.com/vision/docs/fulltext-annotations)



## Code sample

### Python

Before trying this sample, follow the Python setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def get_document_bounds(image_file, feature):
        """Finds the document bounds given an image and feature type.
    
        Args:
            image_file: path to the image file.
            feature: feature type to detect.
    
        Returns:
            List of coordinates for the corresponding feature type.
        """
        client = vision.ImageAnnotatorClient()
    
        bounds = []
    
        with open(image_file, "rb") as image_file:
            content = image_file.read()
    
        image = vision.Image(content=content)
    
        response = client.document_text_detection(image=image)
        document = response.full_text_annotation
    
        # Collect specified feature bounds by enumerating all document features
        for page in document.pages:
            for block in page.blocks:
                for paragraph in block.paragraphs:
                    for word in paragraph.words:
                        for symbol in word.symbols:
                            if feature == FeatureType.SYMBOL:
                                bounds.append(symbol.bounding_box)
    
                        if feature == FeatureType.WORD:
                            bounds.append(word.bounding_box)
    
                    if feature == FeatureType.PARA:
                        bounds.append(paragraph.bounding_box)
    
                if feature == FeatureType.BLOCK:
                    bounds.append(block.bounding_box)
    
        # The list `bounds` contains the coordinates of the bounding boxes.
        return bounds
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudvision). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
