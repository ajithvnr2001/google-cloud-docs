---
url: https://docs.cloud.google.com/vision/docs/samples/vision-localize-objects/
title: Detect multiple objects in a local file \u00a0|\u00a0 Cloud Vision API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:01:15.836383+00:00
---

# Detect multiple objects in a local file  |  Cloud Vision API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/docs/samples/vision-localize-objects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Vision API ](https://docs.cloud.google.com/vision/docs)
  * [ Samples ](https://docs.cloud.google.com/vision/docs/samples)



#  Detect multiple objects in a local file Stay organized with collections  Save and categorize content based on your preferences. 

Perform object detection for multiple objects in an image on a local file.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Detect multiple objects](https://docs.cloud.google.com/vision/docs/object-localizer)



## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Go API reference documentation](https://godoc.org/cloud.google.com/go/vision/apiv1). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // localizeObjects gets objects and bounding boxes from the Vision API for an image at the given file path.
    func localizeObjects(w io.Writer, file string) error {
    	ctx := context.Background()
    
    	client, err := vision.NewImageAnnotatorClient(ctx)
    	if err != nil {
    		return err
    	}
    
    	f, err := os.Open(file)
    	if err != nil {
    		return err
    	}
    	defer f.Close()
    
    	image, err := vision.NewImageFromReader(f)
    	if err != nil {
    		return err
    	}
    	annotations, err := client.LocalizeObjects(ctx, image, nil)
    	if err != nil {
    		return err
    	}
    
    	if len(annotations) == 0 {
    		fmt.Fprintln(w, "No objects found.")
    		return nil
    	}
    
    	fmt.Fprintln(w, "Objects:")
    	for _, annotation := range annotations {
    		fmt.Fprintln(w, annotation.Name)
    		fmt.Fprintln(w, annotation.Score)
    
    		for _, v := range annotation.BoundingPoly.NormalizedVertices {
    			fmt.Fprintf(w, "(%f,%f)\n", v.X, v.Y)
    		}
    	}
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Detects localized objects in the specified local image.
     *
     * @param filePath The path to the file to perform localized object detection on.
     * @throws Exception on errors while closing the client.
     * @throws IOException on Input/Output errors.
     */
    public static void detectLocalizedObjects(String filePath) throws IOException {
      List<AnnotateImageRequest> requests = new ArrayList<>();
    
      ByteString imgBytes = ByteString.readFrom(new FileInputStream(filePath));
    
      Image img = Image.newBuilder().setContent(imgBytes).build();
      AnnotateImageRequest request =
          AnnotateImageRequest.newBuilder()
              .addFeatures(Feature.newBuilder().setType(Type.OBJECT_LOCALIZATION))
              .setImage(img)
              .build();
      requests.add(request);
    
      // Initialize client that will be used to send requests. This client only needs to be created
      // once, and can be reused for multiple requests. After completing all of your requests, call
      // the "close" method on the client to safely clean up any remaining background resources.
      try (ImageAnnotatorClient client = ImageAnnotatorClient.create()) {
        // Perform the request
        BatchAnnotateImagesResponse response = client.batchAnnotateImages(requests);
        List<AnnotateImageResponse> responses = response.getResponsesList();
    
        // Display the results
        for (AnnotateImageResponse res : responses) {
          for (LocalizedObjectAnnotation entity : res.getLocalizedObjectAnnotationsList()) {
            System.out.format("Object name: %s%n", entity.getName());
            System.out.format("Confidence: %s%n", entity.getScore());
            System.out.format("Normalized Vertices:%n");
            entity
                .getBoundingPoly()
                .getNormalizedVerticesList()
                .forEach(vertex -> System.out.format("- (%s, %s)%n", vertex.getX(), vertex.getY()));
          }
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Node.js API reference documentation](https://googleapis.dev/nodejs/vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client libraries
    const vision = require('[@google-cloud/vision](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)');
    const fs = require('fs');
    
    // Creates a client
    const client = new vision.[ImageAnnotatorClient](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)();
    
    /**
     * TODO(developer): Uncomment the following line before running the sample.
     */
    // const fileName = `/path/to/localImage.png`;
    const request = {
      image: {content: fs.readFileSync(fileName)},
    };
    
    const [result] = await client.objectLocalization(request);
    const objects = result.localizedObjectAnnotations;
    objects.forEach(object => {
      console.log(`Name: ${object.name}`);
      console.log(`Confidence: ${object.score}`);
      const vertices = object.boundingPoly.normalizedVertices;
      vertices.forEach(v => console.log(`x: ${v.x}, y:${v.y}`));
    });

### PHP

Before trying this sample, follow the PHP setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision PHP API reference documentation](https://docs.cloud.google.com/php/docs/reference/cloud-vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace Google\Cloud\Samples\Vision;
    
    use Google\Cloud\Vision\V1\Client\ImageAnnotatorClient;
    
    /**
     * @param string $path Path to the image, e.g. "path/to/your/image.jpg"
     */
    function detect_object(string $path)
    {
        $imageAnnotator = new ImageAnnotatorClient();
    
        # annotate the image
        $image = file_get_contents($path);
        $response = $imageAnnotator->objectLocalization($image);
        $objects = $response->getLocalizedObjectAnnotations();
    
        foreach ($objects as $object) {
            $name = $object->getName();
            $score = $object->getScore();
            $vertices = $object->getBoundingPoly()->getNormalizedVertices();
    
            printf('%s (confidence %f)):' . PHP_EOL, $name, $score);
            print('normalized bounding polygon vertices: ');
            foreach ($vertices as $vertex) {
                printf(' (%f, %f)', $vertex->getX(), $vertex->getY());
            }
            print(PHP_EOL);
        }
    
        $imageAnnotator->close();
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def localize_objects(path):
        """Localize objects in the local image.
    
        Args:
        path: The path to the local file.
        """
        from google.cloud import vision
    
        client = vision.[ImageAnnotatorClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.image_annotator.ImageAnnotatorClient.html)()
    
        with open(path, "rb") as image_file:
            content = image_file.read()
        image = vision.[Image](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.Image.html)(content=content)
    
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
