---
url: https://docs.cloud.google.com/vision/docs/samples/vision-face-detection-tutorial-send-request/
title: Send a request for face detection \u00a0|\u00a0 Cloud Vision API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:27:18.461516+00:00
---

# Send a request for face detection  |  Cloud Vision API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/docs/samples/vision-face-detection-tutorial-send-request/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Vision API ](https://docs.cloud.google.com/vision/docs)
  * [ Samples ](https://docs.cloud.google.com/vision/docs/samples)



#  Send a request for face detection Stay organized with collections  Save and categorize content based on your preferences. 

Send a request to the Cloud Vision API to detected faces in an image.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Face detection tutorial](https://docs.cloud.google.com/vision/docs/face-tutorial)



## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /** Gets up to {@code maxResults} faces for an image stored at {@code path}. */
    public List<FaceAnnotation> detectFaces(Path path, int maxResults) throws IOException {
      byte[] data = Files.readAllBytes(path);
    
      AnnotateImageRequest request =
          new AnnotateImageRequest()
              .setImage(new Image().encodeContent(data))
              .setFeatures(
                  ImmutableList.of(
                      new Feature().setType("FACE_DETECTION").setMaxResults(maxResults)));
      Vision.Images.Annotate annotate =
          vision
              .images()
              .annotate(new BatchAnnotateImagesRequest().setRequests(ImmutableList.of(request)));
      // Due to a bug: requests to Vision API containing large images fail when GZipped.
      annotate.setDisableGZipContent(true);
    
      BatchAnnotateImagesResponse batchResponse = annotate.execute();
      assert batchResponse.getResponses().size() == 1;
      AnnotateImageResponse response = batchResponse.getResponses().get(0);
      if (response.getFaceAnnotations() == null) {
        throw new IOException(
            response.getError() != null
                ? response.getError().getMessage()
                : "Unknown error getting image annotations");
      }
      return response.getFaceAnnotations();
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Node.js API reference documentation](https://googleapis.dev/nodejs/vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    async function detectFaces(inputFile) {
      // Make a call to the Vision API to detect the faces
      const request = {image: {source: {filename: inputFile}}};
      const results = await client.faceDetection(request);
      const faces = results[0].faceAnnotations;
      const numFaces = faces.length;
      console.log(`Found ${numFaces} face${numFaces === 1 ? '' : 's'}.`);
      return faces;
    }

### PHP

Before trying this sample, follow the PHP setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision PHP API reference documentation](https://docs.cloud.google.com/php/docs/reference/cloud-vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # annotate the image
    // $path = 'path/to/your/image.jpg'
    $image = file_get_contents($path);
    $response = $imageAnnotator->faceDetection($image);
    $faces = $response->getFaceAnnotations();

### Python

Before trying this sample, follow the Python setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def detect_face(face_file, max_results=4):
        """Uses the Vision API to detect faces in the given file.
    
        Args:
            face_file: A file-like object containing an image with faces.
    
        Returns:
            An array of Face objects with information about the picture.
        """
        client = vision.ImageAnnotatorClient()
    
        content = face_file.read()
        image = vision.Image(content=content)
    
        return client.face_detection(image=image, max_results=max_results).face_annotations
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudvision). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
