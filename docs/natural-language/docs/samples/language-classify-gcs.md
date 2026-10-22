---
url: https://docs.cloud.google.com/natural-language/docs/samples/language-classify-gcs/
title: Classify content of a Cloud Storage file \u00a0|\u00a0 Cloud Natural Language API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:17:44.010920+00:00
---

# Classify content of a Cloud Storage file  |  Cloud Natural Language API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/natural-language/docs/samples/language-classify-gcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Natural Language API ](https://docs.cloud.google.com/natural-language/docs)
  * [ Samples ](https://docs.cloud.google.com/natural-language/docs/samples)



#  Classify content of a Cloud Storage file Stay organized with collections  Save and categorize content based on your preferences. 

Analyze a file stored in Google Cloud Storage and return a list of content categories that apply to the text found in the document

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Classifying Content](https://docs.cloud.google.com/natural-language/docs/classifying-text)



## Code sample

### Go

To learn how to install and use the client library for Natural Language, see [Natural Language client libraries](https://docs.cloud.google.com/natural-language/docs/reference/libraries). For more information, see the [Natural Language Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1). 

To authenticate to Natural Language, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    func classifyTextFromGCS(ctx context.Context, gcsURI string) (*languagepb.ClassifyTextResponse, error) {
    	return client.ClassifyText(ctx, &languagepb.ClassifyTextRequest{
    		Document: &languagepb.Document{
    			Source: &languagepb.Document_GcsContentUri{
    				GcsContentUri: gcsURI,
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
      // Set the GCS content URI path
      Document doc =
          Document.newBuilder().setGcsContentUri(gcsUri).setType(Type.PLAIN_TEXT).build();
      ClassifyTextRequest request = ClassifyTextRequest.newBuilder().setDocument(doc).build();
      // Detect categories in the given file
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
    
    
    // Imports the Google Cloud client library.
    const language = require('[@google-cloud/language](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/overview.html)');
    
    // Creates a client.
    const client = new language.[LanguageServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/overview.html)();
    
    /**
     * TODO(developer): Uncomment the following lines to run this code
     */
    // const bucketName = 'Your bucket name, e.g. my-bucket';
    // const fileName = 'Your file name, e.g. my-file.txt';
    
    // Prepares a document, representing a text file in Cloud Storage
    const document = {
      gcsContentUri: `gs://${bucketName}/${fileName}`,
      type: 'PLAIN_TEXT',
    };
    
    // Classifies text in the document
    const [classification] = await client.classifyText({document});
    
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
     * @param string $uri The cloud storage object to analyze (gs://your-bucket-name/your-object-name)
     */
    function classify_text_from_file(string $uri): void
    {
        $languageServiceClient = new LanguageServiceClient();
    
        // Create a new Document, pass GCS URI and set type to PLAIN_TEXT
        $document = (new Document())
            ->setGcsContentUri($uri)
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
    
    
    def sample_classify_text(gcs_content_uri):
        """
        Classifying Content in text file stored in Cloud Storage
    
        Args:
          gcs_content_uri Google Cloud Storage URI where the file content is located.
          e.g. gs://[Your Bucket]/[Path to File]
          The text file must include at least 20 words.
        """
    
        client = language_v1.LanguageServiceClient()
    
        # gcs_content_uri = 'gs://cloud-samples-data/language/classify-entertainment.txt'
    
        # Available types: PLAIN_TEXT, HTML
        type_ = language_v1.Document.Type.PLAIN_TEXT
    
        # Optional. If not specified, the language is automatically detected.
        # For list of supported languages:
        # https://cloud.google.com/natural-language/docs/languages
        language = "en"
        document = {
            "gcs_content_uri": gcs_content_uri,
            "type_": type_,
            "language": language,
        }
    
        response = client.[classify_text](https://docs.cloud.google.com/python/docs/reference/language/latest/google.cloud.language_v1.services.language_service.LanguageServiceClient.html#google_cloud_language_v1_services_language_service_LanguageServiceClient_classify_text)(request={"document": document})
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
