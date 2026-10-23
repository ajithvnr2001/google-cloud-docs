---
url: https://docs.cloud.google.com/natural-language/docs/analyzing-entity-sentiment/
title: Analyzing Entity Sentiment \u00a0|\u00a0 Cloud Natural Language API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:34.715327+00:00
---

# Analyzing Entity Sentiment  |  Cloud Natural Language API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/natural-language/docs/analyzing-entity-sentiment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Natural Language API ](https://docs.cloud.google.com/natural-language/docs)
  * [ Guides ](https://docs.cloud.google.com/natural-language/docs/setup)



Send feedback 

#  Analyzing Entity Sentiment Stay organized with collections  Save and categorize content based on your preferences. 

**Entity Sentiment Analysis** combines both entity analysis and sentiment analysis and attempts to determine the sentiment (positive or negative) expressed about entities within the text. Entity sentiment is represented by numerical score and magnitude values and is determined for each mention of an entity. Those scores are then aggregated into an overall sentiment score and magnitude for an entity. For information on how to interpret the `score` and `magnitude` sentiment values included in the analysis, see [Interpreting sentiment analysis values](https://docs.cloud.google.com/natural-language/docs/basics#interpreting_sentiment_analysis_values).

The following examples show how to query the [`analyzeEntitySentiment`](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/documents/analyzeEntitySentiment) method. For each document, you must submit a separate request.

## Analyzing Entity Sentiment

Here is an example of analyzing entity sentiment provided as a string:

### Protocol

To analyze entity sentiment in a document, make a `POST` request to the [`documents:analyzeEntitySentiment`](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/documents/analyzeEntitySentiment) REST method and provide the appropriate request body as shown in the following example.

The example uses the `gcloud auth application-default print-access-token` command to obtain an access token for a service account set up for the project using the Google Cloud Platform [gcloud CLI](https://cloud.google.com/sdk/). For instructions on installing the gcloud CLI, setting up a project with a service account see the [Quickstart](https://docs.cloud.google.com/natural-language/docs/sentiment-analysis-gcloud).
    
    
    curl -X POST \
         -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
         -H "Content-Type: application/json; charset=utf-8" \
         --data "{
      'document':{
        'type':'PLAIN_TEXT',
        'content':'I love R&B music. Marvin Gaye is the best.
                   \'What\'s Going On\' is one of my favorite songs.
                   It was so sad when Marvin Gaye died.'
      },
      'encodingType':'UTF8'
    }" "https://language.googleapis.com/v1/documents:analyzeEntitySentiment"

### gcloud

Refer to the [`analyze-entity-sentiment`](https://docs.cloud.google.com/sdk/gcloud/reference/ml/language/analyze-entity-sentiment) command for complete details.

To perform entity sentiment analysis, use the gcloud CLI and use the `--content` flag to identify the content to analyze:
    
    
    gcloud ml language analyze-entity-sentiment \
      --content="I love R&B music. Marvin Gaye is the best. 'What's Going On' is one of my favorite songs. It was so sad when Marvin Gaye died."
    

### Go

To learn how to install and use the client library for Natural Language, see [Natural Language client libraries](https://docs.cloud.google.com/natural-language/docs/reference/libraries). For more information, see the [Natural Language Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1). 

To authenticate to Natural Language, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    func analyzeEntitySentiment(ctx context.Context, client *language.Client, text string) (*languagepb.AnalyzeEntitySentimentResponse, error) {
    	return client.AnalyzeEntitySentiment(ctx, &languagepb.AnalyzeEntitySentimentRequest{
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
    
    
    // Instantiate the Language client com.google.cloud.language.v1.LanguageServiceClient
    try (com.google.cloud.language.v1.LanguageServiceClient language =
        com.google.cloud.language.v1.LanguageServiceClient.create()) {
      com.google.cloud.language.v1.Document doc =
          com.google.cloud.language.v1.Document.newBuilder().setContent(text)
              .setType(com.google.cloud.language.v1.Document.Type.PLAIN_TEXT).build();
      AnalyzeEntitySentimentRequest request =
          AnalyzeEntitySentimentRequest.newBuilder()
              .setDocument(doc)
              .setEncodingType(com.google.cloud.language.v1.EncodingType.UTF16)
              .build();
      // Detect entity sentiments in the given string
      AnalyzeEntitySentimentResponse response = language.analyzeEntitySentiment(request);
      // Print the response
      for (com.google.cloud.language.v1.Entity entity : response.getEntitiesList()) {
        System.out.printf("Entity: %s\n", entity.getName());
        System.out.printf("Salience: %.3f\n", entity.getSalience());
        System.out.printf("Sentiment : %s\n", entity.getSentiment());
        for (com.google.cloud.language.v1.EntityMention mention : entity.getMentionsList()) {
          System.out.printf("Begin offset: %d\n", mention.getText().getBeginOffset());
          System.out.printf("Content: %s\n", mention.getText().getContent());
          System.out.printf("Magnitude: %.3f\n", mention.getSentiment().getMagnitude());
          System.out.printf("Sentiment score : %.3f\n", mention.getSentiment().getScore());
          System.out.printf("Type: %s\n\n", mention.getType());
        }
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
    
    // Detects sentiment of entities in the document
    const [result] = await client.analyzeEntitySentiment({document});
    const entities = result.entities;
    
    console.log('Entities and sentiments:');
    entities.forEach(entity => {
      console.log(`  Name: ${entity.name}`);
      console.log(`  Type: ${entity.type}`);
      console.log(`  Score: ${entity.sentiment.score}`);
      console.log(`  Magnitude: ${entity.sentiment.magnitude}`);
    });

### Python

To learn how to install and use the client library for Natural Language, see [Natural Language client libraries](https://docs.cloud.google.com/natural-language/docs/reference/libraries). For more information, see the [Natural Language Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/language/latest). 

To authenticate to Natural Language, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import language_v1
    
    
    def sample_analyze_entity_sentiment(text_content):
        """
        Analyzing Entity Sentiment in a String
    
        Args:
          text_content The text content to analyze
        """
    
        client = language_v1.LanguageServiceClient()
    
        # text_content = 'Grapes are good. Bananas are bad.'
    
        # Available types: PLAIN_TEXT, HTML
        type_ = language_v1.types.Document.Type.PLAIN_TEXT
    
        # Optional. If not specified, the language is automatically detected.
        # For list of supported languages:
        # https://cloud.google.com/natural-language/docs/languages
        language = "en"
        document = {"content": text_content, "type_": type_, "language": language}
    
        # Available values: NONE, UTF8, UTF16, UTF32
        encoding_type = language_v1.EncodingType.UTF8
    
        response = client.[analyze_entity_sentiment](https://docs.cloud.google.com/python/docs/reference/language/latest/google.cloud.language_v1.services.language_service.LanguageServiceClient.html#google_cloud_language_v1_services_language_service_LanguageServiceClient_analyze_entity_sentiment)(
            request={"document": document, "encoding_type": encoding_type}
        )
        # Loop through entitites returned from the API
        for entity in response.entities:
            print(f"Representative name for the entity: {entity.name}")
            # Get entity type, e.g. PERSON, LOCATION, ADDRESS, NUMBER, et al
            print(f"Entity type: {language_v1.Entity.Type(entity.type_).name}")
            # Get the salience score associated with the entity in the [0, 1.0] range
            print(f"Salience score: {entity.salience}")
            # Get the aggregate sentiment expressed for this entity in the provided document.
            sentiment = entity.sentiment
            print(f"Entity sentiment score: {sentiment.score}")
            print(f"Entity sentiment magnitude: {sentiment.magnitude}")
            # Loop over the metadata associated with entity. For many known entities,
            # the metadata is a Wikipedia URL (wikipedia_url) and Knowledge Graph MID (mid).
            # Some entity types may have additional metadata, e.g. ADDRESS entities
            # may have metadata for the address street_name, postal_code, et al.
            for metadata_name, metadata_value in entity.metadata.items():
                print(f"{metadata_name} = {metadata_value}")
    
            # Loop over the mentions of this entity in the input document.
            # The API currently supports proper noun mentions.
            for mention in entity.mentions:
                print(f"Mention text: {mention.text.content}")
                # Get the mention type, e.g. PROPER for proper noun
                print(
                    "Mention type: {}".format(
                        language_v1.EntityMention.Type(mention.type_).name
                    )
                )
    
        # Get the language of the text, which will be the same as
        # the language specified in the request or, if not specified,
        # the automatically-detected language.
        print(f"Language of the text: {response.language}")
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/natural-language/docs/reference/libraries) on the client libraries page and then visit the [Natural Language reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.Language.V1/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/natural-language/docs/reference/libraries) on the client libraries page and then visit the [Natural Language reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-language/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/natural-language/docs/reference/libraries) on the client libraries page and then visit the [Natural Language reference documentation for Ruby.](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-language/latest)

## Analyzing Entity Sentiment from Cloud Storage

Here is an example of analyzing entity sentiment stored in a text file on Cloud Storage:

### Protocol

To analyze entity sentiment from a document stored in Cloud Storage, make a `POST` request to the [`documents:analyzeEntitySentiment`](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/documents/analyzeEntitySentiment) REST method and provide the appropriate request body with the path to the document as shown in the following example.
    
    
    curl -X POST \
         -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
         -H "Content-Type: application/json; charset=utf-8" \
         --data "{
      'document':{
        'type':'PLAIN_TEXT',
        'gcsContentUri':'gs://<bucket-name>/<object-name>'
      }
    }" "https://language.googleapis.com/v1/documents:analyzeEntitySentiment"

### gcloud

Refer to the [`analyze-entity-sentiment`](https://docs.cloud.google.com/sdk/gcloud/reference/ml/language/analyze-entity-sentiment) command for complete details.

To perform entity sentiment analysis, use the gcloud CLI and use the `--content` flag to identify the content to analyze:
    
    
    gcloud ml language analyze-entity-sentiment \
      --content-file=gs://<bucket-name>/<object-name>
    

### Java

To learn how to install and use the client library for Natural Language, see [Natural Language client libraries](https://docs.cloud.google.com/natural-language/docs/reference/libraries). For more information, see the [Natural Language Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/overview). 

To authenticate to Natural Language, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Instantiate the Language client com.google.cloud.language.v1.LanguageServiceClient
    try (com.google.cloud.language.v1.LanguageServiceClient language =
        com.google.cloud.language.v1.LanguageServiceClient.create()) {
      com.google.cloud.language.v1.Document doc =
          com.google.cloud.language.v1.Document.newBuilder().setGcsContentUri(gcsUri)
              .setType(com.google.cloud.language.v1.Document.Type.PLAIN_TEXT).build();
      AnalyzeEntitySentimentRequest request =
          AnalyzeEntitySentimentRequest.newBuilder()
              .setDocument(doc)
              .setEncodingType(com.google.cloud.language.v1.EncodingType.UTF16)
              .build();
      // Detect entity sentiments in the given file
      AnalyzeEntitySentimentResponse response = language.analyzeEntitySentiment(request);
      // Print the response
      for (com.google.cloud.language.v1.Entity entity : response.getEntitiesList()) {
        System.out.printf("Entity: %s\n", entity.getName());
        System.out.printf("Salience: %.3f\n", entity.getSalience());
        System.out.printf("Sentiment : %s\n", entity.getSentiment());
        for (com.google.cloud.language.v1.EntityMention mention : entity.getMentionsList()) {
          System.out.printf("Begin offset: %d\n", mention.getText().getBeginOffset());
          System.out.printf("Content: %s\n", mention.getText().getContent());
          System.out.printf("Magnitude: %.3f\n", mention.getSentiment().getMagnitude());
          System.out.printf("Sentiment score : %.3f\n", mention.getSentiment().getScore());
          System.out.printf("Type: %s\n\n", mention.getType());
        }
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
     * TODO(developer): Uncomment the following lines to run this code
     */
    // const bucketName = 'Your bucket name, e.g. my-bucket';
    // const fileName = 'Your file name, e.g. my-file.txt';
    
    // Prepares a document, representing a text file in Cloud Storage
    const document = {
      gcsContentUri: `gs://${bucketName}/${fileName}`,
      type: 'PLAIN_TEXT',
    };
    
    // Detects sentiment of entities in the document
    const [result] = await client.analyzeEntitySentiment({document});
    const entities = result.entities;
    
    console.log('Entities and sentiments:');
    entities.forEach(entity => {
      console.log(`  Name: ${entity.name}`);
      console.log(`  Type: ${entity.type}`);
      console.log(`  Score: ${entity.sentiment.score}`);
      console.log(`  Magnitude: ${entity.sentiment.magnitude}`);
    });

### Python

To learn how to install and use the client library for Natural Language, see [Natural Language client libraries](https://docs.cloud.google.com/natural-language/docs/reference/libraries). For more information, see the [Natural Language Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/language/latest). 

To authenticate to Natural Language, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import language_v1
    
    
    def sample_analyze_entity_sentiment(gcs_content_uri):
        """
        Analyzing Entity Sentiment in text file stored in Cloud Storage
    
        Args:
          gcs_content_uri Google Cloud Storage URI where the file content is located.
          e.g. gs://[Your Bucket]/[Path to File]
        """
    
        client = language_v1.LanguageServiceClient()
    
        # gcs_content_uri = 'gs://cloud-samples-data/language/entity-sentiment.txt'
    
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
    
        # Available values: NONE, UTF8, UTF16, UTF32
        encoding_type = language_v1.EncodingType.UTF8
    
        response = client.[analyze_entity_sentiment](https://docs.cloud.google.com/python/docs/reference/language/latest/google.cloud.language_v1.services.language_service.LanguageServiceClient.html#google_cloud_language_v1_services_language_service_LanguageServiceClient_analyze_entity_sentiment)(
            request={"document": document, "encoding_type": encoding_type}
        )
        # Loop through entitites returned from the API
        for entity in response.entities:
            print(f"Representative name for the entity: {entity.name}")
            # Get entity type, e.g. PERSON, LOCATION, ADDRESS, NUMBER, et al
            print(f"Entity type: {language_v1.Entity.Type(entity.type_).name}")
            # Get the salience score associated with the entity in the [0, 1.0] range
            print(f"Salience score: {entity.salience}")
            # Get the aggregate sentiment expressed for this entity in the provided document.
            sentiment = entity.sentiment
            print(f"Entity sentiment score: {sentiment.score}")
            print(f"Entity sentiment magnitude: {sentiment.magnitude}")
            # Loop over the metadata associated with entity. For many known entities,
            # the metadata is a Wikipedia URL (wikipedia_url) and Knowledge Graph MID (mid).
            # Some entity types may have additional metadata, e.g. ADDRESS entities
            # may have metadata for the address street_name, postal_code, et al.
            for metadata_name, metadata_value in entity.metadata.items():
                print(f"{metadata_name} = {metadata_value}")
    
            # Loop over the mentions of this entity in the input document.
            # The API currently supports proper noun mentions.
            for mention in entity.mentions:
                print(f"Mention text: {mention.text.content}")
                # Get the mention type, e.g. PROPER for proper noun
                print(
                    "Mention type: {}".format(
                        language_v1.EntityMention.Type(mention.type_).name
                    )
                )
    
        # Get the language of the text, which will be the same as
        # the language specified in the request or, if not specified,
        # the automatically-detected language.
        print(f"Language of the text: {response.language}")
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/natural-language/docs/reference/libraries) on the client libraries page and then visit the [Natural Language reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.Language.V1/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/natural-language/docs/reference/libraries) on the client libraries page and then visit the [Natural Language reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-language/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/natural-language/docs/reference/libraries) on the client libraries page and then visit the [Natural Language reference documentation for Ruby.](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-language/latest)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
