---
url: https://docs.cloud.google.com/translate/docs/samples/translate-v3-detect-language/
title: Detect the language (Advanced edition) \u00a0|\u00a0 Cloud Translation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:21.664436+00:00
---

# Detect the language (Advanced edition)  |  Cloud Translation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/translate/docs/samples/translate-v3-detect-language/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Translation ](https://docs.cloud.google.com/translate/docs)
  * [ Samples ](https://docs.cloud.google.com/translate/docs/samples)



#  Detect the language (Advanced edition) Stay organized with collections  Save and categorize content based on your preferences. 

Detect the language of a text string.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Detecting languages](https://docs.cloud.google.com/translate/docs/detect-language)



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
    
    // detectLanguage detects the language of a text string.
    func detectLanguage(w io.Writer, projectID string, text string) error {
    	// projectID := "my-project-id"
    	// text := "Hello, world!"
    
    	ctx := context.Background()
    	client, err := translate.[NewTranslationClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/apiv3.html#cloud_google_com_go_translate_apiv3_TranslationClient_NewTranslationClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewTranslationClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/apiv3.html#cloud_google_com_go_translate_apiv3_TranslationClient_Close)()
    
    	req := &translatepb.DetectLanguageRequest{
    		Parent:   fmt.Sprintf("projects/%s/locations/global", projectID),
    		MimeType: "text/plain", // Mime types: "text/plain", "text/html"
    		Source: &translatepb.DetectLanguageRequest_Content{
    			Content: text,
    		},
    	}
    
    	resp, err := client.DetectLanguage(ctx, req)
    	if err != nil {
    		return fmt.Errorf("DetectLanguage: %w", err)
    	}
    
    	// Display list of detected languages sorted by detection confidence.
    	// The most probable language is first.
    	for _, language := range resp.GetLanguages() {
    		// The language detected.
    		fmt.Fprintf(w, "Language code: %v\n", language.GetLanguageCode())
    		// Confidence of detection result for this language.
    		fmt.Fprintf(w, "Confidence: %v\n", language.GetConfidence())
    	}
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.translate.v3.[DetectLanguageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.DetectLanguageRequest.html);
    import com.google.cloud.translate.v3.[DetectLanguageResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.DetectLanguageResponse.html);
    import com.google.cloud.translate.v3.[DetectedLanguage](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.DetectedLanguage.html);
    import com.google.cloud.translate.v3.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html);
    import com.google.cloud.translate.v3.[TranslationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html);
    import java.io.IOException;
    
    public class DetectLanguage {
    
      public static void detectLanguage() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "YOUR-PROJECT-ID";
        String text = "your-text";
    
        detectLanguage(projectId, text);
      }
    
      // Detecting the language of a text string
      public static void detectLanguage(String projectId, String text) throws IOException {
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([TranslationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html) client = [TranslationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html).create()) {
          // Supported Locations: `global`, [glossary location], or [model location]
          // Glossaries must be hosted in `us-central1`
          // Custom Models must use the same location as your model. (us-central1)
          [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html) parent = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html).of(projectId, "global");
    
          // Supported Mime Types: https://cloud.google.com/translate/docs/supported-formats
          [DetectLanguageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.DetectLanguageRequest.html) request =
              [DetectLanguageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.DetectLanguageRequest.html).newBuilder()
                  .setParent(parent.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html#com_google_cloud_translate_v3_LocationName_toString__)())
                  .setMimeType("text/plain")
                  .setContent(text)
                  .build();
    
          [DetectLanguageResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.DetectLanguageResponse.html) response = client.detectLanguage(request);
    
          // Display list of detected languages sorted by detection confidence.
          // The most probable language is first.
          for ([DetectedLanguage](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.DetectedLanguage.html) language : response.[getLanguagesList](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.DetectLanguageResponse.html#com_google_cloud_translate_v3_DetectLanguageResponse_getLanguagesList__)()) {
            // The language detected
            System.out.printf("Language code: %s\n", language.getLanguageCode());
            // Confidence of detection result for this language
            System.out.printf("Confidence: %s\n", language.getConfidence());
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
    // const text = 'text to translate';
    
    // Imports the Google Cloud Translation library
    const {TranslationServiceClient} = require('[@google-cloud/translate](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/overview.html)');
    
    // Instantiates a client
    const translationClient = new [TranslationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/overview.html)();
    
    async function detectLanguage() {
      // Construct request
      const request = {
        parent: `projects/${projectId}/locations/${location}`,
        content: text,
      };
    
      // Run request
      const [response] = await translationClient.detectLanguage(request);
    
      console.log('Detected Languages:');
      for (const language of response.languages) {
        console.log(`Language Code: ${[language](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/translate/v2.detectresult.html).languageCode}`);
        console.log(`Confidence: ${[language](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/translate/v2.detectresult.html).confidence}`);
      }
    }
    
    detectLanguage();

### PHP

Before trying this sample, follow the PHP setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/translate/v2/translateclient). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Translate\V3\Client\TranslationServiceClient;
    use Google\Cloud\Translate\V3\DetectLanguageRequest;
    
    /**
     * @param string $text      The text whose language to detect.  This will be detected as en.
     * @param string $projectId Your Google Cloud project ID.
     */
    function v3_detect_language(string $text, string $projectId): void
    {
        $translationServiceClient = new TranslationServiceClient();
    
        /** Uncomment and populate these variables in your code */
        // $text = 'Hello, world!';
        // $projectId = '[Google Cloud Project ID]';
        $formattedParent = $translationServiceClient->locationName($projectId, 'global');
    
        // Optional. Can be "text/plain" or "text/html".
        $mimeType = 'text/plain';
    
        try {
            $request = (new DetectLanguageRequest())
                ->setParent($formattedParent)
                ->setContent($text)
                ->setMimeType($mimeType);
            $response = $translationServiceClient->detectLanguage($request);
            // Display list of detected languages sorted by detection confidence.
            // The most probable language is first.
            foreach ($response->getLanguages() as $language) {
                // The language detected
                printf('Language code: %s' . PHP_EOL, $language->getLanguageCode());
                // Confidence of detection result for this language
                printf('Confidence: %s' . PHP_EOL, $language->getConfidence());
            }
        } finally {
            $translationServiceClient->close();
        }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/translate/latest). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import translate
    
    
    def detect_language(
        project_id: str = "YOUR_PROJECT_ID",
    ) -> translate.DetectLanguageResponse:
        """Detecting the language of a text string.
    
        Args:
            project_id: The GCP project ID.
    
        Returns:
            The detected language of the text.
        """
        client = translate.TranslationServiceClient()
    
        location = "global"
    
        parent = f"projects/{project_id}/locations/{location}"
    
        # Detail on supported types can be found here:
        # https://cloud.google.com/translate/docs/supported-formats
        response = client.detect_language(
            content="Hello, world!",
            parent=parent,
            mime_type="text/plain",  # mime types: text/plain, text/html
        )
    
        # Display list of detected languages sorted by detection confidence.
        # The most probable language is first.
        for language in response.languages:
            # The language detected
            print(f"Language code: {language.language_code}")
            # Confidence of detection result for this language
            print(f"Confidence: {language.confidence}")
    
        return response
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudtranslation). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
