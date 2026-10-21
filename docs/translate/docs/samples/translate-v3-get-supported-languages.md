---
url: https://docs.cloud.google.com/translate/docs/samples/translate-v3-get-supported-languages/
title: Get supported languages (Advanced edition) \u00a0|\u00a0 Cloud Translation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:09.990490+00:00
---

# Get supported languages (Advanced edition)  |  Cloud Translation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/translate/docs/samples/translate-v3-get-supported-languages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Translation ](https://docs.cloud.google.com/translate/docs)
  * [ Samples ](https://docs.cloud.google.com/translate/docs/samples)



#  Get supported languages (Advanced edition) Stay organized with collections  Save and categorize content based on your preferences. 

Retrieve a list of supported language codes.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [List Supported languages](https://docs.cloud.google.com/translate/docs/list-supported-languages)



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
    
    // getSupportedLanguages gets a list of supported language codes.
    func getSupportedLanguages(w io.Writer, projectID string) error {
    	// projectID := "my-project-id"
    
    	ctx := context.Background()
    	client, err := translate.[NewTranslationClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/apiv3.html#cloud_google_com_go_translate_apiv3_TranslationClient_NewTranslationClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewTranslationClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/apiv3.html#cloud_google_com_go_translate_apiv3_TranslationClient_Close)()
    
    	req := &translatepb.GetSupportedLanguagesRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/global", projectID),
    	}
    
    	resp, err := client.GetSupportedLanguages(ctx, req)
    	if err != nil {
    		return fmt.Errorf("GetSupportedLanguages: %w", err)
    	}
    
    	// List language codes of supported languages
    	fmt.Fprintf(w, "Supported languages:\n")
    	for _, language := range resp.GetLanguages() {
    		fmt.Fprintf(w, "Language code: %v\n", language.GetLanguageCode())
    	}
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.translate.v3.[GetSupportedLanguagesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GetSupportedLanguagesRequest.html);
    import com.google.cloud.translate.v3.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html);
    import com.google.cloud.translate.v3.[SupportedLanguage](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.SupportedLanguage.html);
    import com.google.cloud.translate.v3.[SupportedLanguages](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.SupportedLanguages.html);
    import com.google.cloud.translate.v3.[TranslationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html);
    import java.io.IOException;
    
    public class GetSupportedLanguages {
    
      public static void getSupportedLanguages() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "YOUR-PROJECT-ID";
        getSupportedLanguages(projectId);
      }
    
      // Getting a list of supported language codes
      public static void getSupportedLanguages(String projectId) throws IOException {
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([TranslationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html) client = [TranslationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html).create()) {
          // Supported Locations: `global`, [glossary location], or [model location]
          // Glossaries must be hosted in `us-central1`
          // Custom Models must use the same location as your model. (us-central1)
          [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html) parent = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html).of(projectId, "global");
          [GetSupportedLanguagesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GetSupportedLanguagesRequest.html) request =
              [GetSupportedLanguagesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GetSupportedLanguagesRequest.html).newBuilder().setParent(parent.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html#com_google_cloud_translate_v3_LocationName_toString__)()).build();
    
          [SupportedLanguages](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.SupportedLanguages.html) response = client.getSupportedLanguages(request);
    
          // List language codes of supported languages
          for ([SupportedLanguage](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.SupportedLanguage.html) language : response.[getLanguagesList](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.SupportedLanguages.html#com_google_cloud_translate_v3_SupportedLanguages_getLanguagesList__)()) {
            System.out.printf("Language Code: %s\n", language.getLanguageCode());
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
    
    // Imports the Google Cloud Translation library
    const {TranslationServiceClient} = require('[@google-cloud/translate](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/overview.html)');
    
    // Instantiates a client
    const translationClient = new [TranslationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/overview.html)();
    
    async function getSupportedLanguages() {
      // Construct request
      const request = {
        parent: `projects/${projectId}/locations/${location}`,
      };
    
      // Get supported languages
      const [response] = await translationClient.getSupportedLanguages(request);
    
      for (const language of response.languages) {
        // Supported language code, generally consisting of its ISO 639-1 identifier, for
        // example, 'en', 'ja'. In certain cases, BCP-47 codes including language and
        // region identifiers are returned (for example, 'zh-TW' and 'zh-CN')
        console.log(`Language - Language Code: ${[language](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/translate/v2.detectresult.html).languageCode}`);
        // Human readable name of the language localized in the display language specified
        // in the request.
        console.log(`Language - Display Name: ${[language](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/translate/v2.detectresult.html).displayName}`);
        // Can be used as source language.
        console.log(`Language - Support Source: ${[language](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/translate/v2.detectresult.html).supportSource}`);
        // Can be used as target language.
        console.log(`Language - Support Target: ${[language](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/translate/v2.detectresult.html).supportTarget}`);
      }
    }
    
    getSupportedLanguages();

### PHP

Before trying this sample, follow the PHP setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/translate/v2/translateclient). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Translate\V3\Client\TranslationServiceClient;
    use Google\Cloud\Translate\V3\GetSupportedLanguagesRequest;
    
    /**
     * @param string $projectId Your Google Cloud project ID.
     */
    function v3_get_supported_languages(string $projectId): void
    {
        $translationServiceClient = new TranslationServiceClient();
    
        $formattedParent = $translationServiceClient->locationName($projectId, 'global');
    
        try {
            $request = (new GetSupportedLanguagesRequest())
                ->setParent($formattedParent);
            $response = $translationServiceClient->getSupportedLanguages($request);
            // List language codes of supported languages
            foreach ($response->getLanguages() as $language) {
                printf('Language Code: %s' . PHP_EOL, $language->getLanguageCode());
            }
        } finally {
            $translationServiceClient->close();
        }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/translate/latest). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [translate](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.Client.html)
    
    
    def get_supported_languages(
        project_id: str = "YOUR_PROJECT_ID",
    ) -> translate.SupportedLanguages:
        """Getting a list of supported language codes.
    
        Args:
            project_id: The GCP project ID.
    
        Returns:
            A list of supported language codes.
        """
        client = [translate](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.Client.html).[TranslationServiceClient](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3.services.translation_service.TranslationServiceClient.html)()
    
        parent = f"projects/{project_id}"
    
        # Supported language codes: https://cloud.google.com/translate/docs/languages
        response = [client](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.html).[get_supported_languages](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3.services.translation_service.TranslationServiceClient.html#google_cloud_translate_v3_services_translation_service_TranslationServiceClient_get_supported_languages)(parent=parent)
    
        # List language codes of supported languages.
        print("Supported Languages:")
        for language in response.languages:
            print(f"Language Code: {language.language_code}")
    
        return response
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudtranslation). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
