---
url: https://docs.cloud.google.com/vision/docs/python-client-migration/
title: Migrating to Python Client Library v0.25.1 \u00a0|\u00a0 Cloud Vision API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:24:48.757931+00:00
---

# Migrating to Python Client Library v0.25.1  |  Cloud Vision API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/docs/python-client-migration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Vision API ](https://docs.cloud.google.com/vision/docs)
  * [ Reference ](https://docs.cloud.google.com/vision/docs/apis)



Send feedback 

#  Migrating to Python Client Library v0.25.1 Stay organized with collections  Save and categorize content based on your preferences. 

The Client Library for Python v0.25.1 includes some significant changes to how previous client libraries were designed. These changes can be summarized as follows:

  * Consolidation of modules into fewer types

  * Replacing untyped parameters with strongly-typed classes and enumerations




This topic provides details on the changes that you will need to make to your Python code for the Cloud Vision API client libraries in order to use the v0.25.1 Python client library.

**Note:** Upcoming functionality of the API will only be supported in the v.0.25.1 and newer versions of the client library. 

## Running previous versions of the client library

You are not required to upgrade your Python client library to v0.25.1. If you want to continue using a previous version of the Python client library and do not want to migrate your code, then you should specify the version of the Python client library used by your app. To specify a specific library version, edit the `requirements.txt` file as shown:
    
    
    google-cloud-vision==0.25
    

## Removed Modules

The following modules were removed in the Python Client Library v0.25.1 package.

  * `google.cloud.vision.annotations`

  * `google.cloud.vision.batch`

  * `google.cloud.vision.client`

  * `google.cloud.vision.color`

  * `google.cloud.vision.crop_hint`

  * `google.cloud.vision.entity`

  * `google.cloud.vision.face`

  * `google.cloud.vision.feature`

  * `google.cloud.vision.geometry`

  * `google.cloud.vision.image`

  * `google.cloud.vision.likelihood`

  * `google.cloud.vision.safe_search`

  * `google.cloud.vision.text`

  * `google.cloud.vision.web`




## Required Code Changes

### Imports

Include the new `google.cloud.vision.types` module in order to access the new types in the Python Client Library v0.25.1.

The `types` module contains the new classes that are required for creating requests, such as `types.Image`.
    
    
    from google.cloud import vision
    

Additionally, the new `google.cloud.vision.enums` module contains the enumerations useful for parsing and understanding API responses, such as `enums.Likelihood.UNLIKELY` and `enums.FaceAnnotation.Landmark.Type.LEFT_EYE`.

### Create a client

The `Client` class has been replaced with the `ImageAnnotatorClient` class. Replace references to the `Client` class with `ImageAnnotatorClient`.

**Previous versions of the client libraries:**
    
    
    old_client = vision.Client()
    

**Python Client Library v0.25.1:**
    
    
    client = vision.ImageAnnotatorClient()

### Constructing objects that represent image content

To identify image content from a local file, from a Google Cloud Storage URI, or from a web URI, use the new `Image` class.

#### Constructing objects that represent image content from a local file

The following example shows the new way to represent image content from a local file.

**Previous versions of the client libraries:**
    
    
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
    
    image = old_client.image(content=content)
    

**Python Client Library v0.25.1:**
    
    
    with open(path, "rb") as image_file:
        content = image_file.read()
    
    image = vision.Image(content=content)

#### Constructing objects that represent image content from a URI

The following example shows the new way to represent image content from a Google Cloud Storage URI or a web URI. `uri` is the URI to an image file on Google Cloud Storage or on the web.

**Previous versions of the client libraries:**
    
    
    image = old_client.image(source_uri=uri)
    

**Python Client Library v0.25.1:**
    
    
    image = vision.Image()
    image.source.image_uri = uri

### Making requests and processing responses

With the Python Client Library v.0.25.1 the API methods such as `face_detection` belong to the `ImageAnnotatorClient` object as opposed to the `Image` objects.

The returned values are different for several methods as explained below.

Particularly, bounding box vertices are now stored in `bounding_poly.vertices` as opposed to `bounds.vertices`. The coordinates of each vertex are stored in `vertex.x` and `vertex.y` as opposed to `vertex.x_coordinate` and `vertex.y_coordinate`.

The bounding box change affects `face_detection`, `logo_detection`, `text_detection`, `document_text_detection`, and `crop_hints`.

#### Making a face detection request and processing the response

**Python Client Library v0.25.1:**
    
    
    with open(path, "rb") as image_file:
        content = image_file.read()
    
    image = vision.Image(content=content)
    
    response = client.face_detection(image=image)
    faces = response.face_annotations
    
    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = (
        "UNKNOWN",
        "VERY_UNLIKELY",
        "UNLIKELY",
        "POSSIBLE",
        "LIKELY",
        "VERY_LIKELY",
    )
    print("Faces:")
    
    for face in faces:
        print(f"anger: {likelihood_name[face.anger_likelihood]}")
        print(f"joy: {likelihood_name[face.joy_likelihood]}")
        print(f"surprise: {likelihood_name[face.surprise_likelihood]}")
    
        vertices = [
            f"({vertex.x},{vertex.y})" for vertex in face.bounding_poly.vertices
        ]
    
        print("face bounds: {}".format(",".join(vertices)))
    
    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )

