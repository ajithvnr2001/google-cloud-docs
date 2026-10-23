---
url: https://docs.cloud.google.com/run/docs/samples/cloudrun-imageproc-handler-blur/
title: Retrieve image from Cloud Storage to blur and then upload to a storage bucket \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:03:22.301688+00:00
---

# Retrieve image from Cloud Storage to blur and then upload to a storage bucket  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/samples/cloudrun-imageproc-handler-blur/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Samples ](https://docs.cloud.google.com/run/docs/samples)



#  Retrieve image from Cloud Storage to blur and then upload to a storage bucket Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial demonstrates using Cloud Run, Cloud Vision API, and ImageMagick to detect and blur offensive images uploaded to a Cloud Storage bucket.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Process images from Cloud Storage tutorial](https://docs.cloud.google.com/run/docs/tutorials/image-processing)



## Code sample

### Go

To authenticate to Cloud Run, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    

### Java

To authenticate to Cloud Run, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
      // Blurs the file described by blobInfo using ImageMagick,
      // and uploads it to the blurred bucket.
      public static void blur(BlobInfo blobInfo) throws IOException {
        String bucketName = blobInfo.getBucket();
        String fileName = blobInfo.getName();
        // Download image
        Blob blob = storage.get(BlobId.of(bucketName, fileName));
        Path download = Paths.get("/tmp/", fileName);
        blob.downloadTo(download);
    
        // Construct the command.
        List<String> args = new ArrayList<>();
        args.add("convert");
        args.add(download.toString());
        args.add("-blur");
        args.add("0x8");
        Path upload = Paths.get("/tmp/", "blurred-" + fileName);
        args.add(upload.toString());
        try {
          ProcessBuilder pb = new ProcessBuilder(args);
          Process process = pb.start();
          process.waitFor();
        } catch (Exception e) {
          System.out.println(String.format("Error: %s", e.getMessage()));
        }
    
        // Upload image to blurred bucket.
        BlobId blurredBlobId = BlobId.of(BLURRED_BUCKET_NAME, fileName);
        BlobInfo blurredBlobInfo =
            BlobInfo.newBuilder(blurredBlobId).setContentType(blob.getContentType()).build();
        try {
          byte[] blurredFile = Files.readAllBytes(upload);
          Blob blurredBlob = storage.create(blurredBlobInfo, blurredFile);
          System.out.println(
              String.format("Blurred image uploaded to: gs://%s/%s", BLURRED_BUCKET_NAME, fileName));
        } catch (Exception e) {
          System.out.println(String.format("Error in upload: %s", e.getMessage()));
        }
    
        // Remove images from fileSystem
        Files.delete(download);
        Files.delete(upload);
      }
    }

### Node.js

To authenticate to Cloud Run, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### Python

To authenticate to Cloud Run, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def __blur_image(current_blob):
        """Blurs the given file using ImageMagick.
    
        Args:
            current_blob: a Cloud Storage blob
        """
        file_name = current_blob.name
        _, temp_local_filename = tempfile.mkstemp()
    
        # Download file from bucket.
        current_blob.download_to_filename(temp_local_filename)
        print(f"Image {file_name} was downloaded to {temp_local_filename}.")
    
        # Blur the image using ImageMagick.
        with Image(filename=temp_local_filename) as image:
            image.resize(*image.size, blur=16, filter="hamming")
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
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudrun). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
