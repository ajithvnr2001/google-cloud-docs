---
url: https://docs.cloud.google.com/natural-language/docs/samples/language-entity-sentiment-gcs/
title: Analyze entity sentiment in a Cloud Storage file \u00a0|\u00a0 Cloud Natural Language API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:18:01.110878+00:00
---

# Analyze entity sentiment in a Cloud Storage file  |  Cloud Natural Language API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/natural-language/docs/samples/language-entity-sentiment-gcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Natural Language API ](https://docs.cloud.google.com/natural-language/docs)
  * [ Samples ](https://docs.cloud.google.com/natural-language/docs/samples)



#  Analyze entity sentiment in a Cloud Storage file Stay organized with collections  Save and categorize content based on your preferences. 

Determine the sentiment (positive or negative) expressed about entities within the text from a file stored in Cloud Storage.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Analyzing Entity Sentiment](https://docs.cloud.google.com/natural-language/docs/analyzing-entity-sentiment)



## Code sample

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

### PHP

To learn how to install and use the client library for Natural Language, see [Natural Language client libraries](https://docs.cloud.google.com/natural-language/docs/reference/libraries). 

To authenticate to Natural Language, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Language\V1\AnalyzeEntitySentimentRequest;
    use Google\Cloud\Language\V1\Client\LanguageServiceClient;
    use Google\Cloud\Language\V1\Document;
    use Google\Cloud\Language\V1\Document\Type;
    use Google\Cloud\Language\V1\Entity\Type as EntityType;
    
    /**
     * @param string $uri The cloud storage object to analyze (gs://your-bucket-name/your-object-name)
     */
    function analyze_entity_sentiment_from_file(string $uri): void
    {
        // Create the Natural Language client
        $languageServiceClient = new LanguageServiceClient();
    
        // Create a new Document, pass GCS URI and set type to PLAIN_TEXT
        $document = (new Document())
            ->setGcsContentUri($uri)
            ->setType(Type::PLAIN_TEXT);
    
        // Call the analyzeEntitySentiment function
        $request = (new AnalyzeEntitySentimentRequest())
            ->setDocument($document);
        $response = $languageServiceClient->analyzeEntitySentiment($request);
        $entities = $response->getEntities();
        // Print out information about each entity
        foreach ($entities as $entity) {
            printf('Entity Name: %s' . PHP_EOL, $entity->getName());
            printf('Entity Type: %s' . PHP_EOL, EntityType::name($entity->getType()));
            printf('Entity Salience: %s' . PHP_EOL, $entity->getSalience());
            $sentiment = $entity->getSentiment();
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
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudnaturallanguageapi). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
