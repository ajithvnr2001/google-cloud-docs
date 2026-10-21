---
url: https://docs.cloud.google.com/vision/docs/samples/vision-handwritten-ocr-beta/
title: Detect handwritten text in a local file (beta) \u00a0|\u00a0 Cloud Vision API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:27:18.708137+00:00
---

# Detect handwritten text in a local file (beta)  |  Cloud Vision API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/docs/samples/vision-handwritten-ocr-beta/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Vision API ](https://docs.cloud.google.com/vision/docs)
  * [ Samples ](https://docs.cloud.google.com/vision/docs/samples)



#  Detect handwritten text in a local file (beta) Stay organized with collections  Save and categorize content based on your preferences. 

Perform handwritten text detection on a local file (for beta launch).

## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Performs handwritten text detection on a local image file.
     *
     * @param filePath The path to the local file to detect handwritten text on.
     * @param out A {@link PrintStream} to write the results to.
     * @throws Exception on errors while closing the client.
     * @throws IOException on Input/Output errors.
     */
    public static void detectHandwrittenOcr(String filePath, PrintStream out) throws Exception {
      List<AnnotateImageRequest> requests = new ArrayList<>();
    
      ByteString imgBytes = ByteString.readFrom(new FileInputStream(filePath));
    
      Image img = Image.newBuilder().setContent(imgBytes).build();
      Feature feat = Feature.newBuilder().setType(Type.DOCUMENT_TEXT_DETECTION).build();
      // Set the Language Hint codes for handwritten OCR
      ImageContext imageContext =
          ImageContext.newBuilder().addLanguageHints("en-t-i0-handwrit").build();
    
      AnnotateImageRequest request =
          AnnotateImageRequest.newBuilder()
              .addFeatures(feat)
              .setImage(img)
              .setImageContext(imageContext)
              .build();
      requests.add(request);
    
      try (ImageAnnotatorClient client = ImageAnnotatorClient.create()) {
        BatchAnnotateImagesResponse response = client.batchAnnotateImages(requests);
        List<AnnotateImageResponse> responses = response.getResponsesList();
        client.close();
    
        for (AnnotateImageResponse res : responses) {
          if (res.hasError()) {
            out.printf("Error: %s\n", res.getError().getMessage());
            return;
          }
    
          // For full list of available annotations, see http://g.co/cloud/vision/docs
          TextAnnotation annotation = res.getFullTextAnnotation();
          for (Page page : annotation.getPagesList()) {
            String pageText = "";
            for (Block block : page.getBlocksList()) {
              String blockText = "";
              for (Paragraph para : block.getParagraphsList()) {
                String paraText = "";
                for (Word word : para.getWordsList()) {
                  String wordText = "";
                  for (Symbol symbol : word.getSymbolsList()) {
                    wordText = wordText + symbol.getText();
                    out.format(
                        "Symbol text: %s (confidence: %f)\n",
                        symbol.getText(), symbol.getConfidence());
                  }
                  out.format("Word text: %s (confidence: %f)\n\n", wordText, word.getConfidence());
                  paraText = String.format("%s %s", paraText, wordText);
                }
                // Output Example using Paragraph:
                out.println("\nParagraph: \n" + paraText);
                out.format("Paragraph Confidence: %f\n", para.getConfidence());
                blockText = blockText + paraText;
              }
              pageText = pageText + blockText;
            }
          }
          out.println("\nComplete annotation:");
          out.println(annotation.getText());
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Node.js API reference documentation](https://googleapis.dev/nodejs/vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client libraries
    const vision = require('[@google-cloud/vision](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)').v1p3beta1;
    const fs = require('fs');
    
    // Creates a client
    const client = new vision.[ImageAnnotatorClient](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)();
    
    /**
     * TODO(developer): Uncomment the following line before running the sample.
     */
    // const fileName = `/path/to/localImage.png`;
    
    const request = {
      image: {
        content: fs.readFileSync(fileName),
      },
      feature: {
        languageHints: ['en-t-i0-handwrit'],
      },
    };
    
    const [result] = await client.documentTextDetection(request);
    const fullTextAnnotation = result.fullTextAnnotation;
    console.log(`Full text: ${fullTextAnnotation.text}`);

### Python

Before trying this sample, follow the Python setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def detect_handwritten_ocr(path):
        """Detects handwritten characters in a local image.
    
        Args:
        path: The path to the local file.
        """
        from google.cloud import vision_v1p3beta1 as vision
    
        client = vision.ImageAnnotatorClient()
    
        with open(path, "rb") as image_file:
            content = image_file.read()
    
        image = vision.Image(content=content)
    
        # Language hint codes for handwritten OCR:
        # en-t-i0-handwrit, mul-Latn-t-i0-handwrit
        # Note: Use only one language hint code per request for handwritten OCR.
        image_context = vision.ImageContext(language_hints=["en-t-i0-handwrit"])
    
        response = client.document_text_detection(image=image, image_context=image_context)
    
        print(f"Full Text: {response.full_text_annotation.text}")
        for page in response.full_text_annotation.pages:
            for block in page.blocks:
                print(f"\nBlock confidence: {block.confidence}\n")
    
                for paragraph in block.paragraphs:
                    print("Paragraph confidence: {}".format(paragraph.confidence))
    
                    for word in paragraph.words:
                        word_text = "".join([symbol.text for symbol in word.symbols])
                        print(
                            "Word text: {} (confidence: {})".format(
                                word_text, word.confidence
                            )
                        )
    
                        for symbol in word.symbols:
                            print(
                                "\tSymbol: {} (confidence: {})".format(
                                    symbol.text, symbol.confidence
                                )
                            )
    
        if response.error.message:
            raise Exception(
                "{}\nFor more info on error messages, check: "
                "https://cloud.google.com/apis/design/errors".format(response.error.message)
            )
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudvision). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
