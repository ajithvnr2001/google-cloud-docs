---
url: https://docs.cloud.google.com/vision/docs/samples/vision-text-detection-pdf-gcs/
title: Detect text in a PDF file in Cloud Storage \u00a0|\u00a0 Cloud Vision API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:27:10.161577+00:00
---

# Detect text in a PDF file in Cloud Storage  |  Cloud Vision API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/docs/samples/vision-text-detection-pdf-gcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Vision API ](https://docs.cloud.google.com/vision/docs)
  * [ Samples ](https://docs.cloud.google.com/vision/docs/samples)



#  Detect text in a PDF file in Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

Perform optical character recognition (OCR) on a PDF file stored in Cloud Storage.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Detect text in files (PDF/TIFF)](https://docs.cloud.google.com/vision/docs/pdf)



## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Go API reference documentation](https://godoc.org/cloud.google.com/go/vision/apiv1). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // detectAsyncDocumentURI performs Optical Character Recognition (OCR) on a
    // PDF file stored in GCS.
    func detectAsyncDocumentURI(w io.Writer, gcsSourceURI, gcsDestinationURI string) error {
    	ctx := context.Background()
    
    	client, err := vision.NewImageAnnotatorClient(ctx)
    	if err != nil {
    		return err
    	}
    
    	request := &visionpb.AsyncBatchAnnotateFilesRequest{
    		Requests: []*visionpb.AsyncAnnotateFileRequest{
    			{
    				Features: []*visionpb.Feature{
    					{
    						Type: visionpb.Feature_DOCUMENT_TEXT_DETECTION,
    					},
    				},
    				InputConfig: &visionpb.InputConfig{
    					GcsSource: &visionpb.GcsSource{Uri: gcsSourceURI},
    					// Supported MimeTypes are: "application/pdf" and "image/tiff".
    					MimeType: "application/pdf",
    				},
    				OutputConfig: &visionpb.OutputConfig{
    					GcsDestination: &visionpb.GcsDestination{Uri: gcsDestinationURI},
    					// How many pages should be grouped into each json output file.
    					BatchSize: 2,
    				},
    			},
    		},
    	}
    
    	operation, err := client.AsyncBatchAnnotateFiles(ctx, request)
    	if err != nil {
    		return err
    	}
    
    	fmt.Fprintf(w, "Waiting for the operation to finish.")
    
    	resp, err := operation.Wait(ctx)
    	if err != nil {
    		return err
    	}
    
    	fmt.Fprintf(w, "%v", resp)
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Performs document text OCR with PDF/TIFF as source files on Google Cloud Storage.
     *
     * @param gcsSourcePath The path to the remote file on Google Cloud Storage to detect document
     *     text on.
     * @param gcsDestinationPath The path to the remote file on Google Cloud Storage to store the
     *     results on.
     * @throws Exception on errors while closing the client.
     */
    public static void detectDocumentsGcs(String gcsSourcePath, String gcsDestinationPath)
        throws Exception {
    
      // Initialize client that will be used to send requests. This client only needs to be created
      // once, and can be reused for multiple requests. After completing all of your requests, call
      // the "close" method on the client to safely clean up any remaining background resources.
      try (ImageAnnotatorClient client = ImageAnnotatorClient.create()) {
        List<AsyncAnnotateFileRequest> requests = new ArrayList<>();
    
        // Set the GCS source path for the remote file.
        GcsSource gcsSource = GcsSource.newBuilder().setUri(gcsSourcePath).build();
    
        // Create the configuration with the specified MIME (Multipurpose Internet Mail Extensions)
        // types
        InputConfig inputConfig =
            InputConfig.newBuilder()
                .setMimeType(
                    "application/pdf") // Supported MimeTypes: "application/pdf", "image/tiff"
                .setGcsSource(gcsSource)
                .build();
    
        // Set the GCS destination path for where to save the results.
        GcsDestination gcsDestination =
            GcsDestination.newBuilder().setUri(gcsDestinationPath).build();
    
        // Create the configuration for the System.output with the batch size.
        // The batch size sets how many pages should be grouped into each json System.output file.
        OutputConfig outputConfig =
            OutputConfig.newBuilder().setBatchSize(2).setGcsDestination(gcsDestination).build();
    
        // Select the Feature required by the vision API
        Feature feature = Feature.newBuilder().setType(Feature.Type.DOCUMENT_TEXT_DETECTION).build();
    
        // Build the OCR request
        AsyncAnnotateFileRequest request =
            AsyncAnnotateFileRequest.newBuilder()
                .addFeatures(feature)
                .setInputConfig(inputConfig)
                .setOutputConfig(outputConfig)
                .build();
    
        requests.add(request);
    
        // Perform the OCR request
        OperationFuture<AsyncBatchAnnotateFilesResponse, OperationMetadata> response =
            client.asyncBatchAnnotateFilesAsync(requests);
    
        System.out.println("Waiting for the operation to finish.");
    
        // Wait for the request to finish. (The result is not used, since the API saves the result to
        // the specified location on GCS.)
        List<AsyncAnnotateFileResponse> result =
            response.get(180, TimeUnit.SECONDS).getResponsesList();
    
        // Once the request has completed and the System.output has been
        // written to GCS, we can list all the System.output files.
        Storage storage = StorageOptions.getDefaultInstance().getService();
    
        // Get the destination location from the gcsDestinationPath
        Pattern pattern = Pattern.compile("gs://([^/]+)/(.+)");
        Matcher matcher = pattern.matcher(gcsDestinationPath);
    
        if (matcher.find()) {
          String bucketName = matcher.group(1);
          String prefix = matcher.group(2);
    
          // Get the list of objects with the given prefix from the GCS bucket
          Bucket bucket = storage.get(bucketName);
          com.google.api.gax.paging.Page<Blob> pageList = bucket.list(BlobListOption.prefix(prefix));
    
          Blob firstOutputFile = null;
    
          // List objects with the given prefix.
          System.out.println("Output files:");
          for (Blob blob : pageList.iterateAll()) {
            System.out.println(blob.getName());
    
            // Process the first System.output file from GCS.
            // Since we specified batch size = 2, the first response contains
            // the first two pages of the input file.
            if (firstOutputFile == null) {
              firstOutputFile = blob;
            }
          }
    
          // Get the contents of the file and convert the JSON contents to an AnnotateFileResponse
          // object. If the Blob is small read all its content in one request
          // (Note: the file is a .json file)
          // Storage guide: https://cloud.google.com/storage/docs/downloading-objects
          String jsonContents = new String(firstOutputFile.getContent());
          Builder builder = AnnotateFileResponse.newBuilder();
          JsonFormat.parser().merge(jsonContents, builder);
    
          // Build the AnnotateFileResponse object
          AnnotateFileResponse annotateFileResponse = builder.build();
    
          // Parse through the object to get the actual response for the first page of the input file.
          AnnotateImageResponse annotateImageResponse = annotateFileResponse.getResponses(0);
    
          // Here we print the full text from the first page.
          // The response contains more information:
          // annotation/pages/blocks/paragraphs/words/symbols
          // including confidence score and bounding boxes
          System.out.format("%nText: %s%n", annotateImageResponse.getFullTextAnnotation().getText());
        } else {
          System.out.println("No MATCH");
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Node.js API reference documentation](https://googleapis.dev/nodejs/vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client libraries
    const vision = require('[@google-cloud/vision](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)').v1;
    
    // Creates a client
    const client = new vision.[ImageAnnotatorClient](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)();
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // Bucket where the file resides
    // const bucketName = 'my-bucket';
    // Path to PDF file within bucket
    // const fileName = 'path/to/document.pdf';
    // The folder to store the results
    // const outputPrefix = 'results'
    
    const gcsSourceUri = `gs://${bucketName}/${fileName}`;
    const gcsDestinationUri = `gs://${bucketName}/${outputPrefix}/`;
    
    const inputConfig = {
      // Supported mime_types are: 'application/pdf' and 'image/tiff'
      mimeType: 'application/pdf',
      gcsSource: {
        uri: gcsSourceUri,
      },
    };
    const outputConfig = {
      gcsDestination: {
        uri: gcsDestinationUri,
      },
    };
    const features = [{type: 'DOCUMENT_TEXT_DETECTION'}];
    const request = {
      requests: [
        {
          inputConfig: inputConfig,
          features: features,
          outputConfig: outputConfig,
        },
      ],
    };
    
    const [operation] = await client.asyncBatchAnnotateFiles(request);
    const [filesResponse] = await operation.promise();
    const destinationUri =
      filesResponse.responses[0].outputConfig.gcsDestination.uri;
    console.log('Json saved to: ' + destinationUri);

### PHP

Before trying this sample, follow the PHP setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision PHP API reference documentation](https://docs.cloud.google.com/php/docs/reference/cloud-vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace Google\Cloud\Samples\Vision;
    
    use Google\Cloud\Storage\StorageClient;
    use Google\Cloud\Vision\V1\AnnotateFileResponse;
    use Google\Cloud\Vision\V1\AsyncAnnotateFileRequest;
    use Google\Cloud\Vision\V1\AsyncBatchAnnotateFilesRequest;
    use Google\Cloud\Vision\V1\Client\ImageAnnotatorClient;
    use Google\Cloud\Vision\V1\Feature;
    use Google\Cloud\Vision\V1\Feature\Type;
    use Google\Cloud\Vision\V1\GcsDestination;
    use Google\Cloud\Vision\V1\GcsSource;
    use Google\Cloud\Vision\V1\InputConfig;
    use Google\Cloud\Vision\V1\OutputConfig;
    
    /**
     * @param string $path    GCS path to the document, e.g. "gs://path/to/your/document.pdf"
     * @param string $output  GCS path to store the results, e.g. "gs://path/to/store/results/"
     */
    function detect_pdf_gcs(string $path, string $output)
    {
        # select ocr feature
        $feature = (new Feature())
            ->setType(Type::DOCUMENT_TEXT_DETECTION);
    
        # set $path (file to OCR) as source
        $gcsSource = (new GcsSource())
            ->setUri($path);
        # supported mime_types are: 'application/pdf' and 'image/tiff'
        $mimeType = 'application/pdf';
        $inputConfig = (new InputConfig())
            ->setGcsSource($gcsSource)
            ->setMimeType($mimeType);
    
        # set $output as destination
        $gcsDestination = (new GcsDestination())
            ->setUri($output);
        # how many pages should be grouped into each json output file.
        $batchSize = 2;
        $outputConfig = (new OutputConfig())
            ->setGcsDestination($gcsDestination)
            ->setBatchSize($batchSize);
    
        # prepare request using configs set above
        $request = (new AsyncAnnotateFileRequest())
            ->setFeatures([$feature])
            ->setInputConfig($inputConfig)
            ->setOutputConfig($outputConfig);
        $requests = [$request];
    
        # make request
        $imageAnnotator = new ImageAnnotatorClient();
        $request = (new AsyncBatchAnnotateFilesRequest())
            ->setRequests($requests);
        $operation = $imageAnnotator->asyncBatchAnnotateFiles($request);
        print('Waiting for operation to finish.' . PHP_EOL);
        $operation->pollUntilComplete();
    
        # once the request has completed and the output has been
        # written to GCS, we can list all the output files.
        preg_match('/^gs:\/\/([a-zA-Z0-9\._\-]+)\/?(\S+)?$/', $output, $match);
        $bucketName = $match[1];
        $prefix = isset($match[2]) ? $match[2] : '';
    
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
        $options = ['prefix' => $prefix];
        $objects = $bucket->objects($options);
    
        # save first object for sample below
        $objects->next();
        $firstObject = $objects->current();
    
        # list objects with the given prefix.
        print('Output files:' . PHP_EOL);
        foreach ($objects as $object) {
            print($object->name() . PHP_EOL);
        }
    
        # process the first output file from GCS.
        # since we specified batch_size=2, the first response contains
        # the first two pages of the input file.
        $jsonString = $firstObject->downloadAsString();
        $firstBatch = new AnnotateFileResponse();
        $firstBatch->mergeFromJsonString($jsonString);
    
        # get annotation and print text
        foreach ($firstBatch->getResponses() as $response) {
            $annotation = $response->getFullTextAnnotation();
            print($annotation->getText());
        }
    
        $imageAnnotator->close();
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def async_detect_document(gcs_source_uri, gcs_destination_uri):
        """OCR with PDF/TIFF as source files on GCS"""
        import json
        import re
        from google.cloud import vision
        from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
        # Supported mime_types are: 'application/pdf' and 'image/tiff'
        mime_type = "application/pdf"
    
        # How many pages should be grouped into each json output file.
        batch_size = 2
    
        client = vision.[ImageAnnotatorClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.image_annotator.ImageAnnotatorClient.html)()
    
        feature = vision.[Feature](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.Feature.html)(type_=vision.[Feature](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.Feature.html).Type.DOCUMENT_TEXT_DETECTION)
    
        gcs_source = vision.[GcsSource](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.GcsSource.html)(uri=gcs_source_uri)
        input_config = vision.[InputConfig](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.InputConfig.html)(gcs_source=gcs_source, mime_type=mime_type)
    
        gcs_destination = vision.[GcsDestination](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.GcsDestination.html)(uri=gcs_destination_uri)
        output_config = vision.[OutputConfig](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.OutputConfig.html)(
            gcs_destination=gcs_destination, batch_size=batch_size
        )
    
        async_request = vision.[AsyncAnnotateFileRequest](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.AsyncAnnotateFileRequest.html)(
            features=[feature], input_config=input_config, output_config=output_config
        )
    
        operation = client.[async_batch_annotate_files](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.image_annotator.ImageAnnotatorClient.html#google_cloud_vision_v1_services_image_annotator_ImageAnnotatorClient_async_batch_annotate_files)(requests=[async_request])
    
        print("Waiting for the operation to finish.")
        operation.result(timeout=420)
    
        # Once the request has completed and the output has been
        # written to GCS, we can list all the output files.
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
        match = re.match(r"gs://([^/]+)/(.+)", gcs_destination_uri)
        bucket_name = match.[group](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.acl.ACL.html#google_cloud_storage_acl_ACL_group)(1)
        prefix = match.[group](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.acl.ACL.html#google_cloud_storage_acl_ACL_group)(2)
    
        bucket = storage_client.[get_bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_get_bucket)(bucket_name)
    
        # List objects with the given prefix, filtering out folders.
        blob_list = [
            blob
            for blob in list(bucket.list_blobs(prefix=prefix))
            if not blob.name.endswith("/")
        ]
        print("Output files:")
        for blob in blob_list:
            print(blob.name)
    
        # Process the first output file from GCS.
        # Since we specified batch_size=2, the first response contains
        # the first two pages of the input file.
        output = blob_list[0]
    
        json_string = output.[download_as_bytes](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_bytes)().decode("utf-8")
        response = json.loads(json_string)
    
        # The actual response for the first page of the input file.
        first_page_response = response["responses"][0]
        annotation = first_page_response["fullTextAnnotation"]
    
        # Here we print the full text from the first page.
        # The response contains more information:
        # annotation/pages/blocks/paragraphs/words/symbols
        # including confidence scores and bounding boxes
        print("Full text:\n")
        print(annotation["text"])
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudvision). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
