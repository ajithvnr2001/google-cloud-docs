---
url: https://docs.cloud.google.com/vision/docs/internet-detection/
title: Web detection tutorial \u00a0|\u00a0 Cloud Vision API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:24:49.189831+00:00
---

# Web detection tutorial  |  Cloud Vision API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/docs/internet-detection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Vision API ](https://docs.cloud.google.com/vision/docs)
  * [ Guides ](https://docs.cloud.google.com/vision/docs/features-list)



Send feedback 

#  Web detection tutorial Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial demonstrates how to use the Vision API Web detection feature in a Python application to identify web entities, matching pages, and similar images.

## Audience

The goal of this tutorial is to help you develop applications using the Vision API Web detection feature. It assumes you are familiar with basic programming constructs and techniques, but even if you are a beginning programmer, you should be able to follow along and run this tutorial without difficulty, then use the [Vision API reference documentation](https://docs.cloud.google.com/vision/reference/rest) to create basic applications.

This tutorial steps through a Cloud Vision API application, showing you how to make a call to the Cloud Vision API to use its Web detection feature.

## Prerequisites

  * [Set up a Vision API project](https://docs.cloud.google.com/vision/docs/getting-started#set_up_a_google_cloud_vision_api_project) in the Google Cloud console.
  * Set up your environment for using [Application Default Credentials](https://docs.cloud.google.com/vision/docs/authentication).




### Python

  * Install [Python](https://www.python.org/).
  * [Install pip](https://pip.pypa.io/en/latest/installing/).
  * Install the [Google Cloud Client Library](https://docs.cloud.google.com/vision/docs/reference/libraries#installing_the_client_library).



## Overview

This tutorial walks you through a basic Cloud Vision API application that uses a `Web detection` _request_. A `Web detection` _response_ annotates the image sent in the request with:

  * labels obtained from the Web
  * site URLs that have matching images
  * URLs to Web images that partially or fully match the image in the request
  * URLs to visually similar images



## Code listing

As you read the code, we recommend that you follow along by referring to the [Vision API Python reference](https://docs.cloud.google.com/python/docs/reference/vision/latest).
    
    
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

This application performs the following tasks:

  * Imports the libraries necessary to run the application
  * Takes an image path as an argument and passes it to the `main()` function
  * Uses the Google Cloud API Client to perform Web detection
  * Loops over the response and prints out the results
  * Prints list of Web entities with description and score
  * Prints a list of matching pages
  * Prints a list of partially-matching images
  * Prints a list of fully-matching images



## A closer look

The following sections examine the key components of the sample application in detail.

### Importing libraries
    
    
    import argparse
    
    from google.cloud import vision
    

We import standard libraries:

  * `argparse` to allow the application to accept input filenames as arguments
  * `io` for reading from files



Other imports:

  * The `ImageAnnotatorClient` class within the `google.cloud.vision` library for accessing the Cloud Vision API.
  * The `types` module within the `google.cloud.vision` library for constructing requests.



### Running the application
    
    
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

Here, we parse the passed-in argument that specifies the URL of the Web image, and pass it to the `main()` function.

### Authenticating to the API

Before communicating with the Cloud Vision API service, you must authenticate your service using previously acquired credentials. Within an application, the simplest way to obtain credentials is to use [Application Default Credentials](https://docs.cloud.google.com/vision/docs/setup) (ADC). The client library obtains the credentials automatically. By default, this is done by obtaining credentials from the `GOOGLE_APPLICATION_CREDENTIALS` environment variable, which should be set to point to your service account's JSON key file (see [Set Up a Service Account](https://docs.cloud.google.com/vision/docs/setup) for more information.)

### Constructing the request
    
    
    client = vision.ImageAnnotatorClient()
    
    if path.startswith("http") or path.startswith("gs:"):
        image = vision.Image()
        image.source.image_uri = path
    
    else:
        with open(path, "rb") as image_file:
            content = image_file.read()
    
        image = vision.Image(content=content)
    
    web_detection = client.web_detection(image=image).web_detection

Now that our Cloud Vision API service is ready, we can construct a request to the service.

This code snippet performs the following tasks:

  1. Creates an `ImageAnnotatorClient` instance as the client.
  2. Constructs an `Image` object from either a local file or a URI.
  3. Passes the `Image` object to the `web_detection` method of the client.
  4. Returns the annotations.



### Printing the response
    
    
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

Once the operation has been completed, we walk through the [WebDetection](https://docs.cloud.google.com/vision/reference/rest/v1/images/annotate#WebDetection), and print the entities and URLs contained in the annotation (the top two results from each annotation type are shown in the next section).

### Running the application

To run the application, we pass in the Web URL (<http://www.photos-public-domain.com/wp-content/uploads/2011/01/old-vw-bug-and-van.jpg>) of the following car image.

![](https://docs.cloud.google.com/static/vision/docs/images/old-vw-bug-and-van.jpg)

Here is the Python command with the passed-in Web URL of the car image, followed by console output. Note that a relevancy score is added after the listed entities. Note that scores are not normalized or comparable across different image queries.
    
    
    python web_detect.py "http://www.photos-public-domain.com/wp-content/uploads/2011/01/old-vw-bug-and-van.jpg"
    
    
    
    5 Pages with matching images retrieved
    Url   : http://www.photos-public-domain.com/2011/01/07/old-volkswagen-bug-and-van/
    Url   : http://pix-hd.com/old+volkswagen+van+for+sale
    ...
    
    2 Full Matches found:
    Url  : http://www.photos-public-domain.com/wp-content/uploads/2011/01/old-vw-bug-and-van.jpg
    Url  : http://www.wbwagen.com/media/old-volkswagen-bug-and-van-picture-free-photograph-photos-public_s_66f487042adad5a6.jpg
    
    4 Partial Matches found:
    Url  : http://www.photos-public-domain.com/wp-content/uploads/2011/01/old-vw-bug-and-van.jpg
    Url  : http://www.wbwagen.com/media/old-vw-bug-and-vanjpg_s_ac343d7f041b5f8d.jpg
    ...
    
    5 Web entities found:
    Score      : 5.35028934479
    Description: Volkswagen Beetle
    Score      : 1.43998003006
    Description: Volkswagen
    Score      : 0.828279972076
    Description: Volkswagen Type 2
    Score      : 0.75271999836
    Description: Van
    Score      : 0.690039992332
    Description: Car
    

As expected, Cloud Vision Web detection has detected and returned under `fullMatchingImages` the URL of the Web image that we passed as input to the application (the last URL listed above).

Congratulations! You've performed Web detection using the Vision API!

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
