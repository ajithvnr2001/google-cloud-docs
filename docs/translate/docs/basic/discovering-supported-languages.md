---
url: https://docs.cloud.google.com/translate/docs/basic/discovering-supported-languages/
title: List Supported languages \u00a0|\u00a0 Cloud Translation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:09:37.162943+00:00
---

# List Supported languages  |  Cloud Translation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/translate/docs/basic/discovering-supported-languages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Translation ](https://docs.cloud.google.com/translate/docs)
  * [ Guides ](https://docs.cloud.google.com/translate/docs/overview)



Send feedback 

#  List Supported languages Stay organized with collections  Save and categorize content based on your preferences. 

This guide describes how to use your preferred version of the Cloud Translation API to list [supported languages](https://docs.cloud.google.com/translate/docs/languages).

## Before you begin

Before you can start using the Cloud Translation API, you should complete the [Cloud Translation setup](https://docs.cloud.google.com/translate/docs/setup) page, which includes creating a project, enabling the Cloud Translation API, and setting up authentication. The setup page also provides instructions for installing client libraries for common programming languages, which is optional.

Choose your preferred API version:

Advanced Basic

* * *

## List supported languages {:id="supported-languages"}

### REST

To get a list of all supported languages, make a `GET` request to the `https://translation.googleapis.com/v3/projects/project-number-or-id/locations/location/supportedLanguages` URL. The following shows an example of a `GET` request using `curl` and PowerShell. The example uses the access token for a service account set up for the project using the Google Cloud [Google Cloud CLI](https://cloud.google.com/sdk/). For instructions on installing the Google Cloud CLI, setting up a project with a service account, and obtaining an access token, see the [Setup](https://docs.cloud.google.com/translate/docs/setup) page.

Before using any of the request data, make the following replacements: 

  * PROJECT_NUMBER_OR_ID: the numeric or alphanumeric ID of your Google Cloud project



HTTP method and URL: 
    
    
    GET https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/global/supportedLanguages

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_NUMBER_OR_ID" \  
         "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/global/supportedLanguages"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_NUMBER_OR_ID" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/global/supportedLanguages" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "languages": [
         "languageCode": "af",
          "supportSource": true,
          "supportTarget": true
        },
        {
          "languageCode": "am",
          "supportSource": true,
          "supportTarget": true
        },
        {
          "languageCode": "ar",
          "supportSource": true,
          "supportTarget": true
        },
        ....
        {
          "languageCode": "zu",
          "supportSource": true,
          "supportTarget": true
        }
       ]
    }
    

The list is sorted alphabetically by language code. This query returns ISO-639 language codes for supported languages. Some language codes also include a country code, like zh-CN or zh-TW. For example:
    
    
       {
          "languageCode": "zh-TW",
          "supportSource": true,
          "supportTarget": true
        },

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
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.Translate.V3/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-translate/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-translate/latest/Google/Cloud/Translate.html)

## List supported languages with target language name

### REST

Here is another example that returns the list of supported languages with the returned language names written in the specified target language. The returned list is sorted alphabetically according to the target language.

Before using any of the request data, make the following replacements: 

  * PROJECT_NUMBER_OR_ID: the numeric or alphanumeric ID of your Google Cloud project



HTTP method and URL: 
    
    
    GET https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/global/supportedLanguages?display_language_code=sq

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_NUMBER_OR_ID" \  
         "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/global/supportedLanguages?display_language_code=sq"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_NUMBER_OR_ID" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/global/supportedLanguages?display_language_code=sq" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "languages": [{
          "languageCode": "af",
          "displayName": "Afrikanisht",
          "supportSource": true,
          "supportTarget": true
        },
        {
          "languageCode": "am",
          "displayName": "Amarikisht",
          "supportSource": true,
          "supportTarget": true
        },
        {
          "languageCode": "en",
          "displayName": "Anglisht",
          "supportSource": true,
          "supportTarget": true
        },
        ...{
          "languageCode": "zu",
          "displayName": "Zulu",
          "supportSource": true,
          "supportTarget": true
        }
    
    	]
    }
    

