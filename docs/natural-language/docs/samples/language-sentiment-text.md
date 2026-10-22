---
url: https://docs.cloud.google.com/natural-language/docs/samples/language-sentiment-text/
title: Analyze sentiment in a string \u00a0|\u00a0 Cloud Natural Language API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:17:37.480819+00:00
---

# Analyze sentiment in a string  |  Cloud Natural Language API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/natural-language/docs/samples/language-sentiment-text/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Natural Language API ](https://docs.cloud.google.com/natural-language/docs)
  * [ Samples ](https://docs.cloud.google.com/natural-language/docs/samples)



#  Analyze sentiment in a string Stay organized with collections  Save and categorize content based on your preferences. 

Inspect the given text and identify the prevailing emotional opinion.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Analyzing Sentiment](https://docs.cloud.google.com/natural-language/docs/analyzing-sentiment)



## Code sample

### Go

To learn how to install and use the client library for Natural Language, see [Natural Language client libraries](https://docs.cloud.google.com/natural-language/docs/reference/libraries). For more information, see the [Natural Language Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1). 

To authenticate to Natural Language, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    func analyzeSentiment(ctx context.Context, client *language.Client, text string) (*languagepb.AnalyzeSentimentResponse, error) {
    	return client.AnalyzeSentiment(ctx, &languagepb.AnalyzeSentimentRequest{
    		Document: &languagepb.Document{
    			Source: &languagepb.Document_Content{
    				Content: text,
    			},
    			Type: languagepb.Document_PLAIN_TEXT,
    		},
    	})
    }
    

### Java

To learn how to install and use the client library for Natural Language, see [Natural Language client libraries](https://docs.cloud.google.com/natural-language/docs/reference/libraries). For more information, see the [Natural Language Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/overview). 

To authenticate to Natural Language, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Instantiate the Language client com.google.cloud.language.v2.LanguageServiceClient
    try (LanguageServiceClient language = LanguageServiceClient.create()) {
      Document doc = Document.newBuilder().setContent(text).setType(Type.PLAIN_TEXT).build();
      AnalyzeSentimentResponse response = language.analyzeSentiment(doc);
      Sentiment sentiment = response.getDocumentSentiment();
      if (sentiment == null) {
        System.out.println("No sentiment found");
      } else {
        System.out.printf("Sentiment magnitude: %.3f\n", sentiment.getMagnitude());
        System.out.printf("Sentiment score: %.3f\n", sentiment.getScore());
      }
      return sentiment;
    }

### Node.js

To learn how to install and use the client library for Natural Language, see [Natural Language client libraries](https://docs.cloud.google.com/natural-language/docs/reference/libraries). For more information, see the [Natural Language Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/language/latest). 

To authenticate to Natural Language, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const language = require('[@google-cloud/language](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/overview.html)');
    
    // Creates a client
    const client = new language.[LanguageServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/overview.html)();
    
    /**
     * TODO(developer): Uncomment the following line to run this code.
     */
    // const text = 'Your text to analyze, e.g. Hello, world!';
    
    // Prepares a document, representing the provided text
    const document = {
      content: text,
      type: 'PLAIN_TEXT',
    };
    
    // Detects the sentiment of the document
    const [result] = await client.analyzeSentiment({document});
    
    const sentiment = result.documentSentiment;
    console.log('Document sentiment:');
    console.log(`  Score: ${sentiment.score}`);
    console.log(`  Magnitude: ${sentiment.magnitude}`);
    
    const sentences = result.sentences;
    sentences.forEach(sentence => {
      console.log(`Sentence: ${sentence.text.content}`);
      console.log(`  Score: ${sentence.sentiment.score}`);
      console.log(`  Magnitude: ${sentence.sentiment.magnitude}`);
    });
    

### PHP

To learn how to install and use the client library for Natural Language, see [Natural Language client libraries](https://docs.cloud.google.com/natural-language/docs/reference/libraries). 

To authenticate to Natural Language, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Language\V1\AnalyzeSentimentRequest;
    use Google\Cloud\Language\V1\Client\LanguageServiceClient;
    use Google\Cloud\Language\V1\Document;
    use Google\Cloud\Language\V1\Document\Type;
    
    /**
     * @param string $text The text to analyze
     */
    function analyze_sentiment(string $text): void
    {
        $languageServiceClient = new LanguageServiceClient();
    
        // Create a new Document, add text as content and set type to PLAIN_TEXT
        $document = (new Document())
            ->setContent($text)
            ->setType(Type::PLAIN_TEXT);
    
        // Call the analyzeSentiment function
        $request = (new AnalyzeSentimentRequest())
            ->setDocument($document);
        $response = $languageServiceClient->analyzeSentiment($request);
        $document_sentiment = $response->getDocumentSentiment();
        // Print document information
        printf('Document Sentiment:' . PHP_EOL);
        printf('  Magnitude: %s' . PHP_EOL, $document_sentiment->getMagnitude());
        printf('  Score: %s' . PHP_EOL, $document_sentiment->getScore());
        printf(PHP_EOL);
        $sentences = $response->getSentences();
        foreach ($sentences as $sentence) {
            printf('Sentence: %s' . PHP_EOL, $sentence->getText()->getContent());
            printf('Sentence Sentiment:' . PHP_EOL);
            $sentiment = $sentence->getSentiment();
            if ($sentiment) {
                printf('Entity Magnitude: %s' . PHP_EOL, $sentiment->getMagnitude());
                printf('Entity Score: %s' . PHP_EOL, $sentiment->getScore());
            }
            print(PHP_EOL);
        }
    }

### Python

To learn how to install and use the client library for Natural Language, see [Natural Language client libraries](https://docs.cloud.google.com/natural-language/docs/reference/libraries). For more information, see the [Natural Language Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/language/latest). 

To authenticate to Natural Language, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import language_v2
    
    
    def sample_analyze_sentiment(text_content: str = "I am so happy and joyful.") -> None:
        """
        Analyzes Sentiment in a string.
    
        Args:
          text_content: The text content to analyze.
        """
    
        client = language_v2.LanguageServiceClient()
    
        # text_content = 'I am so happy and joyful.'
    
        # Available types: PLAIN_TEXT, HTML
        document_type_in_plain_text = language_v2.Document.Type.PLAIN_TEXT
    
        # Optional. If not specified, the language is automatically detected.
        # For list of supported languages:
        # https://cloud.google.com/natural-language/docs/languages
        language_code = "en"
        document = {
            "content": text_content,
            "type_": document_type_in_plain_text,
            "language_code": language_code,
        }
    
        # Available values: NONE, UTF8, UTF16, UTF32
        # See https://cloud.google.com/natural-language/docs/reference/rest/v2/EncodingType.
        encoding_type = language_v2.EncodingType.UTF8
    
        response = client.[analyze_sentiment](https://docs.cloud.google.com/python/docs/reference/language/latest/google.cloud.language_v1.services.language_service.LanguageServiceClient.html#google_cloud_language_v1_services_language_service_LanguageServiceClient_analyze_sentiment)(
            request={"document": document, "encoding_type": encoding_type}
        )
        # Get overall sentiment of the input document
        print(f"Document sentiment score: {response.document_sentiment.score}")
        print(f"Document sentiment magnitude: {response.document_sentiment.magnitude}")
        # Get sentiment for all sentences in the document
        for sentence in response.sentences:
            print(f"Sentence text: {sentence.text.content}")
            print(f"Sentence sentiment score: {sentence.sentiment.score}")
            print(f"Sentence sentiment magnitude: {sentence.sentiment.magnitude}")
    
        # Get the language of the text, which will be the same as
        # the language specified in the request or, if not specified,
        # the automatically-detected language.
        print(f"Language of the text: {response.language_code}")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudnaturallanguageapi). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
