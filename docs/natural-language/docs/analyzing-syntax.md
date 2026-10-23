---
url: https://docs.cloud.google.com/natural-language/docs/analyzing-syntax/
title: Analyzing Syntax \u00a0|\u00a0 Cloud Natural Language API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:03.880019+00:00
---

# Analyzing Syntax  |  Cloud Natural Language API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/natural-language/docs/analyzing-syntax/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Natural Language API ](https://docs.cloud.google.com/natural-language/docs)
  * [ Guides ](https://docs.cloud.google.com/natural-language/docs/setup)



Send feedback 

#  Analyzing Syntax Stay organized with collections  Save and categorize content based on your preferences. 

While most Natural Language methods analyze what a given text is _about_ , the `analyzeSyntax` method inspects the structure of the language itself. **Syntactic Analysis** breaks up the given text into a series of sentences and tokens (generally, words) and provides linguistic information about those tokens. See [Morphology & Dependency Trees](https://docs.cloud.google.com/natural-language/docs/morphology) for details about the linguistic analysis and [Language Support](https://docs.cloud.google.com/natural-language/docs/languages) for a list of the languages whose syntax the Natural Language API can analyze.

This section demonstrates a few ways to detect syntax in a document. For each document, you must submit a separate request.

## Analyzing Syntax in a String

Here is an example of performing syntactic analysis on a text string sent directly to the Natural Language API:

### Protocol

To analyze syntax in a document, make a `POST` request to the [`documents:analyzeSyntax`](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/documents/analyzeSyntax) REST method and provide the appropriate request body as shown in the following example.

The example uses the `gcloud auth application-default print-access-token` command to obtain an access token for a service account set up for the project using the Google Cloud Platform [gcloud CLI](https://cloud.google.com/sdk/). For instructions on installing the gcloud CLI, setting up a project with a service account see the [Quickstart](https://docs.cloud.google.com/natural-language/docs/sentiment-analysis-gcloud).
    
    
    curl -X POST \
         -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
         -H "Content-Type: application/json; charset=utf-8" \
         --data "{
      'encodingType': 'UTF8',
      'document': {
        'type': 'PLAIN_TEXT',
        'content': 'Google, headquartered in Mountain View, unveiled the new Android phone at the Consumer Electronic Show.  Sundar Pichai said in his keynote that users love their new Android phones.'
      }
    }" "https://language.googleapis.com/v1/documents:analyzeSyntax"

If you don't specify `document.language`, then the language will be automatically detected. For information on which languages are supported by the Natural Language API, see [Language Support](https://docs.cloud.google.com/natural-language/docs/languages). See the [`Document`](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/documents#Document) reference documentation for more information on configuring the request body.

If the request is successful, the server returns a `200 OK` HTTP status code and the response in JSON format:
    
    
    {
      "sentences": [
        {
          "text": {
            "content": "Google, headquartered in Mountain View, unveiled the new Android phone at the Consumer Electronic Show.",
            "beginOffset": 0
          }
        },
        {
          "text": {
            "content": "Sundar Pichai said in his keynote that users love their new Android phones.",
            "beginOffset": 105
          }
        }
      ],
      "tokens": [
        {
          "text": {
            "content": "Google",
            "beginOffset": 0
          },
          "partOfSpeech": {
            "tag": "NOUN",
            "aspect": "ASPECT_UNKNOWN",
            "case": "CASE_UNKNOWN",
            "form": "FORM_UNKNOWN",
            "gender": "GENDER_UNKNOWN",
            "mood": "MOOD_UNKNOWN",
            "number": "SINGULAR",
            "person": "PERSON_UNKNOWN",
            "proper": "PROPER",
            "reciprocity": "RECIPROCITY_UNKNOWN",
            "tense": "TENSE_UNKNOWN",
            "voice": "VOICE_UNKNOWN"
          },
          "dependencyEdge": {
            "headTokenIndex": 7,
            "label": "NSUBJ"
          },
          "lemma": "Google"
        },
        ...
        {
          "text": {
            "content": ".",
            "beginOffset": 179
          },
          "partOfSpeech": {
            "tag": "PUNCT",
            "aspect": "ASPECT_UNKNOWN",
            "case": "CASE_UNKNOWN",
            "form": "FORM_UNKNOWN",
            "gender": "GENDER_UNKNOWN",
            "mood": "MOOD_UNKNOWN",
            "number": "NUMBER_UNKNOWN",
            "person": "PERSON_UNKNOWN",
            "proper": "PROPER_UNKNOWN",
            "reciprocity": "RECIPROCITY_UNKNOWN",
            "tense": "TENSE_UNKNOWN",
            "voice": "VOICE_UNKNOWN"
          },
          "dependencyEdge": {
            "headTokenIndex": 20,
            "label": "P"
          },
          "lemma": "."
        }
      ],
      "language": "en"
    }
    

The `tokens` array contains [`Token`](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/Token) objects representing the detected sentence tokens, which include information such as a token's part of speech and its position in the sentence.

### gcloud

Refer to the [`analyze-syntax`](https://docs.cloud.google.com/sdk/gcloud/reference/ml/language/analyze-syntax) command for complete details.

To perform syntax analysis, use the gcloud CLI and use the `--content` flag to identify the content to analyze:
    
    
    gcloud ml language analyze-syntax --content="Google, headquartered in Mountain View, unveiled the new Android phone at the Consumer Electronic Show.  Sundar Pichai said in his keynote that users love their new Android phones."
    

If the request is successful, the server returns a response in JSON format:
    
    
    {
      "sentences": [
        {
          "text": {
            "content": "Google, headquartered in Mountain View, unveiled the new Android phone at the Consumer Electronic Show.",
            "beginOffset": 0
          }
        },
        {
          "text": {
            "content": "Sundar Pichai said in his keynote that users love their new Android phones.",
            "beginOffset": 105
          }
        }
      ],
      "tokens": [
        {
          "text": {
            "content": "Google",
            "beginOffset": 0
          },
          "partOfSpeech": {
            "tag": "NOUN",
            "aspect": "ASPECT_UNKNOWN",
            "case": "CASE_UNKNOWN",
            "form": "FORM_UNKNOWN",
            "gender": "GENDER_UNKNOWN",
            "mood": "MOOD_UNKNOWN",
            "number": "SINGULAR",
            "person": "PERSON_UNKNOWN",
            "proper": "PROPER",
            "reciprocity": "RECIPROCITY_UNKNOWN",
            "tense": "TENSE_UNKNOWN",
            "voice": "VOICE_UNKNOWN"
          },
          "dependencyEdge": {
            "headTokenIndex": 7,
            "label": "NSUBJ"
          },
          "lemma": "Google"
        },
        ...
        {
          "text": {
            "content": ".",
            "beginOffset": 179
          },
          "partOfSpeech": {
            "tag": "PUNCT",
            "aspect": "ASPECT_UNKNOWN",
            "case": "CASE_UNKNOWN",
            "form": "FORM_UNKNOWN",
            "gender": "GENDER_UNKNOWN",
            "mood": "MOOD_UNKNOWN",
            "number": "NUMBER_UNKNOWN",
            "person": "PERSON_UNKNOWN",
            "proper": "PROPER_UNKNOWN",
            "reciprocity": "RECIPROCITY_UNKNOWN",
            "tense": "TENSE_UNKNOWN",
            "voice": "VOICE_UNKNOWN"
          },
          "dependencyEdge": {
            "headTokenIndex": 20,
            "label": "P"
          },
          "lemma": "."
        }
      ],
      "language": "en"
    }
    

The `tokens` array contains [`Token`](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/Token) objects representing the detected sentence tokens, which include information such as a token's part of speech and its position in the sentence.

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
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/natural-language/docs/reference/libraries) on the client libraries page and then visit the [Natural Language reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.Language.V1/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/natural-language/docs/reference/libraries) on the client libraries page and then visit the [Natural Language reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-language/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/natural-language/docs/reference/libraries) on the client libraries page and then visit the [Natural Language reference documentation for Ruby.](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-language/latest)

## Analyzing Syntax from Cloud Storage

For your convenience, the Natural Language API can perform syntactic analysis directly on a file located in Cloud Storage, without the need to send the contents of the file in the body of your request.

Here is an example of performing syntactic analysis on a file located in Cloud Storage.

### Protocol

To analyze syntax in a document stored in Cloud Storage, make a `POST` request to the [`documents:analyzeSyntax`](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/documents/analyzeSyntax) REST method and provide the appropriate request body with the path to the document as shown in the following example.
    
    
    curl -X POST \
         -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
         -H "Content-Type: application/json; charset=utf-8" \
         --data "{
      'encodingType': 'UTF8',
      'document': {
        'type': 'PLAIN_TEXT',
        'gcsContentUri': 'gs://<bucket-name>/<object-name>'
      }
    }" "https://language.googleapis.com/v1/documents:analyzeSyntax"

If you don't specify `document.language`, then the language will be automatically detected. For information on which languages are supported by the Natural Language API, see [Language Support](https://docs.cloud.google.com/natural-language/docs/languages). See the [`Document`](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/documents#Document) reference documentation for more information on configuring the request body.

If the request is successful, the server returns a `200 OK` HTTP status code and the response in JSON format:
    
    
    {
      "sentences": [
        {
          "text": {
            "content": "Hello, world!",
            "beginOffset": 0
          }
        }
      ],
      "tokens": [
        {
          "text": {
            "content": "Hello",
            "beginOffset": 0
          },
          "partOfSpeech": {
            "tag": "X",
            // ...
          },
          "dependencyEdge": {
            "headTokenIndex": 2,
            "label": "DISCOURSE"
          },
          "lemma": "Hello"
        },
        {
          "text": {
            "content": ",",
            "beginOffset": 5
          },
          "partOfSpeech": {
            "tag": "PUNCT",
            // ...
          },
          "dependencyEdge": {
            "headTokenIndex": 2,
            "label": "P"
          },
          "lemma": ","
        },
        // ...
      ],
      "language": "en"
    }

The `tokens` array contains [`Token`](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/Token) objects representing the detected sentence tokens, which include information such as a token's part of speech and its position in the sentence.

### gcloud

Refer to the [`analyze-syntax`](https://docs.cloud.google.com/sdk/gcloud/reference/ml/language/analyze-syntax) command for complete details. 

To perform syntax analysis on a file in Cloud Storage, use the `gcloud` command line tool and use the `--content-file` flag to identify the file path that contains the content to analyze:
    
    
    gcloud ml language analyze-syntax --content-file=gs://YOUR_BUCKET_NAME/YOUR_FILE_NAME
    

If the request is successful, the server returns a response in JSON format:
    
    
    {
      "sentences": [
        {
          "text": {
            "content": "Hello, world!",
            "beginOffset": 0
          }
        }
      ],
      "tokens": [
        {
          "text": {
            "content": "Hello",
            "beginOffset": 0
          },
          "partOfSpeech": {
            "tag": "X",
            // ...
          },
          "dependencyEdge": {
            "headTokenIndex": 2,
            "label": "DISCOURSE"
          },
          "lemma": "Hello"
        },
        {
          "text": {
            "content": ",",
            "beginOffset": 5
          },
          "partOfSpeech": {
            "tag": "PUNCT",
            // ...
          },
          "dependencyEdge": {
            "headTokenIndex": 2,
            "label": "P"
          },
          "lemma": ","
        },
        // ...
      ],
      "language": "en"
    }

The `tokens` array contains [`Token`](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/Token) objects representing the detected sentence tokens, which include information such as a token's part of speech and its position in the sentence.

### Go

To learn how to install and use the client library for Natural Language, see [Natural Language client libraries](https://docs.cloud.google.com/natural-language/docs/reference/libraries). For more information, see the [Natural Language Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1). 

To authenticate to Natural Language, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    func analyzeSyntaxFromGCS(ctx context.Context, gcsURI string) (*languagepb.AnnotateTextResponse, error) {
    	return client.AnnotateText(ctx, &languagepb.AnnotateTextRequest{
    		Document: &languagepb.Document{
    			Source: &languagepb.Document_GcsContentUri{
    				GcsContentUri: gcsURI,
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
          com.google.cloud.language.v1.Document.newBuilder().setGcsContentUri(gcsUri).setType(
            com.google.cloud.language.v1.Document.Type.PLAIN_TEXT
          ).build();
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
     * TODO(developer): Uncomment the following lines to run this code
     */
    // const bucketName = 'Your bucket name, e.g. my-bucket';
    // const fileName = 'Your file name, e.g. my-file.txt';
    
    // Prepares a document, representing a text file in Cloud Storage
    const document = {
      gcsContentUri: `gs://${bucketName}/${fileName}`,
      type: 'PLAIN_TEXT',
    };
    
    // Need to specify an encodingType to receive word offsets
    const encodingType = 'UTF8';
    
    // Detects the sentiment of the document
    const [syntax] = await client.analyzeSyntax({document, encodingType});
    
    console.log('Parts of speech:');
    syntax.tokens.forEach(part => {
      console.log(`${part.partOfSpeech.tag}: ${part.text.content}`);
      console.log('Morphology:', part.partOfSpeech);
    });

### Python

To learn how to install and use the client library for Natural Language, see [Natural Language client libraries](https://docs.cloud.google.com/natural-language/docs/reference/libraries). For more information, see the [Natural Language Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/language/latest). 

To authenticate to Natural Language, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import language_v1
    
    
    def sample_analyze_syntax(gcs_content_uri):
        """
        Analyzing Syntax in text file stored in Cloud Storage
    
        Args:
          gcs_content_uri Google Cloud Storage URI where the file content is located.
          e.g. gs://[Your Bucket]/[Path to File]
        """
    
        client = language_v1.LanguageServiceClient()
    
        # gcs_content_uri = 'gs://cloud-samples-data/language/syntax-sentence.txt'
    
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
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/natural-language/docs/reference/libraries) on the client libraries page and then visit the [Natural Language reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.Language.V1/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/natural-language/docs/reference/libraries) on the client libraries page and then visit the [Natural Language reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-language/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/natural-language/docs/reference/libraries) on the client libraries page and then visit the [Natural Language reference documentation for Ruby.](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-language/latest)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
