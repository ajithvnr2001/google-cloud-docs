---
url: https://docs.cloud.google.com/translate/docs/advanced/adaptive-translation/
title: Translate text by using adaptive translation \u00a0|\u00a0 Cloud Translation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:59.585153+00:00
---

# Translate text by using adaptive translation  |  Cloud Translation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/translate/docs/advanced/adaptive-translation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Translation ](https://docs.cloud.google.com/translate/docs)
  * [ Guides ](https://docs.cloud.google.com/translate/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Translate text by using adaptive translation

When you request an adaptive translation, you provide the text to translate and example translations that Cloud Translation uses to tailor its responses.

For programmatic translation requests, you can include example translations in a dataset or as part of your translation request. When you use a dataset, Cloud Translation automatically selects five reference sentences that are most similar to your source sentence to customize translations. If you include reference sentences in your translation request, Cloud Translation uses all of them to customize the translation.

## Before you begin

To use adaptive translation, you must enable the Cloud Translation API in your project and set up authentication. For more information, see the Cloud Translation [Setup](https://docs.cloud.google.com/translate/docs/setup).

Also, check that your source and target [languages](https://docs.cloud.google.com/translate/docs/languages#adaptive_translation) are supported by adaptive translation.

### Data requirements and suggestions

If you create a dataset or use the Google Cloud console, you must provide example translations in a [TSV or TMX file](https://docs.cloud.google.com/translate/docs/advanced/custom-translations#file-prep). The examples must be sentence pairs in your intended source and target languages. We recommend that you provide examples that cover the vocabulary, usage, and grammatical quirks of your domain. For additional tips, see [Data preparation](https://docs.cloud.google.com/translate/docs/advanced/automl-beginner#data-preparation) in the AutoML Translation documentation.

Your data must include at least 5 sentence pairs and no more than 10,000 pairs if you use the console and no more than 30,000 pairs if you use the API. A segment pair can be at most 512 characters (total).

### Limitations

  * You can translate to only one target language at a time.
  * Adaptive translation has limits on the number of input and output characters. For more information, see the [Adaptive translation](https://docs.cloud.google.com/translate/quotas#adaptive_translation) limits on the Quotas page.



## Request translations

For translations, the input can be plain text or HTML. Cloud Translation doesn't translate any HTML tags in the input, only text that appears between the tags. The output retains the (untranslated) HTML tags, with the translated text between the tags to the extent possible due to differences between the source and target languages.

**Note:** Cloud Translation API does not support input text that uses other markup languages such as XML. The result when attempting to translate content with other forms of markup is undefined.

### Console

When using the Google Cloud console, select a file that includes your example translations and then request translations. Cloud Translation doesn't store your imported data. If you prefer to work with persistent datasets, use the API.

  1. Go to the AutoML Translation console.

[Go to the Adaptive Translation page](https://console.cloud.google.com/translation/adaptive-translation)

  2. Select a local file or a file in Cloud Storage that contains your example translations.

After you select a file, Cloud Translation sets the **Source language** and **Target language** fields based on your data. For example, if you import an English to Portuguese dataset, the console lets you translate only English sentences to Portuguese.

  3. Enter text in the source language field.

Adaptive translation does have limits on the number of input and output characters. For more information, see the [Adaptive translation limits](https://docs.cloud.google.com/translate/quotas#adaptive_translation) on the Quotas page.

  4. To adjust parameters, use the sliders or text fields to set values:

     * **Temperature** \- Controls the degree of randomness in token selection. For lower temperatures, expect a true or correct response. For higher temperatures, expect more diverse or unexpected results.
     * **Number of examples** \- Sets the number of examples to use from your source data to prompt the LLM.
  5. Select **Compare with NMT model** to include translations from the default Google NMT model along with the adaptive translation output.

  6. Click **Translate**.

In a few moments, Cloud Translation returns a response in the target language field. Cloud Translation doesn't return any text beyond the output character limit.




### API

Use the API to request adaptive translations by including reference sentence pairs or by specifying a dataset.

  * Adaptive translations with reference sentence pairs
  * Adaptive translations with a dataset

**Note:** The API has a limit of one QPS per project.

## Adaptive translations with reference sentence pairs

To include example translations as part of your translation requests, include your example source and target sentence pairs in the `referenceSentencePairs` field, which is part of the `referenceSentenceConfig` object. For more information, see the [adaptiveMtTranslate](https://docs.cloud.google.com/translate/docs/reference/rest/v3/projects.locations/adaptiveMtTranslate) method. You can include up to five sentence pairs.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_NUMBER_OR_ID: the numeric or alphanumeric ID of your Google Cloud project
  * LOCATION: The region where your translation request is handled, such as `us-central1`.
  * REFERENCE_SOURCE: A sentence in the source language that is part of a reference sentence pair.
  * REFERENCE_TARGET: A sentence in the target language that is part of a reference sentence pair.
  * SOURCE_LANGUAGE: The [language code](https://docs.cloud.google.com/translate/docs/languages#adaptive_translation) of the source text.
  * TARGET_LANGUAGE: The [language code](https://docs.cloud.google.com/translate/docs/languages#adaptive_translation) of the language to translate the source text to.
  * SOURCE_TEXT: The text to translate.
  * MIME_TYPE (Optional): The format of the source text, such as `text/html` or `text/plain`. By default, the MIME type is set to `text/plain`.



HTTP method and URL: 
    
    
    POST https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION:adaptiveMtTranslate

Request JSON body: 
    
    
    {
      "referenceSentenceConfig": {
        "referenceSentencePairLists": [
          {
            "referenceSentencePairs": [{
              "sourceSentence": REFERENCE_SOURCE_1_1,
              "targetSentence": REFERENCE_TARGET_1_1
            },
            {
              "sourceSentence": REFERENCE_SOURCE_1_2,
              "targetSentence": REFERENCE_SOURCE_1_2
            }]
          }
        ],
        "sourceLanguageCode": SOURCE_LANGUAGE,
        "targetLanguageCode": TARGET_LANGUAGE
      }
      "content": ["SOURCE_TEXT"],
      "mimeType": "MIME_TYPE"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_NUMBER_OR_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION:adaptiveMtTranslate"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_NUMBER_OR_ID" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION:adaptiveMtTranslate" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "translations": [
        {
          "translatedText": "TRANSLATED_TEXT"
        }
      ],
      "languageCode": "TARGET_LANGUAGE"
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /** Translates using AdaptiveMt. */
    private static void adaptiveMtTranslate(
        TranslationServiceClient translationServiceClient, String projectId, String sourceLang, String targetLang, Pair<String, String> referencePairs) {
      ReferenceSentencePairList refList = ReferenceSentencePairList.newBuilder();
      for (Pair<String, String> referencePair: referencePairs) {
        ReferenceSentencePair refPair = ReferenceSentencePair.newBuilder()
          .setSourceSentence(referencePair.getKey())
          .setTargetSentence(referencePair.getValue());
        refList.addReferenceSentencePair(refPair);
      }
      AdaptiveMtTranslateRequest request =
          AdaptiveMtTranslateRequest.newBuilder()
              .setParent(LocationName.of(projectId, "us-central1").toString())
              .setSourceLanguageCode(sourceLang)
              .setTargetLanguageCOde(targetLang)
              .addReferenceSentencePairLists(refList)
              .build();
      AdaptiveMtTranslateResponse response = translationServiceClient.adaptiveMtTranslate(request);
    
      System.out.println("Translating using AdaptiveMt");
      System.out.println(response);
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Node.js API reference documentation](https://googleapis.dev/nodejs/translate/latest/index.html). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    async function translate() {
      const request = {
        parent: `projects/${projectId}/locations/${location}`,
        referenceSentenceConfig: {
          referenceSentencePairLists: [
            {
              referenceSentencePairs: [{
                sourceSentence: 'Sample reference source 1'
                targetSentence: 'Sample reference target 1'
              },
              {
                sourceSentence: 'Sample reference source 2'
                targetSentence: 'Sample reference target 2'
              }]
            }
          ],
          sourceLanguageCode: 'en'
          targetLanguageCode: 'ja'
        },
        content: ['Sample translate query']
      } const [response] = await translationClient.adaptiveMtTranslate(request)
      console.log('Translating')
      console.log(response)
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/translate/latest). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def adaptive_mt_translate():
      # Create a client
      client = translate.TranslationServiceClient()
      # Initialize the request
      request = translate.AdaptiveMtTranslateRequest(
        parent="projects/PROJECT_ID/locations/LOCATION",
        reference_sentence_config=[
          "reference_sentence_pair_lists": [
            "reference_sentence_pairs": {
              "source_sentence": 'REFERENCE_SOURCE_1_1'
              "target_sentence": 'REFERENCE_TARGET_1_1'
            },
            "reference_sentence_pairs": {
              "source_sentence": 'REFERENCE_SOURCE_1_2'
              "target_sentence": 'REFERENCE_TARGET_1_2'
            }
          ],
          "source_language_code": 'SOURCE_LANGUAGE'
          "target_language_code": 'TARGET_LANGUAGE'
        ],
        content=["SOURCE_TEXT"]
      )
      # Make the request
      response = client.adaptive_mt_translate(request)
      # Handle the response
      print(response)

## Adaptive translations with a dataset

To use a dataset with translations, create a dataset and import sentence pairs first. If you already have a dataset, you can request adaptive translations with it. The dataset persists in your project until you delete it.

  1. Create a dataset where you import your example translations.

The source and target [languages](https://docs.cloud.google.com/translate/docs/languages#adaptive_translation) must match the languages that you intend to use in your translations. For more information, see the [adaptiveMtDataset.create](https://docs.cloud.google.com/translate/docs/reference/rest/v3/projects.locations.adaptiveMtDatasets/create) method.

### REST

Before using any of the request data, make the following replacements: 

     * PROJECT_NUMBER_OR_ID: the numeric or alphanumeric ID of your Google Cloud project
     * LOCATION: The region where your source dataset is located, such as `us-central1`.
     * DATASET_ID: A unique identifier for your dataset. 
     * DISPLAY_NAME: A descriptive name for your dataset. 
     * SOURCE_LANGUAGE: The language code of the input text. For supported language codes, see [Supported languages](https://docs.cloud.google.com/translate/docs/languages#adaptive_translation).
     * TARGET_LANGUAGE: The target language to translate the input text to. For supported language codes, see [Supported languages](https://docs.cloud.google.com/translate/docs/languages#adaptive_translation).

HTTP method and URL: 
    
    POST https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION/adaptiveMtDatasets

Request JSON body: 
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/adaptiveMtDatasets/DATASET_ID,
      "display_name": "DISPLAY_NAME",
      "source_language_code": "SOURCE_LANGUAGE",
      "target_language_code": "TARGET_LANGUAGE"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_NUMBER_OR_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION/adaptiveMtDatasets"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_NUMBER_OR_ID" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION/adaptiveMtDatasets" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/adaptiveMtDatasets/DATASET_ID",
      "displayName": "DISPLAY_NAME",
      "sourceLanguageCode": "SOURCE_LANGUAGE",
      "targetLanguageCode": "TARGET_LANGUAGE"
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    /** Creates an AdaptiveMtDataset. */
    private static void createAdaptiveMtDataset(
        TranslationServiceClient translationServiceClient, String projectName, String datasetName) {
      String adaptiveMtDatasetName =
          String.format(
              "projects/%s/locations/LOCATION/adaptiveMtDatasets/%s", projectName, datasetName);
      AdaptiveMtDataset adaptiveMtDataset =
          AdaptiveMtDataset.newBuilder()
              .setName(adaptiveMtDatasetName)
              .setDisplayName("DATASET_DISPLAY_NAME")
              .setSourceLanguageCode("SOURCE_LANGUAGE_CODE")
              .setTargetLanguageCode("TARGET_LANGUAGE_CODE")
              .build();
      CreateAdaptiveMtDatasetRequest request =
          CreateAdaptiveMtDatasetRequest.newBuilder()
              .setParent(LocationName.of("PROJECT_NAME", "LOCATION").toString())
              .setAdaptiveMtDataset(adaptiveMtDataset)
              .build();
      AdaptiveMtDataset dataset = translationServiceClient.createAdaptiveMtDataset(request);
      System.out.println("Created dataset");
      System.out.println(dataset);
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Node.js API reference documentation](https://googleapis.dev/nodejs/translate/latest/index.html). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    async function createAdaptiveMtDataset() {
      // Construct request
      const request = {
        parent: `projects/${projectId}/locations/${location}`,
        adaptiveMtDataset: {
          name: `projects/${projectId}/locations/${location}/adaptiveMtDatasets/${
              adaptiveMtDatasetName}`,
          displayName: 'DATASET_DISPLAY_NAME',
          sourceLanguageCode: 'SOURCE_LANGUAGE_CODE',
          targetLanguageCode: 'TARGET_LANGUAGE_CODE',
        }
      };
    
      // Run request
      const [response] = await translationClient.createAdaptiveMtDataset(request);
      console.log('Created')
      console.log(response)
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/translate/latest). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    def create_adaptive_mt_dataset():
      # Create a client
      client = translate.TranslationServiceClient()
      # Initialize request argument(s)
      adaptive_mt_dataset = translate.AdaptiveMtDataset()
      adaptive_mt_dataset.name = "projects/PROJECT_ID/locations/LOCATION/adaptiveMtDatasets/DATASET_ID"
      adaptive_mt_dataset.display_name = "DATASET_DISPLAY_NAME"
      adaptive_mt_dataset.source_language_code = "SOURCE_LANGUAGE_CODE"
      adaptive_mt_dataset.target_language_code = "TARGET_LANGUAGE_CODE"
      request = translate.CreateAdaptiveMtDatasetRequest(
          parent="projects/PROJECT_ID/locations/LOCATION",
          adaptive_mt_dataset=adaptive_mt_dataset,
      )
      # Make the request
      response = client.create_adaptive_mt_dataset(request=request)
      # Handle the response
      print(response)

  2. After you create a dataset, populate it with example translations from a TSV or TMX file.

You can import data from multiple files into a single dataset. For more information, see the [adaptiveMtDatasets.importAdaptiveMtFile](https://docs.cloud.google.com/translate/docs/reference/rest/v3/projects.locations.adaptiveMtDatasets/importAdaptiveMtFile) method.

### REST

Before using any of the request data, make the following replacements: 

     * PROJECT_NUMBER_OR_ID: the numeric or alphanumeric ID of your Google Cloud project
     * LOCATION: The region where your dataset is located, such as `us-central1`.
     * DATASET_ID: The unique identifier of your dataset where the data is to be imported. 
     * GCS_FILE_PATH: The path to the source data file in Cloud Storage, such as `gs://example/data.tsv`.

HTTP method and URL: 
    
    POST https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION/adaptiveMtDatasets/DATASET_ID:importAdaptiveMtFile

Request JSON body: 
    
    {
      "gcs_input_source": {
        "input_uri": "GCS_FILE_PATH"
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_NUMBER_OR_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION/adaptiveMtDatasets/DATASET_ID:importAdaptiveMtFile"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_NUMBER_OR_ID" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION/adaptiveMtDatasets/DATASET_ID:importAdaptiveMtFile" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    {
      "adaptiveMtFile": {
        "name": "DATASET_NAME",
        "displayName": "FILE_NAME",
        "entryCount": TOTAL_ENTRIES
      }
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    /** Imports an AdaptiveMtFile. */
    private static String importAdaptiveMtFile(
        TranslationServiceClient translationServiceClient,
        String projectId,
        String datasetId,
        String gcsUri) {
      String adaptiveMtDatasetName =
          String.format(
              "projects/%s/locations/LOCATION/adaptiveMtDatasets/%s", projectId, datasetId);
      ImportAdaptiveMtFileRequest importAdaptiveMtFileRequest =
          ImportAdaptiveMtFileRequest.newBuilder()
              .setParent(adaptiveMtDatasetName)
              .setGcsInputSource(GcsInputSource.newBuilder().setInputUri(gcsUri).build())
              .build();
      ImportAdaptiveMtFileResponse response =
          translationServiceClient.importAdaptiveMtFile(importAdaptiveMtFileRequest);
    
      System.out.println("Importing file");
      System.out.println(response);
      return response.getAdaptiveMtFile().getName();
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Node.js API reference documentation](https://googleapis.dev/nodejs/translate/latest/index.html). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    async function importAdaptiveMtFile() {
      const request = {
        parent: `projects/${projectId}/locations/${location}/adaptiveMtDatasets/${
            adaptiveMtDatasetName}`,
        gcsInputSource: {inputUri: gcs_file_uri}
      } const [response] = await translationClient.importAdaptiveMtFile(request)
      console.log('Importing file')
      console.log(response)
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/translate/latest). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    def import_adaptive_mt_file():
      # Create a client
      client = translate.TranslationServiceClient()
      gcs_input_source = translate.GcsInputSource()
      gcs_input_source.input_uri = "gs://SOURCE_LOCATION/FILE.tsv"
      # Initialize the request
      request = translate.ImportAdaptiveMtFileRequest(
          parent="projects/PROJECT_ID/locations/LOCATION/adaptiveMtDatasets/DATASET_ID",
          gcs_input_source=gcs_input_source
      )
      # Make the request
      response = client.import_adaptive_mt_file(request)
      # Handle the response
      print(response)

  3. Request an adaptive translation by providing the source text to translate and the dataset that Cloud Translation uses to customize the translation.

Cloud Translation uses the source and target language from the dataset to determine which languages to use for your translation. For example, an `en` to `es` dataset translates text from English to Spanish. For more information, see the [adaptiveMtTranslate](https://docs.cloud.google.com/translate/docs/reference/rest/v3/projects.locations/adaptiveMtTranslate) method.

### REST

Before using any of the request data, make the following replacements: 

     * PROJECT_NUMBER_OR_ID: the numeric or alphanumeric ID of your Google Cloud project
     * LOCATION: The region where your source dataset is located, such as `us-central1`.
     * DATASET_NAME: The name of the dataset that Cloud Translation uses to customize your translations, formatted as `projects/PROJECT_ID/locations/LOCATION/adaptiveMtDatasets/DATASET_ID`. You can get dataset names by [listing all datasets](https://docs.cloud.google.com/translate/docs/advanced/adaptive-translation-data) in your project.
     * SOURCE_TEXT: The text to translate.
     * MIME_TYPE (Optional): The format of the source text, such as `text/html` or `text/plain`. By default, the MIME type is set to `text/plain`.

HTTP method and URL: 
    
    POST https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION:adaptiveMtTranslate

Request JSON body: 
    
    {
      "dataset": "DATASET_NAME",
      "content": ["SOURCE_TEXT"],
      "mimeType": "MIME_TYPE"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_NUMBER_OR_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION:adaptiveMtTranslate"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_NUMBER_OR_ID" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION:adaptiveMtTranslate" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    {
      "translations": [
        {
          "translatedText": "TRANSLATED_TEXT"
        }
      ],
      "languageCode": "TARGET_LANGUAGE"
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    /** Translates using AdaptiveMt. */
    private static void adaptiveMtTranslate(
        TranslationServiceClient translationServiceClient, String projectId, String datasetId) {
      String adaptiveMtDatasetName =
          String.format(
              "projects/%s/locations/LOCATION/adaptiveMtDatasets/%s", projectId, datasetId);
    
      AdaptiveMtTranslateRequest request =
          AdaptiveMtTranslateRequest.newBuilder()
              .setParent(LocationName.of(projectId, "us-central1").toString())
              .setDataset(adaptiveMtDatasetName)
              .addContent("Sample translation text")
              .build();
      AdaptiveMtTranslateResponse response = translationServiceClient.adaptiveMtTranslate(request);
    
      System.out.println("Translating using AdaptiveMt");
      System.out.println(response);
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Node.js API reference documentation](https://googleapis.dev/nodejs/translate/latest/index.html). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    async function translate() {
      const request = {
        parent: `projects/${projectId}/locations/${location}`,
        dataset: `projects/${projectId}/locations/${location}/adaptiveMtDatasets/${
            adaptiveMtDatasetName}`,
        content: ['Sample translate query']
      } const [response] = await translationClient.adaptiveMtTranslate(request)
      console.log('Translating')
      console.log(response)
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/translate/latest). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    def adaptive_mt_translate():
      # Create a client
      client = translate.TranslationServiceClient()
      # Initialize the request
      request = translate.AdaptiveMtTranslateRequest(
          parent="projects/PROJECT_ID/locations/LOCATION",
          dataset="projects/PROJECT_ID/locations/LOCATION/adaptiveMtDatasets/DATASET_ID",
          content=["Sample translation request"]
      )
      # Make the request
      response = client.adaptive_mt_translate(request)
      # Handle the response
      print(response)




## What's next

  * [Use a glossary with adaptive translations](https://docs.cloud.google.com/translate/docs/advanced/glossary#dataset)
  * [Manage datasets](https://docs.cloud.google.com/translate/docs/advanced/adaptive-translation-data) (API only)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
