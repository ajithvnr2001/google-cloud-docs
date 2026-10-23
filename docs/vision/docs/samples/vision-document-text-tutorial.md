---
url: https://docs.cloud.google.com/vision/docs/samples/vision-document-text-tutorial/
title: Detect text in a document \u00a0|\u00a0 Cloud Vision API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:01:17.774798+00:00
---

# Detect text in a document  |  Cloud Vision API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/docs/samples/vision-document-text-tutorial/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Vision API ](https://docs.cloud.google.com/vision/docs)
  * [ Samples ](https://docs.cloud.google.com/vision/docs/samples)



#  Detect text in a document Stay organized with collections  Save and categorize content based on your preferences. 

Draw boxes around the text detected in a document.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Dense document text detection tutorial](https://docs.cloud.google.com/vision/docs/fulltext-annotations)



## Code sample

### Python

Before trying this sample, follow the Python setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import argparse
    from enum import Enum
    
    from google.cloud import vision
    from PIL import [Image](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.Image.html), ImageDraw
    
    
    
    class FeatureType(Enum):
        PAGE = 1
        BLOCK = 2
        PARA = 3
        WORD = 4
        SYMBOL = 5
    
    
    def draw_boxes(image, bounds, color):
        """Draws a border around the image using the hints in the vector list.
    
        Args:
            image: the input image object.
            bounds: list of coordinates for the boxes.
            color: the color of the box.
    
        Returns:
            An image with colored bounds added.
        """
        draw = ImageDraw.Draw(image)
    
        for bound in bounds:
            draw.polygon(
                [
                    bound.vertices[0].x,
                    bound.vertices[0].y,
                    bound.vertices[1].x,
                    bound.vertices[1].y,
                    bound.vertices[2].x,
                    bound.vertices[2].y,
                    bound.vertices[3].x,
                    bound.vertices[3].y,
                ],
                None,
                color,
            )
        return image
    
    
    def get_document_bounds(image_file, feature):
        """Finds the document bounds given an image and feature type.
    
        Args:
            image_file: path to the image file.
            feature: feature type to detect.
    
        Returns:
            List of coordinates for the corresponding feature type.
        """
        client = vision.[ImageAnnotatorClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.image_annotator.ImageAnnotatorClient.html)()
    
        bounds = []
    
        with open(image_file, "rb") as image_file:
            content = image_file.read()
    
        image = vision.[Image](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.Image.html)(content=content)
    
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
    
    
    
    
    def render_doc_text(filein, fileout):
        """Outlines document features (blocks, paragraphs and words) given an image.
    
        Args:
            filein: path to the input image.
            fileout: path to the output image.
        """
        image = [Image](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.Image.html).open(filein)
        bounds = get_document_bounds(filein, FeatureType.BLOCK)
        draw_boxes(image, bounds, "blue")
        bounds = get_document_bounds(filein, FeatureType.PARA)
        draw_boxes(image, bounds, "red")
        bounds = get_document_bounds(filein, FeatureType.WORD)
        draw_boxes(image, bounds, "yellow")
    
        if fileout != 0:
            image.save(fileout)
        else:
            image.show()
    
    
    if __name__ == "__main__":
        parser = argparse.ArgumentParser()
        parser.add_argument("detect_file", help="The image for text detection.")
        parser.add_argument("-out_file", help="Optional output file", default=0)
        args = parser.parse_args()
    
        render_doc_text(args.detect_file, args.out_file)

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudvision). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
