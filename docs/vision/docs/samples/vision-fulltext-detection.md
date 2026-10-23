---
url: https://docs.cloud.google.com/vision/docs/samples/vision-fulltext-detection/
title: Detect text in a local file \u00a0|\u00a0 Cloud Vision API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:20.370682+00:00
---

# Detect text in a local file  |  Cloud Vision API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/docs/samples/vision-fulltext-detection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Vision API ](https://docs.cloud.google.com/vision/docs)
  * [ Samples ](https://docs.cloud.google.com/vision/docs/samples)



#  Detect text in a local file Stay organized with collections  Save and categorize content based on your preferences. 

Perform text detection on a local file.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Detect handwriting in images](https://docs.cloud.google.com/vision/docs/handwriting)



## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Go API reference documentation](https://godoc.org/cloud.google.com/go/vision/apiv1). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // detectDocumentText gets the full document text from the Vision API for an image at the given file path.
    func detectDocumentText(w io.Writer, file string) error {
    	ctx := context.Background()
    
    	client, err := vision.NewImageAnnotatorClient(ctx)
    	if err != nil {
    		return err
    	}
    
    	f, err := os.Open(file)
    	if err != nil {
    		return err
    	}
    	defer f.Close()
    
    	image, err := vision.NewImageFromReader(f)
    	if err != nil {
    		return err
    	}
    	annotation, err := client.DetectDocumentText(ctx, image, nil)
    	if err != nil {
    		return err
    	}
    
    	if annotation == nil {
    		fmt.Fprintln(w, "No text found.")
    	} else {
    		fmt.Fprintln(w, "Document Text:")
    		fmt.Fprintf(w, "%q\n", annotation.Text)
    
    		fmt.Fprintln(w, "Pages:")
    		for _, page := range annotation.Pages {
    			fmt.Fprintf(w, "\tConfidence: %f, Width: %d, Height: %d\n", page.Confidence, page.Width, page.Height)
    			fmt.Fprintln(w, "\tBlocks:")
    			for _, block := range page.Blocks {
    				fmt.Fprintf(w, "\t\tConfidence: %f, Block type: %v\n", block.Confidence, block.BlockType)
    				fmt.Fprintln(w, "\t\tParagraphs:")
    				for _, paragraph := range block.Paragraphs {
    					fmt.Fprintf(w, "\t\t\tConfidence: %f", paragraph.Confidence)
    					fmt.Fprintln(w, "\t\t\tWords:")
    					for _, word := range paragraph.Words {
    						symbols := make([]string, len(word.Symbols))
    						for i, s := range word.Symbols {
    							symbols[i] = s.Text
    						}
    						wordText := strings.Join(symbols, "")
    						fmt.Fprintf(w, "\t\t\t\tConfidence: %f, Symbols: %s\n", word.Confidence, wordText)
    					}
    				}
    			}
    		}
    	}
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    public static void detectDocumentText(String filePath) throws IOException {
      List<AnnotateImageRequest> requests = new ArrayList<>();
    
      ByteString imgBytes = ByteString.readFrom(new FileInputStream(filePath));
    
      Image img = Image.newBuilder().setContent(imgBytes).build();
      Feature feat = Feature.newBuilder().setType(Type.DOCUMENT_TEXT_DETECTION).build();
      AnnotateImageRequest request =
          AnnotateImageRequest.newBuilder().addFeatures(feat).setImage(img).build();
      requests.add(request);
    
      // Initialize client that will be used to send requests. This client only needs to be created
      // once, and can be reused for multiple requests. After completing all of your requests, call
      // the "close" method on the client to safely clean up any remaining background resources.
      try (ImageAnnotatorClient client = ImageAnnotatorClient.create()) {
        BatchAnnotateImagesResponse response = client.batchAnnotateImages(requests);
        List<AnnotateImageResponse> responses = response.getResponsesList();
        client.close();
    
        for (AnnotateImageResponse res : responses) {
          if (res.hasError()) {
            System.out.format("Error: %s%n", res.getError().getMessage());
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
                    System.out.format(
                        "Symbol text: %s (confidence: %f)%n",
                        symbol.getText(), symbol.getConfidence());
                  }
                  System.out.format(
                      "Word text: %s (confidence: %f)%n%n", wordText, word.getConfidence());
                  paraText = String.format("%s %s", paraText, wordText);
                }
                // Output Example using Paragraph:
                System.out.println("%nParagraph: %n" + paraText);
                System.out.format("Paragraph Confidence: %f%n", para.getConfidence());
                blockText = blockText + paraText;
              }
              pageText = pageText + blockText;
            }
          }
          System.out.println("%nComplete annotation:");
          System.out.println(annotation.getText());
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Node.js API reference documentation](https://googleapis.dev/nodejs/vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const vision = require('[@google-cloud/vision](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)');
    
    // Creates a client
    const client = new vision.[ImageAnnotatorClient](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)();
    
    /**
     * TODO(developer): Uncomment the following line before running the sample.
     */
    // const fileName = 'Local image file, e.g. /path/to/image.png';
    
    // Read a local image as a text document
    const [result] = await client.documentTextDetection(fileName);
    const fullTextAnnotation = result.fullTextAnnotation;
    console.log(`Full text: ${fullTextAnnotation.text}`);
    fullTextAnnotation.pages.forEach(page => {
      page.blocks.forEach(block => {
        console.log(`Block confidence: ${block.confidence}`);
        block.paragraphs.forEach(paragraph => {
          console.log(`Paragraph confidence: ${paragraph.confidence}`);
          paragraph.words.forEach(word => {
            const wordText = word.symbols.map(s => s.text).join('');
            console.log(`Word text: ${wordText}`);
            console.log(`Word confidence: ${word.confidence}`);
            word.symbols.forEach(symbol => {
              console.log(`Symbol text: ${symbol.text}`);
              console.log(`Symbol confidence: ${symbol.confidence}`);
            });
          });
        });
      });
    });

### PHP

Before trying this sample, follow the PHP setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision PHP API reference documentation](https://docs.cloud.google.com/php/docs/reference/cloud-vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace Google\Cloud\Samples\Vision;
    
    use Google\Cloud\Vision\V1\Client\ImageAnnotatorClient;
    
    /**
     * @param string $path Path to the image, e.g. "path/to/your/image.jpg"
     */
    function detect_document_text(string $path)
    {
        $imageAnnotator = new ImageAnnotatorClient();
    
        # annotate the image
        $image = file_get_contents($path);
        $response = $imageAnnotator->documentTextDetection($image);
        $annotation = $response->getFullTextAnnotation();
    
        # print out detailed and structured information about document text
        if ($annotation) {
            foreach ($annotation->getPages() as $page) {
                foreach ($page->getBlocks() as $block) {
                    $block_text = '';
                    foreach ($block->getParagraphs() as $paragraph) {
                        foreach ($paragraph->getWords() as $word) {
                            foreach ($word->getSymbols() as $symbol) {
                                $block_text .= $symbol->getText();
                            }
                            $block_text .= ' ';
                        }
                        $block_text .= "\n";
                    }
                    printf('Block content: %s', $block_text);
                    printf('Block confidence: %f' . PHP_EOL,
                        $block->getConfidence());
    
                    # get bounds
                    $vertices = $block->getBoundingBox()->getVertices();
                    $bounds = [];
                    foreach ($vertices as $vertex) {
                        $bounds[] = sprintf('(%d,%d)', $vertex->getX(),
                            $vertex->getY());
                    }
                    print('Bounds: ' . join(', ', $bounds) . PHP_EOL);
                    print(PHP_EOL);
                }
            }
        } else {
            print('No text found' . PHP_EOL);
        }
    
        $imageAnnotator->close();
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def detect_document(path):
        """Detects document features in an image."""
        from google.cloud import vision
    
        client = vision.[ImageAnnotatorClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.image_annotator.ImageAnnotatorClient.html)()
    
        with open(path, "rb") as image_file:
            content = image_file.read()
    
        image = vision.[Image](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.Image.html)(content=content)
    
        response = client.document_text_detection(image=image)
    
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
