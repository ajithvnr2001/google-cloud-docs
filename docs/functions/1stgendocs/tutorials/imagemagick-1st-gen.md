---
url: https://docs.cloud.google.com/functions/1stgendocs/tutorials/imagemagick-1st-gen/
title: ImageMagick Tutorial (1st gen) \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:11:35.842989+00:00
---

# ImageMagick Tutorial (1st gen)  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/tutorials/imagemagick-1st-gen/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback 

#  ImageMagick Tutorial (1st gen) Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial demonstrates using Cloud Run functions, the [Cloud Vision API](https://docs.cloud.google.com/vision), and [ImageMagick](https://www.imagemagick.org) to detect and blur offensive images that get uploaded to a [Cloud Storage](https://docs.cloud.google.com/storage) bucket.

**Note:** While this tutorial demonstrates blurring images, ImageMagick can do much more than just blur images. You might also consider using the Node.js wrapper for ImageMagick [found on npm](https://www.npmjs.com/package/imagemagick).

## Objectives

  * Deploy a storage-triggered [Background Cloud Run function](https://docs.cloud.google.com/functions/1stgendocs/writing/write-event-driven-functions#background-functions).
  * Use the Vision API to detect violent or adult content.
  * Use ImageMagick to blur offensive images.
  * Test the function by uploading an image of a flesh-eating zombie.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * Cloud Run functions
  * Cloud Storage
  * Cloud Vision



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Cloud Functions, Cloud Build, Cloud Storage, and Cloud Vision APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudfunctions,cloudbuild.googleapis.com,storage_api,vision&redirect=https%3A//cloud.google.com/functions/1stgendocs/tutorials/imagemagick-1st-gen)

  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  6. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  8. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Enable the Cloud Functions, Cloud Build, Cloud Storage, and Cloud Vision APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudfunctions,cloudbuild.googleapis.com,storage_api,vision&redirect=https%3A//cloud.google.com/functions/1stgendocs/tutorials/imagemagick-1st-gen)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

If you already have the gcloud CLI installed, update it by running the following command:
    
    gcloud components update

  14. Prepare your development environment. 

###  Node.js 

[ Go to the Node.js setup guide ](https://docs.cloud.google.com/nodejs/docs/setup)

###  Python 

[ Go to the Python setup guide ](https://docs.cloud.google.com/python/docs/setup)

###  Go 

[ Go to the Go setup guide ](https://docs.cloud.google.com/go/docs/setup)

###  Java 

[ Go to the Java setup guide ](https://docs.cloud.google.com/java/docs/setup)

###  Ruby 

[ Go to the Ruby setup guide ](https://docs.cloud.google.com/ruby/docs/setup)




## Visualizing the flow of data

The flow of data in the ImageMagick tutorial application involves several steps:

  1. An image is uploaded to a Cloud Storage bucket.
  2. The function analyzes the image using the Vision API.
  3. If violent or adult content is detected, the function uses ImageMagick to blur the image.
  4. The blurred image is uploaded to another Cloud Storage bucket for use.



## Preparing the application

  1. Create a Cloud Storage bucket for uploading images, where `YOUR_INPUT_BUCKET_NAME` is a globally unique bucket name:
         
         gcloud storage buckets create gs://YOUR_INPUT_BUCKET_NAME

  2. Create a Cloud Storage bucket to receive blurred images, where `YOUR_OUTPUT_BUCKET_NAME` is a globally unique bucket name:
         
         gcloud storage buckets create gs://YOUR_OUTPUT_BUCKET_NAME

  3. Clone the sample app repository to your local machine:

###  Node.js 
         
         git clone https://github.com/GoogleCloudPlatform/nodejs-docs-samples.git

Alternatively, you can [ download the sample ](https://github.com/GoogleCloudPlatform/nodejs-docs-samples/archive/main.zip) as a zip file and extract it. 

###  Python 
         
         git clone https://github.com/GoogleCloudPlatform/python-docs-samples.git

Alternatively, you can [ download the sample ](https://github.com/GoogleCloudPlatform/python-docs-samples/archive/main.zip) as a zip file and extract it. 

###  Go 
         
         git clone https://github.com/GoogleCloudPlatform/golang-samples.git

Alternatively, you can [ download the sample ](https://github.com/GoogleCloudPlatform/golang-samples/archive/main.zip) as a zip file and extract it. 

###  Java 
         
         git clone https://github.com/GoogleCloudPlatform/java-docs-samples.git

Alternatively, you can [ download the sample ](https://github.com/GoogleCloudPlatform/java-docs-samples/archive/main.zip) as a zip file and extract it. 

###  Ruby 
         
         git clone https://github.com/GoogleCloudPlatform/ruby-docs-samples.git

Alternatively, you can [ download the sample ](https://github.com/GoogleCloudPlatform/ruby-docs-samples/archive/main.zip) as a zip file and extract it. 

  4. Change to the directory that contains the Cloud Run functions sample code:

###  Node.js 
         
         cd nodejs-docs-samples/functions/imagemagick/

###  Python 
         
         cd python-docs-samples/functions/imagemagick/

###  Go 
         
         cd golang-samples/functions/imagemagick/

###  Java 
         
         cd java-docs-samples/functions/imagemagick/

###  Ruby 
         
         cd ruby-docs-samples/functions/imagemagick/




## Understanding the code

### Importing dependencies

The application must import several dependencies in order to interact with Google Cloud services, ImageMagick, and the file system:

**Note:** ImageMagick and its command-line tool `convert` are included by default within the Cloud Run functions execution environment for most of the runtimes. Note that Cloud Run functions does _not_ support installing custom system-level packages.

###  Node.js 
    
    
    const sharp = require('sharp');
    const fs = require('fs').promises;
    const path = require('path');
    const vision = require('[@google-cloud/vision](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)');
    
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    const client = new vision.[ImageAnnotatorClient](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)();
    
    const {BLURRED_BUCKET_NAME} = process.env;

###  Python 
    
    
    import os
    import tempfile
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest), vision
    from wand.image import [Image](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.Image.html)
    
    storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    vision_client = vision.[ImageAnnotatorClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.image_annotator.ImageAnnotatorClient.html)()

###  Go 
    
    
    // Package imagemagick contains an example of using ImageMagick to process a
    // file uploaded to Cloud Storage.
    package imagemagick
    
    import (
    	"context"
    	"errors"
    	"fmt"
    	"log"
    	"os"
    	"os/exec"
    
    	"cloud.google.com/go/storage"
    	vision "cloud.google.com/go/vision/apiv1"
    	"cloud.google.com/go/vision/v2/apiv1/visionpb"
    )
    
    // Global API clients used across function invocations.
    var (
    	storageClient *storage.Client
    	visionClient  *vision.ImageAnnotatorClient
    )
    
    func init() {
    	// Declare a separate err variable to avoid shadowing the client variables.
    	var err error
    
    	storageClient, err = storage.NewClient(context.Background())
    	if err != nil {
    		log.Fatalf("storage.NewClient: %v", err)
    	}
    
    	visionClient, err = vision.NewImageAnnotatorClient(context.Background())
    	if err != nil {
    		log.Fatalf("vision.NewAnnotatorClient: %v", err)
    	}
    }
    

###  Java 
    
    
    
    import com.google.cloud.functions.BackgroundFunction;
    import com.google.cloud.functions.Context;
    import com.google.cloud.storage.[Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html);
    import com.google.cloud.storage.[BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html);
    import com.google.cloud.storage.[BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import com.google.cloud.vision.v1.[AnnotateImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageRequest.html);
    import com.google.cloud.vision.v1.[AnnotateImageResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageResponse.html);
    import com.google.cloud.vision.v1.[BatchAnnotateImagesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.BatchAnnotateImagesResponse.html);
    import com.google.cloud.vision.v1.[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html);
    import com.google.cloud.vision.v1.[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html).Type;
    import com.google.cloud.vision.v1.[Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Image.html);
    import com.google.cloud.vision.v1.[ImageAnnotatorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageAnnotatorClient.html);
    import com.google.cloud.vision.v1.[ImageSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageSource.html);
    import com.google.cloud.vision.v1.[SafeSearchAnnotation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.SafeSearchAnnotation.html);
    import functions.eventpojos.GcsEvent;
    import java.io.IOException;
    import java.nio.file.Files;
    import java.nio.file.Path;
    import java.nio.file.Paths;
    import java.util.List;
    import java.util.logging.Level;
    import java.util.logging.Logger;
    
    public class ImageMagick implements BackgroundFunction<GcsEvent> {
    
      private static [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).getDefaultInstance().getService();
      private static final String BLURRED_BUCKET_NAME = System.getenv("BLURRED_BUCKET_NAME");
      private static final Logger logger = Logger.getLogger(ImageMagick.class.getName());
    }

###  Ruby 
    
    
    require "functions_framework"
    
    FunctionsFramework.on_startup do
      set_global :storage_client do
        require "google/cloud/storage"
        Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      end
    
      set_global :vision_client do
        require "google/cloud/vision"
        Google::Cloud::[Vision](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision.html).[image_annotator](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision/latest/Google-Cloud-Vision.html)
      end
    end

### Analyzing images

The following function is invoked when an image is uploaded to the Cloud Storage bucket you created for storing images. The function uses the Vision API to detect violent or adult content in uploaded images.

###  Node.js 
    
    
    // Blurs uploaded images that are flagged as Adult or Violence.
    exports.blurOffensiveImages = async event => {
      // This event represents the triggering Cloud Storage object.
      const object = event;
      if (object.bucket === BLURRED_BUCKET_NAME) {
        console.log(
          'Event triggered by the blurred bucket; skip to avoid recursion'
        );
        return;
      }
    
      const file = storage.bucket(object.bucket).file(object.name);
      const filePath = `gs://${object.bucket}/${object.name}`;
    
      console.log(`Analyzing ${file.name}.`);
    
      try {
        const [result] = await client.safeSearchDetection(filePath);
        const detections = result.safeSearchAnnotation || {};
    
        if (
          // Levels are defined in https://cloud.google.com/vision/docs/reference/rest/v1/AnnotateImageResponse#likelihood
          detections.adult === 'VERY_LIKELY' ||
          detections.violence === 'VERY_LIKELY'
        ) {
          console.log(`Detected ${file.name} as inappropriate.`);
          return await blurImage(file, BLURRED_BUCKET_NAME);
        } else {
          console.log(`Detected ${file.name} as OK.`);
        }
      } catch (err) {
        console.error(`Failed to analyze ${file.name}.`, err);
        throw err;
      }
    };

###  Python 
    
    
    # Blurs uploaded images that are flagged as Adult or Violence.
    def blur_offensive_images(data, context):
        file_data = data
    
        file_name = file_data["name"]
        bucket_name = file_data["bucket"]
    
        blob = storage_client.bucket(bucket_name).get_blob(file_name)
        blob_uri = f"gs://{bucket_name}/{file_name}"
        blob_source = vision.Image(source=vision.ImageSource(gcs_image_uri=blob_uri))
    
        # Ignore already-blurred files
        if file_name.startswith("blurred-"):
            print(f"The image {file_name} is already blurred.")
            return
    
        print(f"Analyzing {file_name}.")
    
        result = vision_client.safe_search_detection(image=blob_source)
        detected = result.safe_search_annotation
    
        # Process image
        if detected.adult == 5 or detected.violence == 5:
            print(f"The image {file_name} was detected as inappropriate.")
            return __blur_image(blob)
        else:
            print(f"The image {file_name} was detected as OK.")
    
    

###  Go 
    
    
    // GCSEvent is the payload of a GCS event.
    type GCSEvent struct {
    	Bucket string `json:"bucket"`
    	Name   string `json:"name"`
    }
    
    // BlurOffensiveImages blurs offensive images uploaded to GCS.
    func BlurOffensiveImages(ctx context.Context, e GCSEvent) error {
    	outputBucket := os.Getenv("BLURRED_BUCKET_NAME")
    	if outputBucket == "" {
    		return errors.New("BLURRED_BUCKET_NAME must be set")
    	}
    
    	img := vision.NewImageFromURI(fmt.Sprintf("gs://%s/%s", e.Bucket, e.Name))
    
    	resp, err := visionClient.DetectSafeSearch(ctx, img, nil)
    	if err != nil {
    		return fmt.Errorf("AnnotateImage: %w", err)
    	}
    
    	if resp.GetAdult() == visionpb.Likelihood_VERY_LIKELY ||
    		resp.GetViolence() == visionpb.Likelihood_VERY_LIKELY {
    		return blur(ctx, e.Bucket, outputBucket, e.Name)
    	}
    	log.Printf("The image %q was detected as OK.", e.Name)
    	return nil
    }
    

###  Java 
    
    
    @Override
    // Blurs uploaded images that are flagged as Adult or Violence.
    public void accept(GcsEvent event, Context context) {
      // Validate parameters
      if (event.getBucket() == null || event.getName() == null) {
        logger.severe("Error: Malformed GCS event.");
        return;
      }
    
      BlobInfo blobInfo = BlobInfo.newBuilder(event.getBucket(), event.getName()).build();
    
      // Construct URI to GCS bucket and file.
      String gcsPath = String.format("gs://%s/%s", event.getBucket(), event.getName());
      logger.info(String.format("Analyzing %s", event.getName()));
    
      // Construct request.
      ImageSource imgSource = ImageSource.newBuilder().setImageUri(gcsPath).build();
      Image img = Image.newBuilder().setSource(imgSource).build();
      Feature feature = Feature.newBuilder().setType(Type.SAFE_SEARCH_DETECTION).build();
      AnnotateImageRequest request =
          AnnotateImageRequest.newBuilder().addFeatures(feature).setImage(img).build();
      List<AnnotateImageRequest> requests = List.of(request);
    
      // Send request to the Vision API.
      try (ImageAnnotatorClient client = ImageAnnotatorClient.create()) {
        BatchAnnotateImagesResponse response = client.batchAnnotateImages(requests);
        List<AnnotateImageResponse> responses = response.getResponsesList();
        for (AnnotateImageResponse res : responses) {
          if (res.hasError()) {
            logger.info(String.format("Error: %s", res.getError().getMessage()));
            return;
          }
          // Get Safe Search Annotations
          SafeSearchAnnotation annotation = res.getSafeSearchAnnotation();
          if (annotation.getAdultValue() == 5 || annotation.getViolenceValue() == 5) {
            logger.info(String.format("Detected %s as inappropriate.", event.getName()));
            blur(blobInfo);
          } else {
            logger.info(String.format("Detected %s as OK.", event.getName()));
          }
        }
      } catch (IOException e) {
        logger.log(Level.SEVERE, "Error with Vision API: " + e.getMessage(), e);
      }
    }

###  Ruby 
    
    
    # Blurs uploaded images that are flagged as Adult or Violence.
    FunctionsFramework.cloud_event "blur_offensive_images" do |event|
      # Event-triggered Ruby functions receive a CloudEvents::Event::V1 object.
      # See https://cloudevents.github.io/sdk-ruby/latest/CloudEvents/Event/V1.html
      # The storage event payload can be obtained from the event data.
      payload = event.data
      file_name = payload["name"]
      bucket_name = payload["bucket"]
    
      # Ignore already-blurred files
      if file_name.start_with? "blurred-"
        logger.info "The image #{file_name} is already blurred."
        return
      end
    
      # Get image annotations from the Vision service
      logger.info "Analyzing #{file_name}."
      gs_uri = "gs://#{bucket_name}/#{file_name}"
      result = global(:vision_client).safe_search_detection image: gs_uri
      annotation = result.responses.first.safe_search_annotation
    
      # Respond to annotations by possibly blurring the image
      if annotation.adult == :VERY_LIKELY || annotation.violence == :VERY_LIKELY
        logger.info "The image #{file_name} was detected as inappropriate."
        blur_image bucket_name, file_name
      else
        logger.info "The image #{file_name} was detected as OK."
      end
    end

### Blurring images

The following function is called when violent or adult content is detected in an uploaded image. The function downloads the offensive image, uses ImageMagick to blur the image, and then uploads the blurred image over the original image.

###  Node.js 
    
    
    // Blurs the given file using sharp, and uploads it to another bucket.
    const blurImage = async (file, blurredBucketName) => {
      const tempLocalPath = `/tmp/${path.parse(file.name).base}`;
      const tempLocalBlurredPath = `/tmp/blurred-${path.parse(file.name).base}`;
    
      // Download file from bucket.
      try {
        await file.download({destination: tempLocalPath});
    
        console.log(`Downloaded ${file.name} to ${tempLocalPath}.`);
      } catch (err) {
        throw new Error(`File download failed: ${err}`);
      }
      try {
        await sharp(tempLocalPath).blur(16).toFile(tempLocalBlurredPath);
    
        console.log(`Blurred image: ${file.name}`);
      } catch (err) {
        console.error('Failed to blur image.', err);
        throw err;
      }
    
      // Upload result to a different bucket, to avoid re-triggering this function.
      const blurredBucket = storage.bucket(blurredBucketName);
    
      // Upload the Blurred image back into the bucket.
      const gcsPath = `gs://${blurredBucketName}/${file.name}`;
      try {
        await blurredBucket.upload(tempLocalBlurredPath, {destination: file.name});
        console.log(`Uploaded blurred image to: ${gcsPath}`);
      } catch (err) {
        throw new Error(`Unable to upload blurred image to ${gcsPath}: ${err}`);
      } finally {
        // Delete the temporary file.
        await Promise.allSettled([
          fs.unlink(tempLocalPath),
          fs.unlink(tempLocalBlurredPath),
        ]);
      }
    };

###  Python 
    
    
    # Blurs the given file using ImageMagick.
    def __blur_image(current_blob):
        file_name = current_blob.name
        _, temp_local_filename = tempfile.mkstemp()
    
        # Download file from bucket.
        current_blob.download_to_filename(temp_local_filename)
        print(f"Image {file_name} was downloaded to {temp_local_filename}.")
    
        # Blur the image using ImageMagick.
        with Image(filename=temp_local_filename) as image:
            image.blur(radius=0, sigma=16)
            image.save(filename=temp_local_filename)
    
        print(f"Image {file_name} was blurred.")
    
        # Upload result to a second bucket, to avoid re-triggering the function.
        # You could instead re-upload it to the same bucket + tell your function
        # to ignore files marked as blurred (e.g. those with a "blurred" prefix)
        blur_bucket_name = os.getenv("BLURRED_BUCKET_NAME")
        blur_bucket = storage_client.bucket(blur_bucket_name)
        new_blob = blur_bucket.blob(file_name)
        new_blob.upload_from_filename(temp_local_filename)
        print(f"Blurred image uploaded to: gs://{blur_bucket_name}/{file_name}")
    
        # Delete the temporary file.
        os.remove(temp_local_filename)
    
    

###  Go 
    
    
    // blur blurs the image stored at gs://inputBucket/name and stores the result in
    // gs://outputBucket/name.
    func blur(ctx context.Context, inputBucket, outputBucket, name string) error {
    	inputBlob := storageClient.Bucket(inputBucket).Object(name)
    	r, err := inputBlob.NewReader(ctx)
    	if err != nil {
    		return fmt.Errorf("NewReader: %w", err)
    	}
    
    	outputBlob := storageClient.Bucket(outputBucket).Object(name)
    	w := outputBlob.NewWriter(ctx)
    	defer w.Close()
    
    	// Use - as input and output to use stdin and stdout.
    	cmd := exec.Command("convert", "-", "-blur", "0x8", "-")
    	cmd.Stdin = r
    	cmd.Stdout = w
    
    	if err := cmd.Run(); err != nil {
    		return fmt.Errorf("cmd.Run: %w", err)
    	}
    
    	log.Printf("Blurred image uploaded to gs://%s/%s", outputBlob.BucketName(), outputBlob.ObjectName())
    
    	return nil
    }
    

###  Java 
    
    
    // Blurs the file described by blobInfo using ImageMagick,
    // and uploads it to the blurred bucket.
    private static void blur(BlobInfo blobInfo) throws IOException {
      String bucketName = blobInfo.getBucket();
      String fileName = blobInfo.getName();
    
      // Download image
      Blob blob = storage.get(BlobId.of(bucketName, fileName));
      Path download = Paths.get("/tmp/", fileName);
      blob.downloadTo(download);
    
      // Construct the command.
      Path upload = Paths.get("/tmp/", "blurred-" + fileName);
      List<String> args = List.of("convert", download.toString(), "-blur", "0x8", upload.toString());
      try {
        ProcessBuilder pb = new ProcessBuilder(args);
        Process process = pb.start();
        process.waitFor();
      } catch (Exception e) {
        logger.info(String.format("Error: %s", e.getMessage()));
      }
    
      // Upload image to blurred bucket.
      BlobId blurredBlobId = BlobId.of(BLURRED_BUCKET_NAME, fileName);
      BlobInfo blurredBlobInfo =
          BlobInfo.newBuilder(blurredBlobId).setContentType(blob.getContentType()).build();
    
      byte[] blurredFile = Files.readAllBytes(upload);
      storage.create(blurredBlobInfo, blurredFile);
      logger.info(
          String.format("Blurred image uploaded to: gs://%s/%s", BLURRED_BUCKET_NAME, fileName));
    
      // Remove images from fileSystem
      Files.delete(download);
      Files.delete(upload);
    }

###  Ruby 
    
    
    require "tempfile"
    require "mini_magick"
    
    # Blurs the given file using ImageMagick.
    def blur_image bucket_name, file_name
      tempfile = Tempfile.new
      begin
        # Download the image file
        bucket = global(:storage_client).bucket bucket_name
        file = bucket.file file_name
        file.download tempfile
        tempfile.close
    
        # Blur the image using ImageMagick
        MiniMagick::Image.new tempfile.path do |image|
          image.blur "0x16"
        end
        logger.info "Image #{file_name} was blurred"
    
        # Upload result to a second bucket, to avoid re-triggering the function.
        # You could instead re-upload it to the same bucket and tell your function
        # to ignore files marked as blurred (e.g. those with a "blurred" prefix.)
        blur_bucket_name = ENV["BLURRED_BUCKET_NAME"]
        blur_bucket = global(:storage_client).bucket blur_bucket_name
        blur_bucket.create_file tempfile.path, file_name
        logger.info "Blurred image uploaded to gs://#{blur_bucket_name}/#{file_name}"
      ensure
        # Ruby will remove the temp file when garbage collecting the object,
        # but it is good practice to remove it explicitly.
        tempfile.unlink
      end
    end

## Deploying the function

**Note:** You must deploy the function with a runtime that is [based on Ubuntu 18.04](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#runtimes). Later runtimes don't include support for ImageMagick.

To deploy your function with a storage trigger, run the following command in the directory that contains the sample code (or in the case of Java, the `pom.xml` file):

### Node.js
    
    
    gcloud functions deploy blurOffensiveImages \
    --no-gen2 \
    --runtime=RUNTIME \
    --trigger-bucket=YOUR_INPUT_BUCKET_NAME \
    --set-env-vars=BLURRED_BUCKET_NAME=YOUR_OUTPUT_BUCKET_NAME
    

### Python
    
    
    gcloud functions deploy blur_offensive_images \
    --no-gen2 \
    --runtime=RUNTIME \
    --trigger-bucket=YOUR_INPUT_BUCKET_NAME \
    --set-env-vars=BLURRED_BUCKET_NAME=YOUR_OUTPUT_BUCKET_NAME
    

### Go
    
    
    gcloud functions deploy BlurOffensiveImages \
    --no-gen2 \
    --runtime=RUNTIME \
    --trigger-bucket=YOUR_INPUT_BUCKET_NAME \
    --set-env-vars=BLURRED_BUCKET_NAME=YOUR_OUTPUT_BUCKET_NAME
    

### Java
    
    
    gcloud functions deploy java-blur-function \
    --no-gen2 \
    --entry-point=functions.ImageMagick \
    --runtime=RUNTIME \
    --memory 512MB \
    --trigger-bucket=YOUR_INPUT_BUCKET_NAME \
    --set-env-vars=BLURRED_BUCKET_NAME=YOUR_OUTPUT_BUCKET_NAME
    

### C#
    
    
    gcloud functions deploy csharp-blur-function \
    --no-gen2 \
    --entry-point=ImageMagick.Function \
    --runtime=RUNTIME \
    --trigger-bucket=YOUR_INPUT_BUCKET_NAME \
    --set-env-vars=BLURRED_BUCKET_NAME=YOUR_OUTPUT_BUCKET_NAME
    

### Ruby
    
    
    gcloud functions deploy blur_offensive_images \
    --no-gen2 \
    --runtime=RUNTIME \
    --trigger-bucket=YOUR_INPUT_BUCKET_NAME \
    --set-env-vars=BLURRED_BUCKET_NAME=YOUR_OUTPUT_BUCKET_NAME
    

Replace the following:

  * `RUNTIME`: a runtime that is [based on Ubuntu 18.04](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#runtimes) (later runtimes don't include support for ImageMagick).
  * `YOUR_INPUT_BUCKET_NAME`: the name of the Cloud Storage bucket for uploading images.
  * `YOUR_OUTPUT_BUCKET_NAME`: the name of the bucket that the blurred images should be saved to.



For this particular example, don't include `gs://` as part of the bucket names in the `deploy` command.

## Uploading an image

  1. Upload an offensive image, such as this image of a [flesh-eating zombie](https://cdn.pixabay.com/photo/2015/09/21/14/24/zombie-949916_960_720.jpg):
         
         gcloud storage cp zombie.jpg gs://YOUR_INPUT_BUCKET_NAME

where `YOUR_INPUT_BUCKET_NAME` is the Cloud Storage bucket you created earlier for uploading images.

  2. Watch the logs to be sure the executions have completed:
         
         gcloud functions logs read --limit 100

  3. You can view the blurred images in the `YOUR_OUTPUT_BUCKET_NAME` Cloud Storage bucket you created earlier.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Deleting the project

The easiest way to eliminate billing is to delete the project that you created for the tutorial. 

To delete the project: 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Deleting the function

Deleting Cloud Run functions does not remove any resources stored in Cloud Storage.

To delete the function you deployed in this tutorial, run the following command:

###  Node.js 
    
    
    gcloud functions delete blurOffensiveImages 

###  Python 
    
    
    gcloud functions delete blur_offensive_images 

###  Go 
    
    
    gcloud functions delete BlurOffensiveImages 

###  Java 
    
    
    gcloud functions delete java-blur-function 

###  Ruby 
    
    
    gcloud functions delete blur_offensive_images 

You can also delete Cloud Run functions from the [Google Cloud console](https://console.cloud.google.com/functions/list).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