#### Making a label detection request and processing the response

**Previous versions of the client libraries:** :
    
    
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
    
    image = old_client.image(content=content)
    
    labels = image.detect_labels()
    
    for label in labels:
        print(label.description)
    

**Python Client Library v0.25.1:**
    
    
    with open(path, "rb") as image_file:
        content = image_file.read()
    
    image = vision.Image(content=content)
    
    response = client.label_detection(image=image)
    labels = response.label_annotations
    print("Labels:")
    
    for label in labels:
        print(label.description)
    
    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )

#### Making a landmark detection request and processing the response

**Previous versions of the client libraries:** :

Landmark locations' latitude and longitude are now stored in `location.lat_lng.latitude` and `location.lat_lng.longitude`, as opposed to `location.latitude` and `location.longitude`.
    
    
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
    
    image = old_client.image(content=content)
    
    landmarks = image.detect_landmarks()
    
    for landmark in landmarks:
        print(landmark.description, landmark.score)
        for location in landmark.locations:
            print('Latitude'.format(location.latitude))
            print('Longitude'.format(location.longitude))
    

**Python Client Library v0.25.1:**
    
    
    with open(path, "rb") as image_file:
        content = image_file.read()
    
    image = vision.Image(content=content)
    
    response = client.landmark_detection(image=image)
    landmarks = response.landmark_annotations
    print("Landmarks:")
    
    for landmark in landmarks:
        print(landmark.description)
        for location in landmark.locations:
            lat_lng = location.lat_lng
            print(f"Latitude {lat_lng.latitude}")
            print(f"Longitude {lat_lng.longitude}")
    
    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )

#### Making a logo detection request and processing the response

**Previous versions of the client libraries:** :
    
    
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
    
    image = old_client.image(content=content)
    
    logos = image.detect_logos()
    
    for logo in logos:
        print(logo.description, logo.score)
    

**Python Client Library v0.25.1:**
    
    
    with open(path, "rb") as image_file:
        content = image_file.read()
    
    image = vision.Image(content=content)
    
    request = {
        "image": image,
        "features": [{"type_": vision.Feature.Type.LOGO_DETECTION}],
    }
    
    response = client.annotate_image(request=request)
    logos = response.logo_annotations
    print("Logos:")
    
    for logo in logos:
        print(logo.description)
    
    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )

#### Making a SafeSearch detection request and processing the response

SafeSearch likelihoods are now returned as enumerations. The names of likelihood labels can be recovered by importing `google.cloud.vision.enums.Likelihood`.

**Previous versions of the client libraries:** :
    
    
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
    
    image = old_client.image(content=content)
    
    safe = image.detect_safe_search()
    print('Safe search:')
    print('adult: {}'.format(safe.adult))
    print('medical: {}'.format(safe.medical))
    print('spoofed: {}'.format(safe.spoof))
    print('violence: {}'.format(safe.violence))
    

