---
url: https://docs.cloud.google.com/vision/docs/samples/vision-async-batch-annotate-images-beta/
title: Annotate a batch of images asynchronously (beta) \u00a0|\u00a0 Cloud Vision API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:24:47.358149+00:00
---

# Annotate a batch of images asynchronously (beta)  |  Cloud Vision API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/docs/samples/vision-async-batch-annotate-images-beta/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Vision API ](https://docs.cloud.google.com/vision/docs)
  * [ Samples ](https://docs.cloud.google.com/vision/docs/samples)



#  Annotate a batch of images asynchronously (beta) Stay organized with collections  Save and categorize content based on your preferences. 

Annotate a batch of image files in Cloud Storage while off-line.

## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.api.gax.paging.[Page](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.Page.html);
    import com.google.cloud.storage.[Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html);
    import com.google.cloud.storage.[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).[BlobListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.BlobListOption.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import com.google.cloud.vision.v1p4beta1.AnnotateImageRequest;
    import com.google.cloud.vision.v1p4beta1.AsyncBatchAnnotateImagesRequest;
    import com.google.cloud.vision.v1p4beta1.AsyncBatchAnnotateImagesResponse;
    import com.google.cloud.vision.v1p4beta1.BatchAnnotateImagesResponse;
    import com.google.cloud.vision.v1p4beta1.BatchAnnotateImagesResponse.Builder;
    import com.google.cloud.vision.v1p4beta1.Feature;
    import com.google.cloud.vision.v1p4beta1.Feature.Type;
    import com.google.cloud.vision.v1p4beta1.GcsDestination;
    import com.google.cloud.vision.v1p4beta1.Image;
    import com.google.cloud.vision.v1p4beta1.ImageAnnotatorClient;
    import com.google.cloud.vision.v1p4beta1.ImageSource;
    import com.google.cloud.vision.v1p4beta1.[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-storagebatchoperations/latest/com.google.cloud.storagebatchoperations.v1.OperationMetadata.html);
    import com.google.cloud.vision.v1p4beta1.OutputConfig;
    import com.google.protobuf.util.[JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html);
    import java.util.ArrayList;
    import java.util.List;
    import java.util.concurrent.TimeUnit;
    import java.util.regex.Matcher;
    import java.util.regex.Pattern;
    
    public class AsyncBatchAnnotateImagesGcs {
    
      // Performs asynchronous batch annotation of images on Google Cloud Storage
      public static void asyncBatchAnnotateImagesGcs(String gcsSourcePath, String gcsDestinationPath)
          throws Exception {
        // String gcsSourcePath = "gs://YOUR_BUCKET_ID/path_to_your_data";
        // String gcsDestinationPath = "gs://YOUR_BUCKET_ID/path_to_store_annotation";
        try (ImageAnnotatorClient client = ImageAnnotatorClient.create()) {
          List<AnnotateImageRequest> requests = new ArrayList<>();
    
          ImageSource imgSource = ImageSource.newBuilder().setImageUri(gcsSourcePath).build();
    
          Image image = Image.newBuilder().setSource(imgSource).build();
    
          // Set the GCS destination path for where to save the results.
          GcsDestination gcsDestination =
              GcsDestination.newBuilder().setUri(gcsDestinationPath).build();
    
          // Create the configuration for the output with the batch size.
          // The batch size sets how many pages should be grouped into each json output file.
          OutputConfig outputConfig =
              OutputConfig.newBuilder().setGcsDestination(gcsDestination).setBatchSize(2).build();
    
          // Select the Features required by the vision API
          Feature features =
              Feature.newBuilder()
                  .[setType](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.Identity.Builder.html#com_google_cloud_storageinsights_v1_Identity_Builder_setType_com_google_cloud_storageinsights_v1_Identity_IdentityType_)(Type.LABEL_DETECTION)
                  .[setType](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.Identity.Builder.html#com_google_cloud_storageinsights_v1_Identity_Builder_setType_com_google_cloud_storageinsights_v1_Identity_IdentityType_)(Type.TEXT_DETECTION)
                  .[setType](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.Identity.Builder.html#com_google_cloud_storageinsights_v1_Identity_Builder_setType_com_google_cloud_storageinsights_v1_Identity_IdentityType_)(Type.IMAGE_PROPERTIES)
                  .build();
    
          // Build the request
          AnnotateImageRequest annotateImageRequest =
              AnnotateImageRequest.newBuilder().setImage(image).addFeatures(features).build();
    
          requests.add(annotateImageRequest);
          AsyncBatchAnnotateImagesRequest request =
              AsyncBatchAnnotateImagesRequest.newBuilder()
                  .addAllRequests(requests)
                  .setOutputConfig(outputConfig)
                  .build();
    
          OperationFuture<AsyncBatchAnnotateImagesResponse, OperationMetadata> response =
              client.asyncBatchAnnotateImagesAsync(request);
          System.out.println("Waiting for the operation to finish.");
    
          // we're not processing the response, since we'll be reading the output from GCS.
          response.get(180, TimeUnit.SECONDS);
    
          // Once the request has completed and the output has been
          // written to GCS, we can list all the output files.
          [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).getDefaultInstance().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
    
          // Get the destination location from the gcsDestinationPath
          Pattern pattern = Pattern.compile("gs://([^/]+)/(.+)");
          Matcher matcher = pattern.matcher(gcsDestinationPath);
    
          if (matcher.[find](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.TypeRegistry.html#com_google_protobuf_util_JsonFormat_TypeRegistry_find_java_lang_String_)()) {
            String bucketName = matcher.group(1);
            String prefix = matcher.group(2);
    
            // Get the list of objects with the given prefix from the GCS bucket
            [Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) bucket = storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(bucketName);
            Page<Blob> pageList = bucket.[list](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html#com_google_cloud_storage_Bucket_list_com_google_cloud_storage_Storage_BlobListOption____)(BlobListOption.prefix(prefix));
    
            [Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html) firstOutputFile = null;
    
            // List objects with the given prefix.
            System.out.println("Output files:");
            for ([Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html) blob : pageList.iterateAll()) {
              System.out.println(blob.getName());
    
              // Process the first output file from GCS.
              // Since we specified batch size = 2, the first response contains
              // the first two image requests
              if (firstOutputFile == null) {
                firstOutputFile = blob;
              }
            }
    
            // Get the contents of the file and convert the JSON contents to an
            // BatchAnnotateImagesResponse
            // object. If the Blob is small read all its content in one request
            // (Note: the file is a .json file)
            // Storage guide: https://cloud.google.com/storage/docs/downloading-objects
            String jsonContents = new String(firstOutputFile.[getContent](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html#com_google_cloud_storage_Blob_getContent_com_google_cloud_storage_Blob_BlobSourceOption____)());
            Builder builder = BatchAnnotateImagesResponse.newBuilder();
            [JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html).parser().merge(jsonContents, builder);
    
            // Build the AnnotateFileResponse object
            BatchAnnotateImagesResponse batchAnnotateImagesResponse = builder.build();
    
            // Here we print the response for the first image
            // The response contains more information:
            // annotation/pages/blocks/paragraphs/words/symbols/colors
            // including confidence score and bounding boxes
            System.out.format("\nResponse: %s\n", batchAnnotateImagesResponse.getResponses(0));
    
          } else {
            System.out.println("No MATCH");
          }
        } catch (Exception e) {
          System.out.println("Error during asyncBatchAnnotateImagesGcs: \n" + e.toString());
        }
      }
    }
    

### Python

Before trying this sample, follow the Python setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def async_batch_annotate_images_uri(input_image_uri, output_uri):
        """Batch annotation of images on Google Cloud Storage asynchronously.
    
        Args:
        input_image_uri: The path to the image in Google Cloud Storage (gs://...)
        output_uri: The path to the output path in Google Cloud Storage (gs://...)
        """
        import re
    
        from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
        from google.cloud import vision_v1p4beta1 as vision
    
        client = vision.ImageAnnotatorClient()
    
        # Construct the request for the image(s) to be annotated:
        image_source = vision.ImageSource(image_uri=input_image_uri)
        image = vision.Image(source=image_source)
        features = [
            vision.Feature(type_=vision.Feature.[Type](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest/google.cloud.storage_control_v2.types.ObjectFullContext.Type.html).LABEL_DETECTION),
            vision.Feature(type_=vision.Feature.[Type](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest/google.cloud.storage_control_v2.types.ObjectFullContext.Type.html).TEXT_DETECTION),
            vision.Feature(type_=vision.Feature.[Type](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest/google.cloud.storage_control_v2.types.ObjectFullContext.Type.html).IMAGE_PROPERTIES),
        ]
        requests = [
            vision.AnnotateImageRequest(image=image, features=features),
        ]
    
        gcs_destination = vision.GcsDestination(uri=output_uri)
        output_config = vision.OutputConfig(gcs_destination=gcs_destination, batch_size=2)
    
        operation = client.async_batch_annotate_images(
            requests=requests, output_config=output_config
        )
    
        print("Waiting for the operation to finish.")
        operation.result(timeout=10000)
    
        # Once the request has completed and the output has been
        # written to Google Cloud Storage, we can list all the output files.
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
        match = re.match(r"gs://([^/]+)/(.+)", output_uri)
        bucket_name = match.[group](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.acl.ACL.html#google_cloud_storage_acl_ACL_group)(1)
        prefix = match.[group](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.acl.ACL.html#google_cloud_storage_acl_ACL_group)(2)
    
        bucket = storage_client.[get_bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_get_bucket)(bucket_name)
    
        # Lists objects with the given prefix.
        blob_list = list(bucket.list_blobs(prefix=prefix))
        print("Output files:")
        for blob in blob_list:
            print(blob.name)
    
        # Processes the first output file from Google Cloud Storage.
        # Since we specified batch_size=2, the first response contains
        # annotations for the first two annotate image requests.
        output = blob_list[0]
    
        json_string = output.[download_as_bytes](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_bytes)().decode("utf-8")
        response = vision.BatchAnnotateImagesResponse.from_json(json_string)
    
        # Prints the actual response for the first annotate image request.
        print(
            "The annotation response for the first request: {}".format(
                response.responses[0]
            )
        )
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudvision). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
