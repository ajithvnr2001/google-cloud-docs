---
url: https://docs.cloud.google.com/run/docs/samples/cloudrun-imageproc-handler-analyze/
title: Use Cloud Vision API to determine if image is safe \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:03:22.807794+00:00
---

# Use Cloud Vision API to determine if image is safe  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/samples/cloudrun-imageproc-handler-analyze/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Samples ](https://docs.cloud.google.com/run/docs/samples)



#  Use Cloud Vision API to determine if image is safe Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial demonstrates using Cloud Run, Cloud Vision API, and ImageMagick to detect and blur offensive images uploaded to a Cloud Storage bucket.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Process images from Cloud Storage tutorial](https://docs.cloud.google.com/run/docs/tutorials/image-processing)



## Code sample

### Go

To authenticate to Cloud Run, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    

### Java

To authenticate to Cloud Run, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Blurs uploaded images that are flagged as Adult or Violence.
    public static void blurOffensiveImages(JsonObject data) {
      String fileName = data.get("name").getAsString();
      String bucketName = data.get("bucket").getAsString();
      BlobInfo blobInfo = BlobInfo.newBuilder(bucketName, fileName).build();
      // Construct URI to GCS bucket and file.
      String gcsPath = String.format("gs://%s/%s", bucketName, fileName);
      System.out.println(String.format("Analyzing %s", fileName));
    
      // Construct request.
      List<AnnotateImageRequest> requests = new ArrayList<>();
      ImageSource imgSource = ImageSource.newBuilder().setImageUri(gcsPath).build();
      Image img = Image.newBuilder().setSource(imgSource).build();
      Feature feature = Feature.newBuilder().setType(Type.SAFE_SEARCH_DETECTION).build();
      AnnotateImageRequest request =
          AnnotateImageRequest.newBuilder().addFeatures(feature).setImage(img).build();
      requests.add(request);
    
      // Send request to the Vision API.
      try (ImageAnnotatorClient client = ImageAnnotatorClient.create()) {
        BatchAnnotateImagesResponse response = client.batchAnnotateImages(requests);
        List<AnnotateImageResponse> responses = response.getResponsesList();
        for (AnnotateImageResponse res : responses) {
          if (res.hasError()) {
            System.out.println(String.format("Error: %s\n", res.getError().getMessage()));
            return;
          }
          // Get Safe Search Annotations
          SafeSearchAnnotation annotation = res.getSafeSearchAnnotation();
          if (annotation.getAdultValue() == 5 || annotation.getViolenceValue() == 5) {
            System.out.println(String.format("Detected %s as inappropriate.", fileName));
            blur(blobInfo);
          } else {
            System.out.println(String.format("Detected %s as OK.", fileName));
          }
        }
      } catch (Exception e) {
        System.out.println(String.format("Error with Vision API: %s", e.getMessage()));
      }
    }

### Node.js

To authenticate to Cloud Run, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
          return blurImage(file, BLURRED_BUCKET_NAME);
        } else {
          console.log(`Detected ${file.name} as OK.`);
        }
      } catch (err) {
        console.error(`Failed to analyze ${file.name}.`, err);
        throw err;
      }
    };

### Python

To authenticate to Cloud Run, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def blur_offensive_images(data):
        """Blurs uploaded images that are flagged as Adult or Violence.
    
        Args:
            data: Pub/Sub message data
        """
        file_data = data
    
        file_name = file_data["name"]
        bucket_name = file_data["bucket"]
    
        blob = storage_client.bucket(bucket_name).get_blob(file_name)
        blob_uri = f"gs://{bucket_name}/{file_name}"
        blob_source = vision.Image(source=vision.ImageSource(image_uri=blob_uri))
    
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
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudrun). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
