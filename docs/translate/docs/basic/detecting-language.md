---
url: https://docs.cloud.google.com/translate/docs/basic/detecting-language/
title: Detecting languages \u00a0|\u00a0 Cloud Translation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:39:59.353159+00:00
---

# Detecting languages  |  Cloud Translation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/translate/docs/basic/detecting-language/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Translation ](https://docs.cloud.google.com/translate/docs)
  * [ Guides ](https://docs.cloud.google.com/translate/docs/overview)



Send feedback 

#  Detecting languages Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to detect the language of input text with both the Basic and Advanced editions of Cloud Translation.

## Before you begin

Before you can start using the Cloud Translation API, you should complete the [Cloud Translation setup](https://docs.cloud.google.com/translate/docs/setup) page, which includes creating a project, enabling the Cloud Translation API, and setting up authentication. The setup page also provides instructions for installing client libraries for common programming languages, which is optional.

Choose your preferred API version:

Advanced Basic

* * *

## Detecting the language of a text string

You can detect the language of a text string by sending an HTTP request using a URL of the following format:
    
    
    https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/global:detectLanguage

**Note:** project-id works as well, but project-number is preferred going forward.

### Detecting the language of a single string

### REST

To detect the language of some text, make a `POST` request and provide the appropriate request body. The following shows an example of a `POST` request using `curl` and PowerShell. The example uses the access token for a service account set up for the project using the Google Cloud [Google Cloud CLI](https://cloud.google.com/sdk/). For instructions on installing the Google Cloud CLI, setting up a project with a service account, and obtaining an access token, see the [Setup](https://docs.cloud.google.com/translate/docs/setup) page.

Before using any of the request data, make the following replacements: 

  * PROJECT_NUMBER_OR_ID: the numeric or alphanumeric ID of your Google Cloud project



HTTP method and URL: 
    
    
    POST https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/global:detectLanguage

Request JSON body: 
    
    
    {
       "content":"Доктор Ватсон, иди сюда!"
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
         "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/global:detectLanguage"

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
        -Uri "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/global:detectLanguage" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "languages": [
        {
          "languageCode": "ru",
          "confidence": 1
        }
      ]
    }
    

In the response, `languageCode` provides the language code of the language detected. `confidence` is a range from 0 to 1. 1 is 100% confident. 

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
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.Translate.V3/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-translate/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-translate/latest/Google/Cloud/Translate.html)

## Resources and further reading

  * To start using the API, get [set up](https://docs.cloud.google.com/translate/docs/setup) and then try the [quickstart guide](https://docs.cloud.google.com/translate/docs/translate-text).
  * [Compare supported models](https://docs.cloud.google.com/translate/compare-models)
  * [Customize the NMT model](https://docs.cloud.google.com/translate/docs/advanced/automl-beginner)
  * [Customize the Translation LLM](https://docs.cloud.google.com/translate/docs/advanced/custom-translations)
  * [Supported languages](https://docs.cloud.google.com/translate/docs/languages)
  * [Supported formats](https://docs.cloud.google.com/translate/docs/supported-formats)
  * [Perform adaptive translation](https://docs.cloud.google.com/translate/adaptive-translation)
  * [Migrate to Translation Advanced](https://docs.cloud.google.com/translate/migrate-to-v3)
  * For answers to general questions about Cloud Translation, refer to the [General FAQs](https://docs.cloud.google.com/translate/faq) page.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
