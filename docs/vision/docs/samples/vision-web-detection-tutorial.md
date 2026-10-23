---
url: https://docs.cloud.google.com/vision/docs/samples/vision-web-detection-tutorial/
title: Web detection \u00a0|\u00a0 Cloud Vision API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:23.536196+00:00
---

# Web detection  |  Cloud Vision API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/docs/samples/vision-web-detection-tutorial/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Vision API ](https://docs.cloud.google.com/vision/docs)
  * [ Samples ](https://docs.cloud.google.com/vision/docs/samples)



#  Web detection Stay organized with collections  Save and categorize content based on your preferences. 

Perform web detection on a file, URL, or Cloud Storage URI.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Web detection tutorial](https://docs.cloud.google.com/vision/docs/internet-detection)



## Code sample

### Python

Before trying this sample, follow the Python setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import argparse
    
    from google.cloud import vision
    
    
    
    def annotate(path: str) -> vision.WebDetection:
        """Returns web annotations given the path to an image.
    
        Args:
            path: path to the input image.
    
        Returns:
            An WebDetection object with relevant information of the
            image from the internet (i.e., the annotations).
        """
        client = vision.[ImageAnnotatorClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.image_annotator.ImageAnnotatorClient.html)()
    
        if path.startswith("http") or path.startswith("gs:"):
            image = vision.[Image](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.Image.html)()
            image.source.image_uri = path
    
        else:
            with open(path, "rb") as image_file:
                content = image_file.read()
    
            image = vision.[Image](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.Image.html)(content=content)
    
        web_detection = client.web_detection(image=image).web_detection
    
        return web_detection
    
    
    def report(annotations: vision.WebDetection) -> None:
        """Prints detected features in the provided web annotations.
    
        Args:
            annotations: The web annotations (WebDetection object) from which
            the features should be parsed and printed.
        """
        if annotations.pages_with_matching_images:
            print(
                f"\n{len(annotations.pages_with_matching_images)} Pages with matching images retrieved"
            )
    
            for page in annotations.pages_with_matching_images:
                print(f"Url   : {page.url}")
    
        if annotations.full_matching_images:
            print(f"\n{len(annotations.full_matching_images)} Full Matches found: ")
    
            for image in annotations.full_matching_images:
                print(f"Url  : {image.url}")
    
        if annotations.partial_matching_images:
            print(f"\n{len(annotations.partial_matching_images)} Partial Matches found: ")
    
            for image in annotations.partial_matching_images:
                print(f"Url  : {image.url}")
    
        if annotations.web_entities:
            print(f"\n{len(annotations.web_entities)} Web entities found: ")
    
            for entity in annotations.web_entities:
                print(f"Score      : {entity.score}")
                print(f"Description: {entity.description}")
    
    
    if __name__ == "__main__":
        parser = argparse.ArgumentParser(
            description=__doc__,
            formatter_class=argparse.RawDescriptionHelpFormatter,
        )
        path_help = str(
            "The image to detect, can be web URI, "
            "Google Cloud Storage, or path to local file."
        )
        parser.add_argument("image_url", help=path_help)
        args = parser.parse_args()
    
        report(annotate(args.image_url))

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudvision). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
