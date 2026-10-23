---
url: https://docs.cloud.google.com/natural-language/docs/samples/language-classify-text/
title: Classify text \u00a0|\u00a0 Cloud Natural Language API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:59:53.429711+00:00
---

# Classify text  |  Cloud Natural Language API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/natural-language/docs/samples/language-classify-text/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Natural Language API ](https://docs.cloud.google.com/natural-language/docs)
  * [ Samples ](https://docs.cloud.google.com/natural-language/docs/samples)



#  Classify text Stay organized with collections  Save and categorize content based on your preferences. 

Analyze text and return a list of content categories that apply to the text.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Classifying Content](https://docs.cloud.google.com/natural-language/docs/classifying-text)



## Code sample

### Go

To learn how to install and use the client library for Natural Language, see [Natural Language client libraries](https://docs.cloud.google.com/natural-language/docs/reference/libraries). For more information, see the [Natural Language Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1). 

To authenticate to Natural Language, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    func classifyText(ctx context.Context, client *language.Client, text string) (*languagepb.ClassifyTextResponse, error) {
    	return client.ClassifyText(ctx, &languagepb.ClassifyTextRequest{
    		Document: &languagepb.Document{
    			Source: &languagepb.Document_Content{
    				Content: text,
    			},
    			Type: languagepb.Document_PLAIN_TEXT,
    		},
    		ClassificationModelOptions: &languagepb.ClassificationModelOptions{
    			ModelType: &languagepb.ClassificationModelOptions_V2Model_{
    				V2Model: &languagepb.ClassificationModelOptions_V2Model{
    					ContentCategoriesVersion: languagepb.ClassificationModelOptions_V2Model_V2,
    				},
    			},
    		},
    	})
    }
    

### Java

To learn how to install and use the client library for Natural Language, see [Natural Language client libraries](https://docs.cloud.google.com/natural-language/docs/reference/libraries). For more information, see the [Natural Language Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/overview). 

To authenticate to Natural Language, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Instantiate the Language client com.google.cloud.language.v2.LanguageServiceClient
    try (LanguageServiceClient language = LanguageServiceClient.create()) {
      // Set content to the text string
      Document doc = Document.newBuilder().setContent(text).setType(Type.PLAIN_TEXT).build();
      ClassifyTextRequest request = ClassifyTextRequest.newBuilder().setDocument(doc).build();
      // Detect categories in the given text
      ClassifyTextResponse response = language.classifyText(request);
    
      for (ClassificationCategory category : response.getCategoriesList()) {
        System.out.printf(
            "Category name : %s, Confidence : %.3f\n",
            category.getName(), category.getConfidence());
      }
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
    
    const classificationModelOptions = {
      v2Model: {
        contentCategoriesVersion: 'V2',
      },
    };
    
    // Classifies text in the document
    const [classification] = await client.classifyText({
      document,
      classificationModelOptions,
    });
    console.log('Categories:');
    classification.categories.forEach(category => {
      console.log(`Name: ${category.name}, Confidence: ${category.confidence}`);
    });

### PHP

To learn how to install and use the client library for Natural Language, see [Natural Language client libraries](https://docs.cloud.google.com/natural-language/docs/reference/libraries). 

To authenticate to Natural Language, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Language\V1\ClassifyTextRequest;
    use Google\Cloud\Language\V1\Client\LanguageServiceClient;
    use Google\Cloud\Language\V1\Document;
    use Google\Cloud\Language\V1\Document\Type;
    
    /**
     * @param string $text The text to analyze
     */
    function classify_text(string $text): void
    {
        // Make sure we have enough words (20+) to call classifyText
        if (str_word_count($text) < 20) {
            printf('20+ words are required to classify text.' . PHP_EOL);
            return;
        }
        $languageServiceClient = new LanguageServiceClient();
    
        // Create a new Document, add text as content and set type to PLAIN_TEXT
        $document = (new Document())
            ->setContent($text)
            ->setType(Type::PLAIN_TEXT);
    
        // Call the analyzeSentiment function
        $request = (new ClassifyTextRequest())
            ->setDocument($document);
        $response = $languageServiceClient->classifyText($request);
        $categories = $response->getCategories();
        // Print document information
        foreach ($categories as $category) {
            printf('Category Name: %s' . PHP_EOL, $category->getName());
            printf('Confidence: %s' . PHP_EOL, $category->getConfidence());
            print(PHP_EOL);
        }
    }

### Python

To learn how to install and use the client library for Natural Language, see [Natural Language client libraries](https://docs.cloud.google.com/natural-language/docs/reference/libraries). For more information, see the [Natural Language Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/language/latest). 

To authenticate to Natural Language, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import language_v1
    
    
    def sample_classify_text(text_content):
        """
        Classifying Content in a String
    
        Args:
          text_content The text content to analyze.
        """
    
        client = language_v1.LanguageServiceClient()
    
        # text_content = "That actor on TV makes movies in Hollywood and also stars in a variety of popular new TV shows."
    
        # Available types: PLAIN_TEXT, HTML
        type_ = language_v1.Document.Type.PLAIN_TEXT
    
        # Optional. If not specified, the language is automatically detected.
        # For list of supported languages:
        # https://cloud.google.com/natural-language/docs/languages
        language = "en"
        document = {"content": text_content, "type_": type_, "language": language}
    
        content_categories_version = (
            language_v1.[ClassificationModelOptions](https://docs.cloud.google.com/python/docs/reference/language/latest/google.cloud.language_v1.types.ClassificationModelOptions.html).[V2Model](https://docs.cloud.google.com/python/docs/reference/language/latest/google.cloud.language_v1.types.ClassificationModelOptions.V2Model.html).[ContentCategoriesVersion](https://docs.cloud.google.com/python/docs/reference/language/latest/google.cloud.language_v1.types.ClassificationModelOptions.V2Model.ContentCategoriesVersion.html).V2
        )
        response = client.[classify_text](https://docs.cloud.google.com/python/docs/reference/language/latest/google.cloud.language_v1.services.language_service.LanguageServiceClient.html#google_cloud_language_v1_services_language_service_LanguageServiceClient_classify_text)(
            request={
                "document": document,
                "classification_model_options": {
                    "v2_model": {"content_categories_version": content_categories_version}
                },
            }
        )
        # Loop through classified categories returned from the API
        for category in response.categories:
            # Get the name of the category representing the document.
            # See the predefined taxonomy of categories:
            # https://cloud.google.com/natural-language/docs/categories
            print(f"Category name: {category.name}")
            # Get the confidence. Number representing how certain the classifier
            # is that this category represents the provided text.
            print(f"Confidence: {category.confidence}")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudnaturallanguageapi). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
