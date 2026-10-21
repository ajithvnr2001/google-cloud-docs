---
url: https://docs.cloud.google.com/vision/docs/samples/vision-async-batch-annotate-images/
title: Annotate a batch of images asynchronously \u00a0|\u00a0 Cloud Vision API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:06:30.978090+00:00
---

# Annotate a batch of images asynchronously  |  Cloud Vision API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/docs/samples/vision-async-batch-annotate-images/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Vision API ](https://docs.cloud.google.com/vision/docs)
  * [ Samples ](https://docs.cloud.google.com/vision/docs/samples)



#  Annotate a batch of images asynchronously Stay organized with collections  Save and categorize content based on your preferences. 

Annotate a batch of image files in Cloud Storage while off-line.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Batch image annotation offline](https://docs.cloud.google.com/vision/docs/batch)



## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.vision.v1.[AnnotateImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageRequest.html);
    import com.google.cloud.vision.v1.[AsyncBatchAnnotateImagesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AsyncBatchAnnotateImagesRequest.html);
    import com.google.cloud.vision.v1.[AsyncBatchAnnotateImagesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AsyncBatchAnnotateImagesResponse.html);
    import com.google.cloud.vision.v1.[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html);
    import com.google.cloud.vision.v1.[GcsDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.GcsDestination.html);
    import com.google.cloud.vision.v1.[Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Image.html);
    import com.google.cloud.vision.v1.[ImageAnnotatorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageAnnotatorClient.html);
    import com.google.cloud.vision.v1.[ImageSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageSource.html);
    import com.google.cloud.vision.v1.[OutputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.OutputConfig.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    
    public class AsyncBatchAnnotateImages {
    
      public static void asyncBatchAnnotateImages()
          throws InterruptedException, ExecutionException, IOException {
        String inputImageUri = "gs://cloud-samples-data/vision/label/wakeupcat.jpg";
        String outputUri = "gs://YOUR_BUCKET_ID/path/to/save/results/";
        asyncBatchAnnotateImages(inputImageUri, outputUri);
      }
    
      public static void asyncBatchAnnotateImages(String inputImageUri, String outputUri)
          throws IOException, ExecutionException, InterruptedException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([ImageAnnotatorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageAnnotatorClient.html) imageAnnotatorClient = [ImageAnnotatorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageAnnotatorClient.html).create()) {
    
          // You can send multiple images to be annotated, this sample demonstrates how to do this with
          // one image. If you want to use multiple images, you have to create a `AnnotateImageRequest`
          // object for each image that you want annotated.
          // First specify where the vision api can find the image
          [ImageSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageSource.html) source = [ImageSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageSource.html).newBuilder().[setImageUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageSource.Builder.html#com_google_cloud_vision_v1_ImageSource_Builder_setImageUri_java_lang_String_)(inputImageUri).build();
          [Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Image.html) image = [Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Image.html).newBuilder().[setSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Image.Builder.html#com_google_cloud_vision_v1_Image_Builder_setSource_com_google_cloud_vision_v1_ImageSource_)(source).build();
    
          // Set the type of annotation you want to perform on the image
          // https://cloud.google.com/vision/docs/reference/rpc/google.cloud.vision.v1#google.cloud.vision.v1.Feature.Type
          [Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html) feature = [Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html).newBuilder().setType([Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html).Type.LABEL_DETECTION).build();
    
          // Build the request object for that one image. Note: for additional images you have to create
          // additional `AnnotateImageRequest` objects and store them in a list to be used below.
          [AnnotateImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageRequest.html) imageRequest =
              [AnnotateImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageRequest.html).newBuilder().setImage(image).addFeatures(feature).build();
    
          // Set where to store the results for the images that will be annotated.
          [GcsDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.GcsDestination.html) gcsDestination = [GcsDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.GcsDestination.html).newBuilder().setUri(outputUri).build();
          [OutputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.OutputConfig.html) outputConfig =
              [OutputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.OutputConfig.html).newBuilder()
                  .[setGcsDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.OutputConfig.Builder.html#com_google_cloud_vision_v1_OutputConfig_Builder_setGcsDestination_com_google_cloud_vision_v1_GcsDestination_)(gcsDestination)
                  .[setBatchSize](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.OutputConfig.Builder.html#com_google_cloud_vision_v1_OutputConfig_Builder_setBatchSize_int_)(2) // The max number of responses to output in each JSON file
                  .build();
    
          // Add each `AnnotateImageRequest` object to the batch request and add the output config.
          [AsyncBatchAnnotateImagesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AsyncBatchAnnotateImagesRequest.html) request =
              [AsyncBatchAnnotateImagesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AsyncBatchAnnotateImagesRequest.html).newBuilder()
                  .addRequests(imageRequest)
                  .setOutputConfig(outputConfig)
                  .build();
    
          // Make the asynchronous batch request.
          [AsyncBatchAnnotateImagesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AsyncBatchAnnotateImagesResponse.html) response =
              imageAnnotatorClient.[asyncBatchAnnotateImagesAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageAnnotatorClient.html#com_google_cloud_vision_v1_ImageAnnotatorClient_asyncBatchAnnotateImagesAsync_com_google_cloud_vision_v1_AsyncBatchAnnotateImagesRequest_)(request).get();
    
          // The output is written to GCS with the provided output_uri as prefix
          String gcsOutputUri = response.[getOutputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AsyncBatchAnnotateImagesResponse.html#com_google_cloud_vision_v1_AsyncBatchAnnotateImagesResponse_getOutputConfig__)().getGcsDestination().getUri();
          System.out.format("Output written to GCS with prefix: %s%n", gcsOutputUri);
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Node.js API reference documentation](https://googleapis.dev/nodejs/vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const inputImageUri = 'gs://cloud-samples-data/vision/label/wakeupcat.jpg';
    // const outputUri = 'gs://YOUR_BUCKET_ID/path/to/save/results/';
    
    // Imports the Google Cloud client libraries
    const {ImageAnnotatorClient} = require('[@google-cloud/vision](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)').v1;
    
    // Instantiates a client
    const client = new [ImageAnnotatorClient](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)();
    
    // You can send multiple images to be annotated, this sample demonstrates how to do this with
    // one image. If you want to use multiple images, you have to create a request object for each image that you want annotated.
    async function asyncBatchAnnotateImages() {
      // Set the type of annotation you want to perform on the image
      // https://cloud.google.com/vision/docs/reference/rpc/google.cloud.vision.v1#google.cloud.vision.v1.Feature.Type
      const features = [{type: 'LABEL_DETECTION'}];
    
      // Build the image request object for that one image. Note: for additional images you have to create
      // additional image request objects and store them in a list to be used below.
      const imageRequest = {
        image: {
          source: {
            imageUri: inputImageUri,
          },
        },
        features: features,
      };
    
      // Set where to store the results for the images that will be annotated.
      const outputConfig = {
        gcsDestination: {
          uri: outputUri,
        },
        batchSize: 2, // The max number of responses to output in each JSON file
      };
    
      // Add each image request object to the batch request and add the output config.
      const request = {
        requests: [
          imageRequest, // add additional request objects here
        ],
        outputConfig,
      };
    
      // Make the asynchronous batch request.
      const [operation] = await client.asyncBatchAnnotateImages(request);
    
      // Wait for the operation to complete
      const [filesResponse] = await operation.promise();
    
      // The output is written to GCS with the provided output_uri as prefix
      const destinationUri = filesResponse.outputConfig.gcsDestination.uri;
      console.log(`Output written to GCS with prefix: ${destinationUri}`);
    }
    
    asyncBatchAnnotateImages();

### Python

Before trying this sample, follow the Python setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [vision_v1](https://docs.cloud.google.com/python/docs/reference/vision/latest)
    
    
    def sample_async_batch_annotate_images(
        input_image_uri="gs://cloud-samples-data/vision/label/wakeupcat.jpg",
        output_uri="gs://your-bucket/prefix/",
    ):
        """Perform async batch image annotation."""
        client = [vision_v1](https://docs.cloud.google.com/python/docs/reference/vision/latest).[ImageAnnotatorClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.image_annotator.ImageAnnotatorClient.html)()
    
        source = {"image_uri": input_image_uri}
        image = {"source": source}
        features = [
            {"type_": [vision_v1](https://docs.cloud.google.com/python/docs/reference/vision/latest).[Feature](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.Feature.html).Type.LABEL_DETECTION},
            {"type_": [vision_v1](https://docs.cloud.google.com/python/docs/reference/vision/latest).[Feature](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.Feature.html).Type.IMAGE_PROPERTIES},
        ]
    
        # Each requests element corresponds to a single image.  To annotate more
        # images, create a request element for each image and add it to
        # the array of requests
        requests = [{"image": image, "features": features}]
        gcs_destination = {"uri": output_uri}
    
        # The max number of responses to output in each JSON file
        batch_size = 2
        output_config = {"gcs_destination": gcs_destination, "batch_size": batch_size}
    
        operation = client.[async_batch_annotate_images](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.image_annotator.ImageAnnotatorClient.html#google_cloud_vision_v1_services_image_annotator_ImageAnnotatorClient_async_batch_annotate_images)(
            requests=requests, output_config=output_config
        )
    
        print("Waiting for operation to complete...")
        response = operation.result(90)
    
        # The output is written to GCS with the provided output_uri as prefix
        gcs_output_uri = response.output_config.gcs_destination.uri
        print(f"Output written to GCS with prefix: {gcs_output_uri}")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudvision). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
