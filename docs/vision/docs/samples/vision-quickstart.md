---
url: https://docs.cloud.google.com/vision/docs/samples/vision-quickstart/
title: Detect labels on an image \u00a0|\u00a0 Cloud Vision API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:00.736900+00:00
---

# Detect labels on an image  |  Cloud Vision API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/docs/samples/vision-quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Vision API ](https://docs.cloud.google.com/vision/docs)
  * [ Samples ](https://docs.cloud.google.com/vision/docs/samples)



#  Detect labels on an image Stay organized with collections  Save and categorize content based on your preferences. 

Perform label detection on an image.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Quickstart: Detect labels in an image by using client libraries](https://docs.cloud.google.com/vision/docs/detect-labels-image-client-libraries)
  * [Vision client libraries](https://docs.cloud.google.com/vision/docs/libraries)



## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Go API reference documentation](https://godoc.org/cloud.google.com/go/vision/apiv1). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Sample vision-quickstart uses the Google Cloud Vision API to label an image.
    package main
    
    import (
    	"context"
    	"fmt"
    	"log"
    	"os"
    
    	vision "cloud.google.com/go/vision/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    
    	// Creates a client.
    	client, err := vision.[NewImageAnnotatorClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/latest/apiv1.html#cloud_google_com_go_vision_apiv1_ImageAnnotatorClient_NewImageAnnotatorClient)(ctx)
    	if err != nil {
    		log.Fatalf("Failed to create client: %v", err)
    	}
    	defer client.Close()
    
    	// Sets the name of the image file to annotate.
    	filename := "../testdata/cat.jpg"
    
    	file, err := os.Open(filename)
    	if err != nil {
    		log.Fatalf("Failed to read file: %v", err)
    	}
    	defer file.Close()
    	image, err := vision.[NewImageFromReader](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/latest/apiv1.html#cloud_google_com_go_vision_apiv1_NewImageFromReader)(file)
    	if err != nil {
    		log.Fatalf("Failed to create image: %v", err)
    	}
    
    	labels, err := client.[DetectLabels](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/latest/apiv1.html#cloud_google_com_go_vision_apiv1_ImageAnnotatorClient_DetectLabels)(ctx, image, nil, 10)
    	if err != nil {
    		log.Fatalf("Failed to detect labels: %v", err)
    	}
    
    	fmt.Println("Labels:")
    	for _, label := range labels {
    		fmt.Println(label.Description)
    	}
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    
    import com.google.cloud.vision.v1.[AnnotateImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageRequest.html);
    import com.google.cloud.vision.v1.[AnnotateImageResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageResponse.html);
    import com.google.cloud.vision.v1.[BatchAnnotateImagesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.BatchAnnotateImagesResponse.html);
    import com.google.cloud.vision.v1.[EntityAnnotation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.EntityAnnotation.html);
    import com.google.cloud.vision.v1.[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html);
    import com.google.cloud.vision.v1.[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html).[Type](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Type.html);
    import com.google.cloud.vision.v1.[Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Image.html);
    import com.google.cloud.vision.v1.[ImageAnnotatorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageAnnotatorClient.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.nio.file.Files;
    import java.nio.file.Path;
    import java.nio.file.Paths;
    import java.util.ArrayList;
    import java.util.List;
    
    public class QuickstartSample {
      public static void main(String... args) throws Exception {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([ImageAnnotatorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageAnnotatorClient.html) vision = [ImageAnnotatorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageAnnotatorClient.html).create()) {
    
          // The path to the image file to annotate
          String fileName = "./resources/wakeupcat.jpg";
    
          // Reads the image file into memory
          Path path = Paths.get(fileName);
          byte[] data = Files.readAllBytes(path);
          [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) imgBytes = [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(data);
    
          // Builds the image annotation request
          List<AnnotateImageRequest> requests = new ArrayList<>();
          [Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Image.html) img = [Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Image.html).newBuilder().setContent(imgBytes).build();
          [Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html) feat = [Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html).newBuilder().setType([Type](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Type.html).LABEL_DETECTION).build();
          [AnnotateImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageRequest.html) request =
              [AnnotateImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageRequest.html).newBuilder().addFeatures(feat).setImage(img).build();
          requests.add(request);
    
          // Performs label detection on the image file
          [BatchAnnotateImagesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.BatchAnnotateImagesResponse.html) response = vision.batchAnnotateImages(requests);
          List<AnnotateImageResponse> responses = response.[getResponsesList](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.BatchAnnotateImagesResponse.html#com_google_cloud_vision_v1_BatchAnnotateImagesResponse_getResponsesList__)();
    
          for ([AnnotateImageResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageResponse.html) res : responses) {
            if (res.hasError()) {
              System.out.format("Error: %s%n", res.getError().getMessage());
              return;
            }
    
            for ([EntityAnnotation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.EntityAnnotation.html) annotation : res.getLabelAnnotationsList()) {
              annotation
                  .getAllFields()
                  .forEach((k, v) -> System.out.format("%s : %s%n", k, v.toString()));
            }
          }
        }
      }
    }

### Kotlin
    
    
    import com.google.api.gax.rpc.ApiException
    import com.google.api.gax.rpc.InvalidArgumentException
    import com.google.cloud.vision.v1.AnnotateImageRequest
    import com.google.cloud.vision.v1.Feature
    import com.google.cloud.vision.v1.Image
    import com.google.cloud.vision.v1.ImageAnnotatorClient
    import com.google.cloud.vision.v1.ImageSource
    import java.io.IOException
    
    /**
     * Detects labels in an image stored in Google Cloud Storage using Cloud Vision.
     * Referencing a Cloud Storage URI avoids transferring raw image bytes from the
     * client workstation.
     *
     * @param gcsUri Cloud Storage URI of the target image (for example, "gs://example-bucket/example-image.jpg").
     */
    fun annotateImage(gcsUri: String) {
      val imageSource = ImageSource.newBuilder().setGcsImageUri(gcsUri).build()
      val image = Image.newBuilder().setSource(imageSource).build()
    
      // Limit label detection to 5 results to return only high-confidence annotations.
      val feature =
        Feature.newBuilder()
          .setType(Feature.Type.LABEL_DETECTION)
          .setMaxResults(5)
          .build()
      val request =
          AnnotateImageRequest.newBuilder()
            .addFeatures(feature)
            .setImage(image)
            .build()
    
      try {
        ImageAnnotatorClient.create().use { client ->
          val response = client.batchAnnotateImages(listOf(request))
          val imageResponse = response.responsesList.firstOrNull()
    
          if (imageResponse == null) {
            System.err.println(
              "error: no response received from Vision API for image '$gcsUri'"
            )
          } else if (imageResponse.hasError()) {
            System.err.println(
              "error: annotation failed for image '$gcsUri': ${imageResponse.error.message}"
            )
          } else {
            println("Resource ID: $gcsUri")
            println("Annotation Count: ${imageResponse.labelAnnotationsCount}")
            for (annotation in imageResponse.labelAnnotationsList) {
              println("Description: ${annotation.description}")
              println("Mid: ${annotation.mid}")
              println("Score: ${annotation.score}")
            }
          }
        }
      } catch (err: InvalidArgumentException) {
        System.err.println(
          "error: invalid annotation request for image '$gcsUri': ${err.message}"
        )
      } catch (err: ApiException) {
        System.err.println(
          "error: failed to annotate image '$gcsUri': ${err.message}"
        )
      } catch (err: IOException) {
        System.err.println(
          "error: failed to initialize Vision client for image '$gcsUri': ${err.message}"
        )
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Node.js API reference documentation](https://googleapis.dev/nodejs/vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    async function quickstart() {
      // Imports the Google Cloud client library
      const vision = require('[@google-cloud/vision](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)');
    
      // Creates a client
      const client = new vision.[ImageAnnotatorClient](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)();
    
      // Performs label detection on the image file
      const [result] = await client.labelDetection('./resources/wakeupcat.jpg');
      const labels = result.labelAnnotations;
      console.log('Labels:');
      labels.forEach(label => console.log(label.description));
    }
    quickstart();

### PHP

Before trying this sample, follow the PHP setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision PHP API reference documentation](https://docs.cloud.google.com/php/docs/reference/cloud-vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # includes the autoloader for libraries installed with composer
    require __DIR__ . '/vendor/autoload.php';
    
    # imports the Google Cloud client library
    use Google\Cloud\Vision\V1\Client\ImageAnnotatorClient;
    
    # instantiates a client
    $imageAnnotator = new ImageAnnotatorClient();
    
    # the name of the image file to annotate
    $fileName = 'test/data/wakeupcat.jpg';
    
    # prepare the image to be annotated
    $image = file_get_contents($fileName);
    
    # performs label detection on the image file
    $response = $imageAnnotator->labelDetection($image);
    $labels = $response->getLabelAnnotations();
    
    if ($labels) {
        echo('Labels:' . PHP_EOL);
        foreach ($labels as $label) {
            echo($label->getDescription() . PHP_EOL);
        }
    } else {
        echo('No label found' . PHP_EOL);
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Imports the Google Cloud client library
    from google.cloud import vision
    
    
    
    def run_quickstart() -> vision.EntityAnnotation:
        """Provides a quick start example for Cloud Vision."""
    
        # Instantiates a client
        client = vision.ImageAnnotatorClient()
    
        # The URI of the image file to annotate
        file_uri = "gs://cloud-samples-data/vision/label/wakeupcat.jpg"
    
        image = vision.Image()
        image.source.image_uri = file_uri
    
        # Performs label detection on the image file
        response = client.label_detection(image=image)
        labels = response.label_annotations
    
        print("Labels:")
        for label in labels:
            print(label.description)
    
        return labels
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudvision). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
