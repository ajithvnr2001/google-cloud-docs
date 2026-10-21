---
url: https://docs.cloud.google.com/natural-language/docs/classifying-text/
title: Classifying Content \u00a0|\u00a0 Cloud Natural Language API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:59:53.700192+00:00
---

# Classifying Content  |  Cloud Natural Language API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/natural-language/docs/classifying-text/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Natural Language API ](https://docs.cloud.google.com/natural-language/docs)
  * [ Guides ](https://docs.cloud.google.com/natural-language/docs/setup)



Send feedback 

#  Classifying Content Stay organized with collections  Save and categorize content based on your preferences. 

**Content Classification** analyzes a document and returns a list of content categories that apply to the text found in the document. To classify the content in a document, call the [`classifyText`](https://docs.cloud.google.com/natural-language/reference/rest/v1/documents/classifyText) method.

A complete list of content categories returned for the [`classifyText`](https://docs.cloud.google.com/natural-language/reference/rest/v1/documents/classifyText) method are found [here](https://docs.cloud.google.com/natural-language/docs/categories).

You can choose which model to use for the [`classifyText`](https://docs.cloud.google.com/natural-language/reference/rest/v1/documents/classifyText) method by setting the optional [`classificationModelOptions`](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/ClassificationModelOptions) field:

  * The [`V2 model`](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/ClassificationModelOptions) is a newer model with better performance that supports both [Version 1 content categories](https://docs.cloud.google.com/natural-language/docs/categories#categories_version_1) and [Version 2 content categories](https://docs.cloud.google.com/natural-language/docs/categories#categories_version_2).
  * The [`V1 model`](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/ClassificationModelOptions) supports only [Version 1 content categories](https://docs.cloud.google.com/natural-language/docs/categories#categories_version_1).

**Important:** You must supply a text block (document) with at least twenty tokens (words) to the [`classifyText`](https://docs.cloud.google.com/natural-language/reference/rest/v1/documents/classifyText) method when using the [`V1 model`](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/ClassificationModelOptions).

This section demonstrates how to classify content in a document. For each document, you must submit a separate request.

### Classifying Content

Here is an example of classifying content provided as a string:

### Protocol

To classify content from a document, make a `POST` request to the [`documents:classifyText`](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/documents/classifyText) REST method and provide the appropriate request body as shown in the following example.

The example uses the `gcloud auth application-default print-access-token` command to obtain an access token for a service account set up for the project using the Google Cloud Platform [gcloud CLI](https://cloud.google.com/sdk/). For instructions on installing the gcloud CLI, setting up a project with a service account see the [Quickstart](https://docs.cloud.google.com/natural-language/docs/sentiment-analysis-gcloud).
    
    
    curl -X POST \
         -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
         -H "Content-Type: application/json; charset=utf-8" \
         --data "{
      'document':{
        'type':'PLAIN_TEXT',
        'content':'Google, headquartered in Mountain View, unveiled the new Android
        phone at the Consumer Electronic Show.  Sundar Pichai said in his keynote
        that users love their new Android phones.'
      },
      'classificationModelOptions': {
        'v2Model': {
          'contentCategoriesVersion': 'V2',
        }
      }
    }" "https://language.googleapis.com/v1/documents:classifyText"

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
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/natural-language/docs/reference/libraries) on the client libraries page and then visit the [Natural Language reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.Language.V1/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/natural-language/docs/reference/libraries) on the client libraries page and then visit the [Natural Language reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-language/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/natural-language/docs/reference/libraries) on the client libraries page and then visit the [Natural Language reference documentation for Ruby.](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-language/latest)

### Classifying Content from Cloud Storage

Here is an example of classifying content stored in a text file on Cloud Storage:

### Protocol

To classify content from a document stored in Cloud Storage, make a `POST` request to the [`documents:classifyText`](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/documents/classifyText) REST method and provide the appropriate request body with the path to the document as shown in the following example.
    
    
    curl -X POST \
         -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
         -H "Content-Type: application/json; charset=utf-8" \
         --data "{
      'document':{
        'type':'PLAIN_TEXT',
        'gcsContentUri':'gs://<bucket-name>/<object-name>'
      }
      'classificationModelOptions': {
        'v1Model': {
        }
      }
    }" "https://language.googleapis.com/v1/documents:classifyText"

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
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/natural-language/docs/reference/libraries) on the client libraries page and then visit the [Natural Language reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.Language.V1/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/natural-language/docs/reference/libraries) on the client libraries page and then visit the [Natural Language reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-language/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/natural-language/docs/reference/libraries) on the client libraries page and then visit the [Natural Language reference documentation for Ruby.](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-language/latest)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
