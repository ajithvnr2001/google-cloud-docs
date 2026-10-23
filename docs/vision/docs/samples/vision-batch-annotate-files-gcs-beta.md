---
url: https://docs.cloud.google.com/vision/docs/samples/vision-batch-annotate-files-gcs-beta/
title: Annotate a batch of files in Cloud Storage (beta) \u00a0|\u00a0 Cloud Vision API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:59.794144+00:00
---

# Annotate a batch of files in Cloud Storage (beta)  |  Cloud Vision API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/docs/samples/vision-batch-annotate-files-gcs-beta/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Vision API ](https://docs.cloud.google.com/vision/docs)
  * [ Samples ](https://docs.cloud.google.com/vision/docs/samples)



#  Annotate a batch of files in Cloud Storage (beta) Stay organized with collections  Save and categorize content based on your preferences. 

Annotate a batch of files in Cloud Storage while online.

## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.core.[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html);
    import com.google.cloud.vision.v1p4beta1.AnnotateFileRequest;
    import com.google.cloud.vision.v1p4beta1.AnnotateFileResponse;
    import com.google.cloud.vision.v1p4beta1.BatchAnnotateFilesRequest;
    import com.google.cloud.vision.v1p4beta1.BatchAnnotateFilesResponse;
    import com.google.cloud.vision.v1p4beta1.Block;
    import com.google.cloud.vision.v1p4beta1.Feature;
    import com.google.cloud.vision.v1p4beta1.Feature.Type;
    import com.google.cloud.vision.v1p4beta1.GcsSource;
    import com.google.cloud.vision.v1p4beta1.ImageAnnotatorClient;
    import com.google.cloud.vision.v1p4beta1.InputConfig;
    import com.google.cloud.vision.v1p4beta1.Page;
    import com.google.cloud.vision.v1p4beta1.Paragraph;
    import com.google.cloud.vision.v1p4beta1.Symbol;
    import com.google.cloud.vision.v1p4beta1.TextAnnotation;
    import com.google.cloud.vision.v1p4beta1.Word;
    import java.util.ArrayList;
    import java.util.Arrays;
    import java.util.List;
    
    public class DetectBatchAnnotateFilesGcs {
    
      // Performs document feature detection on a remote PDF/TIFF/GIF file on Google Cloud Storage.
      public static void detectBatchAnnotateFilesGcs(String gcsPath) {
        // String gcsPath = "gs://Your_BUCKET_ID/path_to_your_data";
    
        try (ImageAnnotatorClient client = ImageAnnotatorClient.[create](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.SettableApiFuture.html#com_google_api_core_SettableApiFuture__V_create__)()) {
          // Annotate the first two pages and the last one (max 5 pages)
          // First page starts at 1, and not 0. Last page is -1.
          List<Integer> pages = Arrays.asList(1, 2, -1);
          GcsSource gcsSource = GcsSource.newBuilder().setUri(gcsPath).build();
          Feature feat = Feature.newBuilder().setType(Type.DOCUMENT_TEXT_DETECTION).build();
          // Other supported mime types : 'image/tiff' or 'image/gif'
          InputConfig inputConfig =
              InputConfig.newBuilder().setMimeType("application/pdf").setGcsSource(gcsSource).build();
          AnnotateFileRequest request =
              AnnotateFileRequest.newBuilder()
                  .addFeatures(feat)
                  .setInputConfig(inputConfig)
                  .addAllPages(pages)
                  .build();
          List<AnnotateFileRequest> requests = new ArrayList<>();
          requests.add(request);
    
          BatchAnnotateFilesRequest batchAnnotateFilesRequest =
              BatchAnnotateFilesRequest.newBuilder().addAllRequests(requests).build();
          ApiFuture<BatchAnnotateFilesResponse> future =
              client.batchAnnotateFilesCallable().futureCall(batchAnnotateFilesRequest);
          BatchAnnotateFilesResponse response = future.get();
    
          // Getting the first response
          AnnotateFileResponse annotateFileResponse = response.getResponses(0);
    
          // For full list of available annotations, see http://g.co/cloud/vision/docs
          TextAnnotation textAnnotation = annotateFileResponse.getResponses(0).getFullTextAnnotation();
          for (Page page : textAnnotation.getPagesList()) {
            String pageText = "";
            for (Block block : page.getBlocksList()) {
              String blockText = "";
              for (Paragraph para : block.getParagraphsList()) {
                String paraText = "";
                for (Word word : para.getWordsList()) {
                  String wordText = "";
                  for (Symbol symbol : word.getSymbolsList()) {
                    wordText = wordText + symbol.getText();
                    System.out.format(
                        "Symbol text: %s (Confidence: %f)\n", symbol.getText(), symbol.getConfidence());
                  }
                  System.out.format(
                      "Word text: %s (Confidence: %f)\n\n", wordText, word.getConfidence());
                  paraText = String.format("%s %s", paraText, wordText);
                }
                // Output Example using Paragraph:
                System.out.println("\nParagraph: \n" + paraText);
                System.out.format("Paragraph Confidence: %f\n", para.getConfidence());
                blockText = blockText + paraText;
              }
              pageText = pageText + blockText;
            }
          }
          System.out.println("\nComplete annotation:");
          System.out.println(textAnnotation.getText());
    
        } catch (Exception e) {
          System.out.println("Error during detectPdfText: \n" + e.toString());
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def detect_batch_annotate_files_uri(gcs_uri):
        """Detects document features in a PDF/TIFF/GIF file.
    
        While your PDF file may have several pages,
        this API can process up to 5 pages only.
    
        Args:
        uri: The path to the file in Google Cloud Storage (gs://...)
        """
        from google.cloud import vision_v1p4beta1 as vision
    
        client = vision.ImageAnnotatorClient()
    
        # Other supported mime_types: image/tiff' or 'image/gif'
        mime_type = "application/pdf"
        input_config = vision.InputConfig(
            gcs_source=vision.GcsSource(uri=gcs_uri), mime_type=mime_type
        )
    
        feature = vision.Feature(type_=vision.Feature.Type.DOCUMENT_TEXT_DETECTION)
        # Annotate the first two pages and the last one (max 5 pages)
        # First page starts at 1, and not 0. Last page is -1.
        pages = [1, 2, -1]
    
        request = vision.AnnotateFileRequest(
            input_config=input_config, features=[feature], pages=pages
        )
    
        response = client.batch_annotate_files(requests=[request])
    
        for image_response in response.responses[0].responses:
            for page in image_response.full_text_annotation.pages:
                for block in page.blocks:
                    print(f"\nBlock confidence: {block.confidence}\n")
                    for par in block.paragraphs:
                        print(f"\tParagraph confidence: {par.confidence}")
                        for word in par.words:
                            symbol_texts = [symbol.text for symbol in word.symbols]
                            word_text = "".join(symbol_texts)
                            print(
                                "\t\tWord text: {} (confidence: {})".format(
                                    word_text, word.confidence
                                )
                            )
                            for symbol in word.symbols:
                                print(
                                    "\t\t\tSymbol: {} (confidence: {})".format(
                                        symbol.text, symbol.confidence
                                    )
                                )
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudvision). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