**Python Client Library v0.25.1:**
    
    
    with open(path, "rb") as image_file:
        content = image_file.read()
    
    image = vision.Image(content=content)
    
    response = client.safe_search_detection(image=image)
    safe = response.safe_search_annotation
    
    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = (
        "UNKNOWN",
        "VERY_UNLIKELY",
        "UNLIKELY",
        "POSSIBLE",
        "LIKELY",
        "VERY_LIKELY",
    )
    print("Safe search:")
    
    print(f"adult: {likelihood_name[safe.adult]}")
    print(f"medical: {likelihood_name[safe.medical]}")
    print(f"spoofed: {likelihood_name[safe.spoof]}")
    print(f"violence: {likelihood_name[safe.violence]}")
    print(f"racy: {likelihood_name[safe.racy]}")
    
    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )

#### Making a text detection request and processing the response

**Previous versions of the client libraries:** :
    
    
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
    
    image = old_client.image(content=content)
    
    texts = image.detect_text()
    
    for text in texts:
        print('\n"{}"'.format(text.description))
    
        vertices = (['({},{})'.format(bound.x_coordinate, bound.y_coordinate)
                    for bound in text.bounds.vertices])
    
        print('bounds: {}'.format(','.join(vertices)))
    

**Python Client Library v0.25.1:**
    
    
    with open(path, "rb") as image_file:
        content = image_file.read()
    
    image = vision.Image(content=content)
    
    response = client.text_detection(image=image)
    texts = response.text_annotations
    print("Texts:")
    
    for text in texts:
        print(f'\n"{text.description}"')
    
        vertices = [
            f"({vertex.x},{vertex.y})" for vertex in text.bounding_poly.vertices
        ]
    
        print("bounds: {}".format(",".join(vertices)))
    
    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )

#### Making a document text detection request and processing the response

**Previous versions of the client libraries:** :
    
    
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
    
    image = old_client.image(content=content)
    
    document = image.detect_full_text()
    
    for page in document.pages:
        for block in page.blocks:
            block_words = []
            for paragraph in block.paragraphs:
                block_words.extend(paragraph.words)
    
            block_symbols = []
            for word in block_words:
                block_symbols.extend(word.symbols)
    
            block_text = ''
            for symbol in block_symbols:
                block_text = block_text + symbol.text
    
            print('Block Content: {}'.format(block_text))
            print('Block Bounds:\n {}'.format(block.bounding_box))
    

**Python Client Library v0.25.1:**
    
    
    with open(path, "rb") as image_file:
        content = image_file.read()
    
    image = vision.Image(content=content)
    
    response = client.document_text_detection(image=image)
    
    for page in response.full_text_annotation.pages:
        for block in page.blocks:
            print(f"\nBlock confidence: {block.confidence}\n")
    
            for paragraph in block.paragraphs:
                print("Paragraph confidence: {}".format(paragraph.confidence))
    
                for word in paragraph.words:
                    word_text = "".join([symbol.text for symbol in word.symbols])
                    print(
                        "Word text: {} (confidence: {})".format(
                            word_text, word.confidence
                        )
                    )
    
                    for symbol in word.symbols:
                        print(
                            "\tSymbol: {} (confidence: {})".format(
                                symbol.text, symbol.confidence
                            )
                        )
    
    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )

#### Making an image properties request and processing the response

Dominant color information is now stored in `props.dominant_colors.colors` as opposed to `props.colors`.

**Previous versions of the client libraries:** :
    
    
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
    
    image = old_client.image(content=content)
    
    props = image.detect_properties()
    
    for color in props.colors:
        print('fraction: {}'.format(color.pixel_fraction))
        print('\tr: {}'.format(color.color.red))
        print('\tg: {}'.format(color.color.green))
        print('\tb: {}'.format(color.color.blue))
        print('\ta: {}'.format(color.color.alpha))
    

**Python Client Library v0.25.1:**
    
    
    with open(path, "rb") as image_file:
        content = image_file.read()
    
    image = vision.Image(content=content)
    
    response = client.image_properties(image=image)
    props = response.image_properties_annotation
    print("Properties:")
    
    for color in props.dominant_colors.colors:
        print(f"fraction: {color.pixel_fraction}")
        print(f"\tr: {color.color.red}")
        print(f"\tg: {color.color.green}")
        print(f"\tb: {color.color.blue}")
        print(f"\ta: {color.color.alpha}")
    
    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )

