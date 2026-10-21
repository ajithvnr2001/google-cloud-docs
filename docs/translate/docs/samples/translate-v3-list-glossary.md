---
url: https://docs.cloud.google.com/translate/docs/samples/translate-v3-list-glossary/
title: List glossaries (Advanced edition only) \u00a0|\u00a0 Cloud Translation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:24.682513+00:00
---

# List glossaries (Advanced edition only)  |  Cloud Translation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/translate/docs/samples/translate-v3-list-glossary/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Translation ](https://docs.cloud.google.com/translate/docs)
  * [ Samples ](https://docs.cloud.google.com/translate/docs/samples)



#  List glossaries (Advanced edition only) Stay organized with collections  Save and categorize content based on your preferences. 

List all the glossaries for a given project.

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
    	"google.golang.org/api/iterator"
    )
    
    // listGlossaries gets the specified glossary.
    func listGlossaries(w io.Writer, projectID string, location string) error {
    	// projectID := "my-project-id"
    	// location := "us-central1"
    
    	ctx := context.Background()
    	client, err := translate.[NewTranslationClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/apiv3.html#cloud_google_com_go_translate_apiv3_TranslationClient_NewTranslationClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewTranslationClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/apiv3.html#cloud_google_com_go_translate_apiv3_TranslationClient_Close)()
    
    	req := &translatepb.ListGlossariesRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/%s", projectID, location),
    	}
    
    	it := client.ListGlossaries(ctx, req)
    
    	// Iterate over all results
    	for {
    		glossary, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("ListGlossaries.Next: %w", err)
    		}
    		fmt.Fprintf(w, "Name: %v\n", glossary.GetName())
    		fmt.Fprintf(w, "Entry count: %v\n", glossary.GetEntryCount())
    		fmt.Fprintf(w, "Input URI: %v\n", glossary.GetInputConfig().GetGcsSource().GetInputUri())
    		for _, languageCode := range glossary.GetLanguageCodesSet().GetLanguageCodes() {
    			fmt.Fprintf(w, "Language code: %v\n", languageCode)
    		}
    		if languagePair := glossary.GetLanguagePair(); languagePair != nil {
    			fmt.Fprintf(w, "Language pair: %v, %v\n",
    				languagePair.GetSourceLanguageCode(), languagePair.GetTargetLanguageCode())
    		}
    	}
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.translate.v3.[Glossary](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.Glossary.html);
    import com.google.cloud.translate.v3.[ListGlossariesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.ListGlossariesRequest.html);
    import com.google.cloud.translate.v3.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html);
    import com.google.cloud.translate.v3.[TranslationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html);
    import java.io.IOException;
    
    public class ListGlossaries {
    
      public static void listGlossaries() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "YOUR-PROJECT-ID";
        listGlossaries(projectId);
      }
    
      // List all the glossaries in a specified location
      public static void listGlossaries(String projectId) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([TranslationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html) client = [TranslationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html).create()) {
          // Supported Locations: `global`, [glossary location], or [model location]
          // Glossaries must be hosted in `us-central1`
          // Custom Models must use the same location as your model. (us-central1)
          [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html) parent = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html).of(projectId, "us-central1");
          [ListGlossariesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.ListGlossariesRequest.html) request =
              [ListGlossariesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.ListGlossariesRequest.html).newBuilder().setParent(parent.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html#com_google_cloud_translate_v3_LocationName_toString__)()).build();
    
          for ([Glossary](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.Glossary.html) responseItem : client.listGlossaries(request).iterateAll()) {
            System.out.printf("Glossary name: %s\n", responseItem.getName());
            System.out.printf("Entry count: %s\n", responseItem.getEntryCount());
            System.out.printf(
                "Input URI: %s\n", responseItem.getInputConfig().getGcsSource().getInputUri());
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
    
    async function listGlossaries() {
      // Construct request
      const request = {
        parent: `projects/${projectId}/locations/${location}`,
      };
    
      // Run request
      const [response] = await translationClient.listGlossaries(request);
    
      for (const glossary of response) {
        console.log(`Name: ${glossary.name}`);
        console.log(`Entry count: ${glossary.entryCount}`);
        console.log(`Input uri: ${glossary.inputConfig.gcsSource.inputUri}`);
        for (const languageCode of glossary.languageCodesSet.languageCodes) {
          console.log(`Language code: ${languageCode}`);
        }
      }
    }
    
    listGlossaries();

### PHP

Before trying this sample, follow the PHP setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/translate/v2/translateclient). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Translate\V3\Client\TranslationServiceClient;
    use Google\Cloud\Translate\V3\ListGlossariesRequest;
    
    /**
     * @param string $projectId Your Google Cloud project ID.
     */
    function v3_list_glossary(string $projectId): void
    {
        $translationServiceClient = new TranslationServiceClient();
    
        $formattedParent = $translationServiceClient->locationName(
            $projectId,
            'us-central1'
        );
    
        try {
            // Iterate through all elements
            $request = (new ListGlossariesRequest())
                ->setParent($formattedParent);
            $pagedResponse = $translationServiceClient->listGlossaries($request);
            foreach ($pagedResponse->iterateAllElements() as $responseItem) {
                printf('Glossary name: %s' . PHP_EOL, $responseItem->getName());
                printf('Entry count: %s' . PHP_EOL, $responseItem->getEntryCount());
                printf(
                    'Input URI: %s' . PHP_EOL,
                    $responseItem->getInputConfig()
                        ->getGcsSource()
                        ->getInputUri()
                );
            }
        } finally {
            $translationServiceClient->close();
        }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/translate/latest). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import translate
    
    
    def list_glossaries(project_id: str = "YOUR_PROJECT_ID") -> translate.Glossary:
        """List Glossaries.
    
        Args:
            project_id: The GCP project ID.
    
        Returns:
            The glossary.
        """
        client = translate.TranslationServiceClient()
    
        location = "us-central1"
    
        parent = f"projects/{project_id}/locations/{location}"
    
        # Iterate over all results
        for glossary in client.list_glossaries(parent=parent):
            print(f"Name: {glossary.name}")
            print(f"Entry count: {glossary.entry_count}")
            print(f"Input uri: {glossary.input_config.gcs_source.input_uri}")
    
            # Note: You can create a glossary using one of two modes:
            # language_code_set or language_pair. When listing the information for
            # a glossary, you can only get information for the mode you used
            # when creating the glossary.
            for language_code in glossary.language_codes_set.language_codes:
                print(f"Language code: {language_code}")
    
        return glossary
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudtranslation). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
