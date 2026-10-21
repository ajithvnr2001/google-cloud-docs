---
url: https://docs.cloud.google.com/vision/docs/handwriting/
title: Detect handwriting in images \u00a0|\u00a0 Cloud Vision API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:06:34.322225+00:00
---

# Detect handwriting in images  |  Cloud Vision API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/docs/handwriting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Vision API ](https://docs.cloud.google.com/vision/docs)
  * [ Guides ](https://docs.cloud.google.com/vision/docs/features-list)



Send feedback 

#  Detect handwriting in images Stay organized with collections  Save and categorize content based on your preferences. 

**Note:**

  * Using this API in a mobile device app? Try [Firebase Machine Learning](https://firebase.google.com/docs/ml) and [ML Kit](https://developers.google.com/ml-kit), which provide platform-specific Android and iOS SDKs for using Cloud Vision services, as well as on-device ML Vision APIs and on-device inference using custom ML models. 
  * The Vision API now supports offline **asynchronous batch image annotation** for all features. This asynchronous request supports up to 2000 image files and returns response JSON files that are stored in your Cloud Storage bucket. For more information about this feature, refer to [Offline batch image annotation](https://docs.cloud.google.com/vision/docs/batch). 

Pricing for document text detection is at the `DOCUMENT_TEXT_DETECTION` rate. Please see the [Pricing](https://cloud.google.com/vision/pricing) page for details.

## Handwriting detection with Optical Character Recognition (OCR)

The Vision API can detect and extract text from images:

  * `DOCUMENT_TEXT_DETECTION` extracts text from an image (or [file](https://docs.cloud.google.com/vision/docs/pdf)); the response is **optimized for dense text and documents**. The JSON includes page, block, paragraph, word, and break information.

![Screenshot simulating how an OCR system might identify and extract text, highlighting headings, paragraphs, and icons.](https://docs.cloud.google.com/static/vision/docs/images/document_text_highlighted.png)

One specific use of [DOCUMENT_TEXT_DETECTION](https://docs.cloud.google.com/vision/docs/ocr) is to detect handwriting in an image.

![Lined paper with Google Cloud Platform written in cursive.](https://docs.cloud.google.com/static/vision/docs/images/detect_handwriting_OCR-detect-handwriting_SMALL.png)




##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how Cloud Vision API performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try Cloud Vision API free ](https://console.cloud.google.com/freetrial)

## Document text detection requests

### Set up your Google Cloud project and authentication

If you have not created a Google Cloud project, do so now. Expand this section for instructions. 

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Vision API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=vision.googleapis.com)

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

  10. Enable the Vision API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=vision.googleapis.com)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init




### Detect document text in a local image

You can use the Vision API to perform feature detection on a local image file.

For REST requests, send the contents of the image file as a [base64 encoded](https://docs.cloud.google.com/vision/docs/base64) string in the body of your request.

For `gcloud` and client library requests, specify the path to a local image in your request. 

### REST

Before using any of the request data, make the following replacements: 

  * BASE64_ENCODED_IMAGE: The base64 representation (ASCII string) of your binary image data. This string should look similar to the following string: 
    * `/9j/4QAYRXhpZgAA...9tAVx/zDQDlGxn//2Q==`
Visit the [base64 encode](https://docs.cloud.google.com/vision/docs/base64) topic for more information.
  * PROJECT_ID: Your Google Cloud project ID.



HTTP method and URL: 
    
    
    POST https://vision.googleapis.com/v1/images:annotate

Request JSON body: 
    
    
    {
      "requests": [
        {
          "image": {
            "content": "BASE64_ENCODED_IMAGE"
          },
          "features": [
            {
              "type": "DOCUMENT_TEXT_DETECTION"
            }
          ]
        }
      ]
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://vision.googleapis.com/v1/images:annotate"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://vision.googleapis.com/v1/images:annotate" | Select-Object -Expand Content

If the request is successful, the server returns a `200 OK` HTTP status code and the response in JSON format.

**Note: Zero coordinate values omitted.** When the API detects a coordinate ("x" or "y") value of 0, **_that coordinate is omitted in the JSON response_**. Thus, a response with a bounding poly around the entire image would be   
**[{},{"x": 100},{"x": 100,"y": 100},{"y": 100}] for an image that is 100 pixels by 100 pixels**. For more information, see the [API Reference documentation](https://cloud.google.com/vision/docs/reference/rest/v1/images/annotate#boundingpoly). 

#### Response
    
    
    {
      "responses": [
        {
          "textAnnotations": [
            {
              "locale": "en",
              "description": "O Google Cloud Platform\n",
              "boundingPoly": {
                "vertices": [
                  {
                    "x": 14,
                    "y": 11
                  },
                  {
                    "x": 279,
                    "y": 11
                  },
                  {
                    "x": 279,
                    "y": 37
                  },
                  {
                    "x": 14,
                    "y": 37
                  }
                ]
              }
            },
          ],
          "fullTextAnnotation": {
            "pages": [
              {
                "property": {
                  "detectedLanguages": [
                    {
                      "languageCode": "en"
                    }
                  ]
                },
                "width": 281,
                "height": 44,
                "blocks": [
                  {
                    "property": {
                      "detectedLanguages": [
                        {
                          "languageCode": "en"
                        }
                      ]
                    },
                    "boundingBox": {
                      "vertices": [
                        {
                          "x": 14, "y": 11
                        },
                        {
                          "x": 279, "y": 11
                        },
                        {
                          "x": 279, "y": 37
                        },
                        {
                          "x": 14, "y": 37
                        }
                      ]
                    },
                    "paragraphs": [
                      {
                        "property": {
                          "detectedLanguages": [
                            {
                              "languageCode": "en"
                            }
                          ]
                        },
                        "boundingBox": {
                          "vertices": [
                            {
                              "x": 14, "y": 11
                            },
                            {
                              "x": 279, "y": 11
                            },
                            {
                              "x": 279, "y": 37
                            },
                            {
                              "x": 14, "y": 37
                            }
                          ]
                        },
                        "words": [
                          {
                            "property": {
                              "detectedLanguages": [
                                {
                                  "languageCode": "en"
                                }
                              ]
                            },
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 14, "y": 11
                                },
                                {
                                  "x": 23, "y": 11
                                },
                                {
                                  "x": 23, "y": 37
                                },
                                {
                                  "x": 14, "y": 37
                                }
                              ]
                            },
                            "symbols": [
                              {
                                "property": {
                                  "detectedLanguages": [
                                    {
                                      "languageCode": "en"
                                    }
                                  ],
                                  "detectedBreak": {
                                    "type": "SPACE"
                                  }
                                },
                                "boundingBox": {
                                  "vertices": [
                                    {
                                      "x": 14, "y": 11
                                    },
                                    {
                                      "x": 23, "y": 11
                                    },
                                    {
                                      "x": 23, "y": 37
                                    },
                                    {
                                      "x": 14, "y": 37
                                    }
                                  ]
                                },
                                "text": "O"
                              }
                            ]
                          },
                        ]
                      }
                    ],
                    "blockType": "TEXT"
                  }
                ]
              }
            ],
            "text": "Google Cloud Platform\n"
          }
        }
      ]
    }
    

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

Before trying this sample, follow the Java setup instructions in the [Vision API Quickstart Using Client Libraries](https://docs.cloud.google.com/vision/docs/detect-labels-image-client-libraries). For more information, see the [ Vision API Java reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview).

**Note:** For Java **Spring framework** users, [Spring Cloud Google Cloud](https://docs.cloud.google.com/vision/docs/adding-spring) offers a way to automatically configure authentication settings and client objects to use Vision API. 
    
    
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
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/vision/docs/libraries) on the client libraries page and then visit the [Vision reference documentation for .NET.](https://googleapis.dev/dotnet/Google.Apis.Vision.v1/latest/api/Google.Apis.Vision.v1.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/vision/docs/libraries) on the client libraries page and then visit the [Vision reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-vision/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/vision/docs/libraries) on the client libraries page and then visit the [Vision reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-vision/latest/Google/Cloud/Vision.html)

### Detect document text in a remote image

You can use the Vision API to perform feature detection on a remote image file that is located in Cloud Storage or on the Web. To send a remote file request, specify the file's Web URL or Cloud Storage URI in the request body. 

**Caution:** When fetching images from HTTP/HTTPS URLs, Google cannot guarantee that the request will be completed. Your request might fail if the specified host denies the request (for example, due to request throttling or [DoS](https://en.wikipedia.org/wiki/Denial-of-service_attack) prevention), or if Google throttles requests to the site for abuse prevention. **As a best practice, don't depend on externally-hosted images for production applications**. 

### REST

Before using any of the request data, make the following replacements: 

  * CLOUD_STORAGE_IMAGE_URI: the path to a valid image file in a Cloud Storage bucket. You must at least have read privileges to the file. Example: 
    * gs://cloud-samples-data/vision/handwriting_image.png

  * PROJECT_ID: Your Google Cloud project ID.



HTTP method and URL: 
    
    
    POST https://vision.googleapis.com/v1/images:annotate

Request JSON body: 
    
    
    {
      "requests": [
        {
          "image": {
            "source": {
              "imageUri": "CLOUD_STORAGE_IMAGE_URI"
            }
           },
           "features": [
             {
               "type": "DOCUMENT_TEXT_DETECTION"
             }
           ]
        }
      ]
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://vision.googleapis.com/v1/images:annotate"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://vision.googleapis.com/v1/images:annotate" | Select-Object -Expand Content

If the request is successful, the server returns a `200 OK` HTTP status code and the response in JSON format.

**Note: Zero coordinate values omitted.** When the API detects a coordinate ("x" or "y") value of 0, **_that coordinate is omitted in the JSON response_**. Thus, a response with a bounding poly around the entire image would be   
**[{},{"x": 100},{"x": 100,"y": 100},{"y": 100}] for an image that is 100 pixels by 100 pixels**. For more information, see the [API Reference documentation](https://cloud.google.com/vision/docs/reference/rest/v1/images/annotate#boundingpoly). 

#### Response
    
    
    {
      "responses": [
        {
          "textAnnotations": [
            {
              "locale": "en",
              "description": "O Google Cloud Platform\n",
              "boundingPoly": {
                "vertices": [
                  {
                    "x": 14,
                    "y": 11
                  },
                  {
                    "x": 279,
                    "y": 11
                  },
                  {
                    "x": 279,
                    "y": 37
                  },
                  {
                    "x": 14,
                    "y": 37
                  }
                ]
              }
            },
          ],
          "fullTextAnnotation": {
            "pages": [
              {
                "property": {
                  "detectedLanguages": [
                    {
                      "languageCode": "en"
                    }
                  ]
                },
                "width": 281,
                "height": 44,
                "blocks": [
                  {
                    "property": {
                      "detectedLanguages": [
                        {
                          "languageCode": "en"
                        }
                      ]
                    },
                    "boundingBox": {
                      "vertices": [
                        {
                          "x": 14, "y": 11
                        },
                        {
                          "x": 279, "y": 11
                        },
                        {
                          "x": 279, "y": 37
                        },
                        {
                          "x": 14, "y": 37
                        }
                      ]
                    },
                    "paragraphs": [
                      {
                        "property": {
                          "detectedLanguages": [
                            {
                              "languageCode": "en"
                            }
                          ]
                        },
                        "boundingBox": {
                          "vertices": [
                            {
                              "x": 14, "y": 11
                            },
                            {
                              "x": 279, "y": 11
                            },
                            {
                              "x": 279, "y": 37
                            },
                            {
                              "x": 14, "y": 37
                            }
                          ]
                        },
                        "words": [
                          {
                            "property": {
                              "detectedLanguages": [
                                {
                                  "languageCode": "en"
                                }
                              ]
                            },
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 14, "y": 11
                                },
                                {
                                  "x": 23, "y": 11
                                },
                                {
                                  "x": 23, "y": 37
                                },
                                {
                                  "x": 14, "y": 37
                                }
                              ]
                            },
                            "symbols": [
                              {
                                "property": {
                                  "detectedLanguages": [
                                    {
                                      "languageCode": "en"
                                    }
                                  ],
                                  "detectedBreak": {
                                    "type": "SPACE"
                                  }
                                },
                                "boundingBox": {
                                  "vertices": [
                                    {
                                      "x": 14, "y": 11
                                    },
                                    {
                                      "x": 23, "y": 11
                                    },
                                    {
                                      "x": 23, "y": 37
                                    },
                                    {
                                      "x": 14, "y": 37
                                    }
                                  ]
                                },
                                "text": "O"
                              }
                            ]
                          },
                        ]
                      }
                    ],
                    "blockType": "TEXT"
                  }
                ]
              }
            ],
            "text": "Google Cloud Platform\n"
          }
        }
      ]
    }
    

### Go

Before trying this sample, follow the Go setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Go API reference documentation](https://godoc.org/cloud.google.com/go/vision/apiv1). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // detectDocumentText gets the full document text from the Vision API for an image at the given file path.
    func detectDocumentTextURI(w io.Writer, file string) error {
    	ctx := context.Background()
    
    	client, err := vision.NewImageAnnotatorClient(ctx)
    	if err != nil {
    		return err
    	}
    
    	image := vision.NewImageFromURI(file)
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

Before trying this sample, follow the Java setup instructions in the [Vision API Quickstart Using Client Libraries](https://docs.cloud.google.com/vision/docs/detect-labels-image-client-libraries). For more information, see the [ Vision API Java reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview).

**Note:** For Java **Spring framework** users, [Spring Cloud Google Cloud](https://docs.cloud.google.com/vision/docs/adding-spring) offers a way to automatically configure authentication settings and client objects to use Vision API. 
    
    
    public static void detectDocumentTextGcs(String gcsPath) throws IOException {
      List<AnnotateImageRequest> requests = new ArrayList<>();
    
      ImageSource imgSource = ImageSource.newBuilder().setGcsImageUri(gcsPath).build();
      Image img = Image.newBuilder().setSource(imgSource).build();
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
    
    
    // Imports the Google Cloud client libraries
    const vision = require('[@google-cloud/vision](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)');
    
    // Creates a client
    const client = new vision.[ImageAnnotatorClient](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)();
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // const bucketName = 'Bucket where the file resides, e.g. my-bucket';
    // const fileName = 'Path to file within bucket, e.g. path/to/image.png';
    
    // Read a remote image as a text document
    const [result] = await client.documentTextDetection(
      `gs://${bucketName}/${fileName}`
    );
    const fullTextAnnotation = result.fullTextAnnotation;
    console.log(fullTextAnnotation.text);

### Python

Before trying this sample, follow the Python setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def detect_document_uri(uri):
        """Detects document features in the file located in Google Cloud
        Storage."""
        from google.cloud import vision
    
        client = vision.[ImageAnnotatorClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.image_annotator.ImageAnnotatorClient.html)()
        image = vision.[Image](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.Image.html)()
        image.source.image_uri = uri
    
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
    
    

### gcloud

To perform handwriting detection, use the [`gcloud ml vision detect-document`](https://docs.cloud.google.com/sdk/gcloud/reference/ml/vision/detect-document) command as shown in the following example:
    
    
    gcloud ml vision detect-document gs://cloud-samples-data/vision/handwriting_image.png
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/vision/docs/libraries) on the client libraries page and then visit the [Vision reference documentation for .NET.](https://googleapis.dev/dotnet/Google.Apis.Vision.v1/latest/api/Google.Apis.Vision.v1.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/vision/docs/libraries) on the client libraries page and then visit the [Vision reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-vision/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/vision/docs/libraries) on the client libraries page and then visit the [Vision reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-vision/latest/Google/Cloud/Vision.html)

### Specify the language (optional)

Both types of OCR requests support one or more `languageHints` that specify the language of any text in the image. However, an empty value usually yields the best results, because omitting a value enables automatic language detection. For languages based on the Latin alphabet, setting `languageHints` is not needed. In rare cases, when the language of the text in the image is known, setting a hint helps get better results (although it can be a significant hindrance if the hint is wrong). Text detection returns an error if one or more of the specified languages is not one of the [supported languages](https://cloud.google.com/vision/docs/languages). 

If you choose to provide a language hint, modify the body of your request (`request.json` file) to provide the string of one of the supported languages in the `imageContext.languageHints` field as shown in the following sample: 
    
    
    {
      "requests": [
        {
          "image": {
            "source": {
              "imageUri": "IMAGE_URL"
            }
          },
          "features": [
            {
              "type": "DOCUMENT_TEXT_DETECTION"
            }
          ],**      "imageContext"**: {**        "languageHints"**: **[ "en-t-i0-handwrit"]**
          }
        }
      ]
    }

**How do language hints work?**

The `languageHint` format follows the [BCP47](https://tools.ietf.org/html/bcp47) language code formatting guidelines. The BCP47 specified format is as follows: 

`language` ["-" `script`] ["-" `region`] *("-" `variant`) *("-" `extension`) ["-" `privateuse`].

For example, the language hint "`en`-`t`-`i0`-`handwrit`" specifies English language (`en`), [transform](https://tools.ietf.org/html/rfc6497) extension singleton (`t`), [input method engine transform](http://www.unicode.org/reports/tr35/) extension code (`i0`), and [handwriting transform code](http://unicode.org/repos/cldr/tags/latest/common/bcp47/transform_ime.xml) (`handwrit`). This code says that the language is "English transformed from handwriting." You don't need to specify a script code because `Latn` is implied by the "`en`" language. 

## Multi-regional support

This functionality currently only applies to the OCR feature (types `TEXT_DETECTION` or `DOCUMENT_TEXT_DETECTION`). 

You can now specify continent-level data storage and OCR processing. The following regions are currently supported: 

  * `us`: USA country only
  * `eu`: The European Union



### Locations

Cloud Vision offers you some control over where the resources for your project are stored and processed. In particular, you can configure Cloud Vision to store and process your data only in the European Union. 

By default Cloud Vision stores and processes resources in a **Global** location, which means that Cloud Vision doesn't guarantee that your resources will remain within a particular location or region. If you choose the **European Union** location, Google will store your data and process it only in the European Union. You and your users can access the data from any location. 

### Setting the location using the API

The Vision API supports a global API endpoint (`vision.googleapis.com`) and also two region-based endpoints: a European Union endpoint (`eu-vision.googleapis.com`) and United States endpoint (`us-vision.googleapis.com`). Use these endpoints for region-specific processing. For example, to store and process your data in the European Union only, use the URI `eu-vision.googleapis.com` in place of `vision.googleapis.com` for your REST API calls: 

  * https://**eu-** vision.googleapis.com/v1/projects/PROJECT_ID/locations/**eu** /images:annotate
  * https://**eu-** vision.googleapis.com/v1/projects/PROJECT_ID/locations/**eu** /images:asyncBatchAnnotate
  * https://**eu-** vision.googleapis.com/v1/projects/PROJECT_ID/locations/**eu** /files:annotate
  * https://**eu-** vision.googleapis.com/v1/projects/PROJECT_ID/locations/**eu** /files:asyncBatchAnnotate



To store and process your data in the United States only, use the US endpoint (`us-vision.googleapis.com`) with the preceding methods. 

### Setting the location using the client libraries

The Vision API client libraries accesses the global API endpoint (`vision.googleapis.com`) by default. To store and process your data in the European Union only, you need to explicitly set the endpoint (`eu-vision.googleapis.com`). The following code samples show how to configure this setting. 

### REST

Before using any of the request data, make the following replacements: 

  * REGION_ID: One of the valid regional location identifiers: 
    * `us`: USA country only
    * `eu`: The European Union
  * CLOUD_STORAGE_IMAGE_URI: the path to a valid image file in a Cloud Storage bucket. You must at least have read privileges to the file. Example: 
    * gs://cloud-samples-data/vision/handwriting_image.png

  * PROJECT_ID: Your Google Cloud project ID.



HTTP method and URL: 
    
    
    POST https://REGION_ID-vision.googleapis.com/v1/projects/PROJECT_ID/locations/REGION_ID/images:annotate

Request JSON body: 
    
    
    {
      "requests": [
        {
          "image": {
            "source": {
              "imageUri": "CLOUD_STORAGE_IMAGE_URI"
            }
           },
           "features": [
             {
               "type": "DOCUMENT_TEXT_DETECTION"
             }
           ]
        }
      ]
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://REGION_ID-vision.googleapis.com/v1/projects/PROJECT_ID/locations/REGION_ID/images:annotate"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://REGION_ID-vision.googleapis.com/v1/projects/PROJECT_ID/locations/REGION_ID/images:annotate" | Select-Object -Expand Content

If the request is successful, the server returns a `200 OK` HTTP status code and the response in JSON format.

**Note: Zero coordinate values omitted.** When the API detects a coordinate ("x" or "y") value of 0, **_that coordinate is omitted in the JSON response_**. Thus, a response with a bounding poly around the entire image would be   
**[{},{"x": 100},{"x": 100,"y": 100},{"y": 100}] for an image that is 100 pixels by 100 pixels**. For more information, see the [API Reference documentation](https://cloud.google.com/vision/docs/reference/rest/v1/images/annotate#boundingpoly). 

#### Response
    
    
    {
      "responses": [
        {
          "textAnnotations": [
            {
              "locale": "en",
              "description": "O Google Cloud Platform\n",
              "boundingPoly": {
                "vertices": [
                  {
                    "x": 14,
                    "y": 11
                  },
                  {
                    "x": 279,
                    "y": 11
                  },
                  {
                    "x": 279,
                    "y": 37
                  },
                  {
                    "x": 14,
                    "y": 37
                  }
                ]
              }
            },
          ],
          "fullTextAnnotation": {
            "pages": [
              {
                "property": {
                  "detectedLanguages": [
                    {
                      "languageCode": "en"
                    }
                  ]
                },
                "width": 281,
                "height": 44,
                "blocks": [
                  {
                    "property": {
                      "detectedLanguages": [
                        {
                          "languageCode": "en"
                        }
                      ]
                    },
                    "boundingBox": {
                      "vertices": [
                        {
                          "x": 14, "y": 11
                        },
                        {
                          "x": 279, "y": 11
                        },
                        {
                          "x": 279, "y": 37
                        },
                        {
                          "x": 14, "y": 37
                        }
                      ]
                    },
                    "paragraphs": [
                      {
                        "property": {
                          "detectedLanguages": [
                            {
                              "languageCode": "en"
                            }
                          ]
                        },
                        "boundingBox": {
                          "vertices": [
                            {
                              "x": 14, "y": 11
                            },
                            {
                              "x": 279, "y": 11
                            },
                            {
                              "x": 279, "y": 37
                            },
                            {
                              "x": 14, "y": 37
                            }
                          ]
                        },
                        "words": [
                          {
                            "property": {
                              "detectedLanguages": [
                                {
                                  "languageCode": "en"
                                }
                              ]
                            },
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 14, "y": 11
                                },
                                {
                                  "x": 23, "y": 11
                                },
                                {
                                  "x": 23, "y": 37
                                },
                                {
                                  "x": 14, "y": 37
                                }
                              ]
                            },
                            "symbols": [
                              {
                                "property": {
                                  "detectedLanguages": [
                                    {
                                      "languageCode": "en"
                                    }
                                  ],
                                  "detectedBreak": {
                                    "type": "SPACE"
                                  }
                                },
                                "boundingBox": {
                                  "vertices": [
                                    {
                                      "x": 14, "y": 11
                                    },
                                    {
                                      "x": 23, "y": 11
                                    },
                                    {
                                      "x": 23, "y": 37
                                    },
                                    {
                                      "x": 14, "y": 37
                                    }
                                  ]
                                },
                                "text": "O"
                              }
                            ]
                          },
                        ]
                      }
                    ],
                    "blockType": "TEXT"
                  }
                ]
              }
            ],
            "text": "Google Cloud Platform\n"
          }
        }
      ]
    }
    

### Go

Before trying this sample, follow the Go setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Go API reference documentation](https://godoc.org/cloud.google.com/go/vision/apiv1). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    
    	vision "cloud.google.com/go/vision/apiv1"
    	"google.golang.org/api/option"
    )
    
    // setEndpoint changes your endpoint.
    func setEndpoint(endpoint string) error {
    	// endpoint := "eu-vision.googleapis.com:443"
    
    	ctx := context.Background()
    	client, err := vision.[NewImageAnnotatorClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/latest/apiv1.html#cloud_google_com_go_vision_apiv1_ImageAnnotatorClient_NewImageAnnotatorClient)(ctx, option.WithEndpoint(endpoint))
    	if err != nil {
    		return fmt.Errorf("NewImageAnnotatorClient: %w", err)
    	}
    	defer client.Close()
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Vision API Quickstart Using Client Libraries](https://docs.cloud.google.com/vision/docs/detect-labels-image-client-libraries). For more information, see the [ Vision API Java reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview).

**Note:** For Java **Spring framework** users, [Spring Cloud Google Cloud](https://docs.cloud.google.com/vision/docs/adding-spring) offers a way to automatically configure authentication settings and client objects to use Vision API. 
    
    
    ImageAnnotatorSettings settings =
        ImageAnnotatorSettings.newBuilder().setEndpoint("eu-vision.googleapis.com:443").build();
    
    // Initialize client that will be used to send requests. This client only needs to be created
    // once, and can be reused for multiple requests. After completing all of your requests, call
    // the "close" method on the client to safely clean up any remaining background resources.
    ImageAnnotatorClient client = ImageAnnotatorClient.create(settings);

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Node.js API reference documentation](https://googleapis.dev/nodejs/vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const vision = require('[@google-cloud/vision](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)');
    
    async function setEndpoint() {
      // Specifies the location of the api endpoint
      const clientOptions = {apiEndpoint: 'eu-vision.googleapis.com'};
    
      // Creates a client
      const client = new vision.[ImageAnnotatorClient](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)(clientOptions);
    
      // Performs text detection on the image file
      const [result] = await client.textDetection('./resources/wakeupcat.jpg');
      const labels = result.textAnnotations;
      console.log('Text:');
      labels.forEach(label => console.log(label.description));
    }
    setEndpoint();

### Python

Before trying this sample, follow the Python setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import vision
    
    client_options = {"api_endpoint": "eu-vision.googleapis.com"}
    
    client = vision.[ImageAnnotatorClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.image_annotator.ImageAnnotatorClient.html)(client_options=client_options)

## Try the feature with the Google APIs Explorer

Try text detection and document text detection in the Google APIs Explorer. You can use the image specified already (`gs://cloud-samples-data/vision/handwriting_image.png`) by clicking **Execute** , or you can specify your own image in its place.

![Lined paper with Google Cloud Platform written in cursive.](https://docs.cloud.google.com/static/vision/docs/images/detect_handwriting_OCR-detect-handwriting_SMALL.png)

**Request body:**
    
    
    {
      "requests": [
        {
          "features": [
            {
              "type": "DOCUMENT_TEXT_DETECTION"
            }
          ],
          "image": {
            "source": {
              "imageUri": "gs://cloud-samples-data/vision/handwriting_image.png"
            }
          }
        }
      ]
    }

### Open the Google APIs Explorer and send the request

  1. To open the Google APIs Explorer, click **Try it!**.

Try it!

  2. Optional. Modify the existing request body.

  3. To send the request, click **Execute**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
