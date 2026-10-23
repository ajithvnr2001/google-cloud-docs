---
url: https://docs.cloud.google.com/vision/docs/samples/vision-localize-objects-gcs-beta/
title: Detect multiple objects in a Cloud Storage file (beta) \u00a0|\u00a0 Cloud Vision API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:19.516302+00:00
---

# Detect multiple objects in a Cloud Storage file (beta)  |  Cloud Vision API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/docs/samples/vision-localize-objects-gcs-beta/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Vision API ](https://docs.cloud.google.com/vision/docs)
  * [ Samples ](https://docs.cloud.google.com/vision/docs/samples)



#  Detect multiple objects in a Cloud Storage file (beta) Stay organized with collections  Save and categorize content based on your preferences. 

Perform object detection for multiple objects in an image on a file stored in Cloud Storage (for beta launch).

## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Detects localized objects in a remote image on Google Cloud Storage.
     *
     * @param gcsPath The path to the remote file on Google Cloud Storage to detect localized objects
     *     on.
     * @param out A {@link PrintStream} to write detected objects to.
     * @throws Exception on errors while closing the client.
     * @throws IOException on Input/Output errors.
     */
    public static void detectLocalizedObjectsGcs(String gcsPath, PrintStream out)
        throws Exception, IOException {
      List<AnnotateImageRequest> requests = new ArrayList<>();
    
      ImageSource imgSource = ImageSource.newBuilder().setGcsImageUri(gcsPath).build();
      Image img = Image.newBuilder().setSource(imgSource).build();
    
      AnnotateImageRequest request =
          AnnotateImageRequest.newBuilder()
              .addFeatures(Feature.newBuilder().setType(Type.OBJECT_LOCALIZATION))
              .setImage(img)
              .build();
      requests.add(request);
    
      // Perform the request
      try (ImageAnnotatorClient client = ImageAnnotatorClient.create()) {
        BatchAnnotateImagesResponse response = client.batchAnnotateImages(requests);
        List<AnnotateImageResponse> responses = response.getResponsesList();
        client.close();
        // Display the results
        for (AnnotateImageResponse res : responses) {
          for (LocalizedObjectAnnotation entity : res.getLocalizedObjectAnnotationsList()) {
            out.format("Object name: %s\n", entity.getName());
            out.format("Confidence: %s\n", entity.getScore());
            out.format("Normalized Vertices:\n");
            entity
                .getBoundingPoly()
                .getNormalizedVerticesList()
                .forEach(vertex -> out.format("- (%s, %s)\n", vertex.getX(), vertex.getY()));
          }
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def localize_objects_uri(uri):
        """Localize objects in the image on Google Cloud Storage
    
        Args:
        uri: The path to the file in Google Cloud Storage (gs://...)
        """
        from google.cloud import vision_v1p3beta1 as vision
    
        client = vision.ImageAnnotatorClient()
    
        image = vision.Image()
        image.source.image_uri = uri
    
        objects = client.object_localization(image=image).localized_object_annotations
    
        print(f"Number of objects found: {len(objects)}")
        for object_ in objects:
            print(f"\n{object_.name} (confidence: {object_.score})")
            print("Normalized bounding polygon vertices: ")
            for vertex in object_.bounding_poly.normalized_vertices:
                print(f" - ({vertex.x}, {vertex.y})")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudvision). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