In this case, the query returns the same language codes as above, along with `name` strings that give the names of the languages written in the target language. In this example, the language is Albanian (sq). 

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
    
    // getSupportedLanguagesForTarget gets a list of supported language codes with target language names.
    func getSupportedLanguagesForTarget(w io.Writer, projectID string, languageCode string) error {
    	// projectID := "my-project-id"
    	// languageCode := "is"
    
    	ctx := context.Background()
    	client, err := translate.[NewTranslationClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/apiv3.html#cloud_google_com_go_translate_apiv3_TranslationClient_NewTranslationClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewTranslationClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/apiv3.html#cloud_google_com_go_translate_apiv3_TranslationClient_Close)()
    
    	req := &translatepb.GetSupportedLanguagesRequest{
    		Parent:              fmt.Sprintf("projects/%s/locations/global", projectID),
    		DisplayLanguageCode: languageCode,
    	}
    
    	resp, err := client.GetSupportedLanguages(ctx, req)
    	if err != nil {
    		return fmt.Errorf("GetSupportedLanguages: %w", err)
    	}
    
    	// List language codes of supported languages
    	fmt.Fprintf(w, "Supported languages:\n")
    	for _, language := range resp.GetLanguages() {
    		fmt.Fprintf(w, "Language code: %v\n", language.GetLanguageCode())
    		fmt.Fprintf(w, "Display name: %v\n", language.GetDisplayName())
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
    
    public class GetSupportedLanguagesForTarget {
    
      public static void getSupportedLanguagesForTarget() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "YOUR-PROJECT-ID";
        // Supported Languages: https://cloud.google.com/translate/docs/languages
        String languageCode = "your-language-code";
        getSupportedLanguagesForTarget(projectId, languageCode);
      }
    
      // Listing supported languages with target language name
      public static void getSupportedLanguagesForTarget(String projectId, String languageCode)
          throws IOException {
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([TranslationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html) client = [TranslationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html).create()) {
          // Supported Locations: `global`, [glossary location], or [model location]
          // Glossaries must be hosted in `us-central1`
          // Custom Models must use the same location as your model. (us-central1)
          [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html) parent = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html).of(projectId, "global");
          [GetSupportedLanguagesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GetSupportedLanguagesRequest.html) request =
              [GetSupportedLanguagesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GetSupportedLanguagesRequest.html).newBuilder()
                  .setParent(parent.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html#com_google_cloud_translate_v3_LocationName_toString__)())
                  .[setDisplayLanguageCode](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GetSupportedLanguagesRequest.Builder.html#com_google_cloud_translate_v3_GetSupportedLanguagesRequest_Builder_setDisplayLanguageCode_java_lang_String_)(languageCode)
                  .build();
    
          [SupportedLanguages](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.SupportedLanguages.html) response = client.getSupportedLanguages(request);
    
          // List language codes of supported languages
          for ([SupportedLanguage](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.SupportedLanguage.html) language : response.[getLanguagesList](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.SupportedLanguages.html#com_google_cloud_translate_v3_SupportedLanguages_getLanguagesList__)()) {
            System.out.printf("Language Code: %s\n", language.getLanguageCode());
            System.out.printf("Display Name: %s\n", language.getDisplayName());
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
        displayLanguageCode: 'en',
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

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/translate/latest). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [translate](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.Client.html)
    
    
    def get_supported_languages_with_target(
        project_id: str = "YOUR_PROJECT_ID",
    ) -> translate.SupportedLanguages:
        """Listing supported languages with target language name.
    
        Args:
            project_id: Your Google Cloud project ID.
    
        Returns:
            Supported languages.
        """
        client = [translate](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.Client.html).[TranslationServiceClient](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3.services.translation_service.TranslationServiceClient.html)()
    
        location = "global"
    
        parent = f"projects/{project_id}/locations/{location}"
    
        # Supported language codes: https://cloud.google.com/translate/docs/languages
        response = [client](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.html).[get_supported_languages](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3.services.translation_service.TranslationServiceClient.html#google_cloud_translate_v3_services_translation_service_TranslationServiceClient_get_supported_languages)(
            display_language_code="is", parent=parent  # target language code
        )
        # List language codes of supported languages
        for language in response.languages:
            print(f"Language Code: {language.language_code}")
            print(f"Display Name: {language.display_name}")
    
        return response
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.Translate.V3/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-translate/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-translate/latest/Google/Cloud/Translate.html)

## Additional resources

  * For help on resolving common issues or errors, see the [Troubleshooting](https://docs.cloud.google.com/translate/troubleshooting) page.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
