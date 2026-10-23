---
url: https://docs.cloud.google.com/translate/docs/samples/translate-v3-translate-text/
title: Translate text (Advanced edition) \u00a0|\u00a0 Cloud Translation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:29.637153+00:00
---

# Translate text (Advanced edition)  |  Cloud Translation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/translate/docs/samples/translate-v3-translate-text/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Translation ](https://docs.cloud.google.com/translate/docs)
  * [ Samples ](https://docs.cloud.google.com/translate/docs/samples)



#  Translate text (Advanced edition) Stay organized with collections  Save and categorize content based on your preferences. 

Translate input text by using Cloud Translation - Advanced (v3).

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Cloud Translation client libraries](https://docs.cloud.google.com/translate/docs/reference/libraries/v3/overview-v3)
  * [Translate text](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/translate/translate-text)
  * [Translate text with Cloud Translation](https://docs.cloud.google.com/translate/docs/translate-text)



## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Go API reference documentation](https://godoc.org/cloud.google.com/go/translate). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud Translation library
    import (
    	"context"
    	"fmt"
    	"io"
    
    	translate "cloud.google.com/go/translate/apiv3"
    	"cloud.google.com/go/translate/apiv3/translatepb"
    )
    
    func translateText(w io.Writer, projectID string, sourceLang string, targetLang string, text string) error {
    	// projectID := "your-project-id"
    	// sourceLang := "en-US"
    	// targetLang := "fr"
    	// text := "Text you wish to translate"
    
    	// Instantiates a client
    	ctx := context.Background()
    	client, err := translate.[NewTranslationClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/apiv3.html#cloud_google_com_go_translate_apiv3_TranslationClient_NewTranslationClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewTranslationClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/apiv3.html#cloud_google_com_go_translate_apiv3_TranslationClient_Close)()
    
    	// Construct request
    	req := &translatepb.TranslateTextRequest{
    		Parent:             fmt.Sprintf("projects/%s/locations/global", projectID),
    		SourceLanguageCode: sourceLang,
    		TargetLanguageCode: targetLang,
    		MimeType:           "text/plain", // Mime types: "text/plain", "text/html"
    		Contents:           []string{text},
    	}
    
    	resp, err := client.TranslateText(ctx, req)
    	if err != nil {
    		return fmt.Errorf("TranslateText: %w", err)
    	}
    
    	// Display the translation for each input text provided
    	for _, translation := range resp.GetTranslations() {
    		fmt.Fprintf(w, "Translated text: %v\n", translation.GetTranslatedText())
    	}
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud Translation library.
    import com.google.cloud.translate.v3.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html);
    import com.google.cloud.translate.v3.[TranslateTextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslateTextRequest.html);
    import com.google.cloud.translate.v3.[TranslateTextResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslateTextResponse.html);
    import com.google.cloud.translate.v3.[Translation](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.Translation.html);
    import com.google.cloud.translate.v3.[TranslationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html);
    import java.io.IOException;
    
    
    public class TranslateText {
    
      // Set and pass variables to overloaded translateText() method for translation.
      public static void translateText() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "YOUR-PROJECT-ID";
        // Supported Languages: https://cloud.google.com/translate/docs/languages
        String targetLanguage = "your-target-language";
        String text = "your-text";
        translateText(projectId, targetLanguage, text);
      }
    
      // Translate text to target language.
      public static void translateText(String projectId, String targetLanguage, String text)
          throws IOException {
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([TranslationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html) client = [TranslationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html).create()) {
          // Supported Locations: `global`, [glossary location], or [model location]
          // Glossaries must be hosted in `us-central1`
          // Custom Models must use the same location as your model. (us-central1)
          [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html) parent = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html).of(projectId, "global");
    
          // Supported Mime Types: https://cloud.google.com/translate/docs/supported-formats
          [TranslateTextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslateTextRequest.html) request =
              [TranslateTextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslateTextRequest.html).newBuilder()
                  .setParent(parent.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html#com_google_cloud_translate_v3_LocationName_toString__)())
                  .setMimeType("text/plain")
                  .setTargetLanguageCode(targetLanguage)
                  .addContents(text)
                  .build();
    
          [TranslateTextResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslateTextResponse.html) response = client.translateText(request);
    
          // Display the translation for each input text provided
          for ([Translation](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.Translation.html) translation : response.[getTranslationsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslateTextResponse.html#com_google_cloud_translate_v3_TranslateTextResponse_getTranslationsList__)()) {
            System.out.printf("Translated text: %s\n", translation.getTranslatedText());
          }
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Node.js API reference documentation](https://googleapis.dev/nodejs/translate/latest/index.html). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const location = 'global';
    // const text = 'text to translate';
    
    // Imports the Google Cloud Translation library
    const {TranslationServiceClient} = require('[@google-cloud/translate](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/overview.html)');
    
    // Instantiates a client
    const translationClient = new [TranslationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/overview.html)();
    
    async function translateText() {
      // MIME type of the content to translate
      // Supported MIME types:
      // https://cloud.google.com/translate/docs/supported-formats
      const mimeType = 'text/plain';
    
      // Construct request
      const request = {
        parent: `projects/${projectId}/locations/${location}`,
        contents: [text],
        mimeType: mimeType,
        sourceLanguageCode: 'en',
        targetLanguageCode: 'sr-Latn',
      };
    
      // Run request
      const [response] = await translationClient.translateText(request);
    
      for (const translation of response.translations) {
        console.log(`Translation: ${translation.translatedText}`);
      }
    }
    
    translateText();

### PHP

Before trying this sample, follow the PHP setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/translate/v2/translateclient). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Translate\V3\Client\TranslationServiceClient;
    use Google\Cloud\Translate\V3\TranslateTextRequest;
    
    /**
     * @param string $text           The text to translate.
     * @param string $targetLanguage Language to translate to.
     * @param string $projectId      Your Google Cloud project ID.
     */
    function v3_translate_text(
        string $text,
        string $targetLanguage,
        string $projectId
    ): void {
        $translationServiceClient = new TranslationServiceClient();
    
        $contents = [$text];
        $formattedParent = $translationServiceClient->locationName($projectId, 'global');
    
        try {
            $request = (new TranslateTextRequest())
                ->setContents($contents)
                ->setTargetLanguageCode($targetLanguage)
                ->setParent($formattedParent);
            $response = $translationServiceClient->translateText($request);
    
            // Display the translation for each input text provided
            foreach ($response->getTranslations() as $translation) {
                printf('Translated text: %s' . PHP_EOL, $translation->getTranslatedText());
            }
        } finally {
            $translationServiceClient->close();
        }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/translate/latest). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import os
    
    # Import the Google Cloud Translation library.
    from google.cloud import [translate](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.Client.html)_v3
    
    PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT")
    
    
    def translate_text(
        text: str = "YOUR_TEXT_TO_TRANSLATE",
        source_language_code: str = "en-US",
        target_language_code: str = "fr",
    ) -> translate_v3.TranslationServiceClient:
        """Translate Text from a Source language to a Target language.
        Args:
            text: The content to translate.
            source_language_code: The code of the source language.
            target_language_code: The code of the target language.
                For example: "fr" for French, "es" for Spanish, etc.
                Find available languages and codes here:
                https://cloud.google.com/translate/docs/languages#neural_machine_translation_model
        """
    
        # Initialize Translation client.
        client = translate_v3.[TranslationServiceClient](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3.services.translation_service.TranslationServiceClient.html)()
        parent = f"projects/{PROJECT_ID}/locations/global"
    
        # MIME type of the content to translate.
        # Supported MIME types:
        # https://cloud.google.com/translate/docs/supported-formats
        mime_type = "text/plain"
    
        # Translate text from the source to the target language.
        response = [client](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.html).[translate_text](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3.services.translation_service.TranslationServiceClient.html#google_cloud_translate_v3_services_translation_service_TranslationServiceClient_translate_text)(
            contents=[text],
            parent=parent,
            mime_type=mime_type,
            source_language_code=source_language_code,
            target_language_code=target_language_code,
        )
    
        # Display the translation for the text.
        # For example, for "Hello! How are you doing today?":
        # Translated text: Bonjour comment vas-tu aujourd'hui?
        for translation in response.translations:
            print(f"Translated text: {translation.translated_text}")
    
        return response

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudtranslation). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
