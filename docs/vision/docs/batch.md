---
url: https://docs.cloud.google.com/vision/docs/batch/
title: Batch image annotation offline \u00a0|\u00a0 Cloud Vision API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:19.129608+00:00
---

# Batch image annotation offline  |  Cloud Vision API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/docs/batch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Vision API ](https://docs.cloud.google.com/vision/docs)
  * [ Guides ](https://docs.cloud.google.com/vision/docs/features-list)



Send feedback 

#  Batch image annotation offline Stay organized with collections  Save and categorize content based on your preferences. 

The Vision API can run offline (asynchronous) detection services and annotation of a large batch of image files using any Vision [feature type](https://docs.cloud.google.com/vision/docs/reference/rest/v1/Feature#type). For example, you can specify one or more Vision API features (such as `TEXT_DETECTION`, `LABEL_DETECTION`, and `LANDMARK_DETECTION`) for a single batch of images.

Output from an offline batch request is written to a JSON file created in the specified Cloud Storage bucket.

**Note:** All Vision API [feature types](https://docs.cloud.google.com/vision/docs/reference/rest/v1/Feature#type) also offer **online synchronous batch image annotation**. Online synchronous requests offer an immediate response to an annotation request. For more information, refer to the [how-to](https://docs.cloud.google.com/vision/docs/how-to) pages.

  * **online (synchronous)** requests - An online annotation request (`images:annotate` or `files:annotate`) immediately returns inline annotations to the user. Online annotation requests limit the number of files you can annotate in a single request. With an `images:annotate` request you can only specify a small number of images (<=16) to be annotated ; with a `files:annotate` request you can only specify a single file and specify a small number of pages (<=5) in that file to be annotated. 
  * **offline (asynchronous)** requests - An offline annotation request (`images:asyncBatchAnnotate` or `files:asyncBatchAnnotate`) starts a long-running operation (LRO) and does not immediately return a response to the caller. When the LRO completes, annotations are stored as files in a Cloud Storage bucket you specify. A `images:asyncBatchAnnotate` request allows you to specify up to 2000 images per request ; a `files:asyncBatchAnnotate` request allows you to specify larger batches of files and can specify more pages (<=2000) per file for annotation at a single time than you are able to with online requests. 



## Limitations

The Vision API accepts up to 2,000 image files. A larger batch of image files will return an error.

**Note:** If there are files in a batch request that Cloud Vision didn't process successfully, resubmit those files that failed processing to avoid being charged for files that were successfully processed.

## Currently supported feature types

Feature type  
---  
[`CROP_HINTS`](https://docs.cloud.google.com/vision/docs/detecting-crop-hints) | Determine suggested vertices for a crop region on an image.  
[`DOCUMENT_TEXT_DETECTION`](https://docs.cloud.google.com/vision/docs/pdf) | Perform OCR on dense text images, such as documents (PDF/TIFF), and images with handwriting. `TEXT_DETECTION` can be used for sparse text images. Takes precedence when both `DOCUMENT_TEXT_DETECTION` and `TEXT_DETECTION` are present.   
[`FACE_DETECTION`](https://docs.cloud.google.com/vision/docs/detecting-faces) | Detect faces within the image.  
[`IMAGE_PROPERTIES`](https://docs.cloud.google.com/vision/docs/detecting-properties) | Compute a set of image properties, such as the image's dominant colors.  
[`LABEL_DETECTION`](https://docs.cloud.google.com/vision/docs/labels) | Add labels based on image content.  
[`LANDMARK_DETECTION`](https://docs.cloud.google.com/vision/docs/detecting-landmarks) | Detect geographic landmarks within the image.  
[`LOGO_DETECTION`](https://docs.cloud.google.com/vision/docs/detecting-logos) | Detect company logos within the image.  
[`OBJECT_LOCALIZATION`](https://docs.cloud.google.com/vision/docs/object-localizer) | Detect and extract multiple objects in an image.  
[`SAFE_SEARCH_DETECTION`](https://docs.cloud.google.com/vision/docs/detecting-safe-search) | Run SafeSearch to detect potentially unsafe or undesirable content.  
[`TEXT_DETECTION`](https://docs.cloud.google.com/vision/docs/ocr) | Perform Optical Character Recognition (OCR) on text within the image. Text detection is optimized for areas of sparse text within a larger image. If the image is a document (PDF/TIFF), has dense text, or contains handwriting, use `DOCUMENT_TEXT_DETECTION` instead.   
[`WEB_DETECTION`](https://docs.cloud.google.com/vision/docs/detecting-web) | Detect topical entities such as news, events, or celebrities within the image, and find similar images on the web using the power of Google Image Search.   
  
## Sample code

Use the following code samples to run offline annotation services on a batch of image files in Cloud Storage.

**Note** : In the following code samples each requests element (`requests_element`/`requestsElement`) corresponds to a single image. To annotate more images, create a request element for each image and add it to the array of requests (`requests`). 

### Java

Before trying this sample, follow the Java setup instructions in the [Vision API Quickstart Using Client Libraries](https://docs.cloud.google.com/vision/docs/detect-labels-image-client-libraries). For more information, see the [ Vision API Java reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview).

**Note:** For Java **Spring framework** users, [Spring Cloud Google Cloud](https://docs.cloud.google.com/vision/docs/adding-spring) offers a way to automatically configure authentication settings and client objects to use Vision API. 
    
    
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
    
    

#### Response

A successful request returns response JSON files in the Cloud Storage bucket you indicated in the code sample. The number of responses per JSON file is dictated by `batch_size` in the code sample.

The returned response is similar to regular Vision API feature responses, depending on which features you request for an image.

The following responses show `LABEL_DETECTION` and `TEXT_DETECTION` annotations for `image1.png`, `IMAGE_PROPERTIES` annotations for `image2.jpg`, and `OBJECT_LOCALIZATION` annotations for `image3.jpg`.

The response also contain a `context` field showing the file's URI.

#### `offline_batch_output/output-1-to-2.json`
    
    
    {
      "responses": [
        {
          "**labelAnnotations** ": [
            {
              "mid": "/m/07s6nbt",
              "description": "Text",
              "score": 0.93413997,
              "topicality": 0.93413997
            },
            {
              "mid": "/m/0dwx7",
              "description": "Logo",
              "score": 0.8733531,
              "topicality": 0.8733531
            },
            ...
            {
              "mid": "/m/03bxgrp",
              "description": "Company",
              "score": 0.5682425,
              "topicality": 0.5682425
            }
          ],
          "**textAnnotations** ": [
            {
              "locale": "en",
              "description": "Google\n",
              "boundingPoly": {
                "vertices": [
                  {
                    "x": 72,
                    "y": 40
                  },
                  {
                    "x": 613,
                    "y": 40
                  },
                  {
                    "x": 613,
                    "y": 233
                  },
                  {
                    "x": 72,
                    "y": 233
                  }
                ]
              }
            },
            ...
                    ],
                    "blockType": "TEXT"
                  }
                ]
              }
            ],
            "text": "Google\n"
          },
          "context": {
            "uri": "**gs://cloud-samples-data/vision/document_understanding/image1.png** "
          }
        },
        {
          "**imagePropertiesAnnotation** ": {
            "dominantColors": {
              "colors": [
                {
                  "color": {
                    "red": 229,
                    "green": 230,
                    "blue": 238
                  },
                  "score": 0.2744754,
                  "pixelFraction": 0.075339235
                },
                ...
                {
                  "color": {
                    "red": 86,
                    "green": 87,
                    "blue": 95
                  },
                  "score": 0.025770646,
                  "pixelFraction": 0.13109145
                }
              ]
            }
          },
          "cropHintsAnnotation": {
            "cropHints": [
              {
                "boundingPoly": {
                  "vertices": [
                    {},
                    {
                      "x": 1599
                    },
                    {
                      "x": 1599,
                      "y": 1199
                    },
                    {
                      "y": 1199
                    }
                  ]
                },
                "confidence": 0.79999995,
                "importanceFraction": 1
              }
            ]
          },
          "context": {
            "uri": "**gs://cloud-samples-data/vision/document_understanding/image2.jpg** "
          }
        }
      ]
    }

#### `offline_batch_output/output-3-to-3.json`
    
    
    {
      "responses": [
        {
          "context": {
            "uri": "**gs://cloud-samples-data/vision/document_understanding/image3.jpg** "
          },
          "**localizedObjectAnnotations** ": [
            {
              "mid": "/m/0bt9lr",
              "name": "Dog",
              "score": 0.9669734,
              "boundingPoly": {
                "normalizedVertices": [
                  {
                    "x": 0.6035543,
                    "y": 0.1357359
                  },
                  {
                    "x": 0.98546547,
                    "y": 0.1357359
                  },
                  {
                    "x": 0.98546547,
                    "y": 0.98426414
                  },
                  {
                    "x": 0.6035543,
                    "y": 0.98426414
                  }
                ]
              }
            },
            ...
            {
              "mid": "/m/0jbk",
              "name": "Animal",
              "score": 0.58003056,
              "boundingPoly": {
                "normalizedVertices": [
                  {
                    "x": 0.014534635,
                    "y": 0.1357359
                  },
                  {
                    "x": 0.37197515,
                    "y": 0.1357359
                  },
                  {
                    "x": 0.37197515,
                    "y": 0.98426414
                  },
                  {
                    "x": 0.014534635,
                    "y": 0.98426414
                  }
                ]
              }
            }
          ]
        }
      ]
    }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
