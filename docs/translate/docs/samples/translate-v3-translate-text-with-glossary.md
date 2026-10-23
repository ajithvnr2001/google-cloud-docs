---
url: https://docs.cloud.google.com/translate/docs/samples/translate-v3-translate-text-with-glossary/
title: Translate text with a glossary (Advanced edition only) \u00a0|\u00a0 Cloud Translation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:43.639448+00:00
---

# Translate text with a glossary (Advanced edition only)  |  Cloud Translation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/translate/docs/samples/translate-v3-translate-text-with-glossary/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Translation ](https://docs.cloud.google.com/translate/docs)
  * [ Samples ](https://docs.cloud.google.com/translate/docs/samples)



#  Translate text with a glossary (Advanced edition only) Stay organized with collections  Save and categorize content based on your preferences. 

Translate input text with a glossary.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Creating and using glossaries (Advanced)](https://docs.cloud.google.com/translate/docs/advanced/glossary)



## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Go API reference documentation](https://godoc.org/cloud.google.com/go/translate). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	translate "cloud.google.com/go/translate/apiv3"
    	"cloud.google.com/go/translate/apiv3/translatepb"
    )
    
    // translateTextWithGlossary translates input text and returns translated text.
    func translateTextWithGlossary(w io.Writer, projectID string, location string, sourceLang string, targetLang string, text string, glossaryID string) error {
    	// projectID := "my-project-id"
    	// location := "us-central1"
    	// sourceLang := "en"
    	// targetLang := "ja"
    	// text := "Hello world"
    	// glossaryID := "your-glossary-id"
    
    	ctx := context.Background()
    	client, err := translate.[NewTranslationClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/apiv3.html#cloud_google_com_go_translate_apiv3_TranslationClient_NewTranslationClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewTranslationClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/apiv3.html#cloud_google_com_go_translate_apiv3_TranslationClient_Close)()
    
    	req := &translatepb.TranslateTextRequest{
    		Parent:             fmt.Sprintf("projects/%s/locations/%s", projectID, location),
    		SourceLanguageCode: sourceLang,
    		TargetLanguageCode: targetLang,
    		MimeType:           "text/plain", // Mime types: "text/plain", "text/html"
    		Contents:           []string{text},
    		GlossaryConfig: &translatepb.TranslateTextGlossaryConfig{
    			Glossary: fmt.Sprintf("projects/%s/locations/%s/glossaries/%s", projectID, location, glossaryID),
    		},
    	}
    
    	resp, err := client.TranslateText(ctx, req)
    	if err != nil {
    		return fmt.Errorf("TranslateText: %w", err)
    	}
    
    	// Display the translation for each input text provided
    	for _, translation := range resp.GetGlossaryTranslations() {
    		fmt.Fprintf(w, "Translated text: %v\n", translation.GetTranslatedText())
    	}
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.translate.v3.[GlossaryName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GlossaryName.html);
    import com.google.cloud.translate.v3.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html);
    import com.google.cloud.translate.v3.[TranslateTextGlossaryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslateTextGlossaryConfig.html);
    import com.google.cloud.translate.v3.[TranslateTextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslateTextRequest.html);
    import com.google.cloud.translate.v3.[TranslateTextResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslateTextResponse.html);
    import com.google.cloud.translate.v3.[Translation](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.Translation.html);
    import com.google.cloud.translate.v3.[TranslationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html);
    import java.io.IOException;
    
    public class TranslateTextWithGlossary {
    
      public static void translateTextWithGlossary() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "YOUR-PROJECT-ID";
        // Supported Languages: https://cloud.google.com/translate/docs/languages
        String sourceLanguage = "your-source-language";
        String targetLanguage = "your-target-language";
        String text = "your-text";
        String glossaryId = "your-glossary-display-name";
        translateTextWithGlossary(projectId, sourceLanguage, targetLanguage, text, glossaryId);
      }
    
      // Translates a given text using a glossary.
      public static void translateTextWithGlossary(
          String projectId,
          String sourceLanguage,
          String targetLanguage,
          String text,
          String glossaryId)
          throws IOException {
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([TranslationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html) client = [TranslationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html).create()) {
          // Supported Locations: `global`, [glossary location], or [model location]
          // Glossaries must be hosted in `us-central1`
          // Custom Models must use the same location as your model. (us-central1)
          String location = "us-central1";
          [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html) parent = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html).of(projectId, location);
    
          [GlossaryName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GlossaryName.html) glossaryName = [GlossaryName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GlossaryName.html).of(projectId, location, glossaryId);
          [TranslateTextGlossaryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslateTextGlossaryConfig.html) glossaryConfig =
              [TranslateTextGlossaryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslateTextGlossaryConfig.html).newBuilder().setGlossary(glossaryName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GlossaryName.html#com_google_cloud_translate_v3_GlossaryName_toString__)()).build();
    
          // Supported Mime Types: https://cloud.google.com/translate/docs/supported-formats
          [TranslateTextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslateTextRequest.html) request =
              [TranslateTextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslateTextRequest.html).newBuilder()
                  .setParent(parent.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html#com_google_cloud_translate_v3_LocationName_toString__)())
                  .setMimeType("text/plain")
                  .setSourceLanguageCode(sourceLanguage)
                  .setTargetLanguageCode(targetLanguage)
                  .addContents(text)
                  .setGlossaryConfig(glossaryConfig)
                  .build();
    
          [TranslateTextResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslateTextResponse.html) response = client.translateText(request);
    
          // Display the translation for each input text provided
          for ([Translation](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.Translation.html) translation : response.[getGlossaryTranslationsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslateTextResponse.html#com_google_cloud_translate_v3_TranslateTextResponse_getGlossaryTranslationsList__)()) {
            System.out.printf("Translated text: %s\n", translation.getTranslatedText());
          }
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Node.js API reference documentation](https://googleapis.dev/nodejs/translate/latest/index.html). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const location = 'global';
    // const glossaryId = 'YOUR_GLOSSARY_ID';
    // const text = 'text to translate';
    
    // Imports the Google Cloud Translation library
    const {TranslationServiceClient} = require('[@google-cloud/translate](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/overview.html)');
    
    // Instantiates a client
    const translationClient = new [TranslationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/overview.html)();
    async function translateTextWithGlossary() {
      const glossaryConfig = {
        glossary: `projects/${projectId}/locations/${location}/glossaries/${glossaryId}`,
      };
      // Construct request
      const request = {
        parent: `projects/${projectId}/locations/${location}`,
        contents: [text],
        mimeType: 'text/plain', // mime types: text/plain, text/html
        sourceLanguageCode: 'en',
        targetLanguageCode: 'es',
        glossaryConfig: glossaryConfig,
      };
    
      // Run request
      const [response] = await translationClient.translateText(request);
    
      for (const translation of response.glossaryTranslations) {
        console.log(`Translation: ${translation.translatedText}`);
      }
    }
    
    translateTextWithGlossary();

### PHP

Before trying this sample, follow the PHP setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/translate/v2/translateclient). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Translate\V3\Client\TranslationServiceClient;
    use Google\Cloud\Translate\V3\TranslateTextGlossaryConfig;
    use Google\Cloud\Translate\V3\TranslateTextRequest;
    
    /**
     * @param string $text          The text to translate.
     * @param string $targetLanguage    Language to translate to.
     * @param string $sourceLanguage    Language of the source.
     * @param string $projectId     Your Google Cloud project ID.
     * @param string $glossaryId    Your glossary ID.
     */
    function v3_translate_text_with_glossary(
        string $text,
        string $targetLanguage,
        string $sourceLanguage,
        string $projectId,
        string $glossaryId
    ): void {
        $translationServiceClient = new TranslationServiceClient();
    
        $glossaryPath = $translationServiceClient->glossaryName(
            $projectId,
            'us-central1',
            $glossaryId
        );
        $contents = [$text];
        $formattedParent = $translationServiceClient->locationName(
            $projectId,
            'us-central1'
        );
        $glossaryConfig = new TranslateTextGlossaryConfig();
        $glossaryConfig->setGlossary($glossaryPath);
    
        // Optional. Can be "text/plain" or "text/html".
        $mimeType = 'text/plain';
    
        try {
            $request = (new TranslateTextRequest())
                ->setContents($contents)
                ->setTargetLanguageCode($targetLanguage)
                ->setParent($formattedParent)
                ->setSourceLanguageCode($sourceLanguage)
                ->setGlossaryConfig($glossaryConfig)
                ->setMimeType($mimeType);
            $response = $translationServiceClient->translateText($request);
            // Display the translation for each input text provided
            foreach ($response->getGlossaryTranslations() as $translation) {
                printf('Translated text: %s' . PHP_EOL, $translation->getTranslatedText());
            }
        } finally {
            $translationServiceClient->close();
        }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/translate/latest). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [translate](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.Client.html)
    
    
    def translate_text_with_glossary(
        text: str = "YOUR_TEXT_TO_TRANSLATE",
        project_id: str = "YOUR_PROJECT_ID",
        glossary_id: str = "YOUR_GLOSSARY_ID",
    ) -> translate.TranslateTextResponse:
        """Translates a given text using a glossary.
    
        Args:
            text: The text to translate.
            project_id: The ID of the GCP project that owns the glossary.
            glossary_id: The ID of the glossary to use.
    
        Returns:
            The translated text."""
        client = [translate](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.Client.html).[TranslationServiceClient](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3.services.translation_service.TranslationServiceClient.html)()
        location = "us-central1"
        parent = f"projects/{project_id}/locations/{location}"
    
        glossary = [client](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.html).[glossary_path](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3.services.translation_service.TranslationServiceClient.html#google_cloud_translate_v3_services_translation_service_TranslationServiceClient_glossary_path)(
            project_id, "us-central1", glossary_id  # The location of the glossary
        )
    
        glossary_config = [translate](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.Client.html).[TranslateTextGlossaryConfig](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3.types.TranslateTextGlossaryConfig.html)(glossary=glossary)
    
        # Supported language codes: https://cloud.google.com/translate/docs/languages
        response = [client](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.html).[translate_text](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3.services.translation_service.TranslationServiceClient.html#google_cloud_translate_v3_services_translation_service_TranslationServiceClient_translate_text)(
            request={
                "contents": [text],
                "target_language_code": "ja",
                "source_language_code": "en",
                "parent": parent,
                "glossary_config": glossary_config,
            }
        )
    
        print("Translated text: \n")
        for translation in response.glossary_translations:
            print(f"\t {translation.translated_text}")
    
        return response
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudtranslation). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