#### Making a web detection request and processing the response

**Previous versions of the client libraries:** :
    
    
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
    
    image = old_client.image(content=content)
    
    notes = image.detect_web()
    
    if notes.pages_with_matching_images:
        print('\n{} Pages with matching images retrieved')
    
        for page in notes.pages_with_matching_images:
            print('Score : {}'.format(page.score))
            print('Url   : {}'.format(page.url))
    
    if notes.full_matching_images:
        print ('\n{} Full Matches found: '.format(
               len(notes.full_matching_images)))
    
        for image in notes.full_matching_images:
            print('Score:  {}'.format(image.score))
            print('Url  : {}'.format(image.url))
    
    if notes.partial_matching_images:
        print ('\n{} Partial Matches found: '.format(
               len(notes.partial_matching_images)))
    
        for image in notes.partial_matching_images:
            print('Score: {}'.format(image.score))
            print('Url  : {}'.format(image.url))
    
    if notes.web_entities:
        print ('\n{} Web entities found: '.format(len(notes.web_entities)))
    
        for entity in notes.web_entities:
            print('Score      : {}'.format(entity.score))
            print('Description: {}'.format(entity.description))
    

**Python Client Library v0.25.1:**
    
    
    with open(path, "rb") as image_file:
        content = image_file.read()
    
    image = vision.Image(content=content)
    
    response = client.web_detection(image=image)
    annotations = response.web_detection
    
    if annotations.best_guess_labels:
        for label in annotations.best_guess_labels:
            print(f"\nBest guess label: {label.label}")
    
    if annotations.pages_with_matching_images:
        print(
            "\n{} Pages with matching images found:".format(
                len(annotations.pages_with_matching_images)
            )
        )
    
        for page in annotations.pages_with_matching_images:
            print(f"\n\tPage url   : {page.url}")
    
            if page.full_matching_images:
                print(
                    "\t{} Full Matches found: ".format(len(page.full_matching_images))
                )
    
                for image in page.full_matching_images:
                    print(f"\t\tImage url  : {image.url}")
    
            if page.partial_matching_images:
                print(
                    "\t{} Partial Matches found: ".format(
                        len(page.partial_matching_images)
                    )
                )
    
                for image in page.partial_matching_images:
                    print(f"\t\tImage url  : {image.url}")
    
    if annotations.web_entities:
        print("\n{} Web entities found: ".format(len(annotations.web_entities)))
    
        for entity in annotations.web_entities:
            print(f"\n\tScore      : {entity.score}")
            print(f"\tDescription: {entity.description}")
    
    if annotations.visually_similar_images:
        print(
            "\n{} visually similar images found:\n".format(
                len(annotations.visually_similar_images)
            )
        )
    
        for image in annotations.visually_similar_images:
            print(f"\tImage url    : {image.url}")
    
    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )

#### Making a crop hints request and processing the response

**Previous versions of the client libraries:** :
    
    
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
    
    image = old_client.image(content=content)
    
    hints = image.detect_crop_hints(aspect_ratios=[1.77])
    
    for n, hint in enumerate(hints):
        print('\nCrop Hint: {}'.format(n))
    
        vertices = (['({},{})'.format(bound.x_coordinate, bound.y_coordinate)
                    for bound in hint.bounds.vertices])
    
        print('bounds: {}'.format(','.join(vertices)))
    

**Python Client Library v0.25.1:**
    
    
    with open(path, "rb") as image_file:
        content = image_file.read()
    image = vision.Image(content=content)
    
    crop_hints_params = vision.CropHintsParams(aspect_ratios=[1.77])
    image_context = vision.ImageContext(crop_hints_params=crop_hints_params)
    
    response = client.crop_hints(image=image, image_context=image_context)
    hints = response.crop_hints_annotation.crop_hints
    
    for n, hint in enumerate(hints):
        print(f"\nCrop Hint: {n}")
    
        vertices = [
            f"({vertex.x},{vertex.y})" for vertex in hint.bounding_poly.vertices
        ]
    
        print("bounds: {}".format(",".join(vertices)))
    
    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )

Note that the aspect ratios need to be passed in through a `CropHintsParams` and an `ImageContext`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
