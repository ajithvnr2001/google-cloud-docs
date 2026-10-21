---
url: https://docs.cloud.google.com/vision/docs/samples/vision-batch-annotate-files-gcs/
title: Annotate a batch of files in Cloud Storage \u00a0|\u00a0 Cloud Vision API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:27:09.367366+00:00
---

# Annotate a batch of files in Cloud Storage  |  Cloud Vision API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/docs/samples/vision-batch-annotate-files-gcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Vision API ](https://docs.cloud.google.com/vision/docs)
  * [ Samples ](https://docs.cloud.google.com/vision/docs/samples)



#  Annotate a batch of files in Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

Annotate a batch of files in Cloud Storage while online.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Small batch file annotation online](https://docs.cloud.google.com/vision/docs/file-small-batch)



## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.vision.v1.[AnnotateFileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateFileRequest.html);
    import com.google.cloud.vision.v1.[AnnotateImageResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageResponse.html);
    import com.google.cloud.vision.v1.[BatchAnnotateFilesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.BatchAnnotateFilesRequest.html);
    import com.google.cloud.vision.v1.[BatchAnnotateFilesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.BatchAnnotateFilesResponse.html);
    import com.google.cloud.vision.v1.[Block](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Block.html);
    import com.google.cloud.vision.v1.[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html);
    import com.google.cloud.vision.v1.[GcsSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.GcsSource.html);
    import com.google.cloud.vision.v1.[ImageAnnotatorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageAnnotatorClient.html);
    import com.google.cloud.vision.v1.[InputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.InputConfig.html);
    import com.google.cloud.vision.v1.[Page](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Page.html);
    import com.google.cloud.vision.v1.[Paragraph](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Paragraph.html);
    import com.google.cloud.vision.v1.[Symbol](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Symbol.html);
    import com.google.cloud.vision.v1.[Word](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Word.html);
    import java.io.IOException;
    
    public class BatchAnnotateFilesGcs {
    
      public static void batchAnnotateFilesGcs() throws IOException {
        String gcsUri = "gs://cloud-samples-data/vision/document_understanding/kafka.pdf";
        batchAnnotateFilesGcs(gcsUri);
      }
    
      public static void batchAnnotateFilesGcs(String gcsUri) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([ImageAnnotatorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageAnnotatorClient.html) imageAnnotatorClient = [ImageAnnotatorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageAnnotatorClient.html).create()) {
          // You can send multiple files to be annotated, this sample demonstrates how to do this with
          // one file. If you want to use multiple files, you have to create a `AnnotateImageRequest`
          // object for each file that you want annotated.
          // First specify where the vision api can find the image
          [GcsSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.GcsSource.html) gcsSource = [GcsSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.GcsSource.html).newBuilder().setUri(gcsUri).build();
    
          // Specify the input config with the file's uri and its type.
          // Supported mime_type: application/pdf, image/tiff, image/gif
          // https://cloud.google.com/vision/docs/reference/rpc/google.cloud.vision.v1#inputconfig
          [InputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.InputConfig.html) inputConfig =
              [InputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.InputConfig.html).newBuilder().[setMimeType](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.InputConfig.Builder.html#com_google_cloud_vision_v1_InputConfig_Builder_setMimeType_java_lang_String_)("application/pdf").setGcsSource(gcsSource).build();
    
          // Set the type of annotation you want to perform on the file
          // https://cloud.google.com/vision/docs/reference/rpc/google.cloud.vision.v1#google.cloud.vision.v1.Feature.Type
          [Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html) feature = [Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html).newBuilder().setType([Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html).Type.DOCUMENT_TEXT_DETECTION).build();
    
          // Build the request object for that one file. Note: for additional file you have to create
          // additional `AnnotateFileRequest` objects and store them in a list to be used below.
          // Since we are sending a file of type `application/pdf`, we can use the `pages` field to
          // specify which pages to process. The service can process up to 5 pages per document file.
          // https://cloud.google.com/vision/docs/reference/rpc/google.cloud.vision.v1#google.cloud.vision.v1.AnnotateFileRequest
          [AnnotateFileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateFileRequest.html) fileRequest =
              [AnnotateFileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateFileRequest.html).newBuilder()
                  .setInputConfig(inputConfig)
                  .addFeatures(feature)
                  .addPages(1) // Process the first page
                  .addPages(2) // Process the second page
                  .addPages(-1) // Process the last page
                  .build();
    
          // Add each `AnnotateFileRequest` object to the batch request.
          [BatchAnnotateFilesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.BatchAnnotateFilesRequest.html) request =
              [BatchAnnotateFilesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.BatchAnnotateFilesRequest.html).newBuilder().addRequests(fileRequest).build();
    
          // Make the synchronous batch request.
          [BatchAnnotateFilesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.BatchAnnotateFilesResponse.html) response = imageAnnotatorClient.batchAnnotateFiles(request);
    
          // Process the results, just get the first result, since only one file was sent in this
          // sample.
          for ([AnnotateImageResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageResponse.html) imageResponse :
              response.[getResponsesList](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.BatchAnnotateFilesResponse.html#com_google_cloud_vision_v1_BatchAnnotateFilesResponse_getResponsesList__)().get(0).getResponsesList()) {
            System.out.format("Full text: %s%n", imageResponse.getFullTextAnnotation().getText());
            for ([Page](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Page.html) page : imageResponse.getFullTextAnnotation().getPagesList()) {
              for ([Block](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Block.html) block : page.getBlocksList()) {
                System.out.format("%nBlock confidence: %s%n", block.getConfidence());
                for ([Paragraph](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Paragraph.html) par : block.getParagraphsList()) {
                  System.out.format("\tParagraph confidence: %s%n", par.getConfidence());
                  for ([Word](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Word.html) word : par.getWordsList()) {
                    System.out.format("\t\tWord confidence: %s%n", word.getConfidence());
                    for ([Symbol](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Symbol.html) symbol : word.getSymbolsList()) {
                      System.out.format(
                          "\t\t\tSymbol: %s, (confidence: %s)%n",
                          symbol.getText(), symbol.getConfidence());
                    }
                  }
                }
              }
            }
          }
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Node.js API reference documentation](https://googleapis.dev/nodejs/vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const gcsSourceUri = 'gs://cloud-samples-data/vision/document_understanding/kafka.pdf';
    
    // Imports the Google Cloud client libraries
    const {ImageAnnotatorClient} = require('[@google-cloud/vision](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)').v1;
    
    // Instantiates a client
    const client = new [ImageAnnotatorClient](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)();
    
    // You can send multiple files to be annotated, this sample demonstrates how to do this with
    // one file. If you want to use multiple files, you have to create a request object for each file that you want annotated.
    async function batchAnnotateFiles() {
      // First Specify the input config with the file's uri and its type.
      // Supported mime_type: application/pdf, image/tiff, image/gif
      // https://cloud.google.com/vision/docs/reference/rpc/google.cloud.vision.v1#inputconfig
      const inputConfig = {
        mimeType: 'application/pdf',
        gcsSource: {
          uri: gcsSourceUri,
        },
      };
    
      // Set the type of annotation you want to perform on the file
      // https://cloud.google.com/vision/docs/reference/rpc/google.cloud.vision.v1#google.cloud.vision.v1.Feature.Type
      const features = [{type: 'DOCUMENT_TEXT_DETECTION'}];
    
      // Build the request object for that one file. Note: for additional files you have to create
      // additional file request objects and store them in a list to be used below.
      // Since we are sending a file of type `application/pdf`, we can use the `pages` field to
      // specify which pages to process. The service can process up to 5 pages per document file.
      // https://cloud.google.com/vision/docs/reference/rpc/google.cloud.vision.v1#google.cloud.vision.v1.AnnotateFileRequest
      const fileRequest = {
        inputConfig: inputConfig,
        features: features,
        // Annotate the first two pages and the last one (max 5 pages)
        // First page starts at 1, and not 0. Last page is -1.
        pages: [1, 2, -1],
      };
    
      // Add each `AnnotateFileRequest` object to the batch request.
      const request = {
        requests: [fileRequest],
      };
    
      // Make the synchronous batch request.
      const [result] = await client.batchAnnotateFiles(request);
    
      // Process the results, just get the first result, since only one file was sent in this
      // sample.
      const responses = result.responses[0].responses;
    
      for (const response of responses) {
        console.log(`Full text: ${response.fullTextAnnotation.text}`);
        for (const page of response.fullTextAnnotation.pages) {
          for (const block of page.blocks) {
            console.log(`Block confidence: ${block.confidence}`);
            for (const paragraph of block.paragraphs) {
              console.log(` Paragraph confidence: ${paragraph.confidence}`);
              for (const word of paragraph.words) {
                const symbol_texts = word.symbols.map(symbol => symbol.text);
                const word_text = symbol_texts.join('');
                console.log(
                  `  Word text: ${word_text} (confidence: ${word.confidence})`
                );
                for (const symbol of word.symbols) {
                  console.log(
                    `   Symbol: ${symbol.text} (confidence: ${symbol.confidence})`
                  );
                }
              }
            }
          }
        }
      }
    }
    
    batchAnnotateFiles();

### Python

Before trying this sample, follow the Python setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [vision_v1](https://docs.cloud.google.com/python/docs/reference/vision/latest)
    
    
    def sample_batch_annotate_files(
        storage_uri="gs://cloud-samples-data/vision/document_understanding/kafka.pdf",
    ):
        """Perform batch file annotation."""
        mime_type = "application/pdf"
    
        client = [vision_v1](https://docs.cloud.google.com/python/docs/reference/vision/latest).[ImageAnnotatorClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.image_annotator.ImageAnnotatorClient.html)()
    
        gcs_source = {"uri": storage_uri}
        input_config = {"gcs_source": gcs_source, "mime_type": mime_type}
        features = [{"type_": [vision_v1](https://docs.cloud.google.com/python/docs/reference/vision/latest).[Feature](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.Feature.html).Type.DOCUMENT_TEXT_DETECTION}]
    
        # The service can process up to 5 pages per document file.
        # Here we specify the first, second, and last page of the document to be
        # processed.
        pages = [1, 2, -1]
        requests = [{"input_config": input_config, "features": features, "pages": pages}]
    
        response = client.[batch_annotate_files](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.image_annotator.ImageAnnotatorClient.html#google_cloud_vision_v1_services_image_annotator_ImageAnnotatorClient_batch_annotate_files)(requests=requests)
        for image_response in response.responses[0].responses:
            print(f"Full text: {image_response.full_text_annotation.text}")
            for page in image_response.full_text_annotation.pages:
                for block in page.blocks:
                    print(f"\nBlock confidence: {block.confidence}")
                    for par in block.paragraphs:
                        print(f"\tParagraph confidence: {par.confidence}")
                        for word in par.words:
                            print(f"\t\tWord confidence: {word.confidence}")
                            for symbol in word.symbols:
                                print(
                                    "\t\t\tSymbol: {}, (confidence: {})".format(
                                        symbol.text, symbol.confidence
                                    )
                                )
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudvision). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
