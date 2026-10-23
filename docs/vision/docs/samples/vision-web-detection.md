---
url: https://docs.cloud.google.com/vision/docs/samples/vision-web-detection/
title: Detect web annotations in a local file \u00a0|\u00a0 Cloud Vision API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:19.801047+00:00
---

# Detect web annotations in a local file  |  Cloud Vision API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/docs/samples/vision-web-detection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Vision API ](https://docs.cloud.google.com/vision/docs)
  * [ Samples ](https://docs.cloud.google.com/vision/docs/samples)



#  Detect web annotations in a local file Stay organized with collections  Save and categorize content based on your preferences. 

Perform web annotation detection on a local file.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Detect Web entities and pages](https://docs.cloud.google.com/vision/docs/detecting-web)



## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Go API reference documentation](https://godoc.org/cloud.google.com/go/vision/apiv1). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // detectWeb gets image properties from the Vision API for an image at the given file path.
    func detectWeb(w io.Writer, file string) error {
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
    	web, err := client.DetectWeb(ctx, image, nil)
    	if err != nil {
    		return err
    	}
    
    	fmt.Fprintln(w, "Web properties:")
    	if len(web.FullMatchingImages) != 0 {
    		fmt.Fprintln(w, "\tFull image matches:")
    		for _, full := range web.FullMatchingImages {
    			fmt.Fprintf(w, "\t\t%s\n", full.Url)
    		}
    	}
    	if len(web.PagesWithMatchingImages) != 0 {
    		fmt.Fprintln(w, "\tPages with this image:")
    		for _, page := range web.PagesWithMatchingImages {
    			fmt.Fprintf(w, "\t\t%s\n", page.Url)
    		}
    	}
    	if len(web.WebEntities) != 0 {
    		fmt.Fprintln(w, "\tEntities:")
    		fmt.Fprintln(w, "\t\tEntity\t\tScore\tDescription")
    		for _, entity := range web.WebEntities {
    			fmt.Fprintf(w, "\t\t%-14s\t%-2.4f\t%s\n", entity.EntityId, entity.Score, entity.Description)
    		}
    	}
    	if len(web.BestGuessLabels) != 0 {
    		fmt.Fprintln(w, "\tBest guess labels:")
    		for _, label := range web.BestGuessLabels {
    			fmt.Fprintf(w, "\t\t%s\n", label.Label)
    		}
    	}
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.vision.v1.[AnnotateImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageRequest.html);
    import com.google.cloud.vision.v1.[AnnotateImageResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageResponse.html);
    import com.google.cloud.vision.v1.[BatchAnnotateImagesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.BatchAnnotateImagesResponse.html);
    import com.google.cloud.vision.v1.[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html);
    import com.google.cloud.vision.v1.[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html).[Type](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Type.html);
    import com.google.cloud.vision.v1.[Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Image.html);
    import com.google.cloud.vision.v1.[ImageAnnotatorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageAnnotatorClient.html);
    import com.google.cloud.vision.v1.[WebDetection](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.html);
    import com.google.cloud.vision.v1.[WebDetection](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.html).[WebEntity](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.WebEntity.html);
    import com.google.cloud.vision.v1.[WebDetection](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.html).[WebImage](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.WebImage.html);
    import com.google.cloud.vision.v1.[WebDetection](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.html).[WebLabel](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.WebLabel.html);
    import com.google.cloud.vision.v1.[WebDetection](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.html).[WebPage](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.WebPage.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.FileInputStream;
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.List;
    
    public class DetectWebDetections {
    
      public static void detectWebDetections() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String filePath = "path/to/your/image/file.jpg";
        detectWebDetections(filePath);
      }
    
      // Finds references to the specified image on the web.
      public static void detectWebDetections(String filePath) throws IOException {
        List<AnnotateImageRequest> requests = new ArrayList<>();
    
        [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) imgBytes = [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[readFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_readFrom_java_io_InputStream_)(new FileInputStream(filePath));
    
        [Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Image.html) img = [Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Image.html).newBuilder().setContent(imgBytes).build();
        [Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html) feat = [Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html).newBuilder().setType([Type](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Type.html).WEB_DETECTION).build();
        [AnnotateImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageRequest.html) request =
            [AnnotateImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageRequest.html).newBuilder().addFeatures(feat).setImage(img).build();
        requests.add(request);
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([ImageAnnotatorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageAnnotatorClient.html) client = [ImageAnnotatorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageAnnotatorClient.html).create()) {
          [BatchAnnotateImagesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.BatchAnnotateImagesResponse.html) response = client.batchAnnotateImages(requests);
          List<AnnotateImageResponse> responses = response.[getResponsesList](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.BatchAnnotateImagesResponse.html#com_google_cloud_vision_v1_BatchAnnotateImagesResponse_getResponsesList__)();
    
          for ([AnnotateImageResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageResponse.html) res : responses) {
            if (res.hasError()) {
              System.out.format("Error: %s%n", res.getError().getMessage());
              return;
            }
    
            // Search the web for usages of the image. You could use these signals later
            // for user input moderation or linking external references.
            // For a full list of available annotations, see http://g.co/cloud/vision/docs
            [WebDetection](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.html) annotation = res.getWebDetection();
            System.out.println("Entity:Id:Score");
            System.out.println("===============");
            for ([WebEntity](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.WebEntity.html) entity : annotation.[getWebEntitiesList](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.html#com_google_cloud_vision_v1_WebDetection_getWebEntitiesList__)()) {
              System.out.println(
                  entity.getDescription() + " : " + entity.getEntityId() + " : " + entity.getScore());
            }
            for ([WebLabel](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.WebLabel.html) label : annotation.[getBestGuessLabelsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.html#com_google_cloud_vision_v1_WebDetection_getBestGuessLabelsList__)()) {
              System.out.format("%nBest guess label: %s", label.getLabel());
            }
            System.out.println("%nPages with matching images: Score%n==");
            for ([WebPage](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.WebPage.html) page : annotation.[getPagesWithMatchingImagesList](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.html#com_google_cloud_vision_v1_WebDetection_getPagesWithMatchingImagesList__)()) {
              System.out.println(page.getUrl() + " : " + page.getScore());
            }
            System.out.println("%nPages with partially matching images: Score%n==");
            for ([WebImage](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.WebImage.html) image : annotation.[getPartialMatchingImagesList](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.html#com_google_cloud_vision_v1_WebDetection_getPartialMatchingImagesList__)()) {
              System.out.println(image.getUrl() + " : " + image.getScore());
            }
            System.out.println("%nPages with fully matching images: Score%n==");
            for ([WebImage](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.WebImage.html) image : annotation.[getFullMatchingImagesList](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.html#com_google_cloud_vision_v1_WebDetection_getFullMatchingImagesList__)()) {
              System.out.println(image.getUrl() + " : " + image.getScore());
            }
            System.out.println("%nPages with visually similar images: Score%n==");
            for ([WebImage](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.WebImage.html) image : annotation.[getVisuallySimilarImagesList](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.html#com_google_cloud_vision_v1_WebDetection_getVisuallySimilarImagesList__)()) {
              System.out.println(image.getUrl() + " : " + image.getScore());
            }
          }
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Node.js API reference documentation](https://googleapis.dev/nodejs/vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const vision = require('[@google-cloud/vision](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)');
    
    // Creates a client
    const client = new vision.[ImageAnnotatorClient](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)();
    
    /**
     * TODO(developer): Uncomment the following line before running the sample.
     */
    // const fileName = 'Local image file, e.g. /path/to/image.png';
    
    // Detect similar images on the web to a local file
    const [result] = await client.webDetection(fileName);
    const webDetection = result.webDetection;
    if (webDetection.fullMatchingImages.length) {
      console.log(
        `Full matches found: ${webDetection.fullMatchingImages.length}`
      );
      webDetection.fullMatchingImages.forEach(image => {
        console.log(`  URL: ${image.url}`);
        console.log(`  Score: ${image.score}`);
      });
    }
    
    if (webDetection.partialMatchingImages.length) {
      console.log(
        `Partial matches found: ${webDetection.partialMatchingImages.length}`
      );
      webDetection.partialMatchingImages.forEach(image => {
        console.log(`  URL: ${image.url}`);
        console.log(`  Score: ${image.score}`);
      });
    }
    
    if (webDetection.webEntities.length) {
      console.log(`Web entities found: ${webDetection.webEntities.length}`);
      webDetection.webEntities.forEach(webEntity => {
        console.log(`  Description: ${webEntity.description}`);
        console.log(`  Score: ${webEntity.score}`);
      });
    }
    
    if (webDetection.bestGuessLabels.length) {
      console.log(
        `Best guess labels found: ${webDetection.bestGuessLabels.length}`
      );
      webDetection.bestGuessLabels.forEach(label => {
        console.log(`  Label: ${label.label}`);
      });
    }

### PHP

Before trying this sample, follow the PHP setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision PHP API reference documentation](https://docs.cloud.google.com/php/docs/reference/cloud-vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace Google\Cloud\Samples\Vision;
    
    use Google\Cloud\Vision\V1\Client\ImageAnnotatorClient;
    
    /**
     * @param string $path Path to the image, e.g. "path/to/your/image.jpg"
     */
    function detect_web(string $path)
    {
        $imageAnnotator = new ImageAnnotatorClient();
    
        # annotate the image
        $image = file_get_contents($path);
        $response = $imageAnnotator->webDetection($image);
        $web = $response->getWebDetection();
    
        // Print best guess labels
        printf('%d best guess labels found' . PHP_EOL,
            count($web->getBestGuessLabels()));
        foreach ($web->getBestGuessLabels() as $label) {
            printf('Best guess label: %s' . PHP_EOL, $label->getLabel());
        }
        print(PHP_EOL);
    
        // Print pages with matching images
        printf('%d pages with matching images found' . PHP_EOL,
            count($web->getPagesWithMatchingImages()));
        foreach ($web->getPagesWithMatchingImages() as $page) {
            printf('URL: %s' . PHP_EOL, $page->getUrl());
        }
        print(PHP_EOL);
    
        // Print full matching images
        printf('%d full matching images found' . PHP_EOL,
            count($web->getFullMatchingImages()));
        foreach ($web->getFullMatchingImages() as $fullMatchingImage) {
            printf('URL: %s' . PHP_EOL, $fullMatchingImage->getUrl());
        }
        print(PHP_EOL);
    
        // Print partial matching images
        printf('%d partial matching images found' . PHP_EOL,
            count($web->getPartialMatchingImages()));
        foreach ($web->getPartialMatchingImages() as $partialMatchingImage) {
            printf('URL: %s' . PHP_EOL, $partialMatchingImage->getUrl());
        }
        print(PHP_EOL);
    
        // Print visually similar images
        printf('%d visually similar images found' . PHP_EOL,
            count($web->getVisuallySimilarImages()));
        foreach ($web->getVisuallySimilarImages() as $visuallySimilarImage) {
            printf('URL: %s' . PHP_EOL, $visuallySimilarImage->getUrl());
        }
        print(PHP_EOL);
    
        // Print web entities
        printf('%d web entities found' . PHP_EOL,
            count($web->getWebEntities()));
        foreach ($web->getWebEntities() as $entity) {
            printf('Description: %s, Score %s' . PHP_EOL,
                $entity->getDescription(),
                $entity->getScore());
        }
    
        $imageAnnotator->close();
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def detect_web(path):
        """Detects web annotations given an image."""
        from google.cloud import vision
    
        client = vision.[ImageAnnotatorClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.image_annotator.ImageAnnotatorClient.html)()
    
        with open(path, "rb") as image_file:
            content = image_file.read()
    
        image = vision.[Image](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.Image.html)(content=content)
    
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
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudvision). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
