---
url: https://docs.cloud.google.com/natural-language/docs/samples/language-quickstart/
title: Detect sentiment \u00a0|\u00a0 Cloud Natural Language API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:59:54.931074+00:00
---

# Detect sentiment  |  Cloud Natural Language API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/natural-language/docs/samples/language-quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Natural Language API ](https://docs.cloud.google.com/natural-language/docs)
  * [ Samples ](https://docs.cloud.google.com/natural-language/docs/samples)



#  Detect sentiment Stay organized with collections  Save and categorize content based on your preferences. 

Detect the sentiment of some sample text.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Natural Language client libraries](https://docs.cloud.google.com/natural-language/docs/reference/libraries)
  * [Quickstart: Perform sentiment analysis by using client libraries](https://docs.cloud.google.com/natural-language/docs/sentiment-analysis-client-libraries)



## Code sample

### Go

To learn how to install and use the client library for Natural Language, see [Natural Language client libraries](https://docs.cloud.google.com/natural-language/docs/reference/libraries). For more information, see the [Natural Language Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1). 

To authenticate to Natural Language, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Sample language-quickstart uses the Google Cloud Natural API to analyze the
    // sentiment of "Hello, world!".
    package main
    
    import (
    	"context"
    	"fmt"
    	"log"
    
    	language "cloud.google.com/go/language/apiv1"
    	"cloud.google.com/go/language/apiv1/languagepb"
    )
    
    func main() {
    	ctx := context.Background()
    
    	// Creates a client.
    	client, err := language.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1.html#cloud_google_com_go_language_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		log.Fatalf("Failed to create client: %v", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1.html#cloud_google_com_go_language_apiv1_Client_Close)()
    
    	// Sets the text to analyze.
    	text := "Hello, world!"
    
    	// Detects the sentiment of the text.
    	sentiment, err := client.AnalyzeSentiment(ctx, &languagepb.AnalyzeSentimentRequest{
    		Document: &languagepb.Document{
    			Source: &languagepb.Document_Content{
    				Content: text,
    			},
    			Type: languagepb.[Document_PLAIN_TEXT](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1/languagepb.html#cloud_google_com_go_language_apiv1_languagepb_Document_TYPE_UNSPECIFIED_Document_PLAIN_TEXT_Document_HTML),
    		},
    		EncodingType: languagepb.[EncodingType_UTF8](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1/languagepb.html#cloud_google_com_go_language_apiv1_languagepb_EncodingType_NONE_EncodingType_UTF8_EncodingType_UTF16_EncodingType_UTF32),
    	})
    	if err != nil {
    		log.Fatalf("Failed to analyze text: %v", err)
    	}
    
    	fmt.Printf("Text: %v\n", text)
    	if sentiment.DocumentSentiment.Score >= 0 {
    		fmt.Println("Sentiment: positive")
    	} else {
    		fmt.Println("Sentiment: negative")
    	}
    }
    

### Java

To learn how to install and use the client library for Natural Language, see [Natural Language client libraries](https://docs.cloud.google.com/natural-language/docs/reference/libraries). For more information, see the [Natural Language Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/overview). 

To authenticate to Natural Language, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    import com.google.cloud.language.v1.[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1.Document.html);
    import com.google.cloud.language.v1.[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1.Document.html).Type;
    import com.google.cloud.language.v1.[LanguageServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1.LanguageServiceClient.html);
    import com.google.cloud.language.v1.[Sentiment](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1.Sentiment.html);
    
    public class QuickstartSample {
      public static void main(String... args) throws Exception {
        // Instantiates a client
        try ([LanguageServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1.LanguageServiceClient.html) language = [LanguageServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1.LanguageServiceClient.html).create()) {
    
          // The text to analyze
          String text = "Hello, world!";
          [Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1.Document.html) doc = [Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1.Document.html).newBuilder().setContent(text).setType(Type.PLAIN_TEXT).build();
    
          // Detects the sentiment of the text
          [Sentiment](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1.Sentiment.html) sentiment = language.analyzeSentiment(doc).getDocumentSentiment();
    
          System.out.printf("Text: %s%n", text);
          System.out.printf("Sentiment: %s, %s%n", sentiment.[getScore](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1.Sentiment.html#com_google_cloud_language_v1_Sentiment_getScore__)(), sentiment.[getMagnitude](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1.Sentiment.html#com_google_cloud_language_v1_Sentiment_getMagnitude__)());
        }
      }
    }

### Node.js

To learn how to install and use the client library for Natural Language, see [Natural Language client libraries](https://docs.cloud.google.com/natural-language/docs/reference/libraries). For more information, see the [Natural Language Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/language/latest). 

To authenticate to Natural Language, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    async function quickstart() {
      // Imports the Google Cloud client library
      const language = require('[@google-cloud/language](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/overview.html)');
    
      // Instantiates a client
      const client = new language.[LanguageServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/overview.html)();
    
      // The text to analyze
      const text = 'Hello, world!';
    
      const document = {
        content: text,
        type: 'PLAIN_TEXT',
      };
    
      // Detects the sentiment of the text
      const [result] = await client.analyzeSentiment({document: document});
      const sentiment = result.documentSentiment;
    
      console.log(`Text: ${text}`);
      console.log(`Sentiment score: ${sentiment.score}`);
      console.log(`Sentiment magnitude: ${sentiment.magnitude}`);
    }

### PHP

To learn how to install and use the client library for Natural Language, see [Natural Language client libraries](https://docs.cloud.google.com/natural-language/docs/reference/libraries). 

To authenticate to Natural Language, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Includes the autoloader for libraries installed with composer
    require __DIR__ . '/vendor/autoload.php';
    
    # Imports the Google Cloud client library
    use Google\Cloud\Language\V2\AnalyzeSentimentRequest;
    use Google\Cloud\Language\V2\Client\LanguageServiceClient;
    use Google\Cloud\Language\V2\Document;
    
    # Your Google Cloud Platform project ID
    $projectId = 'YOUR_PROJECT_ID';
    
    # Instantiates a client
    $language = new LanguageServiceClient([
        'projectId' => $projectId
    ]);
    
    # The text to analyze
    $text = 'Hello, world!';
    $document = (new Document())
        ->setContent($text)
        ->setType(Document\Type::PLAIN_TEXT);
    $analyzeSentimentRequest = (new AnalyzeSentimentRequest())
        ->setDocument($document);
    
    # Detects the sentiment of the text
    $response = $language->analyzeSentiment($analyzeSentimentRequest);
    foreach ($response->getSentences() as $sentence) {
        $sentiment = $sentence->getSentiment();
        echo 'Text: ' . $sentence->getText()->getContent() . PHP_EOL;
        printf('Sentiment: %s, %s' . PHP_EOL, $sentiment->getScore(), $sentiment->getMagnitude());
    }
    

### Python

To learn how to install and use the client library for Natural Language, see [Natural Language client libraries](https://docs.cloud.google.com/natural-language/docs/reference/libraries). For more information, see the [Natural Language Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/language/latest). 

To authenticate to Natural Language, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Imports the Google Cloud client library.
    from google.cloud import language_v1
    
    # Instantiates a client.
    client = language_v1.LanguageServiceClient()
    
    # The text to analyze.
    text = "Hello, world!"
    document = language_v1.types.Document(
        content=text, type_=language_v1.types.Document.Type.PLAIN_TEXT
    )
    
    # Detects the sentiment of the text.
    sentiment = client.[analyze_sentiment](https://docs.cloud.google.com/python/docs/reference/language/latest/google.cloud.language_v1.services.language_service.LanguageServiceClient.html#google_cloud_language_v1_services_language_service_LanguageServiceClient_analyze_sentiment)(
        request={"document": document}
    ).document_sentiment
    
    print(f"Text: {text}")
    print(f"Sentiment: {sentiment.score}, {sentiment.magnitude}")

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudnaturallanguageapi). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
