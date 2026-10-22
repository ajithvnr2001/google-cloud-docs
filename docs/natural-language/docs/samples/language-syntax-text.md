---
url: https://docs.cloud.google.com/natural-language/docs/samples/language-syntax-text/
title: Analyze syntax of a string \u00a0|\u00a0 Cloud Natural Language API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:17:37.637301+00:00
---

# Analyze syntax of a string  |  Cloud Natural Language API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/natural-language/docs/samples/language-syntax-text/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Natural Language API ](https://docs.cloud.google.com/natural-language/docs)
  * [ Samples ](https://docs.cloud.google.com/natural-language/docs/samples)



#  Analyze syntax of a string Stay organized with collections  Save and categorize content based on your preferences. 

Break up the given text into a series of sentences and tokens (generally, words) and provide linguistic information about those tokens.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Analyzing Syntax](https://docs.cloud.google.com/natural-language/docs/analyzing-syntax)



## Code sample

### Go

To learn how to install and use the client library for Natural Language, see [Natural Language client libraries](https://docs.cloud.google.com/natural-language/docs/reference/libraries). For more information, see the [Natural Language Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1). 

To authenticate to Natural Language, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    func analyzeSyntax(ctx context.Context, client *language.Client, text string) (*languagepb.AnnotateTextResponse, error) {
    	return client.AnnotateText(ctx, &languagepb.AnnotateTextRequest{
    		Document: &languagepb.Document{
    			Source: &languagepb.Document_Content{
    				Content: text,
    			},
    			Type: languagepb.Document_PLAIN_TEXT,
    		},
    		Features: &languagepb.AnnotateTextRequest_Features{
    			ExtractSyntax: true,
    		},
    		EncodingType: languagepb.EncodingType_UTF8,
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
      AnalyzeSyntaxRequest request =
          AnalyzeSyntaxRequest.newBuilder()
              .setDocument(doc)
              .setEncodingType(com.google.cloud.language.v1.EncodingType.UTF16)
              .build();
      // Analyze the syntax in the given text
      AnalyzeSyntaxResponse response = language.analyzeSyntax(request);
      // Print the response
      for (Token token : response.getTokensList()) {
        System.out.printf("\tText: %s\n", token.getText().getContent());
        System.out.printf("\tBeginOffset: %d\n", token.getText().getBeginOffset());
        System.out.printf("Lemma: %s\n", token.getLemma());
        System.out.printf("PartOfSpeechTag: %s\n", token.getPartOfSpeech().getTag());
        System.out.printf("\tAspect: %s\n", token.getPartOfSpeech().getAspect());
        System.out.printf("\tCase: %s\n", token.getPartOfSpeech().getCase());
        System.out.printf("\tForm: %s\n", token.getPartOfSpeech().getForm());
        System.out.printf("\tGender: %s\n", token.getPartOfSpeech().getGender());
        System.out.printf("\tMood: %s\n", token.getPartOfSpeech().getMood());
        System.out.printf("\tNumber: %s\n", token.getPartOfSpeech().getNumber());
        System.out.printf("\tPerson: %s\n", token.getPartOfSpeech().getPerson());
        System.out.printf("\tProper: %s\n", token.getPartOfSpeech().getProper());
        System.out.printf("\tReciprocity: %s\n", token.getPartOfSpeech().getReciprocity());
        System.out.printf("\tTense: %s\n", token.getPartOfSpeech().getTense());
        System.out.printf("\tVoice: %s\n", token.getPartOfSpeech().getVoice());
        System.out.println("DependencyEdge");
        System.out.printf("\tHeadTokenIndex: %d\n", token.getDependencyEdge().getHeadTokenIndex());
        System.out.printf("\tLabel: %s\n\n", token.getDependencyEdge().getLabel());
      }
      return response.getTokensList();
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
    
    // Need to specify an encodingType to receive word offsets
    const encodingType = 'UTF8';
    
    // Detects the sentiment of the document
    const [syntax] = await client.analyzeSyntax({document, encodingType});
    
    console.log('Tokens:');
    syntax.tokens.forEach(part => {
      console.log(`${part.partOfSpeech.tag}: ${part.text.content}`);
      console.log('Morphology:', part.partOfSpeech);
    });

### PHP

To learn how to install and use the client library for Natural Language, see [Natural Language client libraries](https://docs.cloud.google.com/natural-language/docs/reference/libraries). 

To authenticate to Natural Language, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Language\V1\AnalyzeSyntaxRequest;
    use Google\Cloud\Language\V1\Client\LanguageServiceClient;
    use Google\Cloud\Language\V1\Document;
    use Google\Cloud\Language\V1\Document\Type;
    use Google\Cloud\Language\V1\PartOfSpeech\Tag;
    
    /**
     * @param string $text The text to analyze
     */
    function analyze_syntax(string $text): void
    {
        // Create the Natural Language client
        $languageServiceClient = new LanguageServiceClient();
    
        // Create a new Document, add text as content and set type to PLAIN_TEXT
        $document = (new Document())
            ->setContent($text)
            ->setType(Type::PLAIN_TEXT);
    
        // Call the analyzeEntities function
        $request = (new AnalyzeSyntaxRequest())
            ->setDocument($document);
        $response = $languageServiceClient->analyzeSyntax($request);
        $tokens = $response->getTokens();
        // Print out information about each entity
        foreach ($tokens as $token) {
            printf('Token text: %s' . PHP_EOL, $token->getText()->getContent());
            printf('Token part of speech: %s' . PHP_EOL, Tag::name($token->getPartOfSpeech()->getTag()));
            print(PHP_EOL);
        }
    }

### Python

To learn how to install and use the client library for Natural Language, see [Natural Language client libraries](https://docs.cloud.google.com/natural-language/docs/reference/libraries). For more information, see the [Natural Language Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/language/latest). 

To authenticate to Natural Language, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import language_v1
    
    
    def sample_analyze_syntax(text_content):
        """
        Analyzing Syntax in a String
    
        Args:
          text_content The text content to analyze
        """
    
        client = language_v1.LanguageServiceClient()
    
        # text_content = 'This is a short sentence.'
    
        # Available types: PLAIN_TEXT, HTML
        type_ = language_v1.Document.Type.PLAIN_TEXT
    
        # Optional. If not specified, the language is automatically detected.
        # For list of supported languages:
        # https://cloud.google.com/natural-language/docs/languages
        language = "en"
        document = {"content": text_content, "type_": type_, "language": language}
    
        # Available values: NONE, UTF8, UTF16, UTF32
        encoding_type = language_v1.EncodingType.UTF8
    
        response = client.[analyze_syntax](https://docs.cloud.google.com/python/docs/reference/language/latest/google.cloud.language_v1.services.language_service.LanguageServiceClient.html#google_cloud_language_v1_services_language_service_LanguageServiceClient_analyze_syntax)(
            request={"document": document, "encoding_type": encoding_type}
        )
        # Loop through tokens returned from the API
        for token in response.tokens:
            # Get the text content of this token. Usually a word or punctuation.
            text = token.text
            print(f"Token text: {text.content}")
            print(f"Location of this token in overall document: {text.begin_offset}")
            # Get the part of speech information for this token.
            # Part of speech is defined in:
            # http://www.lrec-conf.org/proceedings/lrec2012/pdf/274_Paper.pdf
            part_of_speech = token.part_of_speech
            # Get the tag, e.g. NOUN, ADJ for Adjective, et al.
            print(
                "Part of Speech tag: {}".format(
                    language_v1.[PartOfSpeech](https://docs.cloud.google.com/python/docs/reference/language/latest/google.cloud.language_v1.types.PartOfSpeech.html).[Tag](https://docs.cloud.google.com/python/docs/reference/language/latest/google.cloud.language_v1.types.PartOfSpeech.Tag.html)(part_of_speech.tag).name
                )
            )
            # Get the voice, e.g. ACTIVE or PASSIVE
            print(
                "Voice: {}".format(
                    language_v1.[PartOfSpeech](https://docs.cloud.google.com/python/docs/reference/language/latest/google.cloud.language_v1.types.PartOfSpeech.html).[Voice](https://docs.cloud.google.com/python/docs/reference/language/latest/google.cloud.language_v1.types.PartOfSpeech.Voice.html)(part_of_speech.voice).name
                )
            )
            # Get the tense, e.g. PAST, FUTURE, PRESENT, et al.
            print(
                "Tense: {}".format(
                    language_v1.[PartOfSpeech](https://docs.cloud.google.com/python/docs/reference/language/latest/google.cloud.language_v1.types.PartOfSpeech.html).[Tense](https://docs.cloud.google.com/python/docs/reference/language/latest/google.cloud.language_v1.types.PartOfSpeech.Tense.html)(part_of_speech.tense).name
                )
            )
            # See API reference for additional Part of Speech information available
            # Get the lemma of the token. Wikipedia lemma description
            # https://en.wikipedia.org/wiki/Lemma_(morphology)
            print(f"Lemma: {token.lemma}")
            # Get the dependency tree parse information for this token.
            # For more information on dependency labels:
            # http://www.aclweb.org/anthology/P13-2017
            dependency_edge = token.dependency_edge
            print(f"Head token index: {dependency_edge.head_token_index}")
            print(
                "Label: {}".format(
                    language_v1.[DependencyEdge](https://docs.cloud.google.com/python/docs/reference/language/latest/google.cloud.language_v1.types.DependencyEdge.html).[Label](https://docs.cloud.google.com/python/docs/reference/language/latest/google.cloud.language_v1.types.DependencyEdge.Label.html)(dependency_edge.label).name
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
